---
title: "Mapa de Jornada do Usuário — Cariri Cultural"
project: "Cariri Cultural"
artifact: "Mapa de Jornada do Usuário"
version: "1.1"
date: "2026-07-26"
status: "Proposto para validação"
---

# Mapa de Jornada do Usuário — Cariri Cultural

| Controle do artefato | Informação |
| --- | --- |
| Projeto | Cariri Cultural |
| Produto | Plataforma web/mobile com catálogo regional e assistente conversacional |
| Versão | 1.1 |
| Data | 26 de julho de 2026 |
| Estado do sistema | Fase de requisitos, com protótipos e sem implementação funcional |
| Tipo de jornada | Jornada futura projetada (*to-be*), fundamentada nas dores da experiência atual (*as-is*) |
| Escopo | Experiência pública e pessoal do visitante, da descoberta ao pós-visita |

---

## 1. Objetivo e recorte

Este mapa descreve a experiência desejada de uma pessoa que quer descobrir e viver uma experiência turística, cultural, gastronômica ou de lazer no Cariri usando o **Cariri Cultural**. Ele evidencia objetivos, ações, necessidades, pontos de dor, emoções, oportunidades de melhoria e momentos críticos ao longo da jornada.

A versão 1.1 também confronta a jornada com o **protótipo de alto nível**. Uma interação visível no protótipo indica que ela foi representada no design, mas não comprova implementação, validação com usuários ou aprovação como requisito.

A jornada principal usa como lente **Lucas**, novo morador, estudante e trabalhador, cauteloso na tomada de decisão e habituado ao smartphone. Ele quer conhecer a região, mas encontra informações fragmentadas, incompletas ou desatualizadas. A síntese também contempla os outros perfis diretos registrados no Modelo Onion e nos artefatos de UX:

- **Turista/visitante:** tem pouco tempo e precisa montar um roteiro confiável.
- **Novo morador:** quer referências, autonomia e pertencimento cultural.
- **Morador curioso/de longa data:** quer sair da rotina e descobrir experiências menos óbvias.
- **Pessoa que planeja para família ou grupo:** prioriza segurança, orçamento, adequação infantil, conforto e consenso.

> **Cenário:** em um momento de folga, Lucas decide conhecer um lugar diferente no Cariri. Ele acessa a plataforma, explora opções, avalia informações, planeja a visita, desloca-se, vive a experiência e depois registra ou compartilha sua percepção.

## 2. Evidências que fundamentam o mapa

A síntese foi construída pela triangulação dos artefatos do repositório:

| Evidência | Contribuição para a jornada |
| --- | --- |
| 12 entrevistas e relatório consolidado | Revelam fontes atuais, critérios de decisão, desistências, frustrações, barreiras de deslocamento e expectativas. |
| Survey com 29 respondentes e 10 gráficos | Quantifica o problema: 62,1% já desistiram de uma visita por falta de informação; 93,1% têm forte interesse na plataforma; localização/rota, horário e preço lideram as informações pré-visita. |
| Personas PATHY e CHATHY | Evidenciam uso prioritário de celular, preferência por interfaces simples, informação visual e direta, cautela, privacidade e necessidade de suporte conversacional confiável. |
| Storytelling e storyboards | Estruturam os gatilhos e arcos dos três perfis: desejo de novidade, frustração com fontes dispersas, descoberta da plataforma e experiência satisfatória. |
| HTA, BPMN e Diagrama de Casos de Uso | Detalham tarefas de explorar, buscar, consultar, planejar, usar o assistente e organizar. A cobertura do Diagrama de Casos de Uso é parcial em algumas etapas e não abrange o pós-visita atual. |
| Requisitos funcionais, não funcionais, regras de negócio e priorizações | Definem capacidades, dados mínimos, desempenho, acessibilidade, transparência, confiabilidade e condições de exceção. |
| Matriz de rastreabilidade e dependências | Conectam necessidades e tarefas às histórias, requisitos e fontes de origem. |
| Benchmarking de cinco soluções | Reforça catálogo centralizado, mobilidade, contextualização cultural, roteiros e interface conversacional; destaca lacunas que o Cariri Cultural pode preencher. |
| Modelo Onion | Confirma os perfis diretos e o ecossistema de stakeholders que mantém e se beneficia da informação. |
| Protótipo de alto nível — 17 telas e respectivos arquivos HTML | Materializa a navegação do explorador e do gestor, busca, filtros, detalhes, assistente, planejamento, comunidade, avaliações e perfil; também evidencia lacunas entre a jornada desejada e a interface representada. |
| Demais protótipos, diagramas e relatório acadêmico | Consolidam o posicionamento mobile/web, os pontos de contato e o escopo atual do projeto. |

