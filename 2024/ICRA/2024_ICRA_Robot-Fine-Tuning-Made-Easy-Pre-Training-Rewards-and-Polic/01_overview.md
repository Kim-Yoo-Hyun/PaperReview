# Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ICRA57147.2024.10610421.
> PDF retrieval source: https://arxiv.org/pdf/2310.15145. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: Jingyun Yang, Max Sobol Mark, Brandon Vu, Archit Sharma, Jeannette Bohg, Chelsea Finn
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, offline RL, reward model, real-world adaptation, policy fine-tuning
- Official paper: https://api.crossref.org/works/10.1109/ICRA57147.2024.10610421
- Full-text retrieval: https://arxiv.org/pdf/2310.15145
- Code/Project: https://robofume.github.io
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboFuME는 기존 조작 자료에서 시작해 실제 로봇이 사람이 매번 보상을 주거나 환경을 초기화할 필요 없이 목표 과제에 적응하도록 한다. [PDF 1쪽](https://arxiv.org/pdf/2310.15145v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The pre-train and fine-tune paradigm in machine learning has had dramatic success in a wide range of domains because the use of existing data or ...
- **p. 1 / Abstract - extractive body cue:** We aim to enable this paradigm in robotic reinforcement learning, allowing a robot to learn a new task with little human effort by leveraging data ...
- **p. 1 / Abstract - extractive body cue:** However, reinforcement learning often requires significant human effort in the form of manual reward specification or environment resets, even if the policy is pre-trained.
- **p. 1 / Abstract - extractive body cue:** We introduce ROBOFUME, a reset-free fine-tuning system that pre-trains a multi-task manipulation policy from diverse datasets of prior experiences and self-improves online to learn a ...
- **p. 1 / Abstract - extractive body cue:** Our insights are to utilize calibrated offline reinforcement learning techniques to ensure efficient online finetuning of a pre-trained policy in the presence of distribution shifts ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, numerous challenges arise when using this recipe in practice.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the pre-training phase, we assume access to a diverse prior dataset, a few task demonstrations and reset demonstrations of the target task, and a ...

## Core Idea

- **p. 3 / III. PRELIMINARIES - extractive body cue:** Our method assumes access to a prior dataset Dprior = ∪N j=1Dj = ∪N j=1{(sj i, aj i, s′j i )}K i=1, which consists of ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We propose a system that enables autonomous and efficient real-world robot learning.
- **p. 1 / Abstract - extractive body cue:** In a diverse set of five real robot manipulation tasks, we show that our method can incorporate data from an existing robot dataset collected at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our framework by pre-training it on the Bridge dataset [19] and testing it on a diverse set of real-world downstream tasks: cloth folding, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We perform more quantitative experiments in a simulation setup, where we illustrate that our method outperforms imitation learning and offline RL methods that either do ...
- **p. 3 / IV. ROBOFUME - extractive body cue:** The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this paradigm in robotics.
- **p. 4 / IV. ROBOFUME - extractive body cue:** We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label of whether the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector through an MLP, and produces the output ... | dataset state/observation, action, reward와 return-to-go | p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME) |
| State/latent | policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task, representation, proprioceptive | Q/value 또는 sequence-policy state | p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 3 (III. PRELIMINARIES) |
| Output/action | We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label of whether the current observation corresponds to a successful state ... | dataset-supported action sequence | p. 4 (IV. ROBOFUME), p. 3 (III. PRELIMINARIES), p. 4 (IV. ROBOFUME) |
| Objective/outcome | The VLM outputs a sparse binary reward, returning success if the ‘yes' token has a higher probability than ‘no' token. | offline policy value, OOD safety와 closed-loop success | p. 4 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 3 (IV. ROBOFUME) |

## Main Claims and Actual Contribution

- 오프라인 강화학습의 가치 추정 교정과 시각언어모델 기반 성공 분류기를 결합해 온라인 학습을 진행했다. [PDF 3쪽](https://arxiv.org/pdf/2310.15145v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2310.15145v1#page=4)
- 다섯 실물 조작에서 적응 결과를 비교하고 온라인 학습에 쓰인 보상 분류기의 정확도도 측정했다. [PDF 5쪽](https://arxiv.org/pdf/2310.15145v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2310.15145v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Embodiment/environment | Similarly, we find that one-hot task encodings perform substantially worse than language-conditioned policies, as the prior dataset used in real-robot training is larger and more diverse compared to the simulation experiments. | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | Simulation Experiments and Ablations We use a suite of simulated robotic manipulation environments to ablate contributions of different components of our algorithm. | role, split, size and leakage | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Metric | For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps of online fine-tuning. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. EXPERIMENTS - extractive body cue:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We provide 10 forward and reset demonstrations for each task, 30 failure demos, and 10 demos each for 20 prior tasks that show picking and ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We find that in the Vase simulated task, VIP fails to obtain good behaviors.
- **p. 6 / VI. CONCLUSION AND FUTURE WORK - extractive body cue:** Integrating this work with new VLM models that can exhibit robust zero-shot performance on unseen manipulation tasks and improving the reset efficiency of this framework ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (IV. ROBOFUME)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, numerous challenges arise when using this recipe in practice. (p. 1, I. INTRODUCTION).
- **Actual contribution:** We evaluate our framework by pre-training it on the Bridge dataset [19] and testing it on a diverse set of real-world downstream tasks: cloth folding, cloth covering, sponge pickand-place, placing ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by 58% on an average. (p. 5, V. EXPERIMENTS).
- **Explicit failure boundary:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures. (p. 5, V. EXPERIMENTS).
