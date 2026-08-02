---
title: Casos de Uso Descritivos
---
## Priorização de Casos de Uso

- **Must have**: necessário na linha de base atual.
- **Should have**: importante, mas pode entrar depois do núcleo essencial.
- **Could have**: desejável se houver capacidade.
- **Won't have nesta entrega**: não integra a versão de entrega atual; não significa baixa importância futura. Os itens nessa situação podem ser modelados como hipóteses para orientar descoberta e validação, mas não constituem escopo aprovado.

| Casos de uso | Prioridade de entrega |
|--------------|-----------------------|
| UC-01 a UC-05 | Must have |
| UC-06 | Must have |
| UC-07 | Should have |
| UC-08 | Should have |
| UC-09, UC-10 e UC-12 | Must have |
| UC-11, UC-15 e UC-16 | Should have |
| UC-13, UC-14 e UC-17 | Could have |
| UC-26 | Must have |
| UC-18 a UC-25 | Hipótese em validação |

> A priorização acima está compatível com a priorização de requisitos.

---

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
2. O sistema apresenta o catálogo regional unificado.
3. O visitante seleciona uma lista, categoria ou item.
4. O sistema ordena a lista pelo critério documentado e identifica conteúdo patrocinado.
5. O sistema apresenta o resultado e permite consultar seus detalhes.

**Fluxos alternativos**

- A1 — O visitante escolhe “populares”; o sistema ordena por visitação/interações, avaliações e recência.
- A2 — O visitante escolhe “pouco divulgados”; o sistema aplica o critério de avaliação e visitas.

**Fluxos de exceção**

- E1 — Catálogo indisponível: o sistema informa a falha sem expor detalhes técnicos e orienta nova tentativa.
- E2 — Registro duplicado detectado: o sistema não publica ambos até a consolidação.

---

