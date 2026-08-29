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

1. **Triagem inteligente e viva.** O aluno declara restrições alimentares e lesões; o sistema
   cruza automaticamente com o banco de exercícios e de alimentos e entrega ao coach a
   prescrição **já sinalizada** — ele nunca prescreve às cegas. Quem declara lesão só recebe
   treino **depois** de falar com o coach, e a restrição é **revisada em prazo acordado**, para
   que o alerta nunca se apoie em informação vencida.

2. **Prescrição híbrida.** O coach pode montar tudo do zero **ou** partir de modelos
   próprios por objetivo, editando o que quiser. O sistema aprende com os modelos dele, não
   com um algoritmo genérico.

3. **Plano que funciona em qualquer academia.** Cada exercício tem um titular e **dois
   substitutos equivalentes**: se o aparelho não existe ali ou está ocupado, o aluno troca sem
   sair do protocolo e sem esperar resposta.

4. **Execução medida, não declarada.** O aluno registra carga série a série e adesão
   alimentar refeição a refeição. Isso vira, sem trabalho manual, um relatório profissional
   de evolução (composição corporal, adesão, progressão de carga).

5. **Ritual semanal.** Videochamada de 30 minutos com relatório na tela. O acompanhamento
   deixa de ser "manda no WhatsApp" e vira consultoria com evidência.

6. **Vagas limitadas e fila de espera.** O coach define quantos alunos aceita; lotado, o
   interessado entra numa fila com posição visível. Protege a qualidade do atendimento e cria
   escassez real.

**O acompanhamento começa gratuito.** Nada de pagamento entra na primeira versão — isso liberou
2 a 3 semanas de cronograma, realocadas para engenharia de qualidade e confiabilidade
(seção 14). Cobrança fica como planejamento da Fase 2, para quando houver demanda.

**Prazo estimado do MVP:** 10 a 14 semanas após o congelamento do escopo.
**Custo operacional estimado:** R$ 3 a R$ 15 por mês no início, lançando como aplicativo
instalável pelo navegador (PWA); cerca de R$ 190/mês quando o volume justificar backup
gerenciado e publicação nas lojas. Detalhamento e ressalvas na seção 17.

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
- Resultados de alunos (fotos antes/depois **somente com autorização escrita** — ver seção 12)
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
registrado** do termo de consentimento específico para foto corporal (seção 12).

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
Abre com a pergunta que muda o fluxo: **"Você possui alguma lesão, dor recorrente ou limitação
de movimento?"** — Sim / Não. Quem responde **sim** detalha região, histórico, dor de 0 a 10,
tratamento em curso, liberação médica e laudo opcional, e tem a ficha marcada com **contato
prévio obrigatório** (todo o fluxo está na seção 6). Em seguida, para todos: cirurgias, hérnia
de disco, hipertensão, diabetes, gestação, uso de medicamentos e exercícios que já sabe que não
consegue executar.

**Etapa 8 — Rotina**
Dias e horários disponíveis para treinar, local de treino (academia completa / academia
simples / casa), quem cozinha, orçamento alimentar aproximado, sono, nível de estresse,
consumo de álcool.

**Etapa 9 — Consentimentos e envio**
Aceite da Política de Privacidade e dos Termos de Uso, aceite específico para dados de saúde,
aceite (opcional e separado) para uso de imagem em divulgação. Botão **"ENVIAR PARA O
AZAMBUJA"**.

### 3.3 Confirmação e SLA

Quem declarou lesão vê, já nessa tela, o aviso de que **o Azambuja falará com ele antes de
montar o treino**, e pode escolher um horário na agenda ali mesmo.

Assim que envia, o aluno vê uma tela de confirmação com o **prazo de resposta do coach**
(parâmetro configurável — sugestão: até 2 dias úteis) e recebe o mesmo prazo por e-mail e
por WhatsApp. Se o prazo estourar, o sistema avisa o coach automaticamente.

### 3.4 Aprovação e liberação

1. O coach analisa a ficha na fila de solicitações. Fichas com lesão declarada vêm com
   **selo vermelho de contato obrigatório**.

2. Aprova (ou recusa com justificativa, ou pede complemento de informação).
3. Aprovado → conta criada e acesso ao app liberado. *(No MVP o acompanhamento é gratuito;
   quando houver cobrança, é aqui que entra o pagamento — seção 9.)*

4. Coach notificado para montar o protocolo.

5. **Se houver lesão declarada:** o coach faz o contato prévio e registra a conversa, a
   conduta e o prazo de revisão acordado. O sistema não libera a publicação do treino antes
   disso (seção 6.3).

6. Coach publica treino + dieta → aluno é notificado ("Seu protocolo chegou!").

### 3.5 Uso diário

- **Hoje:** tela inicial com o treino do dia e as refeições do dia.
- **Treino:** menus por grupo muscular → exercícios → séries, carga, técnica.
- **Dieta:** menus por refeição → opções → marcação do que comeu → contador e gráfico.
- **Evolução:** peso, medidas e fotos periódicas.
- **Fale com o Azambuja:** canal de mensagens.
- **Minha call:** agendamento e link da videochamada semanal.

---

### 3.6 Controle de vagas e fila de espera

Com o acompanhamento gratuito no início, o gargalo deixa de ser o preço e passa a ser **o tempo
do coach**. Sem controle, a divulgação funciona bem demais: chegam 60 inscrições, ele não
responde no prazo prometido, e a primeira impressão do produto é de abandono.

Por isso:

- O coach define **quantas vagas** aceita (número editável a qualquer momento).
- Com vagas abertas, o botão é **"Quero ser aluno"**.
- Lotado, o mesmo botão vira **"Entrar na fila de espera"**, com posição visível: *"você é o
  12º da fila"*.

- Quando abre vaga, o primeiro da fila é avisado por e-mail e WhatsApp e tem **prazo para
  confirmar** antes de a vez passar adiante.

- O coach vê a fila no painel e pode puxar alguém para frente, se quiser.

> Além de proteger a qualidade do atendimento, a fila cria escassez real — o que ajuda
> exatamente no momento em que ele decidir passar a cobrar.

### 3.7 Situações do dia a dia que precisam de resposta definida

Casos que ocorrem em qualquer operação de coaching e que, sem regra escrita, viram improviso:

| Situação | Como o sistema trata |
|---|---|
| **Aluno pausa** (férias, viagem, lesão longa) | Conta congelada, sem perder histórico. Não recebe cobrança de revisão nem lembrete de treino. Volta de onde parou |
| **Aluno não treinou no dia** | O treino **não vence**: fica pendente e pode ser executado depois, com a data real registrada. A adesão conta a sessão como realizada fora do dia, e não como falha — mas o relatório mostra a diferença |
| **Aluno sai** | Conta arquivada, dados retidos pelo prazo da política e depois excluídos. Se voltar, o histórico é recuperado |
| **Coach de férias ou doente** | Ele ativa o **modo ausência**: o prazo de resposta é suspenso, o aluno vê o aviso e a data de retorno, e novas inscrições pausam |
| **Aluno troca de celular** | Login em qualquer aparelho; tudo está no servidor. Recuperação de acesso por e-mail, com verificação |
| **O app quebra** | Canal de **suporte técnico separado** do "Fale com o Azambuja" — o coach não deve receber, nem tentar resolver, problema de software |

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
| **Grupo de equivalência** | Exercícios que substituem este quando falta equipamento (ver 4.4) |
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

### 4.4 Titular e substitutos — três opções para cada exercício

Para cada exercício prescrito, o coach define **no mínimo três opções**, em ordem:

1. **Titular** — o exercício que ele quer que o aluno faça.
2. **Substituto A** e **Substituto B** — equivalentes, para quando a academia não tem o
   equipamento, o aparelho está ocupado ou está quebrado.

