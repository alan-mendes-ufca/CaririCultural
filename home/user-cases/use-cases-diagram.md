---
title: Diagramas de Casos de Uso
---
- Os diagramas seguem a notação de **Diagrama de Casos de Uso (UML)** adaptada à sintaxe do Mermaid (que não possui um tipo de diagrama "use case" nativo).
- **Atenção:** A autenticação de usuário comum é **pré-condição** de uso da plataforma, não um caso de uso (por isso não há nó de autenticação genérico nestes diagramas); o único caso de autenticação modelado é UC-046 (administrador), nos diagramas 10 e 11.

---

## 1. Visão geral por épico e ator
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
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
    V --- C1 & C2 & C3 & C4 & C6
    U --- C3 & C5 & C6 & C7
    VA --- C6
    ADM --- C3
    RESP --- C3
    G --- C7
    APL --- C7
    AEC --- C7
    AEG --- C7

    %% Especialização
    U -.->|especializa| V
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
        UC077((UC-077 Validar parâmetros de busca))
        UC078((UC-078 Buscar por proximidade))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC001 & UC002 & UC003 & UC004 & UC005

    %% Relações Include / Extend
    UC004 -.->|include| UC077
    UC005 -.->|include| UC077

    UC002 -.->|extend| UC001
    UC003 -.->|extend| UC001

    UC078 -.->|extend| UC004
    UC078 -.->|extend| UC005
    GEO --- UC078
```

---

## 3. Perfil do local — identidade e contexto
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])

    %% Fronteira
    subgraph CC [Cariri Cultural — identidade e contexto]
        direction TB
        UC006((UC-006 Fotos e mídias do ambiente))
        UC016((UC-016 Informações históricas e culturais))
        UC017((UC-017 Links de redes sociais do local))
        UC018((UC-018 Imagens do local na plataforma))
        UC019((UC-019 Regras e políticas do local))

        %% Nós convidados: extensões vindas dos diagramas 6 e 9
        UC088((UC-088 Sinalizar e acompanhar<br/>dado incorreto))
        UC089((UC-089 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC006 & UC016 & UC017 & UC018 & UC019
    U --- UC088 & UC089
    U -.->|especializa| V

    %% Relações Extend vindas de fora do recorte
    UC088 -.->|extend| UC006 & UC016 & UC017 & UC018 & UC019
    UC089 -.->|extend| UC006 & UC016 & UC017 & UC018 & UC019
```

---

