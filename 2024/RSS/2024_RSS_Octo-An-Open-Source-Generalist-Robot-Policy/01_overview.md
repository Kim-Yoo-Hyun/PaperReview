# Octo: An Open-Source Generalist Robot Policy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://www.roboticsproceedings.org/rss20/p090.html)
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2405.12213.
> PDF retrieval source: https://arxiv.org/pdf/2405.12213. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Dibya Ghosh, Homer Rich Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Tobias Kreiman, Charles Xu, Jianlan Luo, You Liang Tan, Lawrence Yunliang Chen, Quan Vuong, Ted Xiao, Pannag R Sanketi, Dorsa Sadigh, Chelsea Finn, Sergey Levine
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, generalist policy, Imitation Learning
- Official paper: https://arxiv.org/abs/2405.12213
- Full-text retrieval: https://arxiv.org/pdf/2405.12213
- Code/Project: https://octo-models.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Octo는 다양한 로봇에서 수집한 시연으로 하나의 범용 조작 정책을 사전학습하고, 익숙하지 않은 로봇의 센서와 행동 공간에 적응시키는 방법을 다룬다. [원문](https://www.roboticsproceedings.org/rss20/p090.html)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies ...
- **p. 1 / Abstract - extractive body cue:** However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset ...
- **p. 1 / Abstract - extractive body cue:** It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users ...

## Core Idea

Octo는 Open X-Embodiment의 로봇 궤적 약 80만 개로 사전학습한 Transformer 정책이다. 언어 지시나 목표 이미지를 조건으로 연속 행동 청크를 생성하며, 새 센서와 행동 공간에 맞춰 미세조정할 수 있다. [원문](https://www.roboticsproceedings.org/rss20/p090.html)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding [17]. | image/video, language instruction, proprioception과 history | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION) |
| State/latent | supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked, action, prediction | language-grounded task state와 action-policy context | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL) |
| Output/action | The core of our model is a transformer architecture that maps arbitrary input tokens (created from observations and tasks) to output tokens (then decoded into actions), which can be trained on a ... | continuous action, pose 또는 action chunk | p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL) |
| Objective/outcome | We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping of 1.0. | instruction following, task success, generalization과 latency | p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL) |

## Main Claims and Actual Contribution

같은 사전학습 모델을 여러 로봇에서 평가하고 새로운 관측·행동 공간에 미세조정했다. 언어 지시와 목표 이미지 조건에서의 조작 성능을 각각 보고했다. [원문](https://www.roboticsproceedings.org/rss20/p090.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Embodiment/environment | We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and environments with small target domain datasets. | hardware/simulator version and reset protocol | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Dataset/benchmark | In the BridgeV2 domain, we performed a fine-grained analysis of the zero-shot capabilities in Table VII; measuring performance on setups seen in the dataset, and for novel environments, scenes, and skills. | role, split, size and leakage | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL) |
| Metric | Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task per robot. ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Baseline/ablation | On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. | fair input/data/compute/action matching | p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors like ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** (1) The hyperparameters α, γ, and σ correspond to the noise schedule: we use the standard cosine schedule from [66].

## Why Read It

여러 로봇에서 사전학습한 정책을 다른 플랫폼에 옮길 때 어떤 입력부와 행동 출력부를 조정하는지 비교할 기준을 제공한다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets. (p. 2, I. INTRODUCTION).
- **Actual contribution:** Octo는 Open X-Embodiment의 로봇 궤적 약 80만 개로 사전학습한 Transformer 정책이다. 언어 지시나 목표 이미지를 조건으로 연속 행동 청크를 생성하며, 새 센서와 행동 공간에 맞춰 미세조정할 수 있다. [원문](https://www.roboticsproceedings.org/rss20/p090.html)
- **Evaluation boundary:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users to a pre-defined and often ... (p. 2, I. INTRODUCTION).