Isso resolve um problema diário e real: o aluno chega na academia, aquela máquina não existe
ali, e ele improvisa sozinho (saindo do plano) ou simplesmente pula o exercício. Com titular e
substitutos, **o protocolo continua válido em qualquer academia**, sem o aluno ter que
adivinhar nem esperar resposta do coach.

**Para o aluno:** o titular aparece em destaque. Abaixo, o botão *"Não tenho esse aparelho"*
abre as duas alternativas, cada uma com seu próprio vídeo e descrição. Ele marca qual executou
e o registro guarda a variação — não apenas "fez peito", mas *o que* fez.

**Três implicações que precisam ser tratadas, ou a regra vira um peso:**

1. **O trabalho de montagem triplicaria.** Exigir três opções por exercício, digitadas uma a
   uma, tornaria a prescrição insustentável. A solução é criar **grupos de equivalência** no
   banco de exercícios: o coach cadastra **uma vez** que supino reto com barra, supino com
   halteres e supino na máquina são equivalentes. Ao montar, ele escolhe o titular e o sistema
   já sugere os dois substitutos, que ele confirma ou troca em um clique. **Sem isso, a regra
   não se sustenta na prática** — por isso o grupo de equivalência entra como item do MVP.

2. **A progressão de carga passa a ser por variação.** Não se compara carga de supino com
   barra e de supino na máquina — seriam duas curvas misturadas num gráfico sem sentido. O
   relatório passa a mostrar a progressão **por variação executada** e, junto, o
   **percentual de sessões feitas no titular**. Se o aluno faz sempre o substituto, o coach
   descobre e provavelmente troca o titular — informação que hoje ele não teria.

3. **O alerta de restrição roda nas três opções.** De nada adianta o titular ser seguro se o
   substituto B agride o ombro lesionado. A verificação de contraindicação vale para titular e
   substitutos, igualmente.

**Validação ao publicar:** o sistema exige as três opções. Se o coach considerar um exercício
insubstituível, ele dispensa a exigência com justificativa registrada.

> **Melhoria sugerida — inventário da academia do aluno.** No cadastro o aluno já informa onde
> treina. Vale deixá-lo marcar **quais equipamentos a academia dele tem** (lista curta, com
> foto). Com isso, o app ordena as opções mostrando primeiro o que ele consegue executar, e o
> coach vê, no momento da prescrição, se o titular sequer existe naquela academia. Custo baixo
> de implementação, ganho alto de aderência. **A decidir.**

### 4.5 Tela do aluno — execução do treino

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
4. Se não tiver o aparelho do titular, abre as opções substitutas (ver 4.4) e registra qual
   executou.

5. Se sentir dor, marca o exercício e informa a intensidade em uma **escala de 0 a 10** — isso
   dispara alerta imediato ao coach (ver 6.5), sem esperar a call da semana.

6. Ao terminar, marca **"Treino concluído"** → gera o registro da sessão.

**Recurso de retenção:** o app funciona **offline** durante o treino (a academia costuma ter
sinal ruim) e sincroniza quando a conexão voltar. Isso é um diferencial prático enorme e
raramente bem resolvido pelos concorrentes.

### 4.6 Técnicas avançadas — ponto em aberto

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

## 6. Gestão de restrições e lesões

### 6.1 Por que isto é um módulo, e não um campo de cadastro

Restrição não é dado estático. Um ombro lesionado melhora, um exame de intolerância muda o
diagnóstico, uma gestação começa e termina, uma dor nova aparece. Se o sistema tratar a
restrição como algo preenchido uma única vez na inscrição, em três meses o coach estará
prescrevendo com base em informação vencida — e o alerta automático, que é um dos principais
diferenciais do produto, perde o valor.

Por isso restrição passa a ter **ciclo de vida**: é declarada, gera contato, é revisada em
prazo acordado, muda de status e pode ser encerrada.

### 6.2 No cadastro: a pergunta que muda o fluxo

Na etapa de restrições, uma pergunta objetiva:

> **"Você possui alguma lesão, dor recorrente ou limitação de movimento?"** — Sim / Não

- **Não** → segue o fluxo normal de inscrição.
- **Sim** → abre o detalhamento e a ficha é marcada com **contato prévio obrigatório**.

O detalhamento pedido a quem marcou "sim":

| Campo | Para quê |
|---|---|
| Região afetada | Cruza com as tags de contraindicação do banco de exercícios |
| O que aconteceu e quando | Contexto clínico para o coach |
| Está em tratamento? Com qual profissional? | Define se há conduta externa a respeitar |
| **Dor atual, de 0 a 10** | Linha de base para medir evolução |
| Tem liberação médica para treinar? | Sim / Não / Não sei — define se o coach exige antes de prescrever |
| Movimentos que já sabe que não consegue | Entrada direta para o alerta automático |
| Laudo, exame ou atestado | Upload **opcional** |

O laudo é dado de saúde e recebe **o mesmo tratamento reforçado das fotos corporais**:
área privada, link temporário, auditoria de acesso e retenção definida (seção 12).

A mesma lógica vale para restrições alimentares clínicas: celíaco, alergia diagnosticada ou
intolerância confirmada abrem campo para data do diagnóstico e exame, porque também precisarão
de revisão.

### 6.3 Contato obrigatório antes de montar o treino

Quem declarou lesão **não recebe treino antes de falar com o coach**. Isso não é uma sugestão
do sistema, é uma trava:

1. A ficha entra na fila de solicitações com **selo vermelho: "Contato obrigatório antes da
   prescrição"**, com o resumo da lesão visível já na listagem.

2. O sistema **impede a publicação do treino** enquanto o contato não for registrado.
3. Ao registrar, o coach preenche: data, canal (videochamada, telefone, áudio), resumo do que
   foi apurado, **conduta definida** e a **periodicidade de revisão acordada com o aluno**.

4. Se ele julgar o contato dispensável em um caso específico, dispensa com justificativa — e a
   dispensa fica registrada em log.

O aluno é avisado no momento certo: *"O Azambuja vai falar com você antes de montar seu treino,
porque você relatou uma lesão."* — e já pode escolher um horário na agenda dele, o que elimina
o vai-e-vem de mensagens.

> **Isso protege o coach.** Fica documentado que houve avaliação individual antes de prescrever
> exercício a um aluno lesionado. Em uma eventual discussão sobre responsabilidade
> profissional, esse registro é exatamente o que se pede.

### 6.4 Revisão periódica — prazo acordado, conforme tipo e gravidade

No registro do contato, coach e aluno **acordam o prazo de revisão**. Os prazos são definidos
pelo coach; a tabela abaixo serve apenas como ponto de partida para a discussão:

| Situação | Revisão sugerida |
|---|---|
| Lesão aguda, em tratamento ou pós-operatório | 15 dias |
| Lesão em recuperação, dor moderada | 30 dias |
| Limitação crônica estável (ex.: desgaste antigo de joelho) | 60 a 90 dias |
| Restrição alimentar clínica (celíaco, alergia, intolerância) | 6 meses, ou a cada novo exame |
| Preferência alimentar (vegetariano, vegano) | 6 a 12 meses |

**Somente alunos com restrição entram nesse ciclo.** Quem não declarou nada nunca vê essa tela,
nunca recebe esse lembrete e não tem trabalho adicional nenhum.

Como funciona na prática:

- **Semáforo no painel do coach:** verde (revisada em dia), amarelo (vence em até 7 dias),
  vermelho (vencida). Ele bate o olho e sabe quem precisa de atenção.

- **Lembrete automático** para os dois, antes do vencimento.
- **Tela de revisão curta**, que o aluno responde em menos de um minuto: melhorou / igual /
  piorou, dor atual de 0 a 10, mudou algo no tratamento, novo laudo se houver.

