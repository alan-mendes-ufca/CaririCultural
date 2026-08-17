# Formulário de Observação — Avaliação de Usabilidade

**Projeto:** Cariri Cultural
**Método:** Entrevista com Think Aloud
**Dispositivo utilizado:** Celular / Smartphone
**Sessão:** 02

| Campo | Preenchimento |
| --- | --- |
| Participante | Kamily Rocha Cavalcante |
| Data | 15 / 08 / 2026 |
| Avaliador | Alan Mendes Vieira |
| Local da sessão | Residência do participante |

---

## 1. Observações gerais da sessão

| Aspecto observado | Anotações |
| --- | --- |
| A participante entendeu a proposta do sistema? | **Sim.** |
| A participante compreendeu as instruções do teste? | **Sim.** Executou todas as tarefas propostas sem pedir reformulação. |
| Houve interrupções ou dificuldades externas? | **Sim, duas.** (1) Lentidão de resposta do protótipo causada pelo *tunelamento (ngrok)* e internet do dispositivo móvel utilizado, o que confundia o participante gerando dúvida sobre o desempenho do sistema. (2) Algumas telas não estavam implementadas, o que gerava dúvidas por parte do participante. |

---

## 2. Registro das tarefas

| Tarefa | Concluiu? | Dificuldades observadas |
| --- | --- | --- |
| **Criar conta e consultar o perfil do usuário** (T-001) | **Sim** | O perfil abriu, mas **sem exibir as informações da conta recém-criada** — o avaliador atribuiu a limitação ao estágio do protótipo. |
| **Buscar uma atração ou local no Cariri Cultural** (T-002) | **Sim** | Não utilizou a caixa de pesquisa, apenas rolou a tela para verificar os locais estão mapeados. **A descoberta ocorreu por rolagem, não por busca.** |
| **Visualizar detalhes de um local** (T-002) | **Sim** | Percorreu a ficha com autonomia e leu horário, preço, acessibilidade, segurança, regras e avaliações. |
| **Usar filtros ou categorias de busca** (T-002) | **Não realizada** | Os filtros e critérios de ordenação da aba Explorar **não foram exercitados nesta sessão** — nem por iniciativa da participante, nem por solicitação do avaliador. A navegação se deu por rolagem da listagem padrão. | — |
| **Interagir com o assistente conversacional** (T-004) | **Parcial** | A pergunta livre formulada por iniciativa própria (sobre clima) não foi respondida. As perguntas sugeridas — única via funcional do assistente — **passaram despercebidas**, e a participante identificou a causa com precisão: estão em cinza, na mesma cor do campo de digitação. Após ser apontada a existência delas, selecionou uma e obteve resposta considerada satisfatória. |
| **Salvar, favoritar ou planejar uma visita** (T-003)| **Sim, mas gerou dúvidas** | Concluiu destino, data e confirmação sem obstáculo operacional. **A finalidade do checklist não foi autoexplicativa** — perguntou diretamente ao avaliador o que aquela seção significava. Tentou adicionar um item próprio; o botão não estava implementado. Em seguida, navegou pela lista de visitas planejadas e usou a exclusão. |
| **Consultar Avaliações** (T-005) | **Sim** | A consulta ocorreu sem qualquer dificuldade: acessou "ver mais avaliações" diretamente, sem hesitação, e identificou sozinha nota, mídias da comunidade, textos, curtida e compartilhamento. |

---

## 3. Problemas identificados

