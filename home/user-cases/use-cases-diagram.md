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

Resumo macro dos épicos Must/Should/Could e da hipótese administrativa do Épico 8. Serve como mapa de navegação para os diagramas detalhados (2 a 6).

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    VA([Votante Anônimo])
    ADM([Administrador autorizado<br/>em curadoria])
    RESP([Responsável pelo local])
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])
    AEG([Administrador de estabelecimento gastronômico])

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
        C8((Gerir cadastros e conteúdos<br/>administrativos — hipótese))
    end

    %% Relações Ator -> Caso de Uso
    V --- C1 & C2 & C3
    U --- C4 & C5 & C6 & C7
    VA --- C6
    ADM --- C7
    RESP --- C7
    APL --- C8
    AEC --- C8
    AEG --- C8

    %% Especialização
    U -.->|especializa| V
```

> Ver diagramas 2 a 5 para os casos de uso da linha de base (UC-01 a UC-17 e UC-26) e o diagrama 6 para as hipóteses UC-18 a UC-25.

---

## 2. Experiência pública: Exploração e Detalhes

Ações do visitante para encontrar informações de locais e eventos, incluindo a extensão autenticada para sinalizar dados incorretos.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    ADM([Administrador autorizado<br/>em curadoria])
    RESP([Responsável pelo local])
    GEO([Serviço de Geolocalização])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC01((UC-01 Explorar catálogo))
        UC02((UC-02 Pesquisar e filtrar))
        UC03((UC-03 Consultar detalhes do local))
        UC04((UC-04 Consultar eventos, equipamentos e atrações))
        UC05((UC-05 Consultar avaliações e mídia))
        UC26((UC-26 Sinalizar e tratar dado incorreto))

        %% Includes do UC-03
        UC03A((Identidade e contexto))
        UC03B((Informações operacionais))
        UC03C((Condições da visita))

        %% Extends
        PROX((Buscar por proximidade))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC01 & UC02 & UC03 & UC04 & UC05
    U --- UC26
    ADM --- UC26
    RESP --- UC26
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
    TP([Serviço/operador de transporte parceiro])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC03((UC-03 Consultar detalhes do local))
        UC04((UC-04 Consultar eventos, equipamentos e atrações))
        UC16((UC-16 Consultar transporte alternativo parceiro))

        %% Extends
        TRAJ((Obter trajeto geral))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC03 & UC04 & UC16
    TP --- UC16

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
    MAP([Serviço de Mapas e Transportes])

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
    U --- UC08 & UC09 & UC10 & UC11 & UC12 & UC15
    MAP --- UC09

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

    CTX -.->|extend: iniciado em página| UC06
    AUDIO -.->|extend: entrada por áudio| UC06
    UC17 -.->|extend: anexar à avaliação| UC07

    AUD --- AUDIO
```

---

## 6. Hipótese de escopo administrativo: Equipamentos e estabelecimentos

Os fluxos do Épico 8 foram modelados como hipóteses verificáveis, derivadas de RF-042 a RF-058 e HU-042 a HU-058. O núcleo de cadastro administrativo (RF-042, RF-044, RF-046 a RF-048, RF-050 e RF-051) já integra a entrega atual; os demais (RF-049 e RF-052 a RF-058) permanecem fora dela. Em ambos os casos, os fluxos e telas administrativas ainda dependem de validação com os futuros stakeholders administrativos.

```mermaid
flowchart LR
    %% Atores
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])
    AEG([Administrador de estabelecimento gastronômico])
    V([Visitante])

    %% Fronteira
    subgraph CC [Cariri Cultural — hipótese do Épico 8]
        direction TB
        UC18((UC-18 Cadastrar equipamento cultural))
        UC19((UC-19 Editar equipamento cultural))
        UC20((UC-20 Consultar equipamento cultural))
        UC21((UC-21 Associar administrador a equipamento))
        UC22((UC-22 Autenticar administrador))
        UC23((UC-23 Gerenciar atrações))
        UC24((UC-24 Cadastrar estabelecimento e gerenciar ofertas))
        UC25((UC-25 Gerenciar publicações administrativas))
    end

    %% Relações Ator -> Caso de Uso
    APL --- UC18 & UC19 & UC21 & UC22 & UC24 & UC25
    AEC --- UC22 & UC23 & UC25
    AEG --- UC22 & UC24 & UC25
    V --- UC20 & UC23

    %% Relações Include
    UC18 -.->|include| UC22
    UC19 -.->|include| UC22
    UC21 -.->|include| UC22
    UC23 -.->|include| UC22
    UC24 -.->|include| UC22
    UC25 -.->|include| UC22
```

---