- **Piora dispara alerta imediato** ao coach, com sugestão de antecipar o contato — não espera
  o vencimento nem a call da semana.

- **Enquanto a revisão está vencida**, o sistema bloqueia a *renovação automática por modelo* e
  exige a revisão antes. O coach continua podendo publicar manualmente, com registro. O aluno
  **não** perde acesso ao treino atual: ele continua treinando normalmente; o que trava é
  prescrever protocolo novo com dado velho.

- Cada revisão vira registro no histórico do aluno e alimenta o **gráfico de dor** no relatório
  de evolução — que passa a mostrar, lado a lado, evolução de carga e evolução da dor.

### 6.5 Dor relatada no treino fecha o ciclo

O campo de observação por exercício ganha uma **escala de dor de 0 a 10** e um marcador
"senti dor". Quando o aluno marca:

1. **Alerta imediato ao coach**, sem esperar a call.
2. O exercício fica sinalizado na ficha daquele aluno.
3. Se a dor é na região de uma restrição já declarada → o sistema sugere **antecipar a
   revisão**.

4. Se é uma região nova → sugere **abrir uma nova restrição**, com o mesmo fluxo de contato.

É isto que fecha o ciclo entre as três coisas: o que o aluno declarou na inscrição, o que é
revisado periodicamente, e o que realmente acontece dentro da academia.

### 6.6 O que muda no alerta automático

O alerta de contraindicação passa a considerar **status e data** da restrição, não apenas a
existência dela. "Lesão de ombro, moderada, revisada há 12 dias" é uma informação diferente de
"lesão de ombro declarada há 8 meses, nunca revisada" — e o coach precisa ver essa diferença no
momento em que prescreve.

Restrição com revisão vencida aparece com aviso próprio:
*"⚠️ Esta restrição está sem revisão há X dias. O dado pode estar desatualizado."*

---

## 7. Módulo de evolução e relatórios

### 7.1 O que o aluno registra periodicamente

| Dado | Frequência sugerida |
|---|---|
| Peso corporal | Diário ou semanal (definido pelo coach) |
| Circunferências (cintura, quadril, braço, coxa, panturrilha, tórax) | Quinzenal |
| Fotos de acompanhamento (mesmos 3 ângulos, mesma luz, mesma hora) | Quinzenal ou mensal |
| Dobras cutâneas / bioimpedância | Quando houver |
| Sono, energia, dores, apetite, humor | Semanal (check-in rápido) |
| **Revisão de restrição ou lesão** | Prazo acordado com o coach, conforme gravidade (seção 6.4) |

### 7.2 Relatório profissional

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
- **Evolução da dor** (escala 0 a 10) ao lado da evolução de carga, para quem tem lesão
- Observações do aluno no período (dores, dificuldades)
- **Espaço para o parecer do coach** — o texto dele, que é o que dá valor ao documento
- Rodapé com marca, CREF/CRN e data de emissão

Esse relatório é o roteiro da videochamada semanal e, ao mesmo tempo, o principal argumento
de renovação do plano: o aluno **vê** o que comprou.

---

## 8. Comunicação com o coach

### 8.1 Canal "Fale com o Azambuja"

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

### 8.2 Videochamada semanal

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

## 9. Pagamentos e planos

> ### 🕐 Fora do MVP
>
> **O acompanhamento começa gratuito.** Nada de pagamento entra na primeira versão: sem planos,
> sem gateway, sem cobrança, sem bloqueio por inadimplência. Isso retira 2 a 3 semanas do
> cronograma, que foram realocadas para a seção 14 (qualidade e confiabilidade).
>
> O modelo de dados já nasce preparado para receber cobrança, e esta seção fica registrada como
> **planejamento da Fase 2**, para quando houver demanda que justifique cobrar. Nada aqui está
> decidido.
>
> **Gratuito não reduz nenhuma exigência:** LGPD, consentimento, proteção das fotos e
> responsabilidade profissional valem igual, cobrando ou não.

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

## 10. Painel administrativo do coach

Tudo em uma única interface web (e também acessível pelo celular):

1. **Início** — solicitações novas, **contatos prévios pendentes**, **revisões de restrição
   vencidas ou vencendo (semáforo)**, **dores relatadas no treino**, mensagens vencendo hoje,
   calls do dia, alunos sem registrar treino há X dias (alerta de abandono).

2. **Solicitações e fila de espera** — vagas abertas, fila com posições, e a fila de leads com ficha completa, fotos e restrições destacadas, com
   **selo vermelho nas que exigem contato antes da prescrição**; aprovar, recusar, pedir
   complemento, registrar o contato prévio.

3. **Alunos** — lista com busca e filtros (objetivo, nível, plano, adesão, status); ficha
   individual com histórico completo.

4. **Prescrição** — montagem de treino e dieta, modelos, publicação.
5. **Bancos** — exercícios (com os grupos de equivalência) e alimentos.
6. **Restrições** — todos os alunos com lesão ou restrição, ordenados por vencimento da
   revisão, com histórico de cada revisão e da dor relatada.

7. **Mensagens** — caixa de entrada com SLA.
8. **Agenda** — disponibilidade e calls.
9. **Financeiro** — planos, cobranças, inadimplência.
10. **Relatórios** — por aluno e agregados.
11. **Configurações** — marca, textos da landing page, prazos, notificações.

---

## 11. Notificações

Push (celular) e e-mail, todas configuráveis pelo coach e pelo aluno:

- Lembrete de treino no horário que o aluno escolheu
- Lembrete de registrar as refeições
- "Seu protocolo novo chegou"
- "O Azambuja respondeu você"
- Lembrete de call (24h e 1h antes)
- Lembrete de pesagem/medidas/fotos
- **Revisão de lesão ou restrição vencendo** (para o aluno e para o coach)
- Vaga aberta, para quem está na fila de espera
- Aviso de modo ausência do coach
- Para o coach: nova solicitação, **ficha aguardando contato prévio**, **dor relatada no
  treino**, **revisão de restrição vencida**, mensagem próxima do prazo, aluno sumido,
  pagamento falhou

---

## 12. LGPD, segurança e conformidade

Esta é a seção mais sensível do projeto e precisa ser levada a sério desde o primeiro dia:
o projeto trata **dados pessoais sensíveis** — dados de saúde e imagens corporais.

### 12.1 Enquadramento legal

- Dados sobre saúde e condição física são **dados pessoais sensíveis** (art. 5º, II da LGPD).
  Fotos corporais para avaliação física, no contexto deste serviço, devem ser tratadas com o
  mesmo rigor.

- A base legal adequada é o **consentimento específico e destacado** (art. 11, I) — o aluno
  precisa consentir de forma separada, para finalidades específicas, e pode revogar.

- **O coach é o Controlador** dos dados; quem desenvolve e opera a infraestrutura atua como
  **Operador**. Isso precisa estar num contrato escrito entre as partes.

### 12.2 Medidas concretas que serão implementadas

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
- Log de auditoria de todas as ações administrativas, com retenção própria e separada dos
  logs de erro.

- **Logs de erro sem nenhum dado pessoal ou de saúde** — filtro obrigatório antes do envio,
  gravação de sessão desligada, retenção de 30 a 90 dias (detalhamento na seção 13.5).

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

### 12.3 Responsabilidade profissional

- O app é uma ferramenta de trabalho do profissional habilitado; a prescrição é sempre dele.
- Deve constar de forma visível o **CREF** (e o **CRN** do responsável pela prescrição
  dietética — vale confirmar como o coach opera esse ponto hoje: se ele é nutricionista, se
  trabalha com nutricionista parceiro, ou se atua com orientação alimentar dentro do escopo do
  profissional de educação física. **Item obrigatório da pauta da reunião.**).

