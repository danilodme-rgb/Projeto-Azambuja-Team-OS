# Minuta de Projeto — Azambuja Team OS

**Plataforma exclusiva de coaching de nutrição e treino de musculação**
Aplicativo iOS e Android para alunos · Site de captação · Painel administrativo do coach

| | |
|---|---|
| **Versão** | 1.0 — minuta para discussão |
| **Data** | Agosto de 2026 |
| **Status** | Pré-projeto. Escopo sujeito a validação na reunião de definição |
| **Documento de apoio** | `anexo-c-checklist-reuniao.md` (pauta da reunião) |

---

## 1. Sumário executivo

O objetivo é entregar ao coach uma plataforma **proprietária e exclusiva** — não um
aplicativo genérico de treino, nem uma planilha compartilhada, nem uma ferramenta de
prateleira com a marca dele por cima. A tese do produto é simples:

> O aluno paga pelo **método do coach**, não pelo software. O software existe para
> (a) fazer o método caber no bolso do aluno todos os dias e (b) devolver ao coach dados
> confiáveis para ele tomar decisões melhores e mais rápidas do que qualquer concorrente.

O que torna a plataforma diferenciada:

1. **Onboarding com triagem inteligente.** O aluno declara restrições alimentares e
   articulares/lesões uma única vez; o sistema cruza automaticamente essas restrições com o
   banco de exercícios e de alimentos e entrega ao coach a prescrição **já sinalizada** —
   ele nunca prescreve às cegas algo que o aluno não pode fazer ou comer.
2. **Prescrição híbrida.** O coach pode montar tudo do zero **ou** partir de modelos
   próprios por objetivo, editando o que quiser. O sistema aprende com os modelos dele, não
   com um algoritmo genérico.
3. **Execução medida, não declarada.** O aluno registra carga série a série e adesão
   alimentar refeição a refeição. Isso vira, sem trabalho manual, um relatório profissional
   de evolução (composição corporal, adesão, progressão de carga).
4. **Ritual semanal.** Videochamada de 30 minutos com relatório na tela. O acompanhamento
   deixa de ser "manda no WhatsApp" e vira consultoria com evidência.
5. **Recorrência de receita.** Planos mensal, trimestral, semestral e anual, com Pix e cartão,
   cobrança automática e renovação.

**Prazo estimado do MVP:** 10 a 14 semanas após o congelamento do escopo.
**Custo operacional estimado:** R$ 350 a R$ 700 por mês no início (detalhamento na seção 13).

---

## 2. Papéis e permissões

| Papel | Quem é | O que faz |
|---|---|---|
| **Administrador (coach)** | Azambuja | Acesso total: aprova alunos, monta treino e dieta, edita bancos de exercícios/alimentos, vê relatórios, responde mensagens, gerencia planos e cobranças |
| **Aluno** | Cliente pagante | Vê e executa o próprio treino e dieta, registra cargas e refeições, envia fotos e medidas, fala com o coach, participa da call semanal |
| **Lead** | Interessado que preencheu o formulário e ainda não foi aprovado/pagou | Acesso apenas ao status da própria solicitação |
| **Assistente (futuro)** | Estagiário/nutricionista parceiro | Permissões limitadas, definidas pelo coach. **Fora do MVP**, mas o modelo de dados já nasce preparado |

> **Nota de arquitetura:** mesmo com um único administrador hoje, o sistema é construído
> como multi-coach desde o primeiro dia (todo dado pertence a um `coach_id`). Isso não
> encarece o MVP e abre a porta para, no futuro, o Azambuja licenciar a plataforma para
> outros profissionais — uma segunda fonte de receita sem reescrever nada.

---

## 3. Jornada do aluno

### 3.1 Captação — o link de divulgação

O coach recebe **um link único e permanente** (ex.: `azambujateam.com.br` ou
`azambujateam.com.br/quero-treinar`) que ele divulga como quiser: bio do Instagram,
stories, WhatsApp, panfleto com QR Code, anúncio pago.

Ao clicar, abre uma **página de apresentação (landing page)** com:

- Vídeo ou foto de abertura + frase de posicionamento
- Os diferenciais do método (blocos curtos, com ícone)
- Como funciona, em 4 passos
- Resultados de alunos (fotos antes/depois **somente com autorização escrita** — ver seção 11)
- Planos e preços
- Perguntas frequentes
- **Botão principal: "QUERO SER ALUNO"** (repetido no topo, no meio e no fim da página)

**Recurso extra recomendado (baixo custo, alto retorno):** links rastreáveis por canal
(`/quero-treinar?origem=instagram`), para o coach saber de onde vêm os alunos que realmente
fecham — e onde vale investir.

### 3.2 Formulário de inscrição (anamnese)

Ao clicar em "Quero ser aluno", abre um formulário em **etapas curtas** (uma pergunta por
tela, estilo conversa — reduz muito a desistência em comparação a um formulário longo):

**Etapa 1 — Identificação**
Nome completo, data de nascimento, sexo/como se identifica, telefone (WhatsApp), e-mail,
cidade/UF.

**Etapa 2 — Dados corporais**
Altura, peso atual, peso desejado (opcional), circunferências (cintura, quadril, braço,
coxa — opcionais no cadastro, obrigatórias no acompanhamento).

**Etapa 3 — Fotos de avaliação**
Foto de sunga (homens) / biquíni (mulheres), nos três ângulos padrão: **frente, lado e
costas**. A tela explica em linguagem simples por que a foto é necessária, quem vê, por
quanto tempo fica guardada e como pedir a exclusão. Só avança com o **aceite explícito e
registrado** do termo de consentimento específico para foto corporal (seção 11).

