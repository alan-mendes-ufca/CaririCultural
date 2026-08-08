---
title: Diagramas de Casos de Uso
---
- Os diagramas seguem a notação de **Diagrama de Casos de Uso (UML)** adaptada à sintaxe do Mermaid (que não possui um tipo de diagrama "use case" nativo).
- **Atenção:** A autenticação de usuário comum é **pré-condição** de uso da plataforma, não um caso de uso (por isso não há nó de autenticação genérico nestes diagramas); o único caso de autenticação modelado é UC-038 (administrador), nos diagramas 8 e 9.

---

## 1. Visão geral por épico e ator
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    VA([Votante Anônimo])
    G([Gestor])
    ADM([Administrador autorizado<br/>em curadoria])
    RESP([Responsável pelo local])
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])
    AEG([Administrador de estabelecimento gastronômico])

    %% Fronteira do Sistema
    subgraph CC [Sistema Cariri Cultural]
        direction TB
        C1((Descoberta e busca))
        C2((Perfil do local))
        C3((Agenda comunidade e avaliações))
        C4((Assistente virtual))
        C5((Área pessoal e roteiros))
        C6((Social enquetes e compartilhamento))
        C7((Gestão administrativa — hipótese))
    end

    %% Relações Ator -> Agrupamento
    V --- C1 & C2 & C3 & C4 & C5 & C6 & C7
    VA --- C6
    ADM --- C3
    RESP --- C3
    G --- C7
    APL --- C7
    AEC --- C7
    AEG --- C7
```

---

## 2. Descoberta e busca
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    GEO([Serviço de Geolocalização])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC001((UC-001 Catálogo regional))
        UC002((UC-002 Locais em alta visitação))
        UC003((UC-003 Locais pouco divulgados))
        UC004((UC-004 Pesquisa por termo))
        UC005((UC-005 Filtro por categoria e público))
        UC069((UC-069 Validar parâmetros de busca))
        UC070((UC-070 Buscar por proximidade))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC001 & UC002 & UC003 & UC004 & UC005

    %% Relações Include / Extend
    UC004 -.->|include| UC069
    UC005 -.->|include| UC069

    UC002 -.->|extend| UC001
    UC003 -.->|extend| UC001

    UC070 -.->|extend| UC004
    UC070 -.->|extend| UC005
    GEO --- UC070
```

---

