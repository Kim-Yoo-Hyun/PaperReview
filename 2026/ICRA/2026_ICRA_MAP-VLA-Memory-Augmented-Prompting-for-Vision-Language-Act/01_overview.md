# MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11697046.
> PDF retrieval source: https://arxiv.org/pdf/2511.09516v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: Runhao Li, Wenkai Guo, Zhenyu Wu, Changyuan Wang, Haoyuan Deng, Zhenyu Weng, Yap-Peng Tan, Ziwei Wang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://api.crossref.org/works/10.1109/icra57385.2026.11697046
- Full-text retrieval: https://arxiv.org/pdf/2511.09516v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

MAP-VLA는 시연에서 얻은 단계별 기억을 동결된 VLA에 제공해 긴 조작 과제에서 다음 행동을 선택하게 한다. [PDF 1쪽](https://arxiv.org/pdf/2511.09516v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs.
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to ...
- **p. 1 / Abstract - extractive body cue:** To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task.
- **p. 1 / Abstract - extractive body cue:** These memory units are implemented as learnable soft prompts optimized through prompt tuning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In other words, the robot lacks episodic memory; it cannot directly recall "how an expert accomplished a similar stage" when it is performing one.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite the advantages mentioned above, current VLA models have a key limitation: they fail to leverage historical memory at task execution.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also develop MemoryAugmented Action Generation (MAAG), which enables memory retrieval and dynamic memory-aware prompt ensembling to augment action generation during realtime task execution. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present the Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), bridging the gap in current VLA models by enabling dynamic access to demonstration-derived ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose Memory-Augmented Action Generation, which retrieves the most relevant stage-specific memory prompt along with the corresponding demonstration actions by comparing the trajectory similarity.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To overcome this, we introduce a memory-augmented framework that enhances VLA models for better long-horizon task performance.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To identify meaningful task stage boundaries, we first select a well-performed demonstration as reference and extract its key poses that mark salient transitions such as ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Instead, we use it as an action prior to guide the dynamic weighting between Abase t and Amem t .

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an overview image I1 t, a wrist image ... | image/video, language instruction, proprioception과 history | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| State/latent | demonstration, consists, sequence, observation-action, pairs, where, observation, includes, overview, image, wrist, language | language-grounded task state와 action-policy context | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Output/action | VLA models acquire broad knowledge about the world from vision-language pre-training and learn to map raw visual observations and natural language instructions directly to robot actions through end-to-end training on diverse robotic ... | continuous action, pose 또는 action chunk | p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Objective/outcome | To encode the stage-specific memory, we optimize Vk by aligning the model's predicted action tokens with expert actions using the flow matching loss: V∗ k = arg min Vk Ep(At/ot), q(Aτ t ... | instruction following, task success, generalization과 latency | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- 시연을 작업 단계로 나누고 단계별 정보를 학습 가능한 소프트 프롬프트로 저장했다. [PDF 3쪽](https://arxiv.org/pdf/2511.09516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2511.09516v1#page=4)
- 실행 중 최근 궤적과 유사한 시연을 찾아 프롬프트를 선택하고, 시뮬레이션과 실물에서 긴 과제의 성공을 비교했다. [PDF 4쪽](https://arxiv.org/pdf/2511.09516v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2511.09516v1#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2511.09516v1#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest baseline, π0, across three long-horizon tasks. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | We also note that MAP-VLA's trial outcomes are more consistent, with a lower standard deviation in success rate (0.7%) across runs than π0 (2.3%). | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | As summarized in Table II, MAPVLA again outperforms the baseline policy. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, the memoryless baseline policy π0 exhibits inconsistent and ambiguous object alignment behavior, especially during critical pick-and-place phases (as circled in the figure), often leading ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** By dynamically balancing the task-level generalization of the base prompt with the stage-specificity of the retrieved prompt, the model maintains robustness to retrieval inaccuracies, improves ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This reduced variability suggests improved robustness and reliability, as a result of encoding additional contextual memory into the prompt and dynamic prompt ensembling as we ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In contrast, our MAP-VLA framework demonstrates memory-augmented robustness in such settings.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY)이다.
