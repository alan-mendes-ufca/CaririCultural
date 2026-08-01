---
title: Service Blueprint - Cariri Cultural
---

# Service Blueprint - Cariri Cultural

## Objetivo e recorte

O Blueprint representa a prestação do serviço Cariri Cultural para turistas, novos moradores e moradores da região. O cenário principal começa quando a pessoa procura algo para fazer e termina quando registra a experiência, contribui com a comunidade ou inicia uma nova descoberta. Um fluxo complementar mostra como o Gestor mantém as informações e interações que sustentam essa experiência.

O serviço deve transformar informações turísticas e culturais dispersas em uma escolha confiável, um plano viável e uma experiência coerente com o que foi apresentado na plataforma.

## Blueprint da jornada principal

| Raia / etapa | 1. Descobrir | 2. Acessar e explorar | 3. Buscar e filtrar | 4. Avaliar e escolher | 5. Planejar | 6. Visitar e usar | 7. Contribuir e retornar |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Evidências e pontos de contato** | Redes sociais, indicação, cartaz, campanha ou QR code | Home, cabeçalho e navegação Início, Explorar, Assistente, Favoritos, Comunidade e Perfil | Explorar, Pesquisa Inteligente, sugestões, buscas recentes, filtros, cartões, estados vazios e mapa | Detalhes do local, história, fotos, localização, orientações pré-visita, avaliações e Planejar visita | Planejamento de visita, checklist, status do preparo, listas, mapa e transporte | Página do local, serviço de mapas, Assistente Cultural, entrada por texto ou áudio e sinalização de dado incorreto | Avaliações, Comunidade, mídias, enquetes, discussões, conquistas, perfil, histórico e alternância de modo |
| **Ações do usuário** | Define ocasião, companhia, tempo e orçamento | Abre a plataforma e explora categorias, mais visitados, pouco explorados e eventos | Pesquisa, retoma busca recente, aplica filtros e seleciona um resultado | Confere informações, avaliações e orientações e escolhe o local | Aciona Planejar visita, organiza itens e acompanha o checklist | Reconfere horário e rota, consulta o assistente e adapta o plano | Registra a visita, avalia, compartilha, participa da comunidade, acompanha correções e, quando Gestor, alterna o modo de perfil |
| **Linha de interação** |  |  |  |  |  |  |  |
| **Frontstage: ações visíveis** | Exibe locais populares, pouco explorados, eventos e conteúdo patrocinado identificado | Permite consulta pública e apresenta categorias, destaques e navegação persistente | Mostra sugestões, buscas recentes, filtros e resultados; oferece estado vazio e alternativas | Apresenta descrição, história, fotos, localização, condições da visita, avaliações e acesso ao planejamento | Exibe checklist e progresso representados no protótipo; roteiro, recálculo e transporte seguem os requisitos aplicáveis | Responde pelo assistente, oferece ações rápidas, texto ou áudio, informa limitações e permite sinalizar informação incorreta | Exibe comunidade, enquetes, avaliações, perfil, visitas e conquistas; confirma envio, moderação e resultado de correções quando aplicável |
| **Linha de visibilidade** |  |  |  |  |  |  |  |
| **Backstage: ações invisíveis** | Equipe seleciona destaques e diferencia curadoria de promoção paga | Sistema verifica sessão, perfil, consentimento, dispositivo e permissões | Sistema valida taxonomia, executa busca, ordena, pagina e calcula proximidade autorizada | Gestores mantêm descrição, história, fotos, horários e eventos; curadoria verifica cadastro, fontes e links | Sistema persiste checklist, cruza interesses, horários, distância e público e preserva ajustes manuais | Assistente interpreta contexto, consulta a base e aciona fallback; curadoria recebe sinalizações | Sistema valida autoria; equipe modera conteúdo; gestor responde avaliações e acompanha métricas; curador encerra protocolos |
| **Linha de interação interna** |  |  |  |  |  |  |  |
| **Processos de apoio** | Curadoria editorial, divulgação regional e parcerias institucionais | Identidade, LGPD, segurança, acessibilidade, hospedagem e monitoramento | Banco de dados, índices de busca, geolocalização, cache, paginação e CDN | Cadastro do Gestor, governança do catálogo, fontes, armazenamento de mídia e integração com mapas | Motor de recomendação, roteirização, listas, checklists e persistência de preferências | Base de conhecimento, IA, transcrição de áudio, mapas, cache e observabilidade | Moderação, respostas do Gestor, notificações, auditoria, analytics, backups e recuperação |
| **Responsáveis principais** | Equipe de conteúdo e comunicação | Equipe de produto, identidade e infraestrutura | Equipe técnica e responsável pelo catálogo | Curador, gestor do local e fontes institucionais | Sistema de recomendação e serviços de mapas | Equipe técnica, IA, mapas e curadoria | Usuário, moderação, gestor do local e curador |
| **Regras e controles essenciais** | Conteúdo patrocinado deve ser identificado | Consulta pública não exige autenticação; dados pessoais exigem consentimento | Localização só pode ser usada com autorização e deve haver alternativa manual | Dados sensíveis precisam de fonte e verificação; registros incompletos não devem ser publicados | Recomendações usam somente dados autorizados e locais elegíveis | Áudio deve ter tratamento transitório; falhas externas não podem bloquear os dados locais | Contribuições exigem autoria quando aplicável; votação em enquete pode ser anônima; conteúdo denunciado passa por revisão |
| **Pontos críticos** | Repetição dos mesmos locais ou influência indevida de publicidade | Login precoce, lentidão ou navegação confusa | Resultado irrelevante, filtro insuficiente ou busca sem saída | Informação antiga, incompleta ou diferente da realidade | Roteiro inviável por horário, distância, transporte ou custo | Local fechado, falta de sinal, rota indisponível ou IA sem resposta | Envio interrompido, moderação opaca, exposição de dados ou ausência de retorno |
| **Critério de qualidade** | Diversidade e transparência dos destaques | Catálogo carregado em até 2 segundos em conexão 4G | Pesquisa respondida em até 1,5 segundo e com alternativa acionável | Detalhes carregados em até 3 segundos e dados verificáveis | Plano compatível com restrições e ajustável pelo usuário | Primeira resposta do assistente em até 5 segundos e fallback disponível | Confirmação clara, privacidade, rastreabilidade e retorno da moderação ou correção |

