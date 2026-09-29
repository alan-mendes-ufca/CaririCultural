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

Toda a documentação do projeto fica **somente nesta wiki**; o repositório guarda apenas o código. Há duas formas de editar:

- **Pela interface**: botão **Edit** no topo de cada página, ou **New Page** para criar uma página.
- **Via Git** (edições grandes, imagens e PDFs): clone `https://github.com/alan-mendes-ufca/CaririCultural-wiki.wiki.git`, edite e faça push. As páginas ficam organizadas em pastas por área (`01-Projeto/`, `02-Pesquisa/`, `03-Requisitos/`, …).

Convenções:
- O nome do arquivo é o nome da página (`Requisitos-Funcionais.md` → página *Requisitos Funcionais*). Nomes devem ser únicos, independentemente da pasta.
- Links entre páginas usam apenas o nome: `[Regras de Negócio](Regras-de-Neg%C3%B3cio#RN-001)`.
- Imagens e PDFs ficam na pasta `assets/` da wiki e são referenciados a partir da raiz: `![diagrama](assets/bpmn/BPMN-Cariri-Cultural.png)`.
- Novas páginas devem ser adicionadas ao menu em `_Sidebar.md`.

## Milestones e labels

Milestones e labels são declarados em `.github/project/milestones.json` e `.github/project/labels.json` e sincronizados pelo workflow `Sincronizar milestones e labels` (também pode ser executado manualmente na aba **Actions**).
