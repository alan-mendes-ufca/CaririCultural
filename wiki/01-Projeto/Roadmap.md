# Roadmap

Plano de desenvolvimento do aplicativo Android, organizado em milestones no estilo do projeto [clone-tabnews](https://github.com/filipedeschamps/clone-tabnews). O andamento atualizado fica nas [milestones](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestones) e nas [issues](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues) do repositório; esta página é o índice do plano.

Cada issue cita os requisitos, regras de negócio, casos de uso e histórias que a originam. Prioridades seguem a classificação MoSCoW (`must-have`, `should-have`) dos [requisitos priorizados](Requisitos-Funcionais-Priorizados).

## [Milestone 0: Em construção](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/1)

Documentação organizada na Wiki, repositório preparado e primeira versão instalável do aplicativo Android (tela "Em construção") distribuída para a equipe.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#1 Organização da Wiki](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/1) | must-have | documentation |
| [#2 Tipo da Licença](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/2) | — | documentation |
| [#3 README do Projeto](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/3) | — | documentation |
| [#4 Projeto Android Inicial](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/4) | must-have | app, infra |
| [#5 Distribuição Interna](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/5) | — | infra |

## [Milestone 1: Fundação](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/2)

Arquitetura do app e do backend, modelo de dados, design system, navegação base e esteira de qualidade (linters, testes automatizados e integração contínua).

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#6 Proposta de Arquitetura e Pastas](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/6) | must-have | app, infra |
| [#7 Revisão do RNF-POR-004 (Estratégia de Deploy)](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/7) | must-have | documentation |
| [#8 Backend e Contrato da API](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/8) | must-have | backend |
| [#9 Modelo de Dados e Taxonomia do Catálogo](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/9) | must-have | backend, app |
| [#10 Design System](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/10) | must-have | app, ux |
| [#11 Navegação Base](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/11) | should-have | app, ux |
| [#12 Camada de Rede](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/12) | must-have | app |
| [#13 Banco de Dados Local e Cache Offline](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/13) | must-have | app |
| [#14 Testes Automatizados](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/14) | must-have | infra |
| [#15 Linter de Código](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/15) | — | infra |
| [#16 Linter de Commits](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/16) | — | infra |
| [#17 Continuous Integration](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/17) | must-have | infra |

## [Milestone 2: Catálogo e Descoberta](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/3)

Épicos 1 e 2: catálogo regional, busca, filtros, perfil do local, horários, localização, agenda de eventos e procedência dos dados.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#18 Catálogo Regional](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/18) | must-have | app, backend |
| [#19 Tela Início e Destaques](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/19) | should-have | app |
| [#20 Busca de Locais e Eventos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/20) | must-have | app, backend |
| [#21 Filtros por Categoria, Cidade e Público](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/21) | must-have | app, backend |
| [#22 Perfil do Local](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/22) | must-have | app |
| [#23 Horários e Status Aberto/Fechado](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/23) | must-have | app, backend |
| [#24 Localização, Mapa e Como Chegar](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/24) | must-have | app |
| [#25 Agenda de Eventos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/25) | must-have | app, backend |
| [#26 Procedência e Atualização dos Dados](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/26) | must-have | app, backend |
| [#27 Importação de Dados Externos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/27) | must-have | backend |
| [#28 Compartilhar Local ou Evento](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/28) | should-have | app |

## [Milestone 3: Usuários, Autenticação e Privacidade](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/4)

Cadastro, login, sessões, papéis (RBAC), perfil do usuário e conformidade com a LGPD.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#29 Cadastro de Usuários](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/29) | must-have | app, backend |
| [#30 Login e Sessão](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/30) | must-have | app, backend |
| [#31 Autorização por Papéis](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/31) | must-have | backend |
| [#32 Perfil do Usuário](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/32) | should-have | app |
| [#33 Privacidade e LGPD](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/33) | must-have | app, backend |
| [#34 Retomar Rascunho após Autenticação](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/34) | should-have | app |

## [Milestone 4: Avaliações e Comunidade](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/5)

Épico 3: consulta e publicação de avaliações, relevância, marcação de utilidade e sinalização de dados incorretos.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#35 Consultar Avaliações](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/35) | must-have | app, backend |
| [#36 Publicar Avaliação](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/36) | must-have | app, backend |
| [#37 Sinalizar Dado Incorreto](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/37) | must-have | app, backend |
| [#38 Marcar Avaliação como Útil](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/38) | should-have | app, backend |

## [Milestone 5: Planejamento Pessoal](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/6)

Épicos 4 e 5: listas de locais desejados, roteiros personalizados, checklists de passeio, locais visitados e recomendações.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#39 Listas de Locais Desejados](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/39) | must-have | app, backend |
| [#40 Roteiros Personalizados](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/40) | must-have | app, backend |
| [#41 Checklists de Passeio](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/41) | must-have | app |
| [#42 Locais Visitados](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/42) | should-have | app, backend |
| [#43 Recomendações Personalizadas](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/43) | should-have | app, backend |

## [Milestone 6: Assistente Virtual](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/7)

Épico 6: assistente conversacional com interpretação de intenção, contexto da tela, dados do catálogo e fallback gracioso.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#44 Interface de Chat do Assistente](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/44) | must-have | app, ia |
| [#45 Serviço de IA e Interpretação de Intenção](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/45) | must-have | backend, ia |
| [#46 Assistente com Contexto da Tela](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/46) | must-have | app, ia |
| [#47 Fallback do Assistente](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/47) | must-have | app, backend, ia |

## [Milestone 7: Gestão de Estabelecimentos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/8)

Épicos 8 e 11: autenticação de administradores, cadastro de equipamentos culturais, atrações e estabelecimentos, e modo Gestor.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#48 Autenticação de Administradores](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/48) | must-have | app, backend |
| [#49 Cadastro de Equipamentos Culturais](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/49) | must-have | app, backend |
| [#50 Cadastro de Atrações e Eventos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/50) | must-have | app, backend |
| [#51 Cadastro de Estabelecimentos Gastronômicos](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/51) | must-have | app, backend |
| [#52 Modo Gestor e Painel](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/52) | should-have | app |
| [#53 Responder Avaliações](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/53) | should-have | app, backend |

## [Milestone 8: Qualidade e Lançamento](https://github.com/alan-mendes-ufca/CaririCultural-wiki/milestone/9)

Acessibilidade (WCAG 2.1 AA), desempenho, monitoramento, testes de usabilidade no app nativo e publicação na Google Play.

| Issue | Prioridade | Área |
| --- | --- | --- |
| [#54 Acessibilidade](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/54) | must-have | app, ux |
| [#55 Desempenho](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/55) | must-have | app |
| [#56 Monitoramento de Erros e Métricas](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/56) | — | app, infra |
| [#57 Testes de Usabilidade do App](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/57) | — | ux |
| [#58 Publicação na Google Play](https://github.com/alan-mendes-ufca/CaririCultural-wiki/issues/58) | must-have | app, infra |
