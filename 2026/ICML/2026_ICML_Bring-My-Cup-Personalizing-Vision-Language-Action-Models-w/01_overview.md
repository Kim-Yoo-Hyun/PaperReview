# Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/62528.
> PDF retrieval source: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Sangoh Lee, Sangwoo Mo, Wook-Shin Han
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://icml.cc/virtual/2026/poster/62528
- Full-text retrieval: https://arxiv.org/pdf/2512.20014.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Visual Attentive Prompting은 참조 사진 몇 장으로 사용자가 원하는 특정 물체를 찾아, 기존 VLA가 비슷한 물체들 중 올바른 대상을 조작하도록 한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=1) · [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on ...
- **p. 1 / Abstract - extractive body cue:** We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.
- **p. 1 / Abstract - extractive body cue:** VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then ...
- **p. 1 / Abstract - extractive body cue:** We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipu1GSAI, POSTECH 2IME, POSTECH.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this semantic gap, we formulate the challenge of manipulating personal objects.
- **p. 2 / 1. Introduction - extractive body cue:** In each benchmark, one object is replaced by a user-specific instance, same-category distractors are added, and the policy must ground the correct instance from a ...

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** The category is known, but the specific instance is novel and unseen during training, and at test time the robot encounters o amidst visually similar ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V v=1 denotes multi-view RGB images from V ... | image/video, language instruction, proprioception과 history | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction) |
| State/latent | consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes, multi-view, RGB | language-grounded task state와 action-policy context | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation) |
| Output/action | Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ... | continuous action, pose 또는 action chunk | p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 2 (1. Introduction) |
| Objective/outcome | While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation. | instruction following, task success, generalization과 latency | p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- 참조 사진을 시각 기억으로 저장하고 물체 검출과 특징 대응으로 현재 영상의 대상을 표시한 뒤 언어 지시를 다시 써서 고정된 정책에 제공한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=5)
- 두 개인화 시뮬레이션 벤치마크와 실제 탁상 과제를 만들어, 작업 성공 여부와 올바른 물체를 조작했는지를 구분해 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lee26ax/lee26ax.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |
| Embodiment/environment | Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware. | hardware/simulator version and reset protocol | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks) |
| Dataset/benchmark | We evaluate VAP on a real-world benchmark comprising four selection and four pick-and-place tasks (Figure 5). | role, split, size and leakage | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks), p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |
| Metric | Table 18. Controlled occlusion sweep on Personalized-SIMPLER. We vary the number of consecutive frames during which the target is fully occluded and report tracking accuracy and task success rate. The spatio-temporal tracker ... | definition, denominator, direction and uncertainty | p. 45 (Figure/Table caption), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Baseline/ablation | VAP outperforms other baselines across all scenarios. | fair input/data/compute/action matching | p. 7 (5.1. Experimental Setup), p. 8 (5.3. Results on Simulation Benchmarks), p. 8 (5.2. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 42 / Figure/Table caption - extractive body cue:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain largely concentrated near the intended personal object, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as <my cup>, because they can only interpret ...
- **p. 9 / 5.5. Error Case Analysis - extractive body cue:** First, the sequential factorization of grounding and manipulation does not itself bound performance: reliable spatio-temporal tracking maintains target identity through several seconds of complete invisibility, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. VAP builds a visual memory from a few reference images, grounds the target with frozen detection and segmentation, and prompts a frozen VLA ...
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive body cue:** Failure analysis across benchmarks.
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive body cue:** We report the overall failure rate for each setting.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 1 (1. Introduction)이다.