### 2.1. Confronto com o protótipo de alto nível

| Etapa | Evidência visível no protótipo | Ajuste ou lacuna relevante para a jornada |
| --- | --- | --- |
| 1. Gatilho | Home com categorias, “Mais Visitados”, “Pouco Explorados” e “Eventos em Destaque”. | Confirma descoberta por inspiração; entradas por ocasião — “hoje”, “gratuito”, “com crianças” — ainda não estão claras na Home. |
| 2. Acesso | Navegação inferior persistente: Home, Explorar, Assistente, Comunidade e Perfil. | Confirma arquitetura mobile; exploração pública sem login, onboarding, permissões e acessibilidade ainda precisam ser demonstrados. |
| 3. Exploração | Busca com sugestões, histórico recente, autocompletar e estado vazio; Explorar com filtros de categoria, público e preço, ordenação por popularidade e cartões com nota, distância e tags. | Confirma recuperação de busca vazia e sinais rápidos de decisão; cidade, data, filtros ativos, critérios de ordenação e uso consentido do histórico precisam ficar explícitos. |
| 4. Avaliação | Detalhes com status “aberto agora”, horário, preço, acessibilidade, segurança, história/cultura, mapa externo, regras antes da visita, avaliações e botão “Planejar visita”. | Confirma a estrutura central de decisão; fonte, data de atualização, estados de verificação e fundamento de atributos como “segurança alta” não aparecem. |
| 5. Planejamento | Tela de checklist com destino, data, participantes, progresso e inclusão de itens. | Confirma o checklist e a passagem “Planejar visita”; custos, transporte, sequência de roteiro, alternativas e preservação antes do login não estão demonstrados. |
| 6. Experiência | Página do local, acesso ao Google Maps, conteúdo cultural e assistente com resposta contextual e cartão de local. | Confirma continuidade parcial entre conteúdo, mapa e assistente; modo leve/offline, atualização de última hora, fallback e canal “informação não confere” não aparecem. |
| 7. Pós-visita | Avaliações, feed/comunidade, enquetes, conquistas, perfil por tipo de explorador e histórico de lugares visitados. | Confirma retorno comunitário e histórico; envio/moderação, consentimento, privacidade e retorno sobre correções precisam ser explicitados. |

**Leitura de escopo:** as telas de gestor demonstram cadastro em etapas, edição de local, eventos, avaliações pendentes e métricas. Neste mapa do visitante, elas são evidência indireta de manutenção do catálogo e resposta da organização, não novos passos da jornada principal.

## 3. Legenda

- **Emoção:** escala de `-2` (muito negativa) a `+2` (muito positiva).
- **MC:** momento crítico — ponto com forte influência sobre continuidade, confiança ou satisfação.
- **Dor atual:** problema observado nas fontes usadas hoje, como Instagram, Google Maps, buscas e indicações.
- **Risco na solução:** falha que ainda pode ocorrer no Cariri Cultural e deve ser evitada no projeto.
- **Representado no protótipo:** interação desenhada em uma tela de alto nível; não equivale a funcionalidade implementada ou requisito aprovado.

## 4. Visão geral da jornada

