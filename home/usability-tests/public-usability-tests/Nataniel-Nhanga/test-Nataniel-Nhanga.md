# Formulário de Observação — Avaliação de Usabilidade

**Projeto:** Cariri Cultural
**Método:** Entrevista com Think Aloud
**Dispositivo utilizado:** Celular / Smartphone

| Campo | Preenchimento |
| --- | --- |
| Participante | Nataniel Nhanga |
| Data | 12 / 08 / 2026 |
| Avaliador | Alan Mendes Vieira |
| Local da sessão | UFCA |

---

## 1. Observações gerais da sessão

| Aspecto observado | Anotações |
| --- | --- |
| O participante entendeu a proposta do sistema? | **Sim.** |
| O participante compreendeu as instruções do teste? | **Sim**, executou todas as tarefas propostas sem pedir reformulação do enunciado. |
| Houve interrupções ou dificuldades externas? | **Sim, duas.** (1) Lentidão de resposta do protótipo causada pelo *tunelamento (ngrok)* e internet do dispositivo móvel utilizado, o que confundia o participante gerando dúvida sobre o desempenho do sistema. (2) Interrupção de terceiro no ambiente. |

---

## 2. Registro das tarefas

| Tarefa | Concluiu? | Dificuldades observadas |
| --- | --- | --- |
| **Fazer seu cadastro e consultar o perfil do usuário** (T-001) | **Sim** | Ao inspecionar, constatou que o tipo de explorador escolhido no cadastro não estava refletido no perfil. |
| **Buscar uma atração ou local no Cariri Cultural** (T-002) | **Sim** | Operou a busca sem dificuldade de interação, mas não encontrou o local que procurou espontaneamente (Arajara Park), por ausência de cadastro. |
| **Visualizar detalhes de um local** (T-002) | **Sim** | Nenhuma dificuldade de navegação. |
| **Usar filtros ou categorias de busca** (T-002) | **Parcial** | **Não descobriu os filtros e a ordenação por conta própria** — só os percebeu após indicação direta do avaliador. Interpretou incorretamente o rótulo do filtro "Público", associando-o a popularidade em vez de perfil de público-alvo. |
| **Interagir com o assistente conversacional** (T-004) | **Não** | A pergunta livre formulada espontaneamente ("quais seriam os locais de mais interesse, os mais procurados") não foi respondida. O fallback ofereceu apenas sugestões pré-definidas, sem encaminhar para a tela que já contém essa informação. A resposta obtida via sugestão pronta também ficou incompleta: citou as três cidades, mas não respondeu qual é a maior.
| **Salvar, favoritar ou planejar uma visita** (T-003) | **Sim, mas gerou dúvidas** | Concluiu o fluxo de planejamento e a confirmação. A dificuldade foi **semântica, não operacional**: leu os itens do checklist como proibições do local antes de compreender que eram sugestões de preparo. Também ficou em dúvida se aquilo encaminharia para um tela de pagamento. |
| **Consultar Avaliações** (T-005) | **Sim** | Localizou a seção de avaliações sem dificuldade e usou corretamente "ver mais avaliações". Marcou uma avaliação como útil por iniciativa própria. |

---

## 3. Problemas identificados

