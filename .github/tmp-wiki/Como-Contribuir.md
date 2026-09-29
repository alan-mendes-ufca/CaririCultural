# Como Contribuir

## Fluxo de trabalho

1. **Escolha uma issue** da milestone atual no [Roadmap](Roadmap) e atribua-a a você.
2. **Crie uma branch** a partir de `main`: `feat/<numero>-descricao-curta` (ex.: `feat/12-busca-locais`) ou `fix/…`, `docs/…`, `chore/…`.
3. **Faça commits pequenos** seguindo [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `feat: adiciona filtro por cidade`, `fix: corrige status aberto/fechado em feriados`, `docs(wiki): atualiza RNF-POR-004`.
4. **Abra um Pull Request** citando a issue (`Closes #12`) e preencha o [template de pull request](#template-de-pull-request).
5. **Revisão**: pelo menos uma aprovação da equipe e CI verde antes do merge.

## Template de pull request

Todo PR é aberto com o template [`.github/pull_request_template.md`](https://github.com/alan-mendes-ufca/CaririCultural/blob/main/.github/pull_request_template.md). **Antes de fechar uma issue**, responda três perguntas, em uma ou duas frases cada:

1. **Como funciona?**
2. **Por que assim e não de outra forma?**
3. **O que acontece quando falha?**

Por que essa redação:
- A pergunta 2 traz "e não de outra forma" de propósito: ela obriga a nomear uma **alternativa descartada**. Sem isso, o "por quê" vira justificativa vazia.
- A pergunta 3 testa se você conhece os **limites da solução**, e não só o caminho feliz.

Exemplo (armazenamento do token, issue #48):
1. **Como:** o token é salvo após o login e lido pelo Repository em cada requisição.
2. **Por que assim:** DataStore com criptografia via Keystore, em vez de SharedPreferences em texto puro, porque é um token de administrador.
3. **Quando falha:** se o token expirar, a API devolve 401, o Repository limpa o token e a navegação volta ao login.

> [!IMPORTANT]
> As respostas são do **autor do PR, com as próprias palavras**. Se uma resposta exigir abrir a IA, essa é a lacuna de estudo daquela fatia. Agentes de IA não respondem essas perguntas; a regra está no [`CLAUDE.md`](https://github.com/alan-mendes-ufca/CaririCultural/blob/main/CLAUDE.md) do repositório.

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
