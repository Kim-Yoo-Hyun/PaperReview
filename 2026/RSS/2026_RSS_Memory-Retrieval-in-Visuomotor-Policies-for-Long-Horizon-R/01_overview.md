# Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss22/p010.html.
> review-time program locator (PDF retrieval URL not recorded). Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RSS
- Authors: Rutav Shah, Yisu Li, Femi Bello, Yuke Zhu, Roberto Martín-Martín
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, memory, long-horizon, partial observability, Imitation Learning, retrieval
- Official paper: https://www.roboticsproceedings.org/rss22/p010.html
- Published PDF: https://www.roboticsproceedings.org/rss22/p010.pdf
- Code/Project: https://robin-lab.cs.utexas.edu/HALO/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

HALO는 긴 조작 중 과거 정보가 필요한 시점에 시연 이력에서 관련 장면을 찾아 행동을 결정한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p010.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose robots operating in partially observable environments, such as homes, require memory to support autonomy.
- **p. 1 / Abstract - extractive body cue:** They must recall diverse information from the past, such as where objects were placed, which tasks a human partner has completed, and when an appliance ...
- **p. 1 / Abstract - extractive body cue:** Achieving this versatility requires a memory retrieval mechanism that generalizes well across tasks.
- **p. 1 / Abstract - extractive body cue:** However, hand-designed or heuristicbased methods rely on task-specific assumptions that may not transfer to different settings.
- **p. 1 / Abstract - extractive body cue:** Transformer architectures that use attention over long contexts for memory retrieval provide a promising alternative, as they learn retrieval from data without task-specific assumptions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges.
- **p. 2 / I. INTRODUCTION - extractive body cue:** HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across these settings, we show that VQA-induced task priors provide a general solution, improving absolute task success by 7% on average across diverse tasks and ...
- **p. 1 / Abstract - extractive body cue:** To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of a general memory retrieval mechanism that can be learned end-to-end, rather than tailored to individual tasks or modalities [6]-[9].
- **p. 4 / III. HALO - extractive body cue:** For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer ...
- **p. 4 / III. HALO - extractive body cue:** Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in microwave How many ...
- **p. 3 / III. HALO - extractive body cue:** First, because attention aggregates information from all stored history Mt, the policy may attend to task-irrelevant details and incorporate them into decision-making, leading to spurious ...
- **p. 1 / Abstract - extractive body cue:** However, directly incorporating longcontext transformer architecture into imitation learning from offline data introduces two key challenges: (1) the policy may learn spurious correlations between the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an action encoder gact θ , which map ... | observation, uncertainty/risk estimate와 task command | p. 3 (III. HALO), p. 3 (III. HALO) |
| State/latent | parameterize, visuomotor, policy, three, main, components, modality-specific, encoders, consisting, observation, encoder, gobs | safe set, recovery state 또는 constraint margin | p. 3 (III. HALO), p. 3 (III. HALO), p. 4 (III. HALO) |
| Output/action | Given Mt, the current embedding xt, and the task instruction l, the policy backbone fθ produces a latent state zt = fθ(Mt, xt, l), This latent state is passed to two prediction ... | shielded, recovery 또는 safe action | p. 3 (III. HALO), p. 4 (III. HALO), p. 4 (III. HALO) |
| Objective/outcome | The VQA objective biases memory retrieval towards task-relevant information, whereas the action prediction objective may still access information needed for low-level control. | task return과 violation/failure probability | p. 2 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO) |

## Main Claims and Actual Contribution

- 시연에서 기억 의존형 영상 질문과 정답을 만들어 정책의 행동 학습과 공동 학습한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p010.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p010.pdf#page=5)
- 현재 결정에 관련된 일부 과거 토큰만 읽는 희소 어텐션을 사용해 실행 오차가 기억을 따라 누적되는 문제를 다뤘다. [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p010.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p010.pdf#page=5)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in the ‘Retrieve Object' task, respectively. | hardware/simulator version and reset protocol | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Dataset/benchmark | Across episodes, the involved objects and their relations vary. | role, split, size and leakage | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | A moderate value (k = 8) achieves the best performance (52% success). | definition, denominator, direction and uncertainty | p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. | fair input/data/compute/action matching | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results support our hypothesis that HALO reduces model drift (fewer manipulation failures)
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Method Retrieve Object Return to Container LSTM 0.14 0.12 Mamba 0.20 0.18 TransformerXL 0.12 0.20 Window Attention 0.13 0.16 Strided Attention 0.20 0.28 Hierarchical Attention ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Developing adaptive strategies that retrieve only the necessary amount of information at each step is a promising direction for future work.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. HALO)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. (p. 7, IV. EXPERIMENTS).
- **Explicit failure boundary:** These errors introduce noise into the stored representations, which can degrade latent representation quality, leading to model drift and cascading failures over long horizons. (p. 3, III. HALO).
