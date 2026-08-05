# Relatório de Inspeção de Usabilidade — Protótipo de Alta Fidelidade
## Plataforma Cariri Cultural

**Data da inspeção:** [preencher]
**Responsáveis pela inspeção:** [preencher]
**Versão do protótipo inspecionada:** [preencher]

---

## 1. Introdução

### 1.1 Objetivo
Este relatório documenta a inspeção de usabilidade realizada sobre o protótipo de alta fidelidade da plataforma Cariri Cultural, com o objetivo de identificar inconsistências visuais, de navegação, de acessibilidade e de cobertura de requisitos antes da evolução para a próxima etapa de desenvolvimento.

### 1.2 Passo a passo da inspeção
1. **Preparação:** definição do escopo de telas a inspecionar, com base nas Histórias de Usuário e nos Casos de Uso já validados (fluxos de descoberta, chat com assistente virtual, comunidade, perfil de gestor e detalhes de local).
2. **Percurso guiado (walkthrough):** navegação sequencial pelo protótipo simulando os principais fluxos de uso (exploração de locais, uso do assistente virtual, avaliação de estabelecimentos, navegação como gestor).
3. **Inspeção heurística:** avaliação de cada tela quanto a consistência visual (cores, ícones, iconografia), legibilidade/contraste, comportamento responsivo (teclado virtual, elementos fixos) e clareza da informação apresentada.
4. **Checagem cruzada com requisitos:** comparação do que foi observado no protótipo com os Requisitos Funcionais, Requisitos Não Funcionais e Histórias de Usuário já documentados, para identificar tanto desvios de implementação quanto lacunas de requisito.
5. **Registro:** cada desvio identificado foi documentado como uma inconsistência individual, com print de tela, artefato impactado e proposta de correção.
6. **Consolidação:** as inconsistências foram agrupadas em resumos temáticos e vinculadas em matriz de rastreabilidade para acompanhamento até a correção.

### 1.3 Escopo inspecionado
- Tela inicial (Home)
- Tela do Assistente Virtual (Chatbot)
- Tela de Comunidade
- Tela de detalhes do local
- Perfil e painel do gestor
- Ícones e elementos de navegação global

---

## 2. Inconsistências identificadas

---

### INSP-01 — Contraste insuficiente da cor das letras sobre fundo vermelho

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-01.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo de Alta Fidelidade (telas com uso de vermelho/alertas) × RNF-ACE-002 (Conformidade WCAG 2.1 AA) |
| Correção aplicada | Ajuste do par de cores texto/fundo para atingir contraste mínimo 4.5:1 (WCAG AA) |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-02 — Barra de input do chatbot não some ao enviar a mensagem

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-02.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — tela do Assistente Virtual × RF-030 a RF-037 |
| Correção aplicada | Ajuste do comportamento da barra para recolher/ocultar corretamente durante o envio e a exibição da resposta |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-03 — Botão de enviar fica oculto quando o teclado sobe

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-03.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — tela do chat × requisito de usabilidade mobile |
| Correção aplicada | Reposicionamento do botão de envio para permanecer visível acima do teclado (ajuste de layout responsivo / safe area) |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-04 — Ambiguidade no símbolo de configurações

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-04.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — ícone de configurações |
| Correção aplicada | Substituição por ícone padrão (engrenagem) reconhecível, com rótulo/tooltip |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-05 — Símbolo de pesquisa duplicado no aplicativo

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-05.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — telas com ícone de busca |
| Correção aplicada | Padronização de um único ícone de pesquisa em todas as telas |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-06 — Ícone do assistente inconsistente entre Home e Comunidade

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-06.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — telas Home × Comunidade |
| Correção aplicada | Padronização do ícone do assistente virtual conforme design system único |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-07 — Botão "Painel do Gestor" redundante no perfil do gestor

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-07.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — tela de perfil do gestor × RF-074/RF-075 (navegação do gestor) |
| Correção aplicada | Remoção do botão redundante ou redirecionamento a um destino distinto (ex. configurações do perfil) |
| Nova versão gerada | Protótipo v[a definir] |

---

### INSP-08 — Informação de acessibilidade genérica ("sim", sem especificar o quê)

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-08.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Protótipo — tela de detalhes do local × RF-011, HU-011 |
| Correção aplicada | Substituição do campo binário por lista de recursos específicos (rampa, vaga PCD, banheiro adaptado, piso tátil, elevador etc.) |
| Nova versão gerada | Protótipo v[a definir] + RF-011 revisado |

---

### INSP-09 — Falta de requisito para compartilhar o perfil de um local específico

**Imagem da inconsistência:**
`[inserir print de tela aqui — ex. ./imagens/insp-09.png]`

