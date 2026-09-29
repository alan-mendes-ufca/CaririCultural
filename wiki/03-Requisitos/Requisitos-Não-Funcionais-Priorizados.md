# Requisitos Não Funcionais Priorizados

Critério usado: requisitos não funcionais indicados como principais para disponibilidade, desempenho, fallback, usabilidade, privacidade, acessibilidade, portabilidade e escalabilidade.

| id | requisito não funcional | descrição priorizada |
| --- | --- | --- |
| [RNF-DIS-001](Requisitos-N%C3%A3o-Funcionais#RNF-DIS-001) | Disponibilidade mínima do sistema | Disponibilidade mínima de 99,5% (uptime), equivalente a aproximadamente 43,8 horas de indisponibilidade por ano. |
| [RNF-DES-001](Requisitos-N%C3%A3o-Funcionais#RNF-DES-001) | Tempo de carregamento do catálogo e listas | Catálogo e listas devem carregar em no máximo 2 segundos (P95) em conexão 4G. |
| [RNF-DES-002](Requisitos-N%C3%A3o-Funcionais#RNF-DES-002) | Tempo de resposta da pesquisa | Pesquisa deve retornar resultados em no máximo 1,5 segundo (P95). |
| [RNF-DES-004](Requisitos-N%C3%A3o-Funcionais#RNF-DES-004) | Tempo de primeira resposta do assistente virtual | Chatbot deve retornar a primeira resposta em no máximo 5 segundos (P95). |
| [RNF-DIS-005](Requisitos-N%C3%A3o-Funcionais#RNF-DIS-005) | Fallback gracioso do assistente virtual | O sistema deve oferecer fallback gracioso quando o serviço de IA estiver indisponível. |
| [RNF-USA-001](Requisitos-N%C3%A3o-Funcionais#RNF-USA-001) | Facilidade de aprendizado | Novo usuário deve conseguir realizar uma busca em menos de 30 segundos. |
| [RNF-PDD-003](Requisitos-N%C3%A3o-Funcionais#RNF-PDD-003) | Conformidade com a LGPD | O sistema deve manter conformidade total com a LGPD (Lei nº 13.709/2018). |
| [RNF-ACE-001](Requisitos-N%C3%A3o-Funcionais#RNF-ACE-001) | Conformidade WCAG 2.1 AA | O sistema deve atender à WCAG 2.1 nível AA para acessibilidade plena. |
| [RNF-POR-002](Requisitos-N%C3%A3o-Funcionais#RNF-POR-002) | Responsividade plena | Layout 100% responsivo para mobile, tablet e desktop. |
| [RNF-POR-004](Requisitos-N%C3%A3o-Funcionais#RNF-POR-004) | Estratégia de deploy universal | Estratégia PWA ou app híbrido para máxima capilaridade. |
| [RNF-ESC-001](Requisitos-N%C3%A3o-Funcionais#RNF-ESC-001) | Suporte a usuários simultâneos em operação normal | Suporte a 1.000 usuários simultâneos em operação normal. |
| [RNF-ESC-002](Requisitos-N%C3%A3o-Funcionais#RNF-ESC-002) | Escalonamento horizontal em picos de demanda | Escalonamento para 5.000 usuários simultâneos em picos, como eventos culturais e feriados. |
