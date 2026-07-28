---
title: Casos de Uso Descritivos
---
## Leitura de prioridade e procedência

- **Must have**: necessário na linha de base atual.
- **Should have**: importante, mas pode entrar depois do núcleo essencial.
- **Could have**: desejável se houver capacidade.
- **Won't have nesta entrega**: fora da linha de base atual; não significa baixa importância futura. Os itens nessa situação ficam somente no backlog.

| Casos de uso | Prioridade de entrega | Evidência principal |
|--------------|-----------------------|---------------------|
| UC-01 a UC-05 | Must have | [Entrevistas](home/interviews/relatorio-entrevistas), [questionário](home/survey), [RFs priorizados](home/priorizated-fr) e [telas Início/Explorar/Detalhes/Comunidade](prototype-interaction-workflows). |
| UC-06 | Must have | [Entrevistas](home/interviews/relatorio-entrevistas), [RF-030/RF-031/RF-033](home/traceability-matrix#TM-UC-06) e [tela Assistente](prototype-interaction-workflows). |
| UC-07 | Should have | [Entrevistas](home/interviews/relatorio-entrevistas), [RF-022](home/traceability-matrix#TM-UC-07) e [tela Comunidade](prototype-interaction-workflows). |
| UC-08 | Should have | [RF-023 a RF-025](home/traceability-matrix#TM-UC-08). |
| UC-09, UC-10 e UC-12 | Must have | [Entrevistas](home/interviews/relatorio-entrevistas), [RF-026](home/traceability-matrix#TM-UC-09)/[RF-027](home/traceability-matrix#TM-UC-10)/[RF-029](home/traceability-matrix#TM-UC-12) e [tela Planejamento de visita](prototype-interaction-workflows). |
| UC-11, UC-15 e UC-16 | Should have | [Entrevistas](home/interviews/relatorio-entrevistas) e [RF-028](home/traceability-matrix#TM-UC-11)/[RF-039](home/traceability-matrix#TM-UC-16)/[RF-041](home/traceability-matrix#TM-UC-15). |
| UC-13, UC-14 e UC-17 | Could have | [Entrevistas](home/interviews/relatorio-entrevistas), [RF-038](home/traceability-matrix#TM-UC-13)/[RF-038](home/traceability-matrix#TM-UC-14)/[RF-040](home/traceability-matrix#TM-UC-17) e [tela Comunidade](prototype-interaction-workflows). |
| UC-26 | Must have | [Relatos de Sarah](home/interviews/interview-Sarah-Linhars), [Iago](home/interviews/interview-Iago-Conserva) e [Kamily](home/interviews/interview-Kamily-Rocha); [questionário](home/survey); [RN-037/RN-038](home/traceability-matrix#TM-UC-26). |

> A priorização acima está compatível com a priorização de requisitos.

---

<a id="UC-01"></a>
## UC-01 — Explorar catálogo regional

| Campo | Especificação |
|-------|---------------|
| Objetivo | Descobrir locais, eventos e experiências regionais, inclusive populares e pouco divulgados. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Catálogo disponível. |
| Pós-condições | Itens compatíveis são exibidos e o visitante pode abrir um resultado. |
| RF | [RF-001, RF-002, RF-003](home/traceability-matrix#TM-UC-01). |
| RN | [RN-001, RN-002, RN-006, RN-007, RN-008, RN-010, RN-022, RN-077](home/traceability-matrix#TM-UC-01). |

**Fluxo principal**

1. O visitante acessa a exploração.
2. [O sistema apresenta o catálogo regional unificado.](home/traceability-matrix#TM-UC-01)
3. O visitante seleciona uma lista, categoria ou item.
4. [O sistema ordena a lista pelo critério documentado](home/traceability-matrix#TM-UC-01) e [identifica conteúdo patrocinado.](home/traceability-matrix#TM-UC-01)
5. [O sistema apresenta o resultado e permite consultar seus detalhes.](home/traceability-matrix#TM-UC-01)

**Fluxos alternativos**

- A1 — O visitante escolhe “populares”; [o sistema ordena por visitação/interações, avaliações e recência.](home/traceability-matrix#TM-UC-01)
- A2 — O visitante escolhe “pouco divulgados”; [o sistema aplica o critério de avaliação e visitas.](home/business-rules#RN-077)

**Fluxos de exceção**

- E1 — Catálogo indisponível: [o sistema informa a falha sem expor detalhes técnicos e orienta nova tentativa.](home/business-rules#RN-010)
- E2 — Registro duplicado detectado: [o sistema não publica ambos até a consolidação.](home/traceability-matrix#TM-UC-01)

---

<a id="UC-02"></a>
## UC-02 — Pesquisar e filtrar locais e eventos

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar conteúdo por termo, nome, categoria, cidade, perfil de público e proximidade da localização escolhida. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de geolocalização/mapas, somente quando o visitante escolher proximidade. |
| Pré-condições | Registros pesquisáveis contêm os dados mínimos; localização do dispositivo depende de consentimento. |
| Pós-condições | Resultados filtrados ou alternativas de busca são apresentados; quando aplicável, distância e referência de origem ficam explícitas. |
| RF | [RF-004, RF-005, RF-006, RF-011](home/traceability-matrix#TM-UC-02), [RF-077](home/traceability-matrix#TM-HU-077), [RF-078](home/traceability-matrix#TM-HU-078). |
| RN | [RN-003, RN-004, RN-005, RN-009, RN-010](home/traceability-matrix#TM-UC-02), [RN-078](home/traceability-matrix#TM-HU-077), [RN-079, RN-080](home/traceability-matrix#TM-HU-078). |

**Fluxo principal**

1. O visitante informa termo e/ou filtros, ou escolhe descobrir o que está próximo de uma localização.
2. [O sistema valida formato, domínio, cardinalidade e taxonomia dos valores informados.](home/traceability-matrix#TM-HU-077)
3. [O sistema pesquisa nome, palavras-chave, categoria e cidade.](home/traceability-matrix#TM-UC-02)
4. [O sistema exibe os resultados e os filtros aplicados.](home/traceability-matrix#TM-UC-02)
5. O visitante seleciona um resultado.

**Fluxos alternativos**

- A1 — Sem resultado exato: [o sistema sugere correções, categorias próximas ou outra cidade.](home/traceability-matrix#TM-UC-02)
- A2 — O visitante altera ou remove filtros e [a pesquisa é refeita.](home/traceability-matrix#TM-UC-02)
- A3 — O visitante escolhe “Mais próximos”; [o sistema solicita consentimento, obtém a localização atual, calcula as distâncias e ordena os resultados elegíveis.](home/traceability-matrix#TM-HU-078)
- A4 — O visitante não quer usar a localização atual; informa um bairro, cidade ou ponto de referência e [o sistema usa essa origem para a busca por proximidade.](home/traceability-matrix#TM-HU-078)

**Fluxos de exceção**

- E1 — Valor de filtro inválido: [o sistema oferece apenas valores aprovados.](home/traceability-matrix#TM-HU-077)
- E2 — Falha de consulta: [o sistema informa a situação e uma próxima ação.](home/traceability-matrix#TM-UC-02)
- E3 — Permissão de localização negada ou posição indisponível: [a pesquisa continua por cidade e o sistema oferece a origem manual, sem bloquear o catálogo.](home/traceability-matrix#TM-HU-078)
- E4 — Distância não calculável: [o item pode permanecer no resultado, mas sem distância estimada e sem ser indevidamente priorizado como próximo.](home/traceability-matrix#TM-HU-078)

---

<a id="UC-03"></a>
## UC-03 — Consultar detalhes de local

| Campo | Especificação |
|-------|---------------|
| Objetivo | Apoiar a decisão e o planejamento da visita com informações completas e confiáveis. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de mapas/transportes. |
| Pré-condições | Local publicado e visível. |
| Pós-condições | Detalhes são visualizados; eventual canal externo pode ser aberto. |
| RF | [RF-007 a RF-015, RF-017 a RF-020, RF-035, RF-036](home/traceability-matrix#TM-UC-03), [RF-079](home/traceability-matrix#TM-HU-079). |
| RN | [RN-022 e os conjuntos referenciados nos blocos UC-03A, UC-03B e UC-03C](home/traceability-matrix#TM-UC-03), [RN-081 a RN-083](home/traceability-matrix#TM-HU-079). |
| Pontos de extensão | [Solicitar trajeto](home/traceability-matrix#TM-HU-079); [consultar transporte parceiro](#UC-16); [sinalizar dado incorreto](#UC-26). |

**Fluxo principal**

1. O visitante abre um local.
2. [O sistema inclui os blocos de identidade e contexto](#UC-03A), [informações operacionais](#UC-03B) e [condições da visita.](#UC-03C)
3. [O sistema identifica a fonte, a data da última verificação e eventual estado “em revisão” dos dados sensíveis à atualização.](home/traceability-matrix#TM-HU-079)
4. [O visitante pode abrir trajeto, contato ou perfil oficial externo.](home/traceability-matrix#TM-HU-079)

**Fluxos alternativos**

- A1 — [Link oficial disponível](home/traceability-matrix#TM-UC-03): [o sistema abre o serviço externo após a ação do visitante.](home/traceability-matrix#TM-HU-079)
- A2 — Feriado ou horário especial: [o status usa a programação excepcional cadastrada.](home/traceability-matrix#TM-UC-03)
- A3 — O visitante aciona “Sinalizar dado incorreto”; [inicia o UC-26 sem precisar publicar uma avaliação.](home/traceability-matrix#TM-HU-088)
- A4 — [Há transporte parceiro ativo para o local/evento; o sistema oferece o UC-16 como opção adicional, sem substituir as informações gerais de acesso.](home/traceability-matrix#TM-HU-087)

**Fluxos de exceção**

- E1 — Dado desatualizado ou não verificado: [o sistema sinaliza a limitação.](home/traceability-matrix#TM-HU-079)
- E2 — Serviço externo indisponível: [os dados locais permanecem visíveis e o sistema informa que o trajeto/link não pôde ser aberto.](home/traceability-matrix#TM-HU-079)
- E3 — Cadastro não atende aos dados mínimos: [o local não é publicado.](home/traceability-matrix#TM-UC-03)

<a id="UC-03A"></a>
#### UC-03A — Consultar identidade e contexto

Bloco obrigatório incluído por UC-03. Apresenta descrição, categoria, tipo de experiência, fotos reais, características, informações históricas/culturais e regras do local.

| RF | RN |
|----|----|
| [RF-007, RF-008, RF-018, RF-019, RF-035, RF-036](home/traceability-matrix#TM-UC-03) | [RN-014 a RN-016, RN-024 a RN-027](home/traceability-matrix#TM-UC-03) |

<a id="UC-03B"></a>
#### UC-03B — Consultar informações operacionais

Bloco obrigatório incluído por UC-03. Apresenta horários e status, preços, cardápio/taxas, formato de serviço e contatos atualizados.

| RF | RN |
|----|----|
| [RF-009, RF-010, RF-017, RF-020](home/traceability-matrix#TM-UC-03) | [RN-011, RN-021, RN-024, RN-028](home/traceability-matrix#TM-UC-03) |

<a id="UC-03C"></a>
#### UC-03C — Consultar condições da visita

Bloco obrigatório incluído por UC-03. Apresenta localização, acesso, transporte, segurança, higiene, acessibilidade e adequação infantil. É o bloco reutilizado pelos pontos de extensão de trajeto e transporte parceiro.

| RF | RN |
|----|----|
| [RF-011 a RF-015](home/traceability-matrix#TM-UC-03) | [RN-012, RN-013, RN-017 a RN-020](home/traceability-matrix#TM-UC-03) |

---

<a id="UC-04"></a>
## UC-04 — Consultar eventos, equipamentos e atrações

| Campo | Especificação |
|-------|---------------|
| Objetivo | Conhecer programação, datas, horários, equipamentos e atrações disponíveis. |
| Ator principal | Visitante. |
| Pré-condições | Conteúdo publicado e vínculo com local ativo. |
| Pós-condições | Programação ou atração escolhida é exibida. |
| RF | [RF-016](home/traceability-matrix#TM-UC-04), [RF-080 e RF-081](home/traceability-matrix#TM-HU-080). [RF-044 e RF-050](home/traceability-matrix#TM-UC-04) permanecem associados ao backlog do Épico 8. |
| RN | [RN-012, RN-021, RN-022](home/traceability-matrix#TM-UC-04), [RN-084](home/traceability-matrix#TM-HU-080). |
| Pontos de extensão | [Consultar transporte parceiro](#UC-16); [sinalizar dado incorreto](#UC-26). |

**Fluxo principal**

1. O visitante abre a agenda ou um equipamento.
2. [O sistema lista atrações e eventos públicos.](home/traceability-matrix#TM-UC-04)
3. O visitante escolhe um item.
4. [O sistema exibe descrição, data, horário, local e programação associada.](home/traceability-matrix#TM-UC-04)

**Fluxos alternativos**

- A1 — O visitante filtra a agenda por [data](home/traceability-matrix#TM-HU-080), [cidade ou categoria](home/traceability-matrix#TM-UC-02).
- A2 — A atração está encerrada: [o sistema a identifica como inativa ou a mantém apenas em arquivo.](home/traceability-matrix#TM-HU-080)
- A3 — [Há transporte parceiro ativo para o evento; o sistema oferece o UC-16.](home/traceability-matrix#TM-HU-087)
- A4 — O visitante identifica programação, horário ou local incorreto; [inicia o UC-26 sem precisar publicar uma avaliação.](home/traceability-matrix#TM-HU-088)

**Fluxos de exceção**

- E1 — Vínculo do conteúdo com o local deixou de ser válido: [o conteúdo não é exibido.](home/business-rules#RN-072)

<a id="UC-05"></a>
## UC-05 — Consultar avaliações e mídia comunitária

| Campo | Especificação |
|-------|---------------|
| Objetivo | Reduzir incertezas com relatos, notas, fotos e vídeos reais da comunidade. |
| Ator principal | Visitante. |
| Pré-condições | Local público; avaliações/mídias aprovadas. |
| Pós-condições | Conteúdo comunitário é exibido na ordenação escolhida. |
| RF | [RF-021, RF-040](home/traceability-matrix#TM-UC-05). |
| RN | [RN-007, RN-022, RN-029, RN-031 a RN-036](home/traceability-matrix#TM-UC-05). |

**Fluxo principal**

1. O visitante abre a área comunitária de um local.
2. [O sistema mostra avaliações aprovadas com autoria, nota e data.](home/traceability-matrix#TM-UC-05)
3. O visitante ordena por [recência ou relevância.](home/traceability-matrix#TM-UC-05)
4. [O sistema mostra fotos e vídeos vinculados à experiência real.](home/traceability-matrix#TM-UC-05)

**Fluxos alternativos**

- A1 — Não há conteúdo comunitário: [o sistema informa a ausência sem fabricar nota.](home/traceability-matrix#TM-UC-05)
- A2 — Conteúdo foi denunciado: [ele segue visível ou preventivamente oculto conforme a gravidade.](home/traceability-matrix#TM-UC-05)

**Fluxos de exceção**

- E1 — Mídia não pode ser carregada: a avaliação textual continua disponível.

<a id="UC-06"></a>
## UC-06 — Usar assistente virtual

| Campo | Especificação |
|-------|---------------|
| Objetivo | Obter respostas e recomendações sobre locais e eventos em linguagem natural. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de transcrição de áudio. |
| Pré-condições | Assistente disponível. |
| Pós-condições | Resposta textual, limitação ou orientação alternativa é apresentada. |
| RF | [RF-030 a RF-033, RF-037](home/traceability-matrix#TM-UC-06). |
| RN | [RN-054 a RN-057, RN-059, RN-060](home/traceability-matrix#TM-UC-06). |

**Fluxo principal**

1. O visitante abre o assistente e envia uma pergunta textual.
2. [O sistema interpreta a intenção e o contexto atual.](home/traceability-matrix#TM-UC-06)
3. [O sistema prioriza informações do catálogo regional.](home/traceability-matrix#TM-UC-06)
4. [O sistema retorna resposta textual pertinente e links internos úteis.](home/traceability-matrix#TM-UC-06)

**Fluxos alternativos**

- A1 — Iniciado em página de local/evento: [o sistema usa esse item como contexto.](home/traceability-matrix#TM-UC-06)
- A2 — Pergunta por áudio: [o serviço transcreve; o sistema processa e responde em texto.](home/traceability-matrix#TM-UC-06)
- A3 — Informação insuficiente: [o sistema explicita a limitação e sugere buscas, categorias ou canais oficiais.](home/traceability-matrix#TM-UC-06)

**Fluxos de exceção**

- E1 — Áudio incompreensível: o sistema solicita nova gravação ou entrada textual.
- E2 — Fontes conflitantes/desatualizadas: o sistema não afirma certeza e identifica a limitação.

<a id="UC-07"></a>
## UC-07 — Publicar avaliação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que um usuário contribua com avaliação sobre experiência real. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Usuário autenticado; local existente. |
| Pós-condições | Avaliação é enviada para publicação/moderação e vinculada ao autor. |
| RF | [RF-022](home/traceability-matrix#TM-UC-07), [RF-082](home/traceability-matrix#TM-HU-081). |
| RN | [RN-030, RN-033, RN-035, RN-036](home/traceability-matrix#TM-UC-07), [RN-085](home/traceability-matrix#TM-HU-081). |

**Fluxo principal**

1. O usuário abre o formulário do local.
2. Informa nota, comentário e, opcionalmente, contexto e mídias.
3. [O sistema valida formato e vínculo.](home/traceability-matrix#TM-UC-07)
4. O usuário confirma.
5. [O sistema associa a avaliação ao perfil e a publica ou encaminha à moderação.](home/traceability-matrix#TM-UC-07)

**Fluxos alternativos**

- A1 — A avaliação contém mídia; o envio de arquivo segue as validações do [UC-17](#UC-17).
- A2 — O usuário também percebe dado cadastral incorreto; [o sistema oferece o UC-26 como ação separada e preserva a avaliação já preenchida.](home/traceability-matrix#TM-HU-081)

**Fluxos de exceção**

- E1 — Conteúdo viola regra grave: [o sistema rejeita/oculta e informa o motivo aplicável.](home/traceability-matrix#TM-UC-07)
- E2 — Sessão expirada: [o sistema solicita nova autenticação e restaura o conteúdo preenchido antes de enviar.](home/traceability-matrix#TM-HU-081)

<a id="UC-08"></a>
## UC-08 — Receber recomendações personalizadas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Descobrir locais compatíveis com preferências, histórico e perfis similares. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Consentimento e dados pessoais suficientes para o critério escolhido. |
| Pós-condições | Recomendações justificáveis são exibidas sem revelar terceiros. |
| RF | [RF-023, RF-024, RF-025](home/traceability-matrix#TM-UC-08), [RF-083](home/traceability-matrix#TM-HU-082). |
| RN | [RN-039 a RN-042](home/traceability-matrix#TM-UC-08), [RN-086](home/traceability-matrix#TM-HU-082). |

**Fluxo principal**

1. O usuário acessa recomendações.
2. [O sistema considera histórico permitido, avaliações válidas e preferências.](home/traceability-matrix#TM-UC-08)
3. [O sistema calcula compatibilidade e exclui dados inválidos/moderados.](home/traceability-matrix#TM-UC-08)
4. [O sistema exibe locais recomendados.](home/traceability-matrix#TM-UC-08)

**Fluxos alternativos**

- A1 — Dados insuficientes: [o sistema solicita interesses ou mostra opções gerais.](home/traceability-matrix#TM-HU-082)
- A2 — Filtragem colaborativa: [resultados agregados são usados sem revelar identidade ou histórico alheio.](home/traceability-matrix#TM-UC-08)

**Fluxos de exceção**

- E1 — Usuário não autorizou uso do histórico: [esse histórico é ignorado.](home/traceability-matrix#TM-UC-08)

<a id="UC-09"></a>
## UC-09 — Gerar roteiro personalizado

| Campo | Especificação |
|-------|---------------|
| Objetivo | Planejar passeio ordenado de acordo com interesses e restrições práticas. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Serviço de mapas/transportes. |
| Pré-condições | Preferências informadas; catálogo com locais elegíveis. |
| Pós-condições | [Roteiro é exibido](home/traceability-matrix#TM-UC-09) e [pode ser salvo e ajustado.](home/traceability-matrix#TM-HU-083) |
| RF | [RF-026](home/traceability-matrix#TM-UC-09), [RF-084](home/traceability-matrix#TM-HU-083). |
| RN | [RN-043, RN-044, RN-052, RN-053](home/traceability-matrix#TM-UC-09), [RN-087](home/traceability-matrix#TM-HU-083). |

**Fluxo principal**

1. O usuário informa interesses, período, origem e perfil do público.
2. [O sistema seleciona locais públicos com dados mínimos.](home/traceability-matrix#TM-UC-09)
3. [O sistema considera distância, horários, status e adequação.](home/traceability-matrix#TM-UC-09)
4. [O sistema gera uma sequência de passeio.](home/traceability-matrix#TM-UC-09)
5. O usuário revisa e [salva o roteiro.](home/traceability-matrix#TM-HU-083)

**Fluxos alternativos**

- A1 — Usuário reorganiza manualmente; [o sistema preserva a ordem definida.](home/traceability-matrix#TM-UC-09)
- A2 — Usuário remove/substitui um local; [o sistema recalcula os trechos afetados.](home/traceability-matrix#TM-HU-083)

**Fluxos de exceção**

- E1 — Não há combinação viável: [o sistema explica as restrições e sugere flexibilizações.](home/traceability-matrix#TM-HU-083)

<a id="UC-10"></a>
## UC-10 — Gerenciar listas pessoais

| Campo | Especificação |
|-------|---------------|
| Objetivo | Criar, nomear, organizar, editar e excluir listas de locais. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Sessão válida. |
| Pós-condições | Lista do proprietário é persistida conforme a operação. |
| RF | [RF-027](home/traceability-matrix#TM-UC-10). |
| RN | [RN-045, RN-046](home/traceability-matrix#TM-UC-10). |

**Fluxo principal**

1. O usuário cria uma lista e informa o nome.
2. Adiciona, remove ou reordena locais.
3. [O sistema valida a propriedade.](home/traceability-matrix#TM-UC-10)
4. [O sistema salva a lista.](home/traceability-matrix#TM-UC-10)

**Fluxos alternativos**

- A1 — Usuário edita ou exclui uma lista própria.

**Fluxos de exceção**

- E1 — Tentativa de alterar lista de terceiro: [o sistema nega a operação.](home/traceability-matrix#TM-UC-10)

<a id="UC-11"></a>
## UC-11 — Registrar locais visitados

| Campo | Especificação |
|-------|---------------|
| Objetivo | Manter histórico pessoal de experiências na região. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Sessão válida; local existente. |
| Pós-condições | Histórico pessoal é criado, alterado ou removido sem mudar o cadastro público. |
| RF | [RF-028](home/traceability-matrix#TM-UC-11). |
| RN | [RN-039, RN-047 a RN-049](home/traceability-matrix#TM-UC-11). |

**Fluxo principal**

1. O usuário marca um local como visitado.
2. Opcionalmente informa data e observação.
3. [O sistema vincula o registro ao usuário.](home/traceability-matrix#TM-UC-11)
4. [O sistema confirma a atualização do histórico.](home/traceability-matrix#TM-UC-11)

**Fluxos alternativos**

- A1 — O proprietário edita ou remove o registro.

**Fluxos de exceção**

- E1 — Tentativa de acessar histórico alheio: [o sistema nega.](home/traceability-matrix#TM-UC-11)

<a id="UC-12"></a>
## UC-12 — Usar checklists

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acompanhar tarefas e atividades pessoais de um passeio. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Sessão válida; checklist ou roteiro selecionado. |
| Pós-condições | Progresso pessoal é atualizado. |
| RF | [RF-029](home/traceability-matrix#TM-UC-12), [RF-085](home/traceability-matrix#TM-HU-084). |
| RN | [RN-050, RN-051](home/traceability-matrix#TM-UC-12), [RN-088](home/traceability-matrix#TM-HU-084). |

**Fluxo principal**

1. O usuário abre um checklist.
2. Adiciona itens ou marca/desmarca uma atividade.
3. [O sistema salva o progresso pessoal.](home/traceability-matrix#TM-UC-12)

**Fluxos alternativos**

- A1 — Checklist é criado a partir de roteiro personalizado.

**Fluxos de exceção**

- E1 — Item se refere a atração inativa: [o sistema alerta, mas não altera dados oficiais.](home/traceability-matrix#TM-HU-084)

<a id="UC-13"></a>
## UC-13 — Criar e compartilhar enquete

| Campo | Especificação |
|-------|---------------|
| Objetivo | Facilitar decisão em grupo entre locais ou eventos. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Sessão válida; [ao menos duas opções válidas.](home/traceability-matrix#TM-HU-085) |
| Pós-condições | Enquete e link público são criados. |
| RF | [RF-038](home/traceability-matrix#TM-UC-13), [RF-086](home/traceability-matrix#TM-HU-085). |
| RN | [RN-063 a RN-065](home/traceability-matrix#TM-UC-13), [RN-089](home/traceability-matrix#TM-HU-085). |

**Fluxo principal**

1. O usuário inicia uma enquete.
2. Informa título e opções de locais/eventos válidos.
3. [O sistema valida e cria a enquete.](home/traceability-matrix#TM-UC-13)
4. [O sistema gera link público.](home/traceability-matrix#TM-UC-13)
5. O usuário compartilha o link externamente.

**Fluxos alternativos**

- A1 — [Usuário altera opções antes da primeira votação.](home/traceability-matrix#TM-HU-085)

**Fluxos de exceção**

- E1 — Opção inválida/inativa: [o sistema solicita substituição.](home/traceability-matrix#TM-UC-13)

<a id="UC-14"></a>
## UC-14 — Votar em enquete

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar voto sem exigir login ou revelar identidade. |
| Ator principal | Votante anônimo. |
| Pré-condições | Link válido; [enquete aberta.](home/traceability-matrix#TM-HU-085) |
| Pós-condições | [Voto contabilizado e resultado atualizado.](home/traceability-matrix#TM-HU-085) |
| RF | [RF-038](home/traceability-matrix#TM-UC-14), [RF-086](home/traceability-matrix#TM-HU-085). |
| RN | [RN-064, RN-065](home/traceability-matrix#TM-UC-14), [RN-089](home/traceability-matrix#TM-HU-085). |

**Fluxo principal**

1. O votante abre o link público.
2. [O sistema mostra opções e situação da enquete.](home/traceability-matrix#TM-HU-085)
3. O votante escolhe uma opção e confirma.
4. [O sistema aplica controles antifraude sem exposição de identidade.](home/traceability-matrix#TM-UC-14)
5. [O sistema contabiliza o voto.](home/traceability-matrix#TM-UC-14)

**Fluxos alternativos**

- A1 — [Configuração permite múltipla escolha; o votante seleciona o limite permitido.](home/traceability-matrix#TM-HU-085)

**Fluxos de exceção**

- E1 — Enquete encerrada: [o sistema não registra voto e mostra o resultado disponível.](home/traceability-matrix#TM-HU-085)
- E2 — Controle antifraude rejeita duplicidade: [o sistema informa que o voto não foi aceito.](home/traceability-matrix#TM-HU-085)

<a id="UC-15"></a>
## UC-15 — Compartilhar lista pessoal

| Campo | Especificação |
|-------|---------------|
| Objetivo | Disponibilizar uma lista selecionada por link público. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Usuário é proprietário da lista. |
| Pós-condições | [Link público revogável](home/traceability-matrix#TM-HU-086) é gerado sem [dados privados desnecessários.](home/traceability-matrix#TM-UC-15) |
| RF | [RF-041](home/traceability-matrix#TM-UC-15), [RF-087](home/traceability-matrix#TM-HU-086). |
| RN | [RN-045, RN-061, RN-062](home/traceability-matrix#TM-UC-15), [RN-090](home/traceability-matrix#TM-HU-086). |

**Fluxo principal**

1. O usuário escolhe lista própria e aciona compartilhar.
2. [O sistema mostra quais dados ficarão públicos.](home/traceability-matrix#TM-UC-15)
3. O usuário confirma.
4. [O sistema gera link de visualização.](home/traceability-matrix#TM-UC-15)

**Fluxos alternativos**

- A1 — [Proprietário revoga o link; acessos posteriores deixam de exibir a lista.](home/traceability-matrix#TM-HU-086)

**Fluxos de exceção**

- E1 — Lista não pertence ao usuário: [compartilhamento negado.](home/traceability-matrix#TM-UC-15)

<a id="UC-16"></a>
## UC-16 — Consultar transporte alternativo parceiro

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar contatos e opções locais de deslocamento associados a local/evento. |
| Ator principal | Visitante. |
| Atores secundários | Serviço/operador de transporte parceiro. |
| Tipo de relação | `<<extend>>` de [UC-03](#UC-03) e [UC-04](#UC-04) no ponto “consultar opções de deslocamento”. |
| Condição de extensão | [Existe parceiro ativo, com área atendida e contato público compatíveis com o local/evento.](home/traceability-matrix#TM-HU-087) |
| Pré-condições | Local/evento público; [parceiro e contato públicos cadastrados.](home/traceability-matrix#TM-HU-087) |
| Pós-condições | [Opções são exibidas e o visitante pode iniciar contato externo.](home/traceability-matrix#TM-HU-087) |
| RF | [RF-039](home/traceability-matrix#TM-UC-16), [RF-088](home/traceability-matrix#TM-HU-087). |
| RN | [RN-091](home/traceability-matrix#TM-HU-087). |

**Fluxo principal**

1. O visitante abre opções de transporte do local/evento.
2. [O sistema lista modalidade, área atendida, horários e contato.](home/traceability-matrix#TM-HU-087)
3. O visitante escolhe uma opção.
4. [O sistema abre o canal externo após confirmação.](home/traceability-matrix#TM-HU-087)

**Fluxos alternativos**

- A1 — [Não há parceiro elegível: a extensão não é acionada e o sistema mantém as informações gerais de acesso e trajeto](home/traceability-matrix#TM-HU-087) de [UC-03](#UC-03)/[UC-04](#UC-04).

**Fluxos de exceção**

- E1 — Canal indisponível: [o sistema informa sem garantir contratação ou disponibilidade.](home/traceability-matrix#TM-HU-087)

<a id="UC-17"></a>
## UC-17 — Publicar mídia comunitária

| Campo | Especificação |
|-------|---------------|
| Objetivo | Compartilhar fotos e vídeos curtos de uma experiência real. |
| Ator principal | Usuário autenticado. |
| Pré-condições | Sessão válida; local/evento existente. |
| Pós-condições | Mídia fica vinculada ao autor e ao local, sujeita à moderação. |
| RF | [RF-040](home/traceability-matrix#TM-UC-17). |
| RN | [RN-033 a RN-036](home/traceability-matrix#TM-UC-17). |

**Fluxo principal**

1. O usuário seleciona local/evento e envia mídia.
2. Informa contexto mínimo da experiência.
3. [O sistema valida tipo, tamanho e vínculo.](home/traceability-matrix#TM-UC-17)
4. [O sistema publica ou envia à moderação.](home/traceability-matrix#TM-UC-17)

**Fluxos alternativos**

- A1 — Mídia acompanha uma avaliação do [UC-07](#UC-07).

**Fluxos de exceção**

- E1 — Arquivo malicioso ou conteúdo grave: [o sistema bloqueia/oculta preventivamente.](home/traceability-matrix#TM-UC-17)

<a id="UC-26"></a>
## UC-26 — Sinalizar e tratar dado incorreto

| Campo | Especificação |
|-------|---------------|
| Objetivo | Fechar o ciclo entre uma inconsistência percebida pela comunidade e a revisão do cadastro oficial. |
| Prioridade | **Must have** — dor recorrente e diretamente validada nas [entrevistas](home/interviews/relatorio-entrevistas) e no [questionário](home/survey). |
| Ator principal | Usuário autenticado. |
| Atores secundários | [Administrador autorizado, em função de curadoria](home/traceability-matrix#TM-HU-088); responsável pelo local, quando identificável. |
| Pré-condições | Local/evento publicado; usuário autenticado para concluir o envio. |
| Pós-condições | [Sinalização possui protocolo e estado rastreável; após análise, o dado é corrigido, mantido com justificativa ou marcado como não verificável; o autor recebe o resultado.](home/traceability-matrix#TM-HU-088) |
| RF | [RF-022](home/traceability-matrix#TM-UC-07) cobre a contribuição comunitária; [RF-089](home/traceability-matrix#TM-HU-088) cobre o tratamento da sinalização. |
| RN | [RN-015, RN-017, RN-019, RN-021, RN-024, RN-027, RN-037, RN-038](home/traceability-matrix#TM-UC-26), [RN-092 e RN-093](home/traceability-matrix#TM-HU-088). |
| Pontos de extensão | [UC-03](#UC-03) e [UC-04](#UC-04), na ação “Sinalizar dado incorreto”. |

O **administrador autorizado**, em função de curadoria, é o responsável operacional por validar a sinalização e fechar o ciclo. Essa atribuição usa o papel administrativo existente e não cria novo papel de acesso.

**Fluxo principal**

1. [O usuário aciona “Sinalizar dado incorreto” no local ou evento.](home/traceability-matrix#TM-HU-088)
2. [Seleciona o campo afetado, informa o valor observado, data da constatação e, opcionalmente, anexa evidência.](home/traceability-matrix#TM-HU-088)
3. [O sistema valida o envio, preserva uma cópia do valor publicado e cria um protocolo com estado “pendente”.](home/traceability-matrix#TM-HU-088)
4. [O administrador em função de curadoria compara a sinalização com fonte verificável e, quando necessário, solicita confirmação ao responsável pelo local.](home/traceability-matrix#TM-HU-088)
5. [Confirmada a inconsistência, o administrador corrige ou invalida o campo e registra fonte, data, responsável e justificativa da decisão.](home/traceability-matrix#TM-HU-088)
6. [O sistema atualiza a data de verificação, encerra o protocolo e comunica o resultado ao usuário que sinalizou.](home/traceability-matrix#TM-HU-088)

**Fluxos alternativos**

- A1 — Já existe sinalização equivalente pendente: [o sistema associa o novo relato ao protocolo existente, preservando autoria e evidências.](home/traceability-matrix#TM-HU-088)
- A2 — A apuração ainda não terminou: [o campo permanece “em revisão” sem substituir automaticamente o dado oficial.](home/traceability-matrix#TM-HU-088)
- A3 — A sinalização não procede: [o administrador mantém o valor, registra a justificativa e comunica o encerramento.](home/traceability-matrix#TM-HU-088)
- A4 — O usuário iniciou a ação sem autenticação: [o conteúdo preenchido é preservado enquanto o sistema solicita login.](home/traceability-matrix#TM-HU-081)

**Fluxos de exceção**

- E1 — Evidência inválida ou maliciosa: [o arquivo é bloqueado e a sinalização textual pode continuar se contiver dados suficientes.](home/traceability-matrix#TM-HU-088)
- E2 — Campo crítico não pode ser verificado e pode causar risco imediato: [o sistema o oculta preventivamente.](home/traceability-matrix#TM-HU-088)
- E3 — Falha ao registrar o protocolo: [nenhum cadastro é alterado e o sistema orienta nova tentativa.](home/traceability-matrix#TM-HU-088)

## Escopo fora da linha de base

UC-18 a UC-25 mantêm seus identificadores para preservar a rastreabilidade, mas foram retirados deste corpo porque pertencem ao Épico 8, marcado como **Won't have nesta entrega** e sem procedência identificada em stakeholders.
