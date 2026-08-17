#!/usr/bin/env python3
"""Renderiza o relatório de usabilidade em PDF com Cairo/Pango."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

import cairo

from create_usability_report import build_document  # noqa: E402


NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
}
TEXT_STYLE = f"{{{NS['text']}}}style-name"
TABLE_STYLE = f"{{{NS['table']}}}style-name"

A4_W, A4_H = 595.276, 841.89
LEFT, RIGHT = 62.36, 62.36
TOP, BOTTOM = 57.0, 53.0
CONTENT_W = A4_W - LEFT - RIGHT
CM = 72.0 / 2.54


@dataclass
class TextLayout:
    lines: list[str]
    width: float
    font: str
    size: float
    bold: bool
    align: str
    line_height: float


class Renderer:
    def __init__(self, output: Path) -> None:
        self.output = output
        self.surface = cairo.PDFSurface(str(output), A4_W, A4_H)
        self.surface.set_metadata(cairo.PDF_METADATA_TITLE, "Relatório de Resultados da Avaliação de Usabilidade")
        self.surface.set_metadata(cairo.PDF_METADATA_AUTHOR, "Equipe 06 - Cariri Cultural")
        self.ctx = cairo.Context(self.surface)
        self.page_no = 1
        self.y = TOP

    def set_font(self, font: str, size: float, bold: bool) -> None:
        self.ctx.select_font_face(font, cairo.FONT_SLANT_NORMAL,
                                  cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
        self.ctx.set_font_size(size)

    def layout(self, text: str, width: float, font: str, size: float,
               bold: bool = False, align: str = "left", justify: bool = False) -> tuple[TextLayout, float]:
        del justify
        self.set_font(font, size, bold)
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if self.ctx.text_extents(candidate).x_advance <= max(1.0, width):
                current = candidate
            else:
                if current:
                    lines.append(current)
                    current = word
                else:
                    lines.append(word)
        if current or not lines:
            lines.append(current)
        line_height = size * 1.18
        result = TextLayout(lines, width, font, size, bold, align, line_height)
        return result, len(lines) * line_height

    def draw_layout(self, layout: TextLayout, x: float, y: float,
                    color: tuple[float, float, float] = (0, 0, 0)) -> None:
        self.ctx.set_source_rgb(*color)
        self.set_font(layout.font, layout.size, layout.bold)
        for index, line in enumerate(layout.lines):
            advance = self.ctx.text_extents(line).x_advance
            if layout.align == "center":
                line_x = x + (layout.width - advance) / 2
            elif layout.align == "right":
                line_x = x + layout.width - advance
            else:
                line_x = x
            self.ctx.move_to(line_x, y + layout.size + index * layout.line_height)
            self.ctx.show_text(line)

    def render_cover(self) -> None:
        title1, _ = self.layout("RELATÓRIO DE RESULTADOS", CONTENT_W, "Times New Roman", 22, True, "center")
        title2, _ = self.layout("DA AVALIAÇÃO DE USABILIDADE", CONTENT_W, "Times New Roman", 22, True, "center")
        self.draw_layout(title1, LEFT, 307)
        self.draw_layout(title2, LEFT, 346)
        meta = [
            "Projeto: Cariri Cultural",
            "Protótipo / versão avaliada: Protótipo de alta fidelidade - Entrega 05",
            "Data da avaliação: 12/08/26 - 17/08/26   Responsável(is): Equipe 06",
        ]
        for i, line in enumerate(meta):
            layout, _ = self.layout(line, CONTENT_W, "Times New Roman", 10, False, "center")
            self.draw_layout(layout, LEFT, 400 + i * 20)

    def start_page(self) -> None:
        self.y = TOP
        header, _ = self.layout("RELATÓRIO DE AVALIAÇÃO DE USABILIDADE", CONTENT_W, "Arial", 8, False, "center")
        self.draw_layout(header, LEFT, 23)

    def finish_page(self) -> None:
        footer, _ = self.layout(f"Página {self.page_no}", CONTENT_W, "Arial", 8, False, "center")
        self.draw_layout(footer, LEFT, A4_H - 31)

    def new_page(self) -> None:
        if self.page_no > 1:
            self.finish_page()
        self.surface.show_page()
        self.page_no += 1
        self.start_page()

    def ensure(self, height: float) -> None:
        if self.y + height > A4_H - BOTTOM:
            self.new_page()

    def paragraph(self, text: str, style: str) -> None:
        specs = {
            "Body": ("Times New Roman", 10.5, False, "left", True, 6.0, 2.0),
            "Heading1": ("Times New Roman", 14.0, True, "left", False, 9.0, 5.0),
            "Heading2": ("Times New Roman", 12.0, True, "left", False, 8.0, 4.0),
        }
        if style not in specs or not text:
            return
        font, size, bold, align, justify, before, after = specs[style]
        layout, height = self.layout(text, CONTENT_W, font, size, bold, align, justify)
        self.ensure(before + height + after)
        self.y += before
        self.draw_layout(layout, LEFT, self.y)
        self.y += height + after

    @staticmethod
    def cell_text(cell: ET.Element) -> tuple[str, str]:
        para = cell.find("text:p", NS)
        if para is None:
            return "", "TableText"
        return ''.join(para.itertext()), para.attrib.get(TEXT_STYLE, "TableText")

    @staticmethod
    def column_width(col: ET.Element) -> float:
        style = col.attrib.get(TABLE_STYLE, "Col2_0")
        value = style[3:].replace("_", ".")
        return float(value) * CM

    def table(self, element: ET.Element) -> None:
        cols = [self.column_width(col) for col in element.findall("table:table-column", NS)]
        total = sum(cols)
        x0 = LEFT + (CONTENT_W - total) / 2
        header_container = element.find("table:table-header-rows", NS)
        header_row = header_container.find("table:table-row", NS) if header_container is not None else None
        data_rows = element.findall("table:table-row", NS)

        def prepared(row: ET.Element, is_header: bool) -> tuple[list[tuple[TextLayout, float, tuple[float, float, float]]], float]:
            layouts: list[tuple[TextLayout, float, tuple[float, float, float]]] = []
            max_h = 0.0
            for cell, width in zip(row.findall("table:table-cell", NS), cols):
                text, style = self.cell_text(cell)
                if is_header:
                    font, size, bold, align, color = "Times New Roman", 8.4, True, "center", (1, 1, 1)
                elif style == "TableSmall":
                    font, size, bold, align, color = "Times New Roman", 7.4, False, "left", (0, 0, 0)
                elif style == "TableCenter":
                    font, size, bold, align, color = "Times New Roman", 8.4, False, "center", (0, 0, 0)
                else:
                    font, size, bold, align, color = "Times New Roman", 8.4, False, "left", (0, 0, 0)
                layout, height = self.layout(text, width - 7.0, font, size, bold, align)
                layouts.append((layout, height, color))
                max_h = max(max_h, height)
            return layouts, max(19.0 if is_header else 17.0, max_h + 7.0)

        def draw_row(row: ET.Element, is_header: bool) -> float:
            layouts, row_h = prepared(row, is_header)
            x = x0
            for width, (layout, text_h, color) in zip(cols, layouts):
                self.ctx.set_source_rgb(0.50, 0.50, 0.50) if is_header else self.ctx.set_source_rgb(1, 1, 1)
                self.ctx.rectangle(x, self.y, width, row_h)
                self.ctx.fill_preserve()
                self.ctx.set_source_rgb(0, 0, 0)
                self.ctx.set_line_width(0.55)
                self.ctx.stroke()
                self.draw_layout(layout, x + 3.5, self.y + (row_h - text_h) / 2, color)
                x += width
            self.y += row_h
            return row_h

        if header_row is None:
            return
        _, header_h = prepared(header_row, True)
        self.ensure(header_h + 20)
        draw_row(header_row, True)
        for row in data_rows:
            _, row_h = prepared(row, False)
            if self.y + row_h > A4_H - BOTTOM:
                self.new_page()
                draw_row(header_row, True)
            draw_row(row, False)
        self.y += 7.0

    def render(self) -> None:
        self.render_cover()
        root = ET.fromstring(build_document())
        office_text = root.find("office:body/office:text", NS)
        assert office_text is not None
        started = False
        for child in office_text:
            if child.tag == f"{{{NS['text']}}}p":
                style = child.attrib.get(TEXT_STYLE, "Body")
                if style == "PageBreak":
                    if not started:
                        started = True
                        self.new_page()
                    else:
                        self.new_page()
                    continue
                if not started:
                    continue
                self.paragraph(''.join(child.itertext()), style)
            elif child.tag == f"{{{NS['table']}}}table" and started:
                self.table(child)
        self.finish_page()
        self.surface.finish()


def main() -> None:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/Relatorio-Avaliacao-Usabilidade-Cariri-Cultural-Preenchido.pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    Renderer(output).render()
    print(output.resolve())


if __name__ == "__main__":
    main()