- Avisos de "não é serviço de emergência" e recomendação de avaliação médica prévia.
- Menores de 18 anos: exigem consentimento do responsável — definir se serão aceitos.

---

## 13. Arquitetura técnica

### 13.1 É possível construir isso de forma segura, funcional e leve?

**Sim.** E a maneira de garantir isso não é escolher a tecnologia "mais moderna", e sim
escolher uma arquitetura que evite os três erros que afundam projetos deste tipo:

1. **Manter dois códigos separados para iOS e Android.** Dobra custo e tempo. Solução:
   um único código para os dois sistemas.

2. **Construir servidor, autenticação, armazenamento e permissões do zero.** É onde nascem as
   falhas de segurança. Solução: usar uma base gerenciada, madura e auditada, e escrever apenas
   a regra de negócio do coach.

3. **Colocar tudo no MVP.** Solução: fases (seção 16).

### 13.2 Stack recomendada

| Camada | Tecnologia | Por quê |
|---|---|---|
| **App iOS + Android** | React Native com Expo | Um único código para as duas lojas. Atualizações de correção podem ser enviadas sem passar por revisão da loja (OTA). Funciona offline |
| **Site + landing + painel do coach** | Next.js (React) | Mesma linguagem do app (compartilha regras e componentes), páginas muito rápidas e bem indexadas no Google — importante para a captação |
| **Backend, banco e autenticação** | Supabase (PostgreSQL gerenciado) na região de São Paulo | Banco relacional sério, autenticação pronta, armazenamento de arquivos, **segurança por linha (RLS)** e API automática. Reduz meses de trabalho e é onde a segurança fica mais forte |
| **Regras de negócio sensíveis** | Edge Functions (TypeScript) | Cálculo de macros, geração de relatório, integrações, webhooks de pagamento — nada sensível roda no celular |
| **Armazenamento de fotos** | Supabase Storage (bucket privado + URLs assinadas) | Ver seção 12.2 |
| **Pagamentos** | Asaas / Mercado Pago / Pagar.me / Stripe | Pix + cartão + assinatura recorrente |
| **E-mail transacional** | Resend ou Amazon SES | Entregabilidade e registro de envio |
| **Push** | Expo Push Notifications | Nativo do ecossistema, custo zero |
| **Relatório PDF** | Geração no servidor | PDF idêntico para todo mundo, com a marca do coach |
| **Hospedagem web** | Cloudflare Pages | Deploy automático, HTTPS, CDN global, banda ilimitada e **uso comercial permitido no plano gratuito** (o plano gratuito da Vercel proíbe uso comercial) |
| **Erros e monitoramento** | Sentry | Descobrir o problema antes do aluno reclamar |
| **Organização do código** | Monorepo (Turborepo) | App, site e regras compartilhadas no mesmo repositório, sem duplicação |

**Alternativa considerada:** backend próprio em NestJS + PostgreSQL. Dá mais controle, mas
acrescenta de 4 a 6 semanas ao MVP e transfere para nós a responsabilidade de construir
autenticação e permissões — justamente a parte onde erros custam caro. **Recomendação: começar
com Supabase.** Como os dados ficam em PostgreSQL puro, migrar para um backend próprio no
futuro é possível sem perder nada.

### 13.3 Estrutura do repositório

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

### 13.4 "Leve" na prática

- App abaixo de ~30 MB, abre em menos de 2 segundos.
- Telas de treino e dieta **funcionam offline** e sincronizam depois.
- Imagens processadas e comprimidas no envio (a foto de 8 MB do celular vira ~400 KB sem perda
  visual relevante).

- Listas grandes (alimentos, exercícios) carregadas por partes, com busca instantânea local.
- Sem dependências pesadas desnecessárias.

---

### 13.5 Observabilidade — o que acontece quando o app trava

Sim, tudo o que quebra gera registro. Isso não é detalhe técnico: sem log, um problema só é
descoberto quando um aluno reclama — e a maioria não reclama, simplesmente para de usar.

**Três tipos de registro, com finalidades diferentes:**

| Tipo | O que registra | Para quem |
|---|---|---|
| **Erro e travamento** | Crash do app, tela branca, botão que não responde, erro de rede | Para quem mantém o sistema |
| **Erro de servidor** | Falha ao gerar relatório, webhook de pagamento que não chegou, e-mail que não saiu | Para quem mantém o sistema |
| **Auditoria** | Quem acessou qual foto, quais ações administrativas foram feitas | Para o coach e para conformidade com a LGPD (seção 12.2) |

Os dois primeiros são operacionais e têm vida curta. O terceiro é registro legal, tem outra
retenção e **nunca** é apagado junto com os demais.

**O que fica registrado em um travamento**

Tela em que o aluno estava, ação que ele executou, versão do app, modelo do aparelho, versão do
sistema operacional, e o ponto exato do código onde quebrou. Erros idênticos são agrupados
automaticamente: em vez de 40 avisos soltos, aparece *"este erro ocorreu 40 vezes, com 12
alunos, desde a versão 1.4"* — o que já indica se é um caso isolado ou algo que precisa de
correção urgente.

**Travamento sem internet também é registrado.** O registro fica guardado no aparelho e sobe
quando a conexão voltar. Isso importa porque boa parte do uso acontece dentro da academia, com
sinal ruim — exatamente onde os problemas aparecem.

**O que o aluno vê**

Nunca uma tela técnica. Vê uma mensagem clara — *"Não conseguimos salvar seu treino agora. Seus
dados estão guardados no aparelho e serão enviados assim que a conexão voltar."* — com um botão
opcional de "contar o que aconteceu" e um **código curto de referência** que ele pode repassar
ao coach.

**O que o coach vê**

Log técnico não é problema dele. No painel aparece apenas o que exige ação: *"3 alunos
relataram erro ao registrar treino hoje"*. O destinatário do log é quem mantém o sistema, que
recebe **alerta imediato** por e-mail quando surge um erro novo ou quando um erro conhecido
dispara em volume. Log que ninguém lê no momento certo é arqueologia, não monitoramento.

**Meta objetiva:** manter **acima de 99,5% de sessões sem travamento**. É uma métrica medida
automaticamente e serve de critério de qualidade a cada nova versão.

> ### ⚠️ O log não pode virar um vazamento
>
> Ferramentas de monitoramento capturam, por padrão, muito mais do que deveriam: conteúdo de
> formulário, corpo das requisições, e — no recurso de "gravação de sessão" — **a própria tela
> do aluno**. Em um aplicativo que trata peso, medidas, laudos e fotos de sunga e biquíni, isso
> transformaria a ferramenta de erro na maior porta de vazamento do sistema.
>
> Por isso, as regras abaixo são obrigatórias no projeto:
>
> - **Filtro antes do envio:** nenhum conteúdo de formulário, corpo de requisição, token,
>   documento ou imagem sai do aparelho junto com o erro.
> - **Nenhum dado de saúde no log.** Peso, medidas, restrições, laudos e dor ficam fora.
> - **Identificação só por código interno** do aluno — nunca nome, e-mail ou telefone.
> - **Gravação de sessão e captura de tela desligadas.** É o recurso mais tentador e o único que
>   conseguiria capturar uma foto corporal.
> - **Retenção curta:** 30 a 90 dias para log de erro, contra a retenção longa da auditoria.
> - A ferramenta de monitoramento é uma **operadora de dados** e precisa constar no contrato e
>   no registro de operações de tratamento (ROPA), como qualquer outro fornecedor.

