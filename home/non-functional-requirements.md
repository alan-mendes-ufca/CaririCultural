---
title: Requisitos Não Funcionais — Segurança e Desempenho
---

# Identificação e Especificação de Requisitos Não Funcionais de Segurança e Desempenho

## 1. Introdução

Este documento identifica e especifica os Requisitos Não Funcionais (RNF) relacionados à **segurança** e ao **desempenho** do sistema **Cariri Cultural** — plataforma web/mobile com assistente virtual (chatbot IA) voltada ao turismo e à cultura da região do Cariri.

Os requisitos aqui listados foram derivados a partir da análise dos seguintes artefatos do projeto:

- [Requisitos Funcionais](functional-requirements)
- [Histórias de Usuário](user-storys)
- [Entrevistas](interviews) — 12 entrevistas com usuários reais
- [Survey](survey) — questionário com 29 respondentes
- [Benchmarking](benchmarking/interview-analysis-and-benchmarking) — análise comparativa com 5 plataformas
- [HTA](hta) — Análise Hierárquica de Tarefas
- [Storytelling](storytelling) — narrativas de 3 personas

---

## 2. Classificação dos RNF

Os requisitos estão organizados nas seguintes categorias:

| Categoria | Descrição |
|-----------|-----------|
| **SEG** — Segurança | Controle de acesso, autenticação, autorização, proteção contra ataques |
| **PDD** — Proteção de Dados | Privacidade, criptografia, conformidade com LGPD |
| **DES** — Desempenho | Tempo de resposta, throughput, latência |
| **ESC** — Escalabilidade | Capacidade de crescimento horizontal e vertical |
| **DIS** — Disponibilidade | Uptime, recuperação de falhas, redundância |
| **EFI** — Eficiência | Uso otimizado de recursos computacionais |

---

## 3. Requisitos Não Funcionais de Segurança