| Etapa | 1. Gatilho | 2. Acesso e descoberta | 3. Exploração e busca | 4. Avaliação e decisão | 5. Planejamento | 6. Deslocamento e experiência | 7. Pós-visita |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Objetivo** | Encontrar algo interessante para fazer. | Entender rapidamente o valor da plataforma. | Obter opções relevantes para o contexto. | Escolher com confiança e alinhar expectativa. | Transformar a escolha em um plano viável. | Chegar sem imprevistos e viver o esperado. | Registrar, contribuir e descobrir o próximo passeio. |
| **Ações** | Define ocasião, companhia, tempo e orçamento. | Abre a interface; reconhece a Home e a navegação principal. | Busca; usa sugestões ou histórico; filtra por categoria, público e preço; ordena e abre um cartão. | Confere status, horário, preço, acessibilidade, segurança, regras, história, mapa e avaliações; aciona “Planejar visita”. | Confirma destino, data e participantes; acompanha e edita o checklist; complementa rota, transporte e custos. | Reconfere status e rota; consulta conteúdo cultural ou o assistente; adapta o plano se necessário. | Registra a visita; avalia; publica mídia; consulta histórico, comunidade e novas sugestões. |
| **Pontos de contato** | Conversa com família/amigos; redes sociais; rotina local. | Home e navegação Home/Explorar/Assistente/Comunidade/Perfil. | Busca inteligente, Explorar, filtros, ordenação, cartões e assistente. | Detalhes do local, “Planejar visita”, mapa externo e avaliações da comunidade. | Checklist de passeio, listas/roteiros e canais de rota/transporte. | Página do local, Google Maps e assistente contextual. | Avaliações, Comunidade, Perfil e Lugares Visitados. |
| **Necessidades** | Inspiração relevante e alternativas além do óbvio. | Acesso rápido, sem cadastro obrigatório para consultar; interface simples e mobile. | Resposta rápida; filtros por cidade, preço, categoria e público; opções populares e pouco divulgadas. | Informação completa, atualizada, verificável e comparável. | Viabilidade de horário, distância, orçamento, segurança, acessibilidade e transporte. | Atualização em tempo útil, orientação e conteúdo cultural contextual. | Baixo esforço, controle de privacidade e percepção de que a contribuição tem valor. |
| **Pontos de dor/riscos** | Repetição dos mesmos lugares; dependência de boca a boca e algoritmo. | Instalação pesada, proposta confusa, lentidão ou exigência precoce de login. | Informação excessiva, resultados irrelevantes, filtros pobres ou busca sem saída. | Preço/horário ausente; foto antiga; avaliação enganosa; expectativa diferente da realidade. | Transporte caro/escasso, incompatibilidade de horários, roteiro inviável ou custos ocultos. | Local fechado, acesso difícil, regra desconhecida, falta de sinal ou divergência entre cadastro e realidade. | Login interrompe o envio; moderação opaca; receio de exposição; ausência de retorno sobre correções. |
| **Pensamento provável** | “Quero fazer algo diferente, mas não sei o quê.” | “Isso vai resolver mais rápido que procurar em vários lugares?” | “Há algo que combine comigo, perto e dentro do orçamento?” | “Posso confiar que é assim mesmo?” | “Consigo chegar, pagar e aproveitar sem surpresa?” | “As informações bateram com a realidade?” | “Vale ajudar outras pessoas e usar de novo?” |
| **Emoção** | `0` — expectativa moderada | `+1` — curiosidade | `+1` — interesse, podendo cair a `-1` se não encontrar | `-1 → +1` — ansiedade transformada em confiança | `+1` — controle, com risco de `-1` pela mobilidade | `+2` se a promessa for cumprida; `-2` se houver divergência | `+1` — satisfação e pertencimento |
| **Oportunidade central** | Completar a Home com entradas por ocasião, preservando “Mais Visitados”, “Pouco Explorados” e eventos. | Validar a navegação principal e permitir exploração pública. | Tornar filtros/ordenação explicáveis e preservar o estado vazio útil do protótipo. | Acrescentar fonte, data, verificação e fundamento dos atributos à página já prototipada. | Evoluir o checklist para um plano realista com rota, horários, custos, alternativas e contatos. | Acrescentar atualização contextual, modo leve e canal simples para sinalizar divergência. | Tornar avaliação, histórico, comunidade e reconhecimento transparentes e controláveis. |
| **Criticidade** | Média | **Alta — MC1** | **Alta — MC2** | **Muito alta — MC3** | **Muito alta — MC4** | **Muito alta — MC5** | **Alta — MC6** |

### Curva emocional

```text
Emoção
 +2 |                                      ●
 +1 |        ●────────●────────●────●──────╯────●
  0 | ●──────╯
 -1 |                    ╲ risco na decisão/planejamento
 -2 |                                      ╲ divergência grave
     1.Gatilho  2.Acesso  3.Busca  4.Decisão  5.Plano  6.Visita  7.Pós
```

A maior amplitude emocional está entre **decidir** e **vivenciar**: a confiança criada pelos dados da plataforma é testada contra a realidade. Esse é o “momento da verdade” do serviço.

## 5. Detalhamento por etapa

### Etapa 1 — Gatilho: desejo de sair da rotina

**Contexto.** Surge tempo livre, visita de familiares, convite de amigos ou vontade de conhecer melhor a cultura regional.

**Objetivos**

- Descobrir algo novo e adequado à ocasião.
- Evitar repetir sempre as mesmas atrações.
- Considerar companhia, tempo disponível, orçamento e interesse cultural.

**Ações**

- Conversa com amigos ou familiares.
- Recorda lugares já conhecidos.
- Consulta rapidamente redes sociais ou uma indicação.

**Necessidades**

- Inspiração contextual: “hoje”, “perto de mim”, “com crianças”, “à noite” ou “gratuito”.
- Visibilidade para espaços, eventos e iniciativas independentes.
- Valor cultural além de uma lista comercial.

**Pontos de dor**

- As mesmas indicações aparecem repetidamente.
- Eventos menores permanecem invisíveis.
- A descoberta nas redes depende do algoritmo e conteúdos vistos podem desaparecer.

**Emoção:** `0` — vontade e curiosidade, acompanhadas de indecisão.

**Oportunidades**

