#!/usr/bin/env python3
"""Gera o relatório consolidado de avaliação de usabilidade em FODT."""

from __future__ import annotations

import html
import sys
from pathlib import Path


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def p(text: str = "", style: str = "Body") -> str:
    return f'<text:p text:style-name="{style}">{esc(text)}</text:p>'


def page_break() -> str:
    return '<text:p text:style-name="PageBreak"/>'


def table(headers: list[str], rows: list[list[str]], widths: list[float],
          aligns: list[str] | None = None, font_style: str = "TableText") -> str:
    aligns = aligns or ["left"] * len(headers)
    out = ['<table:table table:style-name="ReportTable">']
    for width in widths:
        out.append(f'<table:table-column table:style-name="Col{str(width).replace(".", "_")}"/>')
    out.append('<table:table-header-rows><table:table-row table:style-name="HeaderRow">')
    for header in headers:
        out.append('<table:table-cell table:style-name="HeaderCell" office:value-type="string">')
        out.append(p(header, "TableHeader"))
        out.append('</table:table-cell>')
    out.append('</table:table-row></table:table-header-rows>')
    for row in rows:
        out.append('<table:table-row table:style-name="DataRow">')
        for idx, value in enumerate(row):
            cell_style = "DataCellCenter" if aligns[idx] == "center" else "DataCell"
            para_style = "TableCenter" if aligns[idx] == "center" else font_style
            out.append(f'<table:table-cell table:style-name="{cell_style}" office:value-type="string">')
            out.append(p(value, para_style))
            out.append('</table:table-cell>')
        out.append('</table:table-row>')
    out.append('</table:table>')
    return ''.join(out)