**Etapa 4 — Nível de experiência**
Iniciante · Intermediário · Avançado — com a definição de cada um exibida logo abaixo da
opção (textos prontos no `anexo-b-textos-app.md`), para o aluno se autoclassificar
corretamente.

**Etapa 5 — Objetivo**
Emagrecer · Ganhar massa muscular (hipertrofia) · Recomposição corporal · Competir
(fisiculturismo) · Saúde e condicionamento geral · Performance esportiva · Outro (campo livre).

**Etapa 6 — Restrições alimentares**
Vegetariano (com subtipos) · Vegano · Celíaco / sem glúten · Intolerante à lactose ·
Alergias (amendoim, frutos do mar, ovo, soja, castanhas...) · Outras (campo livre).

**Etapa 7 — Restrições de exercício e saúde**
Lesões e limitações por região (ombro, joelho, lombar, cervical, punho, quadril, tornozelo),
cirurgias, hérnia de disco, hipertensão, diabetes, gestação, uso de medicamentos, exercícios
que já sabe que não consegue executar (campo livre).

**Etapa 8 — Rotina**
Dias e horários disponíveis para treinar, local de treino (academia completa / academia
simples / casa), quem cozinha, orçamento alimentar aproximado, sono, nível de estresse,
consumo de álcool.

**Etapa 9 — Consentimentos e envio**
Aceite da Política de Privacidade e dos Termos de Uso, aceite específico para dados de saúde,
aceite (opcional e separado) para uso de imagem em divulgação. Botão **"ENVIAR PARA O
AZAMBUJA"**.

### 3.3 Confirmação e SLA

Assim que envia, o aluno vê uma tela de confirmação com o **prazo de resposta do coach**
(parâmetro configurável — sugestão: até 2 dias úteis) e recebe o mesmo prazo por e-mail e
por WhatsApp. Se o prazo estourar, o sistema avisa o coach automaticamente.

### 3.4 Aprovação, pagamento e liberação

1. O coach analisa a ficha na fila de solicitações.
2. Aprova (ou recusa com justificativa, ou pede complemento de informação).
3. Aprovado → o aluno recebe o link de pagamento com os planos disponíveis.
4. Pagamento confirmado → conta criada, acesso ao app liberado, coach notificado para montar
   o protocolo.
5. Coach publica treino + dieta → aluno é notificado ("Seu protocolo chegou!").

### 3.5 Uso diário

- **Hoje:** tela inicial com o treino do dia e as refeições do dia.
- **Treino:** menus por grupo muscular → exercícios → séries, carga, técnica.
- **Dieta:** menus por refeição → opções → marcação do que comeu → contador e gráfico.
- **Evolução:** peso, medidas e fotos periódicas.
- **Fale com o Azambuja:** canal de mensagens.
- **Minha call:** agendamento e link da videochamada semanal.

---

## 4. Módulo de treino

### 4.1 Banco de exercícios (do coach)

Banco proprietário, editável só pelo coach. Cada exercício tem:

| Campo | Descrição |
|---|---|
| Nome | Ex.: "Supino reto com barra" |
| Grupo muscular primário | Peito, costas, ombro, bíceps, tríceps, quadríceps, posterior, glúteo, panturrilha, abdômen, antebraço, trapézio |
| Grupos secundários | Para relatórios de volume por músculo |
| Equipamento | Barra, halter, máquina, cabo, peso corporal, elástico, kettlebell |
| Padrão de movimento | Empurrar horizontal/vertical, puxar horizontal/vertical, agachar, dobrar quadril, isolado |
| **Tags de contraindicação** | Ombro, joelho, lombar, punho, cervical, quadril, tornozelo, hipertensão, gestação |
| Descrição de execução | Texto escrito pelo coach — a "voz" dele, um diferencial real |
| **Vídeo demonstrativo** | Link de vídeo público do YouTube (preferência: Leandro Twin) — ver 4.2 |
| Nível recomendado | Iniciante / intermediário / avançado |
| Unilateral? | Sim/não (afeta o registro de carga) |
| Observações internas | Só o coach vê |

**Carga inicial de dados:** entregamos o banco pré-carregado com um catálogo base de
exercícios (estimativa: 200 a 300, cobrindo todos os grupos musculares e equipamentos comuns),
com nomes, grupos, equipamentos e tags de contraindicação já preenchidos. O coach revisa,
apaga o que não usa, renomeia ao gosto dele e acrescenta os próprios. **Ele não começa de uma
tela em branco, mas o banco final é 100% dele.**

### 4.2 Vídeos de execução — como fazer isso corretamente

O coach escolhe o vídeo de referência de cada exercício. A abordagem tecnicamente e
juridicamente correta é:

- **Usar o player oficial do YouTube incorporado** (embed). O vídeo continua sendo servido
  pelo YouTube, o criador continua recebendo a visualização e o crédito, e não há cópia do
  conteúdo. Isso está dentro dos Termos de Serviço do YouTube.
- **Nunca baixar, re-hospedar ou remover a marca do vídeo.** Isso violaria direitos autorais
  e os termos da plataforma.
- Exibir sempre o **nome do canal** ("Canal: Leandro Twin") junto ao player.
- Como o vídeo é de terceiro, ele pode ser removido a qualquer momento. O sistema faz uma
  **verificação periódica automática de links quebrados** e avisa o coach para substituir.