- Entrada por ocasião e intenção, sem exigir que o usuário já saiba o nome do local.
- Destaques equilibrados entre popularidade, novidade e baixa divulgação.
- Calendário com antecedência, preço/entrada, horário e cidade.

### Etapa 2 — Acesso e descoberta do Cariri Cultural

**Contexto.** Lucas chega à plataforma por indicação, busca, QR code, campanha regional, hotel/pousada, aeroporto, universidade ou equipamento cultural.

**Objetivos**

- Entender se a solução oferece informação melhor e mais rápida.
- Começar a explorar sem barreiras.

**Ações**

- Abre o site/PWA/app.
- Reconhece a Home e a navegação persistente entre Home, Explorar, Assistente, Comunidade e Perfil.
- Usa a busca principal, uma categoria ou um destaque como primeiro caminho.
- Permite ou recusa localização.

**Necessidades**

- Linguagem direta, imagens claras e poucos passos.
- Consulta pública sem autenticação.
- Compatibilidade com celulares Android mais antigos, 3G/4G e diferentes tamanhos de tela.
- Acessibilidade de nível WCAG 2.1 AA.

**Pontos de dor e riscos**

- Cadastro obrigatório antes de perceber valor.
- Tela inicial pesada ou confusa.
- Permissão de localização sem justificativa.
- Falta de contraste, textos pequenos ou navegação inacessível.

**Emoção:** `+1` — curiosidade e esperança.

**MC1 — Primeiro valor percebido.** Se a pessoa não compreender a proposta ou não conseguir começar rapidamente, retorna às fontes já conhecidas.

**Oportunidades**

- Preservar na Home os acessos já representados a busca, categorias, “Mais Visitados”, “Pouco Explorados” e “Eventos em Destaque”.
- Acrescentar entradas por ocasião, como “hoje”, “perto de você”, “com crianças” e “gratuito”.
- Validar se os cinco destinos da navegação inferior são compreendidos sem onboarding.
- Explicar permissões e permitir uso manual por cidade.
- Carregar catálogo/listas em até 2 s em 4G.

### Etapa 3 — Exploração e busca

**Contexto.** O usuário ainda pode estar apenas se inspirando ou já ter um objetivo específico.

**Objetivos**

- Encontrar opções relevantes sem pesquisar em várias plataformas.
- Refinar por cidade, categoria, preço, público, data e tipo de experiência.

**Ações**

- Explora mais visitados, pouco explorados, eventos e resultados ordenados por popularidade.
- Pesquisa palavras-chave, usa sugestões, histórico recente ou autocompletar.
- Aplica filtros de categoria, público e preço.
- Interpreta nota, distância e tags dos cartões.
- Pergunta ao assistente: “o que acontece hoje?”, “o que há perto?” ou “como chegar?”.

**Necessidades**

- Busca compreensível, rápida e tolerante a termos incompletos.
- Filtros visíveis, combináveis e fáceis de limpar.
- Controle e explicação sobre buscas recentes e sugestões personalizadas.
- Resultado explicável e sem confundir conteúdo patrocinado com recomendação orgânica.
- Alternativas quando não houver correspondência exata.

**Pontos de dor e riscos**

- Rolagem longa e excesso de resultados.
- Pouca diversidade ou reforço apenas de atrações já famosas.
- Busca vazia sem próxima ação.
- Resposta do chatbot genérica, lenta ou apresentada como certeza sem base.

**Emoção:** `+1` quando há progresso; cai a `-1` quando a busca não ajuda.

**MC2 — Relevância e recuperação de falhas.** Uma busca sem resultado não pode ser um beco sem saída.

**Oportunidades**

- Retornar pesquisa em até 1,5 s e permitir ao novo usuário concluí-la em menos de 30 s.
- Exibir filtros ativos, critério da ordenação e motivo resumido da recomendação.
- Preservar o estado vazio representado no protótipo e ampliá-lo com correção, categoria próxima, outra cidade/data ou consulta ao assistente.
- Solicitar consentimento ou oferecer controle claro para armazenar buscas recentes.
- No chatbot, priorizar o catálogo e assumir limitações quando o dado for ausente, desatualizado ou conflitante.

### Etapa 4 — Avaliação e decisão

**Contexto.** O usuário abre duas ou mais opções e tenta reduzir a incerteza antes de se deslocar.

**Objetivos**

- Confirmar se o local atende interesse, orçamento, companhia e restrições.
- Formar uma expectativa realista.

**Ações**

- Verifica descrição e tipo de experiência.
- Analisa fotos reais e atuais.
- Confere horário e status aberto/fechado.
- Consulta preço, cardápio, taxas, couvert e formato de atendimento.
- Avalia localização, acesso, transporte, segurança, higiene, acessibilidade, adequação infantil, regras e contato.
- Lê avaliações recentes e relevantes.
- Consulta contexto histórico e cultural.
- Usa “Planejar visita” para levar a escolha ao checklist.

