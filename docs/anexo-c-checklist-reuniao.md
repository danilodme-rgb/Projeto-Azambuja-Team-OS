# Anexo C — Pauta da reunião de definição

Checklist para conduzir a reunião com o coach. Cada item fechado aqui é uma semana de
retrabalho evitada depois. **Tempo estimado: 120 a 150 minutos.**

Os códigos `A1`, `B3`, `C5` remetem ao **registro de decisões da seção 18 da minuta**. Os itens
marcados com **`A`** são os que travam o início do desenvolvimento: **se a reunião só conseguir
fechar sete coisas, que sejam essas sete.**

Sugestão de condução: apresentar a minuta em 20 minutos, e usar o resto do tempo nesta pauta.

---

## Bloco 1 — Negócio e marca *(15 min)*

- [ ] `C2` Nome da marca e domínio (`.com.br`)
- [ ] Já existe logo e identidade visual? Se não, quem faz?
- [ ] `C1` Preço dos planos: mensal, trimestral, semestral, anual
- [ ] Política de cancelamento e reembolso
- [ ] Quantos alunos ele quer atender por mês? E qual o teto de atendimento dele?
- [ ] `B6` Gateway de pagamento preferido (Asaas / Mercado Pago / Pagar.me / Stripe)
- [ ] Regime tributário (MEI, ME/Simples) e se precisa de nota fiscal automática
- [ ] E-mail profissional a criar (ex.: `contato@...`)

## Bloco 2 — Habilitação e responsabilidade técnica *(10 min)* ⚠️ crítico

- [ ] Número do **CREF**
- [ ] Ele é **nutricionista**? Tem **CRN**?
- [ ] `A6` Se não: trabalha com nutricionista parceiro, ou atua com orientação alimentar dentro do
      escopo do profissional de educação física? **Isso define o texto legal do app, o que pode
      ser chamado de "dieta" e o que assina o relatório.**

- [ ] `B7` Aceita alunos **menores de 18 anos**? (exige consentimento do responsável)
- [ ] Aceita **gestantes**? Exige liberação médica?
- [ ] Exige atestado médico ou PAR-Q antes de liberar o treino?

## Bloco 3 — Captação e onboarding *(15 min)*

- [ ] `B4` Prazo prometido para responder a solicitação (sugestão: 2 dias úteis)
- [ ] Algum campo a mais ou a menos no formulário de inscrição?
- [ ] Fotos: os 3 ângulos estão certos? Quer alguma pose específica?
- [ ] Ele quer **entrevista/call antes de aprovar**, ou aprova pela ficha?
- [ ] Aprova antes de cobrar, ou cobra antes de aprovar?
- [ ] Quer recusar alunos? Com qual mensagem?
- [ ] Depoimentos e fotos de alunos na landing page — ele já tem autorizações por escrito?

## Bloco 4 — Treino *(25 min)* ⚠️ maior impacto no prazo

- [ ] **`A2` Montagem: do zero, por modelos, ou os dois?** *(recomendação: os dois)*
- [ ] Se por modelos: quantos e quais (por objetivo × nível)?
- [ ] Divisões que ele usa (ABC, ABCD, push/pull/legs, full body, upper/lower...)
- [ ] Ele quer o banco de exercícios pré-carregado ou prefere cadastrar só os dele?
- [ ] **`A1` Técnicas avançadas: preencher o Anexo A** ⚠️
- [ ] `B2` Registra **RIR/RPE**? Ou é complexidade demais para o aluno?
- [ ] Prescreve cardio? Como (tipo, tempo, intensidade, HIIT/LISS)? Precisa registrar?
- [ ] Prescreve aquecimento e mobilidade? Entram como exercício?
- [ ] `B1` Vídeos: só links do YouTube (Leandro Twin) ou também vídeos gravados por ele?
- [ ] Quem escreve a descrição de execução de cada exercício? (é trabalho, mas é o diferencial)
- [ ] O treino é fixo por semana, ou tem periodização com progressão automática?
- [ ] O aluno pode trocar a ordem dos exercícios? Pode pular?

## Bloco 4B — Restrições e lesões *(20 min)* ⚠️ novo, alto impacto

- [ ] Confirmar a pergunta de lesão no cadastro (Sim/Não com detalhamento)
- [ ] **`A4` A trava funciona?** Sistema impedir a publicação do treino até o contato prévio
      ser registrado — ou apenas alertar? *(recomendação: impedir, com dispensa justificada)*

- [ ] Como ele prefere fazer esse contato: videochamada, telefone ou áudio?
- [ ] **`A5` Prazos de revisão por gravidade** — validar ou substituir a tabela sugerida:
      - Lesão aguda / em tratamento / pós-operatório → 15 dias
      - Em recuperação, dor moderada → 30 dias
      - Limitação crônica estável → 60 a 90 dias
      - Restrição alimentar clínica → 6 meses
      - Preferência alimentar → 6 a 12 meses