**Ferramenta e custo.** A recomendação é **Sentry**, cujo plano gratuito (5 mil erros por mês)
atende com folga a fase inicial — já está contemplado no Nível 0 de custos, a R$ 0. Se o coach
preferir que **nenhum dado saia para fornecedor externo**, existe a alternativa de hospedar a
ferramenta na própria infraestrutura (Sentry self-hosted ou GlitchTip): elimina o terceiro, mas
acrescenta trabalho de operação e algum custo de servidor. **A decidir — item `B8`.**

## 14. Qualidade, confiabilidade e desempenho

Esta seção existe porque a minuta descrevia bem **o que** o app faz e mal **como se garante que
ele não quebra**. Aplicativo de excelência não é o que tem mais funcionalidade: é o que abre
rápido, não trava, não perde dado e não surpreende. Isso não acontece por capricho de quem
programa — acontece porque foi orçado, medido e verificado a cada versão.

### 14.1 Metas medíveis

Cada uma é acompanhada automaticamente e vira critério de aprovação de cada nova versão.

| Indicador | Meta | Como é medido |
|---|---|---|
| Sessões sem travamento | **acima de 99,5%** | Ferramenta de monitoramento (13.5) |
| Tempo até a primeira tela útil | **abaixo de 2 s** | Medição automática a cada versão |
| Resposta ao toque (abrir exercício, marcar refeição) | **abaixo de 400 ms** | Medição automática |
| Tamanho do aplicativo | **abaixo de 30 MB** | Verificado antes de publicar |
| Registro de treino perdido | **zero** | Reconciliação da fila offline |
| Disponibilidade do serviço | **99,5% ao mês** | Monitor externo, a cada minuto |
| Tempo para voltar ao ar após falha grave | **abaixo de 4 h** | Teste de restauração |
| Perda máxima de dados em desastre | **24 h** | Backup diário verificado |

### 14.2 Como isso é sustentado

**Três ambientes separados.** Desenvolvimento, **homologação** (cópia fiel da produção, com
dados fictícios — nunca dado real de aluno) e produção. Nada chega ao aluno sem passar por
homologação.

**Testes automatizados**, concentrados onde o erro é caro:

- **Cálculos:** macros, calorias, progressão de carga, percentual de adesão e cruzamento de
  restrições. São os números que o coach usa para decidir — um erro aqui passa despercebido por
  semanas e contamina todos os relatórios.

- **Fluxos críticos de ponta a ponta:** inscrição com foto e consentimento · publicação de
  treino com a trava de contato prévio · registro de treino offline e sincronização · registro
  de refeição · geração de relatório. Se algum quebrar, o produto para.

- **Regras de segurança:** teste automático que confirma que um aluno não consegue ler o dado de
  outro. Roda a cada mudança, porque é a falha mais grave possível neste projeto.

**Verificação automática antes de publicar.** Nenhuma versão vai ao ar sem a bateria de testes
passar, o tamanho do app estar dentro do orçamento e as medições de desempenho baterem a meta.

**Rollback em minutos.** Toda versão publicada pode ser revertida para a anterior sem esperar
revisão de loja — no PWA é imediato; no app de loja, por atualização remota. Além disso,
**atualização obrigatória** para o caso de bug crítico: o app se recusa a rodar em uma versão
sabidamente defeituosa.

### 14.3 Sincronização offline e conflito — a regra escrita

Este é o bug clássico de aplicativo de treino, e precisa de regra definida antes de existir
código. O cenário: o aluno registra o treino sem sinal na academia e, nesse meio-tempo, o coach
publica um protocolo novo.

**A regra:**

1. **O que o aluno executou nunca é sobrescrito.** Registro de execução é fato acontecido: entra
   como registro novo, jamais é substituído por dado vindo do servidor.

2. **A prescrição do coach é a autoridade.** Se ele publicou versão nova, ela vale a partir dali.
3. **Cada sessão fica vinculada à versão do protocolo que valia quando foi executada.** Assim o
   relatório continua correto: compara a carga contra a prescrição certa.

4. **O aluno é avisado, não corrigido:** *"Seu treino foi atualizado pelo Azambuja. O que você
   registrou hoje foi salvo."*

5. Se o mesmo aluno registrar em dois aparelhos, vale o registro mais recente por série, com o
   descartado preservado no histórico — nunca apagado em silêncio.

> **Decorrência:** treino e dieta passam a ser **versionados**. Cada publicação gera uma versão
> com data, e o histórico mostra o que estava valendo em cada semana. Isso também entrega ao
> coach a linha do tempo do aluno, útil na call e necessária como prontuário.

### 14.4 Fuso horário e a virada do dia

Parece detalhe e é fonte garantida de erro. Definições:

- Tudo é gravado em horário universal e exibido no fuso do aluno.
- **O "dia de treino" vira às 3h da manhã, no horário local do aluno.** Quem treina à noite e
  registra 00h30 ainda está registrando o dia anterior, como espera.

- O mesmo vale para o registro alimentar e para a contagem de adesão.

### 14.5 Backup e recuperação

- Backup diário automático do banco e dos arquivos, guardado em local separado da base
  principal.

- **Teste de restauração mensal**, com registro do resultado. Backup que nunca foi restaurado
  não é backup: é suposição.

- Objetivos declarados: perder no máximo **24 horas** de dados e voltar ao ar em até **4 horas**.

### 14.6 Acessibilidade e legibilidade — o app é usado na academia

O ambiente de uso é hostil: luz forte, tela suja, mão suada, pressa entre séries, às vezes uma
mão só. O desenho precisa considerar isso:

- **Contraste alto** e **modo escuro**, que é o que a maioria prefere em ambiente com espelho e
  luz direta.

- **Fonte que respeita o tamanho escolhido pelo aluno** no sistema — inclusive alunos mais
  velhos, com o texto bem maior.

- **Alvos de toque grandes** nos campos de carga e nas opções de refeição, que são o que mais se
  toca no dia a dia.

- Telas principais **operáveis com uma mão**.
- Compatibilidade com leitor de tela nos fluxos principais.
- Nada depende apenas de cor para comunicar — o gráfico de macros também traz número e rótulo.

### 14.7 Saber onde o aluno desiste

Além do log de erro, o app registra, **sem nenhum dado pessoal**, onde as pessoas abandonam:
quantos começam a inscrição e não terminam, em qual etapa param, quantos registram o primeiro
treino, quantos ainda registram na quarta semana. Sem isso não há como melhorar o produto — só
opinar sobre ele. Valem as mesmas regras de filtro da seção 13.5.

---

## 15. Modelo de dados (visão inicial)

Tabelas principais previstas — serve para dimensionar o trabalho, e será refinada:

| Tabela | Guarda |
|---|---|
| `coaches` | Dados do coach, marca, CREF/CRN, configurações, SLA |
| `leads` | Solicitações recebidas pela landing page e status |
| `students` | Alunos ativos, plano, datas |
| `student_profiles` | Anamnese: nível, objetivo, rotina, histórico |
| `dietary_restrictions` / `exercise_restrictions` | Restrições declaradas, com gravidade, status, dor inicial e data da próxima revisão |
| `restriction_reviews` | Histórico de cada revisão: data, evolução, dor, conduta, novo laudo |
| `pre_prescription_contacts` | Registro do contato obrigatório antes da prescrição, ou a dispensa justificada |
| `pain_reports` | Dor relatada durante o treino: exercício, região, intensidade 0-10 |
| `medical_documents` | Laudos, exames e atestados (metadados; arquivo em área privada) |
| `consents` | Cada aceite de LGPD: tipo, versão do texto, data, IP |
| `body_photos` | Fotos de avaliação (metadados; o arquivo fica no bucket privado) |
| `body_measurements` | Peso, circunferências, dobras, bioimpedância |
| `exercises` | Banco de exercícios do coach, com tags e vídeo |
| `exercise_equivalence_groups` | Grupos de substitutos: quais exercícios trocam entre si |
| `student_equipment` | Inventário de equipamentos da academia do aluno *(se adotado)* |
| `workout_templates` / `workout_template_items` | Modelos de treino por objetivo |
| `workout_plans` / `workout_days` / `workout_exercises` | Treino prescrito ao aluno |
| `workout_exercise_options` | Titular e substitutos de cada exercício prescrito, em ordem |
| `workout_sessions` / `set_logs` | Execução: **qual variação foi feita**, carga e repetições por série, RIR, técnica |
| `advanced_techniques` | Catálogo de técnicas (após decisão do coach) |
| `foods` | Base TACO/TBCA/IBGE + alimentos do coach, com tags |
| `recipes` / `recipe_items` | Preparações do coach |
| `diet_plans` / `meals` / `meal_options` / `meal_option_items` | Dieta prescrita (3+ opções por refeição) |
| `food_logs` | O que o aluno realmente comeu |
| `messages` / `message_threads` | Canal com o coach, com prazo de SLA |
| `appointments` | Videochamadas semanais |
| `reports` | Relatórios gerados |
| `subscriptions` / `payments` | Planos e cobranças *(estrutura preparada; sem uso no MVP)* |
| `waitlist` | Fila de espera, com posição, data de entrada e prazo de confirmação |
| `student_status_changes` | Pausas, arquivamentos e retornos, com motivo e data |
| `protocol_versions` | Versões publicadas de treino e dieta, com a data de vigência |
| `sync_queue` | Registros feitos offline aguardando envio, e o que foi descartado por conflito |
| `audit_logs` | Auditoria de acessos e ações administrativas |
| `notifications` | Fila e histórico de envios |

---

## 16. Fases de entrega

### Fase 0 — Definição *(1 a 2 semanas)*
Reunião com o coach usando o `anexo-c-checklist-reuniao.md`; decisões pendentes fechadas;
identidade visual; escolha do gateway de pagamento; escopo do MVP congelado. **É onde estamos.**

### Fase 1 — MVP *(10 a 14 semanas)*
O suficiente para o coach **operar e faturar de verdade**:

- Site + landing page com o link de divulgação e o botão "Quero ser aluno"
- Formulário de inscrição completo, com fotos e consentimentos LGPD
- Fila de solicitações e aprovação pelo coach
- **Controle de vagas e fila de espera**
- Banco de exercícios (pré-carregado + editável) e banco de alimentos (TACO/TBCA/IBGE)
- Montagem de treino do zero + modelos
- Montagem de dieta com 3+ opções por refeição
- Alertas automáticos de restrição (treino e dieta), sensíveis ao status e à data da restrição
- Pergunta de lesão no cadastro, **trava de contato prévio** e registro da conversa
- **Revisão periódica de restrições** com prazo acordado, semáforo e lembretes
- **Titular + 2 substitutos por exercício**, com grupos de equivalência no banco
- Registro de dor 0-10 no treino, com alerta imediato ao coach
- App do aluno: treino (carga por série, vídeo, descrição, offline) e dieta (marcação,
  contador de calorias, gráfico de macros)

- Registro de peso, medidas e fotos
- Relatório de evolução em PDF
- Canal "Fale com o Azambuja" com a regra das 18h
- Agenda e link da call semanal
- Notificações push essenciais
- Monitoramento de erros e travamentos, com filtro de dados pessoais e alerta imediato
- Painel do coach, com modo ausência
- **Engenharia de qualidade (seção 14):** ambiente de homologação, testes automatizados dos
  cálculos e dos fluxos críticos, verificação antes de publicar, rollback, teste de restauração
  de backup e medição de desempenho por versão

- Regra de conflito de sincronização offline e versionamento de protocolo
- Acessibilidade: contraste, modo escuro, fonte ajustável, alvos de toque grandes
- Pausa e arquivamento de aluno, canal de suporte técnico separado
- **Rotina própria de backup diário** (obrigatória: o plano gratuito do banco não faz backup)
- Lançamento como **PWA** — aplicativo instalável pela tela de início, sem taxa de loja e sem
  espera por revisão. Publicação na App Store e no Google Play fica para a Fase 2 (ver 15.4)

> **Nota de cronograma:** a retirada do módulo de pagamento (−2 a 3 semanas) e a entrada da
> engenharia de qualidade (+2 a 3 semanas) se compensam. O prazo do MVP permanece em **10 a 14
> semanas** — o que muda é *onde* o esforço é gasto: menos funcionalidade de cobrança, mais
> garantia de que nada quebra.

### Fase 2 — Consolidação *(4 a 6 semanas)*
**Módulo de pagamento** (planos, Pix e cartão), quando houver demanda que justifique cobrar ·
**Publicação na App Store e no Google Play**, avaliando antes a taxa de loja (9.1) · Técnicas
avançadas (conforme a decisão do coach) · **Inventário de equipamentos da academia do aluno** · Relatórios comparativos e
agregados ·
Chat em tempo real · Programa de indicação ("indique e ganhe") · Metas e conquistas ·
Integração com Apple Health / Google Fit (passos, peso da balança inteligente) ·
Exportações para o coach.

### Fase 3 — Escala *(a definir)*
Múltiplos coaches/assistentes · Loja de e-books e programas avulsos · Automação de marketing ·
Aplicativo de coach dedicado · Nota fiscal automática · Área de comunidade.

---

## 17. Custos estimados

> **Correção em relação à primeira estimativa.** A versão inicial deste documento orçava
> R$ 290 a R$ 400 por mês. Isso estava conservador demais para a fase inicial: dois itens
> daquela lista não são necessários no começo. **O custo real para começar fica entre R$ 5 e
> R$ 15 por mês.** O detalhamento abaixo mostra por quê e quando cada custo passa a existir.

### 17.1 Nível 0 — Validação (do lançamento até ~50 alunos)

| Item | Serviço | Custo/mês |
|---|---|---|
| Banco de dados, login e arquivos | Supabase Free — 500 MB de banco, 1 GB de arquivos, 50 mil usuários/mês | **R$ 0** |
| Hospedagem do site e do painel | Cloudflare Pages Free — banda ilimitada e **uso comercial permitido** | **R$ 0** |
| E-mail transacional | Resend Free — 3.000 e-mails/mês | **R$ 0** |
| E-mail profissional no domínio | Zoho Mail Free, ou redirecionamento do próprio domínio | **R$ 0** |
| Backup diário | Rotina própria para Cloudflare R2 (10 GB gratuitos) | **R$ 0** |
| Monitoramento de erros | Sentry Free | **R$ 0** |
| Videochamada | Google Meet gratuito — chamadas 1 a 1 sem limite prático de tempo | **R$ 0** |
| Domínio `.com.br` | Registro.br, ~R$ 40/ano | **~R$ 3** |
| **Total** | | **~R$ 3 a R$ 15** |

**O que eu errei na primeira estimativa:**

- **Vercel Pro (R$ 110/mês) — desnecessário.** O plano gratuito da Vercel **proíbe uso
  comercial**, o que forçaria o plano pago no dia em que o primeiro Pix entrasse. O
  Cloudflare Pages faz o mesmo trabalho, com banda ilimitada, e **permite uso comercial no
  plano gratuito**. Trocando o fornecedor, o custo some.

- **Google Workspace (R$ 35/mês) — desnecessário.** Era para o e-mail profissional e para
  o Meet. O Zoho Mail gratuito resolve o e-mail no domínio próprio, e o Google Meet gratuito
  já permite chamadas de 1 a 1 sem o limite de 60 minutos (que só se aplica a reuniões com
  três ou mais pessoas). Como a call é sempre coach + aluno, o plano pago não acrescenta nada.