**Necessidades**

- Dados mínimos completos para cada tipo de local.
- Transparência sobre fonte, data de atualização e campos não verificados.
- Fotos representativas da condição atual.
- Avaliações com autoria, data, recência e contexto.
- Conteúdo patrocinado claramente identificado.

**Pontos de dor e riscos**

- Horários, preços e contatos desatualizados.
- Imagens promocionais que não representam a realidade.
- Regras importantes omitidas.
- Nota agregada sem avaliações suficientes.
- Segurança apresentada sem base verificável.

**Emoção:** inicia em `-1` (cautela) e sobe a `+1` quando as evidências são consistentes.

**MC3 — Confiança na informação.** É o principal momento crítico. Dados incompletos ou incorretos podem causar desistência antes da visita ou uma quebra grave de confiança depois dela.

**Oportunidades**

- Indicador de completude e selo “atualizado em”, acompanhado da origem.
- Destaque visual para horário de hoje, preço e rota.
- Estado explícito: “não informado”, “não aplicável”, “não verificado” ou “há divergência”.
- Explicar a origem de atributos sintetizados, especialmente “segurança”, que aparece no protótipo sem critério visível.
- **Hipótese futura:** comparação simples entre favoritos.
- Botão “tirar dúvida sobre este local” que abre o assistente já contextualizado.
- Preservar o botão “Planejar visita” como transição clara entre decisão e planejamento.

### Etapa 5 — Planejamento

**Contexto.** O destino foi escolhido, mas a visita precisa caber na agenda, no orçamento e nas condições de mobilidade.

**Objetivos**

- Organizar uma visita ou roteiro executável.
- Coordenar o grupo e reduzir imprevistos.

**Ações**

- Aciona “Planejar visita” na página do local.
- Confirma destino, data e participantes.
- Acompanha o progresso, marca itens e adiciona itens ao checklist.
- Gera ou ajusta roteiro quando necessário.
- Verifica distância, duração, horários, transporte e locais próximos.
- Abre rota ou contato.

**Necessidades**

- Sequência coerente com deslocamento e funcionamento real.
- Estimativa clara de custos conhecidos.
- Alternativas para transporte e para locais indisponíveis.
- Controle do usuário para reorganizar ou substituir etapas.
- Persistência segura de listas e roteiros.

**Pontos de dor e riscos**

- Transporte público escasso e corrida por aplicativo cara, sobretudo à noite.
- Roteiro sugere local fechado ou distante demais.
- Custos adicionais não aparecem antes da confirmação.
- Exigência de login faz perder o que já foi montado.
- O protótipo mostra checklist e participantes, mas ainda não demonstra custos, transporte, sequência do roteiro ou alternativas.

**Emoção:** `+1` — sensação de controle; pode cair a `-1` diante de barreiras de mobilidade.

**MC4 — Viabilidade do plano.** Uma boa recomendação que não considera horário, distância, adequação e transporte ainda resulta em desistência.

**Oportunidades**

- Gerar roteiro apenas com locais públicos que atendam aos dados mínimos.
- Manter a continuidade já representada entre “Planejar visita” e o checklist.
- Considerar distância, horário, status e público, como determinam as regras do projeto.
- Acrescentar ao planejamento um resumo de horário, custo, rota, transporte e restrições antes da saída.
- Preservar o planejamento ao solicitar autenticação.
- Informar contatos de transporte alternativo e opções próximas.
- **Hipótese futura:** permitir o compartilhamento de roteiros e apoiar o consenso do grupo.

### Etapa 6 — Deslocamento e experiência

**Contexto.** A promessa digital é confrontada com o acesso e a realidade física do local.

**Objetivos**

- Chegar com segurança e no horário.
- Confirmar que ambiente, preço, atendimento e programação correspondem ao planejado.
- Compreender a história e o significado cultural da experiência.

**Ações**

- Reconfere status e rota.
- Desloca-se ao local.
- Consulta regras, programação e conteúdo contextual.
- Abre a rota no Google Maps e usa o assistente para uma dúvida pontual ou uma recomendação contextual.
- Adapta o roteiro se houver imprevisto.

**Necessidades**

- Informação útil em conexão móvel instável.
- Informação de última hora claramente visível, sem pressupor notificações automáticas.
- Continuidade de contexto entre página, mapa e assistente.
- Alternativa quando serviço externo ou IA estiver indisponível.
- Conteúdo cultural curto, acessível e ligado ao lugar visitado.

**Pontos de dor e riscos**