## 4. Perfil do local — informações operacionais
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])

    %% Fronteira
    subgraph CC [Cariri Cultural — informações operacionais]
        direction TB
        UC007((UC-007 Horários e status de funcionamento))
        UC008((UC-008 Cardápio e faixa de preços))
        UC014((UC-014 Calendário e programação de eventos))
        UC015((UC-015 Canais de contato))
        UC020((UC-020 Formato de serviço))
        UC079((UC-079 Procedência do dado e canal externo))

        %% Nós convidados: extensões vindas dos diagramas 6 e 9
        UC088((UC-088 Sinalizar e acompanhar<br/>dado incorreto))
        UC089((UC-089 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC007 & UC008 & UC014 & UC015 & UC020 & UC079
    U --- UC088 & UC089
    U -.->|especializa| V

    %% Relações Include
    UC007 -.->|include| UC079
    UC008 -.->|include| UC079
    UC014 -.->|include| UC079

    %% Relações Extend vindas de fora do recorte
    UC088 -.->|extend| UC007 & UC008 & UC014 & UC015 & UC020
    UC089 -.->|extend| UC007 & UC008 & UC014 & UC015 & UC020
```

> UC-014 também aparece no diagrama 6, onde é filtrado por data e tem seu ciclo de vida controlado por UC-080. UC-079 reaparece no diagrama 5, pelos mesmos motivos de proveniência.

---

## 5. Perfil do local — condições da visita
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    MAP([Serviço de Mapas e Transportes])

    %% Fronteira
    subgraph CC [Cariri Cultural — condições da visita]
        direction TB
        UC009((UC-009 Localização e opções de transporte))
        UC010((UC-010 Informações de segurança))
        UC011((UC-011 Condições de higiene))
        UC012((UC-012 Recursos de acessibilidade))
        UC013((UC-013 Adequação ao público infantil))
        UC079((UC-079 Procedência do dado e canal externo))

        %% Nós convidados: extensões vindas dos diagramas 6 e 9
        UC088((UC-088 Sinalizar e acompanhar<br/>dado incorreto))
        UC089((UC-089 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC009 & UC010 & UC011 & UC012 & UC013 & UC079
    U --- UC088 & UC089
    MAP --- UC009
    U -.->|especializa| V

    %% Relações Include
    UC009 -.->|include| UC079
    UC010 -.->|include| UC079
    UC012 -.->|include| UC079

    %% Relações Extend vindas de fora do recorte
    UC088 -.->|extend| UC009 & UC010 & UC011 & UC012 & UC013
    UC089 -.->|extend| UC009 & UC010 & UC011 & UC012 & UC013
```

---

## 6. Agenda, comunidade e avaliações
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    ADM([Administrador autorizado<br/>em curadoria])
    RESP([Responsável pelo local])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC014((UC-014 Calendário e programação de eventos))
        UC021((UC-021 Avaliações da comunidade))
        UC022((UC-022 Publicar avaliação))
        UC040((UC-040 Mídias publicadas pela comunidade))
        UC059((UC-059 Marcar avaliação como útil))
        UC060((UC-060 Compartilhar avaliação individual))
        UC061((UC-061 Iniciar tópico de discussão))
        UC080((UC-080 Filtrar agenda por data))
        UC081((UC-081 Retomar rascunho após autenticação))
        UC088((UC-088 Sinalizar e acompanhar dado incorreto))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC014 & UC021 & UC040 & UC080
    U --- UC022 & UC059 & UC060 & UC061 & UC081 & UC088
    ADM --- UC088
    RESP --- UC088
    U -.->|especializa| V

    %% Relações Extend
    UC059 -.->|extend| UC021
    UC060 -.->|extend| UC021
    UC040 -.->|extend| UC021
    UC080 -.->|extend| UC014
    UC081 -.->|extend| UC022
    UC081 -.->|extend| UC088
```

---

## 7. Assistente virtual
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    AUD([Serviço de Transcrição de Áudio])
    FONTE([Fonte de dados externa])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC030((UC-030 Consultar assistente virtual))
        UC031((UC-031 Resposta interpretada por intenção))
        UC032((UC-032 Orientação alternativa))
        UC033((UC-033 Contexto da tela))
        UC034((UC-034 Dados por fonte externa))
        UC035((UC-035 Links de redes sociais pelo assistente))
        UC036((UC-036 Imagens do local pelo assistente))
        UC037((UC-037 Pergunta por áudio))
    end

    %% Relações Ator -> Caso de Uso
    V --- UC030 & UC031 & UC032 & UC033 & UC034 & UC035 & UC036 & UC037
    AUD --- UC037
    FONTE --- UC034

    %% Relações Extend
    UC031 -.->|extend| UC030
    UC032 -.->|extend| UC030
    UC033 -.->|extend| UC030
    UC035 -.->|extend| UC030
    UC036 -.->|extend| UC030
    UC037 -.->|extend| UC030
```

---

## 8. Área pessoal: recomendações, roteiros, listas e gamificação
```mermaid
flowchart LR
    %% Atores
    U([Usuário Autenticado])
    MAP([Serviço de Mapas e Transportes])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC023((UC-023 Recomendação por histórico de visitas))
        UC024((UC-024 Recomendação por avaliações realizadas))
        UC025((UC-025 Recomendação por perfis similares))
        UC026((UC-026 Gerar roteiro personalizado))
        UC027((UC-027 Gerenciar listas de locais desejados))
        UC028((UC-028 Registrar locais visitados))
        UC029((UC-029 Checklist de atividades e passeios))
        UC041((UC-041 Compartilhar lista por link))
        UC062((UC-062 Conquistas e distintivos))
        UC063((UC-063 Dicas contextuais no checklist))
        UC082((UC-082 Alternativa de personalização))
        UC083((UC-083 Salvar e ajustar roteiro))
        UC084((UC-084 Alerta de item vinculado a atração inativa))
        UC086((UC-086 Revogar link público de lista))
    end

    %% Relações Ator -> Caso de Uso
    U --- UC023 & UC024 & UC025 & UC026 & UC027 & UC028 & UC029
    U --- UC041 & UC062 & UC063 & UC082 & UC083 & UC084 & UC086
    MAP --- UC026

    %% Relações Include
    UC026 -.->|include| UC083

    %% Relações Extend
    UC082 -.->|extend| UC023
    UC082 -.->|extend| UC024
    UC082 -.->|extend| UC025
    UC084 -.->|extend| UC029
    UC063 -.->|extend| UC029
    UC086 -.->|extend| UC041
```

---

## 9. Social, enquetes, transporte e compartilhamento
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    VA([Votante Anônimo])
    TP([Serviço/operador de transporte parceiro])

    %% Fronteira
    subgraph CC [Cariri Cultural]
        direction TB
        UC038((UC-038 Criar e compartilhar enquete))
        UC039((UC-039 Transporte alternativo parceiro))
        UC085((UC-085 Votar em enquete))
        UC087((UC-087 Acionar contato de transporte parceiro))
        UC089((UC-089 Compartilhar perfil de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    U --- UC038 & UC089
    V --- UC039 & UC087
    VA --- UC085
    TP --- UC039 & UC087
    U -.->|especializa| V

    %% Relações Include / Extend
    UC038 -.->|include| UC085
    UC087 -.->|extend| UC039
```

---

## 10. Hipótese administrativa — equipamentos culturais e atrações
> [!WARNING]
> Os diagramas 10 a 13 modelam **hipóteses verificáveis**. O núcleo de cadastro administrativo (RF-042, RF-044, RF-046 a RF-048, RF-050 e RF-051) já integra a entrega atual; os demais casos do Épico 8 (RF-049 e RF-052 a RF-058) e a totalidade dos Épicos 11 a 13 permanecem fora dela. Em todos os casos, os fluxos e telas administrativas ainda dependem de validação com os futuros stakeholders administrativos.

```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])

    subgraph CC [Cariri Cultural — equipamentos e atrações]
        direction TB
        UC042((UC-042 Cadastrar equipamento cultural))
        UC043((UC-043 Editar equipamento cultural))
        UC044((UC-044 Consultar equipamento cultural))
        UC045((UC-045 Associar administrador a equipamento))
        UC046((UC-046 Autenticar administrador))
        UC047((UC-047 Cadastrar atração))
        UC048((UC-048 Editar atração))
        UC049((UC-049 Remover atração))
        UC050((UC-050 Consultar atrações cadastradas))

        %% Nós convidados: extensões vindas dos diagramas 6 e 9
        UC088((UC-088 Sinalizar e acompanhar<br/>dado incorreto))
        UC089((UC-089 Compartilhar perfil<br/>de local ou evento))
    end

    %% Relações Ator -> Caso de Uso
    APL --- UC042 & UC043 & UC045
    AEC --- UC046 & UC047 & UC048 & UC049
    V --- UC044 & UC050
    U --- UC088 & UC089
    U -.->|especializa| V

    %% Relações Include
    UC042 -.->|include| UC046
    UC043 -.->|include| UC046
    UC045 -.->|include| UC046
    UC047 -.->|include| UC046
    UC048 -.->|include| UC046
    UC049 -.->|include| UC046

    %% Relações Extend
    UC088 -.->|extend| UC044 & UC050
    UC089 -.->|extend| UC044 & UC050
```

---

## 11. Hipótese administrativa — estabelecimentos, ofertas e publicações
```mermaid
flowchart LR
    %% Atores
    APL([Administrador da plataforma])
    AEC([Administrador de equipamento cultural])
    AEG([Administrador de estabelecimento gastronômico])

    subgraph CC [Cariri Cultural — estabelecimentos e conteúdos]
        direction TB
        UC046((UC-046 Autenticar administrador))
        UC051((UC-051 Cadastrar estabelecimento gastronômico))
        UC052((UC-052 Cadastrar oferta))
        UC053((UC-053 Editar oferta))
        UC054((UC-054 Remover oferta))
        UC055((UC-055 Cadastrar publicação))
        UC056((UC-056 Criar publicação vinculada a local))
        UC057((UC-057 Editar publicação))
        UC058((UC-058 Remover publicação))
    end

    %% Relações Ator -> Caso de Uso
    APL --- UC051 & UC055
    AEG --- UC052 & UC053 & UC054 & UC056 & UC057 & UC058
    AEC --- UC056 & UC057 & UC058

    %% Relações Include
    UC051 -.->|include| UC046
    UC052 -.->|include| UC046
    UC053 -.->|include| UC046
    UC054 -.->|include| UC046
    UC055 -.->|include| UC046
    UC056 -.->|include| UC046
    UC057 -.->|include| UC046
    UC058 -.->|include| UC046
```

> UC-046 é o mesmo caso do diagrama 10; aparece nos dois recortes porque é incluído por ações de escrita de ambos.

---

## 12. Gestão de estabelecimentos — painel e indicadores
```mermaid
flowchart LR
    %% Atores
    G([Gestor])

    subgraph CC [Cariri Cultural — painel do Gestor]
        direction TB
        UC064((UC-064 Painel de métricas do estabelecimento))
        UC065((UC-065 Feed de atividades recentes))
        UC066((UC-066 Responder publicamente a avaliação))
        UC067((UC-067 Visualizar página pública))
        UC068((UC-068 Indicadores de desempenho))
        UC069((UC-069 Mapa de origem dos visitantes))
    end

    %% Relações Ator -> Caso de Uso
    G --- UC064 & UC065 & UC066 & UC067 & UC068 & UC069

    %% Relações Extend
    UC067 -.->|extend| UC064
```

---

## 13. Perfil, sessão e navegação global
```mermaid
flowchart LR
    %% Atores
    V([Visitante])
    U([Usuário Autenticado])
    G([Gestor])

    subgraph CC [Cariri Cultural — perfil e navegação]
        direction TB
        UC070((UC-070 Alternar modos Explorador e Gestor))
        UC071((UC-071 Nível de parceria na plataforma))
        UC072((UC-072 Certificações e qualificações))
        UC073((UC-073 Encerrar sessões ativas))
        UC074((UC-074 Barra inferior do Explorador))
        UC075((UC-075 Barra inferior do Gestor))
        UC076((UC-076 Cabeçalho contextual da tela))
    end

    %% Relações Ator -> Caso de Uso
    G --- UC070 & UC071 & UC072 & UC075
    U --- UC073
    V --- UC074 & UC076
    U -.->|especializa| V
```

---