## 3. Perfil do local
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    MAP([Serviço de Mapas e Transportes])

    %% Fronteira
    subgraph CC [Cariri Cultural — perfil do local]
        direction TB
        UC006((UC-006 Perfil do local<br/>ambiente horários preços<br/>regras segurança e público))
        UC007((UC-007 Localização acesso<br/>e opções de transporte))
        UC009((UC-009 Calendário e<br/>programação de eventos))
        UC010((UC-010 Canais de contato<br/>e redes sociais))
        UC011((UC-011 Imagens do local<br/>na plataforma))
        UC008((UC-008 Condições de higiene<br/>fora do escopo desta entrega))
        UC071((UC-071 Procedência do dado<br/>e canal externo))

        %% Nós convidados: extensões vindas dos diagramas 4 e 7
        UC072((UC-072 Filtrar agenda por data))
        UC080((UC-080 Sinalizar e acompanhar<br/>dado incorreto))
        UC033((UC-033 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC006 & UC007 & UC009 & UC010 & UC011
    MAP --- UC007

    %% Relações Include
    UC006 -.->|include| UC071
    UC007 -.->|include| UC071
    UC009 -.->|include| UC071
    UC010 -.->|include| UC071

    %% Relações Extend vindas de fora do recorte
    UC072 -.->|extend| UC009
    UC080 -.->|extend| UC006 & UC007 & UC009 & UC010
    UC033 -.->|extend| UC006 & UC007 & UC009 & UC010

    classDef fora fill:#f4f4f4,stroke:#9e9e9e,stroke-dasharray:4 3,color:#6b6b6b
    class UC008 fora
```

> Os antigos diagramas 3, 4 e 5 foram unificados aqui: a consolidação do Épico 2 reduziu o perfil do local a seis casos, e manter três recortes passou a repetir os mesmos nós.
> UC-008 aparece tracejado por estar fora do escopo desta entrega; não recebe include nem extend enquanto essa decisão valer.
> UC-009 reaparece no diagrama 4, onde seu ciclo de vida é controlado por UC-072. UC-071, UC-080 e UC-033 são nós convidados, detalhados nos diagramas 4 e 7.

---

## 4. Agenda, comunidade e avaliações
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    ADM([Administrador autorizado<br/>em curadoria])
    RESP([Responsável pelo local])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC009((UC-009 Calendário e programação de eventos))
        UC012((UC-012 Avaliações da comunidade))
        UC013((UC-013 Publicar avaliação))
        UC031((UC-031 Mídias publicadas pela comunidade))
        UC051((UC-051 Marcar avaliação como útil))
        UC052((UC-052 Compartilhar avaliação individual))
        UC053((UC-053 Iniciar tópico de discussão))
        UC072((UC-072 Filtrar agenda por data))
        UC073((UC-073 Retomar rascunho após autenticação))
        UC080((UC-080 Sinalizar e acompanhar dado incorreto))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC009 & UC012 & UC031 & UC072 & UC013 & UC051 & UC052 & UC053 & UC073 & UC080
    ADM --- UC080
    RESP --- UC080

    %% Relações Extend
    UC051 -.->|extend| UC012
    UC052 -.->|extend| UC012
    UC031 -.->|extend| UC012
    UC072 -.->|extend| UC009
    UC073 -.->|extend| UC013
    UC073 -.->|extend| UC080
```

---

## 5. Assistente virtual
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    AUD([Serviço de Transcrição de Áudio])
    FONTE([Fonte de dados externa])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC021((UC-021 Consultar assistente virtual))
        UC022((UC-022 Resposta interpretada por intenção))
        UC023((UC-023 Orientação alternativa))
        UC024((UC-024 Contexto da tela))
        UC025((UC-025 Dados por fonte externa))
        UC026((UC-026 Links de redes sociais pelo assistente))
        UC027((UC-027 Imagens do local pelo assistente))
        UC028((UC-028 Pergunta por áudio))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC021 & UC022 & UC023 & UC024 & UC025 & UC026 & UC027 & UC028
    AUD --- UC028
    FONTE --- UC025

    %% Relações Extend
    UC022 -.->|extend| UC021
    UC023 -.->|extend| UC021
    UC024 -.->|extend| UC021
    UC026 -.->|extend| UC021
    UC027 -.->|extend| UC021
    UC028 -.->|extend| UC021
```

---

## 6. Área pessoal: recomendações, roteiros, listas e gamificação
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    MAP([Serviço de Mapas e Transportes])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC014((UC-014 Recomendação por histórico de visitas))
        UC015((UC-015 Recomendação por avaliações realizadas))
        UC016((UC-016 Recomendação por perfis similares))
        UC017((UC-017 Gerar roteiro personalizado))
        UC018((UC-018 Gerenciar listas de locais desejados))
        UC019((UC-019 Registrar locais visitados))
        UC020((UC-020 Checklist de atividades e passeios))
        UC032((UC-032 Compartilhar lista por link))
        UC054((UC-054 Conquistas e distintivos))
        UC055((UC-055 Dicas contextuais no checklist))
        UC074((UC-074 Alternativa de personalização))
        UC075((UC-075 Salvar e ajustar roteiro))
        UC076((UC-076 Alerta de item vinculado a atração inativa))
        UC078((UC-078 Revogar link público de lista))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC014 & UC015 & UC016 & UC017 & UC018 & UC019 & UC020
    V --- UC032 & UC054 & UC055 & UC074 & UC075 & UC076 & UC078
    MAP --- UC017

    %% Relações Include
    UC017 -.->|include| UC075

    %% Relações Extend
    UC074 -.->|extend| UC014
    UC074 -.->|extend| UC015
    UC074 -.->|extend| UC016
    UC076 -.->|extend| UC020
    UC055 -.->|extend| UC020
    UC078 -.->|extend| UC032
```

---

## 7. Social, enquetes, transporte e compartilhamento
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    VA([Votante Anônimo])
    TP([Serviço/operador de transporte parceiro])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC029((UC-029 Criar e compartilhar enquete))
        UC030((UC-030 Transporte alternativo parceiro))
        UC077((UC-077 Votar em enquete))
        UC079((UC-079 Acionar contato de transporte parceiro))
        UC033((UC-033 Compartilhar perfil de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC030 & UC079 & UC029 & UC033
    VA --- UC077
    TP --- UC030 & UC079

    %% Relações Include / Extend
    UC029 -.->|include| UC077
    UC079 -.->|extend| UC030
```

---

## 8. Hipótese administrativa — equipamentos culturais e atrações
> [!WARNING]
> Os diagramas 8 a 11 modelam **hipóteses verificáveis**. O núcleo de cadastro administrativo (UC-034, UC-036, UC-038 a UC-040, UC-042 e UC-043) já integra a entrega atual; os demais casos do Épico 8 (UC-041 e UC-044 a UC-050) e a totalidade dos Épicos 11 a 13 permanecem fora dela. Em todos os casos, os fluxos e telas administrativas ainda dependem de validação com os futuros stakeholders administrativos.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])

    subgraph CC [Cariri Cultural — equipamentos e atrações]
        direction TB
        UC034((UC-034 Cadastrar equipamento cultural))
        UC035((UC-035 Editar equipamento cultural))
        UC036((UC-036 Consultar equipamento cultural))
        UC037((UC-037 Associar administrador a equipamento))
        UC038((UC-038 Autenticar administrador))
        UC039((UC-039 Cadastrar atração))
        UC040((UC-040 Editar atração))
        UC041((UC-041 Remover atração))
        UC042((UC-042 Consultar atrações cadastradas))

        %% Nós convidados: extensões vindas dos diagramas 4 e 7
        UC080((UC-080 Sinalizar e acompanhar<br/>dado incorreto))
        UC033((UC-033 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    APL --- UC034 & UC035 & UC037
    AEC --- UC038 & UC039 & UC040 & UC041
    V --- UC036 & UC042 & UC080 & UC033

    %% Relações Include
    UC034 -.->|include| UC038
    UC035 -.->|include| UC038
    UC037 -.->|include| UC038
    UC039 -.->|include| UC038
    UC040 -.->|include| UC038
    UC041 -.->|include| UC038

    %% Relações Extend
    UC080 -.->|extend| UC036 & UC042
    UC033 -.->|extend| UC036 & UC042
```

---

## 9. Hipótese administrativa — estabelecimentos, ofertas e publicações
```mermaid
flowchart LR
    %% Atores
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])
    AEG([Administrador de estabelecimento gastronômico])

    subgraph CC [Cariri Cultural — estabelecimentos e conteúdos]
        direction TB
        UC038((UC-038 Autenticar administrador))
        UC043((UC-043 Cadastrar estabelecimento gastronômico))
        UC044((UC-044 Cadastrar oferta))
        UC045((UC-045 Editar oferta))
        UC046((UC-046 Remover oferta))
        UC047((UC-047 Cadastrar publicação))
        UC048((UC-048 Criar publicação vinculada a local))
        UC049((UC-049 Editar publicação))
        UC050((UC-050 Remover publicação))
    end

    %% Relações Ator -> Caso de Uso
    APL --- UC043 & UC047
    AEG --- UC044 & UC045 & UC046 & UC048 & UC049 & UC050
    AEC --- UC048 & UC049 & UC050

    %% Relações Include
    UC043 -.->|include| UC038
    UC044 -.->|include| UC038
    UC045 -.->|include| UC038
    UC046 -.->|include| UC038
    UC047 -.->|include| UC038
    UC048 -.->|include| UC038
    UC049 -.->|include| UC038
    UC050 -.->|include| UC038
```

> UC-038 é o mesmo caso do diagrama 8; aparece nos dois recortes porque é incluído por ações de escrita de ambos.

---

## 10. Gestão de estabelecimentos — painel e indicadores
```mermaid
flowchart LR
    %% Atores
    G([Gestor])

    subgraph CC [Cariri Cultural — painel do Gestor]
        direction TB
        UC056((UC-056 Painel de métricas do estabelecimento))
        UC057((UC-057 Feed de atividades recentes))
        UC058((UC-058 Responder publicamente a avaliação))
        UC059((UC-059 Visualizar página pública))
        UC060((UC-060 Indicadores de desempenho))
        UC061((UC-061 Mapa de origem dos visitantes))
    end

    %% Relações Ator -> Caso de Uso
    G --- UC056 & UC057 & UC058 & UC059 & UC060 & UC061

    %% Relações Extend
    UC059 -.->|extend| UC056
```

---

## 11. Perfil, sessão e navegação global
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    G([Gestor])

    subgraph CC [Cariri Cultural — perfil e navegação]
        direction TB
        UC062((UC-062 Alternar modos Explorador e Gestor))
        UC063((UC-063 Nível de parceria na plataforma))
        UC064((UC-064 Certificações e qualificações))
        UC065((UC-065 Encerrar sessões ativas))
        UC066((UC-066 Barra inferior do Explorador))
        UC067((UC-067 Barra inferior do Gestor))
        UC068((UC-068 Cabeçalho contextual da tela))
    end

    %% Relações Ator -> Caso de Uso
    G --- UC062 & UC063 & UC064 & UC067
    V --- UC065 & UC066 & UC068
```

---