- Chegar e encontrar o local fechado ou diferente das fotos.
- Descobrir no local uma taxa, formato de serviço ou regra não informada.
- Entrada sem sinalização ou acesso difícil.
- Perder conexão ou depender de serviço externo indisponível.

**Emoção:** `+2` quando realidade e promessa coincidem; `-2` quando divergem.

**MC5 — Momento da verdade.** A correspondência entre o cadastro e a experiência física determina confiança, satisfação e intenção de retorno.

**Oportunidades**

- **Hipótese futura:** avisos de alteração e horário especial, inclusive por notificações.
- Conteúdo essencial leve e disponível após carregamento inicial.
- Botão “informação não confere” com categorias rápidas e evidência opcional.
- Fallback do chatbot para busca convencional, contato e dados já disponíveis.
- Recomendar alternativa próxima quando o plano falhar.

### Etapa 7 — Pós-visita e relacionamento

**Contexto.** A experiência terminou; o usuário decide se contribuirá e se voltará à plataforma.

**Objetivos**

- Registrar o que viveu.
- Ajudar outras pessoas com informação real.
- Contribuir com a comunidade e receber novas sugestões.

**Ações**

- Conclui o checklist e encontra o local no histórico de lugares visitados.
- Atribui nota e comentário.
- Publica foto/vídeo, navega na Comunidade e participa de enquetes.
- Sinaliza dado incorreto quando esse canal for incorporado.
- Consulta conquistas e novas recomendações baseadas em preferências autorizadas.

**Necessidades**

- Formulário curto e feedback claro sobre publicação/moderação.
- Privacidade, autoria e controle de compartilhamento.
- Reconhecimento de que a correção foi recebida.
- Recomendações transparentes e opção de não usar o histórico.

**Pontos de dor e riscos**

- Fluxo longo após a visita.
- Sessão expira e apaga contribuição.
- Moderação parece arbitrária.
- Dúvida sobre exposição de dados e mídias.
- Correção enviada sem retorno.

**Emoção:** `+1` — satisfação, pertencimento e vontade de compartilhar.

**MC6 — Fechamento do ciclo de confiança.** A contribuição da comunidade sustenta a atualização e reduz a incerteza da próxima pessoa.

**Oportunidades**

- Avaliação progressiva: nota primeiro, detalhes opcionais depois.
- Salvar rascunho quando autenticação ou sessão interromper o envio.
- Mostrar estado da moderação e resultado da correção.
- Solicitar consentimento específico para histórico e recomendações.
- Explicar como lugares visitados e conquistas são registrados e permitir desativar esses registros.
- Conectar a experiência concluída a uma próxima descoberta cultural.

## 6. Momentos críticos consolidados

| ID | Momento crítico | Risco de experiência | Resposta de projeto | Prioridade |
| --- | --- | --- | --- | --- |
| MC1 | Primeiro valor percebido | Abandono por proposta confusa, lentidão ou login precoce. | Validar a Home e a navegação prototipadas; garantir exploração pública, responsividade e carregamento rápido. | Alta |
| MC2 | Busca e recuperação | Usuário não encontra nada e retorna às redes sociais. | Preservar sugestões, filtros e estado vazio do protótipo; acrescentar critérios claros e fallback pelo assistente. | Alta |
| MC3 | Confiança na informação | Desistência ou expectativa falsa causada por dados incompletos/desatualizados. | Completar a tela de detalhes prototipada com fonte/data, verificação, fotos reais, avaliações e fundamento dos atributos. | **Crítica** |
| MC4 | Viabilidade do plano | Boa opção torna-se impraticável por horário, distância, custo ou transporte. | Evoluir o checklist prototipado para um plano baseado em restrições reais, alternativas e contatos de mobilidade. | **Crítica** |
| MC5 | Correspondência com a realidade | Quebra de confiança quando local, preço, regra ou serviço divergem do divulgado. | Atualização visível, canal de inconsistência, fallback e alternativa próxima; alertas permanecem como hipótese futura. | **Crítica** |
| MC6 | Contribuição pós-visita | Perda de conhecimento recente e baixa recorrência. | Avaliação simples, moderação transparente, privacidade e retorno sobre correções. | Alta |

## 7. Oportunidades priorizadas

Notificações, comparação entre favoritos, compartilhamento de roteiros e alertas de última hora são **hipóteses futuras**, não requisitos confirmados. Quando citadas neste mapa, devem ser entendidas apenas como oportunidades sujeitas a validação e priorização.

### Prioridade P0 — indispensável para confiança e continuidade