## Fluxo complementar do Gestor

O Gestor é um usuário da plataforma e também participa da prestação do serviço: cadastra e mantém os locais que aparecem para o Explorador. Este fluxo complementa a jornada principal sem substituir a curadoria e os controles administrativos.

| Raia / etapa | 1. Acessar o modo Gestor | 2. Cadastrar estabelecimento | 3. Manter local e interações | 4. Acompanhar desempenho |
| --- | --- | --- | --- | --- |
| **Evidências e pontos de contato** | Perfil, alternância Explorador/Gestor, Painel do Gestor e Meus Estabelecimentos | Novo Estabelecimento: identificação e localização; horários, contato e acessibilidade; fotos e redes sociais | Gerenciar Local, Ver Público, Salvar Alterações, avaliações pendentes, horários e eventos | Painel do Gestor, atividades e Insights do Estabelecimento |
| **Ações do Gestor** | Alterna o modo, acessa os locais vinculados e inicia um novo cadastro | Informa nome, categoria, descrição, localização, horários, contatos, acessibilidade, fotos e redes sociais; aceita os termos e conclui | Edita descrição e história, adiciona fotos, atualiza horários e eventos, visualiza a página pública e responde avaliações | Consulta fluxo de visitantes, público, visibilidade, horários de pico e alcance regional |
| **Frontstage: ações visíveis** | Exibe estabelecimentos e atividades e oferece Novo Estabelecimento e Gerenciar Local | Apresenta cadastro em três etapas, avanço, retorno, cancelamento e conclusão | Confirma salvamento, mostra visão pública e oferece controles de conteúdo e resposta | Apresenta indicadores e acesso ao mapa de alcance regional |
| **Backstage: ações invisíveis** | Valida autenticação, papel e vínculo administrativo | Valida campos, categoria, localização, contatos, acessibilidade, mídias e vínculo do responsável | Aplica autorização por local, registra alterações, atualiza status e encaminha conteúdo sujeito à moderação | Agrega dados, aplica controles de privacidade e atualiza métricas autorizadas |
| **Processos de apoio** | Identidade, RBAC e gestão de vínculos | Catálogo, geolocalização, armazenamento de mídia, termos e curadoria | Auditoria, moderação, agenda, notificações e CDN | Analytics, anonimização, auditoria e observabilidade |
| **Rastreabilidade principal** | `RF-046`, `RF-064` a `RF-073`, `RF-075`; `RN-023`, `RN-066` e `RN-067` | `RF-042`, `RF-045`, `RF-047` e `RF-051`; `RN-011` a `RN-013`, `RN-023`, `RN-066` a `RN-068` e `RN-076` | `RF-043`, `RF-047` a `RF-058`, `RF-066` e `RF-067`; `RN-038` e `RN-066` a `RN-076` | `RF-064` a `RF-069`; `RN-066` e `RN-068` |

## Evidências e limites do protótipo atualizado

