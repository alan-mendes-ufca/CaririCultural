#!/usr/bin/env python3
"""Gera a versão DOCX editável do relatório consolidado de usabilidade."""

from __future__ import annotations

import datetime as dt
import html
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from create_usability_report import build_document


NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
}
TEXT_STYLE = f"{{{NS['text']}}}style-name"
TABLE_STYLE = f"{{{NS['table']}}}style-name"


def x(value: object) -> str:
    return html.escape(str(value), quote=True)


def run(text: str, bold: bool = False, color: str | None = None,
        font: str | None = None, size_half_points: int | None = None) -> str:
    props: list[str] = []
    if bold:
        props.append("<w:b/><w:bCs/>")
    if color:
        props.append(f'<w:color w:val="{color}"/>')
    if font:
        props.append(f'<w:rFonts w:ascii="{x(font)}" w:hAnsi="{x(font)}" w:cs="{x(font)}"/>')
    if size_half_points:
        props.append(f'<w:sz w:val="{size_half_points}"/><w:szCs w:val="{size_half_points}"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    preserve = ' xml:space="preserve"' if text.startswith(" ") or text.endswith(" ") else ""
    return f"<w:r>{rpr}<w:t{preserve}>{x(text)}</w:t></w:r>"


def paragraph(text: str = "", style: str = "Body", page_break: bool = False) -> str:
    if page_break:
        return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    return f'<w:p><w:pPr><w:pStyle w:val="{x(style)}"/></w:pPr>{run(text)}</w:p>'


def column_dxa(style_name: str) -> int:
    cm = float(style_name[3:].replace("_", "."))
    return round(cm / 2.54 * 1440)


def cell_text(cell: ET.Element) -> tuple[str, str]:
    p = cell.find("text:p", NS)
    if p is None:
        return "", "TableText"
    return ''.join(p.itertext()), p.attrib.get(TEXT_STYLE, "TableText")


def table_xml(element: ET.Element) -> str:
    widths = [column_dxa(col.attrib.get(TABLE_STYLE, "Col2_0"))
              for col in element.findall("table:table-column", NS)]
    total = sum(widths)
    parts = [
        "<w:tbl>",
        "<w:tblPr>",
        f'<w:tblW w:w="{total}" w:type="dxa"/>',
        '<w:jc w:val="center"/><w:tblLayout w:type="fixed"/>',
        '<w:tblBorders><w:top w:val="single" w:sz="6" w:color="000000"/>'
        '<w:left w:val="single" w:sz="6" w:color="000000"/>'
        '<w:bottom w:val="single" w:sz="6" w:color="000000"/>'
        '<w:right w:val="single" w:sz="6" w:color="000000"/>'
        '<w:insideH w:val="single" w:sz="5" w:color="000000"/>'
        '<w:insideV w:val="single" w:sz="5" w:color="000000"/></w:tblBorders>',
        '<w:tblCellMar><w:top w:w="70" w:type="dxa"/><w:left w:w="75" w:type="dxa"/>'
        '<w:bottom w:w="70" w:type="dxa"/><w:right w:w="75" w:type="dxa"/></w:tblCellMar>',
        "</w:tblPr><w:tblGrid>",
    ]
    parts.extend(f'<w:gridCol w:w="{width}"/>' for width in widths)
    parts.append("</w:tblGrid>")

    header_group = element.find("table:table-header-rows", NS)
    rows: list[tuple[ET.Element, bool]] = []
    if header_group is not None:
        header = header_group.find("table:table-row", NS)
        if header is not None:
            rows.append((header, True))
    rows.extend((row, False) for row in element.findall("table:table-row", NS))

    for row, is_header in rows:
        row_props = '<w:trPr><w:cantSplit/>' + ('<w:tblHeader/>' if is_header else '') + '</w:trPr>'
        parts.append(f"<w:tr>{row_props}")
        for idx, cell in enumerate(row.findall("table:table-cell", NS)):
            width = widths[idx] if idx < len(widths) else round(total / max(1, len(widths)))
            text, style = cell_text(cell)
            if is_header:
                style = "TableHeader"
            shade = '<w:shd w:val="clear" w:color="auto" w:fill="808080"/>' if is_header else ''
            parts.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}'
                '<w:vAlign w:val="center"/></w:tcPr>'
            )
            parts.append(paragraph(text, style))
            parts.append("</w:tc>")
        parts.append("</w:tr>")
    parts.append("</w:tbl>")
    return ''.join(parts)


