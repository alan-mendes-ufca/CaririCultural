# Aplicativo Android — Visão do Produto

Esta página conecta a documentação de requisitos e design ao desenvolvimento do **aplicativo nativo Android** do Cariri Cultural. O plano de entregas está no [Roadmap](Roadmap).

## Problema e proposta

A [pesquisa com usuários](Entrevistas) e o [questionário](Question%C3%A1rio-com-Usu%C3%A1rios) mostraram que moradores e visitantes do Cariri têm dificuldade de descobrir locais, eventos e informações confiáveis (horários, preços, acessibilidade, segurança) antes de sair de casa. O app reúne essas informações num **catálogo regional unificado**, com **avaliações da comunidade**, **roteiros e listas pessoais** e um **assistente virtual** que responde com base nos dados do catálogo.

## Públicos

| Perfil | Descrição | Referências |
| --- | --- | --- |
| Visitante / Explorador | Novo morador, turista ou morador de longa data que quer descobrir e planejar passeios | [Storytelling](Storytelling), [PATHY](PATHY-Personas), [Mapas de Jornada](Mapas-de-Jornada) |
| Usuário autenticado | Explorador que avalia locais, salva listas, roteiros e checklists | [Histórias de Usuário](Hist%C3%B3rias-de-Usu%C3%A1rio) |
| Gestor / Administrador | Responsável por equipamentos culturais, atrações e estabelecimentos | [Casos de Uso Descritivos](Casos-de-Uso-Descritivos), [Service Blueprint](Service-Blueprint) |

## Escopo do MVP

O MVP corresponde aos itens **Must have** da priorização MoSCoW:
[Requisitos Funcionais Priorizados](Requisitos-Funcionais-Priorizados), [Requisitos Não Funcionais Priorizados](Requisitos-N%C3%A3o-Funcionais-Priorizados) e [Regras de Negócio Priorizadas](Regras-de-Neg%C3%B3cio-Priorizadas). Itens *Should have* entram nas mesmas milestones como incrementos, identificados pela label `should-have`; itens *Could have* e *Won't have* ficam fora do plano inicial.

## Da documentação às milestones

| Épico (requisitos) | Milestone |
| --- | --- |
| Base técnica, navegação global (Épico 13) | Milestone 1: Fundação |
| Épico 1 — Exploração e Descoberta; Épico 2 — Informações e Detalhes do Local; fluxos do Épico 14 | Milestone 2: Catálogo e Descoberta |
| Requisitos transversais de segurança e privacidade; Épico 12 — Perfil e Autenticação | Milestone 3: Usuários, Autenticação e Privacidade |
| Épico 3 — Avaliações e Comunidade; Épico 9 | Milestone 4: Avaliações e Comunidade |
| Épico 4 — Recomendações; Épico 5 — Organização Pessoal e Roteiros | Milestone 5: Planejamento Pessoal |
| Épico 6 — Assistente Virtual | Milestone 6: Assistente Virtual |
| Épico 8 — Equipamentos e Estabelecimentos; Épico 11 — Gestão | Milestone 7: Gestão de Estabelecimentos |
| RNFs de acessibilidade, desempenho, disponibilidade; publicação | Milestone 8: Qualidade e Lançamento |

Cada issue cita os RFs, RNFs, regras de negócio, casos de uso e histórias que a originam, mantendo a [rastreabilidade](Matriz-de-Rastreabilidade) até o código.

## Arquitetura proposta

> [!NOTE]
> Proposta inicial para discussão. A decisão final será registrada nas issues **Proposta de Arquitetura e Pastas** e **Backend e Contrato da API** (Milestone 1).

```
┌──────────────────────── App Android ────────────────────────┐
│  :feature:* (explorar, local, agenda, assistente, perfil…)  │
│        UI em Jetpack Compose + ViewModel (MVVM / UDF)       │
│  :core:designsystem   :core:data   :core:model              │
│  :core:network (Retrofit/OkHttp)   :core:database (Room)    │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTPS / TLS 1.2+
┌──────────────────────────────▼──────────────────────────────┐
│ Backend: API REST (OpenAPI) · autenticação · catálogo ·     │
│ avaliações · listas/roteiros · importação de fontes externas│
│ · serviço do assistente (LLM + busca no catálogo)           │
└─────────────────────────────────────────────────────────────┘
```

| Camada | Escolha proposta | Motivação (requisitos) |
| --- | --- | --- |
| Linguagem e UI | Kotlin, Jetpack Compose, Material 3 | Padrão atual do Android; acessibilidade nativa (RNF-ACE-001) |
| Arquitetura | MVVM com fluxo de dados unidirecional, módulos por feature, Hilt | Testabilidade e evolução por épicos |
| Dados locais | Room + DataStore, estratégia offline-first para o catálogo | Carregamento do catálogo em até 2 s (RNF-DES-001) e uso com conexão instável |
| Rede | Retrofit, OkHttp, kotlinx.serialization | HTTPS/TLS (RNF-PDD-001) e contrato OpenAPI |
| Mapas | Google Maps SDK + intents para apps de navegação | Localização e trajeto (RF-011, RF-078) |
| Assistente | Chamadas ao backend, que guarda as chaves e consulta o catálogo | Chaves protegidas (RNF-SEG-015), respostas baseadas no catálogo (RN-054, RN-055) e fallback (RNF-DIS-005) |
| Qualidade | ktlint/detekt, testes unitários e de UI, GitHub Actions | Esteira da Milestone 1 |

## Decisões em aberto

- **Estratégia de entrega**: o [RNF-POR-004](Requisitos-N%C3%A3o-Funcionais#RNF-POR-004) previa PWA ou app híbrido; a opção por um app nativo precisa ser registrada e o requisito revisado (issue na Milestone 1).
- **Tecnologia do backend**: API própria ou BaaS (Firebase/Supabase), avaliada pelos RNFs de disponibilidade, escalabilidade, segurança e LGPD.
- **Painel administrativo**: os fluxos de gestor do protótipo ficam no app (modo Gestor); a necessidade de um painel web separado deve ser validada com os stakeholders.