- [ ] Qual nível de dor (0 a 10) dispara alerta imediato para ele?
- [ ] Exige liberação médica de quem marcou lesão? Em quais casos?
- [ ] Aceita upload de laudo/exame? *(é dado sensível — aumenta a exigência de proteção)*
- [x] ~~Revisão vencida deve bloquear a renovação automática do treino?~~ **DECIDIDO:** trava
      apenas a renovação automática por modelo. O coach continua podendo publicar manualmente
      com registro, e o aluno **nunca** perde o acesso ao treino atual. *(Não precisa ser
      rediscutido na reunião — levar apenas para ciência do coach.)*

- [ ] Quem pode encerrar uma restrição: só ele, ou o aluno também pode declarar alta?

## Bloco 4C — Titular e substitutos *(10 min)*

- [ ] Confirmar a regra: **1 titular + 2 substitutos** por exercício
- [ ] `A3` Exigir isso em **todos** os exercícios, ou só nos que dependem de aparelho
      específico? E ele topa cadastrar os grupos de equivalência?

- [ ] Ele topa cadastrar os **grupos de equivalência** no banco (uma vez, para o sistema sugerir
      os substitutos depois)? Sem isso, a regra triplica o tempo de montagem

- [ ] O aluno pode escolher livremente entre as 3, ou o titular é obrigatório quando disponível?
- [ ] `B3` **Inventário de equipamentos da academia do aluno** — MVP ou Fase 2?

## Bloco 5 — Nutrição *(20 min)*

- [ ] Confirmar as bases: **TACO + TBCA + medidas caseiras do IBGE** — ele concorda?
- [ ] Ele trabalha por **macros**, por **porções**, ou por **cardápio fechado**?
- [ ] Confirma **3 opções por refeição** como mínimo? Pode ser mais?
- [ ] Quais refeições padrão (nomes e quantidade)?
- [ ] Prescreve suplementação? Precisa entrar no app?
- [ ] Como trata **dia livre / refeição livre**? Entra no cálculo?
- [ ] Prescreve controle de água? Sódio? Fibras?
- [ ] O aluno pode registrar comida fora do plano? *(recomendação: sim — sem isso o dado morre)*
- [ ] Quer receitas/preparações próprias no banco?

## Bloco 6 — Acompanhamento e relatórios *(15 min)*

- [ ] `B5` Frequência de pesagem, medidas e fotos de acompanhamento
- [ ] Quais circunferências ele mede
- [ ] Usa dobras cutâneas ou bioimpedância? Precisa registrar?
- [ ] O que ele quer ver no relatório que não está na lista da seção 7.2?
- [ ] Quer o **gráfico de evolução da dor** ao lado do de carga, para alunos com lesão?
- [ ] Quer ver o **percentual de sessões feitas no exercício titular**?
- [ ] O relatório vai para o aluno também, ou é só instrumento da call?

## Bloco 7 — Comunicação e agenda *(10 min)*

- [ ] Confirmar a regra das 18h
- [ ] Quer categorias de mensagem? Alguma prioridade especial?
- [ ] `C3` Dias e horários fixos para as calls
- [ ] Ferramenta de vídeo (recomendação: Google Meet)
- [ ] O que acontece se o aluno faltar à call? Remarca? Perde?
- [ ] Quer canal de grupo/comunidade entre alunos? *(sugestão: Fase 2)*

## Bloco 8 — LGPD e retenção *(10 min)*

- [ ] `C4` Por quanto tempo guardar fotos e dados após o fim do contrato (sugestão: 12 meses)
- [ ] `C6` Quem será o **Encarregado de dados (DPO)** e qual e-mail publicar
- [ ] Ele tem advogado para revisar os documentos? Se não, providenciar
- [ ] Ele concorda com o 2FA obrigatório na conta dele?

## Bloco 9 — Escopo do MVP *(10 min)*

- [ ] `C5` **Lançar como PWA (instalável pelo navegador) ou já publicar nas lojas?**
      *(PWA economiza US$ 99/ano da Apple, elimina a espera por revisão e não gera retrabalho —
      o mesmo código vira app de loja depois)*

- [ ] `A7` Revisar a lista da Fase 1 item a item: **entra / não entra**
- [ ] Definir a data-alvo de lançamento
- [ ] Definir quantos alunos entram no piloto (sugestão: 5 a 10, com desconto de fundador)
- [ ] Congelar o escopo **por escrito** e assinar

---

## Saída esperada da reunião

**As sete decisões do Bloco A, fechadas.** São elas que liberam o início do desenvolvimento:
`A1` técnicas avançadas · `A2` como o treino é montado · `A3` titular e substitutos ·
`A4` trava do contato prévio · `A5` prazos de revisão · `A6` CREF/CRN e prescrição alimentar ·
`A7` escopo do MVP congelado.

**Documentos que precisam sair da mesa preenchidos:**

- `anexo-a-tecnicas-avancadas.md` com a coluna "Usa?" marcada
- Tabela de prazos de revisão validada ou substituída
- Lista da Fase 1 revisada item a item, **assinada** por ele
- Data-alvo de lançamento acordada

Com o Bloco A fechado e esses quatro documentos em mãos, o desenvolvimento começa. Os Blocos
B e C podem ser resolvidos por mensagem ao longo das semanas seguintes — mas **com data**,
não "depois a gente vê".
