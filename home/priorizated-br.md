---
title: Regras de Negócio Priorizadas
---

# Regras de Negócio Priorizadas

Critério usado: regras diretamente ligadas aos requisitos funcionais principais e às condições mínimas para publicar, consultar, recomendar e responder com dados confiáveis no catálogo regional.

| id | descrição | motivo da priorização |
| --- | --- | --- |
| [RN-001](home/business-rules#RN-001) | Cada local, evento ou experiência publicado deve possuir um único registro no catálogo regional, associado a cidade, categoria e tipo de experiência. | Evita registros duplicados no catálogo principal. |
| [RN-002](home/business-rules#RN-002) | Registros que representem o mesmo local, evento ou experiência devem ser consolidados antes da publicação pública. | Mantém a consistência dos locais, eventos e experiências publicados. |
| [RN-003](home/business-rules#RN-003) | Todo registro disponível para busca deve conter nome, cidade, categoria e palavras-chave de descoberta. | Garante que registros possam ser encontrados por busca. |
| [RN-004](home/business-rules#RN-004) | Categorias, cidades e perfis de público usados em filtros devem seguir uma taxonomia controlada do catálogo regional. | Sustenta filtros confiáveis por categoria, cidade e perfil de público. |
| [RN-005](home/business-rules#RN-005) | Novas categorias, cidades ou perfis de público só podem ser usados em filtros após validação da equipe responsável pelo catálogo. | Evita crescimento desorganizado das categorias e filtros. |
| [RN-008](home/business-rules#RN-008) | Todo local, evento, lista, recomendação ou publicação com impulsionamento pago, parceria comercial ou destaque editorial patrocinado deve ser identificado como conteúdo patrocinado antes da interação do usuário. | Protege transparência em catálogo, listas e recomendações. |
| [RN-011](home/business-rules#RN-011) | Restaurantes, bares e similares só podem ser publicados com cardápio ou descrição de produtos, faixa de preços, couvert artístico quando aplicável, horários, formato de atendimento, regras do local e canal de contato. | Define informações mínimas para publicação de bares, restaurantes e similares. |
| [RN-012](home/business-rules#RN-012) | Atrações turísticas e culturais só podem ser publicadas com descrição da experiência, horários de visitação, localização, valor de ingresso quando aplicável, acessibilidade, adequação infantil, segurança do entorno, programação associada e contato. | Define informações mínimas para publicação de atrações turísticas e culturais. |
| [RN-013](home/business-rules#RN-013) | Balneários e equipamentos recreativos só podem ser publicados com horários de funcionamento, regras de acesso, valor de entrada quando aplicável, serviços disponíveis, condições especiais de acesso, informações de segurança, estrutura disponível para visitantes e canal de contato ativo. | Define informações mínimas para publicação de balneários e equipamentos recreativos. |
| [RN-014](home/business-rules#RN-014) | Locais, atrações e equipamentos publicados devem possuir pelo menos três fotos reais do ambiente físico ou da estrutura divulgada. | Garante evidência visual básica dos locais publicados. |
| [RN-015](home/business-rules#RN-015) | Imagens publicadas devem representar o estado atual do local, atração, equipamento ou evento ao qual estão vinculadas. | Evita imagens desatualizadas ou incompatíveis com o local. |
| [RN-016](home/business-rules#RN-016) | Fotos do ambiente físico não podem ser imagens ilustrativas, genéricas ou de banco de imagens. | Impede uso de imagens genéricas para representar ambientes reais. |
| [RN-017](home/business-rules#RN-017) | Informações sobre rampas, elevadores, banheiros adaptados e outros recursos de acessibilidade devem corresponder à condição real do espaço no momento da publicação. | Garante que dados de acessibilidade reflitam a condição real do espaço. |
| [RN-019](home/business-rules#RN-019) | Informações de segurança do local e entorno devem se basear em registros, laudos, relatórios, sinalizações oficiais ou informação fornecida pelo responsável pelo local. | Exige base confiável para informações de segurança. |
| [RN-021](home/business-rules#RN-021) | O status aberto ou fechado deve refletir os horários cadastrados, distinguindo dias úteis, fins de semana, feriados e funcionamento noturno. | Mantém horários e status aberto/fechado coerentes. |
| [RN-022](home/business-rules#RN-022) | Informações de consulta, como locais, eventos, atrações, contatos públicos e avaliações publicadas, devem ser acessíveis sem autenticação do visitante. | Garante consulta pública ao catálogo e às avaliações. |
| [RN-029](home/business-rules#RN-029) | Avaliações aprovadas para publicação devem ser visíveis a qualquer visitante da plataforma, independentemente de autenticação. | Torna avaliações aprovadas acessíveis para apoiar decisões dos visitantes. |
| [RN-030](home/business-rules#RN-030) | Toda avaliação publicada deve estar associada ao perfil do usuário que a realizou, impedindo publicação anônima. | Reduz anonimato indevido em avaliações publicadas. |
| [RN-031](home/business-rules#RN-031) | Avaliações publicadas devem poder ser ordenadas por recência ou relevância. | Permite organizar avaliações por recência ou relevância. |
| [RN-032](home/business-rules#RN-032) | A relevância de avaliações deve considerar nota atribuída, recência, completude do comentário e quantidade de interações ou denúncias. | Define como a relevância das avaliações deve ser calculada. |
| [RN-043](home/business-rules#RN-043) | Roteiros personalizados só podem incluir locais com dados mínimos adequados ao tipo de cadastro e visíveis ao público. | Garante que roteiros usem locais com dados mínimos e visíveis ao público. |
| [RN-044](home/business-rules#RN-044) | Roteiros personalizados devem considerar interesses declarados, distância, horários de funcionamento, status do local e adequação ao público. | Define fatores necessários para roteiros personalizados. |
| [RN-045](home/business-rules#RN-045) | Listas pessoais pertencem ao usuário autenticado que as criou. | Protege listas criadas por usuários autenticados. |
| [RN-046](home/business-rules#RN-046) | Listas pessoais só podem ser editadas ou excluídas pelo proprietário. | Restringe edição e exclusão de listas ao proprietário. |
| [RN-050](home/business-rules#RN-050) | Itens marcados em checklists alteram apenas o acompanhamento do usuário ou do roteiro pessoal correspondente. | Limita checklists ao acompanhamento pessoal do usuário. |
| [RN-051](home/business-rules#RN-051) | A conclusão de itens de checklist não altera disponibilidade, status ou dados oficiais de local, evento ou atração. | Impede que checklists alterem dados oficiais de locais ou eventos. |
| [RN-054](home/business-rules#RN-054) | Respostas do assistente virtual devem priorizar dados do catálogo regional e o contexto da página atual quando disponível. | Orienta o assistente a priorizar dados do catálogo regional. |
| [RN-055](home/business-rules#RN-055) | O assistente deve indicar limitação quando o dado solicitado não existir no catálogo, estiver desatualizado, vier de fonte não verificada ou houver conflito entre fontes cadastradas. | Exige sinalização de dados inexistentes, desatualizados ou conflitantes. |
| [RN-057](home/business-rules#RN-057) | Consulta ao assistente iniciada em página de local ou evento deve considerar o local ou evento dessa página como contexto da conversa. | Permite que o assistente use o contexto da página atual. |
| [RN-058](home/business-rules#RN-058) | Informações obtidas de fontes externas só podem atualizar o catálogo quando a fonte e a data de referência forem identificadas. | Controla atualização do catálogo por fontes identificadas e datadas. |
