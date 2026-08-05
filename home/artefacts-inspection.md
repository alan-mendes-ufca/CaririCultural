

*Consolidação: registro de inconsistências, correções redigidas, status dos entregáveis e histórico de alterações*


**Escopo:** requisitos funcionais, requisitos não funcionais, regras de negócio, histórias de usuário, casos de uso descritivos, diagrama de casos de uso, BPMN, mapa de jornada/usuário, Service Blueprint, storytelling, storyboarding e matriz de rastreabilidade. Protótipos e itens derivados exclusivamente deles (Épicos 9 a 13) ficaram fora do escopo, por solicitação do responsável pela revisão.

> [!NOTE]
>
> **Numeração de casos de uso anterior à renumeração.** Este relatório foi redigido quando os casos de uso iam de UC-01 a UC-27. Depois dele, os casos foram granularizados e renumerados para **UC-001 a UC-089**, em correspondência 1:1 com as histórias de usuário. As referências `UC-NN` (dois dígitos) abaixo continuam válidas para os PDFs auditados e **não foram alteradas**, para preservar o registro do que foi efetivamente encontrado. Para localizar o caso correspondente na versão atual, use o de-para abaixo; a fonte corrente é a [matriz de rastreabilidade](home/traceability-matrix) e os [casos de uso descritivos](home/user-cases/descriptive-use-cases).
>
> | Antes | Agora | | Antes | Agora |
> |---|---|---|---|---|
> | UC-01 | UC-001, UC-002, UC-003 | | UC-15 | UC-041, UC-086 |
> | UC-02 | UC-004, UC-005, UC-077, UC-078 | | UC-16 | UC-039, UC-087 |
> | UC-03 | UC-006 a UC-020, UC-079 | | UC-17 | UC-040 |
> | UC-04 | UC-014, UC-080 | | UC-18 | UC-042 |
> | UC-05 | UC-021, UC-040 | | UC-19 | UC-043 |
> | UC-06 | UC-030 a UC-037 | | UC-20 | UC-044 |
> | UC-07 | UC-022 | | UC-21 | UC-045 |
> | UC-08 | UC-023, UC-024, UC-025, UC-082 | | UC-22 | UC-046 |
> | UC-09 | UC-026, UC-083 | | UC-23 | UC-047 a UC-050 |
> | UC-10 | UC-027 | | UC-24 | UC-051 a UC-054 |
> | UC-11 | UC-028 | | UC-25 | UC-055 a UC-058 |
> | UC-12 | UC-029, UC-084 | | UC-26 | UC-088 |
> | UC-13 | UC-038 | | UC-27 | UC-089 |
> | UC-14 | UC-085 | | | |
>
> As correções propostas na seção 3.7 já foram aplicadas na versão atual: a busca por proximidade cita RF-006A em [UC-078](home/user-cases/descriptive-use-cases#UC-078), e a sinalização de dado incorreto cita RF-22A em [UC-088](home/user-cases/descriptive-use-cases#UC-088). Note que o identificador real do requisito é `RF-22A`, e não `RF-022A` como grafado na seção 3.7.

---

## 1. Resumo executivo



Foram identificadas 12 inconsistências entre os artefatos analisados: erros de rastreabilidade, duplicidade de arquivos e de histórias de usuário, contradições diretas entre o BPMN e as regras de negócio/casos de uso, lacunas de requisitos autodeclaradas nos próprios documentos, e desalinhamento de escopo entre o Service Blueprint e o Mapa de Jornada. Para cada inconsistência foi redigido o texto de correção ("De → Para").

---

## 2. Registro de inconsistências

### INC-01 — hta.pdf
- **Elemento/Seção:** Tarefas 5 a 10 — "Requisitos relacionados"
- **Tipo:** Rastreabilidade incorreta
- **Artefatos relacionados:** requisitos_funcionais.pdf
- **Descrição:** IDs de RF citados não correspondem ao conteúdo real das tarefas. Tarefa 5 cita RF-013 (deveria ser RF-016); Tarefa 6 cita RF-014/015 (deveria ser RF-017/018); Tarefa 7 cita RF-016/017 (deveria ser RF-021/022); Tarefa 8 cita RF-021 a 024 (deveria ser RF-023 a 026); Tarefa 9 cita RF-019 (deveria ser RF-027 a 029); Tarefa 10 cita RF-028 a 031 (deveria ser RF-030 a 033).
- **Confiança:** Alta

### INC-02 — mapa_de_usuario.pdf
- **Elemento/Seção:** Documento inteiro
- **Tipo:** Duplicidade / artefato ausente
- **Artefatos relacionados:** mapa_de_jornada.pdf
- **Descrição:** Conteúdo byte-a-byte idêntico a mapa_de_jornada.pdf. Não existe um Mapa de Usuário (personas PATHY/CHATHY) distinto no repositório.
- **Confiança:** Alta

### INC-03 — diagrama_de_caso_de_uso.pdf
- **Elemento/Seção:** Documento inteiro
- **Tipo:** Duplicidade de arquivo
- **Artefatos relacionados:** diagrama-de-casos-de-uso.pdf
- **Descrição:** Mesmo arquivo enviado duas vezes com nomes diferentes (conteúdo idêntico, 5 páginas).
- **Confiança:** Alta

### INC-04 — BPMN-Cariri-Cultural.png
- **Elemento/Seção:** Raia Usuário → ramo Enquete
- **Tipo:** Contradição entre artefatos
- **Artefatos relacionados:** regras_de_negocios.pdf (RN-063); casos_de_usosdescritivos.pdf (UC-13); diagrama_de_caso_de_uso.pdf
- **Descrição:** Nó rotulado "Criar Enquete Compartilhável sem Autenticação" contradiz RN-063 e UC-13 (ambos exigem usuário autenticado para criar; só a votação é anônima). O diagrama de casos de uso reforça isso: mostra UC-13 ligado por `<<include>>` a "Autenticar usuário".
- **Confiança:** Alta

### INC-05 — BPMN-Cariri-Cultural.png
- **Elemento/Seção:** Raia Usuário → ramos Organização e Compartilhar
- **Tipo:** Omissão de fluxo
- **Artefatos relacionados:** regras_de_negocios.pdf (RN-045, RN-047); casos_de_usosdescritivos.pdf (UC-10, UC-11, UC-15)
- **Descrição:** Os ramos "Criar Listas/Marcar Visitados/Checklists" e "Gerar Link Público de Listas Favoritas" não passam por nenhum gate de autenticação, diferente do ramo Avaliação. RN-045/047 e UC-10/11/15 exigem usuário autenticado e proprietário.
- **Confiança:** Alta

### INC-06 — BPMN-Cariri-Cultural.png
- **Elemento/Seção:** Raias Administrador da Plataforma e Administrador Local
- **Tipo:** Escopo em desacordo com priorização
- **Artefatos relacionados:** requisitos_funcionais.pdf (Épico 8); casos_de_usosdescritivos.pdf; matriz_de_rastreaabilidades.pdf
- **Descrição:** O fluxo administrativo completo (Épico 8) é modelado como já validado, mas requisitos_funcionais.pdf marca esse épico "Won't have" e "sem procedência identificada em stakeholders"; casos_de_usosdescritivos.pdf remove UC-18 a UC-25 da linha de base pelo mesmo motivo.
- **Confiança:** Alta

### INC-07 — casos_de_usosdescritivos.pdf
- **Elemento/Seção:** UC-02 — fluxos A3/A4 (busca por proximidade)
- **Tipo:** Rastreabilidade incompleta
- **Artefatos relacionados:** requisitos_funcionais.pdf (Épico 1 e Épico 2)
- **Descrição:** UC-02 introduz busca por proximidade geográfica (ator "Serviço de geolocalização/mapas") e atribui a RF-011, que na verdade descreve apenas a localização exibida na página de detalhes de um local. Nenhum RF do Épico 1 cobre busca por proximidade — confirmado também na matriz de rastreabilidade, onde as linhas de HU-004/HU-005 não citam RF-011 nem equivalente.
- **Confiança:** Alta

### INC-08 — casos_de_usosdescritivos.pdf
- **Elemento/Seção:** UC-26 — campo RF
- **Tipo:** Requisito ausente (autodeclarado)
- **Artefatos relacionados:** requisitos_funcionais.pdf; blueprint.pdf; mapa_de_jornada.pdf
- **Descrição:** O próprio documento afirma: "RF-022 cobre a contribuição comunitária; o requisito funcional específico de tratamento da sinalização deve ser formalizado na próxima revisão da matriz." Confirmado: não há linha correspondente na matriz de rastreabilidade.
- **Confiança:** Alta

### INC-09 — regras_de_negocios.pdf / hus.pdf
- **Elemento/Seção:** Épico 8 (RN-066 a RN-076, HU-042 a HU-058)
- **Tipo:** Investimento em escopo não validado
- **Artefatos relacionados:** requisitos_funcionais.pdf (aviso do Épico 8)
- **Descrição:** RN e HU do Épico 8 foram detalhados por completo apesar do aviso em requisitos_funcionais.pdf de que esse escopo não tem procedência validada em stakeholders — nenhum aviso equivalente aparece em RN ou HU.
- **Confiança:** Alta

### INC-10 — hus.pdf
- **Elemento/Seção:** HU-017, HU-018 (Épico 2)
- **Tipo:** Duplicidade de conteúdo
- **Artefatos relacionados:** hus.pdf (HU-035, HU-036); requisitos_funcionais.pdf (RF-035, RF-036); matriz_de_rastreaabilidades.pdf
- **Descrição:** HU-017 e HU-018 têm texto idêntico a HU-035 e HU-036 (Épico 6). Os RFs que essas histórias descrevem (RF-035, RF-036) pertencem ao Épico 6, não ao Épico 2 — confirmado na matriz, onde as linhas de HU-017/HU-018 já apontam para RF-035/RF-036, duplicando exatamente as linhas de HU-035/HU-036.
- **Confiança:** Alta

### INC-11 — mapa_de_jornada.pdf
- **Elemento/Seção:** Seção 9 — Rastreabilidade resumida, Etapa 7 (Pós-visita)
- **Tipo:** Afirmação desatualizada sobre outro artefato
- **Artefatos relacionados:** diagrama_de_caso_de_uso.pdf
- **Descrição:** O texto afirma que "o diagrama atual não representa avaliações, histórico, mídia da comunidade ou compartilhamento". Porém o diagrama contém as bolhas "Consultar avaliações e mídia comunitária" e "Avaliar, publicar mídia, compartilhar e votar", além de "UC-11 Registrar visitas" e "UC-15 Compartilhar lista" nas páginas detalhadas.
- **Confiança:** Média — leitura de diagrama via OCR; recomenda-se confirmação visual antes de reescrever o texto

### INC-12 — blueprint.pdf
- **Elemento/Seção:** Tabela "Blueprint da jornada principal"
- **Tipo:** Escopo incompleto frente a outro artefato
- **Artefatos relacionados:** mapa_de_jornada.pdf
- **Descrição:** O Blueprint modela apenas 5 etapas (Descobrir, Acessar e explorar, Buscar e filtrar, Avaliar e escolher, Planejar). Não cobre "Deslocamento e experiência" nem "Pós-visita", que são as Etapas 6 e 7 do Mapa de Jornada e envolvem RF-021, RF-022, RF-028, RF-040 e RF-041.
- **Confiança:** Alta

---

## 3. Correções redigidas por artefato

Texto pronto para colar nos artefatos-fonte. Nenhuma alteração foi aplicada aos arquivos originais nesta rodada.

### 3.1 hta.pdf — referências de RF

```
Tarefa 5. Participar de eventos culturais
  De:   Requisitos relacionados: RF-013
  Para: Requisitos relacionados: RF-016

Tarefa 6. Obter informações complementares
  De:   Requisitos relacionados: RF-014, RF-015
  Para: Requisitos relacionados: RF-017, RF-018

Tarefa 7. Utilizar recursos colaborativos
  De:   Requisitos relacionados: RF-016, RF-017
  Para: Requisitos relacionados: RF-021, RF-022

Tarefa 8. Receber recomendações personalizadas
  De:   Requisitos relacionados: RF-021, RF-022, RF-023, RF-024
  Para: Requisitos relacionados: RF-023, RF-024, RF-025, RF-026

Tarefa 9. Organizar experiências pessoais
  De:   Requisitos relacionados: RF-019
  Para: Requisitos relacionados: RF-027, RF-028, RF-029

Tarefa 10. Utilizar assistente virtual
  De:   Requisitos relacionados: RF-028, RF-029, RF-030, RF-031
  Para: Requisitos relacionados: RF-030, RF-031, RF-032, RF-033
```

### 3.2 hus.pdf — remoção de duplicidade

- Remover do Épico 2: HU-017 ("Receber links de redes sociais") e HU-018 ("Receber imagens do local") — texto idêntico a HU-035 e HU-036 do Épico 6.
- Manter os IDs HU-017/HU-018 marcados como "removidos — ver HU-035/HU-036" em vez de renumerar, para não quebrar referências já existentes em outros artefatos.

### 3.3 mapa_de_usuario.pdf — duplicidade

- Substituir o conteúdo (hoje idêntico a mapa_de_jornada.pdf) pelo Mapa de Usuário/personas (PATHY e CHATHY, citadas em mapa_de_jornada.pdf como evidência consultada), ou remover o arquivo do repositório.

### 3.4 diagrama_de_caso_de_uso.pdf — duplicidade

- Manter apenas um dos dois arquivos (diagrama_de_caso_de_uso.pdf ou diagrama-de-casos-de-uso.pdf) e remover o outro.

### 3.5 BPMN-Cariri-Cultural.png — três correções

```
De:   "Criar Enquete Compartilhável sem Autenticação"
Para: "Usuário Autenticado?" (gate) → "Criar Enquete Compartilhável"
      — votação continua sem autenticação
```

- Adicionar o gate "Usuário Autenticado?" antes de "Criar Listas, Marcar Visitados ou Usar Checklists" e antes de "Gerar Link Público de Listas Favoritas", igual ao já usado no ramo Avaliação.
- Adicionar nota nas raias Administrador da Plataforma e Administrador Local: "Fluxo administrativo (Épico 8) ainda sem procedência validada em stakeholders — não representa funcionalidade aprovada", até decisão formal sobre o status do Épico 8.

### 3.6 requisitos_funcionais.pdf — dois requisitos novos

```
RF-006A — O sistema deve permitir buscar e ordenar locais e eventos por
proximidade da localização atual do usuário (mediante consentimento) ou
de uma origem informada manualmente. Prioridade sugerida: Should have.

RF-022A — O sistema deve permitir que o usuário sinalize um dado
incorreto em um local ou evento, registrando campo afetado, valor
observado e evidência opcional, mantendo protocolo rastreável até a
resolução. Prioridade sugerida: Must have.
```

### 3.7 casos_de_usosdescritivos.pdf — correção de referências

```
UC-02, campo RF — De:   RF-004, RF-005, RF-006, RF-011
UC-02, campo RF — Para: RF-004, RF-005, RF-006, RF-006A, RF-011

UC-26, campo RF — De:   "RF-022 cobre a contribuição comunitária;
                          requisito específico a formalizar"
UC-26, campo RF — Para: RF-022, RF-022A
```

### 3.8 blueprint.pdf — etapas faltantes

- Adicionar coluna "6. Deslocamento e experiência" — evidências: localização/rota, status ao vivo, conteúdo cultural, assistente contextual (RF-011, RF-016 a RF-018, RF-030 a RF-033).
- Adicionar coluna "7. Pós-visita" — evidências: avaliações, mídia comunitária, histórico, compartilhamento (RF-021, RF-022, RF-028, RF-040, RF-041).
- Conteúdo detalhado já existe em mapa_de_jornada.pdf, Etapas 6 e 7 — pode ser adaptado de lá.

### 3.9 matriz_de_rastreaabilidades.pdf — ajustes

- Remover linhas HU-017 e HU-018 (duplicam HU-035/HU-036, ambas já apontando para RF-035/RF-036).
- Adicionar linha: HU-004A → RF-006A, RN-009/RN-010.
- Adicionar linha: HU-022A → RF-022A, RN-037/RN-038.
- Linhas do Épico 8 (marcadas "esc adm"): manter como estão até decisão formal sobre o status do épico.

---

## 4. Histórico de alterações (changelog)

Cada linha representa uma alteração redigida nesta rodada e ainda não aplicada ao artefato-fonte.

| Artefato | Situação atual ("De") | Alteração proposta ("Para") | Status |
|---|---|---|---|
| hta.pdf | RF-013/014/015/016/017/019/021/022/028/029 citados incorretamente nas tarefas 5–10 | RF-016, RF-017/018, RF-021/022, RF-023 a 026, RF-027 a 029, RF-030 a 033 (ver 3.1) | Proposto |
| hus.pdf | HU-017 e HU-018 duplicadas no Épico 2 | Remoção de HU-017/HU-018; manter apenas HU-035/HU-036 no Épico 6 | Proposto |
| mapa_de_usuario.pdf | Idêntico a mapa_de_jornada.pdf | Substituir por conteúdo de Mapa de Usuário (personas) ou remover arquivo duplicado | Proposto |
| diagrama_de_caso_de_uso.pdf | Duplicata de diagrama-de-casos-de-uso.pdf | Manter apenas um dos dois arquivos no repositório | Proposto |
| BPMN-Cariri-Cultural.png | Nó "Criar Enquete sem Autenticação"; sem gate de autenticação em Organização/Compartilhar; Épico 8 sem ressalva de escopo | Adicionar gate de autenticação nos 3 pontos (ver 3.5) | Proposto |
| requisitos_funcionais.pdf | Sem RF para busca por proximidade e para sinalização de dado incorreto | Adicionar RF-006A e RF-022A (texto completo em 3.6) | Proposto |
| casos_de_usosdescritivos.pdf | UC-02 cita RF-011 indevidamente; UC-26 sem RF associado | UC-02 → RF-006A; UC-26 → RF-022A | Proposto |
| blueprint.pdf | Tabela de jornada cobre só 5 de 7 etapas | Adicionar etapas "Deslocamento e experiência" e "Pós-visita" (ver 3.8) | Proposto |
| mapa_de_jornada.pdf | Afirmação sobre cobertura do diagrama na Etapa 7 possivelmente desatualizada | Revisar frase após confirmação visual do diagrama (confiança média) | Pendente de verificação |
| matriz_de_rastreaabilidades.pdf | Linhas HU-017/HU-018 duplicadas; sem linha para RF-006A/RF-022A | Remover HU-017/HU-018; adicionar HU-004A→RF-006A e HU-022A→RF-022A (ver 3.9) | Proposto |

---



