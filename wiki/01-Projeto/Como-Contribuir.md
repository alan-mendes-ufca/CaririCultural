# Como Contribuir

## Fluxo de trabalho

1. **Escolha uma issue** da milestone atual no [Roadmap](Roadmap) e atribua-a a você.
2. **Crie uma branch** a partir de `main`: `feat/<numero>-descricao-curta` (ex.: `feat/12-busca-locais`) ou `fix/…`, `docs/…`, `chore/…`.
3. **Faça commits pequenos** seguindo [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `feat: adiciona filtro por cidade`, `fix: corrige status aberto/fechado em feriados`, `docs(wiki): atualiza RNF-POR-004`.
4. **Abra um Pull Request** citando a issue (`Closes #12`), com descrição do que mudou e evidências (prints, testes).
5. **Revisão**: pelo menos uma aprovação da equipe e CI verde antes do merge.

## Labels

| Label | Uso |
| --- | --- |
| `app` | Código do aplicativo Android |
| `backend` | API, banco de dados e serviços |
| `infra` | CI/CD, ferramentas, configuração do repositório |
| `ux` | Design, usabilidade e acessibilidade |
| `ia` | Assistente virtual |
| `documentation` | Wiki e documentação |
| `must-have` / `should-have` / `could-have` | Prioridade MoSCoW herdada dos requisitos |

## Editando esta wiki

A wiki é **gerada automaticamente** a partir da pasta [`wiki/`](https://github.com/alan-mendes-ufca/CaririCultural-wiki/tree/main/wiki) do repositório pelo workflow `Publicar Wiki`. Para alterar uma página:

1. Edite o arquivo `.md` correspondente em `wiki/` (pelo próprio GitHub ou por uma branch).
2. Abra um PR; ao ser mergeado em `main`, a wiki é atualizada.

> [!WARNING]
> Edições feitas diretamente pela interface da wiki são sobrescritas na próxima publicação.

Convenções:
- O nome do arquivo é o nome da página (`Requisitos-Funcionais.md` → página *Requisitos Funcionais*). Nomes devem ser únicos, independentemente da pasta.
- Links entre páginas usam apenas o nome: `[Regras de Negócio](Regras-de-Neg%C3%B3cio#RN-001)`.
- Imagens e PDFs ficam em `wiki/assets/` e são referenciados a partir da raiz: `![diagrama](assets/bpmn/BPMN-Cariri-Cultural.png)`.
- Novas páginas devem ser adicionadas ao menu em `wiki/_Sidebar.md`.

## Milestones e labels

Milestones e labels são declarados em `.github/project/milestones.json` e `.github/project/labels.json` e sincronizados pelo workflow `Sincronizar milestones e labels` (também pode ser executado manualmente na aba **Actions**).
