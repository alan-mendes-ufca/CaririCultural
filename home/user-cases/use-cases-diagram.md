---
title: Diagramas de Casos de Uso
---
Os diagramas seguem a notação de **Diagrama de Casos de Uso (UML)** adaptada à sintaxe do Mermaid (que não possui um tipo de diagrama "use case" nativo):

- **Atores** → forma "stadium" (`([Texto])`), a aproximação mais próxima do boneco-palito em Mermaid.
- **Casos de uso** → forma circular (`((Texto))`), aproximando a elipse UML.
- **Fronteira do sistema** → `subgraph`, representando o retângulo que envolve os casos de uso.
- **Relações `include` e `extend`** → setas tracejadas rotuladas.
- **Associação ator–caso de uso** → linha simples (`---`).
- **Generalização/especialização de ator** → seta tracejada rotulada "especializa".

---

## 1. Visão geral da linha de base

Resumo macro dos épicos Must/Should/Could e seus atores principais. Serve como mapa de navegação para os diagramas detalhados (2 a 5).

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    VA([Votante Anônimo])
    CUR([Curador da Plataforma])

    %% Fronteira do Sistema
    subgraph CC [Sistema Cariri Cultural]
        direction TB
        C1((Explorar, pesquisar e consultar locais/eventos))
        C2((Consultar avaliações e mídia comunitária))
        C3((Usar assistente virtual))
        C4((Receber recomendações e roteiros))
        C5((Organizar listas, visitas e checklists))
        C6((Avaliar, publicar mídia, compartilhar e votar))
        C7((Sinalizar e tratar dado incorreto))
    end

    %% Relações Ator -> Caso de Uso
    V --- C1 & C2 & C3
    U --- C4 & C5 & C6 & C7
    VA --- C6
    CUR --- C7

    %% Especialização
    U -.->|especializa| V
```

> Ver diagramas 2 a 5 para os casos de uso individuais (UC-01 a UC-17) que compõem cada bolha acima.

---

## 2. Experiência pública: Exploração e Detalhes

Ações do Visitante para encontrar e avaliar informações básicas de locais e eventos.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    CUR([Curador da Plataforma])
    GEO([Serviço de Geolocalização])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC01((UC-01 Explorar catálogo))
        UC02((UC-02 Pesquisar e filtrar))
        UC03((UC-03 Consultar detalhes do local))
        UC04((UC-04 Consultar eventos e atrações))
        UC05((UC-05 Consultar avaliações e mídia))
        UC26((UC-26 Sinalizar e tratar dado incorreto))

        %% Includes do UC-03
        UC03A((Identidade e contexto))
        UC03B((Informações operacionais))
        UC03C((Condições da visita))

        %% Extends
        PROX((Ordenar por proximidade))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC01 & UC02 & UC03 & UC04 & UC05
    U --- UC26
    CUR --- UC26
    U -.->|especializa| V

    %% Relações Include / Extend
    UC03 -.->|include| UC03A
    UC03 -.->|include| UC03B
    UC03 -.->|include| UC03C

    PROX -.->|extend| UC02
    GEO --- PROX

    UC26 -.->|extend| UC03
    UC26 -.->|extend| UC04
```

---

## 3. Experiência pública: Logística e Deslocamento

Isolado para não poluir o diagrama de exploração. Mostra como o usuário lida com trajetos e transporte parceiro.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    MAP([Serviço de Mapas e Transportes])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC03((UC-03 Consultar detalhes do local))
        UC04((UC-04 Consultar eventos e atrações))
        UC16((UC-16 Consultar transporte parceiro))

        %% Extends
        TRAJ((Obter trajeto geral))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC16

    %% Relações Include / Extend
    UC16 -.->|extend: parceiro ativo| UC03
    UC16 -.->|extend: parceiro ativo| UC04
    TRAJ -.->|extend: solicitar trajeto| UC03

    MAP --- TRAJ
```

---

## 4. Área pessoal: Planejamento e Roteiros

Funcionalidades exclusivas do Usuário Autenticado para organizar sua própria experiência.

```mermaid
flowchart LR
    %% Atores
    U([Usuário Autenticado])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC08((UC-08 Receber recomendações))
        UC09((UC-09 Gerar roteiro personalizado))
        UC10((UC-10 Gerenciar listas))
        UC11((UC-11 Registrar visitas))
        UC12((UC-12 Usar checklists))
        UC15((UC-15 Compartilhar lista))

        %% Includes
        AUTH((Autenticar usuário))
    end

    %% Relações Ator -> Caso de Uso
    U --- UC08 & UC09 & UC10 & UC11 & UC12

    %% Relações Include / Extend
    UC10 -.->|include| AUTH
    UC11 -.->|include| AUTH

    UC15 -.->|extend: compartilhar| UC10
    UC12 -.->|extend: criar do roteiro| UC09
```

---

## 5. Engajamento: Comunidade, Votação e Assistente

Interação social, publicação de conteúdo e uso do assistente virtual.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    VA([Votante Anônimo])
    AUD([Serviço de Transcrição de Áudio])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC06((UC-06 Usar assistente virtual))
        UC07((UC-07 Publicar avaliação))
        UC13((UC-13 Criar e compartilhar enquete))
        UC14((UC-14 Votar em enquete))
        UC17((UC-17 Publicar mídia comunitária))

        %% Includes
        AUTH((Autenticar usuário))

        %% Extends do UC-06
        CTX((Aplicar contexto da página))
        AUDIO((Transcrever pergunta))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC06
    U --- UC07 & UC13 & UC17
    VA --- UC14
    U -.->|especializa| V

    %% Relações Include / Extend
    UC07 -.->|include| AUTH
    UC13 -.->|include| AUTH
    UC17 -.->|include| AUTH

    UC06 -.->|extend: iniciado em página| CTX
    UC06 -.->|extend: entrada por áudio| AUDIO
    UC17 -.->|extend: anexar à avaliação| UC07

    AUD --- AUDIO
```

---

## 6. Épico 8 fora da linha de base

UC-18 a UC-25 não aparecem nos diagramas acima porque ainda não foram validados.