| Problema observado | Onde ocorreu | Impacto para o usuário | Gravidade |
| --- | --- | --- | --- |
| Perguntas sugeridas do assistente têm contraste insuficiente e são confundidas com o campo de digitação | Assistente conversacional | Bloqueia o acesso ao **único caminho funcional** do assistente; a usuária vai direto ao campo de texto, falha, e não descobre que havia alternativa. Problema de baixo custo de correção e alto impacto | **Alta** |
| Perfil não exibe as informações da conta criada | Tela de perfil | A usuária não obtém confirmação de que o sistema a reconhece. **Convergente com a sessão 01**, onde o mesmo efeito foi observado | **Alta** |
| Assistente não responde a perguntas livres | Assistente conversacional | A intenção espontânea do usuário — a que ele realmente traz — é a que falha; a resposta útil só vem por caminho pré-definido | **Alta** |
| Finalidade do checklist de visita não é autoexplicativa | Tela de planejamento de visita | Exigiu intervenção do avaliador para ser compreendida. **Convergente com a sessão 01**, onde o mesmo componente foi lido como lista de proibições | **Média** |
| Ausência de regras e restrições explícitas do local | Ficha do local | A participante levantou espontaneamente o risco de se deslocar e ser barrada por desconhecer uma restrição. **Convergente com a sessão 01**, cujo participante buscou exatamente essa informação no checklist | **Média** |
| Descoberta de locais depende de rolagem, não de busca | Caixa de pesquisa / listagem | A busca não sustentou a descoberta; a usuária só chegou ao local desejado percorrendo a listagem por orientação do avaliador. **Convergente com a sessão 01**, onde a busca por um local conhecido não retornou resultado | **Média** |
| Conteúdo histórico-cultural inacessível justamente quando a curiosidade foi acionada | Ficha do local, seção de história | A participante formulou a intenção de aprofundar e foi interrompida; é o momento de maior engajamento da jornada e o que mais diferencia o produto | **Média** *(a confirmar com a tela implementada)* |
| Impossibilidade de adicionar item próprio ao checklist | Tela de planejamento de visita | A usuária formulou a intenção por conta própria; a personalização é esperada, não opcional | **Média** *(a confirmar com a tela implementada)* |
| Lentidão de carregamento no início da sessão | Login / Home | Percepção de instabilidade logo no primeiro contato | **Baixa** *(atribuível à infraestrutura do protótipo)* |

---

## 4. Comportamentos observados

| Comportamento | Observação |
| --- | --- |
| Comentou algo positivo espontaneamente | Volume alto de manifestações positivas. Sobre o assistente: "achei bem legal e inovador". Sobre a completude: "o aplicativo em si está completo, porque ele tem basicamente tudo que uma pessoa procura". Sobre o conteúdo comunitário: "direito de fala". Sobre a interface: autoexplicativa, simplificada, cores aprovadas, tema escuro elogiado ("isso é bem bom"). |
| Comentou algo negativo espontaneamente | Praticamente uma única crítica, repetida em três momentos distintos da sessão: o contraste insuficiente das perguntas sugeridas do assistente. A lentidão inicial foi mencionada pelo avaliador, não pela participante. |

---

## 5. Síntese da avaliação

| Item | Anotações |
| --- | --- |
| **Principais facilidades percebidas** | A leitura da ficha do local foi o ponto mais forte da sessão: a participante percorreu horário, preço, acessibilidade, segurança e regras com autonomia total e classificou o conjunto como suficiente para decidir — "sobre a tabela de preço lá, tinha dizendo que era gratuito, tava dizendo sobre o horário, que é o que mais interessa". O acesso às avaliações foi imediato e sem hesitação. O planejamento de visita, a edição e a exclusão foram concluídos sem obstáculo operacional. O assistente, apesar de falhar na pergunta livre, foi eleito a funcionalidade preferida — sinal de que a proposta de valor conversacional é reconhecida mesmo em estado incompleto. |
| **Principais dificuldades percebidas** | Uma dificuldade dominante e duas secundárias. **Dominante:** as perguntas sugeridas do assistente não são percebidas por falta de contraste, o que anula na prática a única via funcional daquele recurso. **Secundárias:** a finalidade do checklist de visita não se comunica sozinha, e a descoberta de locais dependeu de rolagem porque a busca não retornou o que se procurava. Registre-se ainda uma lacuna de conteúdo levantada pela própria participante: a ficha não explicita restrições do local. |
| **Sugestões de melhoria levantadas** | **Pela participante:** alterar a cor das perguntas sugeridas do assistente, adotando o tom do botão de enviar, para diferenciá-las do campo de digitação — sugestão apresentada com justificativa comportamental própria, de que o usuário vai direto ao campo de texto por automatismo; e incluir na ficha do local as **restrições e proibições** aplicáveis, para evitar deslocamento em vão. **Decorrentes da observação:** tornar o checklist autoexplicativo sem depender de mediação; permitir inclusão de itens próprios; e reforçar a busca como caminho de descoberta, já que a rolagem só funcionou por orientação externa. |
| **Conclusão do avaliador** | Sessão de leitura predominantemente positiva, com fluxo principal percorrido do início ao fim e proposta de valor plenamente compreendida. Problemas que podem ser corrigidos para a versão final do protótipo: categorias de busca e checklist de sugestões não autoexplicativos |

---
## Referência 
https://drive.google.com/file/d/1bT5YYgH4QbyHK-7OOIXDuc7WWQObSuex/view?usp=drive_link
