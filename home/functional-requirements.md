---
title: Requisitos Funcionais
---

1. [Épico 1: Exploração e Descoberta](#épico-1-exploração-e-descoberta)
2. [Épico 2: Informações e Detalhes do Local](#épico-2-informações-e-detalhes-do-local)
3. [Épico 3: Avaliações e Comunidade](#épico-3-avaliações-e-comunidade)
4. [Épico 4: Recomendações Personalizadas](#épico-4-recomendações-personalizadas)
5. [Épico 5: Organização Pessoal e Roteiros](#épico-5-organização-pessoal-e-roteiros)
6. [Épico 6: Assistente Virtual (Chatbot)](#épico-6-assistente-virtual-chatbot)
7. [Épico 7: Interações Sociais e Compartilhamento](#épico-7-interações-sociais-e-compartilhamento)
8. [Épico 8: Equipamentos Culturais e Estabelecimentos](#épico-8-equipamentos-culturais-e-estabelecimentos)
9. [Épico 9: Avaliações e Comunidade (Protótipo)](#épico-9-avaliações-e-comunidade-protótipo)
10. [Épico 10: Organização Pessoal e Gamificação (Protótipo)](#épico-10-organização-pessoal-e-gamificação-protótipo)
11. [Épico 11: Gestão de Estabelecimentos (Protótipo)](#épico-11-gestão-de-estabelecimentos-protótipo)
12. [Épico 12: Perfil, Autenticação e Parceria (Protótipo)](#épico-12-perfil-autenticação-e-parceria-protótipo)
13. [Épico 13: Navegação e Interface Global (Protótipo)](#épico-13-navegação-e-interface-global-protótipo)

---

## Critérios de Priorização MoSCoW

- **Must have**: requisito indispensável para a primeira entrega validada do produto.
- **Should have**: requisito importante, mas que pode ser entregue após o núcleo principal sem inviabilizar a solução.
- **Could have**: requisito desejável, condicionado à disponibilidade de tempo e recursos.
- **Won't have**: requisito fora do escopo da entrega atual ou pendente de validação antes de entrar no planejamento.

---

### Épico 1: Exploração e Descoberta

| id     | requisito                                                                                                                           | prioridade (MoSCoW) |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-001"></a>RF-001 | O sistema deve disponibilizar um catálogo regional unificado de locais turísticos, culturais, gastronômicos, comerciais e de lazer. | Must have           |
| <a id="RF-002"></a>RF-002 | O sistema deve exibir listas de locais e experiências com alta visitação ou popularidade.                                           | Should have         |
| <a id="RF-003"></a>RF-003 | O sistema deve exibir listas de locais e experiências pouco divulgadas ou alternativas.                                             | Should have         |
| <a id="RF-004"></a>RF-004 | O sistema deve permitir pesquisa de locais e eventos por palavras-chave, nome, categoria e cidade.                                  | Must have           |
| <a id="RF-005"></a>RF-005 | O sistema deve fornecer sugestões alternativas (termos ou categorias) quando uma busca não retornar resultados.                     | Should have         |
| <a id="RF-006"></a>RF-006 | O sistema deve permitir a filtragem de locais e eventos por categoria e adequação ao público (ex: infantil, famílias).              | Must have           |

### Épico 2: Informações e Detalhes do Local

| id     | requisito                                                                                                                                                                                                     | prioridade (MoSCoW) |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-007"></a>RF-007 | O sistema deve exibir informações descritivas básicas do local, como resumo contextual, categoria e tipo de experiência.                                                                                      | Must have           |
| <a id="RF-008"></a>RF-008 | O sistema deve exibir fotos, mídias e características do ambiente físico dos locais.                                                                                                                          | Must have           |
| <a id="RF-009"></a>RF-009 | O sistema deve exibir horários de funcionamento, status atual (aberto/fechado) e indicar possíveis opções de atividades noturnas.                                                                             | Must have           |
| <a id="RF-010"></a>RF-010 | O sistema deve disponibilizar informações financeiras, incluindo cardápio, faixa de preços, taxas e couvert artístico (quando aplicável).                                                                     | Must have           |
| <a id="RF-011"></a>RF-011 | O sistema deve apresentar dados de localização, trajeto, formas de acesso, opções de transporte e estabelecimentos próximos.                                                                                  | Must have           |
| <a id="RF-012"></a>RF-012 | O sistema deve disponibilizar informações específicas sobre a segurança do local e de seu entorno.                                                                                                            | Must have           |
| <a id="RF-013"></a>RF-013 | O sistema deve disponibilizar informações qualitativas sobre as condições de higiene do estabelecimento.                                                                                                      | Should have         |
| <a id="RF-014"></a>RF-014 | O sistema deve indicar de forma clara os recursos de acessibilidade disponíveis no local.                                                                                                                     | Must have           |
| <a id="RF-015"></a>RF-015 | O sistema deve informar se o local conta com estrutura e adequação para receber o público infantil.                                                                                                           | Should have         |
| <a id="RF-016"></a>RF-016 | O sistema deve exibir calendário e detalhes, como programações musicais, datas e horários dos eventos cadastrados.                                                                                            | Must have           |
| <a id="RF-017"></a>RF-017 | O sistema deve informar os canais de contato atualizados do estabelecimento de forma acessível.                                                                                                               | Should have         |
| <a id="RF-018"></a>RF-018 | O sistema deve fornecer informações e curiosidades históricas, culturais e sociais relacionadas aos locais da região.                                                                                         | Should have         |
| <a id="RF-019"></a>RF-019 | O sistema deve exibir as regras e políticas do local, incluindo itens permitidos e proibidos, restrições de entrada e condições especiais de acesso ou preço.                                                 | Should have         |
| <a id="RF-020"></a>RF-020 | O sistema deve informar o formato de serviço do estabelecimento (ex: atendimento na mesa, self-service, rodízio com garçom, rodízio com fila, balcão), para que o usuário conheça a dinâmica antes da visita. | Should have         |

### Épico 3: Avaliações e Comunidade

| id     | requisito                                                                                                                   | prioridade (MoSCoW) |
| ------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-021"></a>RF-021 | O sistema deve exibir avaliações e comentários públicos deixados por outros visitantes sobre os locais.                     | Must have           |
| <a id="RF-022"></a>RF-022 | O sistema deve permitir que o usuário publique suas próprias avaliações e comentários a respeito dos locais e experiências. | Should have         |

### Épico 4: Recomendações Personalizadas

| id     | requisito                                                                                                                        | prioridade (MoSCoW) |
| ------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-023"></a>RF-023 | O sistema deve exibir recomendações de locais com base no histórico de visitas anteriores do usuário.                            | Should have         |
| <a id="RF-024"></a>RF-024 | O sistema deve fornecer recomendações de locais alinhadas às avaliações realizadas pelo usuário.                                 | Should have         |
| <a id="RF-025"></a>RF-025 | O sistema deve sugerir locais considerando os interesses de usuários com perfis compatíveis (filtragem de interesses similares). | Could have          |
| <a id="RF-026"></a>RF-026 | O sistema deve gerar e recomendar roteiros elaborados e personalizados de passeios de acordo com o interesse do usuário.         | Must have           |

### Épico 5: Organização Pessoal e Roteiros

| id     | requisito                                                                                                   | prioridade (MoSCoW) |
| ------ | ----------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-027"></a>RF-027 | O sistema deve permitir criar, organizar e gerenciar listas de locais que o usuário tem desejo de visitar.  | Must have           |
| <a id="RF-028"></a>RF-028 | O sistema deve permitir que o usuário sinalize e registre os locais físicos que já visitou no passado.      | Should have         |
| <a id="RF-029"></a>RF-029 | O sistema deve disponibilizar checklists de apoio para acompanhamento das atividades e passeios do usuário. | Must have           |

### Épico 6: Assistente Virtual (Chatbot)

| id     | requisito                                                                                                                                                    | prioridade (MoSCoW) |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| <a id="RF-030"></a>RF-030 | O sistema deve disponibilizar um assistente virtual conversacional para responder dúvidas de lugares e eventos.                                              | Must have           |
| <a id="RF-031"></a>RF-031 | O sistema deve ser capaz de interpretar a intenção de busca do usuário no assistente virtual para retornar as informações ou recomendações mais pertinentes. | Must have           |
| <a id="RF-032"></a>RF-032 | O sistema deve orientar alternativas ou repasses no próprio assistente quando este não possuir a informação exata.                                           | Should have         |
| <a id="RF-033"></a>RF-033 | O sistema deve permitir acionar o assistente de forma contextualizada, permitindo a continuidade direta de uma pesquisa em andamento.                        | Must have           |
| <a id="RF-034"></a>RF-034 | O sistema deve disponibilizar um módulo para importar e atualizar as informações de locais e eventos a partir de fontes de dados externas.                   | Must have           |
| <a id="RF-035"></a>RF-035 | O sistema deve ser capaz de disponibilizar links externos para perfis públicos do ponto turístico (caso aplicável).                                          | Should have         |
| <a id="RF-036"></a>RF-036 | O sistema deve exibir imagens disponíveis acerca do local de visita/passeio.                                                                                 | Should have         |
| <a id="RF-037"></a>RF-037 | O sistema deve ser capaz de interpretar prompts de áudio e devolver resultados em texto.                                                                     | Could have          |

### Épico 7: Interações Sociais e Compartilhamento

| id     | requisito                                                                                                                                                        | prioridade (MoSCoW) |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-038"></a>RF-038 | O sistema deve permitir que usuários criem enquetes compartilháveis (via link) de locais ou eventos, permitindo votação anônima sem necessidade de autenticação. | Could have          |
| <a id="RF-039"></a>RF-039 | O sistema deve listar contatos e opções de serviços de transporte alternativo e parceiros locais (ex: mototáxis, vans) atrelados a estabelecimentos ou eventos.  | Should have         |
| <a id="RF-040"></a>RF-040 | O sistema deve possuir uma seção para exibição de mídias (fotos e vídeos curtos) geradas exclusivamente pela comunidade de usuários sobre os locais.             | Could have          |
| <a id="RF-041"></a>RF-041 | O sistema deve permitir que o usuário gere um link público ou compartilhe externamente suas listas personalizadas de locais favoritos.                           | Should have         |

### Épico 8: Equipamentos Culturais e Estabelecimentos

> [!WARNING]
> Os requisitos deste épico não possuem procedência identificada em stakeholders.
> Eles representam escopo administrativo e devem ser revisados antes da validação final.

| id     | requisito                                                                                                                            | prioridade (MoSCoW) |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| <a id="RF-042"></a>RF-042 | O sistema deve permitir o cadastro de equipamentos culturais.                                                                        | Won't have          |
| <a id="RF-043"></a>RF-043 | O sistema deve permitir a edição de informações de equipamentos culturais cadastrados.                                               | Won't have          |
| <a id="RF-044"></a>RF-044 | O sistema deve permitir a consulta de informações de equipamentos culturais.                                                         | Won't have          |
| <a id="RF-045"></a>RF-045 | O sistema deve permitir a associação de administradores a equipamentos culturais.                                                    | Won't have          |
| <a id="RF-046"></a>RF-046 | O sistema deve permitir a autenticação de administradores.                                                                           | Won't have          |
| <a id="RF-047"></a>RF-047 | O sistema deve permitir que administradores de equipamentos culturais cadastrem atrações.                                            | Won't have          |
| <a id="RF-048"></a>RF-048 | O sistema deve permitir que administradores editem atrações cadastradas.                                                             | Won't have          |
| <a id="RF-049"></a>RF-049 | O sistema deve permitir que administradores removam atrações cadastradas.                                                            | Won't have          |
| <a id="RF-050"></a>RF-050 | O sistema deve permitir a consulta de atrações cadastradas.                                                                          | Won't have          |
| <a id="RF-051"></a>RF-051 | O sistema deve permitir o cadastro de estabelecimentos gastronômicos.                                                                | Won't have          |
| <a id="RF-052"></a>RF-052 | O sistema deve permitir que administradores de estabelecimentos gastronômicos cadastrem ofertas.                                     | Won't have          |
| <a id="RF-053"></a>RF-053 | O sistema deve permitir que administradores editem ofertas cadastradas.                                                              | Won't have          |
| <a id="RF-054"></a>RF-054 | O sistema deve permitir que administradores removam ofertas cadastradas.                                                             | Won't have          |
| <a id="RF-055"></a>RF-055 | O sistema deve permitir o cadastro de publicações.                                                                                   | Won't have          |
| <a id="RF-056"></a>RF-056 | O sistema deve permitir que administradores criem publicações associadas a equipamentos culturais ou estabelecimentos gastronômicos. | Won't have          |
| <a id="RF-057"></a>RF-057 | O sistema deve permitir a edição de publicações cadastradas.                                                                         | Won't have          |
| <a id="RF-058"></a>RF-058 | O sistema deve permitir a remoção de publicações cadastradas.                                                                        | Won't have          |

### Épico 9: Avaliações e Comunidade (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                                    | prioridade (MoSCoW) |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-059"></a>RF-059 | O sistema deve permitir que usuários marquem avaliações de outros usuários como úteis e deve exibir publicamente a quantidade de marcações recebidas por cada avaliação. | Should have         |
| <a id="RF-060"></a>RF-060 | O sistema deve permitir o compartilhamento externo de uma avaliação pública individual por meio de link ou aplicativo compatível.                                        | Could have          |
| <a id="RF-061"></a>RF-061 | O sistema deve permitir que usuários iniciem tópicos de discussão associados a locais ou eventos na seção de comunidade.                                                 | Should have         |

### Épico 10: Organização Pessoal e Gamificação (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                     | prioridade (MoSCoW) |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-062"></a>RF-062 | O sistema deve exibir conquistas e distintivos desbloqueáveis de acordo com o engajamento do usuário, como visitas registradas, avaliações publicadas e check-ins realizados. | Could have          |
| <a id="RF-063"></a>RF-063 | O sistema deve exibir dicas contextuais curadas sobre o local associado ao checklist de visita do usuário.                                                                    | Could have          |

### Épico 11: Gestão de Estabelecimentos (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                                                                               | prioridade (MoSCoW) |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-064"></a>RF-064 | O sistema deve exibir ao gestor um painel com métricas resumidas dos estabelecimentos gerenciados, incluindo visitantes, avaliações recentes e eventos ativos.                                                                          | Should have         |
| <a id="RF-065"></a>RF-065 | O sistema deve exibir ao gestor um feed cronológico das atividades recentes relacionadas aos estabelecimentos gerenciados, como novas avaliações, visualizações e interações.                                                           | Could have          |
| <a id="RF-066"></a>RF-066 | O sistema deve permitir que administradores de estabelecimentos respondam publicamente às avaliações realizadas por usuários.                                                                                                            | Should have         |
| <a id="RF-067"></a>RF-067 | O sistema deve permitir que o gestor visualize a página pública do estabelecimento como ela é apresentada aos usuários.                                                                                                                 | Could have          |
| <a id="RF-068"></a>RF-068 | O sistema deve disponibilizar ao gestor um painel de indicadores e análises sobre o desempenho do estabelecimento, incluindo fluxo de visitantes, perfil do público, horários de pico e visibilidade regional.                         | Should have         |
| <a id="RF-069"></a>RF-069 | O sistema deve apresentar ao gestor um mapa com a distribuição geográfica agregada da origem dos visitantes do estabelecimento.                                                                                                         | Could have          |

### Épico 12: Perfil, Autenticação e Parceria (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                            | prioridade (MoSCoW) |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <a id="RF-070"></a>RF-070 | O sistema deve permitir que usuários com perfil de gestor alternem entre os modos Explorador e Gestor sem realizar novo login.                       | Should have         |
| <a id="RF-071"></a>RF-071 | O sistema deve exibir o nível de parceria do gestor na plataforma, acompanhado de identificação visual e descrição dos benefícios associados.        | Could have          |
| <a id="RF-072"></a>RF-072 | O sistema deve exibir as certificações e qualificações obtidas pelo gestor dentro da plataforma.                                                     | Won't have          |
| <a id="RF-073"></a>RF-073 | O sistema deve permitir que o usuário encerre simultaneamente todas as suas sessões ativas.                                                          | Could have          |

### Épico 13: Navegação e Interface Global (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                      | prioridade (MoSCoW) |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| <a id="RF-074"></a>RF-074 | O sistema deve disponibilizar ao Explorador uma barra de navegação inferior fixa com acesso às seções Início, Explorar, Assistente, Comunidade e Perfil.                      | Should have         |
| <a id="RF-075"></a>RF-075 | O sistema deve disponibilizar ao Gestor uma barra de navegação inferior fixa com acesso às seções Painel, Gerenciar, Indicadores, Novo Estabelecimento e Perfil.              | Should have         |
| <a id="RF-076"></a>RF-076 | O sistema deve manter um cabeçalho fixo com título, contexto e ações pertinentes à tela atualmente acessada.                                                                  | Should have         |
