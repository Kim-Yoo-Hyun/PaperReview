# MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2104.08212.
> PDF retrieval source: https://arxiv.org/abs/2104.08212. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / arXiv
- Authors: Dmitry Kalashnikov, Jacob Varley, Yevgen Chebotar, Benjamin Swanson, Rico Jonschkowski, Chelsea Finn, Sergey Levine, Karol Hausman
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, Multi-Task Learning, robot data, real-world manipulation
- Official paper: https://arxiv.org/abs/2104.08212
- Full-text retrieval: https://arxiv.org/abs/2104.08212
- Code/Project: https://karolhausman.github.io/mt-opt/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

MT-Opt는 여러 실제 로봇과 과제의 경험을 공유해 조작 기술을 함께 학습하고 새로운 과제의 강화학습을 시작한다. [PDF 1쪽](https://arxiv.org/pdf/2104.08212v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose robotic systems must master a large repertoire of diverse skills to be useful in a range of daily tasks.
- **p. 1 / Abstract - extractive body cue:** While reinforcement learning provides a powerful framework for acquiring individual behaviors, the time needed to acquire each skill makes the prospect of a generalist robot ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we study how a largescale collective robotic learning system can acquire a repertoire of behaviors simultaneously, sharing exploration, experience, and representations across ...
- **p. 1 / Abstract - extractive body cue:** In this framework new tasks can be continuously instantiated from previously learned tasks improving overall performance and capabilities of the system.
- **p. 1 / Abstract - extractive body cue:** To instantiate this system, we develop a scalable and intuitive framework for specifying new tasks through user-provided examples of desired outcomes, devise a multi-robot collective ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, 11, 86], which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** D) Sample of behaviorally and visually distinct tasks such as covering, chasing, alignment, which we show our method can adapt to.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** First, we discuss two base choices for the impersonation function fI, then we introduce a more principled solution.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** While this basic multi-task Q-learning system can in principle acquire diverse tasks, with each task learning from the data corresponding to that task, this approach ...
- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing between tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, multi-task reinforcement learning is known to be exceedingly difficult from the optimization standpoint, and the hypothesized benefits of multi-task learning have proven hard to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each time step, the policy selects an action a given the current state s and the current task Ti that is set at the beginning of the episode, and receives a ... | multi-view observation, language/task label과 action trajectory | p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW) |
| State/latent | time, step, policy, selects, action, given, current, state, task, beginning, episode, receives | shared representation, embodiment/task identity와 data distribution | p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS) |
| Output/action | 2C), at each time step, a policy takes as input a camera image and a one-hot encoding of the task, and sends a motor command to the robot. | dataset sample 또는 learned policy action | p. 3 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW) |
| Objective/outcome | The goal of the multi-task RL policy is to maximize the expected sum of rewards for all tasks drawn from the distribution p(T ). | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW) |

## Main Claims and Actual Contribution

- 성공 상태 예시로 과제를 정의하고 수집한 궤적에 여러 과제의 성공 판정과 보상을 적용했다. [PDF 3쪽](https://arxiv.org/pdf/2104.08212v2#page=3) · [PDF 5쪽](https://arxiv.org/pdf/2104.08212v2#page=5)
- 여러 로봇에서 모은 경험으로 실제 조작 12개를 평가하고 과제 사이의 경험·정책 공유 효과를 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2104.08212v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2104.08212v2#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |
| Embodiment/environment | The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a large set of vision-based robotic manipulation tasks? | hardware/simulator version and reset protocol | p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS) |
| Dataset/benchmark | The two policies are trained from the same offline dataset. lift-bottle, which have more data, especially on-policy data, have higher success rates than underrepresented tasks, such as lift-box. | role, split, size and leakage | p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |
| Metric | 7 shows the success rates of MT-Opt on the 12 evaluation tasks. | definition, denominator, direction and uncertainty | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 17 (Figure/Table caption) |
| Baseline/ablation | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. | fair input/data/compute/action matching | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VII. EXPERIMENTS - extractive body cue:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to mitigate correlations with spurious workspace features such ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re- balancing where the ratio of success ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** MT-Opt, which uses impersonated successes and failures, achieves 39% success for the same task, a ≈10× improvement.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 11: System overview: Task episodes from disk are continuously loaded by LogReplay job into task replay buffers. LogReplay process assigns binary reward signal to ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 14: Counts of labelled SD training data by task and outcome. This data was generated either from human video demonstration, or by labelling terminal ...
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** A wide range of manipulation behaviors fall into this category, from simple bin-picking to more complex behaviors, such as covering items with a cloth, placing ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 3 (III. SYSTEM OVERVIEW)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, 11, 86], which have so far made it ... (p. 2, I. INTRODUCTION).
- **Actual contribution:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to quickly define new tasks and ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. (p. 7, VII. EXPERIMENTS).
- **Explicit failure boundary:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks. (p. 8, VII. EXPERIMENTS).

## 원문과 공개 자료

- 데이터 · 공식 RLDS 판본의 실물 조작 훈련 샤드 · mt_opt_rlds-train.tfrecord-00000-of-02048 [배포 파일](https://storage.googleapis.com/gresearch/robotics/mt_opt_rlds/1.0.0/mt_opt_rlds-train.tfrecord-00000-of-02048)