### 3.1 Autenticação e Controle de Acesso

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-SEG-001 | O sistema deve implementar autenticação segura para usuários e administradores, utilizando, no mínimo, credenciais de e-mail e senha com hash criptográfico (bcrypt ou argon2). | Derivado de [RF-020](functional-requirements#L33) (publicar avaliações requer identificação do autor), [RF-044](functional-requirements#L82) (autenticação de administradores), [HU-042](user-storys#L78) (login de administradores) e das funcionalidades de personalização que exigem perfil autenticado (RF-021 a RF-027). |
| RNF-SEG-002 | O sistema deve suportar autenticação multifator (MFA) para contas de administradores de equipamentos culturais e estabelecimentos gastronômicos. | Derivado de [RF-043](functional-requirements#L81) (associação de administradores a equipamentos), [RF-044](functional-requirements#L82) (autenticação de administradores). Administradores gerenciam conteúdo público e devem ter proteção adicional. |
| RNF-SEG-003 | O sistema deve implementar controle de acesso baseado em papéis (RBAC) com, no mínimo, dois perfis: usuário autenticado e administrador. | Derivado da distinção de papéis observada nas histórias de usuário: visitante ([HU-009](user-storys#L16), [HU-040](user-storys#L76), [HU-046](user-storys#L82)), usuário autenticado ([HU-018](user-storys#L29) a [HU-025](user-storys#L44)) e administrador ([HU-038](user-storys#L74) a [HU-054](user-storys#L90)). |
| RNF-SEG-004 | O sistema deve garantir que administradores de equipamentos culturais e estabelecimentos gastronômicos acessem apenas os recursos vinculados aos seus próprios estabelecimentos. | Derivado de [RF-043](functional-requirements#L81) (associação de administradores), [HU-041](user-storys#L77) (associação de administradores a equipamentos culturais) e do princípio do menor privilégio. |
| RNF-SEG-005 | O sistema deve encerrar automaticamente sessões inativas após um período máximo de 30 minutos para administradores e 24 horas para usuários comuns. | Boas práticas de segurança aplicadas ao contexto de gestão de conteúdo público ([RF-045](functional-requirements#L83) a [RF-056](functional-requirements#L94)). |
| RNF-SEG-006 | O sistema deve bloquear temporariamente a conta após 5 tentativas consecutivas de login com falha, aplicando bloqueio progressivo (lockout). | Proteção contra ataques de força bruta, especialmente relevante para contas administrativas ([RF-044](functional-requirements#L82)). |

### 3.2 Proteção de Dados e Privacidade

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-PDD-001 | Toda a comunicação entre o cliente (app/web) e o servidor deve ser realizada exclusivamente via HTTPS com TLS 1.2 ou superior. | Requisito transversal. O sistema manipula dados pessoais (histórico de visitas — [RF-021](functional-requirements#L38), avaliações — [RF-020](functional-requirements#L33), listas pessoais — [RF-025](functional-requirements#L46)) e dados de localização ([RF-011](functional-requirements#L20)). |
| RNF-PDD-002 | As senhas dos usuários e administradores devem ser armazenadas utilizando funções de hash seguras (bcrypt com custo mínimo de 10 ou argon2id), nunca em texto claro. | Derivado de [RNF-SEG-001] e das operações de autenticação ([RF-044](functional-requirements#L82)). |
| RNF-PDD-003 | Dados pessoais sensíveis (e-mail, histórico de visitas, listas pessoais, avaliações vinculadas ao perfil) devem ser protegidos em conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018). | O sistema coleta e processa dados pessoais em: histórico de visitas ([RF-021](functional-requirements#L38), [RF-026](functional-requirements#L47)), avaliações com identificação do autor ([RF-020](functional-requirements#L33)), listas de desejos ([RF-025](functional-requirements#L46)), preferências para recomendação personalizada ([RF-022](functional-requirements#L39) a [RF-024](functional-requirements#L41)). |
| RNF-PDD-004 | O sistema deve permitir que o usuário exclua sua conta e todos os dados pessoais associados (direito ao esquecimento), conforme Art. 18 da LGPD. | Derivado de [RNF-PDD-003] e das funcionalidades que armazenam dados pessoais (RF-020 a RF-027). |
| RNF-PDD-005 | O sistema deve apresentar termos de uso e política de privacidade claros antes da coleta de qualquer dado pessoal, exigindo consentimento explícito do usuário. | Exigência legal da LGPD, aplicável a todas as funcionalidades que coletam dados pessoais. |
| RNF-PDD-006 | O sistema deve anonimizar ou pseudonimizar dados de perfis de usuários utilizados para filtragem colaborativa e recomendações por perfis similares. | Derivado de [RF-023](functional-requirements#L40) (sugerir locais com base em usuários com perfis compatíveis), [HU-021](user-storys#L36). A recomendação por perfis similares não deve expor dados de um usuário a outro. |
| RNF-PDD-007 | Registros de áudio enviados ao assistente virtual devem ser processados de forma transitória, sem armazenamento permanente, ou com consentimento explícito do usuário. | Derivado de [RF-035](functional-requirements#L60) (interpretar prompts de áudio), [HU-033](user-storys#L56). Áudio é dado pessoal sensível sob a LGPD. |

### 3.3 Proteção contra Ataques e Integridade

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-SEG-007 | O sistema deve implementar proteção contra ataques de injeção (SQL Injection, NoSQL Injection, XSS) em todos os campos de entrada, incluindo busca por palavras-chave, avaliações, comentários e interações com o chatbot. | Campos de entrada do usuário estão presentes em: pesquisa ([RF-004](functional-requirements#L9)), avaliações e comentários ([RF-020](functional-requirements#L33)), assistente virtual ([RF-028](functional-requirements#L53) a [RF-031](functional-requirements#L56)). |
| RNF-SEG-008 | O sistema deve implementar proteção CSRF (Cross-Site Request Forgery) em todas as operações que alteram estado, incluindo publicação de avaliações, criação de listas, cadastro e edição de equipamentos/atrações/ofertas/publicações. | Operações de escrita incluem: publicar avaliação ([RF-020](functional-requirements#L33)), criar lista ([RF-025](functional-requirements#L46)), cadastrar equipamento ([RF-040](functional-requirements#L78)), cadastrar atração ([RF-045](functional-requirements#L83)), cadastrar oferta ([RF-050](functional-requirements#L88)), cadastrar publicação ([RF-053](functional-requirements#L91)). |
| RNF-SEG-009 | O sistema deve validar e sanitizar todo conteúdo gerado pelo usuário (avaliações, comentários, textos em enquetes) antes da exibição pública, prevenindo ataques XSS armazenados. | Derivado de [RF-019](functional-requirements#L32) (exibir avaliações públicas), [RF-020](functional-requirements#L33) (publicar avaliações), [RF-036](functional-requirements#L74) (enquetes compartilháveis). |
| RNF-SEG-010 | O sistema deve implementar rate limiting nas APIs públicas, limitando o número de requisições por IP/usuário para prevenir ataques de negação de serviço (DoS/DDoS). | O sistema expõe endpoints públicos de consulta (RF-001 a RF-018) e um assistente virtual ([RF-028](functional-requirements#L53)) que pode ser alvo de abuso. |
| RNF-SEG-011 | O sistema deve implementar validação de tipo, tamanho e formato nos arquivos de mídia (fotos, vídeos, áudio) enviados por usuários e administradores, rejeitando arquivos potencialmente maliciosos. | Derivado de [RF-008](functional-requirements#L17) (fotos e mídias), [RF-034](functional-requirements#L59) (imagens do local), [RF-035](functional-requirements#L60) (prompts de áudio), [RF-038](functional-requirements#L76) (mídias da comunidade). |
| RNF-SEG-012 | O sistema deve manter logs de auditoria para todas as operações administrativas (cadastro, edição e remoção de equipamentos, atrações, ofertas e publicações), registrando o responsável, a data/hora e a ação realizada. | Derivado das operações CRUD administrativas ([RF-040](functional-requirements#L78) a [RF-056](functional-requirements#L94)) e da necessidade de rastreabilidade de alterações em conteúdo público. |

### 3.4 Segurança de Integrações Externas

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-SEG-013 | O módulo de importação de dados de fontes externas deve validar e sanitizar todas as informações recebidas antes de integrá-las à base de dados do sistema. | Derivado de [RF-032](functional-requirements#L57) (importar e atualizar informações de fontes externas), [HU-030](user-storys#L53). Dados externos não confiáveis representam vetor de ataque. |
| RNF-SEG-014 | Links externos exibidos no sistema (redes sociais, perfis públicos) devem ser validados quanto à URL e apresentados com atributos `rel="noopener noreferrer"` para prevenir ataques de tabnabbing. | Derivado de [RF-033](functional-requirements#L58) (links para perfis públicos), [RF-017](functional-requirements#L26) (canais de contato com links de redes sociais). |
| RNF-SEG-015 | O sistema deve utilizar chaves de API seguras e rotacionáveis para integração com serviços externos (APIs de mapas, serviços de IA para o chatbot, fontes de dados). | Derivado de [RF-011](functional-requirements#L20) (localização/trajeto — integração com APIs de mapa), [RF-028](functional-requirements#L53) a [RF-035](functional-requirements#L60) (chatbot com IA), [RF-032](functional-requirements#L57) (importação de dados externos). |

---

## 4. Requisitos Não Funcionais de Desempenho

### 4.1 Tempo de Resposta

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-DES-001 | As páginas de consulta ao catálogo regional, listas de locais populares e locais pouco divulgados devem ser carregadas em no máximo **2 segundos** (P95), considerando uma conexão 4G padrão. | Derivado de [RF-001](functional-requirements#L6) (catálogo regional), [RF-002](functional-requirements#L7) (locais populares), [RF-003](functional-requirements#L8) (locais pouco divulgados). Essas são as funcionalidades de entrada do sistema, e a primeira impressão impacta a retenção — conforme as narrativas de storytelling, os usuários esperam encontrar informações de forma "simples e acessível". |
| RNF-DES-002 | As operações de pesquisa por palavras-chave, nome, categoria ou cidade devem retornar resultados em no máximo **1,5 segundo** (P95). | Derivado de [RF-004](functional-requirements#L9) (pesquisa), [RF-005](functional-requirements#L10) (sugestões alternativas), [RF-006](functional-requirements#L11) (filtragem). A pesquisa é uma das funcionalidades mais utilizadas — identificada como prioridade no [survey](survey) (filtros e busca entre as funcionalidades mais citadas). |
| RNF-DES-003 | A página de detalhes de um local (informações descritivas, fotos, mídias, horários, preços, localização, segurança, higiene, acessibilidade) deve ser renderizada em no máximo **3 segundos** (P95), com carregamento progressivo de mídias. | Derivado de [RF-007](functional-requirements#L16) a [RF-015](functional-requirements#L24) e [RF-040](functional-requirements#L33), [RF-041](functional-requirements#L34) (detalhes do local). Essa página agrega muitos dados e mídias; o carregamento progressivo (lazy loading) é necessário para manter a percepção de velocidade. |
| RNF-DES-004 | O assistente virtual (chatbot) deve retornar a primeira resposta em no máximo **5 segundos** (P95), com indicador visual de processamento durante a espera. | Derivado de [RF-028](functional-requirements#L53) a [RF-031](functional-requirements#L56) (assistente virtual), [RF-029](functional-requirements#L54) (interpretação de intenção). Interações conversacionais exigem baixa latência percebida para manter o engajamento. |
| RNF-DES-005 | O processamento de áudio (speech-to-text) no assistente virtual deve converter o prompt de voz em texto em no máximo **4 segundos** (P95) para gravações de até 30 segundos. | Derivado de [RF-035](functional-requirements#L60) (interpretar prompts de áudio), [HU-033](user-storys#L56). |
| RNF-DES-006 | O carregamento de imagens e mídias dos locais deve utilizar lazy loading e formatos otimizados (WebP/AVIF com fallback para JPEG), garantindo que a primeira exibição visual ocorra em no máximo **1,5 segundo**. | Derivado de [RF-008](functional-requirements#L17) (fotos e mídias), [RF-034](functional-requirements#L59) (imagens do local), [RF-038](functional-requirements#L76) (mídias da comunidade). |
| RNF-DES-007 | As operações CRUD administrativas (cadastrar, editar e remover equipamentos, atrações, ofertas e publicações) devem ser processadas em no máximo **2 segundos** (P95). | Derivado de [RF-040](functional-requirements#L78) a [RF-056](functional-requirements#L94) (operações administrativas). |

### 4.2 Escalabilidade

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-ESC-001 | O sistema deve suportar, no mínimo, **1.000 usuários simultâneos** em condições normais de operação, sem degradação perceptível de desempenho. | Dado o público-alvo regional (moradores e turistas do Cariri) e o alto interesse demonstrado no [survey](survey) (93,1% de interesse forte), o sistema deve comportar uso significativo desde o lançamento. |
| RNF-ESC-002 | O sistema deve ser capaz de escalar horizontalmente para suportar picos de até **5.000 usuários simultâneos** durante períodos de alta demanda (eventos culturais regionais, feriados, férias). | A região do Cariri possui eventos de grande porte (ex.: romarias, festivais culturais) que podem gerar picos súbitos de acesso. |
| RNF-ESC-003 | A arquitetura do sistema deve permitir escalonamento independente dos seguintes componentes: API principal, serviço do chatbot, serviço de processamento de mídia e serviço de recomendação. | Derivado da diversidade de funcionalidades com diferentes perfis de carga: catálogo/busca (RF-001 a RF-006), chatbot com IA (RF-028 a RF-035), mídia (RF-008, RF-034, RF-038) e recomendação personalizada (RF-021 a RF-024). |
| RNF-ESC-004 | O banco de dados deve suportar o crescimento do catálogo de locais e eventos sem degradação de performance nas consultas, mantendo tempos de resposta dentro dos SLAs definidos para até **50.000 locais/eventos cadastrados** e **500.000 avaliações**. | O catálogo regional ([RF-001](functional-requirements#L6)) tende a crescer continuamente com a adição de equipamentos culturais, estabelecimentos gastronômicos, atrações e eventos. |

### 4.3 Disponibilidade

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-DIS-001 | O sistema deve garantir disponibilidade mínima de **99,5%** (uptime), equivalente a no máximo ~43,8 horas de indisponibilidade por ano. | Os entrevistados relatam que usam o sistema para planejamento de visitas em tempo real (storytelling — João precisa de informações na sexta-feira à noite; Rafael consulta durante a viagem). Indisponibilidade causa frustração direta e perda de confiança. |
| RNF-DIS-002 | O sistema deve implementar mecanismos de failover automático para os serviços críticos (API principal, banco de dados), com recuperação em no máximo **5 minutos**. | Garantia de continuidade para as operações de consulta ([RF-001](functional-requirements#L6) a [RF-018](functional-requirements#L27)) que são o núcleo do sistema. |
| RNF-DIS-003 | O sistema deve realizar backups automáticos diários do banco de dados, com retenção mínima de 30 dias, e backups incrementais a cada 6 horas. | Proteção contra perda de dados de conteúdo gerado por usuários (avaliações — [RF-020](functional-requirements#L33)), conteúdo administrativo (RF-040 a RF-056) e dados pessoais dos usuários. |
| RNF-DIS-004 | O sistema deve implementar cache (CDN) para recursos estáticos (imagens, mídias, dados do catálogo pouco alterados), reduzindo a carga no servidor de origem e melhorando o tempo de resposta para usuários distribuídos geograficamente. | Derivado de [RF-008](functional-requirements#L17), [RF-034](functional-requirements#L59). Imagens e mídias de locais são acessadas com frequência e raramente alteradas. |
| RNF-DIS-005 | O assistente virtual deve implementar fallback gracioso: quando o serviço de IA estiver indisponível, o sistema deve notificar o usuário e oferecer alternativas de busca convencional. | Derivado de [RF-030](functional-requirements#L55) (orientar alternativas quando não possuir a informação), [HU-028](user-storys#L51). O chatbot depende de serviço externo de IA que pode apresentar indisponibilidade. |

### 4.4 Eficiência no Processamento

| ID | Requisito | Justificativa / Rastreabilidade |
|----|-----------|-------------------------------|
| RNF-EFI-001 | O algoritmo de recomendação personalizada (por histórico, avaliações e perfis similares) deve processar a geração de recomendações em no máximo **3 segundos** (P95) por requisição, utilizando cálculos pré-computados ou cache de resultados quando possível. | Derivado de [RF-021](functional-requirements#L38) a [RF-024](functional-requirements#L41) (recomendações personalizadas). Filtragem colaborativa e geração de roteiros são operações computacionalmente intensivas. |
| RNF-EFI-002 | O sistema deve implementar paginação e carregamento sob demanda (infinite scroll ou paginação explícita) para listas de locais, eventos, avaliações e resultados de busca, limitando a carga inicial a no máximo **20 itens por página**. | Derivado de [RF-001](functional-requirements#L6) (catálogo), [RF-002](functional-requirements#L7) (locais populares), [RF-019](functional-requirements#L32) (avaliações). Evita o carregamento de grandes volumes de dados. |
| RNF-EFI-003 | O processamento de upload de mídias (fotos e vídeos) deve ser realizado de forma assíncrona, com feedback de progresso ao usuário, sem bloquear a interface. | Derivado de [RF-038](functional-requirements#L76) (mídias da comunidade) e das operações de cadastro administrativo que envolvem upload de imagens. |
| RNF-EFI-004 | O módulo de importação de dados de fontes externas deve executar atualizações de forma incremental, processando apenas os registros alterados desde a última importação, minimizando o consumo de recursos. | Derivado de [RF-032](functional-requirements#L57) (importar e atualizar informações de fontes externas). A importação completa é computacionalmente cara e deve ser otimizada. |
| RNF-EFI-005 | As consultas ao banco de dados para pesquisa full-text (busca por palavras-chave) devem utilizar índices otimizados (ex.: GIN/GiST no PostgreSQL ou índices de texto no MongoDB) para garantir performance sub-segundo. | Derivado de [RF-004](functional-requirements#L9) (pesquisa por palavras-chave), [RF-005](functional-requirements#L10) (sugestões alternativas). |

---

## 5. Resumo Quantitativo

| Categoria | Quantidade |
|-----------|:----------:|
| Segurança (SEG) | 15 |
| Proteção de Dados (PDD) | 7 |
| Desempenho (DES) | 7 |
| Escalabilidade (ESC) | 4 |
| Disponibilidade (DIS) | 5 |
| Eficiência (EFI) | 5 |
| **Total** | **43** |

---

## 6. Observações e Considerações

> [!important]
>
> **Conformidade Legal:** Os requisitos de proteção de dados (RNF-PDD-001 a RNF-PDD-007) refletem obrigações legais da LGPD (Lei nº 13.709/2018), aplicável a qualquer sistema que colete e processe dados pessoais de usuários em território brasileiro.

> [!note]
>
> **Métricas de SLA:** Os tempos de resposta definidos nos requisitos de desempenho (RNF-DES) utilizam o percentil 95 (P95) como referência, garantindo que 95% das requisições atenderão ao tempo estipulado. Os 5% restantes contemplam cenários de carga extrema ou condições adversas de rede.

> [!tip]
>
> **Revisão Contínua:** Os valores numéricos de escalabilidade (RNF-ESC) e desempenho (RNF-DES) devem ser revisados após os primeiros ciclos de uso em produção, ajustando-se às métricas reais de adoção da plataforma.
