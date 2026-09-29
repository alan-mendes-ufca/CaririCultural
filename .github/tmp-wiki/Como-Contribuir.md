# Como Contribuir

## Fluxo de trabalho

1. **Escolha uma issue** da milestone atual no [Roadmap](Roadmap) e atribua-a a você.
2. **Crie uma branch** a partir de `main`: `feat/<numero>-descricao-curta` (ex.: `feat/12-busca-locais`) ou `fix/…`, `docs/…`, `chore/…`.
3. **Faça commits pequenos** seguindo [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `feat: adiciona filtro por cidade`, `fix: corrige status aberto/fechado em feriados`, `docs(wiki): atualiza RNF-POR-004`.
4. **Abra um Pull Request** citando a issue (`Closes #12`) e preencha o [template de pull request](#template-de-pull-request).
5. **Revisão**: pelo menos uma aprovação da equipe e CI verde antes do merge.

## Template de pull request

Todo PR é aberto com o template [`.github/pull_request_template.md`](https://github.com/alan-mendes-ufca/CaririCultural/blob/main/.github/pull_request_template.md). **Antes de fechar uma issue**, a descrição do PR precisa responder três itens:

| Seção | O que escrever |
| --- | --- |
| **Decisão principal** | O que foi escolhido, a **alternativa descartada** e o critério que decidiu entre as duas. |
| **Modos de falha testados** | Como a mudança pode quebrar e como você verificou que não quebra (falha, como testou, resultado). |
| **Fora de escopo, de propósito** | O que ficou de fora por decisão e onde será tratado (outra issue, milestone futura ou "não será feito"). |

> [!IMPORTANT]
> As respostas são do **autor do PR, com as próprias palavras**. Este é um projeto acadêmico: além de entregar valor ao usuário, ele existe para quem desenvolve aprender a construir software de forma pensada. Um agente de IA pode ajudar a levantar alternativas, riscos e perguntas, mas **não escreve essas seções** nem toma a decisão. Essa regra também está no [`CLAUDE.md`](https://github.com/alan-mendes-ufca/CaririCultural/blob/main/CLAUDE.md) do repositório, lido pelos agentes.

Dicas:
- Se não houve alternativa real, diga por que a escolha era óbvia; isso também é uma decisão.
- Modos de falha incluem entradas inválidas, falta de conexão, permissões negadas, dados vazios e acessibilidade (TalkBack, fonte ampliada).
- "Fora de escopo" evita que o revisor espere algo que não foi feito e alimenta as próximas issues.

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
- **Via Git** (edições grandes, imagens e PDFs): clone `https://github.com/alan-mendes-ufca/CaririCultural.wiki.git`, edite e faça push. As páginas ficam organizadas em pastas por área (`01-Projeto/`, `02-Pesquisa/`, `03-Requisitos/`, …).

Convenções:
- O nome do arquivo é o nome da página (`Requisitos-Funcionais.md` → página *Requisitos Funcionais*). Nomes devem ser únicos, independentemente da pasta.
- Links entre páginas usam apenas o nome: `[Regras de Negócio](Regras-de-Neg%C3%B3cio#RN-001)`.
- Imagens e PDFs ficam na pasta `assets/` da wiki e são referenciados a partir da raiz: `![diagrama](assets/bpmn/BPMN-Cariri-Cultural.png)`.
- Novas páginas devem ser adicionadas ao menu em `_Sidebar.md`.

## Milestones e labels

Milestones e labels são declarados em `.github/project/milestones.json` e `.github/project/labels.json` e sincronizados pelo workflow `Sincronizar milestones e labels` (também pode ser executado manualmente na aba **Actions**).
