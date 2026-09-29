- Os diagramas seguem a notação de **Diagrama de Casos de Uso (UML)** utilizando **PlantUML**, que oferece suporte nativo a atores, casos de uso, fronteira do sistema e relações `<<include>>` e `<<extend>>`.
- **Atenção:** A autenticação de usuário comum é **pré-condição** de uso da plataforma, não um caso de uso (por isso não há nó de autenticação genérico nestes diagramas); o único caso de autenticação modelado é UC-038 (administrador), nos diagramas 8 e 9.
- **Atores e relações** reproduzem os campos "Ator principal", "Atores secundários", "Tipo de relação" e "Pontos de extensão" da especificação descritiva. Convenções adotadas:
  - `<<include>>`: seta tracejada do caso **base** para o caso **incluído**.
  - `<<extend>>`: seta tracejada do caso **extensor** para o caso **base**.
  - Atores secundários recebem associação, do mesmo modo que o ator principal.
  - **Usuário autenticado** é modelado como especialização de **Visitante** (generalização de ator), pois herda todos os casos de acesso público e acrescenta os que exigem sessão válida.
  - Casos exclusivamente incluídos e nunca iniciados diretamente pelo ator (UC-069, UC-071, UC-075) não recebem associação de ator: são alcançados a partir do caso base.

---

