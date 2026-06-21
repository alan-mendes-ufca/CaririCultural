---
title: Regras de Negócio
---

## Regras de Negócio

### Épico 1: Exploração e Descoberta

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-001 | Catálogo Unificado Regional | O sistema deve disponibilizar um único catálogo que centraliza locais turísticos, culturais, gastronômicos, comerciais e de lazer da região do Cariri, eliminando a necessidade de consulta a múltiplas plataformas externas. | [RF-001](functional-requirements#L7), [HU-001](user-storys#L8) |
| RN-002 | Pesquisa por Palavras-chave | O sistema deve permitir pesquisar locais e eventos por palavras-chave, nome, categoria e cidade, retornando resultados relevantes ou sugestões alternativas. | [RF-004](functional-requirements#L10), [HU-004](user-storys#L11) |
| RN-003 | Filtragem por Categoria e Público | O sistema deve permitir filtrar locais e eventos por categoria (ex: turístico, gastronômico, cultural) e por adequação ao público (ex: infantil, famílias). | [RF-006](functional-requirements#L12), [HU-005](user-storys#L12) |
| RN-004 | Listagem por Popularidade | O sistema deve exibir listas de locais ordenadas por nível de visitação, incluindo tanto os locais mais visitados quanto os menos conhecidos. | [RF-002](functional-requirements#L8), [RF-003](functional-requirements#L9), [HU-002](user-storys#L9), [HU-003](user-storys#L10) |
| RN-005 | Sugestões Alternativas em Buscas sem Resultado | Quando uma busca não retornar resultados, o sistema deve exibir: termos de busca alternativos e categorias similares relacionadas ao termo pesquisado. | [RF-005](functional-requirements#L11), [HU-004](user-storys#L11) |
| RN-006 | Mensagem Informativa em Busca sem Resultado | Quando uma busca não retornar resultados, o sistema deve exibir uma mensagem clara e orientativa ao usuário, sem expor mensagens de erro técnicas. | [RF-005](functional-requirements#L11), [HU-004](user-storys#L11) |

### Épico 2: Informações e Detalhes do Local

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-007 | Campos Obrigatórios — Estabelecimentos Gastronômicos | Todo restaurante, bar ou similar cadastrado no sistema deve conter obrigatoriamente: cardápio com descrição dos pratos; faixa de preços (mínimo e máximo); indicação de couvert artístico (quando aplicável); horários de funcionamento detalhados (dias úteis, fins de semana e horário noturno); formato de atendimento (ex: mesa, self-service, rodízio com garçom, rodízio com fila, balcão); regras e restrições do local; canais de contato atualizados; e pelo menos três fotos do ambiente real. | [RF-007](functional-requirements#L18), [RF-010](functional-requirements#L21), [RF-041](functional-requirements#L31), [HU-008](user-storys#L20) |
| RN-008 | Campos Obrigatórios — Atrações Turísticas e Culturais | Toda atração turística e cultural cadastrada no sistema deve conter obrigatoriamente: descrição contextual (histórico e tipo de experiência); horários de funcionamento e dias de abertura; localização precisa com trajeto de acesso; valor de ingresso ou entrada (quando aplicável); informações de acessibilidade; indicação de adequação para o público infantil; informações sobre a segurança do entorno; eventos e programações associadas; canais de contato atualizados; e pelo menos três fotos do local real. | [RF-007](functional-requirements#L18), [RF-016](functional-requirements#L27), [HU-014](user-storys#L26) |
| RN-009 | Campos Obrigatórios — Balneários e Equipamentos Recreativos | Todo balneário ou equipamento recreativo cadastrado no sistema deve conter obrigatoriamente: horários de funcionamento; regras de acesso (itens permitidos e proibidos); valor de entrada; serviços disponíveis (alimentação, bebidas, lazer noturno); informações de segurança e infraestrutura; condições especiais (ex: isenção para aniversariantes); canal de WhatsApp ativo; e pelo menos três fotos do ambiente e estrutura. | [RF-009](functional-requirements#L20), [HU-007](user-storys#L19) |
| RN-010 | Exatidão de Informações de Acessibilidade | As informações sobre recursos de acessibilidade (rampas, elevadores, banheiros adaptados, etc.) publicadas em um local devem ser verificadas e corresponder à condição real do espaço no momento da publicação. | [RF-014](functional-requirements#L25), [HU-012](user-storys#L24) |
| RN-011 | Exatidão de Informações sobre Adequação Infantil | As informações sobre adequação para o público infantil devem especificar: disponibilidade de espaço para crianças; nível de segurança do ambiente; tipos de atividades adequadas; e faixas etárias com restrição de acesso (quando aplicável). | [RF-015](functional-requirements#L26), [HU-013](user-storys#L25) |
| RN-012 | Exatidão de Informações de Segurança | As informações sobre segurança do local e entorno devem ser baseadas em dados verificáveis (ex: registros de ocorrências, laudos ou relatórios de segurança pública) e não em opiniões subjetivas dos cadastrantes. | [RF-012](functional-requirements#L23), [HU-010](user-storys#L22) |
| RN-013 | Atualização de Status de Funcionamento | O horário de funcionamento exibido deve distinguir: dias úteis, fins de semana, feriados e funcionamento noturno. O status atual (aberto/fechado) deve ser calculado em tempo real com base nos horários cadastrados. | [RF-009](functional-requirements#L20), [HU-007](user-storys#L19) |
| RN-014 | Correspondência Real das Imagens | Todas as imagens publicadas no sistema devem representar o estado atual do local. Fotos de pratos devem corresponder ao que é efetivamente servido. Fotos de ambiente devem mostrar o espaço real, sem edições que distorçam a percepção do visitante. | [RF-034](functional-requirements#L67), [HU-036](user-storys#L30) |
| RN-015 | Acesso Público sem Autenticação | Todas as informações de consulta (locais, eventos, avaliações) devem ser acessíveis sem exigência de autenticação ou cadastro. | [RF-044](functional-requirements#L91), [HU-042](user-storys#L92) |
| RN-016 | Autenticação Obrigatória para Ações Administrativas | Ações de criação, edição e remoção de locais, atrações, ofertas e publicações exigem autenticação prévia com perfil de administrador. | [RF-044](functional-requirements#L91), [HU-042](user-storys#L92) |
| RN-017 | Disponibilização de Links para Redes Sociais | Quando um local possuir perfil público em redes sociais, o sistema deve exibir links diretos para esses perfis na página do local. | [RF-033](functional-requirements#L66), [HU-035](user-storys#L29) |
| RN-018 | Exibição de Informações Históricas e Culturais | O sistema deve disponibilizar informações históricas, culturais e sociais associadas aos locais da região do Cariri, quando disponíveis. | [RF-018](functional-requirements#L29), [HU-016](user-storys#L28) |
| RN-019 | Exibição de Regras e Políticas do Local | O sistema deve exibir as regras e políticas de cada local, incluindo: itens permitidos e proibidos, restrições de entrada e condições especiais de acesso ou preço. | [RF-040](functional-requirements#L30), [HU-038](user-storys#L31) |
| RN-020 | Exibição do Formato de Serviço | O sistema deve informar o formato de atendimento de cada estabelecimento (ex: mesa com garçom, self-service, rodízio, balcão), para que o usuário conheça a dinâmica antes da visita. | [RF-041](functional-requirements#L31), [HU-039](user-storys#L32) |

### Épico 3: Avaliações e Comunidade

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-021 | Visibilidade Pública das Avaliações | Toda avaliação publicada deve ser visível a qualquer usuário da plataforma, esteja autenticado ou não. | [RF-019](functional-requirements#L37), [HU-017](user-storys#L38) |
| RN-022 | Identificação do Avaliador | Toda avaliação publicada deve estar associada ao perfil do usuário que a realizou. Não são permitidas avaliações anônimas. | [RF-019](functional-requirements#L37), [HU-017](user-storys#L38) |
| RN-023 | Ordenação de Avaliações | As avaliações de um local devem poder ser ordenadas por relevância ou por recência, a critério do usuário. | [RF-019](functional-requirements#L37), [HU-017](user-storys#L38) |
| RN-024 | Tipos de Conteúdo Aceitos em Avaliações | O sistema deve aceitar os seguintes tipos de conteúdo em avaliações: texto descritivo com nota numérica; contexto da visita (ex: "visitei com família"); fotos e vídeos capturados pelo usuário; e links para publicações relacionadas ao local em redes sociais. | [RF-020](functional-requirements#L38), [HU-018](user-storys#L39) |
| RN-025 | Moderação de Conteúdo Inapropriado | O sistema deve disponibilizar um mecanismo para que usuários denunciem avaliações com conteúdo inapropriado. Avaliações denunciadas devem ser encaminhadas para revisão antes de serem removidas. | [RF-020](functional-requirements#L38), [HU-018](user-storys#L39) |

### Épico 4: Recomendações Personalizadas

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-026 | Recomendação por Histórico de Visitas | O sistema deve sugerir locais que compartilhem características com os locais que o usuário registrou como visitados anteriormente. | [RF-021](functional-requirements#L44), [HU-019](user-storys#L45) |
| RN-027 | Recomendação por Padrão de Avaliações | O sistema deve sugerir locais alinhados ao padrão de preferências identificado nas avaliações já realizadas pelo usuário. | [RF-022](functional-requirements#L45), [HU-020](user-storys#L46) |
| RN-028 | Recomendação por Perfis Similares | O sistema deve sugerir locais com base nos interesses de outros usuários com perfil compatível ao do usuário autenticado. | [RF-023](functional-requirements#L46), [HU-021](user-storys#L47) |
| RN-029 | Recomendação de Roteiros Personalizados | O sistema deve gerar roteiros de passeio considerando o histórico de visitas, avaliações e interesses declarados do usuário. | [RF-024](functional-requirements#L47), [HU-022](user-storys#L48) |

### Épico 5: Organização Pessoal e Roteiros

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-030 | Criação e Gerenciamento de Lista de Desejos | O sistema deve permitir que o usuário autenticado crie, edite, organize e exclua listas de locais que deseja visitar. | [RF-025](functional-requirements#L53), [HU-023](user-storys#L54) |
| RN-031 | Registro de Locais Visitados | O sistema deve permitir que o usuário autenticado sinalize um local como visitado, registrando a experiência em seu histórico pessoal. | [RF-026](functional-requirements#L54), [HU-024](user-storys#L55) |
| RN-032 | Checklists de Atividades | O sistema deve disponibilizar checklists vinculados a roteiros ou visitas, permitindo que o usuário marque atividades como concluídas durante o passeio. | [RF-027](functional-requirements#L55), [HU-025](user-storys#L56) |
| RN-033 | Roteiros Criados pelo Usuário | O sistema deve permitir que o usuário autenticado crie roteiros manualmente, adicionando locais em uma sequência definida por ele. | [RF-024](functional-requirements#L47), [HU-022](user-storys#L48) |

### Épico 6: Assistente Virtual (Chatbot)

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-034 | Interpretação de Intenção de Busca | O assistente virtual deve interpretar a intenção da consulta do usuário e retornar informações ou recomendações relevantes ao contexto da solicitação. | [RF-029](functional-requirements#L62), [HU-026](user-storys#L62) |
| RN-035 | Orientação Alternativa em Ausência de Informação | Quando o assistente virtual não possuir a informação solicitada, deve indicar caminhos alternativos para que o usuário continue sua busca (ex: sugestão de categorias, links externos). | [RF-030](functional-requirements#L63), [HU-028](user-storys#L64) |
| RN-036 | Acionamento Contextualizado do Assistente | O assistente virtual deve poder ser acionado a partir da página de um local ou evento, recebendo automaticamente o contexto dessa página para permitir continuidade da consulta sem reinicialização. | [RF-031](functional-requirements#L64), [HU-029](user-storys#L65) |
| RN-037 | Entrada de Áudio no Assistente Virtual | O assistente virtual deve aceitar prompts enviados em formato de áudio e retornar as respostas em formato de texto. | [RF-035](functional-requirements#L68), [HU-033](user-storys#L69) |

### Épico 7: Interações Sociais e Compartilhamento

> [!warning]
>
> **Funcionalidades em Avaliação (Aguardando Aprovação do Time)**

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-038 | Compartilhamento de Listas via Link Público | O sistema deve gerar um link público estável para cada lista personalizada do usuário. Esse link deve permitir visualização completa da lista sem exigir autenticação do visitante. | [RF-039](functional-requirements#L81), [HU-037](user-storys#L82) |
| RN-039 | Criação e Compartilhamento de Enquetes | O sistema deve permitir que o usuário autenticado crie enquetes com opções de locais ou eventos e compartilhe via link. A votação deve ser permitida sem autenticação dos votantes. | [RF-036](functional-requirements#L78), [HU-034](user-storys#L79) |
| RN-040 | Anonimato na Votação de Enquetes | A votação em enquetes compartilhadas não deve exigir autenticação nem identificar o votante. | [RF-036](functional-requirements#L78), [HU-034](user-storys#L79) |

### Épico 8: Equipamentos Culturais e Estabelecimentos

> [!warning]
>
> **Funcionalidades em Avaliação (Aguardando Aprovação do Time)**

| id | regra | descrição | relacionada_com |
|----|-------|-----------|-----------------|
| RN-041 | Cadastro de Equipamentos Culturais | O sistema deve permitir que administradores da plataforma cadastrem equipamentos culturais com suas informações completas. | [RF-040](functional-requirements#L87), [HU-038](user-storys#L88) |
| RN-042 | Edição de Equipamentos Culturais | O sistema deve permitir que administradores da plataforma editem as informações de equipamentos culturais já cadastrados. | [RF-041](functional-requirements#L88), [HU-039](user-storys#L89) |
| RN-043 | Consulta de Equipamentos Culturais | O sistema deve permitir que qualquer usuário consulte as informações de equipamentos culturais cadastrados. | [RF-042](functional-requirements#L89), [HU-040](user-storys#L90) |
| RN-044 | Associação de Administrador a Equipamento Cultural | O sistema deve permitir que o administrador da plataforma associe um usuário com perfil de administrador a um equipamento cultural específico. | [RF-043](functional-requirements#L90), [HU-041](user-storys#L91) |
| RN-045 | Autenticação de Administrador de Equipamento Cultural | O sistema deve exigir autenticação do administrador de equipamento cultural antes de permitir o acesso às funcionalidades de gerenciamento de seu equipamento. | [RF-044](functional-requirements#L91), [HU-042](user-storys#L92) |
| RN-046 | Cadastro de Atrações por Administrador | O sistema deve permitir que o administrador de um equipamento cultural cadastre atrações vinculadas ao seu equipamento. | [RF-045](functional-requirements#L92), [HU-043](user-storys#L93) |
| RN-047 | Edição de Atrações Cadastradas | O sistema deve permitir que o administrador de um equipamento cultural edite os dados de atrações previamente cadastradas em seu equipamento. | [RF-046](functional-requirements#L93), [HU-044](user-storys#L94) |
| RN-048 | Remoção de Atrações Cadastradas | O sistema deve permitir que o administrador de um equipamento cultural remova atrações cadastradas em seu equipamento. | [RF-047](functional-requirements#L94), [HU-045](user-storys#L95) |
| RN-049 | Consulta de Atrações | O sistema deve permitir que qualquer usuário consulte as atrações cadastradas em equipamentos culturais. | [RF-048](functional-requirements#L95), [HU-046](user-storys#L96) |
| RN-050 | Cadastro de Estabelecimentos Gastronômicos | O sistema deve permitir que administradores da plataforma cadastrem estabelecimentos gastronômicos com suas informações completas. | [RF-049](functional-requirements#L96), [HU-047](user-storys#L97) |
| RN-051 | Cadastro de Ofertas por Administrador | O sistema deve permitir que o administrador de um estabelecimento gastronômico cadastre ofertas vinculadas ao seu estabelecimento. | [RF-050](functional-requirements#L97), [HU-048](user-storys#L98) |
| RN-052 | Edição de Ofertas Cadastradas | O sistema deve permitir que o administrador de um estabelecimento gastronômico edite os dados de ofertas previamente cadastradas. | [RF-051](functional-requirements#L98), [HU-049](user-storys#L99) |
| RN-053 | Remoção de Ofertas Cadastradas | O sistema deve permitir que o administrador de um estabelecimento gastronômico remova ofertas cadastradas que não sejam mais válidas. | [RF-052](functional-requirements#L99), [HU-050](user-storys#L100) |
| RN-054 | Cadastro de Publicações | O sistema deve permitir que administradores da plataforma cadastrem publicações associadas a equipamentos culturais ou estabelecimentos gastronômicos. | [RF-053](functional-requirements#L100), [HU-051](user-storys#L101) |
| RN-055 | Criação de Publicações pelo Administrador do Local | O sistema deve permitir que o administrador de um equipamento cultural ou estabelecimento gastronômico crie publicações vinculadas ao seu local. | [RF-054](functional-requirements#L101), [HU-052](user-storys#L102) |
| RN-056 | Edição de Publicações Cadastradas | O sistema deve permitir que o administrador responsável edite o conteúdo de publicações já cadastradas. | [RF-055](functional-requirements#L102), [HU-053](user-storys#L103) |
| RN-057 | Remoção de Publicações Cadastradas | O sistema deve permitir que o administrador responsável remova publicações que não devam mais ser exibidas aos usuários. | [RF-056](functional-requirements#L103), [HU-054](user-storys#L104) |