def document_body() -> str:
    root = ET.fromstring(build_document())
    office_text = root.find("office:body/office:text", NS)
    if office_text is None:
        raise RuntimeError("Corpo do relatório não encontrado")
    body: list[str] = []
    first_break = True
    for child in office_text:
        if child.tag == f"{{{NS['text']}}}p":
            style = child.attrib.get(TEXT_STYLE, "Body")
            text = ''.join(child.itertext())
            if style == "FirstPage":
                continue
            if style == "PageBreak":
                body.append(paragraph(page_break=True))
                first_break = False
                continue
            if first_break and style == "CoverSpacer":
                body.append(paragraph("", "CoverSpacer"))
            else:
                body.append(paragraph(text, style))
        elif child.tag == f"{{{NS['table']}}}table":
            body.append(table_xml(child))
    body.append(
        '<w:sectPr><w:headerReference w:type="default" r:id="rId3"/>'
        '<w:footerReference w:type="default" r:id="rId4"/><w:titlePg/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="964" w:right="1247" w:bottom="964" w:left="1247" '
        'w:header="425" w:footer="425" w:gutter="0"/>'
        '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>'
    )
    return ''.join(body)


def styles_xml() -> str:
    def style(style_id: str, name: str, size: int, *, bold: bool = False, align: str | None = None,
              before: int = 0, after: int = 0, line: int | None = None, keep: bool = False,
              font: str = "Times New Roman", color: str | None = None) -> str:
        ppr = [f'<w:spacing w:before="{before}" w:after="{after}"' + (f' w:line="{line}" w:lineRule="auto"' if line else '') + '/>']
        if align:
            ppr.append(f'<w:jc w:val="{align}"/>')
        if keep:
            ppr.append('<w:keepNext/><w:keepLines/>')
        rpr = [f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>',
               f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>']
        if bold:
            rpr.append('<w:b/><w:bCs/>')
        if color:
            rpr.append(f'<w:color w:val="{color}"/>')
        return (f'<w:style w:type="paragraph" w:styleId="{style_id}"><w:name w:val="{name}"/>'
                f'<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr>{"".join(ppr)}</w:pPr>'
                f'<w:rPr>{"".join(rpr)}</w:rPr></w:style>')

    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
 <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
 <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="80" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr></w:style>
 {style("Body", "Corpo", 21, align="both", after=80, line=276)}
 {style("Heading1", "Título 1", 28, bold=True, before=120, after=70, keep=True)}
 {style("Heading2", "Título 2", 24, bold=True, before=110, after=60, keep=True)}
 {style("CoverTitle", "Título da capa", 44, bold=True, align="center", after=100)}
 {style("CoverMeta", "Metadados da capa", 20, align="center", after=35)}
 {style("CoverSpacer", "Espaço da capa", 20, after=340)}
 {style("CoverGap", "Intervalo da capa", 20, after=280)}
 {style("TableText", "Texto de tabela", 17, after=0, line=210)}
 {style("TableSmall", "Texto pequeno de tabela", 15, after=0, line=188)}
 {style("TableCenter", "Texto central de tabela", 17, align="center", after=0, line=210)}
 {style("TableHeader", "Cabeçalho de tabela", 17, bold=True, align="center", after=0, line=200, color="FFFFFF")}
 {style("Header", "Cabeçalho", 16, align="center", after=0, font="Arial")}
 {style("Footer", "Rodapé", 16, align="center", after=0, font="Arial")}
</w:styles>'''


def document_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
 <w:body>{document_body()}</w:body>
</w:document>'''


def header_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">{paragraph("RELATÓRIO DE AVALIAÇÃO DE USABILIDADE", "Header")}</w:hdr>'''


def footer_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
 <w:p><w:pPr><w:pStyle w:val="Footer"/></w:pPr>
  <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">Página </w:t></w:r>
  <w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>
 </w:p>
</w:ftr>'''


def write_docx(output: Path) -> None:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    files = {
        "[Content_Types].xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="xml" ContentType="application/xml"/>
 <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
 <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
 <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
 <Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
 <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
 <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
 <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
 <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>''',
        "_rels/.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
 <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
 <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''',
        "word/_rels/document.xml.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
 <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable" Target="fontTable.xml"/>
 <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
 <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
 <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>''',
        "word/document.xml": document_xml(),
        "word/styles.xml": styles_xml(),
        "word/header1.xml": header_xml(),
        "word/footer1.xml": footer_xml(),
        "word/settings.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:updateFields w:val="true"/><w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat></w:settings>''',
        "word/fontTable.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:fonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:font w:name="Times New Roman"><w:family w:val="roman"/><w:pitch w:val="variable"/></w:font><w:font w:name="Arial"><w:family w:val="swiss"/><w:pitch w:val="variable"/></w:font></w:fonts>''',
        "docProps/core.xml": f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Relatório de Resultados da Avaliação de Usabilidade</dc:title><dc:subject>Cariri Cultural</dc:subject><dc:creator>Equipe 06</dc:creator><cp:lastModifiedBy>Equipe 06</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>''',
        "docProps/app.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office Word</Application><AppVersion>16.0000</AppVersion><Company>Equipe 06</Company></Properties>''',
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(name, content.encode("utf-8"))


def main() -> None:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/Relatorio_Avaliacao_Usabilidade_Cariri_Cultural_Preenchido.docx")
    write_docx(output)
    print(output.resolve())


if __name__ == "__main__":
    main()