> **Recomendação:** vale o coach considerar gravar, com o tempo, os vídeos dos exercícios
> principais com a execução dele. Isso é o diferencial máximo — vídeo próprio não some, não
> depende de terceiro e reforça a autoridade dele. O app já nasce preparado para hospedar
> vídeo próprio (campo alternativo ao link do YouTube). **A decidir com o coach.**

### 4.3 Montagem do treino — os dois caminhos

Fica registrado como **decisão em aberto** se o coach quer um, outro, ou os dois. A
recomendação técnica é **os dois**, porque o custo adicional é pequeno e o ganho de tempo
para ele é grande:

**Caminho A — Montagem do zero.** O coach cria a ficha em branco: adiciona exercícios,
define divisão (ABC, ABCD, push/pull/legs, full body...), séries, repetições, descanso,
técnica, observações por exercício.

**Caminho B — Modelos por objetivo.** O coach cria e salva **modelos próprios** ("Hipertrofia
Intermediário ABC", "Emagrecimento Iniciante Full Body", "Pré-contest 12 semanas"). Ao
prescrever, ele escolhe o modelo, o sistema preenche a ficha inteira e ele ajusta o que quiser.

> Importante: o modelo é **do coach**, não uma "IA que monta treino". O sistema nunca
> prescreve sozinho. Isso preserva a responsabilidade técnica do profissional e o valor
> percebido do serviço.

**Alerta automático de restrição.** Ao montar, se o coach incluir um exercício com tag de
contraindicação que bate com uma restrição declarada pelo aluno, aparece um aviso claro na
tela: *"⚠️ Este aluno declarou lesão no ombro. Este exercício está marcado como contraindicado
para ombro."* — o coach pode prosseguir mesmo assim (ele é a autoridade técnica), mas a
decisão fica **registrada em log**, o que também o protege juridicamente.

### 4.4 Tela do aluno — execução do treino

Exatamente como descrito no briefing:

1. Aluno abre **Treino** → vê a lista de **menus por grupo muscular** (Peito, Costas,
   Pernas...), conforme o treino do dia.
2. Abre o grupo → vê os **exercícios** daquele grupo.
3. Abre o exercício → vê:
   - **Séries prescritas** (ex.: 4 x 8-10, descanso 90s)
   - **Descrição de execução** escrita pelo coach
   - **Vídeo** (thumbnail clicável que abre o player)
   - **Campo de carga por série** — uma linha por série: carga (kg) e repetições realizadas
   - **Campo de RIR/RPE** (o quanto sobrou no tanque) — *opcional, a confirmar com o coach*
   - **Técnica avançada**, quando prescrita: descrição + caixa **"Consegui executar?"**
     (Sim / Parcialmente / Não) + campo de observação
   - **Comparativo automático:** ao lado de cada campo, a carga do mesmo exercício na semana
     anterior — o aluno vê na hora se está progredindo
   - Cronômetro de descanso
   - Campo de observação livre ("senti dor no ombro na terceira série")
4. Ao terminar, marca **"Treino concluído"** → gera o registro da sessão.

**Recurso de retenção:** o app funciona **offline** durante o treino (a academia costuma ter
sinal ruim) e sincroniza quando a conexão voltar. Isso é um diferencial prático enorme e
raramente bem resolvido pelos concorrentes.

### 4.5 Técnicas avançadas — ponto em aberto

O briefing registra corretamente que **as técnicas avançadas mudam a forma de montar o treino**
e que só se trabalha nisso depois da decisão do coach. Isso está preservado.

Preparamos o **`anexo-a-tecnicas-avancadas.md`** com o catálogo das técnicas mais usadas
(drop-set, rest-pause, bi-set, super-série, cluster, myo-reps, oclusão, negativas etc.),
cada uma com o que ela exige de **estrutura de dados diferente** no app. O coach marca quais
usa; só as marcadas entram no desenvolvimento. Isso evita construir dez telas para técnicas
que ele nunca vai prescrever.

---

## 5. Módulo de nutrição

### 5.1 Banco de alimentos — a fonte correta

**Observação técnica importante para a reunião.** O briefing menciona "a lista disponibilizada
pelo Ministério da Saúde". Na prática, o Ministério da Saúde publica o *Guia Alimentar para a
População Brasileira* (diretrizes, não composição nutricional). As bases brasileiras de
**composição de alimentos** de referência, gratuitas e confiáveis, são:

| Base | Origem | Cobertura | Observação |
|---|---|---|---|
| **TACO** — Tabela Brasileira de Composição de Alimentos, 4ª ed. | NEPA/UNICAMP | ~600 alimentos | A mais citada no Brasil, alimentos in natura e preparações típicas |
| **TBCA** — Tabela Brasileira de Composição de Alimentos | FCF/USP e FoRC | Milhares de itens, atualizada continuamente | Mais ampla e mais atual; inclui industrializados |
| **Tabelas da POF/IBGE** | IBGE | Alimentos consumidos no Brasil + medidas caseiras | Excelente para porções em medida caseira ("1 concha", "1 filé médio") |

**Recomendação:** usar **TACO + TBCA como base nutricional** e as **medidas caseiras do IBGE**
para as porções, porque o aluno não pesa tudo — ele pensa em "1 concha de feijão". Essas
bases são de acesso público e acadêmico; usaremos com **crédito visível à fonte** dentro do
app e verificaremos formalmente os termos de uso de cada uma antes da publicação. Se alguma
exigir autorização para uso em produto comercial, isso será solicitado por escrito, ou a base
correspondente será substituída.

Cada alimento carrega: nome, porção padrão, medida caseira, calorias, proteína, carboidrato,
gordura (total/saturada), fibra, sódio e **tags de restrição** (contém glúten, contém lactose,
origem animal, contém ovo, contém oleaginosas, contém frutos do mar, contém soja).

O coach pode: editar valores, criar alimentos próprios, criar **preparações/receitas**
(ex.: "frango grelhado do Azambuja — 150g") e marcar favoritos.

### 5.2 Montagem da dieta

O coach monta o plano semanal por refeição. Conforme o briefing, **cada grupo de refeição tem
no mínimo 3 opções equivalentes**, para o aluno ter escolha sem sair do plano:

```
CAFÉ DA MANHÃ  (alvo: 480 kcal · 35 P · 55 C · 12 G)
  Opção 1 — 3 ovos mexidos + 2 fatias de pão integral + 1 banana
  Opção 2 — Iogurte natural 200g + granola 40g + whey 30g
  Opção 3 — Tapioca 60g + frango desfiado 100g + mamão 100g
```

O sistema mostra ao coach, em tempo real enquanto ele monta, o **total calórico e de macros
de cada opção** e o **desvio entre as opções** — garantindo que as 3 sejam de fato
equivalentes. Isso é trabalho manual pesado hoje e vira automático.

**Alerta automático de restrição:** se o coach incluir um alimento com tag que conflita com a
restrição do aluno (ex.: leite para intolerante à lactose, qualquer item de origem animal para
vegano), o aviso aparece na hora, no mesmo padrão do módulo de treino, e a decisão fica logada.

Além do plano, o coach define: meta calórica diária, metas de macros, estratégia de água,
suplementação e observações.

### 5.3 Tela do aluno — registro alimentar

1. Aluno abre **Dieta** → vê os títulos das refeições do dia: *Café da manhã · Lanche da manhã
   · Almoço · Lanche da tarde · Jantar · Ceia* (nomes e quantidade definidos pelo coach).
2. Abre a refeição → vê as **opções prescritas** → marca a que comeu (um toque).
3. Se comeu algo fora do plano, registra em **"Comi outra coisa"** (busca no banco de
   alimentos) — isso é essencial: se o app não permitir registrar o desvio, o aluno mente ou
   simplesmente não registra, e o dado do coach vira lixo.
4. No rodapé da tela, sempre visível:
   - **Contador de calorias** do dia: consumido / meta / restante
   - **Gráfico de pizza dos macronutrientes** (proteína, carboidrato, gordura) — consumido
     versus meta
   - Marcador de água
5. Ao fim do dia, o app calcula o **percentual de adesão** ao plano.

---

## 6. Módulo de evolução e relatórios

### 6.1 O que o aluno registra periodicamente

| Dado | Frequência sugerida |
|---|---|
| Peso corporal | Diário ou semanal (definido pelo coach) |
| Circunferências (cintura, quadril, braço, coxa, panturrilha, tórax) | Quinzenal |
| Fotos de acompanhamento (mesmos 3 ângulos, mesma luz, mesma hora) | Quinzenal ou mensal |
| Dobras cutâneas / bioimpedância | Quando houver |
| Sono, energia, dores, apetite, humor | Semanal (check-in rápido) |

### 6.2 Relatório profissional

Gerado automaticamente e exportável em **PDF com a identidade visual do coach**, contendo:

- Cabeçalho: aluno, período, objetivo, semana do protocolo
- **Gráfico de evolução do objetivo** (peso e/ou circunferências ao longo do tempo, com a
  linha de meta)
- **Comparativo de fotos** lado a lado (primeira × atual)
- **Gráfico de progressão de carga** por exercício principal (ex.: supino, agachamento,
  levantamento terra) e volume total por grupo muscular
- **Adesão ao treino:** treinos realizados / prescritos, por semana
- **Adesão à dieta:** percentual, média de calorias e macros realizados × prescritos
- Execução das técnicas avançadas (o que ele conseguiu ou não)
- Observações do aluno no período (dores, dificuldades)
- **Espaço para o parecer do coach** — o texto dele, que é o que dá valor ao documento
- Rodapé com marca, CREF/CRN e data de emissão

Esse relatório é o roteiro da videochamada semanal e, ao mesmo tempo, o principal argumento
de renovação do plano: o aluno **vê** o que comprou.

---

## 7. Comunicação com o coach

### 7.1 Canal "Fale com o Azambuja"

Aba no app onde o aluno envia observações sobre treino, dieta, dificuldades, dúvidas, com
anexo de foto opcional. Cada mensagem é **categorizada** (Treino / Dieta / Dor ou lesão /
Financeiro / Outro) — isso permite ao coach priorizar: uma mensagem de dor entra na frente.

Conforme o briefing, a mensagem é **encaminhada para o e-mail profissional do coach** (ex.:
`contato@azambujateam.com.br`, a ser criado), e a resposta dele volta para dentro do app,
ficando registrada na conversa. A **regra de SLA** fica implementada e visível:

> Mensagens recebidas **até as 18h** são respondidas **no dia seguinte**. Mensagens recebidas
> após as 18h entram no ciclo do dia subsequente.

O app mostra ao aluno, no momento do envio, a data-limite da resposta — expectativa clara
evita cobrança. O painel do coach mostra a fila ordenada por prazo, com destaque para o que
está perto de vencer.

> **Ponto de atenção clínico e jurídico:** deve existir um aviso fixo no canal informando que
> ele **não é um serviço de emergência médica**, e que dor aguda, lesão ou mal-estar exigem
> procurar atendimento médico imediatamente. Texto no `anexo-b-textos-app.md`.

### 7.2 Videochamada semanal

- Chamada de **30 minutos por semana**, por aluno.
- O coach define **quais dias e faixas de horário** ele atende (ex.: terça e quinta, 18h-21h).
  O sistema abre apenas esses horários; o aluno escolhe um livre.
- Lembretes automáticos: 24h antes e 1h antes, por push e e-mail.
- O relatório de evolução é gerado automaticamente **antes** da call e fica disponível para os
  dois — a reunião começa com todo mundo olhando o mesmo dado.
- Após a call, o coach registra as **decisões tomadas** (ajuste de dieta, troca de exercício),
  que ficam no histórico do aluno.
- **Ferramenta:** recomendação de usar **Google Meet** (link gerado automaticamente na agenda,
  custo zero se já houver Google Workspace, funciona em qualquer celular sem instalar nada).
  Alternativas: Zoom, Whereby ou vídeo nativo dentro do app (mais caro e sem ganho real
  no MVP). **A decidir.**

---

## 8. Pagamentos e planos

| Plano | Observação |
|---|---|
| Mensal | Porta de entrada, maior taxa de cancelamento |
| Trimestral | Melhor equilíbrio; sugerido como "mais escolhido" |
| Semestral | Desconto maior |
| Anual | Melhor margem e melhor resultado para o aluno |

**Formas de pagamento:** cartão de crédito (com **renovação automática**) e **Pix**.

Detalhes importantes:

- **Nenhum dado de cartão passa pelos nossos servidores.** O pagamento é feito por um
  provedor autorizado (gateway), que devolve apenas um token. Isso é o padrão de mercado e
  reduz drasticamente o risco e a exigência de conformidade (PCI-DSS).
- **Pix não tem débito automático simples.** Para planos pagos por Pix, o sistema gera a
  cobrança e envia lembretes automáticos antes do vencimento (7 dias, 3 dias, no dia) e faz o
  bloqueio do acesso após um período de tolerância definido pelo coach.
- **Provedores recomendados** (todos com Pix + cartão + assinatura recorrente + split e nota):
  **Asaas**, **Mercado Pago**, **Pagar.me** ou **Stripe**. A escolha final depende das taxas
  negociadas e do que o contador do coach preferir. **A decidir.**
- O painel do coach mostra: receita mensal recorrente, alunos ativos, inadimplentes,
  renovações previstas e cancelamentos.
- Emissão de nota fiscal: integração possível, mas **fora do MVP** — a decidir conforme o
  regime tributário dele (MEI, ME/Simples).

---

## 9. Painel administrativo do coach

Tudo em uma única interface web (e também acessível pelo celular):

1. **Início** — solicitações novas, mensagens vencendo hoje, calls do dia, alunos sem registrar
   treino há X dias (alerta de abandono), aniversariantes.
2. **Solicitações** — fila de leads com ficha completa, fotos, restrições destacadas; aprovar,
   recusar, pedir complemento.
3. **Alunos** — lista com busca e filtros (objetivo, nível, plano, adesão, status); ficha
   individual com histórico completo.
4. **Prescrição** — montagem de treino e dieta, modelos, publicação.
5. **Bancos** — exercícios e alimentos.
6. **Mensagens** — caixa de entrada com SLA.
7. **Agenda** — disponibilidade e calls.
8. **Financeiro** — planos, cobranças, inadimplência.
9. **Relatórios** — por aluno e agregados.
10. **Configurações** — marca, textos da landing page, prazos, notificações.

---

## 10. Notificações

Push (celular) e e-mail, todas configuráveis pelo coach e pelo aluno:

- Lembrete de treino no horário que o aluno escolheu
- Lembrete de registrar as refeições
- "Seu protocolo novo chegou"
- "O Azambuja respondeu você"
- Lembrete de call (24h e 1h antes)
- Lembrete de pesagem/medidas/fotos
- Lembrete de vencimento de plano
- Para o coach: nova solicitação, mensagem próxima do prazo, aluno sumido, pagamento falhou

---

## 11. LGPD, segurança e conformidade

Esta é a seção mais sensível do projeto e precisa ser levada a sério desde o primeiro dia:
o projeto trata **dados pessoais sensíveis** — dados de saúde e imagens corporais.

### 11.1 Enquadramento legal

- Dados sobre saúde e condição física são **dados pessoais sensíveis** (art. 5º, II da LGPD).
  Fotos corporais para avaliação física, no contexto deste serviço, devem ser tratadas com o
  mesmo rigor.
- A base legal adequada é o **consentimento específico e destacado** (art. 11, I) — o aluno
  precisa consentir de forma separada, para finalidades específicas, e pode revogar.
- **O coach é o Controlador** dos dados; quem desenvolve e opera a infraestrutura atua como
  **Operador**. Isso precisa estar num contrato escrito entre as partes.

### 11.2 Medidas concretas que serão implementadas

**Consentimento**
- Aceites **separados e independentes**: (a) tratamento de dados de saúde para prestação do
  serviço; (b) armazenamento de fotos corporais; (c) uso de imagem para divulgação
  (**totalmente opcional** — recusar não impede a contratação).
- Cada aceite gravado com data, hora, IP e versão exata do texto aceito.
- Revogação disponível dentro do app, sem precisar pedir a ninguém.

**Fotos corporais — tratamento reforçado**
- Armazenamento em bucket **privado**, criptografado em repouso; nunca em URL pública.
- Acesso apenas por **link temporário assinado** (validade de minutos), gerado a cada
  visualização autorizada.
- **Remoção automática dos metadados EXIF** no upload (a foto do celular carrega
  geolocalização e identificação do aparelho — isso é removido antes de armazenar).
- **Marca d'água discreta** com o identificador do aluno na visualização, para desestimular
  vazamento.
- **Log de auditoria**: fica registrado quem visualizou qual foto e quando.
- Bloqueio de captura de tela nas telas de foto (nativo no Android; no iOS o sistema apenas
  notifica — o app registra e avisa).
- **Política de retenção definida** (sugestão: exclusão automática 12 meses após o fim do
  contrato, salvo pedido de manutenção do próprio aluno).

**Direitos do titular (art. 18)**
Tela de "Meus dados" no app, com: ver tudo o que está guardado, corrigir, **exportar em
arquivo** (portabilidade) e **excluir a conta e os dados**. Sem burocracia, sem precisar
mandar e-mail.

**Segurança técnica**
- Criptografia em trânsito (TLS 1.3) e em repouso.
- Autenticação com senha forte + verificação de e-mail; **2FA obrigatório para a conta do
  coach** (é a conta que vê todos os alunos).
- **Isolamento por linha no banco de dados (RLS)**: a regra "o aluno só enxerga os próprios
  dados" é aplicada pelo próprio banco, não só pelo aplicativo. Se houver uma falha no código
  do app, o banco continua bloqueando.
- Princípio do menor privilégio; segredos e chaves fora do código-fonte.
- Backups automáticos diários com restauração testada.
- Log de auditoria de todas as ações administrativas.
- Rate limiting e proteção contra abuso nos formulários públicos.
- Dados hospedados preferencialmente **em região brasileira** (São Paulo), reduzindo latência
  e simplificando a conformidade.

**Documentos a produzir**
Política de Privacidade, Termos de Uso, Termo de Consentimento para Dados de Saúde, Termo de
Uso de Imagem, Contrato de Prestação de Serviços, Contrato Controlador–Operador, e o
**Registro das Operações de Tratamento** (ROPA).

> **Recomendação:** esses documentos devem ser **revisados por um advogado** antes da
> publicação. Podemos entregar as minutas técnicas prontas para essa revisão, mas a validação
> jurídica não é substituível — especialmente por envolver dados sensíveis e imagem corporal.

### 11.3 Responsabilidade profissional

- O app é uma ferramenta de trabalho do profissional habilitado; a prescrição é sempre dele.
- Deve constar de forma visível o **CREF** (e o **CRN** do responsável pela prescrição
  dietética — vale confirmar como o coach opera esse ponto hoje: se ele é nutricionista, se
  trabalha com nutricionista parceiro, ou se atua com orientação alimentar dentro do escopo do
  profissional de educação física. **Item obrigatório da pauta da reunião.**).
- Avisos de "não é serviço de emergência" e recomendação de avaliação médica prévia.
- Menores de 18 anos: exigem consentimento do responsável — definir se serão aceitos.

---

## 12. Arquitetura técnica

### 12.1 É possível construir isso de forma segura, funcional e leve?

**Sim.** E a maneira de garantir isso não é escolher a tecnologia "mais moderna", e sim
escolher uma arquitetura que evite os três erros que afundam projetos deste tipo:

1. **Manter dois códigos separados para iOS e Android.** Dobra custo e tempo. Solução:
   um único código para os dois sistemas.
2. **Construir servidor, autenticação, armazenamento e permissões do zero.** É onde nascem as
   falhas de segurança. Solução: usar uma base gerenciada, madura e auditada, e escrever apenas
   a regra de negócio do coach.
3. **Colocar tudo no MVP.** Solução: fases (seção 14).

### 12.2 Stack recomendada

| Camada | Tecnologia | Por quê |
|---|---|---|
| **App iOS + Android** | React Native com Expo | Um único código para as duas lojas. Atualizações de correção podem ser enviadas sem passar por revisão da loja (OTA). Funciona offline |
| **Site + landing + painel do coach** | Next.js (React) | Mesma linguagem do app (compartilha regras e componentes), páginas muito rápidas e bem indexadas no Google — importante para a captação |
| **Backend, banco e autenticação** | Supabase (PostgreSQL gerenciado) na região de São Paulo | Banco relacional sério, autenticação pronta, armazenamento de arquivos, **segurança por linha (RLS)** e API automática. Reduz meses de trabalho e é onde a segurança fica mais forte |
| **Regras de negócio sensíveis** | Edge Functions (TypeScript) | Cálculo de macros, geração de relatório, integrações, webhooks de pagamento — nada sensível roda no celular |
| **Armazenamento de fotos** | Supabase Storage (bucket privado + URLs assinadas) | Ver seção 11.2 |
| **Pagamentos** | Asaas / Mercado Pago / Pagar.me / Stripe | Pix + cartão + assinatura recorrente |
| **E-mail transacional** | Resend ou Amazon SES | Entregabilidade e registro de envio |
| **Push** | Expo Push Notifications | Nativo do ecossistema, custo zero |
| **Relatório PDF** | Geração no servidor | PDF idêntico para todo mundo, com a marca do coach |
| **Hospedagem web** | Vercel | Deploy automático, HTTPS, CDN global |
| **Erros e monitoramento** | Sentry | Descobrir o problema antes do aluno reclamar |
| **Organização do código** | Monorepo (Turborepo) | App, site e regras compartilhadas no mesmo repositório, sem duplicação |

**Alternativa considerada:** backend próprio em NestJS + PostgreSQL. Dá mais controle, mas
acrescenta de 4 a 6 semanas ao MVP e transfere para nós a responsabilidade de construir
autenticação e permissões — justamente a parte onde erros custam caro. **Recomendação: começar
com Supabase.** Como os dados ficam em PostgreSQL puro, migrar para um backend próprio no
futuro é possível sem perder nada.

### 12.3 Estrutura do repositório

```
azambuja-team-os/
├─ apps/
│  ├─ mobile/          App do aluno (Expo / React Native) — iOS e Android
│  ├─ web/             Site público + landing de captação + painel do coach (Next.js)
│  └─ functions/       Funções de servidor (webhooks, relatórios, cálculos)
├─ packages/
│  ├─ core/            Regras de negócio compartilhadas (macros, progressão, adesão)
│  ├─ ui/              Componentes visuais compartilhados
│  └─ types/           Tipos e contratos de dados
├─ supabase/
│  ├─ migrations/      Estrutura do banco versionada
│  └─ policies/        Regras de segurança por linha (RLS)
├─ data/               Cargas iniciais (exercícios, TACO/TBCA, medidas caseiras)
└─ docs/               Esta documentação
```

### 12.4 "Leve" na prática

- App abaixo de ~30 MB, abre em menos de 2 segundos.
- Telas de treino e dieta **funcionam offline** e sincronizam depois.
- Imagens processadas e comprimidas no envio (a foto de 8 MB do celular vira ~400 KB sem perda
  visual relevante).
- Listas grandes (alimentos, exercícios) carregadas por partes, com busca instantânea local.
- Sem dependências pesadas desnecessárias.

---

## 13. Modelo de dados (visão inicial)

Tabelas principais previstas — serve para dimensionar o trabalho, e será refinada:

| Tabela | Guarda |
|---|---|
| `coaches` | Dados do coach, marca, CREF/CRN, configurações, SLA |
| `leads` | Solicitações recebidas pela landing page e status |
| `students` | Alunos ativos, plano, datas |
| `student_profiles` | Anamnese: nível, objetivo, rotina, histórico |
| `dietary_restrictions` / `exercise_restrictions` | Restrições declaradas |
| `consents` | Cada aceite de LGPD: tipo, versão do texto, data, IP |
| `body_photos` | Fotos de avaliação (metadados; o arquivo fica no bucket privado) |
| `body_measurements` | Peso, circunferências, dobras, bioimpedância |
| `exercises` | Banco de exercícios do coach, com tags e vídeo |
| `workout_templates` / `workout_template_items` | Modelos de treino por objetivo |
| `workout_plans` / `workout_days` / `workout_exercises` | Treino prescrito ao aluno |
| `workout_sessions` / `set_logs` | Execução: carga e repetições por série, RIR, técnica |
| `advanced_techniques` | Catálogo de técnicas (após decisão do coach) |
| `foods` | Base TACO/TBCA/IBGE + alimentos do coach, com tags |
| `recipes` / `recipe_items` | Preparações do coach |
| `diet_plans` / `meals` / `meal_options` / `meal_option_items` | Dieta prescrita (3+ opções por refeição) |
| `food_logs` | O que o aluno realmente comeu |
| `messages` / `message_threads` | Canal com o coach, com prazo de SLA |
| `appointments` | Videochamadas semanais |
| `reports` | Relatórios gerados |
| `subscriptions` / `payments` | Planos e cobranças |
| `audit_logs` | Auditoria de acessos e ações administrativas |
| `notifications` | Fila e histórico de envios |

---

## 14. Fases de entrega

### Fase 0 — Definição *(1 a 2 semanas)*
Reunião com o coach usando o `anexo-c-checklist-reuniao.md`; decisões pendentes fechadas;
identidade visual; escolha do gateway de pagamento; escopo do MVP congelado. **É onde estamos.**

### Fase 1 — MVP *(10 a 14 semanas)*
O suficiente para o coach **operar e faturar de verdade**:

- Site + landing page com o link de divulgação e o botão "Quero ser aluno"
- Formulário de inscrição completo, com fotos e consentimentos LGPD
- Fila de solicitações e aprovação pelo coach
- Planos, pagamento (Pix + cartão) e liberação de acesso
- Banco de exercícios (pré-carregado + editável) e banco de alimentos (TACO/TBCA/IBGE)
- Montagem de treino do zero + modelos
- Montagem de dieta com 3+ opções por refeição
- Alertas automáticos de restrição (treino e dieta)
- App do aluno: treino (carga por série, vídeo, descrição, offline) e dieta (marcação,
  contador de calorias, gráfico de macros)
- Registro de peso, medidas e fotos
- Relatório de evolução em PDF
- Canal "Fale com o Azambuja" com a regra das 18h
- Agenda e link da call semanal
- Notificações push essenciais
- Painel do coach
- Publicação nas lojas (App Store e Google Play)

### Fase 2 — Consolidação *(4 a 6 semanas)*
Técnicas avançadas (conforme a decisão do coach) · Relatórios comparativos e agregados ·
Chat em tempo real · Programa de indicação ("indique e ganhe") · Metas e conquistas ·
Integração com Apple Health / Google Fit (passos, peso da balança inteligente) ·
Exportações para o coach.

### Fase 3 — Escala *(a definir)*
Múltiplos coaches/assistentes · Loja de e-books e programas avulsos · Automação de marketing ·
Aplicativo de coach dedicado · Nota fiscal automática · Área de comunidade.

---

## 15. Custos estimados

### 15.1 Custo mensal de operação (fase inicial, até ~200 alunos)

| Item | Estimativa/mês |
|---|---|
| Banco de dados, autenticação e armazenamento (Supabase Pro) | ~R$ 140 |
| Hospedagem web (Vercel Pro) | ~R$ 110 |
| E-mail transacional | R$ 0 a R$ 110 |
| E-mail profissional (Google Workspace, 1 conta) | ~R$ 35 |
| Domínio | ~R$ 5 (≈R$ 60/ano) |
| Monitoramento de erros (Sentry — plano gratuito no início) | R$ 0 |
| Videochamada (Google Meet incluso no Workspace) | R$ 0 |
| **Subtotal fixo** | **~R$ 290 a R$ 400** |
| Taxas de pagamento | ~1% (Pix) a ~4% (cartão parcelado) sobre o faturamento |

### 15.2 Custos únicos / anuais

| Item | Valor |
|---|---|
| Conta de desenvolvedor Apple | US$ 99/ano |
| Conta de desenvolvedor Google Play | US$ 25 (uma vez) |
| Builds nas lojas (Expo EAS) | R$ 0 a ~US$ 99/mês, conforme frequência |
| Revisão jurídica dos documentos (advogado) | A orçar |
| Identidade visual / design da marca | A orçar, se ainda não existir |

**Leitura de negócio:** com o custo fixo em torno de R$ 300 a R$ 400 por mês, **3 a 4 alunos
pagantes já cobrem toda a infraestrutura.** Do quinto aluno em diante, é margem.

---

## 16. Riscos e mitigações

| Risco | Impacto | Como mitigamos |
|---|---|---|
| Vazamento de fotos corporais | **Crítico** — dano de imagem e responsabilização legal | Bucket privado, URL assinada de curta duração, sem EXIF, marca d'água, log de auditoria, retenção limitada, 2FA no acesso do coach |
| Escopo crescer sem controle | Atraso e estouro de custo | Escopo do MVP congelado por escrito; novidades vão para a Fase 2 |
| Baixa adesão do aluno ao registro diário | Relatórios vazios, produto perde valor | Registro em 1 toque, funcionamento offline, lembretes, comparativo de carga visível, gráfico imediato |
| Vídeo do YouTube removido pelo criador | Aluno vê link quebrado | Verificação automática de links + plano de gravar vídeos próprios |
| Rejeição do app pelas lojas | Atraso na publicação | Política de privacidade publicada, exclusão de conta dentro do app, avisos de saúde — os três motivos mais comuns de rejeição, tratados desde o início |
| Falta de definição sobre técnicas avançadas | Retrabalho na modelagem do treino | Já isolado como decisão explícita (Anexo A) antes de codificar |
| Inadimplência em planos por Pix | Perda de receita | Lembretes automáticos, tolerância configurável, bloqueio automático |
| Dependência de uma pessoa só (o coach) | Gargalo de atendimento | SLA visível, modelos de treino/dieta, respostas rápidas prontas, e o caminho de "assistente" já previsto na arquitetura |

---

## 17. Decisões pendentes com o coach

Lista resumida — a versão detalhada, pronta para conduzir a reunião, está no
`anexo-c-checklist-reuniao.md`.

1. **Montagem de treino:** só do zero, só por modelos, ou os dois? *(recomendação: os dois)*
2. **Técnicas avançadas:** quais ele efetivamente prescreve? (Anexo A)
3. **Vídeos:** só links do YouTube (Leandro Twin) ou também vídeos próprios dele?
4. **Registro de RIR/RPE:** entra ou é complexidade demais para o aluno?
5. **Prescrição dietética:** ele é nutricionista, tem nutricionista parceiro, ou atua com
   orientação alimentar? Define o texto legal e o CRN no relatório.
6. **Prazo de resposta** para a solicitação inicial (sugestão: 2 dias úteis).
7. **Dias e horários** fixos para as videochamadas.
8. **Preços** dos quatro planos e política de cancelamento/reembolso.
9. **Gateway de pagamento** preferido.
10. **Aceita alunos menores de 18 anos?**
11. **Marca:** nome, logo, cores, domínio.
12. **Periodicidade** de fotos e medidas de acompanhamento.
13. **Retenção de dados:** por quanto tempo guardar fotos após o fim do contrato.
14. **O que entra e o que fica de fora do MVP.**

---

## 18. Conclusão

O projeto é tecnicamente viável, com custo operacional baixo, e o diferencial competitivo está
exatamente onde deveria estar: **no método do coach, amplificado por automação**. As duas
decisões que mais impactam prazo e custo são (i) o conjunto de técnicas avançadas e (ii) o
tamanho do MVP — ambas dependem da reunião de definição.

A recomendação é **congelar um MVP enxuto, colocar no ar e trazer os primeiros 10 alunos
pagantes rapidamente**. O produto amadurece com uso real, e não em reunião. As Fases 2 e 3
existem para ser priorizadas com base no que os alunos e o coach descobrirem na prática.

---

*Documento preparado para apresentação e discussão. Todos os números de prazo e custo são
estimativas de planejamento e serão revisados após o congelamento do escopo.*
