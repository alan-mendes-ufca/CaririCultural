## Épico 1: Exploração e Descoberta

### <a id="UC-001"></a>UC-001 — Consultar catálogo regional

| Campo | Especificação |
|-------|---------------|
| Objetivo | Descobrir locais, eventos e experiências regionais, turísticas, culturais, gastronômicas, comerciais e de lazer, por meio de um catálogo unificado. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Catálogo disponível. |
| Pós-condições | Itens compatíveis são exibidos e o visitante pode abrir um resultado. |
| HU | [HU-001](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-001). |
| RF | [RF-001](Requisitos-Funcionais#RF-001). |
| RN | [RN-001](Regras-de-Neg%C3%B3cio#RN-001), [RN-002](Regras-de-Neg%C3%B3cio#RN-002), [RN-008](Regras-de-Neg%C3%B3cio#RN-008), [RN-022](Regras-de-Neg%C3%B3cio#RN-022). |
| Rastreabilidade | [Linha TM-HU-001](Matriz-de-Rastreabilidade#TM-HU-001). |
| Pontos de extensão | [UC-002](#UC-002) e [UC-003](#UC-003) estendem este caso, na escolha entre a lista de populares e a de pouco divulgados. |

**Fluxo principal**

1. O visitante acessa a exploração.
2. O sistema apresenta o catálogo regional unificado, com locais, eventos e experiências gastronômicas, comerciais e de lazer.
3. O visitante seleciona uma categoria ou item do catálogo.
4. O sistema ordena a lista pelo critério documentado e identifica conteúdo patrocinado.
5. O sistema apresenta o resultado e permite consultar seus detalhes.

**Fluxos de exceção**

- E1 — Catálogo indisponível: o sistema informa a falha sem expor detalhes técnicos e orienta nova tentativa.
- E2 — Registro duplicado detectado: o sistema não publica ambos até a consolidação.

---

### <a id="UC-002"></a>UC-002 — Consultar locais em alta visitação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Descobrir localidades que estão sendo muito visitadas, para acompanhar tendências que estão acontecendo na região. |
| Prioridade | Should have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Catálogo disponível. |
| Pós-condições | Lista de locais populares é exibida, ordenada pelo critério de popularidade. |
| HU | [HU-002](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-002). |
| RF | [RF-002](Requisitos-Funcionais#RF-002). |
| RN | [RN-006](Regras-de-Neg%C3%B3cio#RN-006), [RN-007](Regras-de-Neg%C3%B3cio#RN-007), [RN-008](Regras-de-Neg%C3%B3cio#RN-008). |
| Rastreabilidade | [Linha TM-HU-002](Matriz-de-Rastreabilidade#TM-HU-002). |
| Tipo de relação | `<<extend>>` de [UC-001](#UC-001), no ponto "escolher lista de populares". |
| Condição de extensão | O visitante escolhe consultar os locais mais visitados. |

**Fluxo principal**

1. O visitante escolhe a opção "populares" na exploração.
2. O sistema ordena os locais por visitação/interações, avaliações e recência.
3. O sistema exibe a lista ordenada.
4. O visitante seleciona um item para consultar detalhes.

**Fluxos de exceção**

- E1 — Catálogo indisponível: o sistema informa a falha sem expor detalhes técnicos e orienta nova tentativa.

---

### <a id="UC-003"></a>UC-003 — Consultar locais pouco divulgados

| Campo | Especificação |
|-------|---------------|
| Objetivo | Explorar a região além das opções mais conhecidas, descobrindo localidades pouco divulgadas. |
| Prioridade | Should have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Catálogo disponível. |
| Pós-condições | Lista de locais pouco divulgados é exibida. |
| HU | [HU-003](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-003). |
| RF | [RF-003](Requisitos-Funcionais#RF-003). |
| RN | [RN-006](Regras-de-Neg%C3%B3cio#RN-006), [RN-007](Regras-de-Neg%C3%B3cio#RN-007), [RN-008](Regras-de-Neg%C3%B3cio#RN-008), [RN-077](Regras-de-Neg%C3%B3cio#RN-077), [RN-010](Regras-de-Neg%C3%B3cio#RN-010). |
| Rastreabilidade | [Linha TM-HU-003](Matriz-de-Rastreabilidade#TM-HU-003). |
| Tipo de relação | `<<extend>>` de [UC-001](#UC-001), no ponto "escolher lista de pouco divulgados". |
| Condição de extensão | O visitante escolhe consultar locais pouco divulgados. |

**Fluxo principal**

1. O visitante escolhe a opção "pouco divulgados" na exploração.
2. O sistema aplica o critério de avaliação (RN-077) e visitas para identificar locais elegíveis.
3. O sistema exibe a lista.
4. O visitante seleciona um item para consultar detalhes.

**Fluxos de exceção**

- E1 — Catálogo indisponível: o sistema informa a falha sem expor detalhes técnicos e orienta nova tentativa.

---

### <a id="UC-004"></a>UC-004 — Pesquisar locais e eventos por termo

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar locais e eventos por palavras-chave, nome, categoria ou cidade, recebendo orientações claras com sugestões alternativas quando não houver resultado. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Registros pesquisáveis contêm os dados mínimos. |
| Pós-condições | Resultados da pesquisa ou alternativas de busca são apresentados. |
| HU | [HU-004](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-004). |
| RF | [RF-004](Requisitos-Funcionais#RF-004), [RF-005](Requisitos-Funcionais#RF-005). |
| RN | [RN-003](Regras-de-Neg%C3%B3cio#RN-003), [RN-009](Regras-de-Neg%C3%B3cio#RN-009), [RN-010](Regras-de-Neg%C3%B3cio#RN-010). |
| Rastreabilidade | [Linha TM-HU-004](Matriz-de-Rastreabilidade#TM-HU-004). |
| Tipo de relação | `<<include>>` de [UC-069](#UC-069) (validar parâmetros de busca). |
| Pontos de extensão | [UC-070](#UC-070) (busca por proximidade) estende este caso quando o visitante opta por ordenar os resultados por proximidade. |

**Fluxo principal**

1. O visitante informa um termo de busca.
2. O sistema executa [UC-069](#UC-069) para validar o parâmetro informado.
3. O sistema pesquisa nome, palavras-chave, categoria e cidade.
4. O sistema exibe os resultados encontrados.
5. O visitante seleciona um resultado.

**Fluxos alternativos**

- A1 — Sem resultado exato: o sistema sugere correções, categorias próximas ou outra cidade.

**Fluxos de exceção**

- E1 — Falha de consulta: o sistema informa a situação e uma próxima ação.

---

### <a id="UC-005"></a>UC-005 — Filtrar locais e eventos por categoria e público

| Campo | Especificação |
|-------|---------------|
| Objetivo | Filtrar locais e eventos por categoria e adequação ao público, incluindo opções para crianças e família, para escolher destinos compatíveis com a necessidade do visitante. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Registros pesquisáveis contêm os dados mínimos. |
| Pós-condições | Resultados filtrados são apresentados, com os filtros aplicados explícitos. |
| HU | [HU-005](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-005). |
| RF | [RF-006](Requisitos-Funcionais#RF-006). |
| RN | [RN-004](Regras-de-Neg%C3%B3cio#RN-004), [RN-005](Regras-de-Neg%C3%B3cio#RN-005). |
| Rastreabilidade | [Linha TM-HU-005](Matriz-de-Rastreabilidade#TM-HU-005). |
| Tipo de relação | `<<include>>` de [UC-069](#UC-069) (validar parâmetros de busca). |
| Pontos de extensão | [UC-070](#UC-070) (busca por proximidade) estende este caso quando o visitante opta por ordenar os resultados por proximidade. |

**Fluxo principal**

1. O visitante escolhe categoria e/ou perfil de público.
2. O sistema executa [UC-069](#UC-069) para validar os valores informados.
3. O sistema aplica os filtros sobre o catálogo.
4. O sistema exibe os resultados e os filtros aplicados.

**Fluxos alternativos**

- A1 — O visitante altera ou remove filtros, assim a pesquisa é refeita com os filtros atualizados.

**Fluxos de exceção**

- E1 — Valor de filtro inválido: o sistema oferece apenas valores aprovados (tratamento detalhado em [UC-069](#UC-069)).

---

## Épico 2: Informações e Detalhes do Local

### <a id="UC-006"></a>UC-006 — Consultar perfil do local

| Campo | Especificação |
|-------|---------------|
| Objetivo | Avaliar se um local atende à necessidade da visita, consultando em um único perfil suas características de ambiente, funcionamento, custos, regras, segurança e adequação de público. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Local publicado e visível, atendendo às condições de publicação (RN-068). |
| Pós-condições | Perfil do local é exibido com fonte e data de verificação nos dados sensíveis à atualização; o visitante pode aprofundar em localização, agenda ou contato. |
| HU | [HU-006](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-006), [HU-007](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-007), [HU-008](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-008), [HU-010](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-010), [HU-012](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-012), [HU-013](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-013), [HU-019](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-019), [HU-020](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-020). |
| RF | [RF-007](Requisitos-Funcionais#RF-007), [RF-008](Requisitos-Funcionais#RF-008), [RF-009](Requisitos-Funcionais#RF-009), [RF-010](Requisitos-Funcionais#RF-010), [RF-012](Requisitos-Funcionais#RF-012), [RF-014](Requisitos-Funcionais#RF-014), [RF-015](Requisitos-Funcionais#RF-015), [RF-019](Requisitos-Funcionais#RF-019), [RF-020](Requisitos-Funcionais#RF-020), [RF-036](Requisitos-Funcionais#RF-036). |
| RN | [RN-011](Regras-de-Neg%C3%B3cio#RN-011), [RN-012](Regras-de-Neg%C3%B3cio#RN-012), [RN-013](Regras-de-Neg%C3%B3cio#RN-013), [RN-014](Regras-de-Neg%C3%B3cio#RN-014), [RN-015](Regras-de-Neg%C3%B3cio#RN-015), [RN-016](Regras-de-Neg%C3%B3cio#RN-016), [RN-017](Regras-de-Neg%C3%B3cio#RN-017), [RN-018](Regras-de-Neg%C3%B3cio#RN-018), [RN-019](Regras-de-Neg%C3%B3cio#RN-019), [RN-021](Regras-de-Neg%C3%B3cio#RN-021), [RN-027](Regras-de-Neg%C3%B3cio#RN-027), [RN-028](Regras-de-Neg%C3%B3cio#RN-028), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [TM-HU-006](Matriz-de-Rastreabilidade#TM-HU-006), [TM-HU-007](Matriz-de-Rastreabilidade#TM-HU-007), [TM-HU-008](Matriz-de-Rastreabilidade#TM-HU-008), [TM-HU-010](Matriz-de-Rastreabilidade#TM-HU-010), [TM-HU-012](Matriz-de-Rastreabilidade#TM-HU-012), [TM-HU-013](Matriz-de-Rastreabilidade#TM-HU-013), [TM-HU-019](Matriz-de-Rastreabilidade#TM-HU-019), [TM-HU-020](Matriz-de-Rastreabilidade#TM-HU-020). |
| Tipo de relação | Inclui [UC-071](#UC-071) — a procedência é apurada uma única vez para o conjunto de dados sensíveis do perfil. |
| Pontos de extensão | [UC-080](#UC-080) (sinalizar dado incorreto) e [UC-033](#UC-033) (compartilhar) estendem este caso. |

**Fluxo principal**

1. O visitante abre a página de um local a partir do catálogo, da busca ou de um resultado filtrado.
2. O sistema verifica se o cadastro atende às condições de publicação (RN-068).
3. O sistema inclui [UC-071](#UC-071) para identificar fonte e data da última verificação dos dados sensíveis à atualização exibidos no perfil.
4. O sistema apresenta o perfil consolidado do local, contendo:
   - descrição, categoria, tipo de experiência e características do ambiente (RN-068);
   - fotos e mídias reais vinculadas ao local (RN-014, RN-015, RN-016);
   - horários de funcionamento e status atual, aberto ou fechado (RN-013, RN-021);
   - cardápio ou descrição de produtos, faixa de preços, taxas e couvert artístico quando aplicável (RN-011, RN-028);
   - formato de atendimento do estabelecimento (RN-011, RN-028);
   - regras e políticas do local: itens permitidos e proibidos, restrições de entrada e condições especiais (RN-027);
   - informações de segurança do local (RN-019);
   - recursos de acessibilidade (RN-017);
   - indicação de adequação ao público infantil (RN-018).
5. O visitante navega pelo perfil, navegando entre as imagens ou expandindo as seções de interesse.

**Fluxos alternativos**

- A1 — Feriado ou horário especial cadastrado: o status de funcionamento passa a refletir a programação excepcional em vez do horário regular.
- A2 — O visitante identifica um dado incorreto: aciona a extensão [UC-080](#UC-080), sem precisar publicar uma avaliação.
- A3 — O visitante deseja compartilhar o local: aciona a extensão [UC-033](#UC-033).
- A4 — O visitante quer aprofundar em deslocamento, agenda ou contato: segue para [UC-007](#UC-007), [UC-009](#UC-009) ou [UC-010](#UC-010).

**Fluxos de exceção**

- E1 — Cadastro não atende aos dados mínimos exigidos para o tipo de local: o local não é publicado e o perfil não é exibido (RN-068).
- E2 — Dado sensível desatualizado ou ainda não verificado: o sistema sinaliza a limitação sem ocultar a informação, conforme [UC-071](#UC-071).
- E3 — Uma mídia não pode ser carregada: as demais mídias e o conteúdo textual do perfil permanecem disponíveis.

---

### <a id="UC-007"></a>UC-007 — Consultar localização, acesso e opções de transporte

| Campo | Especificação |
|-------|---------------|
| Objetivo | Planejar o deslocamento e aproveitar melhor o passeio, conhecendo localização, perfil do bairro, trajeto, formas de acesso, transporte, distância a pé e estabelecimentos próximos. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de Mapas e Transportes. |
| Pré-condições | Local publicado e visível. |
| Pós-condições | Localização, trajeto, formas de acesso, opções de transporte, distância a pé e estabelecimentos próximos são exibidos. |
| HU | [HU-009](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-009). |
| RF | [RF-011](Requisitos-Funcionais#RF-011). |
| RN | [RN-012](Regras-de-Neg%C3%B3cio#RN-012). |
| Rastreabilidade | [Linha TM-HU-009](Matriz-de-Rastreabilidade#TM-HU-009). |
| Tipo de relação | `<<include>>` de [UC-071](#UC-071). |
| Pontos de extensão | [UC-080](#UC-080) e [UC-033](#UC-033) estendem este caso. |

**Fluxo principal**

1. O visitante abre a página de um local.
2. O sistema busca as informações necessárias para exibir sobre o local.
3. O sistema executa [UC-071](#UC-071) para identificar a fonte e a data da última verificação.
4. O sistema apresenta localização, perfil do bairro, formas de acesso e distância a pé.
5. O sistema consulta o Serviço de Mapas e Transportes para calcular trajeto e opções de transporte.
5. O visitante pode abrir o trajeto no serviço externo.

**Fluxos alternativos**

- A1 — Trajeto oficial disponível: o sistema abre o serviço externo após a ação do visitante.

**Fluxos de exceção**

- E1 — Serviço externo indisponível: os dados locais permanecem visíveis e o sistema informa que o trajeto não pôde ser aberto.

---

### <a id="UC-009"></a>UC-009 — Consultar calendário e programação de eventos

| Campo | Especificação |
|-------|---------------|
| Objetivo | Planejar a participação em eventos, consultando calendário, programação musical, data, horário, local e descrição. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Conteúdo publicado e vínculo com local ativo. |
| Pós-condições | Programação escolhida é exibida. |
| HU | [HU-014](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-014). |
| RF | [RF-016](Requisitos-Funcionais#RF-016). |
| RN | [RN-012](Regras-de-Neg%C3%B3cio#RN-012). |
| Rastreabilidade | [Linha TM-HU-014](Matriz-de-Rastreabilidade#TM-HU-014). |
| Tipo de relação | `<<include>>` de [UC-071](#UC-071). |
| Pontos de extensão | [UC-072](#UC-072) (filtrar agenda por data e ciclo de vida) estende este caso; [UC-080](#UC-080) e [UC-033](#UC-033) também estendem este caso. |

**Fluxo principal**

1. O visitante abre a agenda de um local ou evento.
2. O sistema lista os eventos e a programação pública.
3. O visitante escolhe um item.
4. O sistema executa [UC-071](#UC-071) para identificar a fonte e a data da última verificação.
5. O sistema exibe descrição, data, horário, local e programação musical associada.

**Fluxos de exceção**

- E1 — Vínculo do conteúdo com o local deixou de ser válido: o conteúdo não é exibido.

---

### <a id="UC-010"></a>UC-010 — Acessar canais de contato e redes sociais

| Campo | Especificação |
|-------|---------------|
| Objetivo | Confirmar informações diretamente com o estabelecimento e acompanhar suas atualizações, acessando canais de contato e perfis públicos de redes sociais. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Local publicado e visível; ao menos um canal de contato ou perfil de rede social cadastrado. |
| Pós-condições | Canais de contato e links de redes sociais são exibidos e o canal escolhido é aberto externamente após ação do visitante. |
| HU | [HU-015](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-015), [HU-017](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-017). |
| RF | [RF-017](Requisitos-Funcionais#RF-017), [RF-035](Requisitos-Funcionais#RF-035). |
| RN | [RN-024](Regras-de-Neg%C3%B3cio#RN-024). |
| Rastreabilidade | [TM-HU-015](Matriz-de-Rastreabilidade#TM-HU-015), [TM-HU-017](Matriz-de-Rastreabilidade#TM-HU-017). |
| Tipo de relação | Inclui [UC-071](#UC-071) — contatos e perfis oficiais são dados sensíveis à atualização. |
| Pontos de extensão | [UC-080](#UC-080) e [UC-033](#UC-033) estendem este caso. |

**Fluxo principal**

1. O visitante abre os canais de contato de um local.
2. O sistema inclui [UC-071](#UC-071) para identificar fonte e data da última verificação dos canais.
3. O sistema apresenta os canais de contato cadastrados e os links de perfis públicos em redes sociais.
4. O visitante seleciona um canal.
5. O sistema encaminha para o serviço externo somente após a ação do visitante.

**Fluxos de exceção**

- E1 — O local não possui canal ou perfil público cadastrado: o sistema informa a ausência sem apresentar link inexistente.
- E2 — Canal indisponível: o sistema informa a situação sem garantir a disponibilidade externa e sem expor detalhes técnicos.

---

## Épico 3: Avaliações e Comunidade

### <a id="UC-012"></a>UC-012 — Consultar avaliações da comunidade

| Campo | Especificação |
|-------|---------------|
| Objetivo | Reduzir incertezas antes da visita, consultando avaliações de outros usuários sobre o local. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Local público; avaliações aprovadas disponíveis. |
| Pós-condições | Avaliações são exibidas na ordenação escolhida pelo visitante. |
| HU | [HU-021](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-021). |
| RF | [RF-021](Requisitos-Funcionais#RF-021). |
| RN | [RN-007](Regras-de-Neg%C3%B3cio#RN-007), [RN-022](Regras-de-Neg%C3%B3cio#RN-022), [RN-029](Regras-de-Neg%C3%B3cio#RN-029), [RN-030](Regras-de-Neg%C3%B3cio#RN-030), [RN-031](Regras-de-Neg%C3%B3cio#RN-031), [RN-032](Regras-de-Neg%C3%B3cio#RN-032), [RN-037](Regras-de-Neg%C3%B3cio#RN-037), [RN-038](Regras-de-Neg%C3%B3cio#RN-038). |
| Rastreabilidade | [Linha TM-HU-021](Matriz-de-Rastreabilidade#TM-HU-021). |
| Pontos de extensão | [UC-051](#UC-051), ao marcar uma avaliação como útil; [UC-052](#UC-052), ao compartilhar uma avaliação individual; [UC-031](#UC-031), quando existe mídia comunitária vinculada ao local. |

**Fluxo principal**

1. O visitante abre a área de avaliações de um local.
2. O sistema mostra avaliações aprovadas com autoria, nota e data.
3. O visitante ordena as avaliações por recência ou relevância.
4. O sistema exibe o conteúdo ordenado e permite abrir cada avaliação individualmente.

**Fluxos alternativos**

- A1 — Não há avaliações publicadas: o sistema informa a ausência de conteúdo sem fabricar nota.
- A2 — Uma avaliação foi denunciada: ela permanece visível ou é preventivamente ocultada conforme a gravidade da denúncia.

**Fluxos de exceção**

- E1 — Mídia anexada a uma avaliação não pode ser carregada: o texto da avaliação continua disponível.

---

### <a id="UC-013"></a>UC-013 — Publicar avaliação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Contribuir com a comunidade publicando avaliações e comentários sobre locais visitados. |
| Prioridade | Must have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; local existente. |
| Pós-condições | Avaliação é enviada para publicação ou moderação e vinculada ao autor. |
| HU | [HU-022](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-022). |
| RF | [RF-022](Requisitos-Funcionais#RF-022). |
| RN | [RN-030](Regras-de-Neg%C3%B3cio#RN-030), [RN-033](Regras-de-Neg%C3%B3cio#RN-033), [RN-035](Regras-de-Neg%C3%B3cio#RN-035), [RN-036](Regras-de-Neg%C3%B3cio#RN-036), [RN-037](Regras-de-Neg%C3%B3cio#RN-037). |
| Rastreabilidade | [Linha TM-HU-022](Matriz-de-Rastreabilidade#TM-HU-022). |
| Pontos de extensão | [UC-073](Matriz-de-Rastreabilidade#TM-HU-081), quando a sessão expira durante o preenchimento da avaliação. |

**Fluxo principal**

1. O usuário abre o formulário de avaliação do local.
2. Informa nota, comentário e, opcionalmente, contexto e mídias.
3. O sistema valida formato e vínculo do conteúdo enviado.
4. O usuário confirma o envio.
5. O sistema associa a avaliação ao perfil do autor e a publica ou encaminha à moderação.

**Fluxos alternativos**

- A1 — A avaliação contém mídia: o envio de arquivo segue as validações descritas em [UC-031](#UC-031).
- A2 — O usuário também percebe um dado cadastral incorreto no mesmo local: essa ação é tratada separadamente pelo caso de sinalização de dado incorreto (UC-080, fora deste escopo), preservando a avaliação já preenchida.

**Fluxos de exceção**

- E1 — Conteúdo viola regra grave: o sistema rejeita ou oculta a avaliação e informa o motivo aplicável.
- E2 — Sessão expira durante o preenchimento: o caso aciona a extensão [UC-073](Matriz-de-Rastreabilidade#TM-HU-081), que preserva o conteúdo já preenchido e solicita nova autenticação antes de restaurá-lo.

---

## Épico 4: Recomendações Personalizadas

- Como saber se o usuário visitou um local ou não? Perguntar se ele realizou a visita? Presumir interesse já que o usuário entou no perfil

## Épico 4: Recomendações Personalizadas

### <a id="UC-014"></a>UC-014 — Receber recomendações por interesse demonstrado

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar locais semelhantes aos que o usuário demonstrou interesse, a partir do histórico de acessos a perfis de locais na plataforma. |
| Prioridade | Should have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; consentimento explícito para uso do histórico de navegação/interesse para fins de recomendação. |
| Pós-condições | Recomendações relacionadas aos interesses demonstrados são exibidas, identificadas como baseadas em interesse — não em visita confirmada —, sem revelar dados de terceiros. |
| HU | [HU-023](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-023). |
| RF | [RF-023](Requisitos-Funcionais#RF-023). |
| RN | [RN-039](Regras-de-Neg%C3%B3cio#RN-039) |
| Rastreabilidade | [Linha TM-HU-023](Matriz-de-Rastreabilidade#TM-HU-023). |
| Pontos de extensão | [UC-074](Matriz-de-Rastreabilidade#TM-HU-082), quando os dados de interesse são insuficientes para personalizar. |

**Fluxo principal**

1. O usuário acessa as recomendações baseadas em interesse.
2. O sistema considera o histórico de acessos a perfis de locais, registrado e autorizado pelo usuário.
3. O sistema calcula a compatibilidade com locais ainda não acessados, excluindo dados inválidos, moderados ou fora da janela de relevância temporal.
4. O sistema exibe os locais recomendados, sinalizando de forma clara que a recomendação é baseada em interesse demonstrado.

**Fluxos de exceção**

- E1 — O usuário não autorizou o uso do histórico de navegação: esse histórico é ignorado e o caso aciona a alternativa especificada em [UC-074](Matriz-de-Rastreabilidade#TM-HU-082).
- E2 — Volume de interações insuficiente para gerar recomendação confiável: o sistema aciona [UC-074](Matriz-de-Rastreabilidade#TM-HU-082) por dados insuficientes.

---

### <a id="UC-015"></a>UC-015 — Receber recomendações por avaliações realizadas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Encontrar opções compatíveis com as preferências reveladas pelas avaliações realizadas pelo usuário. |
| Prioridade | Should have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; usuário com avaliações publicadas. |
| Pós-condições | Recomendações justificáveis pelas avaliações são exibidas. |
| HU | [HU-024](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-024). |
| RF | [RF-024](Requisitos-Funcionais#RF-024). |
| RN | [RN-040](Regras-de-Neg%C3%B3cio#RN-040), [RN-041](Regras-de-Neg%C3%B3cio#RN-041). |
| Rastreabilidade | [Linha TM-HU-024](Matriz-de-Rastreabilidade#TM-HU-024). |
| Pontos de extensão | [UC-074](Matriz-de-Rastreabilidade#TM-HU-082), quando as avaliações disponíveis são insuficientes para personalizar. |

**Fluxo principal**

1. O usuário acessa as recomendações baseadas em avaliações.
2. O sistema considera as avaliações válidas publicadas pelo usuário.
3. O sistema calcula a compatibilidade e exclui avaliações inválidas ou moderadas.
4. O sistema exibe os locais recomendados com base nas preferências reveladas pelas avaliações.

**Fluxos de exceção**

- E1 — O usuário não possui avaliações suficientes: o caso aciona a alternativa especificada em [UC-074](Matriz-de-Rastreabilidade#TM-HU-082).

---

### <a id="UC-016"></a>UC-016 — Receber recomendações por perfis similares

| Campo | Especificação |
|-------|---------------|
| Objetivo | Descobrir locais de interesse a partir de usuários com perfis semelhantes ao do usuário. |
| Prioridade | Could have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; base de usuários suficiente para comparação de perfis. |
| Pós-condições | Recomendações por perfis compatíveis são exibidas sem revelar identidade ou histórico de terceiros. |
| HU | [HU-025](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-025). |
| RF | [RF-025](Requisitos-Funcionais#RF-025). |
| RN | [RN-042](Regras-de-Neg%C3%B3cio#RN-042). |
| Rastreabilidade | [Linha TM-HU-025](Matriz-de-Rastreabilidade#TM-HU-025). |
| Pontos de extensão | [UC-074](Matriz-de-Rastreabilidade#TM-HU-082), quando não há massa de usuários suficiente para personalizar. |

**Fluxo principal**

1. O usuário acessa as recomendações baseadas em perfis similares.
2. O sistema identifica usuários com interesses semelhantes por filtragem colaborativa.
3. O sistema agrega os resultados sem revelar identidade ou histórico individual de terceiros.
4. O sistema exibe os locais recomendados com base nos perfis compatíveis.

**Fluxos alternativos**

- A1 — Filtragem colaborativa: resultados agregados são usados sem revelar identidade ou histórico alheio.

**Fluxos de exceção**

- E1 — Massa de usuários insuficiente para comparação de perfis: o caso aciona a alternativa especificada em [UC-074](Matriz-de-Rastreabilidade#TM-HU-082).

---

### <a id="UC-017"></a>UC-017 — Gerar roteiro personalizado

| Campo | Especificação |
|-------|---------------|
| Objetivo | Planejar passeios ordenados de acordo com os interesses e restrições práticas do usuário. |
| Prioridade | Must have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Serviço de Mapas e Transportes. |
| Pré-condições | Sessão válida; preferências informadas; catálogo com locais elegíveis. |
| Pós-condições | Roteiro é exibido e, por inclusão do UC-075, persistido para permitir ajustes posteriores. |
| HU | [HU-026](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-026). |
| RF | [RF-026](Requisitos-Funcionais#RF-026). |
| RN | [RN-043](Regras-de-Neg%C3%B3cio#RN-043), [RN-044](Regras-de-Neg%C3%B3cio#RN-044), [RN-052](Regras-de-Neg%C3%B3cio#RN-052), [RN-053](Regras-de-Neg%C3%B3cio#RN-053). |
| Rastreabilidade | [Linha TM-HU-026](Matriz-de-Rastreabilidade#TM-HU-026). |
| Tipo de relação | `<<include>>` de UC-075 — o roteiro gerado é sempre persistido e recalculável. |

**Fluxo principal**

1. O usuário informa interesses, período, origem e perfil do público.
2. O sistema seleciona locais públicos com dados mínimos completos.
3. O sistema considera distância, horários e status, apoiado pelo serviço de mapas e transportes.
4. O sistema gera uma sequência de passeio ordenada.
5. O sistema inclui o UC-075 para persistir o roteiro e permitir seu ajuste posterior pelo usuário.

**Fluxos alternativos**

- A1 — O serviço de mapas e transportes não retorna dados de deslocamento para um trecho: o sistema mantém o roteiro com distâncias estimadas e sinaliza a limitação.

**Fluxos de exceção**

- E1 — Não há combinação viável de locais para os critérios informados: o sistema explica as restrições identificadas e sugere flexibilizações antes de acionar o UC-075.

---

## Épico 5: Organização Pessoal e Roteiros

### <a id="UC-018"></a>UC-018 — Gerenciar listas de locais desejados

| Campo | Especificação |
|-------|---------------|
| Objetivo | Organizar futuros passeios na região por meio de listas pessoais de locais desejados. |
| Prioridade | Must have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida. |
| Pós-condições | Lista do proprietário é criada, atualizada ou excluída conforme a operação. |
| HU | [HU-027](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-027). |
| RF | [RF-027](Requisitos-Funcionais#RF-027). |
| RN | [RN-045](Regras-de-Neg%C3%B3cio#RN-045), [RN-046](Regras-de-Neg%C3%B3cio#RN-046). |
| Rastreabilidade | [Linha TM-HU-027](Matriz-de-Rastreabilidade#TM-HU-027). |

**Fluxo principal**

1. O usuário cria uma lista e informa o nome.
2. Adiciona, remove ou reordena locais na lista.
3. O sistema valida a propriedade da lista.
4. O sistema salva a lista atualizada.

**Fluxos alternativos**

- A1 — O usuário edita ou exclui uma lista própria já existente.

**Fluxos de exceção**

- E1 — Tentativa de alterar lista de terceiro: o sistema nega a operação.

---

### <a id="UC-019"></a>UC-019 — Registrar locais visitados (Histórico Pessoal)

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar, de forma pessoal e privada, experiências já vividas na região, marcando locais como visitados. |
| Prioridade | Should have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; local existente. |
| Pós-condições | Histórico pessoal é criado, alterado ou removido, visível apenas ao próprio usuário, sem alterar o cadastro público do local. |
| HU | [HU-028](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-028). |
| RF | [RF-028](Requisitos-Funcionais#RF-028). |
| RN | [RN-047](Regras-de-Neg%C3%B3cio#RN-047), [RN-048](Regras-de-Neg%C3%B3cio#RN-048), [RN-049](Regras-de-Neg%C3%B3cio#RN-049). |
| Rastreabilidade | [Linha TM-HU-028](Matriz-de-Rastreabilidade#TM-HU-028). |

**Fluxo principal**

1. O usuário marca um local como visitado.
2. Opcionalmente informa data e observação sobre a visita.
3. O sistema vincula o registro ao usuário autenticado.
4. O sistema confirma a atualização do histórico pessoal.

**Fluxos alternativos**

- A1 — O proprietário do registro edita ou remove a marcação de visitado.

**Fluxos de exceção**

- E1 — Tentativa de acessar histórico alheio: o sistema nega o acesso.

---

### <a id="UC-020"></a>UC-020 — Usar checklist de atividades e passeios

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acompanhar atividades e passeios já realizados por meio de checklists pessoais. |
| Prioridade | Must have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; checklist ou roteiro selecionado. |
| Pós-condições | Progresso pessoal do checklist é atualizado. |
| HU | [HU-029](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-029). |
| RF | [RF-029](Requisitos-Funcionais#RF-029). |
| RN | [RN-050](Regras-de-Neg%C3%B3cio#RN-050), [RN-051](Regras-de-Neg%C3%B3cio#RN-051). |
| Rastreabilidade | [Linha TM-HU-029](Matriz-de-Rastreabilidade#TM-HU-029). |
| Pontos de extensão | [UC-076](Matriz-de-Rastreabilidade#TM-HU-084), quando um item está vinculado a atração inativa; [UC-055](Matriz-de-Rastreabilidade#TM-HU-063), quando há dica curada disponível para o local do item. |

**Fluxo principal**

1. O usuário abre um checklist pessoal.
2. Adiciona itens ou marca/desmarca uma atividade como concluída.
3. O sistema salva o progresso pessoal do checklist.

**Fluxos alternativos**

- A1 — O checklist é criado a partir de um roteiro personalizado gerado no [UC-017](#UC-017).

**Fluxos de exceção**

- E1 — Falha ao salvar o progresso do checklist: o sistema mantém o último estado válido e orienta nova tentativa.

---

## Épico 6: Assistente Virtual (Chatbot)

### <a id="UC-021"></a>UC-021 — Consultar o assistente virtual

| Campo | Especificação |
|-------|---------------|
| Objetivo | Obter respostas sobre locais e eventos em linguagem natural, sem sair da plataforma. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível. |
| Pós-condições | Resposta textual pertinente é apresentada ao visitante. |
| HU | [HU-030](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-030). |
| RF | [RF-030](Requisitos-Funcionais#RF-030). |
| RN | [RN-054](Regras-de-Neg%C3%B3cio#RN-054), [RN-055](Regras-de-Neg%C3%B3cio#RN-055). |
| Rastreabilidade | [Linha TM-HU-030](Matriz-de-Rastreabilidade#TM-HU-030). |
| Pontos de extensão | [UC-022](#UC-022), na interpretação de intenção; [UC-023](#UC-023), quando a informação é insuficiente; [UC-024](#UC-024), quando acionado a partir de uma página de local/evento; [UC-026](#UC-026), ao solicitar links de redes sociais; [UC-027](#UC-027), ao solicitar imagens do local; [UC-028](#UC-028), ao enviar a pergunta por áudio. |

**Fluxo principal**

1. O visitante abre o assistente e envia uma pergunta textual.
2. O sistema prioriza informações do catálogo regional relacionadas à pergunta.
3. O sistema retorna uma resposta textual pertinente, com links internos úteis quando aplicável.

**Fluxos de exceção**

- E1 — Fontes conflitantes ou desatualizadas sustentam a resposta: o sistema não afirma certeza e identifica a limitação ao visitante.

---

### <a id="UC-022"></a>UC-022 — Receber resposta interpretada por intenção

| Campo | Especificação |
|-------|---------------|
| Objetivo | Obter respostas mais relevantes por meio da interpretação da intenção da pergunta enviada ao assistente. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível; pergunta enviada no UC-021. |
| Pós-condições | Resposta considera a intenção identificada e o contexto atual da consulta. |
| HU | [HU-031](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-031). |
| RF | [RF-031](Requisitos-Funcionais#RF-031). |
| RN | [RN-054](Regras-de-Neg%C3%B3cio#RN-054), [RN-055](Regras-de-Neg%C3%B3cio#RN-055). |
| Rastreabilidade | [Linha TM-HU-031](Matriz-de-Rastreabilidade#TM-HU-031). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | Toda pergunta enviada ao assistente passa por interpretação de intenção antes da resposta. |

**Fluxo principal**

1. O sistema recebe a pergunta enviada no [UC-021](#UC-021).
2. O sistema interpreta a intenção subjacente à pergunta e o contexto atual da consulta.
3. O sistema seleciona as informações mais pertinentes à intenção identificada.
4. O sistema retorna a resposta interpretada ao visitante.

**Fluxos de exceção**

- E1 — A intenção não é identificada com confiança suficiente: o caso aciona a orientação alternativa especificada em [UC-023](#UC-023).

---

### <a id="UC-023"></a>UC-023 — Receber orientação alternativa do assistente

| Campo | Especificação |
|-------|---------------|
| Objetivo | Continuar a busca por informações mesmo quando o assistente não obtém uma resposta satisfatória. |
| Prioridade | Should have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível; consulta em andamento sem resposta satisfatória. |
| Pós-condições | Visitante recebe orientação alternativa para continuar a busca. |
| HU | [HU-032](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-032). |
| RF | [RF-032](Requisitos-Funcionais#RF-032). |
| RN | [RN-056](Regras-de-Neg%C3%B3cio#RN-056). |
| Rastreabilidade | [Linha TM-HU-032](Matriz-de-Rastreabilidade#TM-HU-032). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | A pergunta enviada não obtém resposta satisfatória do assistente. |

**Fluxo principal**

1. O sistema identifica que não possui informação suficiente para responder com confiança.
2. O sistema explicita a limitação ao visitante.
3. O sistema sugere buscas, categorias ou canais oficiais alternativos.

**Fluxos de exceção**

- E1 — Nenhuma alternativa aplicável está disponível: o sistema orienta o visitante a usar a busca geral do catálogo.

---

### <a id="UC-024"></a>UC-024 — Acionar o assistente com contexto da tela

| Campo | Especificação |
|-------|---------------|
| Objetivo | Aprofundar a pesquisa em andamento acionando o assistente com o contexto da tela atual. |
| Prioridade | Should have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível; visitante em uma página de local ou evento. |
| Pós-condições | Consulta ao assistente é iniciada já com o contexto herdado da tela de origem. |
| HU | [HU-033](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-033). |
| RF | [RF-033](Requisitos-Funcionais#RF-033). |
| RN | [RN-057](Regras-de-Neg%C3%B3cio#RN-057). |
| Rastreabilidade | [Linha TM-HU-033](Matriz-de-Rastreabilidade#TM-HU-033). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | O visitante aciona o assistente a partir de uma página de local ou evento. |

**Fluxo principal**

1. O visitante aciona o assistente a partir da página de um local ou evento.
2. O sistema usa esse item como contexto inicial da consulta.
3. O visitante complementa a pergunta, se necessário.
4. O sistema responde considerando o contexto herdado da tela de origem.

**Fluxos de exceção**

- E1 — O contexto da tela não pôde ser recuperado: o sistema inicia a consulta sem contexto pré-carregado e solicita que o visitante informe o local de interesse.

---

### <a id="UC-025"></a>UC-025 — Consultar dados atualizados por fonte externa

| Campo | Especificação |
|-------|---------------|
| Objetivo | Planejar atividades com base em dados recentes e confiáveis sobre locais e eventos. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Fonte de dados externa. |
| Pré-condições | Módulo de importação/atualização configurado com uma fonte de dados externa. |
| Pós-condições | Informações apresentadas ao visitante refletem os dados mais recentes disponíveis. |
| HU | [HU-034](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-034). |
| RF | [RF-034](Requisitos-Funcionais#RF-034). |
| RN | [RN-058](Regras-de-Neg%C3%B3cio#RN-058). |
| Rastreabilidade | [Linha TM-HU-034](Matriz-de-Rastreabilidade#TM-HU-034). |

**Fluxo principal**

1. O visitante consulta o assistente ou uma página de local/evento sobre informações recentes.
2. O sistema verifica a atualidade dos dados armazenados.
3. Quando necessário, o sistema importa ou atualiza os dados a partir da fonte de dados externa configurada.
4. O sistema apresenta as informações atualizadas ao visitante.

**Fluxos de exceção**

- E1 — A fonte de dados externa está indisponível ou retorna dado inconsistente: o sistema mantém os últimos dados válidos e sinaliza que podem estar desatualizados.

---

### <a id="UC-026"></a>UC-026 — Receber links de redes sociais pelo assistente

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acompanhar atualizações dos locais de interesse por meio de seus links de redes sociais, recebidos pelo assistente. |
| Prioridade | Must have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível; local em contexto na conversa. |
| Pós-condições | Links externos de perfis públicos do local são apresentados ao visitante. |
| HU | [HU-035](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-035). |
| RF | [RF-035](Requisitos-Funcionais#RF-035). |
| RN | [RN-024](Regras-de-Neg%C3%B3cio#RN-024). |
| Rastreabilidade | [Linha TM-HU-035](Matriz-de-Rastreabilidade#TM-HU-035). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | O visitante solicita links de redes sociais de um local ou evento durante a conversa com o assistente. |

**Fluxo principal**

1. O visitante pergunta ao assistente pelas redes sociais de um local ou evento.
2. O sistema identifica o local/evento em contexto na conversa.
3. O sistema retorna os links externos de perfis públicos disponíveis.

**Fluxos de exceção**

- E1 — O local não possui perfil público cadastrado: o sistema informa a ausência sem apresentar um link inexistente.

---

### <a id="UC-027"></a>UC-027 — Receber imagens do local pelo assistente

| Campo | Especificação |
|-------|---------------|
| Objetivo | Visualizar imagens do local de interesse diretamente na conversa com o assistente, sem consultar sites externos. |
| Prioridade | Should have. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Assistente disponível; local em contexto na conversa. |
| Pós-condições | Imagens disponíveis do local são apresentadas ao visitante na própria conversa. |
| HU | [HU-036](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-036). |
| RF | [RF-036](Requisitos-Funcionais#RF-036). |
| RN | [RN-014](Regras-de-Neg%C3%B3cio#RN-014), [RN-015](Regras-de-Neg%C3%B3cio#RN-015), [RN-016](Regras-de-Neg%C3%B3cio#RN-016). |
| Rastreabilidade | [Linha TM-HU-036](Matriz-de-Rastreabilidade#TM-HU-036). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | O visitante solicita imagens de um local ou evento durante a conversa com o assistente. |

**Fluxo principal**

1. O visitante pergunta ao assistente por imagens do local que pretende visitar.
2. O sistema identifica o local em contexto na conversa.
3. O sistema retorna as imagens disponíveis diretamente na conversa.

**Fluxos de exceção**

- E1 — A imagem não pode ser carregada: a resposta textual do assistente continua disponível.

---

### <a id="UC-028"></a>UC-028 — Enviar pergunta por áudio ao assistente

| Campo | Especificação |
|-------|---------------|
| Objetivo | Facilitar a comunicação com o assistente virtual por meio do envio de perguntas por áudio. |
| Prioridade | Could have. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de Transcrição de Áudio. |
| Pré-condições | Assistente disponível; visitante autoriza o uso do microfone. |
| Pós-condições | Pergunta enviada por áudio é processada e respondida em texto. |
| HU | [HU-037](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-037). |
| RF | [RF-037](Requisitos-Funcionais#RF-037). |
| RN | [RN-059](Regras-de-Neg%C3%B3cio#RN-059), [RN-060](Regras-de-Neg%C3%B3cio#RN-060). |
| Rastreabilidade | [Linha TM-HU-037](Matriz-de-Rastreabilidade#TM-HU-037). |
| Tipo de relação | `<<extend>>` de [UC-021](#UC-021). |
| Condição de extensão | O visitante opta por enviar a pergunta por áudio em vez de texto. |

**Fluxo principal**

1. O visitante grava e envia uma pergunta por áudio.
2. O serviço de transcrição de áudio converte o áudio em texto.
3. O sistema processa a pergunta transcrita como uma consulta normal ao assistente.
4. O sistema responde em texto.

**Fluxos de exceção**

- E1 — Áudio incompreensível: o sistema solicita nova gravação ou entrada textual.

---

## Épico 7: Interações Sociais e Compartilhamento

### <a id="UC-029"></a>UC-029 — Criar e compartilhar enquete

| Campo | Especificação |
|-------|---------------|
| Objetivo | Facilitar a decisão em grupo criando enquetes rápidas de locais/eventos compartilháveis por link. |
| Prioridade | Could have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; ao menos duas opções de locais/eventos válidas. |
| Pós-condições | Enquete e link público de votação são criados. |
| HU | [HU-038](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-038). |
| RF | [RF-038](Requisitos-Funcionais#RF-038). |
| RN | [RN-063](Regras-de-Neg%C3%B3cio#RN-063), [RN-064](Regras-de-Neg%C3%B3cio#RN-064), [RN-065](Regras-de-Neg%C3%B3cio#RN-065). |
| Rastreabilidade | [Linha TM-HU-038](Matriz-de-Rastreabilidade#TM-HU-038). |
| Tipo de relação | `<<include>>` de UC-077 — o ciclo de vida e o antifraude da enquete valem desde a criação. |

**Fluxo principal**

1. O usuário inicia a criação de uma enquete.
2. Informa título e opções de locais/eventos válidos.
3. O sistema valida as opções e cria a enquete.
4. O sistema gera o link público de votação, sob as regras incluídas do UC-077.
5. O usuário compartilha o link externamente.

**Fluxos alternativos**

- A1 — O usuário altera as opções antes da primeira votação registrada.

**Fluxos de exceção**

- E1 — Opção de local/evento inválida ou inativa: o sistema solicita substituição antes de concluir a criação.

---

### <a id="UC-030"></a>UC-030 — Consultar transporte alternativo parceiro

| Campo | Especificação |
|-------|---------------|
| Objetivo | Conseguir se deslocar com economia e segurança, acessando uma rede de contatos de transporte alternativo. |
| Prioridade | Could have. |
| Ator principal | Visitante. |
| Atores secundários | Serviço/operador de transporte parceiro. |
| Pré-condições | Local/evento público; parceiros de transporte ativos cadastrados. |
| Pós-condições | Opções de transporte alternativo compatíveis são exibidas ao visitante. |
| HU | [HU-039](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-039). |
| RF | [RF-039](Requisitos-Funcionais#RF-039). |
| RN | Nenhuma regra de negócio associada a esta história na matriz. |
| Rastreabilidade | [Linha TM-HU-039](Matriz-de-Rastreabilidade#TM-HU-039). |
| Pontos de extensão | [UC-079](Matriz-de-Rastreabilidade#TM-HU-087), no acionamento do contato após a escolha da opção de transporte. |

**Fluxo principal**

1. O visitante abre as opções de transporte alternativo de um local ou evento.
2. O sistema lista modalidade, área atendida, horários e contato dos parceiros ativos.
3. O visitante escolhe uma opção de interesse.

**Fluxos de exceção**

- E1 — Não há parceiro elegível para o local/evento: o sistema informa a ausência de opções sem interromper a consulta às informações gerais de acesso.

---

### <a id="UC-031"></a>UC-031 — Consultar mídias publicadas pela comunidade

| Campo | Especificação |
|-------|---------------|
| Objetivo | Ter uma visão autêntica do ambiente, consultando fotos e vídeos reais publicados pela comunidade. |
| Prioridade | Could have. |
| Ator principal | Visitante. |
| Atores secundários | Usuário autenticado, ao publicar uma nova mídia. |
| Pré-condições | Local/evento público; mídias aprovadas para exibição. |
| Pós-condições | Mídias comunitárias são exibidas na galeria; quando publicadas, ficam vinculadas ao autor e sujeitas à moderação. |
| HU | [HU-040](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-040). |
| RF | [RF-040](Requisitos-Funcionais#RF-040). |
| RN | [RN-033](Regras-de-Neg%C3%B3cio#RN-033), [RN-034](Regras-de-Neg%C3%B3cio#RN-034). |
| Rastreabilidade | [Linha TM-HU-040](Matriz-de-Rastreabilidade#TM-HU-040). |
| Tipo de relação | `<<extend>>` de [UC-012](#UC-012). |
| Condição de extensão | Existe mídia comunitária vinculada ao local exibido no UC-012. |

**Fluxo principal**

1. O visitante abre a seção de mídias da comunidade de um local/evento.
2. O sistema exibe fotos e vídeos curtos aprovados, vinculados a experiências reais.
3. O visitante abre uma mídia para ampliar ou navegar entre as publicações.

**Fluxos alternativos**

- A1 — Um usuário autenticado publica uma nova mídia: seleciona o local/evento, envia a mídia e um contexto mínimo da experiência; o sistema valida tipo, tamanho e vínculo e publica ou envia à moderação.
- A2 — Não há conteúdo comunitário para o local: o sistema informa a ausência sem fabricar conteúdo.

**Fluxos de exceção**

- E1 — Mídia não pode ser carregada: as demais mídias e o texto das avaliações relacionadas continuam disponíveis.
- E2 — Arquivo malicioso ou conteúdo grave enviado na publicação: o sistema bloqueia ou oculta a mídia preventivamente.

---

### <a id="UC-032"></a>UC-032 — Compartilhar lista pessoal por link público

| Campo | Especificação |
|-------|---------------|
| Objetivo | Facilitar a experiência de quem ainda não conhece a cidade, compartilhando listas pessoais por link público. |
| Prioridade | Should have. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; usuário é proprietário da lista. |
| Pós-condições | Link público de visualização da lista é gerado, sem expor dados privados desnecessários. |
| HU | [HU-041](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-041). |
| RF | [RF-041](Requisitos-Funcionais#RF-041). |
| RN | [RN-045](Regras-de-Neg%C3%B3cio#RN-045), [RN-061](Regras-de-Neg%C3%B3cio#RN-061), [RN-062](Regras-de-Neg%C3%B3cio#RN-062). |
| Rastreabilidade | [Linha TM-HU-041](Matriz-de-Rastreabilidade#TM-HU-041). |
| Pontos de extensão | [UC-078](Matriz-de-Rastreabilidade#TM-HU-086), quando o proprietário revoga o link já gerado. |

**Fluxo principal**

1. O usuário escolhe uma lista própria e aciona compartilhar.
2. O sistema mostra quais dados da lista ficarão públicos.
3. O usuário confirma o compartilhamento.
4. O sistema gera o link público de visualização.

**Fluxos de exceção**

- E1 — A lista não pertence ao usuário: o compartilhamento é negado.

---

### <a id="UC-033"></a>UC-033 — Compartilhar perfil de local ou evento

| Campo | Especificação |
|-------|---------------|
| Objetivo | Recomendar um local ou evento individual a outras pessoas, sem precisar montar uma lista ou publicar uma avaliação. |
| Prioridade | Should have — necessidade identificada na avaliação de usabilidade do protótipo de alta fidelidade, ainda pendente de validação com stakeholders (mesmo tratamento dado às hipóteses dos Épicos 9 a 13). |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Local ou evento publicado e visível; usuário autenticado. |
| Pós-condições | Link público de visualização do perfil do local/evento é gerado e pode ser aberto por qualquer pessoa, autenticada ou não. |
| HU | [HU-089](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-089). |
| RF | [RF-090](Requisitos-Funcionais#RF-090). |
| RN | [RN-094](Regras-de-Neg%C3%B3cio#RN-094). |
| Rastreabilidade | [Linha TM-HU-089](Matriz-de-Rastreabilidade#TM-HU-089). |
| Tipo de relação | `<<extend>>` de [UC-006](#UC-006), [UC-007](#UC-007), [UC-009](#UC-009), [UC-010](#UC-010), [UC-036](#UC-036) e [UC-042](#UC-042). |
| Condição de extensão | O usuário aciona "Compartilhar" na página do local, evento, equipamento ou atração. |

**Fluxo principal**

1. O usuário aciona "Compartilhar" na página de um local, evento, equipamento ou atração.
2. O sistema gera o link público de visualização do perfil correspondente.
3. O usuário compartilha o link externamente por meio de aplicativo compatível ou copiando o link.

**Fluxos alternativos**

- A1 — O usuário aciona "Compartilhar" sem estar autenticado: o sistema solicita login antes de concluir o compartilhamento.

**Fluxos de exceção**

- E1 — O local ou evento é despublicado após o compartilhamento: o acesso ao link informa que o conteúdo não está mais disponível, sem expor detalhes internos.

- - - 

## Épico 8: Equipamentos Culturais e Estabelecimentos

> [!WARNING]
> Os casos deste épico representam uma hipótese de escopo administrativo. Ainda não há stakeholders identificados para validá-los; eles não constituem evidência de necessidade confirmada.
>
> O núcleo de cadastro administrativo (UC-034, UC-036, UC-038 a UC-040, UC-042 e UC-043) é considerado estruturalmente necessário por decisão de produto: sem ele, o catálogo e a agenda de eventos dependem inteiramente da importação de fontes externas (RF-034) como única fonte de dado. A forma final de implementação (fluxos, telas e regras administrativas) ainda depende de validação com stakeholders administrativos, que ainda não foram identificados. Os casos remanescentes (UC-041 e UC-044 a UC-050) permanecem fora do escopo da entrega atual.

---

### <a id="UC-034"></a>UC-034 — Cadastrar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar um equipamento cultural para que possa ser administrado e, quando apto, disponibilizado ao público. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; dados mínimos do equipamento disponíveis. |
| Pós-condições | Equipamento é registrado, com estado de publicação compatível com os dados informados e trilha de auditoria. |
| HU | [HU-042](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-042) |
| RF | [RF-042](Requisitos-Funcionais#RF-042) |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-068](Regras-de-Neg%C3%B3cio#RN-068), [RN-076](Regras-de-Neg%C3%B3cio#RN-076), [RN-095](Regras-de-Neg%C3%B3cio#RN-095) |
| Rastreabilidade | [Linha TM-HU-042](Matriz-de-Rastreabilidade#TM-HU-042) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador da plataforma inicia o cadastro de um equipamento cultural; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa autorizada.
2. O administrador informa identificação, localização, dados de funcionamento, responsável, CNPJ quanto aplicável e demais informações exigidas para o tipo de local.
3. O sistema valida os dados mínimos do cadastro e verifica duplicidade conforme o critério aplicável (RN-095).
4. O sistema registra o equipamento e a operação de auditoria (RN-076).
5. O sistema disponibiliza o equipamento ou o mantém pendente até que atenda às condições de publicação (RN-068).

**Fluxos alternativos**

- A1 — Há dados mínimos pendentes: o sistema mantém o cadastro como não publicado e informa os campos necessários.
- A2 — O equipamento já possui cadastro: o sistema direciona o administrador para [UC-035](#UC-035).

**Fluxos de exceção**

- E1 — A sessão administrativa não é confirmada pelo [UC-038](#UC-038): o sistema nega o cadastro e não cria registro público.

---

### <a id="UC-035"></a>UC-035 — Editar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Manter atualizados os dados de um equipamento cultural cadastrado. |
| Prioridade | Should have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; equipamento existente. |
| Pós-condições | Dados autorizados são atualizados, com histórico da alteração. |
| HU | [HU-043](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-043) |
| RF | [RF-043](Requisitos-Funcionais#RF-043) |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-043](Matriz-de-Rastreabilidade#TM-HU-043) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador da plataforma seleciona um equipamento cultural cadastrado; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema apresenta os dados atuais e verifica o escopo de administração (RN-066).
3. O administrador altera as informações necessárias.
4. O sistema valida os dados e o vínculo do administrador ao equipamento.
5. O sistema salva a alteração e registra responsável, data, hora e recurso afetado (RN-076).

**Fluxos alternativos**

- A1 — A edição torna o cadastro incompleto: o sistema retira o equipamento da exibição pública até a regularização.

**Fluxos de exceção**

- E1 — O equipamento não pertence ao escopo do administrador: o sistema nega a alteração (RN-066).

---

### <a id="UC-036"></a>UC-036 — Consultar equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Consultar informações públicas de um equipamento cultural ativo. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Equipamento publicado e com vínculo válido. |
| Pós-condições | Informações públicas do equipamento são exibidas ao visitante. |
| HU | [HU-044](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-044) |
| RF | [RF-044](Requisitos-Funcionais#RF-044) |
| RN | [RN-022](Regras-de-Neg%C3%B3cio#RN-022), [RN-068](Regras-de-Neg%C3%B3cio#RN-068) |
| Rastreabilidade | [Linha TM-HU-044](Matriz-de-Rastreabilidade#TM-HU-044) |
| Pontos de extensão | [UC-080](#UC-080), ao sinalizar um dado incorreto; [UC-033](#UC-033), ao compartilhar o equipamento. |

Consulta pública: não inclui [UC-038](#UC-038) — o acesso à informação não exige autenticação (RN-022).

**Fluxo principal**

1. O visitante seleciona um equipamento cultural publicado.
2. O sistema verifica se o cadastro atende às condições de publicação (RN-068).
3. O sistema exibe localização, programação, serviços e demais informações públicas disponíveis (RN-022).

**Fluxos alternativos**

- A1 — O visitante identifica um dado incorreto: aciona a extensão [UC-080](#UC-080) sem precisar publicar uma avaliação.
- A2 — O visitante deseja compartilhar o equipamento: aciona a extensão [UC-033](#UC-033).

**Fluxos de exceção**

- E1 — O equipamento não está ativo ou não possui vínculo válido: o sistema não o exibe como conteúdo público.

---

### <a id="UC-037"></a>UC-037 — Associar administrador a equipamento cultural

| Campo | Especificação |
|-------|---------------|
| Objetivo | Vincular um administrador autorizado a um equipamento cultural para delimitar seu escopo de gestão. |
| Prioridade | Should have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Administrador de equipamento cultural. |
| Pré-condições | Sessão administrativa autorizada; equipamento e conta administrativa existentes. |
| Pós-condições | Vínculo de administração é registrado com escopo definido e auditável. |
| HU | [HU-045](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-045) |
| RF | [RF-045](Requisitos-Funcionais#RF-045) |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-067](Regras-de-Neg%C3%B3cio#RN-067), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-045](Matriz-de-Rastreabilidade#TM-HU-045) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador da plataforma seleciona um equipamento e uma conta administrativa; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica a existência dos dois registros.
3. O administrador confirma o escopo de gestão concedido.
4. O sistema registra o vínculo e a operação de auditoria (RN-076).
5. O administrador associado passa a poder acessar apenas as funcionalidades vinculadas ao equipamento, desde que o vínculo já exista antes da liberação de qualquer ação de gestão (RN-066, RN-067).

**Fluxos alternativos**

- A1 — A conta já está associada ao equipamento: o sistema apresenta o vínculo existente e evita duplicidade.

**Fluxos de exceção**

- E1 — Equipamento ou conta não é válido: o sistema não cria a associação.

---

### <a id="UC-038"></a>UC-038 — Autenticar administrador

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que um administrador autorizado acesse somente as funcionalidades administrativas compatíveis com seu vínculo. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural. |
| Atores secundários | Administrador da plataforma; administrador de estabelecimento gastronômico — mesmo fluxo de autenticação, reaproveitado por qualquer perfil administrativo. |
| Pré-condições | Conta administrativa ativa; para gestão de um local específico, vínculo prévio já registrado. |
| Pós-condições | Sessão administrativa é iniciada com o escopo de acesso aplicável. |
| HU | [HU-046](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-046) |
| RF | [RF-046](Requisitos-Funcionais#RF-046) |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-067](Regras-de-Neg%C3%B3cio#RN-067) |
| Rastreabilidade | [Linha TM-HU-046](Matriz-de-Rastreabilidade#TM-HU-046) |

Este é o único caso de autenticação/sessão administrativa do épico. Ele é incluído por [UC-034](#UC-034), [UC-035](#UC-035), [UC-037](#UC-037), [UC-039](#UC-039) a [UC-041](#UC-041), [UC-043](#UC-043) a [UC-050](#UC-050) — qualquer ação administrativa de criação, edição, remoção, associação ou publicação exige que este caso seja executado antes (RN-023). A autenticação do usuário comum (visitante logado) não é modelada como caso de uso; é tratada como pré-condição nos casos que a exigem.

**Fluxo principal**

1. O administrador informa suas credenciais.
2. O sistema verifica a identidade e o vínculo administrativo aplicável.
3. O sistema inicia uma sessão com as permissões correspondentes ao escopo autorizado (RN-023).

**Fluxos alternativos**

- A1 — A conta ainda não possui vínculo com um equipamento: o sistema mantém apenas as permissões compatíveis e orienta a associação por [UC-037](#UC-037), quando necessária.

**Fluxos de exceção**

- E1 — Credenciais inválidas ou conta inativa: o sistema não inicia a sessão administrativa.

---

### <a id="UC-039"></a>UC-039 — Cadastrar atração

| Campo | Especificação |
|-------|---------------|
| Objetivo | Cadastrar uma atração para divulgar atividades realizadas em um equipamento cultural. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada, com vínculo ao equipamento; equipamento ativo. |
| Pós-condições | Atração é criada, com estado de publicação compatível com os dados mínimos e trilha de auditoria. |
| HU | [HU-047](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-047) |
| RF | [RF-047](Requisitos-Funcionais#RF-047) |
| RN | [RN-012](Regras-de-Neg%C3%B3cio#RN-012), [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-038](Regras-de-Neg%C3%B3cio#RN-038), [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-047](Matriz-de-Rastreabilidade#TM-HU-047) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador de equipamento cultural acessa o cadastro de atrações do equipamento ao qual está vinculado; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o equipamento (RN-066).
3. O administrador informa descrição da experiência, horários de visitação, localização, valor de ingresso quando aplicável, acessibilidade, adequação infantil, segurança do entorno, programação associada e contato (RN-012).
4. O sistema valida os dados mínimos e o vínculo com o equipamento ativo (RN-068).
5. O sistema registra a atração e a operação de auditoria (RN-076).

**Fluxos alternativos**

- A1 — Há dados mínimos pendentes: o sistema mantém a atração como não publicada.
- A2 — O cadastro decorre de uma sinalização comunitária validada: a alteração só é aplicada após confirmação do administrador, sem que a sinalização altere o dado oficial por conta própria (RN-038).

**Fluxos de exceção**

- E1 — Administrador tenta cadastrar atração fora do equipamento vinculado: o sistema nega a operação (RN-066).

---

### <a id="UC-040"></a>UC-040 — Editar atração

| Campo | Especificação |
|-------|---------------|
| Objetivo | Editar informações de uma atração cadastrada para corrigir ou atualizar seus dados. |
| Prioridade | Should have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; atração existente vinculada ao equipamento administrado. |
| Pós-condições | Dados da atração são atualizados; atração sem vínculo válido deixa de ficar visível ao público. |
| HU | [HU-048](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-048) |
| RF | [RF-048](Requisitos-Funcionais#RF-048) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-071](Regras-de-Neg%C3%B3cio#RN-071), [RN-072](Regras-de-Neg%C3%B3cio#RN-072), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-048](Matriz-de-Rastreabilidade#TM-HU-048) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma atração cadastrada; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o equipamento e o vínculo da atração com o equipamento ativo (RN-066, RN-071).
3. O administrador altera os dados necessários.
4. O sistema valida os dados e o vínculo.
5. O sistema salva a alteração e registra o histórico da operação (RN-076).

**Fluxos alternativos**

- A1 — A edição invalida o vínculo com o equipamento ativo: a atração deixa de ficar visível ao público (RN-072).

**Fluxos de exceção**

- E1 — A atração não pertence ao escopo do administrador: o sistema nega a alteração (RN-066).

---

### <a id="UC-041"></a>UC-041 — Remover atração

| Campo | Especificação |
|-------|---------------|
| Objetivo | Remover uma atração cadastrada para evitar a exibição de informações desatualizadas ou incorretas. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; atração existente vinculada ao equipamento administrado. |
| Pós-condições | Atração é removida da exibição pública, arquivada ou marcada como inativa, com histórico preservado. |
| HU | [HU-049](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-049) |
| RF | [RF-049](Requisitos-Funcionais#RF-049) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-074](Regras-de-Neg%C3%B3cio#RN-074), [RN-075](Regras-de-Neg%C3%B3cio#RN-075), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-049](Matriz-de-Rastreabilidade#TM-HU-049) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma atração cadastrada e solicita a remoção; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o equipamento (RN-066).
3. O administrador confirma a remoção ou o motivo do encerramento.
4. O sistema retira a atração da exibição pública, arquiva-a ou a marca como inativa (RN-074).
5. O sistema preserva o histórico da alteração para consulta de auditoria (RN-075, RN-076).

**Fluxos alternativos**

- A1 — A atração já está encerrada: o sistema prioriza o arquivamento sobre a exclusão definitiva, para preservar o histórico administrativo.

**Fluxos de exceção**

- E1 — A atração não pertence ao escopo do administrador: o sistema nega a remoção (RN-066).

---

### <a id="UC-042"></a>UC-042 — Consultar atrações cadastradas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Visualizar as atrações cadastradas para descobrir atividades de interesse. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Atração publicada, com vínculo válido a equipamento ativo. |
| Pós-condições | Atrações publicadas são exibidas ao visitante. |
| HU | [HU-050](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-050) |
| RF | [RF-050](Requisitos-Funcionais#RF-050) |
| RN | [RN-012](Regras-de-Neg%C3%B3cio#RN-012), [RN-022](Regras-de-Neg%C3%B3cio#RN-022) |
| Rastreabilidade | [Linha TM-HU-050](Matriz-de-Rastreabilidade#TM-HU-050) |
| Pontos de extensão | [UC-080](#UC-080), ao sinalizar um dado incorreto; [UC-033](#UC-033), ao compartilhar a atração. |

Consulta pública: não inclui [UC-038](#UC-038) — o acesso à informação não exige autenticação (RN-022).

**Fluxo principal**

1. O visitante acessa as atrações de um equipamento cultural.
2. O sistema lista as atrações publicadas e com vínculo válido (RN-022).
3. O visitante seleciona uma atração.
4. O sistema exibe as informações públicas disponíveis: descrição, horários, localização, valor de ingresso quando aplicável, acessibilidade, adequação infantil, segurança do entorno, programação e contato (RN-012).

**Fluxos alternativos**

- A1 — O visitante identifica um dado incorreto: aciona a extensão [UC-080](#UC-080) sem precisar publicar uma avaliação.
- A2 — O visitante deseja compartilhar a atração: aciona a extensão [UC-033](#UC-033).

**Fluxos de exceção**

- E1 — A atração não possui vínculo válido com um equipamento ativo: o sistema não a exibe como conteúdo público.

---

### <a id="UC-043"></a>UC-043 — Cadastrar estabelecimento gastronômico

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar um estabelecimento gastronômico para disponibilizar suas informações aos usuários do sistema. |
| Prioridade | Must have — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; dados mínimos do estabelecimento disponíveis. |
| Pós-condições | Estabelecimento é registrado, com estado de publicação compatível com os dados mínimos e trilha de auditoria. |
| HU | [HU-051](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-051) |
| RF | [RF-051](Requisitos-Funcionais#RF-051) |
| RN | [RN-011](Regras-de-Neg%C3%B3cio#RN-011), [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-038](Regras-de-Neg%C3%B3cio#RN-038), [RN-068](Regras-de-Neg%C3%B3cio#RN-068), [RN-076](Regras-de-Neg%C3%B3cio#RN-076), [RN-095](Regras-de-Neg%C3%B3cio#RN-095) |
| Rastreabilidade | [Linha TM-HU-051](Matriz-de-Rastreabilidade#TM-HU-051) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador da plataforma inicia o cadastro de um estabelecimento gastronômico; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O administrador informa CNPJ quando aplicável, cardápio ou descrição de produtos, faixa de preços, couvert artístico quando aplicável, horários, formato de atendimento, regras do local, canal de contato e o responsável administrativo (RN-011).
3. O sistema valida os dados mínimos do cadastro (RN-068) e verifica duplicidade conforme o critério aplicável (RN-095).
4. O sistema registra o estabelecimento e a operação de auditoria (RN-076).
5. O sistema disponibiliza o estabelecimento ou o mantém pendente até que atenda às condições de publicação.

**Fluxos alternativos**

- A1 — Há dados mínimos pendentes: o sistema mantém o cadastro fora da exibição pública e informa os campos necessários.
- A2 — O estabelecimento já possui cadastro (mesmo CNPJ ou correspondência de nome, endereço e categoria, conforme RN-095): o sistema direciona o administrador para a edição do cadastro existente.
- A3 — O cadastro decorre de uma sinalização comunitária validada: a alteração só é aplicada após confirmação do administrador (RN-038).

**Fluxos de exceção**

- E1 — A sessão administrativa não é confirmada pelo [UC-038](#UC-038): o sistema nega o cadastro e não cria registro público.
---

### <a id="UC-044"></a>UC-044 — Cadastrar oferta

| Campo | Especificação |
|-------|---------------|
| Objetivo | Cadastrar ofertas para divulgar promoções, eventos ou produtos especiais do estabelecimento gastronômico. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada, com vínculo ao estabelecimento; estabelecimento ativo. |
| Pós-condições | Oferta é criada, com estado de publicação compatível com os dados mínimos e trilha de auditoria. |
| HU | [HU-052](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-052) |
| RF | [RF-052](Requisitos-Funcionais#RF-052) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068), [RN-069](Regras-de-Neg%C3%B3cio#RN-069), [RN-071](Regras-de-Neg%C3%B3cio#RN-071), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-052](Matriz-de-Rastreabilidade#TM-HU-052) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador de estabelecimento gastronômico acessa as ofertas do estabelecimento ao qual está vinculado; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o estabelecimento (RN-066).
3. O administrador informa título, descrição, responsável e período de validade da oferta (RN-069).
4. O sistema valida o vínculo com o estabelecimento ativo e os dados mínimos (RN-068, RN-071).
5. O sistema registra a oferta e a operação de auditoria (RN-076).

**Fluxos alternativos**

- A1 — Há dados mínimos pendentes: o sistema mantém a oferta fora da exibição pública.

**Fluxos de exceção**

- E1 — Administrador tenta cadastrar oferta fora do estabelecimento vinculado: o sistema nega a operação (RN-066).

---

### <a id="UC-045"></a>UC-045 — Editar oferta

| Campo | Especificação |
|-------|---------------|
| Objetivo | Editar ofertas cadastradas para manter as informações corretas e atualizadas. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; oferta existente vinculada ao estabelecimento administrado. |
| Pós-condições | Dados da oferta são atualizados; oferta sem vínculo válido deixa de ficar visível ao público. |
| HU | [HU-053](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-053) |
| RF | [RF-053](Requisitos-Funcionais#RF-053) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-071](Regras-de-Neg%C3%B3cio#RN-071), [RN-072](Regras-de-Neg%C3%B3cio#RN-072), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-053](Matriz-de-Rastreabilidade#TM-HU-053) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma oferta cadastrada; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o estabelecimento e o vínculo da oferta com o estabelecimento ativo (RN-066, RN-071).
3. O administrador altera os dados necessários.
4. O sistema valida os dados e o vínculo.
5. O sistema salva a alteração e registra o histórico da operação (RN-076).

**Fluxos alternativos**

- A1 — A edição invalida o vínculo com o estabelecimento ativo: a oferta deixa de ficar visível ao público (RN-072).

**Fluxos de exceção**

- E1 — A oferta não pertence ao escopo do administrador: o sistema nega a alteração (RN-066).

---

### <a id="UC-046"></a>UC-046 — Remover oferta

| Campo | Especificação |
|-------|---------------|
| Objetivo | Remover ofertas cadastradas para evitar a divulgação de informações inválidas. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; oferta existente vinculada ao estabelecimento administrado. |
| Pós-condições | Oferta é removida da exibição pública, arquivada ou marcada como inativa, com histórico preservado. |
| HU | [HU-054](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-054) |
| RF | [RF-054](Requisitos-Funcionais#RF-054) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-073](Regras-de-Neg%C3%B3cio#RN-073), [RN-075](Regras-de-Neg%C3%B3cio#RN-075), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-054](Matriz-de-Rastreabilidade#TM-HU-054) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma oferta cadastrada; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o estabelecimento (RN-066).
3. O sistema identifica se a oferta atingiu o período de validade encerrado (RN-073).
4. O administrador confirma a remoção manual, quando aplicável.
5. O sistema retira a oferta da exibição pública, arquiva-a ou a marca como inativa e preserva o histórico da alteração (RN-073, RN-075, RN-076).

**Fluxos alternativos**

- A1 — A oferta expira antes de qualquer ação manual: o sistema a retira automaticamente da exibição pública, arquivando-a ou marcando-a como inativa (RN-073).

**Fluxos de exceção**

- E1 — A oferta não pertence ao escopo do administrador: o sistema nega a remoção (RN-066).

---

### <a id="UC-047"></a>UC-047 — Cadastrar publicação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Cadastrar publicações para disponibilizar conteúdos relevantes aos usuários. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador da plataforma. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; dados mínimos da publicação disponíveis. |
| Pós-condições | Publicação geral é criada, sem vínculo obrigatório a local específico, com trilha de auditoria. |
| HU | [HU-055](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-055) |
| RF | [RF-055](Requisitos-Funcionais#RF-055) |
| RN | [RN-068](Regras-de-Neg%C3%B3cio#RN-068), [RN-070](Regras-de-Neg%C3%B3cio#RN-070), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-055](Matriz-de-Rastreabilidade#TM-HU-055) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador da plataforma inicia a criação de uma publicação; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O administrador informa título, conteúdo e responsável pela publicação (RN-070).
3. O sistema valida os dados mínimos da publicação (RN-068).
4. O sistema cria a publicação geral, sem vínculo com local específico, e registra a operação de auditoria (RN-076).

**Fluxos alternativos**

- A1 — A publicação é de caráter geral: o administrador da plataforma a publica sem associá-la a um equipamento cultural ou estabelecimento gastronômico específico.

**Fluxos de exceção**

- E1 — Publicação sem os dados mínimos exigidos: o sistema impede sua exibição pública (RN-068).

---

### <a id="UC-048"></a>UC-048 — Criar publicação vinculada a local

| Campo | Especificação |
|-------|---------------|
| Objetivo | Criar publicações associadas ao equipamento cultural ou estabelecimento gastronômico administrado, para divulgar informações relacionadas às atividades do local. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural ou de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada, com vínculo ao local; local ativo. |
| Pós-condições | Publicação vinculada é criada e permanece disponível somente enquanto o vínculo com o local for válido. |
| HU | [HU-056](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-056) |
| RF | [RF-056](Requisitos-Funcionais#RF-056) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-070](Regras-de-Neg%C3%B3cio#RN-070), [RN-071](Regras-de-Neg%C3%B3cio#RN-071), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-056](Matriz-de-Rastreabilidade#TM-HU-056) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador de equipamento cultural ou de estabelecimento gastronômico acessa as publicações do local ao qual está vinculado; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o local (RN-066).
3. O administrador informa título, conteúdo, responsável e o local ao qual a publicação se vincula (RN-070).
4. O sistema valida o vínculo com o local ativo (RN-071).
5. O sistema cria a publicação e registra a operação de auditoria (RN-076).

**Fluxos alternativos**

- A1 — A publicação é vinculada a um local: o sistema a disponibiliza somente enquanto o vínculo permanecer válido (RN-071).

**Fluxos de exceção**

- E1 — Administrador tenta criar publicação fora do local vinculado: o sistema nega a operação (RN-066).

---

### <a id="UC-049"></a>UC-049 — Editar publicação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Editar publicações existentes para atualizar seu conteúdo quando necessário. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural ou de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; publicação existente dentro do escopo do administrador. |
| Pós-condições | Conteúdo da publicação é atualizado; publicação sem vínculo válido deixa de ficar visível ao público. |
| HU | [HU-057](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-057) |
| RF | [RF-057](Requisitos-Funcionais#RF-057) |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-071](Regras-de-Neg%C3%B3cio#RN-071), [RN-072](Regras-de-Neg%C3%B3cio#RN-072), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-057](Matriz-de-Rastreabilidade#TM-HU-057) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma publicação existente; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador e o vínculo da publicação com o local ativo (RN-066, RN-071).
3. O administrador altera título, conteúdo ou demais dados.
4. O sistema valida os dados e o vínculo.
5. O sistema salva a alteração e registra o histórico da operação (RN-076).

**Fluxos alternativos**

- A1 — A edição invalida o vínculo com o local ativo: a publicação deixa de ficar visível ao público (RN-072).

**Fluxos de exceção**

- E1 — A publicação não pertence ao escopo do administrador: o sistema nega a alteração (RN-066).

---

### <a id="UC-050"></a>UC-050 — Remover publicação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Remover publicações para excluir conteúdos que não devam mais ser exibidos aos usuários. |
| Prioridade | Won't have nesta entrega — fluxo e telas administrativas ainda em validação com stakeholders. |
| Ator principal | Administrador de equipamento cultural ou de estabelecimento gastronômico. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão administrativa autorizada; publicação existente dentro do escopo do administrador. |
| Pós-condições | Publicação é removida da exibição pública, arquivada ou marcada como inativa, com histórico preservado. |
| HU | [HU-058](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-058) |
| RF | [RF-058](Requisitos-Funcionais#RF-058) |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-074](Regras-de-Neg%C3%B3cio#RN-074), [RN-075](Regras-de-Neg%C3%B3cio#RN-075), [RN-076](Regras-de-Neg%C3%B3cio#RN-076) |
| Rastreabilidade | [Linha TM-HU-058](Matriz-de-Rastreabilidade#TM-HU-058) |
| Tipo de relação | `<<include>>` de [UC-038](#UC-038) — toda ação administrativa exige sessão administrativa autorizada (RN-023). |

**Fluxo principal**

1. O administrador seleciona uma publicação existente e solicita a remoção; o sistema inclui [UC-038](#UC-038) para confirmar a sessão administrativa.
2. O sistema verifica o escopo do administrador sobre o local vinculado à publicação (RN-066).
3. O administrador confirma a remoção.
4. O sistema retira a publicação da exibição pública, arquiva-a ou a marca como inativa (RN-074).
5. O sistema preserva o histórico da alteração para consulta de auditoria (RN-075, RN-076).

**Fluxos alternativos**

- A1 — A publicação perdeu a validade operacional: o sistema prioriza o arquivamento automático sobre a exclusão definitiva (RN-074).

**Fluxos de exceção**

- E1 — A publicação não pertence ao escopo do administrador: o sistema nega a remoção (RN-066).
## Épico 9: Avaliações e Comunidade (Protótipo)

> [!WARNING]
> As histórias dos épicos 9 a 13 foram derivadas do protótipo de alta fidelidade e permanecem pendentes de validação com stakeholders.

### <a id="UC-051"></a>UC-051 — Marcar avaliação como útil

| Campo | Especificação |
|-------|---------------|
| Objetivo | Identificar contribuições relevantes da comunidade por meio da marcação de avaliações como úteis. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; avaliação publicada e visível. |
| Pós-condições | A marcação de "útil" é registrada vinculada ao usuário e à avaliação, e a contagem pública é atualizada. |
| HU | [HU-059](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-059). |
| RF | [RF-059](Requisitos-Funcionais#RF-059). |
| RN | [RN-029](Regras-de-Neg%C3%B3cio#RN-029), [RN-030](Regras-de-Neg%C3%B3cio#RN-030), [RN-037](Regras-de-Neg%C3%B3cio#RN-037). |
| Rastreabilidade | [Linha TM-HU-059](Matriz-de-Rastreabilidade#TM-HU-059). |
| Tipo de relação | `<<extend>>` de [UC-012](#UC-012) (Consultar avaliações da comunidade), no ponto "marcar avaliação como útil". |
| Condição de extensão | O usuário aciona "marcar como útil" em uma avaliação exibida. |

**Fluxo principal**

1. O usuário autenticado consulta avaliações de um local ([UC-012](#UC-012)).
2. Aciona "marcar como útil" em uma avaliação publicada.
3. O sistema verifica se o usuário já marcou essa avaliação anteriormente.
4. O sistema registra a marcação vinculada ao usuário e à avaliação.
5. O sistema atualiza e exibe a contagem pública de marcações da avaliação.

**Fluxos alternativos**

- A1 — O usuário desmarca uma avaliação previamente marcada como útil; o sistema decrementa a contagem.

**Fluxos de exceção**

- E1 — O usuário tenta marcar novamente uma avaliação já marcada por ele: o sistema mantém a marcação única e não duplica a contagem.

---

### <a id="UC-052"></a>UC-052 — Compartilhar avaliação individual

| Campo | Especificação |
|-------|---------------|
| Objetivo | Recomendar ou discutir externamente uma experiência específica por meio do compartilhamento de uma avaliação individual. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; avaliação publicada e visível. |
| Pós-condições | Link público de visualização da avaliação individual é gerado e pode ser aberto externamente. |
| HU | [HU-060](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-060). |
| RF | [RF-060](Requisitos-Funcionais#RF-060). |
| RN | [RN-029](Regras-de-Neg%C3%B3cio#RN-029), [RN-037](Regras-de-Neg%C3%B3cio#RN-037). |
| Rastreabilidade | [Linha TM-HU-060](Matriz-de-Rastreabilidade#TM-HU-060). |
| Tipo de relação | `<<extend>>` de [UC-012](#UC-012) (Consultar avaliações da comunidade), no ponto "compartilhar avaliação individual". |
| Condição de extensão | O usuário aciona "compartilhar" em uma avaliação individual exibida. |

**Fluxo principal**

1. O usuário consulta avaliações de um local ([UC-012](#UC-012)).
2. Aciona "compartilhar" em uma avaliação publicada específica.
3. O sistema gera o link público de visualização da avaliação individual.
4. O usuário compartilha o link por aplicativo compatível ou copiando o link.

**Fluxos de exceção**

- E1 — A avaliação é removida ou despublicada após o compartilhamento: o acesso ao link informa que o conteúdo não está mais disponível.

---

### <a id="UC-053"></a>UC-053 — Iniciar tópico de discussão na comunidade

| Campo | Especificação |
|-------|---------------|
| Objetivo | Conversar com a comunidade sobre experiências em locais ou eventos por meio de tópicos de discussão. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; local ou evento publicado. |
| Pós-condições | Tópico de discussão é criado, vinculado ao local/evento e ao autor, e fica disponível para respostas da comunidade. |
| HU | [HU-061](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-061). |
| RF | [RF-061](Requisitos-Funcionais#RF-061). |
| RN | [RN-033](Regras-de-Neg%C3%B3cio#RN-033), [RN-034](Regras-de-Neg%C3%B3cio#RN-034). |
| Rastreabilidade | [Linha TM-HU-061](Matriz-de-Rastreabilidade#TM-HU-061). |

**Fluxo principal**

1. O usuário acessa a seção de comunidade de um local ou evento.
2. Aciona "iniciar tópico" e informa título e mensagem inicial.
3. O sistema valida o vínculo com o local/evento e o conteúdo mínimo informado.
4. O sistema publica o tópico associado ao autor e o disponibiliza para respostas da comunidade.

**Fluxos alternativos**

- A1 — O usuário anexa fotos ou vídeos ao tópico; o sistema valida a mídia conforme as regras de conteúdo comunitário.

**Fluxos de exceção**

- E1 — Conteúdo do tópico viola regra grave (ameaça, discriminação, dado pessoal exposto): o sistema oculta preventivamente e informa o motivo.

---

## Épico 10: Organização Pessoal e Gamificação (Protótipo)

### <a id="UC-054"></a>UC-054 — Consultar conquistas e distintivos

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acompanhar o próprio engajamento na plataforma por meio de conquistas e distintivos desbloqueáveis. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida. |
| Pós-condições | Conquistas e distintivos desbloqueados e pendentes são exibidos ao usuário. |
| HU | [HU-062](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-062). |
| RF | [RF-062](Requisitos-Funcionais#RF-062). |
| RN | [RN-047](Regras-de-Neg%C3%B3cio#RN-047), [RN-048](Regras-de-Neg%C3%B3cio#RN-048). |
| Rastreabilidade | [Linha TM-HU-062](Matriz-de-Rastreabilidade#TM-HU-062). |

**Fluxo principal**

1. O usuário acessa a área de conquistas do próprio perfil.
2. O sistema consulta o histórico de visitas, avaliações publicadas e check-ins do usuário.
3. O sistema calcula quais conquistas e distintivos foram desbloqueados.
4. O sistema exibe os distintivos obtidos e os pendentes de desbloqueio.

**Fluxos alternativos**

- A1 — Nenhuma conquista foi desbloqueada ainda: o sistema exibe os critérios para o próximo distintivo.

**Fluxos de exceção**

- E1 — Falha ao vincular histórico de visitas ou avaliações ao usuário autenticado: o sistema não exibe progresso de conquistas baseado em dado de terceiro.

---

### <a id="UC-055"></a>UC-055 — Consultar dicas contextuais no checklist

| Campo | Especificação |
|-------|---------------|
| Objetivo | Preparar-se melhor para a visita por meio de dicas contextuais curadas exibidas no checklist. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; checklist de visita associado a um local. |
| Pós-condições | Dicas contextuais curadas do local são exibidas junto ao checklist, sem alterar o progresso registrado. |
| HU | [HU-063](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-063). |
| RF | [RF-063](Requisitos-Funcionais#RF-063). |
| RN | [RN-050](Regras-de-Neg%C3%B3cio#RN-050), [RN-051](Regras-de-Neg%C3%B3cio#RN-051). |
| Rastreabilidade | [Linha TM-HU-063](Matriz-de-Rastreabilidade#TM-HU-063). |
| Tipo de relação | `<<extend>>` de [UC-020](#UC-020) (Usar checklist de atividades e passeios), no ponto "consultar dicas contextuais". |
| Condição de extensão | Existe dica curada disponível para o local associado ao checklist. |

**Fluxo principal**

1. O usuário abre o checklist de um local ([UC-020](#UC-020)).
2. O sistema verifica se há dicas contextuais curadas para aquele local.
3. O sistema exibe as dicas junto aos itens do checklist, sem alterar o progresso registrado.

**Fluxos alternativos**

- A1 — Não há dica curada disponível para o local: a extensão não é acionada e o checklist é exibido normalmente.

---

## Épico 11: Gestão de Estabelecimentos (Protótipo)

### <a id="UC-056"></a>UC-056 — Consultar painel de métricas do estabelecimento

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acompanhar a atividade do estabelecimento por meio de um painel com métricas resumidas de visitantes, avaliações recentes e eventos ativos. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento; gestor no modo Gestor. |
| Pós-condições | Painel com métricas resumidas do(s) estabelecimento(s) gerenciados é exibido. |
| HU | [HU-064](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-064). |
| RF | [RF-064](Requisitos-Funcionais#RF-064). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [Linha TM-HU-064](Matriz-de-Rastreabilidade#TM-HU-064). |
| Pontos de extensão | [UC-059](#UC-059), na ação "ver como visitante". |

**Fluxo principal**

1. O gestor acessa o painel de métricas.
2. O sistema verifica o vínculo administrativo do gestor com o(s) estabelecimento(s).
3. O sistema consolida visitantes, avaliações recentes e eventos ativos do período.
4. O sistema exibe o painel com as métricas resumidas.

**Fluxos alternativos**

- A1 — O gestor administra mais de um estabelecimento: seleciona qual estabelecimento deseja consultar.

**Fluxos de exceção**

- E1 — Gestor sem vínculo administrativo válido com o estabelecimento: o sistema nega o acesso ao painel.

---

### <a id="UC-057"></a>UC-057 — Acompanhar feed de atividades recentes

| Campo | Especificação |
|-------|---------------|
| Objetivo | Reagir a novas interações por meio de um feed cronológico de atividades recentes do estabelecimento. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento. |
| Pós-condições | Feed cronológico com as atividades recentes (novas avaliações, visualizações, interações) é exibido. |
| HU | [HU-065](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-065). |
| RF | [RF-065](Requisitos-Funcionais#RF-065). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [Linha TM-HU-065](Matriz-de-Rastreabilidade#TM-HU-065). |

**Fluxo principal**

1. O gestor acessa o feed de atividades do estabelecimento.
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema lista as atividades recentes em ordem cronológica.
4. O gestor seleciona um item do feed para consultar mais detalhes.

**Fluxos alternativos**

- A1 — Não há atividade recente registrada: o sistema informa a ausência de novidades sem exibir dado incorreto.

**Fluxos de exceção**

- E1 — Gestor sem vínculo administrativo válido com o estabelecimento: o sistema nega o acesso ao feed.

---

### <a id="UC-058"></a>UC-058 — Responder publicamente a uma avaliação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Dialogar publicamente com usuários por meio de respostas do gestor às avaliações recebidas. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento; avaliação publicada existente. |
| Pós-condições | Resposta pública do gestor é publicada e vinculada à avaliação e ao estabelecimento. |
| HU | [HU-066](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-066). |
| RF | [RF-066](Requisitos-Funcionais#RF-066). |
| RN | [RN-030](Regras-de-Neg%C3%B3cio#RN-030), [RN-033](Regras-de-Neg%C3%B3cio#RN-033), [RN-066](Regras-de-Neg%C3%B3cio#RN-066). |
| Rastreabilidade | [Linha TM-HU-066](Matriz-de-Rastreabilidade#TM-HU-066). |

**Fluxo principal**

1. O gestor abre uma avaliação recebida pelo estabelecimento que administra.
2. Escreve o texto da resposta pública.
3. O sistema valida o vínculo administrativo do gestor com o estabelecimento avaliado.
4. O sistema publica a resposta associada ao autor administrativo e à avaliação original.

**Fluxos alternativos**

- A1 — O gestor edita uma resposta já publicada; o sistema mantém o vínculo com a avaliação original.

**Fluxos de exceção**

- E1 — Gestor tenta responder a avaliação de estabelecimento fora de seu vínculo administrativo: o sistema nega a operação.

---

### <a id="UC-059"></a>UC-059 — Visualizar a página pública como visitante

| Campo | Especificação |
|-------|---------------|
| Objetivo | Conferir a apresentação do estabelecimento tal como é vista pelos usuários. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento; estabelecimento publicado. |
| Pós-condições | Página pública do estabelecimento é exibida ao gestor exatamente como aparece aos visitantes. |
| HU | [HU-067](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-067). |
| RF | [RF-067](Requisitos-Funcionais#RF-067). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [Linha TM-HU-067](Matriz-de-Rastreabilidade#TM-HU-067). |
| Tipo de relação | `<<extend>>` de [UC-056](#UC-056) (Consultar painel de métricas do estabelecimento), no ponto "visualizar página pública como visitante". |
| Condição de extensão | O gestor opta por conferir a apresentação pública do estabelecimento. |

**Fluxo principal**

1. A partir do painel de métricas ([UC-056](#UC-056)), o gestor aciona "ver como visitante".
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema apresenta a página pública do estabelecimento na mesma versão exibida aos visitantes.

**Fluxos de exceção**

- E1 — O estabelecimento não está publicado: o sistema informa que não há página pública disponível para visualização.

---

### <a id="UC-060"></a>UC-060 — Consultar indicadores de desempenho

| Campo | Especificação |
|-------|---------------|
| Objetivo | Orientar decisões de gestão por meio de indicadores e análises de desempenho do estabelecimento. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento. |
| Pós-condições | Indicadores de fluxo de visitantes, perfil do público, horários de pico e visibilidade regional são exibidos. |
| HU | [HU-068](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-068). |
| RF | [RF-068](Requisitos-Funcionais#RF-068). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [Linha TM-HU-068](Matriz-de-Rastreabilidade#TM-HU-068). |

**Fluxo principal**

1. O gestor acessa os indicadores de desempenho do estabelecimento.
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema consolida fluxo de visitantes, perfil do público, horários de pico e visibilidade regional.
4. O sistema exibe o painel de indicadores e análises.

**Fluxos alternativos**

- A1 — O gestor filtra os indicadores por período; o sistema recalcula a análise para o intervalo escolhido.

**Fluxos de exceção**

- E1 — Dados insuficientes para compor algum indicador: o sistema o omite ou sinaliza a limitação, sem apresentar estimativa não confiável.

---

### <a id="UC-061"></a>UC-061 — Consultar mapa de origem dos visitantes

| Campo | Especificação |
|-------|---------------|
| Objetivo | Compreender o alcance do estabelecimento por meio da distribuição geográfica agregada da origem dos visitantes. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento; dados de origem agregados disponíveis. |
| Pós-condições | Mapa com a distribuição geográfica agregada dos visitantes é exibido. |
| HU | [HU-069](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-069). |
| RF | [RF-069](Requisitos-Funcionais#RF-069). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-068](Regras-de-Neg%C3%B3cio#RN-068). |
| Rastreabilidade | [Linha TM-HU-069](Matriz-de-Rastreabilidade#TM-HU-069). |

**Fluxo principal**

1. O gestor acessa o mapa de origem dos visitantes.
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema agrega a origem geográfica dos visitantes sem identificar indivíduos.
4. O sistema exibe o mapa com a distribuição agregada.

**Fluxos de exceção**

- E1 — Volume de dados insuficiente para agregação sem risco de identificação individual: o sistema não exibe a região isoladamente.

---

## Épico 12: Perfil, Autenticação e Parceria (Protótipo)

### <a id="UC-062"></a>UC-062 — Alternar entre os modos Explorador e Gestor

| Campo | Especificação |
|-------|---------------|
| Objetivo | Acessar rapidamente os dois contextos, Explorador e Gestor, sem realizar novo login. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida; usuário possui perfil de gestor vinculado a pelo menos um estabelecimento. |
| Pós-condições | Modo ativo (Explorador ou Gestor) é alternado mantendo a mesma sessão autenticada. |
| HU | [HU-070](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-070). |
| RF | [RF-070](Requisitos-Funcionais#RF-070). |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-067](Regras-de-Neg%C3%B3cio#RN-067). |
| Rastreabilidade | [Linha TM-HU-070](Matriz-de-Rastreabilidade#TM-HU-070). |

**Fluxo principal**

1. O usuário com perfil de gestor aciona a alternância de modo.
2. O sistema verifica o vínculo administrativo ativo do usuário.
3. O sistema troca o contexto de navegação para o modo escolhido (Explorador ou Gestor), preservando a sessão.

**Fluxos de exceção**

- E1 — Usuário sem vínculo administrativo ativo tenta acessar o modo Gestor: o sistema mantém apenas o modo Explorador disponível.

---

### <a id="UC-063"></a>UC-063 — Consultar nível de parceria na plataforma

| Campo | Especificação |
|-------|---------------|
| Objetivo | Compreender a relação com a plataforma por meio do nível de parceria e seus benefícios. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento. |
| Pós-condições | Nível de parceria, identificação visual e descrição dos benefícios são exibidos. |
| HU | [HU-071](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-071). |
| RF | [RF-071](Requisitos-Funcionais#RF-071). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-067](Regras-de-Neg%C3%B3cio#RN-067). |
| Rastreabilidade | [Linha TM-HU-071](Matriz-de-Rastreabilidade#TM-HU-071). |

**Fluxo principal**

1. O gestor acessa a área de parceria do próprio perfil.
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema exibe o nível de parceria atual, identificação visual e os benefícios associados.

**Fluxos de exceção**

- E1 — Gestor sem vínculo administrativo válido: o sistema não exibe nível de parceria associado a nenhum estabelecimento.

---

### <a id="UC-064"></a>UC-064 — Consultar certificações e qualificações

| Campo | Especificação |
|-------|---------------|
| Objetivo | Evidenciar a atuação do gestor por meio das certificações e qualificações obtidas na plataforma. |
| Prioridade | Won't have nesta entrega — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida com vínculo administrativo ao estabelecimento. |
| Pós-condições | Certificações e qualificações do gestor são exibidas. |
| HU | [HU-072](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-072). |
| RF | [RF-072](Requisitos-Funcionais#RF-072). |
| RN | [RN-066](Regras-de-Neg%C3%B3cio#RN-066), [RN-067](Regras-de-Neg%C3%B3cio#RN-067). |
| Rastreabilidade | [Linha TM-HU-072](Matriz-de-Rastreabilidade#TM-HU-072). |

**Fluxo principal**

1. O gestor acessa a área de certificações do próprio perfil.
2. O sistema verifica o vínculo administrativo do gestor com o estabelecimento.
3. O sistema exibe as certificações e qualificações obtidas na plataforma.

**Fluxos de exceção**

- E1 — Gestor sem certificação registrada: o sistema informa a ausência sem exibir dado fictício.

---

### <a id="UC-065"></a>UC-065 — Encerrar todas as sessões ativas

| Campo | Especificação |
|-------|---------------|
| Objetivo | Proteger a conta encerrando simultaneamente todas as sessões ativas do usuário. |
| Prioridade | Could have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida. |
| Pós-condições | Todas as sessões ativas vinculadas à conta são encerradas simultaneamente. |
| HU | [HU-073](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-073). |
| RF | [RF-073](Requisitos-Funcionais#RF-073). |
| RN | [RN-023](Regras-de-Neg%C3%B3cio#RN-023), [RN-067](Regras-de-Neg%C3%B3cio#RN-067). |
| Rastreabilidade | [Linha TM-HU-073](Matriz-de-Rastreabilidade#TM-HU-073). |

**Fluxo principal**

1. O usuário acessa as configurações de segurança da conta.
2. Aciona "encerrar todas as sessões ativas".
3. O sistema confirma a ação com o usuário.
4. O sistema encerra simultaneamente todas as sessões ativas vinculadas à conta.
5. O sistema exige nova autenticação nos dispositivos afetados.

**Fluxos de exceção**

- E1 — Falha ao encerrar alguma sessão remota: o sistema informa a situação e orienta nova tentativa, sem indicar sucesso indevido.

---

## Épico 13: Navegação e Interface Global (Protótipo)

### <a id="UC-066"></a>UC-066 — Navegar pela barra inferior do Explorador

| Campo | Especificação |
|-------|---------------|
| Objetivo | Mudar rapidamente de contexto por meio de uma barra de navegação inferior fixa com as seções principais do Explorador. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Aplicativo/página carregado no modo Explorador. |
| Pós-condições | Seção selecionada (Início, Explorar, Assistente, Comunidade ou Perfil) é exibida. |
| HU | [HU-074](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-074). |
| RF | [RF-074](Requisitos-Funcionais#RF-074). |
| RN | Nenhuma regra de negócio específica. |
| Rastreabilidade | [Linha TM-HU-074](Matriz-de-Rastreabilidade#TM-HU-074). |

**Fluxo principal**

1. O visitante visualiza a barra de navegação inferior fixa com as seções Início, Explorar, Assistente, Comunidade e Perfil.
2. Seleciona uma das seções.
3. O sistema exibe o conteúdo da seção escolhida, mantendo a barra fixa e destacando o item ativo.

**Fluxos de exceção**

- E1 — O visitante não autenticado seleciona "Perfil": o sistema solicita login antes de exibir a seção.

---

### <a id="UC-067"></a>UC-067 — Navegar pela barra inferior do Gestor

| Campo | Especificação |
|-------|---------------|
| Objetivo | Executar as atividades de gestão por meio de uma barra de navegação inferior fixa com as seções de gestão. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Gestor. |
| Atores secundários | Nenhum. |
| Pré-condições | Sessão válida no modo Gestor. |
| Pós-condições | Seção selecionada (Painel, Gerenciar, Indicadores, Novo Estabelecimento ou Perfil) é exibida. |
| HU | [HU-075](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-075). |
| RF | [RF-075](Requisitos-Funcionais#RF-075). |
| RN | Nenhuma regra de negócio específica. |
| Rastreabilidade | [Linha TM-HU-075](Matriz-de-Rastreabilidade#TM-HU-075). |

**Fluxo principal**

1. O gestor visualiza a barra de navegação inferior fixa com as seções Painel, Gerenciar, Indicadores, Novo Estabelecimento e Perfil.
2. Seleciona uma das seções.
3. O sistema exibe o conteúdo da seção escolhida, mantendo a barra fixa e destacando o item ativo.

**Fluxos de exceção**

- E1 — O gestor sem vínculo administrativo ativo seleciona "Gerenciar" ou "Indicadores": o sistema orienta a associação a um estabelecimento antes de exibir a seção.

---

### <a id="UC-068"></a>UC-068 — Consultar cabeçalho contextual da tela

| Campo | Especificação |
|-------|---------------|
| Objetivo | Orientar-se durante a navegação por meio de um cabeçalho fixo com título, contexto e ações da tela atual. |
| Prioridade | Should have — hipótese derivada do protótipo de alta fidelidade, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Tela carregada. |
| Pós-condições | Cabeçalho com título, contexto e ações pertinentes à tela é exibido. |
| HU | [HU-076](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-076). |
| RF | [RF-076](Requisitos-Funcionais#RF-076). |
| RN | Nenhuma regra de negócio específica. |
| Rastreabilidade | [Linha TM-HU-076](Matriz-de-Rastreabilidade#TM-HU-076). |

**Fluxo principal**

1. O visitante acessa qualquer tela da plataforma.
2. O sistema identifica o título, o contexto e as ações pertinentes à tela atual.
3. O sistema exibe o cabeçalho fixo correspondente no topo da tela.
## Épico 14: Fluxos de Uso em Validação

> [!WARNING]
> Os casos de uso deste épico documentam fluxos que já existiam como alternativos ou de exceção em outros casos de uso (Épicos 1 a 7) e foram extraídos como casos independentes. As histórias de usuário, os requisitos funcionais e as regras de negócio aqui referenciados foram derivados destes casos de uso e permanecem hipóteses pendentes de identificação e validação com stakeholders.

---

### <a id="UC-069"></a>UC-069 — Validar parâmetros de busca

| Campo | Especificação |
|-------|---------------|
| Objetivo | Garantir que os parâmetros informados pelo visitante atendam a formato, tamanho, cardinalidade, domínio e taxonomia antes de qualquer busca ser processada. |
| Prioridade | Must have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | O visitante informou termo e/ou filtros para pesquisar locais e eventos. |
| Pós-condições | Parâmetros válidos seguem para a etapa de pesquisa do caso base; parâmetros inválidos são rejeitados antes de qualquer consulta ser processada. |
| HU | [HU-077](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-077) |
| RF | [RF-077](Requisitos-Funcionais#RF-077) |
| RN | [RN-078](Regras-de-Neg%C3%B3cio#RN-078) |
| Rastreabilidade | [Linha TM-HU-077](Matriz-de-Rastreabilidade#TM-HU-077) |
| Tipo de relação | `<<include>>` — incluído por [UC-004](#UC-004) (pesquisa por termo) e [UC-005](#UC-005) (filtros por categoria e público); a validação executa sempre antes do processamento da consulta. |

**Fluxo principal**

1. O caso base ([UC-004](#UC-004) ou [UC-005](#UC-005)) inclui esta validação assim que o visitante envia termo e/ou filtros.
2. O sistema verifica formato, tamanho, cardinalidade, domínio e taxonomia de cada parâmetro informado.
3. Parâmetros válidos são liberados para a etapa de pesquisa do caso base.
4. O sistema retorna o controle ao caso base para prosseguir com a consulta.

**Fluxos alternativos**

- A1 — O visitante corrige o parâmetro apontado como inválido e reenvia a busca ao caso base.

**Fluxos de exceção**

- E1 — Valor de filtro fora do domínio permitido: o sistema rejeita a busca e oferece apenas valores aprovados, sem processar a consulta.
- E2 — Parâmetro em formato ou cardinalidade inválidos (por exemplo, caracteres não suportados ou número de filtros acima do limite): o sistema recusa o processamento e orienta o visitante sobre o formato esperado.

---

### <a id="UC-070"></a>UC-070 — Buscar por proximidade

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que o visitante compare locais e eventos por distância, a partir da localização atual ou de uma origem informada manualmente. |
| Prioridade | Should have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Serviço de Geolocalização. |
| Pré-condições | Pesquisa por termo ([UC-004](#UC-004)) ou filtragem ([UC-005](#UC-005)) em andamento; uso da localização atual depende de consentimento explícito. |
| Pós-condições | Resultados públicos e elegíveis com localização válida são ordenados por distância crescente, com origem e distância explícitas; ou a busca prossegue por cidade quando a proximidade não é viável. |
| HU | [HU-078](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-078) |
| RF | [RF-078](Requisitos-Funcionais#RF-078) |
| RN | [RN-079](Regras-de-Neg%C3%B3cio#RN-079), [RN-080](Regras-de-Neg%C3%B3cio#RN-080) |
| Rastreabilidade | [Linha TM-HU-078](Matriz-de-Rastreabilidade#TM-HU-078) |
| Tipo de relação | `<<extend>>` de [UC-004](#UC-004) e [UC-005](#UC-005). |
| Condição de extensão | O visitante opta por ordenar os resultados por proximidade. |

**Fluxo principal**

1. Durante a pesquisa ([UC-004](#UC-004)) ou a filtragem ([UC-005](#UC-005)), o visitante escolhe “Mais próximos”.
2. O sistema solicita consentimento para uso da localização atual.
3. O Serviço de Geolocalização retorna a posição atual, ou o visitante informa bairro, cidade ou ponto de referência como origem manual.
4. O sistema calcula a distância dos registros públicos e elegíveis com localização válida.
5. O sistema ordena os resultados por distância crescente e retorna o controle ao caso estendido.

**Fluxos alternativos**

- A1 — O visitante prefere não usar a localização atual e informa diretamente um bairro, cidade ou ponto de referência como origem.

**Fluxos de exceção**

- E1 — Permissão de localização negada ou posição indisponível: a busca continua por cidade e o sistema oferece a origem manual, sem bloquear o catálogo.
- E2 — Distância não calculável para um registro: o item pode permanecer no resultado, mas sem distância estimada e sem ser indevidamente priorizado como próximo.

---

### <a id="UC-071"></a>UC-071 — Consultar procedência do dado e abrir canal externo

| Campo | Especificação |
|-------|---------------|
| Objetivo | Dar visibilidade à fonte, à data da última verificação e ao estado de revisão dos dados sensíveis à atualização, e permitir abrir um canal externo oficial. |
| Prioridade | Must have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Local ou evento publicado exibindo dado sensível à atualização (horários, preços, contatos, localização, programação, segurança ou acessibilidade). |
| Pós-condições | Fonte, data de verificação e eventual estado “em revisão” ficam visíveis; canal externo é aberto após ação do visitante, ou o dado local permanece visível caso o canal falhe. |
| HU | [HU-079](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-079) |
| RF | [RF-079](Requisitos-Funcionais#RF-079), [RF-035](Requisitos-Funcionais#RF-035) |
| RN | [RN-081](Regras-de-Neg%C3%B3cio#RN-081), [RN-082](Regras-de-Neg%C3%B3cio#RN-082), [RN-083](Regras-de-Neg%C3%B3cio#RN-083) |
| Rastreabilidade | [Linha TM-HU-079](Matriz-de-Rastreabilidade#TM-HU-079) |
| Tipo de relação | `<<include>>` — incluído por [UC-006](#UC-006), [UC-007](#UC-007), [UC-009](#UC-009) e [UC-010](#UC-010), sempre que exibem dado sensível à atualização. |

**Fluxo principal**

1. O caso base inclui esta consulta ao apresentar um dado sensível à atualização.
2. O sistema identifica a fonte e a data da última verificação do dado.
3. O sistema sinaliza o estado “em revisão” quando há apuração em curso.
4. O visitante aciona um link de mapa/trajeto, telefone, WhatsApp, e-mail, site oficial, rede social oficial ou reserva/ingresso oficial.
5. O sistema abre o canal externo somente após a ação do visitante.

**Fluxos alternativos**

- A1 — Link oficial disponível: o sistema abre o serviço externo diretamente após a confirmação do visitante.

**Fluxos de exceção**

- E1 — Dado desatualizado ou ainda não verificado: o sistema sinaliza a limitação sem ocultar a informação.
- E2 — Serviço externo indisponível: os dados locais permanecem visíveis e o sistema informa que o trajeto ou link não pôde ser aberto, sem expor detalhes técnicos.

---

### <a id="UC-072"></a>UC-072 — Filtrar agenda por data e ocultar itens encerrados

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir refinar a agenda pública por data e assegurar que atrações e eventos encerrados não apareçam como disponíveis. |
| Prioridade | Must have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Nenhum. |
| Pré-condições | Calendário ou agenda de eventos em consulta ([UC-009](#UC-009)). |
| Pós-condições | Agenda exibida reflete apenas o período filtrado e somente itens vigentes; itens encerrados permanecem inativos ou arquivados. |
| HU | [HU-080](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-080) |
| RF | [RF-080](Requisitos-Funcionais#RF-080), [RF-081](Requisitos-Funcionais#RF-081) |
| RN | [RN-084](Regras-de-Neg%C3%B3cio#RN-084) |
| Rastreabilidade | [Linha TM-HU-080](Matriz-de-Rastreabilidade#TM-HU-080) |
| Tipo de relação | `<<extend>>` de [UC-009](#UC-009). |
| Condição de extensão | O visitante filtra a agenda por data. |

**Fluxo principal**

1. Durante a consulta ao calendário ([UC-009](#UC-009)), o visitante informa uma data ou período.
2. O sistema filtra a agenda pública pelo período informado.
3. O sistema verifica o estado de cada evento/atração do período.
4. O sistema retira da lista qualquer item encerrado, mantendo-o apenas inativo ou arquivado.
5. O sistema retorna a agenda filtrada ao caso estendido.

**Fluxos alternativos**

- A1 — O visitante combina o filtro de data com cidade ou categoria.

**Fluxos de exceção**

- E1 — Não há item vigente no período informado: o sistema informa a ausência de resultados sem sugerir agenda inexistente.

---

### <a id="UC-073"></a>UC-073 — Retomar rascunho após autenticação

| Campo | Especificação |
|-------|---------------|
| Objetivo | Preservar o conteúdo já preenchido em uma avaliação ou sinalização e restaurá-lo automaticamente após o usuário concluir a autenticação exigida para o envio. |
| Prioridade | Should have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Usuário iniciou o preenchimento de uma avaliação ([UC-013](#UC-013)) ou de uma sinalização de dado incorreto ([UC-080](#UC-080)) sem estar autenticado. |
| Pós-condições | Conteúdo preenchido é restaurado após a autenticação; o rascunho é descartado após o envio ou o descarte explícito. |
| HU | [HU-081](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-081) |
| RF | [RF-082](Requisitos-Funcionais#RF-082) |
| RN | [RN-085](Regras-de-Neg%C3%B3cio#RN-085) |
| Rastreabilidade | [Linha TM-HU-081](Matriz-de-Rastreabilidade#TM-HU-081) |
| Tipo de relação | `<<extend>>` de [UC-013](#UC-013) e [UC-080](#UC-080). |
| Condição de extensão | O envio do conteúdo exige autenticação e o usuário já preencheu conteúdo antes de autenticar. |

**Fluxo principal**

1. O usuário preenche nota, comentário ou dados de sinalização no caso estendido ([UC-013](#UC-013) ou [UC-080](#UC-080)) sem sessão autenticada.
2. Ao tentar enviar, o sistema identifica a exigência de autenticação e retém temporariamente o conteúdo preenchido.
3. O sistema solicita que o usuário se autentique.
4. Após a autenticação, o sistema restaura o conteúdo preenchido no formulário de origem.
5. O usuário confirma o envio, e o sistema descarta o rascunho temporário.

**Fluxos alternativos**

- A1 — O usuário desiste do envio: o sistema descarta o rascunho preservado de forma explícita.

**Fluxos de exceção**

- E1 — A autenticação não é concluída dentro do prazo de retenção do rascunho: o sistema descarta o conteúdo e informa que será necessário preenchê-lo novamente.

---

### <a id="UC-074"></a>UC-074 — Receber alternativa quando a personalização é insuficiente

| Campo | Especificação |
|-------|---------------|
| Objetivo | Garantir que o usuário continue descobrindo locais mesmo quando não há dados suficientes ou autorizados para gerar recomendações personalizadas. |
| Prioridade | Should have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Consulta de recomendações por histórico ([UC-014](#UC-014)), por avaliações ([UC-015](#UC-015)) ou por perfis similares ([UC-016](#UC-016)) em andamento. |
| Pós-condições | Usuário recebe pedido de interesses ou uma lista de opções gerais elegíveis, sem que o fluxo de recomendação seja interrompido. |
| HU | [HU-082](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-082) |
| RF | [RF-083](Requisitos-Funcionais#RF-083) |
| RN | [RN-086](Regras-de-Neg%C3%B3cio#RN-086) |
| Rastreabilidade | [Linha TM-HU-082](Matriz-de-Rastreabilidade#TM-HU-082) |
| Tipo de relação | `<<extend>>` de [UC-014](#UC-014), [UC-015](#UC-015) e [UC-016](#UC-016). |
| Condição de extensão | Os dados históricos, de avaliações ou de perfis disponíveis são insuficientes para calcular a personalização. |

**Fluxo principal**

1. O caso estendido ([UC-014](#UC-014), [UC-015](#UC-015) ou [UC-016](#UC-016)) verifica que não há dados suficientes ou autorizados para o critério de recomendação.
2. O sistema solicita ao usuário que informe interesses diretamente.
3. Caso o usuário não informe, o sistema apresenta opções gerais públicas e elegíveis.
4. O sistema retorna o controle ao caso estendido com o conjunto de locais obtido.

**Fluxos alternativos**

- A1 — O usuário informa interesses: o sistema os usa para refinar a lista de opções gerais.

**Fluxos de exceção**

- E1 — Usuário não autorizou o uso do histórico necessário ao critério: esse histórico é ignorado e a alternativa é aplicada mesmo assim.

---

### <a id="UC-075"></a>UC-075 — Salvar e ajustar roteiro pessoal

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que o usuário salve o roteiro gerado, reorganize ou substitua locais, e receba explicação quando não houver combinação viável. |
| Prioridade | Must have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Roteiro personalizado gerado ([UC-017](#UC-017)). |
| Pós-condições | Roteiro é persistido, pertence ao usuário e reflete as alterações feitas; trechos afetados por substituição são recalculados. |
| HU | [HU-083](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-083) |
| RF | [RF-084](Requisitos-Funcionais#RF-084) |
| RN | [RN-087](Regras-de-Neg%C3%B3cio#RN-087) |
| Rastreabilidade | [Linha TM-HU-083](Matriz-de-Rastreabilidade#TM-HU-083) |
| Tipo de relação | `<<include>>` — incluído por [UC-017](#UC-017), ao final da geração do roteiro. |

**Fluxo principal**

1. O caso [UC-017](#UC-017) inclui este caso após gerar a sequência de passeio.
2. O usuário revisa o roteiro proposto.
3. O usuário salva o roteiro, que passa a pertencer ao seu perfil.
4. O usuário reorganiza manualmente a ordem dos locais, ou remove/substitui um local.
5. O sistema recalcula os trechos afetados pela alteração.
6. O sistema salva a nova versão do roteiro.

**Fluxos alternativos**

- A1 — Usuário reorganiza manualmente; o sistema preserva a ordem definida sem reordenar automaticamente.
- A2 — Usuário remove ou substitui um local; o sistema recalcula somente os trechos afetados.

**Fluxos de exceção**

- E1 — Não há combinação viável após a alteração: o sistema explica as restrições identificadas e sugere flexibilizações.

---

### <a id="UC-076"></a>UC-076 — Alertar item de checklist vinculado a atração inativa

| Campo | Especificação |
|-------|---------------|
| Objetivo | Avisar o usuário quando um item de seu checklist estiver vinculado a uma atração inativa, sem alterar o progresso pessoal nem o dado oficial. |
| Prioridade | Should have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Checklist com item vinculado a uma atração que passou a inativa ou arquivada ([UC-020](#UC-020)). |
| Pós-condições | Usuário visualiza o alerta; o andamento pessoal e o dado oficial da atração permanecem inalterados. |
| HU | [HU-084](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-084) |
| RF | [RF-085](Requisitos-Funcionais#RF-085) |
| RN | [RN-088](Regras-de-Neg%C3%B3cio#RN-088) |
| Rastreabilidade | [Linha TM-HU-084](Matriz-de-Rastreabilidade#TM-HU-084) |
| Tipo de relação | `<<extend>>` de [UC-020](#UC-020). |
| Condição de extensão | O item do checklist está vinculado a uma atração inativa ou arquivada. |

**Fluxo principal**

1. O usuário abre o checklist ([UC-020](#UC-020)).
2. O sistema verifica o estado da atração vinculada a cada item.
3. O sistema identifica um item cuja atração está inativa ou arquivada.
4. O sistema exibe um alerta visível ao lado do item, sem bloquear as demais interações do checklist.

**Fluxos alternativos**

- A1 — A atração volta a ficar ativa: o alerta deixa de ser exibido no próximo carregamento do checklist.

**Fluxos de exceção**

- E1 — Usuário tenta marcar o item alertado como concluído: o sistema permite a marcação pessoal, mas mantém o alerta visível, deixando claro que o dado oficial não foi alterado.

---

### <a id="UC-077"></a>UC-077 — Votar em enquete sob as regras de ciclo de vida

| Campo | Especificação |
|-------|---------------|
| Objetivo | Registrar o voto do participante e assegurar que a enquete, do começo ao fim, obedeça às regras de edição, encerramento, múltipla escolha e antifraude. |
| Prioridade | Could have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Votante anônimo. |
| Atores secundários | Criador da enquete (usuário autenticado), nas regras de alteração de opções e de encerramento. |
| Pré-condições | Enquete criada com ao menos duas opções válidas ([UC-029](#UC-029)); link público disponível. |
| Pós-condições | Voto é contabilizado sem exigir login nem identificar o votante; resultado é atualizado; a enquete respeita as regras de edição e encerramento ao longo de todo o ciclo. |
| HU | [HU-085](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-085) |
| RF | [RF-086](Requisitos-Funcionais#RF-086) |
| RN | [RN-089](Regras-de-Neg%C3%B3cio#RN-089) |
| Rastreabilidade | [Linha TM-HU-085](Matriz-de-Rastreabilidade#TM-HU-085) |
| Tipo de relação | `<<include>>` — incluído por [UC-029](#UC-029), que aplica o ciclo de vida e o antifraude desde a criação da enquete. |

**Fluxo principal**

1. O caso [UC-029](#UC-029) inclui este caso a partir da criação da enquete e mantém suas regras válidas durante toda a existência dela.
2. O votante abre o link público e o sistema mostra as opções e a situação atual da enquete.
3. O votante escolhe uma opção (ou, se permitido, múltiplas até o limite definido) e confirma.
4. O sistema aplica os controles antifraude sem expor a identidade do votante.
5. O sistema contabiliza o voto e atualiza o resultado.

**Fluxos alternativos**

- A1 — Configuração permite múltipla escolha: o votante seleciona até o limite entre 1 e o número de opções definido pelo criador.
- A2 — O criador altera as opções da enquete antes de registrado o primeiro voto.
- A3 — O criador encerra a enquete manualmente antes do prazo previsto.

**Fluxos de exceção**

- E1 — Enquete encerrada: o sistema não registra o voto e mostra apenas o resultado disponível.
- E2 — Controle antifraude rejeita duplicidade de voto: o sistema informa ao votante que o voto não foi aceito.

---

### <a id="UC-078"></a>UC-078 — Revogar link público de lista

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que o proprietário interrompa o compartilhamento de uma lista pessoal revogando seu link público. |
| Prioridade | Should have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Usuário autenticado. |
| Atores secundários | Nenhum. |
| Pré-condições | Link público da lista já gerado ([UC-032](#UC-032)); usuário é o proprietário da lista. |
| Pós-condições | Link revogado; qualquer acesso posterior é negado sem exibir a lista. |
| HU | [HU-086](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-086) |
| RF | [RF-087](Requisitos-Funcionais#RF-087) |
| RN | [RN-090](Regras-de-Neg%C3%B3cio#RN-090) |
| Rastreabilidade | [Linha TM-HU-086](Matriz-de-Rastreabilidade#TM-HU-086) |
| Tipo de relação | `<<extend>>` de [UC-032](#UC-032). |
| Condição de extensão | O proprietário revoga o link já gerado. |

**Fluxo principal**

1. O proprietário acessa a lista já compartilhada ([UC-032](#UC-032)).
2. Aciona a opção de revogar o link público.
3. O sistema confirma a ação com o proprietário.
4. O sistema invalida o link vigente.
5. O sistema informa que o compartilhamento foi interrompido.

**Fluxos de exceção**

- E1 — A lista não pertence ao usuário que solicita a revogação: o sistema nega a operação.
- E2 — Alguém tenta acessar o link após a revogação: o sistema nega o acesso sem exibir a lista.

---

### <a id="UC-079"></a>UC-079 — Acionar contato de transporte parceiro

| Campo | Especificação |
|-------|---------------|
| Objetivo | Permitir que o visitante inicie contato direto com um parceiro de transporte elegível, sem que a plataforma garanta contratação ou disponibilidade. |
| Prioridade | Could have — hipótese derivada do caso de uso, pendente de validação com stakeholders. |
| Ator principal | Visitante. |
| Atores secundários | Serviço/operador de transporte parceiro. |
| Pré-condições | Parceiro de transporte ativo, com área atendida e contato público compatíveis com o local ou evento ([UC-030](#UC-030)). |
| Pós-condições | Canal externo do parceiro é aberto após confirmação do visitante, sem garantia de contratação ou disponibilidade. |
| HU | [HU-087](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-087) |
| RF | [RF-088](Requisitos-Funcionais#RF-088) |
| RN | [RN-091](Regras-de-Neg%C3%B3cio#RN-091) |
| Rastreabilidade | [Linha TM-HU-087](Matriz-de-Rastreabilidade#TM-HU-087) |
| Tipo de relação | `<<extend>>` de [UC-030](#UC-030). |
| Condição de extensão | Existe parceiro ativo, com área atendida e contato público compatíveis com o local/evento em consulta. |

**Fluxo principal**

1. O visitante consulta as opções de transporte parceiro do local/evento ([UC-030](#UC-030)).
2. O visitante escolhe uma opção elegível.
3. O sistema solicita confirmação antes de acionar o contato externo.
4. Confirmada a ação, o sistema abre o canal do Serviço/operador de transporte parceiro (telefone, WhatsApp ou canal equivalente).

**Fluxos alternativos**

- A1 — Não há parceiro elegível: a extensão não é acionada e o visitante permanece apenas com as informações gerais de acesso e trajeto do caso base.

**Fluxos de exceção**

- E1 — Canal do parceiro indisponível: o sistema informa a falha sem garantir contratação ou disponibilidade e sem expor detalhes técnicos.

---

### <a id="UC-080"></a>UC-080 — Sinalizar e acompanhar dado incorreto

| Campo | Especificação |
|-------|---------------|
| Objetivo | Fechar o ciclo entre uma inconsistência percebida pela comunidade e a revisão do cadastro oficial. |
| Prioridade | **Must have** — dor recorrente e diretamente validada nas [entrevistas](Relat%C3%B3rio-de-Entrevistas) e no [questionário](Question%C3%A1rio-com-Usu%C3%A1rios). |
| Ator principal | Usuário autenticado. |
| Atores secundários | Administrador autorizado, em função de curadoria; responsável pelo local, quando identificável. |
| Pré-condições | Local, evento, equipamento cultural ou atração publicado; usuário autenticado para concluir o envio. |
| Pós-condições | Sinalização possui protocolo e estado rastreável; após análise, o dado é corrigido, mantido com justificativa ou marcado como não verificável; o autor recebe o resultado. |
| HU | [HU-088](Hist%C3%B3rias-de-Usu%C3%A1rio#HU-088) |
| RF | [RF-089](Requisitos-Funcionais#RF-089), [RF-22A](Requisitos-Funcionais#RF-22A) |
| RN | Tratamento da sinalização: [RN-092](Regras-de-Neg%C3%B3cio#RN-092), [RN-093](Regras-de-Neg%C3%B3cio#RN-093). Regras que definem o dado correto nos campos sinalizáveis: [RN-015](Regras-de-Neg%C3%B3cio#RN-015), [RN-017](Regras-de-Neg%C3%B3cio#RN-017), [RN-019](Regras-de-Neg%C3%B3cio#RN-019), [RN-021](Regras-de-Neg%C3%B3cio#RN-021), [RN-024](Regras-de-Neg%C3%B3cio#RN-024), [RN-027](Regras-de-Neg%C3%B3cio#RN-027), [RN-037](Regras-de-Neg%C3%B3cio#RN-037), [RN-038](Regras-de-Neg%C3%B3cio#RN-038). |
| Rastreabilidade | [Linha TM-HU-088](Matriz-de-Rastreabilidade#TM-HU-088) |
| Tipo de relação | `<<extend>>` de [UC-006](#UC-006), [UC-007](#UC-007), [UC-009](#UC-009), [UC-010](#UC-010), [UC-036](#UC-036) e [UC-042](#UC-042). |
| Condição de extensão | O usuário aciona “Sinalizar dado incorreto” na página do local, evento, equipamento cultural ou atração. |
| Pontos de extensão | [UC-073](#UC-073), quando o envio da sinalização exige autenticação com conteúdo já preenchido. |

O **administrador autorizado**, em função de curadoria, é o responsável operacional por validar a sinalização e fechar o ciclo. Essa atribuição usa o papel administrativo existente e não cria novo papel de acesso.

**Fluxo principal**

1. O usuário aciona “Sinalizar dado incorreto” no local, evento, equipamento cultural ou atração.
2. Seleciona o campo afetado, informa o valor observado, data da constatação e, opcionalmente, anexa evidência.
3. O sistema valida o envio, preserva uma cópia do valor publicado e cria um protocolo com estado “pendente”.
4. O administrador em função de curadoria compara a sinalização com fonte verificável e, quando necessário, solicita confirmação ao responsável pelo local.
5. Confirmada a inconsistência, o administrador corrige ou invalida o campo e registra fonte, data, responsável e justificativa da decisão.
6. O sistema atualiza a data de verificação, encerra o protocolo e comunica o resultado ao usuário que sinalizou.

**Fluxos alternativos**

- A1 — Já existe sinalização equivalente pendente: o sistema associa o novo relato ao protocolo existente, preservando autoria e evidências.
- A2 — A apuração ainda não terminou: o campo permanece “em revisão” sem substituir automaticamente o dado oficial.
- A3 — A sinalização não procede: o administrador mantém o valor, registra a justificativa e comunica o encerramento.
- A4 — O usuário inicia a sinalização sem estar autenticado: aciona-se a extensão [UC-073](#UC-073), que preserva o conteúdo preenchido e retoma o envio após a autenticação.

**Fluxos de exceção**

- E1 — Evidência inválida ou maliciosa: o arquivo é bloqueado e a sinalização textual pode continuar se contiver dados suficientes.
- E2 — Campo crítico não pode ser verificado e pode causar risco imediato: o sistema o oculta preventivamente.
- E3 — Falha ao registrar o protocolo: nenhum cadastro é alterado e o sistema orienta nova tentativa.