## UC-02 — Pesquisar e filtrar locais e eventos

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar conteúdo por termo, nome, categoria, cidade, perfil de público e proximidade da localização escolhida. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de geolocalização/mapas, somente quando o visitante escolher proximidade. |
| Pré-condições | Registros pesquisáveis contêm os dados mínimos; localização do dispositivo depende de consentimento. |
| Pós-condições | Resultados filtrados ou alternativas de busca são apresentados; quando aplicável, distância e referência de origem ficam explícitas. |
| RF | [RF-004, RF-005, RF-006, RF-006A, RF-011](home/traceability-matrix#TM-UC-02), [RF-077](home/traceability-matrix#TM-HU-077), [RF-078](home/traceability-matrix#TM-HU-078). |
| RN | [RN-003, RN-004, RN-005, RN-009, RN-010](home/traceability-matrix#TM-UC-02), [RN-078](home/traceability-matrix#TM-HU-077), [RN-079, RN-080](home/traceability-matrix#TM-HU-078). |

**Fluxo principal**

1. O visitante informa termo e/ou filtros, ou escolhe descobrir o que está próximo de uma localização.
2. O sistema valida formato, domínio, cardinalidade e taxonomia dos valores informados.
3. O sistema pesquisa nome, palavras-chave, categoria e cidade.
4. O sistema exibe os resultados e os filtros aplicados.
5. O visitante seleciona um resultado.

**Fluxos alternativos**

- A1 — Sem resultado exato: o sistema sugere correções, categorias próximas ou outra cidade.
- A2 — O visitante altera ou remove filtros e a pesquisa é refeita.
- A3 — O visitante escolhe “Mais próximos”; o sistema solicita consentimento, obtém a localização atual, calcula as distâncias e ordena os resultados elegíveis.
- A4 — O visitante não quer usar a localização atual; informa um bairro, cidade ou ponto de referência e o sistema usa essa origem para a busca por proximidade.

**Fluxos de exceção**

- E1 — Valor de filtro inválido: o sistema oferece apenas valores aprovados.
- E2 — Falha de consulta: o sistema informa a situação e uma próxima ação.
- E3 — Permissão de localização negada ou posição indisponível: a pesquisa continua por cidade e o sistema oferece a origem manual, sem bloquear o catálogo.
- E4 — Distância não calculável: o item pode permanecer no resultado, mas sem distância estimada e sem ser indevidamente priorizado como próximo.

---

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
3. O sistema identifica a fonte, a data da última verificação e eventual estado “em revisão” dos dados sensíveis à atualização.
4. O visitante pode abrir trajeto, contato ou perfil oficial externo.

**Fluxos alternativos**

- A1 — Link oficial disponível: o sistema abre o serviço externo após a ação do visitante.
- A2 — Feriado ou horário especial: o status usa a programação excepcional cadastrada.
- A3 — O visitante aciona “Sinalizar dado incorreto”; inicia o UC-26 sem precisar publicar uma avaliação.
- A4 — Há transporte parceiro ativo para o local/evento; o sistema oferece o UC-16 como opção adicional, sem substituir as informações gerais de acesso.

**Fluxos de exceção**

- E1 — Dado desatualizado ou não verificado: o sistema sinaliza a limitação.
- E2 — Serviço externo indisponível: os dados locais permanecem visíveis e o sistema informa que o trajeto/link não pôde ser aberto.
- E3 — Cadastro não atende aos dados mínimos: o local não é publicado.

#### UC-03A — Consultar identidade e contexto

Bloco obrigatório incluído por UC-03. Apresenta descrição, categoria, tipo de experiência, fotos reais, características, informações históricas/culturais e regras do local.

| RF | RN |
|----|----|
| [RF-007, RF-008, RF-018, RF-019, RF-035, RF-036](home/traceability-matrix#TM-UC-03) | [RN-014 a RN-016, RN-024 a RN-027](home/traceability-matrix#TM-UC-03) |

#### UC-03B — Consultar informações operacionais

Bloco obrigatório incluído por UC-03. Apresenta horários e status, preços, cardápio/taxas, formato de serviço e contatos atualizados.

| RF | RN |
|----|----|
| [RF-009, RF-010, RF-017, RF-020](home/traceability-matrix#TM-UC-03) | [RN-011, RN-021, RN-024, RN-028](home/traceability-matrix#TM-UC-03) |

#### UC-03C — Consultar condições da visita

Bloco obrigatório incluído por UC-03. Apresenta localização, acesso, transporte, segurança, higiene, acessibilidade e adequação infantil. É o bloco reutilizado pelos pontos de extensão de trajeto e transporte parceiro.

| RF | RN |
|----|----|
| [RF-011 a RF-015](home/traceability-matrix#TM-UC-03) | [RN-012, RN-013, RN-017 a RN-020](home/traceability-matrix#TM-UC-03) |

---

## UC-04 — Consultar eventos, equipamentos e atrações

| Campo | Especificação |
|-------|---------------|
| Objetivo | Conhecer programação, datas, horários, equipamentos e atrações disponíveis. |
| Ator principal | Visitante. |
| Pré-condições | Conteúdo publicado e vínculo com local ativo. |
| Pós-condições | Programação ou atração escolhida é exibida. |
| RF | [RF-016](home/traceability-matrix#TM-UC-04), [RF-080 e RF-081](home/traceability-matrix#TM-HU-080). [RF-044 e RF-050](home/traceability-matrix#TM-UC-04) são detalhados como hipóteses em [UC-20](#UC-20) e [UC-23](#UC-23), fora da entrega atual. |
| RN | [RN-012, RN-021, RN-022](home/traceability-matrix#TM-UC-04), [RN-084](home/traceability-matrix#TM-HU-080). |
| Pontos de extensão | [Consultar transporte parceiro](#UC-16); [sinalizar dado incorreto](#UC-26). |

**Fluxo principal**

1. O visitante abre a agenda ou um equipamento.
2. O sistema lista atrações e eventos públicos.
3. O visitante escolhe um item.
4. O sistema exibe descrição, data, horário, local e programação associada.

**Fluxos alternativos**

- A1 — O visitante filtra a agenda por data, cidade ou categoria.
- A2 — A atração está encerrada: o sistema a identifica como inativa ou a mantém apenas em arquivo.
- A3 — Há transporte parceiro ativo para o evento; o sistema oferece o UC-16.
- A4 — O visitante identifica programação, horário ou local incorreto; inicia o UC-26 sem precisar publicar uma avaliação.

**Fluxos de exceção**

- E1 — Vínculo do conteúdo com o local deixou de ser válido: o conteúdo não é exibido.

---

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
2. O sistema mostra avaliações aprovadas com autoria, nota e data.
3. O visitante ordena por recência ou relevância.
4. O sistema mostra fotos e vídeos vinculados à experiência real.

**Fluxos alternativos**

- A1 — Não há conteúdo comunitário: o sistema informa a ausência sem fabricar nota.
- A2 — Conteúdo foi denunciado: ele segue visível ou preventivamente oculto conforme a gravidade.

**Fluxos de exceção**

- E1 — Mídia não pode ser carregada: a avaliação textual continua disponível.

---

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
2. O sistema interpreta a intenção e o contexto atual.
3. O sistema prioriza informações do catálogo regional.
4. O sistema retorna resposta textual pertinente e links internos úteis.

**Fluxos alternativos**

- A1 — Iniciado em página de local/evento: o sistema usa esse item como contexto.
- A2 — Pergunta por áudio: o serviço transcreve; o sistema processa e responde em texto.
- A3 — Informação insuficiente: o sistema explicita a limitação e sugere buscas, categorias ou canais oficiais.

**Fluxos de exceção**

- E1 — Áudio incompreensível: o sistema solicita nova gravação ou entrada textual.
- E2 — Fontes conflitantes/desatualizadas: o sistema não afirma certeza e identifica a limitação.

---

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
3. O sistema valida formato e vínculo.
4. O usuário confirma.
5. O sistema associa a avaliação ao perfil e a publica ou encaminha à moderação.

**Fluxos alternativos**

- A1 — A avaliação contém mídia; o envio de arquivo segue as validações do [UC-17](#UC-17).
- A2 — O usuário também percebe dado cadastral incorreto; o sistema oferece o UC-26 como ação separada e preserva a avaliação já preenchida.

**Fluxos de exceção**

- E1 — Conteúdo viola regra grave: o sistema rejeita/oculta e informa o motivo aplicável.
- E2 — Sessão expirada: o sistema solicita nova autenticação e restaura o conteúdo preenchido antes de enviar.

---

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
2. O sistema considera histórico permitido, avaliações válidas e preferências.
3. O sistema calcula compatibilidade e exclui dados inválidos/moderados.
4. O sistema exibe locais recomendados.

**Fluxos alternativos**

- A1 — Dados insuficientes: o sistema solicita interesses ou mostra opções gerais.
- A2 — Filtragem colaborativa: resultados agregados são usados sem revelar identidade ou histórico alheio.

**Fluxos de exceção**

- E1 — Usuário não autorizou uso do histórico: esse histórico é ignorado.

---

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
2. O sistema seleciona locais públicos com dados mínimos.
3. O sistema considera distância, horários, status e adequação.
4. O sistema gera uma sequência de passeio.
5. O usuário revisa e salva o roteiro.

**Fluxos alternativos**

- A1 — Usuário reorganiza manualmente; o sistema preserva a ordem definida.
- A2 — Usuário remove/substitui um local; o sistema recalcula os trechos afetados.

**Fluxos de exceção**

- E1 — Não há combinação viável: o sistema explica as restrições e sugere flexibilizações.

---

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
3. O sistema valida a propriedade.
4. O sistema salva a lista.

**Fluxos alternativos**

- A1 — Usuário edita ou exclui uma lista própria.

**Fluxos de exceção**

- E1 — Tentativa de alterar lista de terceiro: o sistema nega a operação.

---

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
3. O sistema vincula o registro ao usuário.
4. O sistema confirma a atualização do histórico.

**Fluxos alternativos**

- A1 — O proprietário edita ou remove o registro.

**Fluxos de exceção**

- E1 — Tentativa de acessar histórico alheio: o sistema nega.

---

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
3. O sistema salva o progresso pessoal.

**Fluxos alternativos**

- A1 — Checklist é criado a partir de roteiro personalizado.

**Fluxos de exceção**

- E1 — Item se refere a atração inativa: o sistema alerta, mas não altera dados oficiais.

---

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
3. O sistema valida e cria a enquete.
4. O sistema gera link público.
5. O usuário compartilha o link externamente.

**Fluxos alternativos**

- A1 — Usuário altera opções antes da primeira votação.

**Fluxos de exceção**

- E1 — Opção inválida/inativa: o sistema solicita substituição.

---

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
2. O sistema mostra opções e situação da enquete.
3. O votante escolhe uma opção e confirma.
4. O sistema aplica controles antifraude sem exposição de identidade.
5. O sistema contabiliza o voto.

**Fluxos alternativos**

- A1 — Configuração permite múltipla escolha; o votante seleciona o limite permitido.

**Fluxos de exceção**

- E1 — Enquete encerrada: o sistema não registra voto e mostra o resultado disponível.
- E2 — Controle antifraude rejeita duplicidade: o sistema informa que o voto não foi aceito.

---

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
2. O sistema mostra quais dados ficarão públicos.
3. O usuário confirma.
4. O sistema gera link de visualização.

**Fluxos alternativos**

- A1 — Proprietário revoga o link; acessos posteriores deixam de exibir a lista.

**Fluxos de exceção**

- E1 — Lista não pertence ao usuário: compartilhamento negado.

---

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
2. O sistema lista modalidade, área atendida, horários e contato.
3. O visitante escolhe uma opção.
4. O sistema abre o canal externo após confirmação.

**Fluxos alternativos**

- A1 — Não há parceiro elegível: a extensão não é acionada e o sistema mantém as informações gerais de acesso e trajeto de [UC-03](#UC-03)/[UC-04](#UC-04).

**Fluxos de exceção**

- E1 — Canal indisponível: o sistema informa sem garantir contratação ou disponibilidade.

---

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
3. O sistema valida tipo, tamanho e vínculo.
4. O sistema publica ou envia à moderação.

**Fluxos alternativos**

- A1 — Mídia acompanha uma avaliação do [UC-07](#UC-07).

**Fluxos de exceção**

- E1 — Arquivo malicioso ou conteúdo grave: o sistema bloqueia/oculta preventivamente.

---

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

1. O usuário aciona “Sinalizar dado incorreto” no local ou evento.
2. Seleciona o campo afetado, informa o valor observado, data da constatação e, opcionalmente, anexa evidência.
3. O sistema valida o envio, preserva uma cópia do valor publicado e cria um protocolo com estado “pendente”.
4. O administrador em função de curadoria compara a sinalização com fonte verificável e, quando necessário, solicita confirmação ao responsável pelo local.
5. Confirmada a inconsistência, o administrador corrige ou invalida o campo e registra fonte, data, responsável e justificativa da decisão.
6. O sistema atualiza a data de verificação, encerra o protocolo e comunica o resultado ao usuário que sinalizou.

**Fluxos alternativos**

- A1 — Já existe sinalização equivalente pendente: o sistema associa o novo relato ao protocolo existente, preservando autoria e evidências.
- A2 — A apuração ainda não terminou: o campo permanece “em revisão” sem substituir automaticamente o dado oficial.
- A3 — A sinalização não procede: o administrador mantém o valor, registra a justificativa e comunica o encerramento.
- A4 — O usuário iniciou a ação sem autenticação: o conteúdo preenchido é preservado enquanto o sistema solicita login.

**Fluxos de exceção**

- E1 — Evidência inválida ou maliciosa: o arquivo é bloqueado e a sinalização textual pode continuar se contiver dados suficientes.
- E2 — Campo crítico não pode ser verificado e pode causar risco imediato: o sistema o oculta preventivamente.
- E3 — Falha ao registrar o protocolo: nenhum cadastro é alterado e o sistema orienta nova tentativa.

---

## Hipóteses de fluxo — Épico 8

Os casos UC-18 a UC-25 descrevem uma **hipótese de escopo administrativo** derivada dos requisitos, histórias de usuário, regras de negócio e do protótipo.

## UC-18 — Cadastrar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar um equipamento cultural para que possa ser administrado e, quando apto, disponibilizado ao público. |
| Prioridade | **Must have** — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Pré-condições | Administrador autenticado e autorizado; dados mínimos do equipamento disponíveis. |
| Pós-condições | Equipamento é registrado, com estado de publicação compatível com os dados informados e trilha de auditoria. |
| RF / HU | [RF-042](home/functional-requirements#RF-042), [HU-042](home/user-storys#HU-042). |
| RN | [RN-023, RN-068 e RN-076](home/business-rules#RN-023). |

**Fluxo principal**

1. O administrador inicia o cadastro de um equipamento cultural.
2. Informa identificação, localização, dados de funcionamento, responsável e demais informações exigidas para o tipo de local.
3. O sistema valida a autorização do administrador e os dados mínimos do cadastro.
4. O sistema registra o equipamento e a operação de auditoria.
5. O sistema disponibiliza o equipamento ou o mantém pendente até que atenda às condições de publicação.

**Fluxos alternativos**

- A1 — Há dados mínimos pendentes: o sistema mantém o cadastro como não publicado e informa os campos necessários.
- A2 — O equipamento já possui cadastro: o sistema direciona o administrador para [UC-19](#UC-19).

**Fluxos de exceção**

- E1 — Administrador sem autorização: o sistema nega o cadastro e não cria registro público.

## UC-19 — Editar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Manter atualizados os dados de um equipamento cultural cadastrado. |
| Prioridade | **Should have** — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Pré-condições | Administrador autenticado e autorizado; equipamento existente. |
| Pós-condições | Dados autorizados são atualizados, com histórico da alteração. |
| RF / HU | [RF-043](home/functional-requirements#RF-043), [HU-043](home/user-storys#HU-043). |
| RN | [RN-023, RN-066 e RN-076](home/business-rules#RN-023). |

**Fluxo principal**

1. O administrador seleciona um equipamento cultural cadastrado.
2. O sistema apresenta os dados atuais e verifica o escopo de administração.
3. O administrador altera as informações necessárias.
4. O sistema valida os dados e o vínculo do administrador ao equipamento.
5. O sistema salva a alteração e registra responsável, data, hora e recurso afetado.

**Fluxos alternativos**

- A1 — A edição torna o cadastro incompleto: o sistema retira o equipamento da exibição pública até a regularização.

**Fluxos de exceção**

- E1 — O equipamento não pertence ao escopo do administrador: o sistema nega a alteração.

## UC-20 — Consultar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Consultar informações públicas de um equipamento cultural ativo. |
| Prioridade | **Must have** — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Visitante. |
| Pré-condições | Equipamento publicado e com vínculo válido. |
| Pós-condições | Informações públicas do equipamento são exibidas ao visitante. |
| RF / HU | [RF-044](home/functional-requirements#RF-044), [HU-044](home/user-storys#HU-044). |
| RN | [RN-022 e RN-068](home/business-rules#RN-022). |
| Pontos de extensão | [UC-26](#UC-26), ao sinalizar um dado incorreto. |

**Fluxo principal**

1. O visitante seleciona um equipamento cultural publicado.
2. O sistema verifica se o cadastro atende às condições de publicação.
3. O sistema exibe localização, programação, serviços e demais informações públicas disponíveis.

**Fluxos alternativos**

- A1 — O visitante identifica um dado incorreto: inicia [UC-26](#UC-26) sem precisar publicar uma avaliação.

**Fluxos de exceção**

- E1 — O equipamento não está ativo ou não possui vínculo válido: o sistema não o exibe como conteúdo público.

## UC-21 — Associar administrador a equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Vincular um administrador autorizado a um equipamento cultural para delimitar seu escopo de gestão. |
| Prioridade | **Should have** — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Administrador de equipamento cultural. |
| Pré-condições | Administrador da plataforma autenticado; equipamento e conta administrativa existentes. |
| Pós-condições | Vínculo de administração é registrado com escopo definido e auditável. |
| RF / HU | [RF-045](home/functional-requirements#RF-045), [HU-045](home/user-storys#HU-045). |
| RN | [RN-023, RN-066, RN-067 e RN-076](home/business-rules#RN-023). |

**Fluxo principal**

1. O administrador da plataforma seleciona um equipamento e uma conta administrativa.
2. O sistema verifica a existência dos dois registros e a autorização para realizar a associação.
3. O administrador confirma o escopo de gestão concedido.
4. O sistema registra o vínculo e a operação de auditoria.
5. O administrador associado passa a poder acessar apenas as funcionalidades vinculadas ao equipamento.

**Fluxos alternativos**

- A1 — A conta já está associada ao equipamento: o sistema apresenta o vínculo existente e evita duplicidade.

**Fluxos de exceção**

- E1 — Equipamento ou conta não é válido: o sistema não cria a associação.

## UC-22 — Autenticar administrador

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que um administrador autorizado acesse somente as funcionalidades administrativas compatíveis com seu vínculo. |
| Prioridade | **Must have** — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador autorizado. |
| Pré-condições | Conta administrativa ativa; para gestão de um local, vínculo prévio registrado. |
| Pós-condições | Sessão administrativa é iniciada com o escopo de acesso aplicável. |
| RF / HU | [RF-046](home/functional-requirements#RF-046), [HU-046](home/user-storys#HU-046). |
| RN | [RN-023 e RN-067](home/business-rules#RN-023). |

**Fluxo principal**

1. O administrador informa suas credenciais.
2. O sistema verifica a identidade e o vínculo administrativo aplicável.
3. O sistema inicia uma sessão com as permissões correspondentes ao escopo autorizado.

**Fluxos alternativos**

- A1 — A conta ainda não possui vínculo com um equipamento: o sistema mantém apenas as permissões compatíveis e orienta a associação por [UC-21](#UC-21), quando necessária.

**Fluxos de exceção**

- E1 — Credenciais inválidas ou conta inativa: o sistema não inicia a sessão administrativa.

## UC-23 — Gerenciar atrações de equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Cadastrar, editar, retirar de exibição e consultar atrações vinculadas a um equipamento cultural. |
| Prioridade | **Must have** para cadastro, edição e consulta (RF-047, RF-048, RF-050); **Won't have nesta entrega** para a remoção definitiva (RF-049). Fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural. |
| Atores secundários | Visitante, na consulta de atrações publicadas. |
| Pré-condições | Administrador autenticado e vinculado ao equipamento; equipamento ativo para publicação. |
| Pós-condições | Atração é criada, atualizada, inativada ou exibida conforme vínculo, validade e regras de publicação. |
| RF / HU | [RF-047 a RF-050](home/functional-requirements#RF-047), [HU-047 a HU-050](home/user-storys#HU-047). |
| RN | [RN-012, RN-023, RN-066, RN-068, RN-071, RN-072, RN-074, RN-075 e RN-076](home/business-rules#RN-012). |

**Fluxo principal**

1. O administrador acessa as atrações do equipamento ao qual está vinculado.
2. Seleciona cadastrar, editar ou retirar uma atração de exibição.
3. O sistema valida o escopo do administrador, o vínculo com o equipamento e os dados exigidos.
4. O sistema registra a operação e mantém o histórico da alteração.
5. Quando a atração estiver válida e publicada, o visitante pode consultá-la.

**Fluxos alternativos**

- A1 — A atração encerrou: o sistema a inativa ou arquiva, preservando o histórico administrativo.
- A2 — O visitante consulta uma atração publicada: o sistema apresenta as informações públicas disponíveis.

**Fluxos de exceção**

- E1 — Atração sem vínculo válido com equipamento ativo: o sistema impede sua exibição pública.
- E2 — Administrador tenta gerir atração de outro equipamento: o sistema nega a operação.

## UC-24 — Cadastrar estabelecimento gastronômico e gerenciar ofertas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar um estabelecimento gastronômico e permitir a gestão de ofertas vinculadas a ele. |
| Prioridade | **Must have** para o cadastro do estabelecimento (RF-051); **Won't have nesta entrega** para a gestão de ofertas (RF-052 a RF-054). Fluxo e telas administrativas ainda em validação com stakeholders. |
| Atores principais | Administrador da plataforma; administrador de estabelecimento gastronômico. |
| Pré-condições | Administradores autenticados; estabelecimento ativo e vínculo administrativo prévio para gerir ofertas. |
| Pós-condições | Estabelecimento é registrado e suas ofertas são publicadas, atualizadas, arquivadas ou removidas conforme validade e vínculo. |
| RF / HU | [RF-051 a RF-054](home/functional-requirements#RF-051), [HU-051 a HU-054](home/user-storys#HU-051). |
| RN | [RN-011, RN-023, RN-066, RN-068, RN-069, RN-071, RN-072, RN-073, RN-075 e RN-076](home/business-rules#RN-011). |

**Fluxo principal**

1. O administrador da plataforma cadastra o estabelecimento com os dados mínimos e associa o responsável administrativo.
2. O sistema valida os dados do estabelecimento e registra a operação.
3. O administrador do estabelecimento acessa as ofertas de seu local.
4. Cadastra, edita ou retira uma oferta de exibição, informando vínculo, descrição, responsável e período de validade.
5. O sistema valida escopo, vínculo e validade; então publica, atualiza ou arquiva a oferta e registra o histórico.

**Fluxos alternativos**

- A1 — O estabelecimento ainda não atende aos dados mínimos: o sistema o mantém fora da exibição pública.
- A2 — Uma oferta expira: o sistema a remove da exibição, arquiva ou marca como inativa.

**Fluxos de exceção**

- E1 — Oferta sem vínculo válido com estabelecimento ativo: o sistema impede sua publicação.
- E2 — Administrador sem escopo sobre o estabelecimento: o sistema nega a operação.

## UC-25 — Gerenciar publicações administrativas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Criar, editar e retirar publicações administrativas gerais ou vinculadas a um equipamento cultural ou estabelecimento gastronômico. |
| Prioridade | **Won't have nesta entrega** — hipótese em validação. |
| Atores principais | Administrador da plataforma; administrador de equipamento cultural ou estabelecimento gastronômico. |
| Pré-condições | Administrador autenticado; vínculo administrativo prévio quando a publicação estiver associada a um local. |
| Pós-condições | Publicação é criada, atualizada, inativada ou arquivada, com histórico e visibilidade compatíveis com seu vínculo. |
| RF / HU | [RF-055 a RF-058](home/functional-requirements#RF-055), [HU-055 a HU-058](home/user-storys#HU-055). |
| RN | [RN-023, RN-066, RN-068, RN-070, RN-071, RN-072, RN-074, RN-075 e RN-076](home/business-rules#RN-023). |

**Fluxo principal**

1. O administrador inicia a criação ou seleciona uma publicação existente.
2. Informa ou atualiza título, conteúdo, responsável e, quando aplicável, o local ao qual a publicação se vincula.
3. O sistema verifica a autenticação, o escopo de administração e os dados mínimos da publicação.
4. O sistema cria ou atualiza a publicação e registra o histórico da operação.
5. Quando o administrador solicita retirada, o sistema inativa ou arquiva o conteúdo conforme a regra de validade.

**Fluxos alternativos**

- A1 — A publicação é geral: o administrador da plataforma a publica sem vínculo com local específico.
- A2 — A publicação é vinculada a um local: o sistema a disponibiliza somente se o vínculo permanecer válido.

**Fluxos de exceção**

- E1 — Publicação sem dados mínimos ou vínculo obrigatório: o sistema impede sua exibição pública.
- E2 — Administrador tenta alterar publicação fora de seu escopo: o sistema nega a operação.