1. **Página de decisão completa:** horário/status, preço/cardápio/taxas, localização/rota, segurança, acessibilidade, regras, formato de serviço, contato e fotos reais.
2. **Proveniência e atualidade:** fonte, data de atualização e estados explícitos para informação ausente, não verificada ou conflitante.
3. **Busca e filtros de baixa fricção:** cidade, categoria, preço, data, público e tipo de experiência, com recuperação de busca vazia.
4. **Experiência mobile, rápida e acessível:** consulta pública, responsividade, otimização para 3G/4G e WCAG 2.1 AA.
5. **Falhas recuperáveis:** catálogo indisponível, mapa externo ou IA não podem deixar o usuário sem orientação alternativa.

### Prioridade P1 — amplia valor e diferenciação

1. **Roteiros executáveis:** considerar distância, funcionamento, adequação, orçamento conhecido e alternativas.
2. **Assistente contextual e honesto:** responder a partir do catálogo/página atual e explicitar limitações.
3. **Camada comunitária confiável:** avaliações recentes, mídias reais, autoria, moderação e denúncia.
4. **Mobilidade regional:** rota, transporte, contatos alternativos e atenção especial à noite.
5. **Contextualização cultural:** história, identidade e significado durante a visita.
6. **Ciclo de correção:** permitir sinalizar divergência e informar ao usuário o andamento da validação.
7. **Continuidade entre telas:** manter contexto entre cartão, detalhes, “Planejar visita”, checklist, mapa e assistente.

### Prioridade P2 — engajamento e crescimento

1. Compartilhamento de listas com controle de privacidade; compartilhamento de roteiros apenas como hipótese futura.
2. Recomendações personalizadas explicáveis e baseadas em consentimento.
3. Enquetes para decisão em grupo.
4. Conquistas e reconhecimento não competitivo, com controle do usuário sobre histórico e exposição.

## 8. Indicadores de sucesso

| Dimensão | Indicador sugerido | Meta inicial |
| --- | --- | --- |
| Descoberta | Taxa de usuários que abrem ao menos um detalhe após iniciar exploração | Estabelecer linha de base em teste |
| Encontrabilidade | Novo usuário conclui uma busca | Menos de 30 s |
| Desempenho | Carregamento de catálogo/listas em 4G | P95 ≤ 2 s |
| Desempenho | Resposta da pesquisa | P95 ≤ 1,5 s |
| Decisão | Percentual de páginas publicadas com dados mínimos completos | ≥ 95% |
| Atualidade | Percentual de registros com fonte e data válidas | 100% |
| Confiança | Taxa de divergências confirmadas entre cadastro e realidade | Tendência decrescente |
| Planejamento | Roteiros gerados que são salvos ou iniciados | Estabelecer linha de base |
| Continuidade | Usuários que chegam ao checklist após acionar “Planejar visita” | Estabelecer linha de base em teste |
| Assistente | Primeira resposta | P95 ≤ 5 s |
| Recuperação | Falhas do assistente que oferecem busca/alternativa acionável | 100% |
| Experiência | Conclusão das tarefas críticas em teste de usabilidade | ≥ 90% |
| Satisfação | System Usability Scale (SUS) | ≥ 70 |
| Pós-visita | Taxa de avaliações/correções concluídas após início | Estabelecer linha de base |
| Acessibilidade | Conformidade da experiência crítica | WCAG 2.1 AA |

## 9. Rastreabilidade resumida

| Etapa | Principais requisitos e regras relacionados | Principais fontes de evidência |
| --- | --- | --- |
| 1. Gatilho | RF-001 a RF-003, RF-016, RN-006 a RN-008 | Entrevistas, survey, storytelling, storyboards e protótipo de alto nível |
| 2. Acesso | RN-022, RNF-USA-001, RNF-ACE-001, RNF-POR-002 a RNF-POR-004, RNF-DES-001 | PATHY, relatório, priorização de RNFs e protótipo de alto nível |
| 3. Exploração | RF-004 a RF-006, RF-030 a RF-033, RN-003 a RN-010, RN-054 a RN-057 | Survey, HTA, Diagrama de Casos de Uso e protótipo de alto nível |
| 4. Avaliação | RF-007 a RF-021, RN-011 a RN-032, RNF-DES-003 e RNF-DES-006 | Entrevistas, survey, Diagrama de Casos de Uso — cobertura parcial — e protótipo de alto nível |
| 5. Planejamento | RF-026, RF-027, RF-029, RF-039, RF-041, RN-043 a RN-053 | Entrevistas, PATHY, HTA, Diagrama de Casos de Uso — cobre roteiros e recomendações, mas não todos os requisitos citados — e protótipo de alto nível |
| 6. Experiência | RF-011, RF-016 a RF-018, RF-030 a RF-033, RN-021, RN-054 a RN-058, RNF-DIS-005 | Entrevistas, benchmarking, storytelling, storyboards e protótipo de alto nível |
| 7. Pós-visita | RF-021, RF-022, RF-028, RF-040, RF-041, RN-029 a RN-038, LGPD | Entrevistas, HTA e protótipo de alto nível |