**Ressalvas honestas do Nível 0 — o que se paga por usar o gratuito:**

1. **O Supabase gratuito não faz backup automático.** Como tratamos dado sensível, isso não é
   aceitável como está: a rotina própria de backup diário (para o Cloudflare R2 gratuito) passa
   a ser **item obrigatório do MVP**, não opcional. É trabalho de desenvolvimento, não custo
   mensal.

2. **Projeto gratuito é pausado após 7 dias sem nenhum acesso ao banco.** Irrelevante com
   alunos ativos usando o app todo dia; relevante apenas na janela entre terminar o
   desenvolvimento e entrar o primeiro aluno — resolvido com uma chamada automática diária.

3. **1 GB de fotos** comporta cerca de 2.500 imagens comprimidas — algo como 60 a 80 alunos
   no primeiro ano, com avaliação trimestral. Quando encher, as fotos migram para o
   Cloudflare R2 (10 GB gratuitos, depois cerca de US$ 0,015 por GB) ou sobe-se de plano.

4. Sem suporte por e-mail dos fornecedores. Na prática, irrelevante nessa escala.

### 17.2 Nível 1 — Operação (quando o faturamento justificar)

| Item | Custo/mês |
|---|---|
| Supabase Pro — backup diário gerenciado com 7 dias de retenção, sem pausa, 8 GB de banco, 100 GB de arquivos, suporte | ~R$ 140 |
| Demais itens | continuam gratuitos |
| Domínio | ~R$ 3 |
| **Total** | **~R$ 145** |

**Gatilho para subir de nível:** quando o faturamento passar de aproximadamente R$ 1.500/mês,
ou quando os limites de armazenamento apertarem. Backup gerenciado por fornecedor, com dado
de saúde de dezenas de pessoas, vale os R$ 140 — mas não no primeiro mês, com três alunos.

### 17.3 O custo que não desaparece: as lojas de aplicativos

| Item | Valor |
|---|---|
| Apple Developer Program | **US$ 99 por ano** (~R$ 540/ano, ou ~R$ 45/mês) — obrigatório para publicar na App Store |
| Google Play Console | **US$ 25, pagamento único** |

Esse é, de longe, o maior custo recorrente do Nível 0 — a taxa da Apple sozinha custa mais do
que toda a infraestrutura. **E existe uma forma legítima de adiá-la.**

### 17.4 A alternativa que corta o maior custo: começar como PWA

Um **PWA** (aplicativo web instalável) é um site que o aluno adiciona à tela de início do
celular e que passa a se comportar como aplicativo: ícone próprio, tela cheia, sem barra de
navegador, funcionamento offline e notificações push.

| | PWA | Aplicativo nas lojas |
|---|---|---|
| Taxa da Apple | **R$ 0** | US$ 99/ano |
| Taxa do Google | **R$ 0** | US$ 25 |
| Revisão da loja | **não existe** | dias de espera, com risco de rejeição |
| Correção de bug | **no ar em minutos** | nova submissão e nova revisão |
| Instalação | pelo link, "Adicionar à tela de início" | busca na loja |
| Funciona offline | sim | sim |
| Notificação push | sim (no iOS, após instalar na tela de início) | sim |
| Integração com Apple Health / Google Fit | não | sim |
| Percepção de credibilidade | menor | maior |

**Recomendação: lançar como PWA e publicar nas lojas na Fase 2**, quando o faturamento
justificar a taxa da Apple e houver alunos suficientes para as integrações fazerem diferença.

O ponto decisivo é que **isso não é retrabalho**: a stack escolhida (React Native com Expo)
gera também a versão web a partir do mesmo código. Publicar nas lojas depois é empacotar o que
já existe, não reescrever.

### 17.5 Resumo

| Cenário | Custo mensal |
|---|---|
| **Começo, como PWA** | **R$ 3 a R$ 15** |
| Começo, publicando nas lojas | ~R$ 50 (a taxa da Apple diluída) |
| Em operação, com backup gerenciado e nas lojas | ~R$ 190 |
| Estimativa anterior deste documento *(superestimada)* | ~~R$ 290 a R$ 400~~ |

Somam-se as **taxas de pagamento**, que só incidem sobre o que ele efetivamente receber:
cerca de 1% no Pix e até 4% no cartão parcelado. Esse é o único custo que cresce junto com o
faturamento — e é o custo que realmente importa no longo prazo.

**Leitura de negócio:** começando como PWA, **um único aluno pagante cobre a infraestrutura do
ano inteiro.** O custo relevante do projeto não é a operação: é o desenvolvimento inicial e,
depois, as taxas sobre o faturamento.

## 18. Riscos e mitigações

| Risco | Impacto | Como mitigamos |
|---|---|---|
| Vazamento de fotos corporais | **Crítico** — dano de imagem e responsabilização legal | Bucket privado, URL assinada de curta duração, sem EXIF, marca d'água, log de auditoria, retenção limitada, 2FA no acesso do coach |
| Ferramenta de monitoramento capturar dado sensível no log | **Alto** — vazamento por onde ninguém olha | Filtro antes do envio, gravação de sessão desligada, identificação só por código interno, retenção curta (13.5) |
| Bug chegar ao aluno sem forma de voltar atrás | **Alto** — perda de confiança logo no início | Homologação obrigatória, testes automatizados, verificação antes de publicar e rollback em minutos (14.2) |
| Registro de treino perdido na sincronização offline | **Alto** — o aluno perde o trabalho e desiste do app | Regra escrita de conflito: execução nunca é sobrescrita, protocolo é versionado (14.3) |
| Demanda maior que a capacidade do coach | **Alto** — prazo estourado e má primeira impressão | Vagas limitadas e fila de espera (3.6), com modo ausência |
| Taxa de loja ao começar a cobrar | Médio a alto — até 30% da receita | Avaliar antes de publicar nas lojas; o PWA elimina o problema (9.1) |
| Escopo crescer sem controle | Atraso e estouro de custo | Escopo do MVP congelado por escrito; novidades vão para a Fase 2 |
| Baixa adesão do aluno ao registro diário | Relatórios vazios, produto perde valor | Registro em 1 toque, funcionamento offline, lembretes, comparativo de carga visível, gráfico imediato |
| Vídeo do YouTube removido pelo criador | Aluno vê link quebrado | Verificação automática de links + plano de gravar vídeos próprios |
| Rejeição do app pelas lojas | Atraso na publicação | Política de privacidade publicada, exclusão de conta dentro do app, avisos de saúde — os três motivos mais comuns de rejeição, tratados desde o início |
| Restrição declarada uma vez e nunca atualizada | **Alto** — alerta automático baseado em dado vencido | Revisão periódica com prazo acordado, semáforo, lembrete e bloqueio da renovação automática enquanto vencida |
| Aluno lesionado recebendo treino sem avaliação individual | **Crítico** — risco à saúde e à responsabilidade profissional | Trava de contato prévio: o sistema não publica o treino antes do contato registrado |
| Exigir 3 opções triplicar o tempo de prescrição | Médio — o coach abandona a regra | Grupos de equivalência no banco: o sistema sugere os substitutos e ele só confirma |
| Falta de definição sobre técnicas avançadas | Retrabalho na modelagem do treino | Já isolado como decisão explícita (Anexo A) antes de codificar |
| Inadimplência em planos por Pix | Perda de receita | Lembretes automáticos, tolerância configurável, bloqueio automático |
| Dependência de uma pessoa só (o coach) | Gargalo de atendimento | SLA visível, modelos de treino/dieta, respostas rápidas prontas, e o caminho de "assistente" já previsto na arquitetura |

---

## 19. Registro de decisões