| Evidência observada | Interpretação no Blueprint |
| --- | --- |
| Home, Explorar, Pesquisa Inteligente, Detalhes, Planejamento/checklist, Assistente, Comunidade, avaliações e perfil | Evidenciam os principais pontos de contato do Explorador. |
| Painel e perfil do Gestor, cadastro em três etapas, Gerenciar Local e Insights | Evidenciam o fluxo complementar de manutenção do catálogo e acompanhamento do serviço. |
| Favoritos na navegação e filtros de preço e acessibilidade | São hipóteses visuais do protótipo. Favoritos não possui rota própria e os filtros precisam ser confirmados nos requisitos antes de serem considerados fluxo aprovado. |
| Proximidade, roteiro personalizado, transporte parceiro, protocolo de correção, moderação completa e fallbacks | Estão documentados em requisitos ou casos de uso, mas não são demonstrados de ponta a ponta pelas telas estáticas. |

As telas são evidência de representação da interface, não de implementação funcional.

## Rastreabilidade com requisitos e regras

A tabela relaciona cada etapa do Blueprint aos principais requisitos funcionais e regras de negócio que sustentam o serviço. Um mesmo requisito pode participar de mais de uma etapa. A associação indica cobertura documental, não comprova implementação.

| Etapa do Blueprint | Requisitos funcionais relacionados | Regras de negócio relacionadas | Situação |
| --- | --- | --- | --- |
| **1. Descobrir** | `RF-001` a `RF-003`, `RF-016`, `RF-080` e `RF-081` | `RN-001`, `RN-002`, `RN-006` a `RN-010`, `RN-022`, `RN-077` e `RN-084` | Linha de base; `RN-077`, `RF-080`, `RF-081` e `RN-084` permanecem em validação. |
| **2. Acessar e explorar** | `RF-001`, `RF-027`, `RF-044`, `RF-050`, `RF-074` e `RF-076` | `RN-001`, `RN-022`, `RN-045`, `RN-046` e `RN-072` | Consulta pública documentada; Favoritos é hipótese visual relacionada a listas pessoais; os fluxos administrativos e de navegação ainda dependem de validação. |
| **3. Buscar e filtrar** | `RF-004` a `RF-006`, `RF-030` a `RF-033`, `RF-077`, `RF-078` e `RF-083` | `RN-003` a `RN-005`, `RN-009`, `RN-010`, `RN-054` a `RN-057`, `RN-078` a `RN-080` e `RN-086` | Busca básica na linha de base; proximidade, validação semântica e fallback personalizado permanecem em validação. |
| **4. Avaliar e escolher** | `RF-007` a `RF-021`, `RF-035`, `RF-036`, `RF-079` a `RF-081` | `RN-011` a `RN-032`, `RN-058` e `RN-081` a `RN-084` | Informações centrais na linha de base; procedência e ciclo de vida da agenda permanecem em validação. |
| **5. Planejar** | `RF-023` a `RF-029`, `RF-039`, `RF-063`, `RF-084`, `RF-085` e `RF-088` | `RN-039` a `RN-053`, `RN-086` a `RN-088` e `RN-091` | Roteiros, listas e checklist documentados; dicas do protótipo, persistência, recálculo, alertas e transporte parceiro permanecem em validação. |
| **6. Visitar e usar** | `RF-009`, `RF-011`, `RF-016`, `RF-018` a `RF-020`, `RF-030` a `RF-033`, `RF-037`, `RF-063`, `RF-079`, `RF-088` e `RF-089` | `RN-021`, `RN-025` a `RN-028`, `RN-054` a `RN-060`, `RN-081` a `RN-083` e `RN-091` a `RN-093` | Assistente e consulta contextual documentados; dicas do protótipo, procedência, transporte e sinalização permanecem em validação. |
| **7. Contribuir e retornar** | `RF-022`, `RF-028`, `RF-038`, `RF-040`, `RF-041`, `RF-059` a `RF-062`, `RF-066`, `RF-070`, `RF-082`, `RF-086`, `RF-087` e `RF-089` | `RN-023`, `RN-029` a `RN-038`, `RN-045` a `RN-049`, `RN-061` a `RN-067`, `RN-085`, `RN-089`, `RN-090`, `RN-092` e `RN-093` | Avaliação e histórico documentados; comunidade, conquistas e alternância de modo são representados no protótipo; os demais fluxos indicados permanecem em validação. |
| **Suporte transversal: backstage e processos de apoio** | `RF-034`, `RF-042` a `RF-058`, `RF-064` a `RF-073` e `RF-075` | `RN-058` e `RN-066` a `RN-076` | Sustenta importação, cadastro, curadoria, gestão, moderação e auditoria; os fluxos administrativos dependem de validação com stakeholders e parte deles está fora da entrega atual segundo a priorização MoSCoW. |

Para rastreabilidade detalhada entre histórias de usuário, requisitos, regras, RNFs e casos de uso, deve-se consultar a **Matriz de Rastreabilidade** do projeto.
