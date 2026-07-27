---
title: Service Blueprint - Cariri Cultural
---

# Service Blueprint - Cariri Cultural

## Objetivo e recorte

O Blueprint representa a prestação do serviço Cariri Cultural para turistas, novos moradores e moradores da região. O cenário começa quando a pessoa procura algo para fazer e termina quando registra a experiência, contribui com a comunidade ou inicia uma nova descoberta.

O serviço deve transformar informações turísticas e culturais dispersas em uma escolha confiável, um plano viável e uma experiência coerente com o que foi apresentado na plataforma.

## Blueprint da jornada principal

| Raia / etapa | 1. Descobrir | 2. Acessar e explorar | 3. Buscar e filtrar | 4. Avaliar e escolher | 5. Planejar | 6. Visitar e usar | 7. Contribuir e retornar |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Evidências e pontos de contato** | Redes sociais, indicação, cartaz, campanha ou QR code | Home, cabeçalho e navegação Início, Explorar, Assistente, Comunidade e Perfil | Busca, sugestões, histórico autorizado, filtros, ordenação, cartões e mapa | Detalhes do local, fotos, horários, preços, regras, acessibilidade, história, mapa e avaliações | Planejar visita, roteiro, listas, checklist, dicas, mapa e transporte | Página do local, rota, assistente contextual e sinalização de dado incorreto | Avaliações, comunidade, mídias, enquetes, discussões, conquistas, perfil e histórico |
| **Ações do usuário** | Define ocasião, companhia, tempo e orçamento | Abre a plataforma e explora categorias, destaques e eventos | Pesquisa, aplica filtros, usa sugestões e seleciona um resultado | Confere informações, compara expectativas e escolhe o local | Salva locais, ajusta o roteiro e acompanha o checklist | Reconfere horário e rota, consulta o assistente e adapta o plano | Registra a visita, avalia, compartilha, publica mídia ou discussão e acompanha correções |
| **Linha de interação** |  |  |  |  |  |  |  |
| **Frontstage: ações visíveis** | Exibe locais populares, pouco explorados, eventos e conteúdo patrocinado identificado | Permite consulta pública e mantém navegação, contexto e acessibilidade consistentes | Retorna resultados, mostra filtros e distância e oferece alternativas para busca sem resultado | Exibe informações completas, fonte, atualização e aviso quando um dado não estiver verificado | Apresenta roteiro viável, checklist, dicas e opções de deslocamento | Responde pelo assistente, informa limitações e oferece sinalização de informação incorreta | Confirma envio, informa publicação ou moderação e comunica o resultado de correções |
| **Linha de visibilidade** |  |  |  |  |  |  |  |
| **Backstage: ações invisíveis** | Equipe seleciona destaques e diferencia curadoria de promoção paga | Sistema verifica sessão, perfil, consentimento, dispositivo e permissões | Sistema valida taxonomia, executa busca, ordena, pagina e calcula proximidade autorizada | Curadoria e gestores verificam cadastro, fontes, status, horários, imagens e links | Sistema cruza interesses, horários, distância e adequação do público e preserva ajustes manuais | Assistente interpreta contexto, consulta a base e aciona fallback; curadoria recebe sinalizações | Sistema valida autoria; equipe modera conteúdo; gestor responde avaliações; curador encerra protocolos |
| **Linha de interação interna** |  |  |  |  |  |  |  |
| **Processos de apoio** | Curadoria editorial, divulgação regional e parcerias institucionais | Identidade, LGPD, segurança, acessibilidade, hospedagem e monitoramento | Banco de dados, índices de busca, geolocalização, cache, paginação e CDN | Governança do catálogo, fontes institucionais, armazenamento de mídia e integração com mapas | Motor de recomendação, roteirização, listas, checklists e persistência de preferências | Base de conhecimento, IA, transcrição de áudio, mapas, cache e observabilidade | Moderação, notificações, auditoria, métricas, backups e recuperação |
| **Responsáveis principais** | Equipe de conteúdo e comunicação | Equipe de produto, identidade e infraestrutura | Equipe técnica e responsável pelo catálogo | Curador, gestor do local e fontes institucionais | Sistema de recomendação e serviços de mapas | Equipe técnica, IA, mapas e curadoria | Usuário, moderação, gestor do local e curador |
| **Regras e controles essenciais** | Conteúdo patrocinado deve ser identificado | Consulta pública não exige autenticação; dados pessoais exigem consentimento | Localização só pode ser usada com autorização e deve haver alternativa manual | Dados sensíveis precisam de fonte e verificação; registros incompletos não devem ser publicados | Recomendações usam somente dados autorizados e locais elegíveis | Áudio deve ter tratamento transitório; falhas externas não podem bloquear os dados locais | Contribuições exigem autoria quando aplicável; votação em enquete pode ser anônima; conteúdo denunciado passa por revisão |
| **Pontos críticos** | Repetição dos mesmos locais ou influência indevida de publicidade | Login precoce, lentidão ou navegação confusa | Resultado irrelevante, filtro insuficiente ou busca sem saída | Informação antiga, incompleta ou diferente da realidade | Roteiro inviável por horário, distância, transporte ou custo | Local fechado, falta de sinal, rota indisponível ou IA sem resposta | Envio interrompido, moderação opaca, exposição de dados ou ausência de retorno |
| **Critério de qualidade** | Diversidade e transparência dos destaques | Catálogo carregado em até 2 segundos em conexão 4G | Pesquisa respondida em até 1,5 segundo e com alternativa acionável | Detalhes carregados em até 3 segundos e dados verificáveis | Plano compatível com restrições e ajustável pelo usuário | Primeira resposta do assistente em até 5 segundos e fallback disponível | Confirmação clara, privacidade, rastreabilidade e retorno da moderação ou correção |

## Respostas aos principais pontos de falha

| Falha | Resposta visível ao usuário | Tratamento interno |
| --- | --- | --- |
| Busca sem resultado | Informa a situação e sugere correção, categoria relacionada ou outra cidade | Reexecuta a consulta com alternativas válidas da taxonomia |
| Localização negada ou indisponível | Mantém a busca por cidade e permite informar uma origem manual | Não calcula nem prioriza distância sem origem válida |
| Informação ausente, antiga ou incorreta | Sinaliza a limitação e oferece “Sinalizar dado incorreto” | Cria protocolo, preserva o valor anterior e encaminha ao curador ou gestor |
| Serviço de mapas indisponível | Mantém os dados do local e informa que a rota externa não pôde ser aberta | Registra a falha sem bloquear a página de detalhes |
| Assistente ou microfone indisponível | Oferece busca convencional ou entrada por texto | Aciona fallback e registra o incidente para monitoramento |
| Sessão expirada durante uma contribuição | Preserva o conteúdo quando possível e solicita autenticação | Revalida a sessão antes de publicar ou salvar |
| Conteúdo denunciado | Informa que o conteúdo está em análise quando aplicável | Encaminha para moderação e oculta preventivamente apenas em caso de risco grave |