def build_document() -> str:
    body: list[str] = []

    # Capa
    body.append(p("", "FirstPage"))
    body.extend(p("", "CoverSpacer") for _ in range(10))
    body.append(p("RELATÓRIO DE RESULTADOS", "CoverTitle"))
    body.append(p("DA AVALIAÇÃO DE USABILIDADE", "CoverTitle"))
    body.append(p("", "CoverGap"))
    body.append(p("Projeto: Cariri Cultural", "CoverMeta"))
    body.append(p("Protótipo / versão avaliada: Protótipo de alta fidelidade - Entrega 05", "CoverMeta"))
    body.append(p("Data da avaliação: 12/08/26 - 17/08/26   Responsável(is): Equipe 06", "CoverMeta"))

    # Página 2
    body.append(page_break())
    body.append(p("1. Objetivo do relatório", "Heading1"))
    body.append(p(
        "Este relatório registra e consolida os resultados da avaliação de usabilidade do protótipo de alta "
        "fidelidade do Cariri Cultural. Os achados são relacionados às tarefas executadas, às métricas de "
        "avaliação e às técnicas de observação adotadas, permitindo agrupar ocorrências equivalentes, "
        "classificar sua severidade, propor melhorias e orientar a revisão do protótipo."
    ))
    body.append(p("2. Identificação da avaliação realizada", "Heading1"))
    body.append(table(
        ["Campo", "Registro"],
        [
            ["Quantidade de participantes", "10"],
            ["Perfis contemplados", "Moradora de longa data, turista e novo morador"],
            ["Tarefas avaliadas", "05 tarefas (T-001 a T-005)"],
            ["Técnicas utilizadas", "Observação, Walkthrough e Think Aloud"],
            ["Instrumento pós-teste", "Perguntas abertas de avaliação da experiência de uso"],
            ["Métricas registradas", "Tempo; sucessos; satisfação; suporte; desvios/retrabalho; erros de interação"],
            ["Período / local", "12 a 17/08/2026; UFCA, residência, trabalho e sessões remotas"],
            ["Versão utilizada", "Protótipo de alta fidelidade - Entrega 05"],
        ], [8.0, 8.0]
    ))
    body.append(p("3. Resultados da execução das tarefas", "Heading1"))
    body.append(p(
        "Os resultados consideram 46 execuções registradas. A T-001 possui evidência em seis sessões; "
        "as demais tarefas foram observadas nas dez sessões. Os tempos são medianas das duas sessões "
        "com cronometragem completa."
    ))
    body.append(table(
        ["ID", "Tarefa", "Resultado", "Tempo (s)", "Suporte", "Desvios", "Erros"],
        [
            ["T-001", "Consultar perfil", "6 concluídas com dificuldade", "86", "1", "2", "0"],
            ["T-002", "Buscar lugar", "5 sem e 5 com dificuldade", "14", "2", "5", "1"],
            ["T-003", "Planejar visita", "1 sem e 9 com dificuldade", "89", "2", "9", "3"],
            ["T-004", "Usar assistente", "5 sem; 4 com dificuldade; 1 não", "90", "1", "5", "2"],
            ["T-005", "Acessar avaliações", "4 sem e 6 com dificuldade", "43", "0", "6", "0"],
        ], [1.15, 2.2, 4.2, 1.7, 1.6, 1.6, 1.55],
        ["center", "left", "left", "center", "center", "center", "center"]
    ))

    # Página 3
    body.append(page_break())
    body.append(p("3.1. Síntese das métricas de avaliação", "Heading1"))
    body.append(table(
        ["Métrica", "Forma de consolidação", "Resultado consolidado"],
        [
            ["Tempo de execução", "Mediana entre início e conclusão nas sessões cronometradas.",
             "T-001: 86 s; T-002: 14 s; T-003: 89 s; T-004: 90 s; T-005: 43 s."],
            ["Mapeamento de sucessos", "Classificação por execução: sem dificuldade, com dificuldade ou não concluída.",
             "15 sem dificuldade; 30 com dificuldade; 1 não concluída. Conclusão global: 45/46 (97,8%)."],
            ["Satisfação", "Síntese de clareza, organização, conforto e utilidade percebida.",
             "Predominantemente positiva. Houve compreensão do propósito, elogios à navegação, ao visual e às informações práticas."],
            ["Pedidos de suporte", "Ajuda direta necessária para descobrir ou compreender o próximo passo.",
             "6 ocorrências: T-001 (1), T-002 (2), T-003 (2), T-004 (1), T-005 (0)."],
            ["Desvio e retrabalho", "Passos adicionais, retornos, tentativa alternativa ou navegação fora do fluxo.",
             "27 ocorrências: maior concentração em planejamento/favoritos (9) e avaliações (6)."],
            ["Erros de interação", "Ações equivocadas ou falhas de resposta que alteraram o fluxo.",
             "6 ocorrências: T-002 (1), T-003 (3) e T-004 (2); sem erro registrado em T-001 e T-005."],
        ], [4.0, 5.4, 6.6]
    ))
    body.append(p("Leitura geral das métricas", "Heading2"))
    body.append(p(
        "A taxa de conclusão é alta, porém 65,2% das execuções foram concluídas com alguma dificuldade. "
        "O resultado indica boa eficácia do fluxo principal, acompanhada de perdas de eficiência e "
        "descoberta sobretudo em ações secundárias."
    ))

    # Página 4
    body.append(page_break())
    body.append(p("3.2. Síntese do pós-teste", "Heading1"))
    body.append(p(
        "As respostas pós-teste complementam os registros observacionais e evidenciam percepções, "
        "dúvidas e sugestões manifestadas ao final ou durante a navegação."
    ))
    body.append(table(
        ["Q.", "Pergunta", "Síntese das respostas"],
        [
            ["1", "O que achou da experiência geral?", "Experiência considerada intuitiva, útil, moderna e coerente com turismo e cultura regional."],
            ["2", "Entendeu facilmente o objetivo?", "Sim. O conjunto explorar, planejar, informar e interagir com a comunidade foi reconhecido."],
            ["3", "Funcionalidades mais fáceis?", "Exploração, detalhes dos locais, filtros quando visíveis, avaliações e comunidade."],
            ["4", "Houve confusão ou dificuldade?", "Sim: perfil, busca vazia, filtros, sugestões do assistente, checklist, favoritos e comentário."],
            ["5", "Informações foram claras e úteis?", "Preço, horário, segurança e acessibilidade foram valorizados; pediram restrições e dados mais consistentes."],
            ["6", "O assistente ajudou?", "A proposta foi valorizada, mas perguntas livres, profundidade, atualização, contraste e histórico limitaram o uso."],
            ["7", "Sentiu falta de informação ou recurso?", "Mais locais, regras do local, personalização, respostas com exemplos, feedback e ações mais visíveis."],
            ["8", "O que mudaria no protótipo?", "Reforçar hierarquia e contraste; melhorar busca/filtros; padronizar favoritos; destacar comentários; revisar assistente e checklist."],
        ], [1.0, 5.0, 10.0], ["center", "left", "left"]
    ))

    problems = [
        ["P-01", "T-001 / cadastro", "Cadastro e perfil", "Seleção e dados do perfil não ficam claros ou confirmados.", "Dúvida, perfil não refletido e contraste insuficiente.", "Sucesso, suporte", "5", "3"],
        ["P-02", "T-002 / busca", "Busca e catálogo", "Busca vazia sem recuperação e catálogo pouco representativo.", "Rolagem orientada, local ausente e percepção de pouca variedade.", "Sucesso, desvios", "4", "3"],
        ["P-03", "T-002 / filtros", "Explorar", "Filtros pouco descobertos; rótulo e estado selecionado ambíguos.", "Indicação do avaliador e interpretação invertida de “Público”.", "Suporte, erros", "3", "3"],
        ["P-04", "T-004 / assistente", "Assistente", "Sugestões pouco visíveis; respostas livres limitadas e sem saída contextual.", "Falha em perguntas livres; resposta rasa/desatualizada; histórico perdido.", "Sucesso, erros", "6", "3"],
        ["P-05", "T-003 / planejar", "Roteiro e favoritos", "Nomenclatura, checklist, favoritos e feedback não sustentam o modelo mental.", "Retornos, dúvidas sobre checklist e favoritos escondidos/inconsistentes.", "Desvios, suporte", "8", "3"],
        ["P-06", "T-005 / avaliações", "Ficha e comunidade", "Avaliar/comentar é pouco evidente e fica distante do início da ficha.", "Participantes consultam, mas não descobrem ou confirmam a contribuição.", "Sucesso, desvios", "6", "3"],
        ["P-07", "Fluxos móveis", "Hierarquia visual", "Conteúdo denso, ícones compactos e contraste/hierarquia insuficientes.", "Rolagem extensa, hesitação e esforço de leitura em smartphone.", "Tempo, satisfação", "4", "2"],
        ["P-08", "Global", "Conteúdo e confiança", "Dados duplicados, datados ou incoerentes e mídia sem procedência clara.", "Conteúdo de teste reduziu variedade, atualidade e credibilidade percebida.", "Satisfação", "4", "2"],
    ]

    # Páginas 5 e 6
    for index, chunk in enumerate((problems[:4], problems[4:])):
        body.append(page_break())
        title = "4. Lista consolidada dos problemas de usabilidade encontrados"
        if index:
            title += " (continuação)"
        body.append(p(title, "Heading1"))
        if index == 0:
            body.append(p(
                "As 54 ocorrências registradas foram agrupadas por causa e efeito equivalentes. A severidade "
                "considera impacto, recorrência e capacidade de recuperação do usuário."
            ))
        body.append(table(
            ["ID", "Tarefa / fluxo", "Tela / elemento", "Problema observado", "Evidência", "Métrica", "Part.", "Sev."],
            chunk,
            [1.0, 2.0, 2.1, 3.35, 3.55, 1.7, 1.0, 0.8],
            ["center", "left", "left", "left", "left", "left", "center", "center"],
            "TableSmall"
        ))

    severity_rows = [
        ["P-01 Cadastro e perfil", "3 - Alto", "Afeta personalização e confirmação da identidade; recorrente.", "Alta"],
        ["P-02 Busca e catálogo", "3 - Alto", "Pode encerrar a descoberta sem alternativa de recuperação.", "Alta"],
        ["P-03 Filtros", "3 - Alto", "Recurso não descoberto ou interpretado de modo contrário.", "Alta"],
        ["P-04 Assistente", "3 - Alto", "Falha na intenção espontânea e restringe a única rota útil.", "Alta"],
        ["P-05 Planejamento/favoritos", "3 - Alto", "Oito participantes tiveram dúvida, desvio ou baixa descoberta.", "Alta"],
        ["P-06 Avaliar/comentar", "3 - Alto", "Impede ou dificulta contribuição, função central da comunidade.", "Alta"],
        ["P-07 Hierarquia móvel", "2 - Menor", "Aumenta esforço e tempo, mas permite recuperação.", "Média-baixa"],
        ["P-08 Conteúdo e confiança", "2 - Menor", "Reduz confiança e qualidade percebida sem bloquear a tarefa.", "Média-baixa"],
    ]

    # Página 7
    body.append(page_break())
    body.append(p("5. Classificação da severidade dos problemas", "Heading1"))
    body.append(p(
        "A escala aplicada combina impacto na tarefa, frequência entre participantes e dificuldade de recuperação."
    ))
    body.append(table(
        ["Nível", "Classificação", "Critério de interpretação", "Prioridade"],
        [
            ["1", "Cosmético", "Incômodo visual leve; não prejudica a conclusão.", "Baixa"],
            ["2", "Baixo / menor", "Causa hesitação, esforço adicional ou pequeno atraso.", "Média-baixa"],
            ["3", "Alto / grave", "Prejudica significativamente, causa recorrência ou exige contorno.", "Alta"],
            ["4", "Crítico", "Impede função essencial ou causa perda relevante.", "Imediata"],
        ], [2.0, 3.4, 7.2, 3.4], ["center", "left", "left", "left"]
    ))
    body.append(p("5.1. Registro consolidado por severidade", "Heading1"))
    body.append(table(
        ["Problema / grupo", "Severidade", "Justificativa", "Prioridade"],
        severity_rows[:4], [4.2, 3.0, 5.8, 3.0], ["left", "center", "left", "center"]
    ))

    # Página 8
    body.append(page_break())
    body.append(p("5.1. Registro consolidado por severidade (continuação)", "Heading1"))
    body.append(table(
        ["Problema / grupo", "Severidade", "Justificativa", "Prioridade"],
        severity_rows[4:], [4.2, 3.0, 5.8, 3.0], ["left", "center", "left", "center"]
    ))
    body.append(p("Distribuição consolidada", "Heading2"))
    body.append(p(
        "Foram identificados 8 grupos únicos: 6 de severidade alta, 2 de severidade menor, "
        "nenhum cosmético isolado e nenhum crítico."
    ))

    improvements = [
        ["P-01", "Reformular cadastro; explicar perfis e exibir no perfil os dados selecionados.", "Restabelece confirmação e personalização.", "Menos suporte e dúvidas.", "Alta", "Planejada"],
        ["P-02", "Criar estado vazio com alternativas, sugestão de locais e solicitação de cadastro.", "Evita beco sem saída e amplia descoberta.", "Mais sucesso na busca.", "Alta", "Planejada"],
        ["P-03", "Elevar filtros, renomear “Público” e tornar estado ativo inequívoco.", "Melhora descoberta e interpretação.", "Menos erros e desvios.", "Alta", "Planejada"],
        ["P-04", "Destacar sugestões; responder texto livre; aprofundar conteúdo; preservar histórico e encaminhar a telas úteis.", "Atende à intenção real do usuário.", "Maior conclusão e satisfação.", "Alta", "Planejada"],
        ["P-05", "Unificar Planejar/Roteiros; explicar checklist; padronizar favoritos e manter feedback persistente.", "Alinha terminologia, ação e confirmação.", "Menos retrabalho.", "Alta", "Planejada"],
        ["P-06", "Exibir CTA Avaliar/Comentar próximo ao resumo e confirmar envio/estado.", "Aumenta descoberta da contribuição.", "Mais avaliações concluídas.", "Alta", "Planejada"],
        ["P-07", "Rever hierarquia, contraste, tamanho de alvo e posição dos CTAs em telas móveis.", "Reduz carga visual e rolagem.", "Menor tempo e hesitação.", "Média", "Planejada"],
        ["P-08", "Revisar base, datas, duplicidades, localização e procedência das imagens.", "Reforça consistência e confiança.", "Maior credibilidade.", "Média", "Planejada"],
    ]

    # Páginas 9 e 10
    for index, chunk in enumerate((improvements[:4], improvements[4:])):
        body.append(page_break())
        title = "6. Propostas de melhoria"
        if index:
            title += " (continuação)"
        body.append(p(title, "Heading1"))
        if index == 0:
            body.append(p(
                "Cada ação proposta responde diretamente à causa observada e define o resultado de usabilidade esperado."
            ))
        body.append(table(
            ["Problema", "Proposta de melhoria", "Justificativa", "Resultado esperado", "Prioridade", "Situação"],
            chunk, [1.2, 4.6, 3.3, 3.2, 1.8, 1.9],
            ["center", "left", "left", "left", "center", "center"], "TableSmall"
        ))
        if index == 1:
            body.append(p("7. Versão revisada do protótipo", "Heading1"))
            body.append(p(
                "A próxima versão deverá incorporar prioritariamente P-01 a P-06 e ser submetida a uma rodada "
                "curta de validação com foco em descoberta, compreensão e feedback."
            ))
            body.append(table(
                ["Campo", "Registro"],
                [
                    ["Identificação da nova versão", "Protótipo de alta fidelidade - Entrega 06 (planejada)"],
                    ["Data do planejamento da revisão", "17/08/2026"],
                    ["Localização de referência", "Repositório g6.wiki e arquivo do protótipo da equipe no Figma"],
                ], [6.0, 10.0]
            ))

    # Página 11
    body.append(page_break())
    body.append(p("8. Registro das alterações implementadas", "Heading1"))
    body.append(p(
        "No fechamento desta avaliação, as alterações estão especificadas e aguardam aplicação no protótipo. "
        "O quadro preserva a rastreabilidade para atualização após a revisão."
    ))
    body.append(table(
        ["Tela / fluxo", "Problema(s)", "Alteração especificada", "Motivo", "Status"],
        [
            ["Cadastro e perfil", "P-01", "Perfis explicados e dados confirmados.", "Clareza e personalização.", "Planejada"],
            ["Busca / Explorar", "P-02, P-03", "Estado vazio, filtros visíveis e rótulos revistos.", "Descoberta e recuperação.", "Planejada"],
            ["Assistente", "P-04", "Sugestões destacadas, texto livre, histórico e rotas contextuais.", "Conclusão da intenção.", "Planejada"],
            ["Roteiros / favoritos", "P-05", "Termos unificados, checklist explicado e favorito padronizado.", "Menos desvios.", "Planejada"],
            ["Avaliações", "P-06", "CTA visível e confirmação de envio.", "Contribuição clara.", "Planejada"],
            ["Layout móvel", "P-07", "Contraste, hierarquia e alvos de toque revistos.", "Legibilidade e eficiência.", "Planejada"],
            ["Conteúdo", "P-08", "Base, datas, localização e imagens revisadas.", "Confiança e consistência.", "Planejada"],
        ], [3.0, 2.0, 4.6, 4.0, 2.4], ["left", "center", "left", "left", "center"], "TableSmall"
    ))
    body.append(p("8.1. Evidências da versão revisada", "Heading1"))
    body.append(table(
        ["Evidência", "Tela / fluxo", "Problema(s)", "Descrição da revisão"],
        [["Validação pendente", "Todos os fluxos priorizados", "P-01 a P-08", "Capturas e links deverão ser anexados após a aplicação das correções na Entrega 06."]],
        [3.0, 4.0, 2.5, 6.5], ["center", "left", "center", "left"]
    ))

    # Página 12
    body.append(page_break())
    body.append(p("9. Síntese dos resultados", "Heading1"))
    body.append(table(
        ["Indicador", "Resultado"],
        [
            ["Total de ocorrências registradas", "54"],
            ["Total de problemas únicos após agrupamento", "8"],
            ["Problemas cosméticos (1)", "0"],
            ["Problemas menores (2)", "2"],
            ["Problemas graves (3)", "6"],
            ["Problemas críticos (4)", "0"],
            ["Melhorias propostas", "8"],
            ["Melhorias implementadas na versão revisada", "0; implementação planejada para a Entrega 06"],
            ["Tarefas concluídas sem dificuldade", "15"],
            ["Tarefas concluídas com dificuldade", "30"],
            ["Tarefas não concluídas", "1"],
        ], [8.0, 8.0]
    ))
    body.append(p("10. Conclusão", "Heading1"))
    body.append(p(
        "O protótipo demonstrou boa eficácia: 45 das 46 execuções foram concluídas e todos os participantes "
        "compreenderam a proposta do Cariri Cultural. A navegação geral, a ficha dos locais, o visual e a "
        "utilidade das informações receberam avaliação positiva. Entretanto, 30 execuções exigiram esforço "
        "adicional e uma não foi concluída, com concentração de desvios em planejamento/favoritos, avaliações "
        "e assistente. Recomenda-se priorizar os seis grupos graves, aplicar as oito melhorias e realizar nova "
        "validação dirigida antes de encerrar a revisão."
    ))
    body.append(p("11. Responsáveis pelo registro e revisão", "Heading1"))
    body.append(table(
        ["Nome", "Data / assinatura"],
        [
            ["Cícero Jesus", "17/08/2026"],
            ["Alan Mendes", "17/08/2026"],
            ["Antônio Pereira", "17/08/2026"],
            ["Diogo Gomes", "17/08/2026"],
            ["Randerson do Nascimento", "17/08/2026"],
        ], [8.0, 8.0]
    ))

    widths = sorted({1.0, 1.15, 1.2, 1.55, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.4,
                     2.5, 3.0, 3.2, 3.3, 3.35, 3.4, 3.55, 4.0, 4.2, 4.6, 5.0,
                     5.4, 5.8, 6.0, 6.5, 6.6, 7.2, 8.0, 10.0})
    column_styles = ''.join(
        f'<style:style style:name="Col{str(width).replace(".", "_")}" style:family="table-column">'
        f'<style:table-column-properties style:column-width="{width}cm"/>'
        f'</style:style>' for width in widths
    )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
 xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
 xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
 xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
 xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 office:version="1.2" office:mimetype="application/vnd.oasis.opendocument.text">
 <office:font-face-decls>
  <style:font-face style:name="Times New Roman" svg:font-family="'Times New Roman'" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"/>
  <style:font-face style:name="Arial" svg:font-family="Arial" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"/>
 </office:font-face-decls>
 <office:styles>
  <style:default-style style:family="paragraph"><style:paragraph-properties fo:orphans="2" fo:widows="2"/><style:text-properties style:font-name="Times New Roman" fo:font-size="10.5pt"/></style:default-style>
  <style:style style:name="Body" style:family="paragraph"><style:paragraph-properties fo:text-align="justify" fo:line-height="115%" fo:margin-bottom="1.6mm"/></style:style>
  <style:style style:name="Heading1" style:family="paragraph"><style:paragraph-properties fo:margin-top="2.2mm" fo:margin-bottom="1.6mm" fo:keep-with-next="always"/><style:text-properties style:font-name="Times New Roman" fo:font-size="14pt" fo:font-weight="bold"/></style:style>
  <style:style style:name="Heading2" style:family="paragraph"><style:paragraph-properties fo:margin-top="2mm" fo:margin-bottom="1.2mm" fo:keep-with-next="always"/><style:text-properties style:font-name="Times New Roman" fo:font-size="12pt" fo:font-weight="bold"/></style:style>
  <style:style style:name="CoverTitle" style:family="paragraph"><style:paragraph-properties fo:text-align="center" fo:margin-bottom="2mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="22pt" fo:font-weight="bold"/></style:style>
  <style:style style:name="CoverMeta" style:family="paragraph"><style:paragraph-properties fo:text-align="center" fo:margin-bottom="1.2mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="10pt"/></style:style>
  <style:style style:name="CoverSpacer" style:family="paragraph"><style:paragraph-properties fo:margin-bottom="6mm"/></style:style>
  <style:style style:name="CoverGap" style:family="paragraph"><style:paragraph-properties fo:margin-bottom="5mm"/></style:style>
  <style:style style:name="TableText" style:family="paragraph"><style:paragraph-properties fo:line-height="103%" fo:margin="0mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="8.4pt"/></style:style>
  <style:style style:name="TableSmall" style:family="paragraph"><style:paragraph-properties fo:line-height="100%" fo:margin="0mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="7.4pt"/></style:style>
  <style:style style:name="TableCenter" style:family="paragraph"><style:paragraph-properties fo:text-align="center" fo:line-height="103%" fo:margin="0mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="8.4pt"/></style:style>
  <style:style style:name="TableHeader" style:family="paragraph"><style:paragraph-properties fo:text-align="center" fo:line-height="100%" fo:margin="0mm"/><style:text-properties style:font-name="Times New Roman" fo:font-size="8.4pt" fo:font-weight="bold" fo:color="#ffffff"/></style:style>
  <style:style style:name="Header" style:family="paragraph"><style:paragraph-properties fo:text-align="center"/><style:text-properties style:font-name="Arial" fo:font-size="8pt"/></style:style>
  <style:style style:name="Footer" style:family="paragraph"><style:paragraph-properties fo:text-align="center"/><style:text-properties style:font-name="Arial" fo:font-size="8pt"/></style:style>
 </office:styles>
 <office:automatic-styles>
  <style:page-layout style:name="FirstLayout"><style:page-layout-properties fo:page-width="21cm" fo:page-height="29.7cm" style:print-orientation="portrait" fo:margin-top="2cm" fo:margin-bottom="2cm" fo:margin-left="2.2cm" fo:margin-right="2.2cm"/></style:page-layout>
  <style:page-layout style:name="StandardLayout"><style:page-layout-properties fo:page-width="21cm" fo:page-height="29.7cm" style:print-orientation="portrait" fo:margin-top="1.7cm" fo:margin-bottom="1.7cm" fo:margin-left="2.2cm" fo:margin-right="2.2cm"/><style:header-style><style:header-footer-properties fo:min-height="0.7cm" fo:margin-bottom="0.4cm"/></style:header-style><style:footer-style><style:header-footer-properties fo:min-height="0.7cm" fo:margin-top="0.4cm"/></style:footer-style></style:page-layout>
  <style:style style:name="FirstPage" style:family="paragraph" style:master-page-name="First"/>
  <style:style style:name="PageBreak" style:family="paragraph" style:master-page-name="Standard"><style:paragraph-properties fo:break-before="page"/></style:style>
  <style:style style:name="ReportTable" style:family="table"><style:table-properties table:align="margins" style:width="16cm"/></style:style>
  <style:style style:name="HeaderCell" style:family="table-cell"><style:table-cell-properties fo:background-color="#808080" fo:border="0.6pt solid #000000" fo:padding="1.2mm" style:vertical-align="middle"/></style:style>
  <style:style style:name="DataCell" style:family="table-cell"><style:table-cell-properties fo:border="0.45pt solid #000000" fo:padding="1.15mm" style:vertical-align="middle"/></style:style>
  <style:style style:name="DataCellCenter" style:family="table-cell"><style:table-cell-properties fo:border="0.45pt solid #000000" fo:padding="1.15mm" style:vertical-align="middle"/></style:style>
  <style:style style:name="HeaderRow" style:family="table-row"><style:table-row-properties fo:keep-together="always" style:min-row-height="7mm"/></style:style>
  <style:style style:name="DataRow" style:family="table-row"><style:table-row-properties fo:keep-together="always"/></style:style>
  {column_styles}
 </office:automatic-styles>
 <office:master-styles>
  <style:master-page style:name="First" style:page-layout-name="FirstLayout"/>
  <style:master-page style:name="Standard" style:page-layout-name="StandardLayout">
   <style:header>{p("RELATÓRIO DE AVALIAÇÃO DE USABILIDADE", "Header")}</style:header>
   <style:footer><text:p text:style-name="Footer">Página <text:page-number text:select-page="current">1</text:page-number></text:p></style:footer>
  </style:master-page>
 </office:master-styles>
 <office:body><office:text>{''.join(body)}</office:text></office:body>
</office:document>'''


def main() -> None:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "Relatorio-Avaliacao-Usabilidade-Cariri-Cultural-Preenchido.fodt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_document(), encoding="utf-8")
    print(output.resolve())


if __name__ == "__main__":
    main()