## 1. Visão geral por épico e ator
![Diagrama de casos de uso — 01-visao-geral](assets/user-cases/Cariri-Cultural-UCs/01-visao-geral.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

' Atores
actor "Visitante" as V
actor "Usuário autenticado" as UA
actor "Votante anônimo" as VA
actor "Gestor" as G
actor "Administrador autorizado\nem curadoria" as ADM
actor "Responsável pelo local" as RESP
actor "Administrador da plataforma" as APL
actor "Administrador de equipamento cultural" as AEC
actor "Administrador de estabelecimento gastronômico" as AEG

' Generalização de ator
V <|-- UA

' Fronteira do Sistema
rectangle "Sistema Cariri Cultural" {
    package "Descoberta e busca" as C1
    package "Perfil do local" as C2
    package "Agenda comunidade e avaliações" as C3
    package "Assistente virtual" as C4
    package "Área pessoal e roteiros" as C5
    package "Social enquetes e compartilhamento" as C6
    package "Gestão administrativa — hipótese" as C7
}

' Relações Ator -> Agrupamento
V -- C1
V -- C2
V -- C3
V -- C4
V -- C6
V -- C7
UA -- C3
UA -- C5
UA -- C6
VA -- C6
ADM -- C3
RESP -- C3
G -- C7
APL -- C7
AEC -- C7
AEG -- C7
@enduml
```

</details>

> Visão de contexto: os elementos internos são **pacotes** de casos de uso, não casos de uso individuais. O detalhamento está nos diagramas 2 a 11.

---

## 2. Descoberta e busca
![Diagrama de casos de uso — 02-descoberta-e-busca](assets/user-cases/Cariri-Cultural-UCs/02-descoberta-e-busca.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Visitante" as V
actor "Serviço de Geolocalização" as GEO

' Fronteira
rectangle "Cariri Cultural" {
    usecase "UC-001\nConsultar catálogo regional" as UC001
    usecase "UC-002\nConsultar locais em alta visitação" as UC002
    usecase "UC-003\nConsultar locais pouco divulgados" as UC003
    usecase "UC-004\nPesquisar locais e eventos por termo" as UC004
    usecase "UC-005\nFiltrar locais e eventos\npor categoria e público" as UC005
    usecase "UC-069\nValidar parâmetros de busca" as UC069
    usecase "UC-070\nBuscar por proximidade" as UC070
}

' Relações Ator -> Caso de Uso
V -- UC001
V -- UC002
V -- UC003
V -- UC004
V -- UC005
V -- UC070
GEO -- UC070

' Relações Include / Extend
UC004 ..> UC069 : <<include>>
UC005 ..> UC069 : <<include>>

UC002 ..> UC001 : <<extend>>
UC003 ..> UC001 : <<extend>>

UC070 ..> UC004 : <<extend>>
UC070 ..> UC005 : <<extend>>
@enduml
```

</details>

---

## 3. Perfil do local
![Diagrama de casos de uso — 03-perfil-do-local](assets/user-cases/Cariri-Cultural-UCs/03-perfil-do-local.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction
skinparam usecase {
    BackgroundColor<<fora de escopo>> #F4F4F4
    BorderColor<<fora de escopo>> #9E9E9E
    FontColor<<fora de escopo>> #6B6B6B
    BackgroundColor<<detalhado em outro diagrama>> #EEF3FB
    BorderColor<<detalhado em outro diagrama>> #6B8DB5
    FontColor<<detalhado em outro diagrama>> #33495E
}

' Atores
actor "Visitante" as V
actor "Serviço de Mapas e Transportes" as MAP

' Fronteira
rectangle "Cariri Cultural — perfil do local" {
    usecase "UC-006\nConsultar perfil do local\nambiente funcionamento custos\nregras segurança e público" as UC006
    usecase "UC-007\nConsultar localização acesso\ne opções de transporte" as UC007
    usecase "UC-009\nConsultar calendário e\nprogramação de eventos" as UC009
    usecase "UC-010\nAcessar canais de contato\ne redes sociais" as UC010
    usecase "UC-071\nConsultar procedência do dado\ne abrir canal externo" as UC071
    usecase "UC-008\nConsultar condições de higiene" as UC008 <<fora de escopo>>

    ' Nós convidados: extensões vindas dos diagramas 4 e 7
    usecase "UC-072\nFiltrar agenda por data e\nocultar itens encerrados" as UC072 <<detalhado em outro diagrama>>
    usecase "UC-080\nSinalizar e acompanhar\ndado incorreto" as UC080 <<detalhado em outro diagrama>>
    usecase "UC-033\nCompartilhar perfil\nde local ou evento" as UC033 <<detalhado em outro diagrama>>
}

' Relações Ator -> Caso de Uso
V -- UC006
V -- UC007
V -- UC009
V -- UC010
MAP -- UC007

' Relações Include
UC006 ..> UC071 : <<include>>
UC007 ..> UC071 : <<include>>
UC009 ..> UC071 : <<include>>
UC010 ..> UC071 : <<include>>

' Relações Extend vindas de fora do recorte
UC072 ..> UC009 : <<extend>>
UC080 ..> UC006 : <<extend>>
UC080 ..> UC007 : <<extend>>
UC080 ..> UC009 : <<extend>>
UC080 ..> UC010 : <<extend>>
UC033 ..> UC006 : <<extend>>
UC033 ..> UC007 : <<extend>>
UC033 ..> UC009 : <<extend>>
UC033 ..> UC010 : <<extend>>
@enduml
```

</details>

> Os antigos diagramas 3, 4 e 5 foram unificados aqui: a consolidação do Épico 2 reduziu o perfil do local a quatro casos principais (UC-006, UC-007, UC-009 e UC-010), e manter três recortes passou a repetir os mesmos nós.
> UC-008 aparece destacado por estar fora do escopo desta entrega; não recebe include nem extend enquanto essa decisão valer.
> UC-009 reaparece no diagrama 4, onde seu ciclo de vida é controlado por UC-072. UC-072, UC-080 e UC-033 são nós convidados, detalhados nos diagramas 4 e 7; permanecem dentro da fronteira do sistema porque são casos de uso do próprio Cariri Cultural, e aparecem aqui apenas como origem das relações `<<extend>>`. O ator principal de UC-080 e UC-033 é o usuário autenticado, associado a eles nos diagramas de origem.

---

## 4. Agenda, comunidade e avaliações
![Diagrama de casos de uso — 04-agenda-comunidade-avaliacoes](assets/user-cases/Cariri-Cultural-UCs/04-agenda-comunidade-avaliacoes.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Visitante" as V
actor "Usuário autenticado" as UA
actor "Administrador autorizado\nem curadoria" as ADM
actor "Responsável pelo local" as RESP

' Generalização de ator
V <|-- UA

' Fronteira
rectangle "Cariri Cultural" {
    usecase "UC-009\nConsultar calendário e programação de eventos" as UC009
    usecase "UC-012\nConsultar avaliações da comunidade" as UC012
    usecase "UC-013\nPublicar avaliação" as UC013
    usecase "UC-031\nConsultar mídias publicadas pela comunidade" as UC031
    usecase "UC-051\nMarcar avaliação como útil" as UC051
    usecase "UC-052\nCompartilhar avaliação individual" as UC052
    usecase "UC-053\nIniciar tópico de discussão na comunidade" as UC053
    usecase "UC-072\nFiltrar agenda por data\ne ocultar itens encerrados" as UC072
    usecase "UC-073\nRetomar rascunho após autenticação" as UC073
    usecase "UC-080\nSinalizar e acompanhar dado incorreto" as UC080
}

' Relações Ator -> Caso de Uso
V -- UC009
V -- UC012
V -- UC031
V -- UC072
UA -- UC013
UA -- UC031
UA -- UC051
UA -- UC052
UA -- UC053
UA -- UC073
UA -- UC080
ADM -- UC080
RESP -- UC080

' Relações Extend
UC051 ..> UC012 : <<extend>>
UC052 ..> UC012 : <<extend>>
UC031 ..> UC012 : <<extend>>
UC072 ..> UC009 : <<extend>>
UC073 ..> UC013 : <<extend>>
UC073 ..> UC080 : <<extend>>
@enduml
```

</details>

> Em UC-031 o visitante é o ator principal (consulta das mídias) e o usuário autenticado participa como ator secundário, ao publicar uma nova mídia.

---

## 5. Assistente virtual
![Diagrama de casos de uso — 05-assistente-virtual](assets/user-cases/Cariri-Cultural-UCs/05-assistente-virtual.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Visitante" as V
actor "Serviço de Transcrição de Áudio" as AUD
actor "Fonte de dados externa" as FONTE

' Fronteira
rectangle "Cariri Cultural" {
    usecase "UC-021\nConsultar o assistente virtual" as UC021
    usecase "UC-022\nReceber resposta interpretada por intenção" as UC022
    usecase "UC-023\nReceber orientação alternativa do assistente" as UC023
    usecase "UC-024\nAcionar o assistente com contexto da tela" as UC024
    usecase "UC-025\nConsultar dados atualizados por fonte externa" as UC025
    usecase "UC-026\nReceber links de redes sociais pelo assistente" as UC026
    usecase "UC-027\nReceber imagens do local pelo assistente" as UC027
    usecase "UC-028\nEnviar pergunta por áudio ao assistente" as UC028
}

' Relações Ator -> Caso de Uso
V -- UC021
V -- UC022
V -- UC023
V -- UC024
V -- UC025
V -- UC026
V -- UC027
V -- UC028
AUD -- UC028
FONTE -- UC025

' Relações Extend
UC022 ..> UC021 : <<extend>>
UC023 ..> UC021 : <<extend>>
UC024 ..> UC021 : <<extend>>
UC026 ..> UC021 : <<extend>>
UC027 ..> UC021 : <<extend>>
UC028 ..> UC021 : <<extend>>
@enduml
```

</details>

> UC-025 é o único caso deste recorte sem campo "Tipo de relação" na especificação descritiva; por isso aparece sem `<<extend>>` de UC-021, diferentemente dos demais casos do épico.

---

## 6. Área pessoal: recomendações, roteiros, listas e gamificação
![Diagrama de casos de uso — 06-area-pessoal](assets/user-cases/Cariri-Cultural-UCs/06-area-pessoal.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Usuário autenticado" as UA
actor "Serviço de Mapas e Transportes" as MAP

' Fronteira
rectangle "Cariri Cultural" {
    usecase "UC-014\nReceber recomendações por interesse demonstrado" as UC014
    usecase "UC-015\nReceber recomendações por avaliações realizadas" as UC015
    usecase "UC-016\nReceber recomendações por perfis similares" as UC016
    usecase "UC-017\nGerar roteiro personalizado" as UC017
    usecase "UC-018\nGerenciar listas de locais desejados" as UC018
    usecase "UC-019\nRegistrar locais visitados\nhistórico pessoal" as UC019
    usecase "UC-020\nUsar checklist de atividades e passeios" as UC020
    usecase "UC-032\nCompartilhar lista pessoal por link público" as UC032
    usecase "UC-054\nConsultar conquistas e distintivos" as UC054
    usecase "UC-055\nConsultar dicas contextuais no checklist" as UC055
    usecase "UC-074\nReceber alternativa quando a\npersonalização é insuficiente" as UC074
    usecase "UC-075\nSalvar e ajustar roteiro pessoal" as UC075
    usecase "UC-076\nAlertar item de checklist\nvinculado a atração inativa" as UC076
    usecase "UC-078\nRevogar link público de lista" as UC078
}

' Relações Ator -> Caso de Uso
UA -- UC014
UA -- UC015
UA -- UC016
UA -- UC017
UA -- UC018
UA -- UC019
UA -- UC020
UA -- UC032
UA -- UC054
UA -- UC055
UA -- UC074
UA -- UC076
UA -- UC078
MAP -- UC017

' Relações Include
UC017 ..> UC075 : <<include>>

' Relações Extend
UC074 ..> UC014 : <<extend>>
UC074 ..> UC015 : <<extend>>
UC074 ..> UC016 : <<extend>>
UC076 ..> UC020 : <<extend>>
UC055 ..> UC020 : <<extend>>
UC078 ..> UC032 : <<extend>>
@enduml
```

</details>

> Todos os casos do Épico 5 exigem sessão válida: o ator é o usuário autenticado, não o visitante. UC-075 não recebe associação de ator por ser alcançado exclusivamente pela inclusão a partir de UC-017.

---

## 7. Social, enquetes, transporte e compartilhamento
![Diagrama de casos de uso — 07-social-enquetes-transporte](assets/user-cases/Cariri-Cultural-UCs/07-social-enquetes-transporte.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Visitante" as V
actor "Usuário autenticado" as UA
actor "Votante anônimo" as VA
actor "Serviço/operador de transporte parceiro" as TP

' Generalização de ator
V <|-- UA

' Fronteira
rectangle "Cariri Cultural" {
    usecase "UC-029\nCriar e compartilhar enquete" as UC029
    usecase "UC-030\nConsultar transporte alternativo parceiro" as UC030
    usecase "UC-077\nVotar em enquete sob as\nregras de ciclo de vida" as UC077
    usecase "UC-079\nAcionar contato de transporte parceiro" as UC079
    usecase "UC-033\nCompartilhar perfil de local ou evento" as UC033
}

' Relações Ator -> Caso de Uso
V -- UC030
V -- UC079
UA -- UC029
UA -- UC033
UA -- UC077
VA -- UC077
TP -- UC030
TP -- UC079

' Relações Include / Extend
UC029 ..> UC077 : <<include>>
UC079 ..> UC030 : <<extend>>
@enduml
```

</details>

> Em UC-077 o votante anônimo é o ator principal; o criador da enquete (usuário autenticado) participa como ator secundário, nas regras de alteração de opções e de encerramento.

---

## 8. Hipótese administrativa — equipamentos culturais e atrações
> [!WARNING]
> Os diagramas 8 a 11 modelam **hipóteses verificáveis**. O núcleo de cadastro administrativo (UC-034, UC-036, UC-038 a UC-040, UC-042 e UC-043) já integra a entrega atual; os demais casos do Épico 8 (UC-041 e UC-044 a UC-050) e a totalidade dos Épicos 11 a 13 permanecem fora dela. Em todos os casos, os fluxos e telas administrativas ainda dependem de validação com os futuros stakeholders administrativos.

![Diagrama de casos de uso — 08-admin-equipamentos-atracoes](assets/user-cases/Cariri-Cultural-UCs/08-admin-equipamentos-atracoes.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction
skinparam usecase {
    BackgroundColor<<detalhado em outro diagrama>> #EEF3FB
    BorderColor<<detalhado em outro diagrama>> #6B8DB5
    FontColor<<detalhado em outro diagrama>> #33495E
}

' Atores
actor "Visitante" as V
actor "Administrador da plataforma" as APL
actor "Administrador de equipamento cultural" as AEC

rectangle "Cariri Cultural — equipamentos e atrações" {
    usecase "UC-034\nCadastrar equipamento cultural" as UC034
    usecase "UC-035\nEditar equipamento cultural" as UC035
    usecase "UC-036\nConsultar equipamento cultural" as UC036
    usecase "UC-037\nAssociar administrador a equipamento cultural" as UC037
    usecase "UC-038\nAutenticar administrador" as UC038
    usecase "UC-039\nCadastrar atração" as UC039
    usecase "UC-040\nEditar atração" as UC040
    usecase "UC-041\nRemover atração" as UC041
    usecase "UC-042\nConsultar atrações cadastradas" as UC042

    ' Nós convidados: extensões vindas dos diagramas 4 e 7
    usecase "UC-080\nSinalizar e acompanhar\ndado incorreto" as UC080 <<detalhado em outro diagrama>>
    usecase "UC-033\nCompartilhar perfil\nde local ou evento" as UC033 <<detalhado em outro diagrama>>
}

' Relações Ator -> Caso de Uso
APL -- UC034
APL -- UC035
APL -- UC037
APL -- UC038
AEC -- UC037
AEC -- UC038
AEC -- UC039
AEC -- UC040
AEC -- UC041
V -- UC036
V -- UC042

' Relações Include
UC034 ..> UC038 : <<include>>
UC035 ..> UC038 : <<include>>
UC037 ..> UC038 : <<include>>
UC039 ..> UC038 : <<include>>
UC040 ..> UC038 : <<include>>
UC041 ..> UC038 : <<include>>

' Relações Extend
UC080 ..> UC036 : <<extend>>
UC080 ..> UC042 : <<extend>>
UC033 ..> UC036 : <<extend>>
UC033 ..> UC042 : <<extend>>
@enduml
```

</details>

> UC-036 e UC-042 são consultas públicas: não incluem UC-038, pois o acesso à informação não exige autenticação (RN-022).
> Em UC-037, o administrador de equipamento cultural é ator secundário. Em UC-038, o administrador da plataforma é ator secundário — o fluxo de autenticação é o mesmo para qualquer perfil administrativo.

---

## 9. Hipótese administrativa — estabelecimentos, ofertas e publicações
![Diagrama de casos de uso — 09-admin-estabelecimentos-publicacoes](assets/user-cases/Cariri-Cultural-UCs/09-admin-estabelecimentos-publicacoes.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Administrador da plataforma" as APL
actor "Administrador de equipamento cultural" as AEC
actor "Administrador de estabelecimento gastronômico" as AEG

rectangle "Cariri Cultural — estabelecimentos e conteúdos" {
    usecase "UC-038\nAutenticar administrador" as UC038
    usecase "UC-043\nCadastrar estabelecimento gastronômico" as UC043
    usecase "UC-044\nCadastrar oferta" as UC044
    usecase "UC-045\nEditar oferta" as UC045
    usecase "UC-046\nRemover oferta" as UC046
    usecase "UC-047\nCadastrar publicação" as UC047
    usecase "UC-048\nCriar publicação vinculada a local" as UC048
    usecase "UC-049\nEditar publicação" as UC049
    usecase "UC-050\nRemover publicação" as UC050
}

' Relações Ator -> Caso de Uso
APL -- UC043
APL -- UC047
APL -- UC038
AEC -- UC038
AEG -- UC038
AEG -- UC044
AEG -- UC045
AEG -- UC046
AEG -- UC048
AEG -- UC049
AEG -- UC050
AEC -- UC048
AEC -- UC049
AEC -- UC050

' Relações Include
UC043 ..> UC038 : <<include>>
UC044 ..> UC038 : <<include>>
UC045 ..> UC038 : <<include>>
UC046 ..> UC038 : <<include>>
UC047 ..> UC038 : <<include>>
UC048 ..> UC038 : <<include>>
UC049 ..> UC038 : <<include>>
UC050 ..> UC038 : <<include>>
@enduml
```

</details>

> UC-038 é o mesmo caso do diagrama 8; aparece nos dois recortes porque é incluído por ações de escrita de ambos. Seu ator principal é o administrador de equipamento cultural; o administrador da plataforma e o administrador de estabelecimento gastronômico participam como atores secundários do mesmo fluxo.

---

## 10. Gestão de estabelecimentos — painel e indicadores
![Diagrama de casos de uso — 10-painel-do-gestor](assets/user-cases/Cariri-Cultural-UCs/10-painel-do-gestor.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Gestor" as G

rectangle "Cariri Cultural — painel do Gestor" {
    usecase "UC-056\nConsultar painel de métricas do estabelecimento" as UC056
    usecase "UC-057\nAcompanhar feed de atividades recentes" as UC057
    usecase "UC-058\nResponder publicamente a uma avaliação" as UC058
    usecase "UC-059\nVisualizar a página pública como visitante" as UC059
    usecase "UC-060\nConsultar indicadores de desempenho" as UC060
    usecase "UC-061\nConsultar mapa de origem dos visitantes" as UC061
}

' Relações Ator -> Caso de Uso
G -- UC056
G -- UC057
G -- UC058
G -- UC059
G -- UC060
G -- UC061

' Relações Extend
UC059 ..> UC056 : <<extend>>
@enduml
```

</details>

---

## 11. Perfil, sessão e navegação global
![Diagrama de casos de uso — 11-perfil-sessao-navegacao](assets/user-cases/Cariri-Cultural-UCs/11-perfil-sessao-navegacao.svg)

<details>
<summary>Código-fonte PlantUML</summary>

```plantuml
@startuml
left to right direction

' Atores
actor "Visitante" as V
actor "Usuário autenticado" as UA
actor "Gestor" as G

' Generalização de ator
V <|-- UA

rectangle "Cariri Cultural — perfil e navegação" {
    usecase "UC-062\nAlternar entre os modos Explorador e Gestor" as UC062
    usecase "UC-063\nConsultar nível de parceria na plataforma" as UC063
    usecase "UC-064\nConsultar certificações e qualificações" as UC064
    usecase "UC-065\nEncerrar todas as sessões ativas" as UC065
    usecase "UC-066\nNavegar pela barra inferior do Explorador" as UC066
    usecase "UC-067\nNavegar pela barra inferior do Gestor" as UC067
    usecase "UC-068\nConsultar cabeçalho contextual da tela" as UC068
}

' Relações Ator -> Caso de Uso
G -- UC062
G -- UC063
G -- UC064
G -- UC067
V -- UC066
V -- UC068
UA -- UC065
@enduml
```

</details>

---