| Campo | Descrição |
|---|---|
| Requisito/Artefato impactado | Requisitos Funcionais — Épico 7 (Interações Sociais): requisito ausente |
| Correção aplicada | Criação de novo RF: *"O sistema deve permitir que o usuário compartilhe o perfil de um local específico via link externo ou aplicativos de mensagem."* + HU correspondente |
| Nova versão gerada | Requisitos Funcionais v[a definir] (novo RF a numerar) |

---

## 3. Resumo das inconsistências

| ID | Inconsistência | Categoria | Severidade |
|---|---|---|---|
| INSP-01 | Contraste insuficiente da cor das letras sobre fundo vermelho | Acessibilidade / Visual | Alta |
| INSP-02 | Barra de input do chatbot não some ao enviar mensagem | Comportamento / Layout | Média |
| INSP-03 | Botão de enviar oculto quando o teclado sobe | Comportamento / Layout responsivo | Alta |
| INSP-04 | Ambiguidade no símbolo de configurações | Iconografia | Média |
| INSP-05 | Símbolo de pesquisa duplicado | Iconografia | Baixa |
| INSP-06 | Ícone do assistente inconsistente entre telas | Iconografia | Média |
| INSP-07 | Botão "Painel do Gestor" redundante | Navegação | Baixa |
| INSP-08 | Informação de acessibilidade sem especificação | Conteúdo / Acessibilidade | Alta |
| INSP-09 | Falta de requisito de compartilhamento de local | Lacuna de requisito | Média |

**Total:** 9 inconsistências — 3 de severidade Alta, 4 Média, 2 Baixa.

---

## 4. Resumo das correções

| ID | Correção proposta | Tipo de correção | Situação |
|---|---|---|---|
| INSP-01 | Ajuste de contraste texto/fundo (WCAG AA) | Visual | Pendente |
| INSP-02 | Corrigir comportamento de recolhimento da barra do chat | Comportamental | Pendente |
| INSP-03 | Reposicionar botão de envio acima do teclado | Layout responsivo | Pendente |
| INSP-04 | Padronizar ícone de configurações + rótulo | Iconografia | Pendente |
| INSP-05 | Unificar ícone de pesquisa | Iconografia | Pendente |
| INSP-06 | Padronizar ícone do assistente virtual | Iconografia | Pendente |
| INSP-07 | Remover ou redirecionar botão redundante | Navegação | Pendente |
| INSP-08 | Detalhar campo de acessibilidade em lista de recursos | Conteúdo | Pendente |
| INSP-09 | Criar novo RF + HU de compartilhamento de local | Requisito | Pendente |

**Observação:** os itens INSP-01, 04, 05 e 06 têm causa raiz comum (falta de padronização de design system) — recomenda-se tratá-los em conjunto em uma única correção de guia de estilo, para evitar recorrência do mesmo tipo de inconsistência.

---

## 5. Matriz de rastreabilidade das alterações

| ID | Artefato de origem | Artefato(s) impactado(s) | Tipo de vínculo | Nova versão | Data da correção |
|---|---|---|---|---|---|
| INSP-01 | Protótipo de Alta Fidelidade | RNF-ACE-002 | Conformidade | Protótipo v[a definir] | [preencher] |
| INSP-02 | Protótipo de Alta Fidelidade | RF-030 a RF-037 | Comportamento de funcionalidade | Protótipo v[a definir] | [preencher] |
| INSP-03 | Protótipo de Alta Fidelidade | Requisito de usabilidade mobile (RNF a identificar) | Comportamento de funcionalidade | Protótipo v[a definir] | [preencher] |
| INSP-04 | Protótipo de Alta Fidelidade | — (padronização de UI) | Consistência visual | Protótipo v[a definir] | [preencher] |
| INSP-05 | Protótipo de Alta Fidelidade | — (padronização de UI) | Consistência visual | Protótipo v[a definir] | [preencher] |
| INSP-06 | Protótipo de Alta Fidelidade | — (padronização de UI) | Consistência visual | Protótipo v[a definir] | [preencher] |
| INSP-07 | Protótipo de Alta Fidelidade | RF-074, RF-075 | Navegação/fluxo | Protótipo v[a definir] | [preencher] |
| INSP-08 | Protótipo de Alta Fidelidade | RF-011, HU-011 | Conteúdo/requisito | Protótipo v[a definir] + RF-011 revisado | [preencher] |
| INSP-09 | Requisitos Funcionais (Épico 7) | Novo RF, nova HU | Requisito ausente | Requisitos Funcionais v[a definir] | [preencher] |

---

## 6. Campos a preencher pela equipe
- Data da inspeção e responsáveis
- Versão do protótipo antes/depois de cada correção
- Prints de tela de cada inconsistência (`./imagens/insp-XX.png`)
- Datas de conclusão de cada correção
- Numeração definitiva do novo RF de compartilhamento de local (INSP-09)
