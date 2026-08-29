# Anexo A — Técnicas avançadas de treino

> **Este é um item de decisão, não uma especificação.** Conforme registrado na minuta, as
> técnicas avançadas **mudam a forma de montar o treino e a forma de registrar a execução**.
> Só entram no desenvolvimento as que o coach efetivamente prescreve.
>
> **Como usar:** o coach marca a coluna "Usa?". Cada técnica marcada gera uma estrutura de
> registro específica no app. Cada técnica **não** marcada é custo que não pagamos.

## Por que isso importa tecnicamente

Um exercício simples precisa registrar: **carga × repetições, por série**. Uma linha por série.

As técnicas avançadas quebram essa estrutura. Um drop-set não tem "uma carga" — tem três em
sequência. Um bi-set não é um exercício, são dois amarrados. Um rest-pause tem repetições
fracionadas dentro da mesma série. Se o app for construído assumindo o modelo simples e as
técnicas entrarem depois, boa parte do módulo de treino precisa ser refeita.

Por isso essa decisão vem **antes** de escrever código.

---

## Catálogo para marcação

| # | Técnica | O que é | O que o app precisa registrar a mais | Usa? |
|---|---|---|---|:---:|
| 1 | **Drop-set** (série descendente) | Ao falhar, reduz a carga e continua sem descanso | N sub-séries por série: carga + reps de cada queda | ☐ |
| 2 | **Rest-pause** | Falha, descansa 10-20s, continua até nova falha | Reps de cada micro-série + tempo de pausa | ☐ |
| 3 | **Cluster set** | Série dividida em blocos com pausas curtas planejadas | Blocos, reps por bloco, pausa entre blocos | ☐ |
| 4 | **Myo-reps** | Série ativadora + várias mini-séries curtas | Reps da ativadora + reps de cada mini-série | ☐ |
| 5 | **Bi-set** | Dois exercícios em sequência, sem descanso | Agrupamento de 2 exercícios + ordem | ☐ |
| 6 | **Tri-set** | Três exercícios em sequência | Agrupamento de 3 exercícios + ordem | ☐ |
| 7 | **Série gigante** | Quatro ou mais em sequência | Agrupamento de N exercícios + ordem | ☐ |
| 8 | **Super-série antagonista** | Dois exercícios de músculos opostos, alternados | Agrupamento + marcação de antagonismo | ☐ |
| 9 | **Pré-exaustão** | Isolado antes do composto do mesmo músculo | Ordem obrigatória entre dois exercícios | ☐ |
| 10 | **Pós-exaustão** | Composto antes do isolado | Ordem obrigatória entre dois exercícios | ☐ |
| 11 | **Negativas / excêntrica acentuada** | Ênfase e tempo maior na fase de descida | Tempo (tempo/cadência) por fase: ex. 4-0-1-0 | ☐ |
| 12 | **Isometria / pausa** | Sustentação estática em um ponto do movimento | Segundos de sustentação | ☐ |
| 13 | **Repetições parciais** | Amplitude reduzida ao fim da série | Reps completas + reps parciais, separadas | ☐ |
| 14 | **Repetições forçadas** | Parceiro auxilia após a falha | Reps assistidas + confirmação de que houve ajuda | ☐ |
| 15 | **Pirâmide crescente** | Carga sobe e reps caem a cada série | Nada novo (o modelo simples cobre) | ☐ |
| 16 | **Pirâmide decrescente** | Carga cai e reps sobem a cada série | Nada novo (o modelo simples cobre) | ☐ |
| 17 | **Série queimada (burnout)** | Série final até a falha com carga leve | Marcação de série tipo "burnout" | ☐ |
| 18 | **21s** | 7 parciais baixas + 7 parciais altas + 7 completas | Três blocos fixos de reps | ☐ |
| 19 | **Circuito** | Vários exercícios em rodadas, com pouco descanso | Rodadas + tempo total + ordem | ☐ |
| 20 | **FST-7** | 7 séries finais de isolamento com descanso curto | Bloco de 7 séries com descanso fixo | ☐ |
| 21 | **GVT (10×10)** | 10 séries de 10 com carga fixa | Nada novo (o modelo simples cobre) | ☐ |
| 22 | **Oclusão vascular (BFR/Kaatsu)** | Restrição parcial de fluxo sanguíneo | Pressão/nível de faixa + registro de contraindicações | ☐ |
| 23 | **Tempo sob tensão (TUT) controlado** | Cadência prescrita para toda a série | Cadência em 4 números | ☐ |
| 24 | **Stripping / roubada (cheating)** | Uso controlado de impulso após a falha | Marcação de reps "com roubada" | ☐ |

**Outras que o coach usa e não estão na lista:**

```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

---

## Perguntas complementares

1. As técnicas são prescritas **por exercício**, **por série específica** (ex.: só na última),
   ou **por bloco de treino**?

2. O aluno precisa apenas marcar **"consegui / não consegui"**, ou precisa registrar os
   números de cada sub-série (ex.: as três cargas de um drop-set)?

3. O coach quer ver, no relatório, **a evolução da execução das técnicas** ao longo das semanas?
4. Técnicas avançadas ficam **liberadas só para nível intermediário/avançado** automaticamente,
   ou o coach decide caso a caso?

5. Alguma técnica deve ser **bloqueada automaticamente** para alunos com determinada restrição
   (por exemplo, oclusão para hipertensos)?

---

## Recomendação

Para o MVP, sugerimos implementar um **modelo genérico de série** capaz de comportar:
sub-séries (drop-set, rest-pause, myo-reps, cluster), agrupamento de exercícios (bi-set,
tri-set, super-série, circuito), cadência/tempo e uma marcação de "conseguiu executar".

Esse desenho cobre a grande maioria das técnicas da tabela **sem** construir uma tela
específica para cada uma — e permite ativar novas técnicas depois apenas configurando, sem
refazer código. As marcações do coach nesta tabela definem **quais aparecem na interface** e
**como são apresentadas** ao aluno.
