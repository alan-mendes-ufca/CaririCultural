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
14. [Épico 14: Fluxos de Uso em Validação](#épico-14-fluxos-de-uso-em-validação)

---

## Critérios de Priorização MoSCoW

> "MVP" aqui não é minimalismo absoluto, é o conjunto mínimo que sustenta o fluxo completo de experiência (descoberta → avaliação → planejamento → visita) de ponta a ponta, ainda que de forma simples em cada etapa.

- **Must have**: requisito indispensável para a primeira entrega validada do produto.
- **Should have**: requisito importante, mas que pode ser entregue após o núcleo principal sem inviabilizar a solução.
- **Could have**: requisito desejável, condicionado à disponibilidade de tempo e recursos.
- **Won't have**: requisito fora do escopo da entrega atual ou pendente de validação antes de entrar no planejamento.

---

### Épico 1: Exploração e Descoberta

| id     | requisito                                                                                                                           | prioridade (MoSCoW) | justificativa |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-001"></a>RF-001 | O sistema deve disponibilizar um catálogo regional unificado de locais turísticos, culturais, gastronômicos, comerciais e de lazer. | Must have           | Base indispensável da etapa de descoberta: sem catálogo não há o que explorar. |
| <a id="RF-002"></a>RF-002 | O sistema deve exibir listas de locais e experiências com alta visitação ou popularidade.                                           | Should have         | Destaques por popularidade enriquecem a descoberta, mas a busca e o filtro (RF-004/RF-006) já sustentam o mínimo navegável. |
| <a id="RF-003"></a>RF-003 | O sistema deve exibir listas de locais e experiências pouco divulgadas ou alternativas.                                             | Should have         | Complementa a descoberta central; o catálogo básico (RF-001) já garante navegação mínima ponta a ponta. |
| <a id="RF-004"></a>RF-004 | O sistema deve permitir pesquisa de locais e eventos por palavras-chave, nome, categoria e cidade.                                  | Must have           | Mecanismo essencial para localizar algo específico dentro do catálogo; sem ele a descoberta depende só de rolagem. |
| <a id="RF-005"></a>RF-005 | O sistema deve fornecer sugestões alternativas (termos ou categorias) quando uma busca não retornar resultados.                     | Should have         | Melhora a recuperação de buscas sem resultado, mas a busca básica (RF-004) já funciona sem esse tratamento. |
| <a id="RF-006"></a>RF-006 | O sistema deve permitir a filtragem de locais e eventos por categoria e adequação ao público (ex: infantil, famílias).              | Must have           | Torna o catálogo navegável e relevante; sem filtro a descoberta em um catálogo regional amplo fica inviável na prática. |

### Épico 2: Informações e Detalhes do Local

| id     | requisito                                                                                                                                                                                                     | prioridade (MoSCoW) | justificativa |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-007"></a>RF-007 | O sistema deve exibir informações descritivas básicas do local, como resumo contextual, categoria e tipo de experiência.                                                                                      | Must have           | Mínimo necessário para o usuário entender do que se trata o local na etapa de avaliação. |
| <a id="RF-008"></a>RF-008 | O sistema deve exibir fotos, mídias e características do ambiente físico dos locais.                                                                                                                          | Must have           | Registro visual é decisivo na avaliação; usuários decidem em grande parte pela aparência do ambiente. |
| <a id="RF-009"></a>RF-009 | O sistema deve exibir horários de funcionamento, status atual (aberto/fechado) e indicar possíveis opções de atividades noturnas.                                                                             | Must have           | Evita frustração de deslocamento a local fechado; crítico tanto para avaliação quanto para planejamento. |
| <a id="RF-010"></a>RF-010 | O sistema deve disponibilizar informações financeiras, incluindo cardápio, faixa de preços, taxas e couvert artístico (quando aplicável).                                                                     | Must have           | Custo é critério primário de decisão; sem ele a etapa de avaliação fica incompleta. |
| <a id="RF-011"></a>RF-011 | O sistema deve apresentar dados de localização, trajeto, formas de acesso, opções de transporte e estabelecimentos próximos.                                                                                  | Must have           | Sustenta diretamente a transição planejamento → visita: sem isso o usuário não sabe como chegar ao local. |
| <a id="RF-012"></a>RF-012 | O sistema deve disponibilizar informações específicas sobre a segurança do local e de seu entorno.                                                                                                            | Must have           | Critério decisório essencial, especialmente relevante em contexto de turismo regional. |
| <a id="RF-013"></a>RF-013 | O sistema deve disponibilizar informações qualitativas sobre as condições de higiene do estabelecimento.                                                                                                      | Should have         | Complementa a decisão, mas é secundária frente a critérios mais determinantes já cobertos (preço, segurança, horário). |
| <a id="RF-014"></a>RF-014 | O sistema deve indicar de forma clara os recursos de acessibilidade disponíveis no local.                                                                                                                     | Must have           | Indispensável para o público que depende dessa informação para decidir se a visita é viável. |
| <a id="RF-015"></a>RF-015 | O sistema deve informar se o local conta com estrutura e adequação para receber o público infantil.                                                                                                           | Should have         | Refina a decisão para um segmento específico de público, não é universal a todos os usuários. |
| <a id="RF-016"></a>RF-016 | O sistema deve exibir calendário e detalhes, como programações musicais, datas e horários dos eventos cadastrados.                                                                                            | Must have           | Eventos têm janela temporal definida; sem essa informação a decisão de ir ou não perde sentido. |
| <a id="RF-017"></a>RF-017 | O sistema deve informar os canais de contato atualizados do estabelecimento de forma acessível.                                                                                                               | Must have           | É o mecanismo direto de divulgação/redirecionamento — a plataforma não intermedia negócios, então o contato real é o que efetivamente conecta o usuário ao estabelecimento. |
| <a id="RF-018"></a>RF-018 | O sistema deve fornecer informações e curiosidades históricas, culturais e sociais relacionadas aos locais da região.                                                                                         | Should have         | Enriquece a experiência e o valor cultural, mas não é decisório para a etapa de avaliação. |
| <a id="RF-019"></a>RF-019 | O sistema deve exibir as regras e políticas do local, incluindo itens permitidos e proibidos, restrições de entrada e condições especiais de acesso ou preço.                                                 | Should have         | Refina a decisão, mas as informações centrais já Must (preço, horário, acesso) cobrem o essencial. |
| <a id="RF-020"></a>RF-020 | O sistema deve informar o formato de serviço do estabelecimento (ex: atendimento na mesa, self-service, rodízio com garçom, rodízio com fila, balcão), para que o usuário conheça a dinâmica antes da visita. | Should have         | Informação de conveniência sobre a dinâmica local, não crítica para decidir visitar. |

### Épico 3: Avaliações e Comunidade

| id     | requisito                                                                                                                   | prioridade (MoSCoW) | justificativa |
| ------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-021"></a>RF-021 | O sistema deve exibir avaliações e comentários públicos deixados por outros visitantes sobre os locais.                     | Must have           | Validação social é parte central da etapa de avaliação; sustenta a confiança na decisão. |
| <a id="RF-022"></a>RF-022 | O sistema deve permitir que o usuário publique suas próprias avaliações e comentários a respeito dos locais e experiências. | Must have           | Sem geração de conteúdo por usuários desde o início, o ciclo de avaliação depende só de curadoria administrativa — risco de "cold start" para um produto de comunidade. |

### Épico 4: Recomendações Personalizadas

| id     | requisito                                                                                                                        | prioridade (MoSCoW) | justificativa |
| ------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-023"></a>RF-023 | O sistema deve exibir recomendações de locais com base no histórico de visitas anteriores do usuário.                            | Should have         | Refina a descoberta, mas depende de dados que só existem após uso continuado do sistema. |
| <a id="RF-024"></a>RF-024 | O sistema deve fornecer recomendações de locais alinhadas às avaliações realizadas pelo usuário.                                 | Should have         | Mesma lógica de RF-023: personalização incremental, não bloqueante ao fluxo mínimo de descoberta. |
| <a id="RF-025"></a>RF-025 | O sistema deve sugerir locais considerando os interesses de usuários com perfis compatíveis (filtragem de interesses similares). | Could have          | Recomendação social avançada, dependente de massa crítica de usuários que o MVP ainda não terá. |
| <a id="RF-026"></a>RF-026 | O sistema deve gerar e recomendar roteiros elaborados e personalizados de passeios de acordo com o interesse do usuário.         | Must have           | Núcleo da etapa de planejamento; é o que transforma locais individuais em um passeio coeso. |

### Épico 5: Organização Pessoal e Roteiros

| id     | requisito                                                                                                   | prioridade (MoSCoW) | justificativa |
| ------ | ----------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-027"></a>RF-027 | O sistema deve permitir criar, organizar e gerenciar listas de locais que o usuário tem desejo de visitar.  | Must have           | Sustenta o planejamento ao permitir organizar o que já foi avaliado e decidido visitar. |
| <a id="RF-028"></a>RF-028 | O sistema deve permitir que o usuário sinalize e registre os locais físicos que já visitou no passado.      | Should have         | Registro histórico complementar, útil mas não indispensável para planejar a próxima visita. |
| <a id="RF-029"></a>RF-029 | O sistema deve disponibilizar checklists de apoio para acompanhamento das atividades e passeios do usuário. | Must have           | Sustenta diretamente a etapa de visita, acompanhando a execução do passeio planejado. |

### Épico 6: Assistente Virtual (Chatbot)

| id     | requisito                                                                                                                                                    | prioridade (MoSCoW) | justificativa |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------- |
| <a id="RF-030"></a>RF-030 | O sistema deve disponibilizar um assistente virtual conversacional para responder dúvidas de lugares e eventos.                                              | Must have           | Fio condutor transversal do produto, capaz de guiar o usuário por todas as etapas do fluxo. |
| <a id="RF-031"></a>RF-031 | O sistema deve ser capaz de interpretar a intenção de busca do usuário no assistente virtual para retornar as informações ou recomendações mais pertinentes. | Must have           | É o que torna o assistente funcionalmente útil, não apenas uma interface de conversa decorativa. |
| <a id="RF-032"></a>RF-032 | O sistema deve orientar alternativas ou repasses no próprio assistente quando este não possuir a informação exata.                                           | Should have         | Refina a robustez do assistente em casos de falha, mas a função central (RF-030/RF-031) já opera sem isso. |
| <a id="RF-033"></a>RF-033 | O sistema deve permitir acionar o assistente de forma contextualizada, permitindo a continuidade direta de uma pesquisa em andamento.                        | Should have         | É um refinamento de integração de UX entre telas, não um passo do fluxo em si — o assistente já é Must have via RF-030/RF-031. |
| <a id="RF-034"></a>RF-034 | O sistema deve disponibilizar um módulo para importar e atualizar as informações de locais e eventos a partir de fontes de dados externas.                   | Must have           | Via complementar (não substituta) ao cadastro administrativo (RF-042/RF-051) para povoar o catálogo (RF-001) e a agenda (RF-016). |
| <a id="RF-035"></a>RF-035 | O sistema deve ser capaz de disponibilizar links externos para perfis públicos do ponto turístico (caso aplicável).                                          | Must have           | A plataforma não centraliza negócios nem vende reservas — divulgar e redirecionar externamente é o próprio mecanismo de valor, não um extra. |
| <a id="RF-036"></a>RF-036 | O sistema deve exibir imagens disponíveis acerca do local de visita/passeio.                                                                                 | Should have         | Reforça a etapa de avaliação, mas RF-008 já cobre o mínimo necessário de mídia visual. |
| <a id="RF-037"></a>RF-037 | O sistema deve ser capaz de interpretar prompts de áudio e devolver resultados em texto.                                                                     | Could have          | Conveniência adicional de interação com o assistente, não essencial ao seu funcionamento básico. |

### Épico 7: Interações Sociais e Compartilhamento

| id     | requisito                                                                                                                                                        | prioridade (MoSCoW) | justificativa |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-038"></a>RF-038 | O sistema deve permitir que usuários criem enquetes compartilháveis (via link) de locais ou eventos, permitindo votação anônima sem necessidade de autenticação. | Could have          | Recurso social adicional, fora do núcleo descoberta → avaliação → planejamento → visita. |
| <a id="RF-039"></a>RF-039 | O sistema deve listar contatos e opções de serviços de transporte alternativo e parceiros locais (ex: mototáxis, vans) atrelados a estabelecimentos ou eventos.  | Could have          | A plataforma não centraliza transporte como um serviço próprio (não é um modelo tipo Uber) — é apenas uma conveniência opcional de redirecionamento de contato. |
| <a id="RF-040"></a>RF-040 | O sistema deve possuir uma seção para exibição de mídias (fotos e vídeos curtos) geradas exclusivamente pela comunidade de usuários sobre os locais.             | Could have          | Enriquecimento de conteúdo gerado por usuários, não essencial ao fluxo mínimo. |
| <a id="RF-041"></a>RF-041 | O sistema deve permitir que o usuário gere um link público ou compartilhe externamente suas listas personalizadas de locais favoritos.                           | Should have         | Conveniência social de compartilhamento, não necessária para o próprio usuário completar seu fluxo. |

### Épico 8: Equipamentos Culturais e Estabelecimentos

> [!WARNING]
> O núcleo de cadastro administrativo (RF-042, RF-044, RF-046 a RF-048, RF-050 e RF-051) é considerado estruturalmente necessário por decisão de produto: sem ele, o catálogo e a agenda de eventos dependem inteiramente do RF-034 como única fonte de dado. A forma final de implementação (fluxos, telas e regras administrativas) ainda depende de validação com stakeholders administrativos, que ainda não foram identificados. Os requisitos remanescentes (RF-049 e RF-052 a RF-058) permanecem fora do escopo da entrega atual.

| id     | requisito                                                                                                                            | prioridade (MoSCoW) | justificativa |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------- |
| <a id="RF-042"></a>RF-042 | O sistema deve permitir o cadastro de equipamentos culturais.                                                                        | Must have           | Sem cadastro próprio, o catálogo (RF-001) depende inteiramente do RF-034 como única fonte de dado — via primária de povoamento junto com a importação externa. |
| <a id="RF-043"></a>RF-043 | O sistema deve permitir a edição de informações de equipamentos culturais cadastrados.                                               | Should have         | Sem edição, erro de cadastro só se corrige apagando e recriando; importante para qualidade de dado, mas o cadastro inicial (RF-042) já viabiliza o catálogo. |
| <a id="RF-044"></a>RF-044 | O sistema deve permitir a consulta de informações de equipamentos culturais.                                                         | Must have           | Contrapartida mínima de leitura do cadastro (RF-042) — sem ela não há como o administrador verificar o que foi salvo. |
| <a id="RF-045"></a>RF-045 | O sistema deve permitir a associação de administradores a equipamentos culturais.                                                    | Should have         | Governança multi-admin; um perfil administrativo único pode operar no início sem essa granularidade. |
| <a id="RF-046"></a>RF-046 | O sistema deve permitir a autenticação de administradores.                                                                           | Must have           | Pré-requisito de segurança para qualquer cadastro administrativo (RF-042/RF-051) acontecer com responsabilização. |
| <a id="RF-047"></a>RF-047 | O sistema deve permitir que administradores de equipamentos culturais cadastrem atrações.                                            | Must have           | Sem cadastro próprio de atrações, o calendário de eventos (RF-016, Must have) depende inteiramente do RF-034 como única fonte de dado — mesmo risco de ponto único de falha que motivou elevar RF-042/RF-051. |
| <a id="RF-048"></a>RF-048 | O sistema deve permitir que administradores editem atrações cadastradas.                                                             | Should have         | Sem edição, erro de cadastro de atração só se corrige apagando e recriando; mesma lógica do RF-043. |
| <a id="RF-049"></a>RF-049 | O sistema deve permitir que administradores removam atrações cadastradas.                                                            | Won't have          | RF-081 já cobre a retirada/inativação de atrações encerradas; remoção definitiva é refinamento de menor urgência, ainda sem stakeholder validado. |
| <a id="RF-050"></a>RF-050 | O sistema deve permitir a consulta de atrações cadastradas.                                                                          | Must have           | Contrapartida mínima de leitura do cadastro de atrações (RF-047) — mesma lógica do RF-044. |
| <a id="RF-051"></a>RF-051 | O sistema deve permitir o cadastro de estabelecimentos gastronômicos.                                                                | Must have           | Mesma lógica do RF-042, entidade paralela — via primária de povoamento do catálogo junto com a importação externa. |
| <a id="RF-052"></a>RF-052 | O sistema deve permitir que administradores de estabelecimentos gastronômicos cadastrem ofertas.                                     | Won't have          | Funcionalidade promocional secundária, não estrutural; ainda sem stakeholder validado. |
| <a id="RF-053"></a>RF-053 | O sistema deve permitir que administradores editem ofertas cadastradas.                                                              | Won't have          | Mesma dependência de um painel administrativo ainda não validado. |
| <a id="RF-054"></a>RF-054 | O sistema deve permitir que administradores removam ofertas cadastradas.                                                             | Won't have          | Mesma dependência de um painel administrativo ainda não validado. |
| <a id="RF-055"></a>RF-055 | O sistema deve permitir o cadastro de publicações.                                                                                   | Won't have          | Escopo administrativo sem stakeholder validado para geração de conteúdo institucional. |
| <a id="RF-056"></a>RF-056 | O sistema deve permitir que administradores criem publicações associadas a equipamentos culturais ou estabelecimentos gastronômicos. | Won't have          | Depende do módulo administrativo hipotético, sem validação de necessidade. |
| <a id="RF-057"></a>RF-057 | O sistema deve permitir a edição de publicações cadastradas.                                                                         | Won't have          | Mesma dependência de um painel administrativo ainda não validado. |
| <a id="RF-058"></a>RF-058 | O sistema deve permitir a remoção de publicações cadastradas.                                                                        | Won't have          | Mesma dependência de um painel administrativo ainda não validado. |

### Épico 9: Avaliações e Comunidade (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                                    | prioridade (MoSCoW) | justificativa |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-059"></a>RF-059 | O sistema deve permitir que usuários marquem avaliações de outros usuários como úteis e deve exibir publicamente a quantidade de marcações recebidas por cada avaliação. | Should have         | Refina a curadoria social das avaliações, mas não é essencial ao ciclo básico já coberto por RF-021/RF-022. |
| <a id="RF-060"></a>RF-060 | O sistema deve permitir o compartilhamento externo de uma avaliação pública individual por meio de link ou aplicativo compatível.                                        | Could have          | Conveniência social adicional sobre um recurso que já funciona sem ela (RF-021). |
| <a id="RF-061"></a>RF-061 | O sistema deve permitir que usuários iniciem tópicos de discussão associados a locais ou eventos na seção de comunidade.                                                 | Should have         | Amplia a comunidade além das avaliações, mas o Épico 3 já cobre a interação social mínima. |

### Épico 10: Organização Pessoal e Gamificação (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                     | prioridade (MoSCoW) | justificativa |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-062"></a>RF-062 | O sistema deve exibir conquistas e distintivos desbloqueáveis de acordo com o engajamento do usuário, como visitas registradas, avaliações publicadas e check-ins realizados. | Could have          | Incentivo de engajamento, não necessário ao funcionamento do fluxo descoberta → visita. |
| <a id="RF-063"></a>RF-063 | O sistema deve exibir dicas contextuais curadas sobre o local associado ao checklist de visita do usuário.                                                                    | Could have          | Valor agregado à etapa de visita, mas RF-029 já cobre o acompanhamento essencial via checklist. |

### Épico 11: Gestão de Estabelecimentos (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                                                                               | prioridade (MoSCoW) | justificativa |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-064"></a>RF-064 | O sistema deve exibir ao gestor um painel com métricas resumidas dos estabelecimentos gerenciados, incluindo visitantes, avaliações recentes e eventos ativos.                                                                          | Should have         | Apoia a gestão do estabelecimento, mas depende de validação com stakeholders gestores ainda pendente. |
| <a id="RF-065"></a>RF-065 | O sistema deve exibir ao gestor um feed cronológico das atividades recentes relacionadas aos estabelecimentos gerenciados, como novas avaliações, visualizações e interações.                                                           | Could have          | Refinamento informativo sobre o painel de gestão (RF-064), não essencial à gestão básica. |
| <a id="RF-066"></a>RF-066 | O sistema deve permitir que administradores de estabelecimentos respondam publicamente às avaliações realizadas por usuários.                                                                                                            | Should have         | Fortalece o relacionamento gestor-usuário, mas não é essencial à operação mínima do fluxo do visitante. |
| <a id="RF-067"></a>RF-067 | O sistema deve permitir que o gestor visualize a página pública do estabelecimento como ela é apresentada aos usuários.                                                                                                                 | Could have          | Conveniência de conferência, não funcional ao core de gestão ou ao fluxo do visitante. |
| <a id="RF-068"></a>RF-068 | O sistema deve disponibilizar ao gestor um painel de indicadores e análises sobre o desempenho do estabelecimento, incluindo fluxo de visitantes, perfil do público, horários de pico e visibilidade regional.                         | Should have         | Apoia decisões de gestão, mas é analítico, não operacional, e depende de validação com gestores. |
| <a id="RF-069"></a>RF-069 | O sistema deve apresentar ao gestor um mapa com a distribuição geográfica agregada da origem dos visitantes do estabelecimento.                                                                                                         | Could have          | Recurso analítico avançado, dependente de volume de dados que o MVP ainda não terá. |

### Épico 12: Perfil, Autenticação e Parceria (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                            | prioridade (MoSCoW) | justificativa |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| <a id="RF-070"></a>RF-070 | O sistema deve permitir que usuários com perfil de gestor alternem entre os modos Explorador e Gestor sem realizar novo login.                       | Should have         | Melhora a experiência de usuários com perfil duplo, mas cada perfil pode ser acessado separadamente sem essa conveniência. |
| <a id="RF-071"></a>RF-071 | O sistema deve exibir o nível de parceria do gestor na plataforma, acompanhado de identificação visual e descrição dos benefícios associados.        | Could have          | Reconhecimento visual de parceria, não funcional ao fluxo do visitante ou à operação do gestor. |
| <a id="RF-072"></a>RF-072 | O sistema deve exibir as certificações e qualificações obtidas pelo gestor dentro da plataforma.                                                     | Won't have          | Recurso de reconhecimento sem stakeholder validado, fora do escopo atual. |
| <a id="RF-073"></a>RF-073 | O sistema deve permitir que o usuário encerre simultaneamente todas as suas sessões ativas.                                                          | Could have          | Refinamento de segurança e conveniência, não crítico ao fluxo funcional do MVP. |

### Épico 13: Navegação e Interface Global (Protótipo)

> [!WARNING]
> Os requisitos deste épico foram derivados do protótipo de alta fidelidade e ainda devem ser validados com stakeholders antes da aprovação definitiva do escopo.

| id     | requisito                                                                                                                                                                      | prioridade (MoSCoW) | justificativa |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------- |
| <a id="RF-074"></a>RF-074 | O sistema deve disponibilizar ao Explorador uma barra de navegação inferior fixa com acesso às seções Início, Explorar, Assistente, Comunidade e Perfil.                      | Should have         | Estrutura a experiência do Explorador, mas o acesso às seções pode existir de forma mais simples na primeira entrega. |
| <a id="RF-075"></a>RF-075 | O sistema deve disponibilizar ao Gestor uma barra de navegação inferior fixa com acesso às seções Painel, Gerenciar, Indicadores, Novo Estabelecimento e Perfil.              | Should have         | Mesma lógica de RF-074, aplicada ao perfil Gestor; refinamento de navegação, não bloqueante. |
| <a id="RF-076"></a>RF-076 | O sistema deve manter um cabeçalho fixo com título, contexto e ações pertinentes à tela atualmente acessada.                                                                  | Should have         | Consistência de interface que melhora a usabilidade, mas não é indispensável ao funcionamento do fluxo. |

### Épico 14: Fluxos de Uso em Validação

> [!WARNING]
> Os requisitos deste épico foram derivados dos casos de uso e permanecem hipóteses até a validação com stakeholders.

| id | requisito | prioridade (MoSCoW) | justificativa |
| --- | --- | --- | --- |
| <a id="RF-077"></a>RF-077 | O sistema deve validar formato, tamanho, cardinalidade, domínio e taxonomia dos parâmetros de busca antes de processar a consulta, rejeitando valores inválidos com mensagem compreensível. | Must have | Protege a integridade da etapa de descoberta, cuja busca (RF-004) já é Must have. |
| <a id="RF-078"></a>RF-078 | O sistema deve permitir busca por proximidade mediante consentimento para localização atual ou origem manual informada pelo visitante. | Should have | Refinamento de busca; a descoberta básica por palavra-chave e filtro (RF-004/RF-006) já funciona sem geolocalização. |
| <a id="RF-079"></a>RF-079 | O sistema deve apresentar, para dados sensíveis à atualização, a fonte, a data da última verificação e o eventual estado de revisão. | Must have | Sustenta a confiabilidade da etapa de avaliação, especialmente com dados vindos de importação externa (RF-034). |
| <a id="RF-080"></a>RF-080 | O sistema deve permitir filtrar a agenda pública por data. | Must have | Essencial para eventos com janela temporal definida, complementando o calendário já Must (RF-016). |
| <a id="RF-081"></a>RF-081 | O sistema deve retirar da agenda pública eventos e atrações encerrados, mantendo-os inativos ou arquivados. | Must have | Evita decisões erradas de planejamento baseadas em eventos que não existem mais. |
| <a id="RF-082"></a>RF-082 | O sistema deve preservar temporariamente o conteúdo preenchido em avaliação ou sinalização quando exigir autenticação e restaurá-lo após o retorno do usuário. | Should have | Evita frustração no fluxo de avaliação, mas não é bloqueante — o usuário pode reinserir o conteúdo manualmente. |
| <a id="RF-083"></a>RF-083 | O sistema deve solicitar interesses ou exibir opções gerais elegíveis quando não houver dados suficientes para recomendações personalizadas. | Should have | Trata um caso de borda das recomendações (Épico 4), que já são majoritariamente Should have. |
| <a id="RF-084"></a>RF-084 | O sistema deve permitir salvar roteiros pessoais, recalcular trechos após substituições e explicar inviabilidades de combinação. | Must have | Essencial à funcionalidade central de planejamento, complementando os roteiros e listas já Must (RF-026/RF-027). |
| <a id="RF-085"></a>RF-085 | O sistema deve alertar o usuário quando um item de checklist estiver vinculado a atração inativa. | Should have | Refinamento de robustez sobre o checklist de visita (RF-029), que já funciona sem esse alerta. |
| <a id="RF-086"></a>RF-086 | O sistema deve controlar o ciclo de vida de enquetes, incluindo alteração, encerramento, votação múltipla e tratamento de duplicidade. | Could have | Gestão avançada de um recurso que já é Could have na origem (RF-038). |
| <a id="RF-087"></a>RF-087 | O sistema deve permitir ao proprietário revogar links públicos de listas pessoais. | Should have | Controle de privacidade complementar ao compartilhamento de listas (RF-041), também Should have. |
| <a id="RF-088"></a>RF-088 | O sistema deve exibir e permitir o acionamento do contato de transporte parceiro elegível para um local ou evento. | Could have | Ação de redirecionamento de contato sobre a listagem de transporte parceiro (RF-039); reescrito para não sugerir uma reserva/confirmação intermediada pela plataforma. |
| <a id="RF-089"></a>RF-089 | O sistema deve registrar, acompanhar e tratar sinalizações de dados incorretos em locais e eventos. | Must have | Sustenta a confiabilidade do catálogo ao longo de todo o fluxo, especialmente com dados de fontes externas (RF-034). |