| Problema observado | Onde ocorreu | Impacto para o usuário | Gravidade |
| --- | --- | --- | --- |
| O tipo de explorador definido no cadastro não é refletido no perfil | Tela de perfil, após cadastro como "novo morador" | Quebra a promessa de personalização por perfil, que é premissa de toda a jornada; o usuário não confirma que o sistema o reconhece | **Alta** |
| O assistente não responde a pergunta cuja informação já existe em outra tela do próprio app | Assistente conversacional | Falha de roteamento, não de conteúdo: o usuário conclui que o sistema não sabe algo que ele mesmo descobre minutos depois na Home e na Comunidade | **Alta** |
| Fallback do assistente não oferece alternativa acionável | Assistente conversacional | O usuário se sente confinado às sugestões prontas e sem rota de saída para a busca ou para o catálogo | **Alta** |
| Busca sem resultado não oferece nenhum caminho de recuperação | Caixa de pesquisa | O usuário abandona a intenção silenciosamente; a plataforma perde o sinal mais valioso que existe — a evidência de um local que as pessoas procuram e não está cadastrado | **Alta** |
| Filtros e critérios de ordenação não são descobertos espontaneamente | Aba Explorar | O usuário percorre apenas o resultado padrão e não alcança os recortes que atenderiam sua intenção real | **Alta** |
| Rótulo do filtro "Público" é ambíguo | Aba Explorar | Interpretação invertida do filtro; o usuário aplica um recorte acreditando estar aplicando outro | **Média** |
| Voto em enquete é irreversível e não pede confirmação | Aba Comunidade | Voto acidental sem possibilidade de correção; contamina o dado da enquete e reduz a confiança do usuário em interagir | **Média** |
| Semântica ambígua entre regras do local e itens sugeridos no checklist | Tela de planejamento de visita | O usuário lê sugestões como restrições e pode desistir de comportamentos permitidos, ou ignorar regras reais por não distingui-las | **Média** |
| Imagens geradas por IA reduzem a credibilidade percebida do local | Tela de detalhes do local | O polimento visual excessivo gera suspeita de conteúdo não autêntico justamente onde o produto precisa transmitir confiança | **Média** |
| Dado cadastral incoerente no campo de localização | Tela de detalhes do local | Compromete a leitura da ficha e reforça a percepção de informação não confiável — exatamente a dor que o produto se propõe a resolver | **Média** |
| Seção "Pouco Explorados" fica abaixo da dobra na Home e ausente da aba Explorar | Home / Explorar | O diferencial de descoberta de locais pouco divulgados fica com baixa visibilidade | **Média** |
| Volume de avaliações abaixo da expectativa criada pelo botão "ver mais avaliações" | Tela de avaliações do local | Expectativa frustrada; o rótulo promete mais do que entrega | **Baixa** |
| Sobreposição de elemento na tela de perfil | Tela de perfil | Hesitação momentânea na navegação | **Baixa** |

---

## 4. Comportamentos observados

| Comportamento | Observação |
| --- | --- |
| Comentou algo positivo espontaneamente | Qualidade visual das imagens ("as imagens são muito boas, pô"); recência das avaliações como sinal de confiança; naturalidade das respostas do assistente ("ele dá respostas bem automáticas, é legal isso"); compreensão imediata da camada comunitária ("uau"); e reconhecimento da lógica de preços/gratuidade ("a trilha do Horto é gratuita, né?"). |
| Comentou algo negativo espontaneamente | Lentidão percebida ("achei demorado abrir, algum travou um pouquinho"); desconfiança gerada pelas imagens profissionais demais; ambiguidade do rótulo "Público"; dado de localização incoerente; e falta de realismo de um item do checklist. |

---

## 5. Síntese da avaliação

| Item | Anotações |
| --- | --- |
| **Principais facilidades percebidas** | A proposta de valor do produto foi compreendida sem necessidade de explicação, incluindo a camada comunitária e a lógica de consultar avaliações antes de decidir. A navegação entre Home, Explorar, Comunidade e ficha do local foi fluida. A consulta a avaliações, a marcação de conteúdo útil e a conclusão do checklist de planejamento ocorreram sem obstáculo operacional. A **recência** das avaliações funcionou como sinal forte e imediato de confiança e atualidade — foi o elemento que mais gerou reação positiva espontânea na sessão. |
| **Principais dificuldades percebidas** | Três frentes. **(1) Personalização não entregue:** o perfil escolhido no cadastro não se reflete no sistema. **(2) Descoberta invisível:** filtros e ordenação não são encontrados sem ajuda, e um dos rótulos é interpretado ao contrário. **(3) Becos sem saída:** tanto a busca vazia quanto a falha do assistente terminam sem alternativa acionável, sendo que no caso do assistente a informação pedida já existe em outra tela do aplicativo. Somam-se a isso ambiguidades de leitura no checklist de visita e sinais de confiabilidade comprometidos por conteúdo de placeholder e por imagens que pareceram autênticas demais para o contexto retratado. |
| **Sugestões de melhoria levantadas** | Levantadas **pelo participante**: renomear o filtro "Público" para algo mais específico; rever a irreversibilidade do voto em enquete; ponderar itens de checklist pouco realistas diante do uso real (mapa offline versus Google Maps). Decorrentes **da observação**: transformar a busca sem resultado em ponto de captura de demanda, permitindo sinalizar a ausência de um local; dar ao assistente rota de saída para as telas que já contêm a informação solicitada; elevar a visibilidade de filtros e ordenação; separar visualmente regras do local de itens sugeridos no checklist; e exibir procedência da mídia nas fichas de local. |
| **Conclusão do avaliador** | O protótipo sustenta a compreensão da proposta de valor e o fluxo principal de descoberta → avaliação → planejamento foi percorrido do início ao fim. As falhas concentram-se em **descoberta e entendimento de recursos**. |

---

## Referência
https://drive.google.com/file/d/1H445DZvLMO6wNQNFy2qeyJMMKhmELjh6/view?usp=drive_link