São **25 decisões** e **2 já fechadas**. Estão separadas por **quando cada uma precisa estar
resolvida** — não por assunto. Uma decisão do Bloco A tomada tarde para o desenvolvimento
inteiro; uma do Bloco C tomada tarde atrasa só o lançamento.

Cada decisão traz a pergunta, as opções, a recomendação técnica e **o que muda se ela for
alterada depois** — que é o custo real de adiar.

---

### 19.1 Já decidido

| # | Decisão | Definição |
|---|---|---|
| ✅ **F2** | Cobrança no MVP | **Não existe.** O acompanhamento começa gratuito, sem planos nem gateway. O modelo de dados nasce preparado, e a decisão de cobrar — se, quando e por qual meio — fica em aberto até haver demanda real. Ver 9.1 antes de decidir cobrar dentro de app de loja |
| ✅ **F1** | O que acontece quando a revisão de restrição vence | Trava **apenas a renovação automática por modelo**. O coach continua podendo publicar manualmente, com registro, e o aluno **nunca** perde o acesso ao treino atual. *(Levar à reunião só para ciência.)* |

---

### 19.2 Bloco A — Travam o início do desenvolvimento

**Precisam sair da reunião.** Sem elas, não se escreve a primeira linha de código sem risco de
retrabalho.

**A1 · Técnicas avançadas** — Quais ele efetivamente prescreve?

- **Como decidir:** preencher o `anexo-a-tecnicas-avancadas.md` (24 técnicas, marcar as usadas)
- **Recomendação:** implementar um modelo genérico de série que comporte sub-séries,
  agrupamento de exercícios e cadência — cobre a maioria sem uma tela por técnica

- **Se mudar depois:** refaz boa parte do módulo de treino. É a decisão mais cara do projeto

**A2 · Como o treino é montado** — Do zero, por modelos, ou os dois?

- **Recomendação:** os dois. O custo adicional é pequeno e o ganho de tempo para ele é grande
- **Se mudar depois:** reescreve a tela de prescrição

**A3 · Titular e substitutos** — Exigir três opções em todos os exercícios, ou só nos que
dependem de aparelho específico? E ele topa cadastrar os grupos de equivalência?

- **Recomendação:** exigir em todos, com dispensa justificada; grupos de equivalência são
  obrigatórios — sem eles a regra triplica o tempo de montagem e será abandonada

- **Se mudar depois:** muda a estrutura do exercício prescrito e o gráfico de progressão

**A4 · Trava do contato prévio** — O sistema impede publicar o treino até o contato ser
registrado, ou apenas alerta?

- **Recomendação:** impede, com dispensa justificada e registrada. Alerta que só pisca é
  ignorado no terceiro aluno

- **Se mudar depois:** muda o fluxo de aprovação e o registro de responsabilidade

**A5 · Prazos de revisão de restrição** — Confirmar ou substituir a tabela por gravidade
(15 / 30 / 60-90 dias, 6 meses, 6-12 meses — ver 6.4)

- **Recomendação:** usar a tabela como padrão do sistema, sempre editável caso a caso
- **Se mudar depois:** ajuste simples de parâmetro. Entra no Bloco A por ser insumo da A4

**A6 · CREF, CRN e responsabilidade pela prescrição alimentar** — Ele é nutricionista, tem
nutricionista parceiro, ou atua com orientação alimentar dentro do escopo do profissional de
educação física?

- **Recomendação:** definir com o advogado antes de qualquer texto ir para o ar
- **Se mudar depois:** muda os textos legais do app, o que pode ser chamado de "dieta" e quem
  assina o relatório. **É a decisão de maior risco jurídico**

**A7 · Escopo do MVP** — O que entra e o que fica de fora, item a item da Fase 1

- **Recomendação:** congelar por escrito e assinar; tudo o que surgir depois vai para a Fase 2
- **Se mudar depois:** é exatamente o que faz projeto assim estourar prazo e orçamento

**A8 · Alunos atuais** — Ele já atende alunos hoje? Eles migram para o app no lançamento, ou
entram aos poucos pelo fluxo normal?

- **Recomendação:** entrarem aos poucos, pelo fluxo normal — não custa nada e ainda serve de
  revisão da base. Migração em massa só se ele tiver muitos alunos e histórico que valha
  importar

- **Se mudar depois:** exige construir importação em massa, que é trabalho fora do previsto

---

### 19.3 Bloco B — Precisam sair até a metade do MVP

**Prazo: até a semana 6.** Não travam o começo, mas travam módulos específicos.

| # | Decisão | Recomendação |
|---|---|---|
| **B1** | Vídeos: só links do YouTube ou também vídeos gravados por ele? | Começar com YouTube; gravar os principais com o tempo |
| **B2** | Registro de RIR/RPE entra, ou é complexidade demais para o aluno? | Entrar como campo opcional, ligável por aluno |
| **B3** | Inventário de equipamentos da academia do aluno: MVP ou Fase 2? | MVP, se o custo confirmado for baixo — é o que faz o titular ser realista |
| **B4** | Prazo prometido para responder a solicitação de inscrição | 2 dias úteis |
| **B5** | Periodicidade de fotos e medidas de acompanhamento | Medidas quinzenais, fotos mensais |
| **B6** | Gateway de pagamento | Comparar taxas de Asaas, Mercado Pago, Pagar.me e Stripe com o contador |
| **B7** | Aceita alunos menores de 18 anos? | Se sim, exige consentimento do responsável e muda o fluxo de cadastro |
| **B8** | Monitoramento de erros: ferramenta externa (Sentry) ou hospedada por nós? | Sentry gratuito, com o filtro de dados da seção 13.5. Self-hosted só se ele exigir que nada saia |
| **B9** | Quantas vagas ele aceita simultaneamente? | Começar baixo (10 a 15) e subir conforme sentir o ritmo — é mais fácil abrir vaga do que se desculpar por atraso |
| **B10** | Treino não executado no dia: fica pendente ou vence? | Fica pendente, com a data real registrada e a diferença visível no relatório |
| **B11** | Pausa do aluno: quantas por ano e por quanto tempo? | Livre no início, com registro de motivo. Regra rígida só se virar problema |

---

### 19.4 Bloco C — Precisam sair até o lançamento

**Prazo: até a semana 10.** Nenhuma trava desenvolvimento; todas travam a publicação.

| # | Decisão | Recomendação |
|---|---|---|
| **C1** | Preços dos quatro planos e política de cancelamento/reembolso | Destacar o trimestral como "mais escolhido" |
| **C2** | Marca: nome, logo, cores e domínio | Definir cedo, porque alimenta a landing page |
| **C3** | Dias e horários fixos para as videochamadas | Blocos fixos na semana, não agenda aberta |
| **C4** | Retenção: por quanto tempo guardar fotos e dados após o fim do contrato | 12 meses, com exclusão automática |
| **C5** | Lançar como PWA ou já publicar nas lojas? | PWA primeiro — economiza US$ 99/ano e a espera por revisão, sem retrabalho (ver 17.4) |
| **C6** | Quem é o Encarregado de dados (DPO) e qual e-mail publicar | Pode ser o próprio coach, com e-mail dedicado |

---

### 19.5 Resumo para a reunião

| Bloco | Quantas | Quando | Consequência de não decidir |
|---|---|---|---|
| **A — Travam o início** | 8 | **Na reunião** | O desenvolvimento não começa, ou começa com risco alto de retrabalho |
| **B — Metade do MVP** | 11 | Até a semana 6 | Módulos específicos ficam parados |
| **C — Lançamento** | 6 | Até a semana 10 | O produto fica pronto mas não pode ser publicado |

> A pauta operacional, bloco a bloco e com os itens de apoio de cada decisão, está no
> `anexo-c-checklist-reuniao.md`.

## 20. Conclusão

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