**Limite de cobertura do Diagrama de Casos de Uso:** na etapa 4, a cobertura é parcial; na etapa 5, restringe-se a roteiro e recomendações e não sustenta todos os requisitos relacionados; na etapa 7, o diagrama atual não representa avaliações, histórico, mídia da comunidade ou compartilhamento e, por isso, não é citado como evidência.

## 10. Variações por perfil

| Perfil | Gatilho dominante | Critérios mais sensíveis | Risco principal | Ajuste recomendado |
| --- | --- | --- | --- | --- |
| Turista/visitante | Aproveitar bem poucos dias | Proximidade, tempo, rota, atração e autenticidade | Gastar tempo pesquisando ou deslocar-se para uma opção inadequada | Roteiro por duração, localização e disponibilidade |
| Novo morador | Entender a região e criar pertencimento | Segurança, acesso, contexto cultural e eventos | Depender de uma rede pessoal ainda pequena | Exploração guiada e conteúdo cultural contextual |
| Morador curioso | Sair da rotina | Novidade, preço, ambiente e programação | Repetição e baixa visibilidade de iniciativas locais | Destaque para pouco divulgados e agenda recorrente |
| Família/grupo | Organizar passeio seguro e consensual | Segurança, adequação infantil, regras, conforto e orçamento | Um detalhe omitido comprometer todo o grupo | Checklist e apoio à decisão; comparação como hipótese futura |
| Usuário reservado/mobile | Resolver sem exposição e em poucos passos | Simplicidade, desempenho, privacidade e imagens | Abandonar por cadastro, lentidão ou excesso de interação | Consulta pública, modo leve e consentimento granular |

## 11. Hipóteses a validar

Como o produto ainda não foi implementado, as oportunidades propostas devem ser validadas com usuários representativos:

1. A pessoa identifica a proposta de valor e abre um local em menos de 30 segundos?
2. Os filtros priorizados correspondem ao vocabulário usado por turistas e moradores?
3. Fonte, data de atualização e nível de verificação aumentam a confiança sem sobrecarregar a tela?
4. A página de detalhes responde às dúvidas decisivas sem exigir rolagem excessiva?
5. O roteiro é percebido como executável diante das limitações reais de transporte regional?
6. O fallback de busca/chatbot mantém a pessoa na jornada?
7. O envio pós-visita é curto o suficiente e transmite segurança sobre autoria, privacidade e moderação?
8. Pessoas com deficiência conseguem completar busca, decisão, planejamento e avaliação com tecnologias assistivas?
9. Notificações, comparação entre favoritos, compartilhamento de roteiros e alertas de última hora agregam valor sem aumentar complexidade, distração ou exposição de dados?
10. A navegação Home, Explorar, Assistente, Comunidade e Perfil corresponde ao modelo mental dos três perfis de explorador?
11. Nota, distância, tags e ordenação dão contexto suficiente para escolher um cartão sem induzir confiança excessiva?
12. O botão “Planejar visita” e o checklist formam uma continuidade compreensível e suficiente para uma visita real?

## 12. Fontes internas consultadas

- `home.md`
- `home/interviews/` — roteiros, 12 entrevistas e relatório consolidado
- `home/survey.md` e gráficos associados
- `home/pathy/`, `home/chathy/` e personas mantidas em `uploads/`
- `home/storytelling.md` e `home/storyboarding.md`
- `home/hta.md`
- `home/bpmn/`
- `home/functional-requirements.md` e `home/priorizated-fr.md`
- `home/non-functional-requirements.md` e `home/priorizated-nfr.md`
- `home/business-rules.md` e `home/priorizated-br.md`
- `home/user-storys.md`
- `home/traceability-matrix.md`
- `home/Dependência-de-RFs-e-RNFs/`
- `home/user-cases/Diagrama-Cariri-Cultural.png` — Diagrama de Casos de Uso
- `home/benchmarking/`
- `home/figma/orion-model-cariri-cultural.pdf`
- `home/reports/ES_ER_IHC_TrabalhoPratico1_Equipe06_Relatorio.pdf`
- `home/slides/`, `home/minute/` e protótipo de baixa fidelidade referenciado na wiki
- `/home/cjota/Documentos/prototipo_cariri_cultural/stitch_cariri_cultural_discovery_hub/` — protótipo de alto nível, com telas e HTML de Home, Explorar, busca, detalhes, assistente, checklist, avaliações, comunidade, perfil e fluxos do gestor

---

**Síntese de projeto:** o valor do Cariri Cultural não está apenas em reunir opções, mas em transformar **informação dispersa em confiança**, **confiança em um plano viável** e **o plano em uma experiência que corresponda à promessa**.
