---
title: Requisitos Não Funcionais — Segurança e Desempenho
---

1. [Requisitos Transversais](#requisitos-transversais)
2. [Épico 1: Exploração e Descoberta](#épico-1-exploração-e-descoberta)
3. [Épico 2: Informações e Detalhes do Local](#épico-2-informações-e-detalhes-do-local)
4. [Épico 3: Avaliações e Comunidade](#épico-3-avaliações-e-comunidade)
5. [Épico 4: Recomendações Personalizadas](#épico-4-recomendações-personalizadas)
6. [Épico 5: Organização Pessoal e Roteiros](#épico-5-organização-pessoal-e-roteiros)
7. [Épico 6: Assistente Virtual (Chatbot)](#épico-6-assistente-virtual-chatbot)
8. [Épico 7: Interações Sociais e Compartilhamento](#épico-7-interações-sociais-e-compartilhamento)
9. [Épico 8: Equipamentos Culturais e Estabelecimentos](#épico-8-equipamentos-culturais-e-estabelecimentos)

---

### Requisitos Transversais

> [!note]
>
> Requisitos aplicáveis ao sistema como um todo, não vinculados a um único épico — cobrem autenticação, proteção de dados, segurança da aplicação, disponibilidade e escalabilidade.

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-SEG-001 | Autenticação Segura de Usuários e Administradores | O sistema deve implementar autenticação segura para usuários e administradores, utilizando, no mínimo, credenciais de e-mail e senha com hash criptográfico (bcrypt ou argon2). | [RF-020](functional-requirements#L33), [RF-044](functional-requirements#L82), [HU-042](user-storys#L78), RF-021 a RF-027 |
| RNF-SEG-003 | Controle de Acesso Baseado em Papéis (RBAC) | O sistema deve implementar controle de acesso baseado em papéis (RBAC) com, no mínimo, dois perfis: usuário autenticado e administrador. | [HU-009](user-storys#L16), [HU-040](user-storys#L76), [HU-046](user-storys#L82), [HU-018](user-storys#L29) a [HU-025](user-storys#L44), [HU-038](user-storys#L74) a [HU-054](user-storys#L90) |
| RNF-SEG-005 | Encerramento Automático de Sessões Inativas | O sistema deve encerrar automaticamente sessões inativas após um período máximo de 30 minutos para administradores e 24 horas para usuários comuns. | [RF-045](functional-requirements#L83) a [RF-056](functional-requirements#L94) |
| RNF-SEG-006 | Bloqueio por Tentativas de Login Falhas | O sistema deve bloquear temporariamente a conta após 5 tentativas consecutivas de login com falha, aplicando bloqueio progressivo (lockout). | [RF-044](functional-requirements#L82) |
| RNF-SEG-007 | Proteção contra Ataques de Injeção (SQL/NoSQL/XSS) | O sistema deve implementar proteção contra ataques de injeção (SQL Injection, NoSQL Injection, XSS) em todos os campos de entrada, incluindo busca por palavras-chave, avaliações, comentários e interações com o chatbot. | [RF-004](functional-requirements#L9), [RF-020](functional-requirements#L33), [RF-028](functional-requirements#L53) a [RF-031](functional-requirements#L56) |
| RNF-SEG-008 | Proteção contra CSRF | O sistema deve implementar proteção CSRF (Cross-Site Request Forgery) em todas as operações que alteram estado, incluindo publicação de avaliações, criação de listas, cadastro e edição de equipamentos/atrações/ofertas/publicações. | [RF-020](functional-requirements#L33), [RF-025](functional-requirements#L46), [RF-040](functional-requirements#L78), [RF-045](functional-requirements#L83), [RF-050](functional-requirements#L88), [RF-053](functional-requirements#L91) |
| RNF-SEG-009 | Sanitização de Conteúdo Gerado por Usuários | O sistema deve validar e sanitizar todo conteúdo gerado pelo usuário (avaliações, comentários, textos em enquetes) antes da exibição pública, prevenindo ataques XSS armazenados. | [RF-019](functional-requirements#L32), [RF-020](functional-requirements#L33), [RF-036](functional-requirements#L74) |
| RNF-SEG-010 | Limitação de Requisições (Rate Limiting) | O sistema deve implementar rate limiting nas APIs públicas, limitando o número de requisições por IP/usuário para prevenir ataques de negação de serviço (DoS/DDoS). | RF-001 a RF-018, [RF-028](functional-requirements#L53) |
| RNF-SEG-011 | Validação de Arquivos de Mídia Enviados | O sistema deve implementar validação de tipo, tamanho e formato nos arquivos de mídia (fotos, vídeos, áudio) enviados por usuários e administradores, rejeitando arquivos potencialmente maliciosos. | [RF-008](functional-requirements#L17), [RF-034](functional-requirements#L59), [RF-035](functional-requirements#L60), [RF-038](functional-requirements#L76) |
| RNF-SEG-013 | Validação de Dados Importados de Fontes Externas | O módulo de importação de dados de fontes externas deve validar e sanitizar todas as informações recebidas antes de integrá-las à base de dados do sistema. | [RF-032](functional-requirements#L57), [HU-030](user-storys#L53) |
| RNF-SEG-015 | Gerenciamento Seguro de Chaves de API | O sistema deve utilizar chaves de API seguras e rotacionáveis para integração com serviços externos (APIs de mapas, serviços de IA para o chatbot, fontes de dados). | [RF-011](functional-requirements#L20), [RF-028](functional-requirements#L53) a [RF-035](functional-requirements#L60), [RF-032](functional-requirements#L57) |
| RNF-PDD-001 | Comunicação Criptografada via HTTPS/TLS | Toda a comunicação entre o cliente (app/web) e o servidor deve ser realizada exclusivamente via HTTPS com TLS 1.2 ou superior. | [RF-021](functional-requirements#L38), [RF-020](functional-requirements#L33), [RF-025](functional-requirements#L46), [RF-011](functional-requirements#L20) |
| RNF-PDD-002 | Armazenamento Seguro de Senhas | As senhas dos usuários e administradores devem ser armazenadas utilizando funções de hash seguras (bcrypt com custo mínimo de 10 ou argon2id), nunca em texto claro. | RNF-SEG-001, [RF-044](functional-requirements#L82) |
| RNF-PDD-003 | Conformidade com a LGPD | Dados pessoais sensíveis (e-mail, histórico de visitas, listas pessoais, avaliações vinculadas ao perfil) devem ser protegidos em conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018). | [RF-021](functional-requirements#L38), [RF-026](functional-requirements#L47), [RF-020](functional-requirements#L33), [RF-025](functional-requirements#L46), [RF-022](functional-requirements#L39) a [RF-024](functional-requirements#L41) |
| RNF-PDD-004 | Exclusão de Conta e Dados Pessoais (Direito ao Esquecimento) | O sistema deve permitir que o usuário exclua sua conta e todos os dados pessoais associados (direito ao esquecimento), conforme Art. 18 da LGPD. | RNF-PDD-003, RF-020 a RF-027 |
| RNF-PDD-005 | Consentimento e Política de Privacidade | O sistema deve apresentar termos de uso e política de privacidade claros antes da coleta de qualquer dado pessoal, exigindo consentimento explícito do usuário. | — (exigência legal geral da LGPD) |
| RNF-DIS-001 | Disponibilidade Mínima do Sistema (Uptime) | O sistema deve garantir disponibilidade mínima de 99,5% (uptime), equivalente a no máximo ~43,8 horas de indisponibilidade por ano. | [storytelling](storytelling) |
| RNF-DIS-002 | Failover Automático de Serviços Críticos | O sistema deve implementar mecanismos de failover automático para os serviços críticos (API principal, banco de dados), com recuperação em no máximo 5 minutos. | [RF-001](functional-requirements#L6) a [RF-018](functional-requirements#L27) |
| RNF-DIS-003 | Backups Automáticos do Banco de Dados | O sistema deve realizar backups automáticos diários do banco de dados, com retenção mínima de 30 dias, e backups incrementais a cada 6 horas. | [RF-020](functional-requirements#L33), RF-040 a RF-056 |
| RNF-ESC-001 | Suporte a Usuários Simultâneos em Operação Normal | O sistema deve suportar, no mínimo, 1.000 usuários simultâneos em condições normais de operação, sem degradação perceptível de desempenho. | [survey](survey) |
| RNF-ESC-002 | Escalonamento Horizontal em Picos de Demanda | O sistema deve ser capaz de escalar horizontalmente para suportar picos de até 5.000 usuários simultâneos durante períodos de alta demanda (eventos culturais regionais, feriados, férias). | — (característica regional do Cariri) |
| RNF-ESC-003 | Escalonamento Independente de Componentes | A arquitetura do sistema deve permitir escalonamento independente dos seguintes componentes: API principal, serviço do chatbot, serviço de processamento de mídia e serviço de recomendação. | RF-001 a RF-006, RF-028 a RF-035, RF-008, RF-034, RF-038, RF-021 a RF-024 |
| RNF-EFI-004 | Importação Incremental de Dados Externos | O módulo de importação de dados de fontes externas deve executar atualizações de forma incremental, processando apenas os registros alterados desde a última importação, minimizando o consumo de recursos. | [RF-032](functional-requirements#L57) |

### Épico 1: Exploração e Descoberta

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-DES-001 | Tempo de Carregamento do Catálogo e Listas | As páginas de consulta ao catálogo regional, listas de locais populares e locais pouco divulgados devem ser carregadas em no máximo 2 segundos (P95), considerando uma conexão 4G padrão. | [RF-001](functional-requirements#L6), [RF-002](functional-requirements#L7), [RF-003](functional-requirements#L8), [storytelling](storytelling) |
| RNF-DES-002 | Tempo de Resposta da Pesquisa | As operações de pesquisa por palavras-chave, nome, categoria ou cidade devem retornar resultados em no máximo 1,5 segundo (P95). | [RF-004](functional-requirements#L9), [RF-005](functional-requirements#L10), [RF-006](functional-requirements#L11), [survey](survey) |
| RNF-EFI-002 | Paginação e Carregamento sob Demanda | O sistema deve implementar paginação e carregamento sob demanda (infinite scroll ou paginação explícita) para listas de locais, eventos, avaliações e resultados de busca, limitando a carga inicial a no máximo 20 itens por página. | [RF-001](functional-requirements#L6), [RF-002](functional-requirements#L7), [RF-019](functional-requirements#L32) |
| RNF-EFI-005 | Indexação para Pesquisa Full-Text | As consultas ao banco de dados para pesquisa full-text (busca por palavras-chave) devem utilizar índices otimizados (ex.: GIN/GiST no PostgreSQL ou índices de texto no MongoDB) para garantir performance sub-segundo. | [RF-004](functional-requirements#L9), [RF-005](functional-requirements#L10) |
| RNF-ESC-004 | Escalabilidade do Catálogo de Locais e Eventos | O banco de dados deve suportar o crescimento do catálogo de locais e eventos sem degradação de performance nas consultas, mantendo tempos de resposta dentro dos SLAs definidos para até 50.000 locais/eventos cadastrados e 500.000 avaliações. | [RF-001](functional-requirements#L6) |

### Épico 2: Informações e Detalhes do Local

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-SEG-014 | Segurança em Links Externos de Redes Sociais | Links externos exibidos no sistema (redes sociais, perfis públicos) devem ser validados quanto à URL e apresentados com atributos `rel="noopener noreferrer"` para prevenir ataques de tabnabbing. | [RF-033](functional-requirements#L58), [RF-017](functional-requirements#L26) |
| RNF-DES-003 | Tempo de Renderização da Página de Detalhes do Local | A página de detalhes de um local (informações descritivas, fotos, mídias, horários, preços, localização, segurança, higiene, acessibilidade) deve ser renderizada em no máximo 3 segundos (P95), com carregamento progressivo de mídias. | [RF-007](functional-requirements#L16) a [RF-015](functional-requirements#L24), [RF-040](functional-requirements#L33), [RF-041](functional-requirements#L34) |
| RNF-DES-006 | Otimização de Carregamento de Imagens e Mídias | O carregamento de imagens e mídias dos locais deve utilizar lazy loading e formatos otimizados (WebP/AVIF com fallback para JPEG), garantindo que a primeira exibição visual ocorra em no máximo 1,5 segundo. | [RF-008](functional-requirements#L17), [RF-034](functional-requirements#L59), [RF-038](functional-requirements#L76) |
| RNF-DIS-004 | Cache (CDN) para Recursos Estáticos | O sistema deve implementar cache (CDN) para recursos estáticos (imagens, mídias, dados do catálogo pouco alterados), reduzindo a carga no servidor de origem e melhorando o tempo de resposta para usuários distribuídos geograficamente. | [RF-008](functional-requirements#L17), [RF-034](functional-requirements#L59) |

### Épico 3: Avaliações e Comunidade

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-EFI-003 | Upload Assíncrono de Mídias da Comunidade | O processamento de upload de mídias (fotos e vídeos) deve ser realizado de forma assíncrona, com feedback de progresso ao usuário, sem bloquear a interface. | [RF-038](functional-requirements#L76) |

### Épico 4: Recomendações Personalizadas

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-PDD-006 | Anonimização de Dados para Recomendação por Perfis Similares | O sistema deve anonimizar ou pseudonimizar dados de perfis de usuários utilizados para filtragem colaborativa e recomendações por perfis similares. | [RF-023](functional-requirements#L40), [HU-021](user-storys#L36) |
| RNF-EFI-001 | Tempo de Processamento do Algoritmo de Recomendação | O algoritmo de recomendação personalizada (por histórico, avaliações e perfis similares) deve processar a geração de recomendações em no máximo 3 segundos (P95) por requisição, utilizando cálculos pré-computados ou cache de resultados quando possível. | [RF-021](functional-requirements#L38) a [RF-024](functional-requirements#L41) |

### Épico 5: Organização Pessoal e Roteiros

> [!note]
>
> Nenhum requisito não funcional específico foi identificado para este épico além dos Requisitos Transversais.

### Épico 6: Assistente Virtual (Chatbot)

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-PDD-007 | Tratamento Transitório de Áudio Enviado ao Assistente | Registros de áudio enviados ao assistente virtual devem ser processados de forma transitória, sem armazenamento permanente, ou com consentimento explícito do usuário. | [RF-035](functional-requirements#L60), [HU-033](user-storys#L56) |
| RNF-DES-004 | Tempo de Primeira Resposta do Assistente Virtual | O assistente virtual (chatbot) deve retornar a primeira resposta em no máximo 5 segundos (P95), com indicador visual de processamento durante a espera. | [RF-028](functional-requirements#L53) a [RF-031](functional-requirements#L56), [RF-029](functional-requirements#L54) |
| RNF-DES-005 | Tempo de Conversão de Áudio em Texto (Speech-to-Text) | O processamento de áudio (speech-to-text) no assistente virtual deve converter o prompt de voz em texto em no máximo 4 segundos (P95) para gravações de até 30 segundos. | [RF-035](functional-requirements#L60), [HU-033](user-storys#L56) |
| RNF-DIS-005 | Fallback Gracioso do Assistente Virtual | O assistente virtual deve implementar fallback gracioso: quando o serviço de IA estiver indisponível, o sistema deve notificar o usuário e oferecer alternativas de busca convencional. | [RF-030](functional-requirements#L55), [HU-028](user-storys#L51) |

### Épico 7: Interações Sociais e Compartilhamento

> [!note]
>
> Nenhum requisito não funcional específico foi identificado para este épico além dos Requisitos Transversais.

### Épico 8: Equipamentos Culturais e Estabelecimentos

| id | requisito | descrição | relacionada_com |
| --- | --- | --- | --- |
| RNF-SEG-002 | Autenticação Multifator para Administradores | O sistema deve suportar autenticação multifator (MFA) para contas de administradores de equipamentos culturais e estabelecimentos gastronômicos. | [RF-043](functional-requirements#L81), [RF-044](functional-requirements#L82) |
| RNF-SEG-004 | Escopo de Acesso de Administradores de Local | O sistema deve garantir que administradores de equipamentos culturais e estabelecimentos gastronômicos acessem apenas os recursos vinculados aos seus próprios estabelecimentos. | [RF-043](functional-requirements#L81), [HU-041](user-storys#L77) |
| RNF-SEG-012 | Logs de Auditoria de Operações Administrativas | O sistema deve manter logs de auditoria para todas as operações administrativas (cadastro, edição e remoção de equipamentos, atrações, ofertas e publicações), registrando o responsável, a data/hora e a ação realizada. | [RF-040](functional-requirements#L78) a [RF-056](functional-requirements#L94) |
| RNF-DES-007 | Tempo de Resposta das Operações CRUD Administrativas | As operações CRUD administrativas (cadastrar, editar e remover equipamentos, atrações, ofertas e publicações) devem ser processadas em no máximo 2 segundos (P95). | [RF-040](functional-requirements#L78) a [RF-056](functional-requirements#L94) |