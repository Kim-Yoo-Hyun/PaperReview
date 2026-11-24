# LAGEA: Language Guided Embodied Agents for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/60801.
> PDF retrieval source: https://openreview.net/pdf/28f8573440fbd9bb2ac48d0e31f3573d128fcf46.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Abdul Monaf Chowdhury, Akm Moshiur Rahman Mazumder, Safaeid Hossain Arib, Rabeya Akter
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning
- Official paper: https://icml.cc/virtual/2026/poster/60801
- Full-text retrieval: https://arxiv.org/pdf/2509.23155.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

LAGEA는 조작 시도의 결정적 순간에 VLM의 언어 피드백을 연결하고 이를 시간 단계별 강화학습 보상으로 변환한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation benefits from foundation models that describe goals, but today's agents still lack a principled way to learn from their own mistakes.
- **p. 1 / Abstract - extractive body cue:** We ask whether natural language can serve as feedback, an error-reasoning signal that helps embodied agents diagnose what went wrong and correct course.
- **p. 1 / Abstract - extractive body cue:** We introduce LAGEA (Language Guided Embodied Agents), a framework that turns episodic, schema-constrained reflections from a vision language model (VLM) into temporally grounded guidance for ...
- **p. 1 / Abstract - extractive body cue:** LAGEA summarizes each attempt in concise language, localizes the decisive moments in the trajectory, aligns feedback with visual state in a shared representation, and converts ...
- **p. 1 / Abstract - extractive body cue:** This design yields dense signals early when exploration needs direction and gracefully recedes as competence grows.
- **p. 1 / 1. Introduction - extractive body cue:** Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Learning from mistakes requires detecting failures and causal understanding.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** For this purpose, we present our framework LAGEA, which addresses this by using VLMs to generate episodic natural-language reflections on a robot's 1.
- **p. 2 / 1. Introduction - extractive body cue:** Our core contributions are: • We present LAGEA, an embodied VLM-RL framework that generates causal episodic feedback which are localized in time to turn failures ...
- **p. 3 / 3. Methodology - extractive body cue:** Our framework overview is given in Figure 1.
- **p. 4 / 3.1.2. KEY FRAME GENERATION - extractive body cue:** They are later used in feedback alignment, where each timestep's contribution is scaled by ˆwt so imagefeedback geometry is learned primarily from causal moments, and ...
- **p. 4 / 3.1.3. FEEDBACK ALIGNMENT - extractive body cue:** The first enforces absolute calibration: the diagonal cosine ψt = ⟨zt, zf⟩is treated as a logit (scaled by temperature τbce) and supervised with the per-step ...
- **p. 4 / 3.2. Reward Generation - extractive body cue:** We define a goal potential ϕt by averaging instruction text- and image-goal affinities, then shape its temporal difference and get the goal-delta reward, rgoal t ...
- **p. 3 / 3.1.2. KEY FRAME GENERATION - extractive body cue:** To keep the gate deterministic and model-agnostic, we compute key frames from the goal-similarity trajectory using image embeddings.
- **p. 3 / 3. Methodology - extractive body cue:** Each episode, Qwen-2.5-VL-3B emits a compact, structured self-reflection, which we encode with a lightweight GPT-2 (Radford et al., 2019) model and pair it with keyframe-based ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We project images, instruction text, and feedback with Ei, Et, Ef and use unit-norm embeddings for the current state zt, the goal image zg, the episodic feedback zf, and the instruction text ... | image/video, language instruction, proprioception과 history | p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT) |
| State/latent | project, images, instruction, text, feedback, unit-norm, embeddings, current, state, goal, image, episodic | language-grounded task state와 action-policy context | p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 5 (3.2. Reward Generation) |
| Output/action | Key-frame weights ˆwt identify when gradients should matter; the remaining step is to make the episodic feedback f actionable by aligning it with visual states in a shared space. | continuous action, pose 또는 action chunk | p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 5 (3.2. Reward Generation), p. 1 (1. Introduction) |
| Objective/outcome | With the shared space in place, we convert progress toward the task and movement toward the feedback into dense, directional rewards. | instruction following, task success, generalization과 latency | p. 4 (3.2. Reward Generation), p. 4 (3.2. Reward Generation), p. 5 (3.2. Reward Generation) |

## Main Claims and Actual Contribution

- 언어 피드백과 시각 상태의 일치도·목표 진행도로 범위가 제한된 보상을 만들고, 실패 정도에 따라 보상 가중치를 조정한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=5)
- Meta-World MT10과 Fetch 조작에서 학습 속도와 성공률을 비교하고 언어 피드백을 시각 상태와 정렬하는 과정의 영향을 시험했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/chowdhury26a/chowdhury26a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 15 (Figure/Table caption), p. 6 (4. Experiments) |
| Embodiment/environment | Setup: We evaluate LAGEA framework on ten robotics tasks from the Meta-world MT10 benchmark (Yu et al., 2020) and Robotic Fetch (Plappert et al., 2018), utilizing sparse rewards. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Dataset/benchmark | LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 0 20 40 60 80 100 Success Rate (%) button-press-topdown-v2 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M ... | role, split, size and leakage | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| Metric | Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in brackets); higher is better. comparison highlights that while stronger VLM ... | definition, denominator, direction and uncertainty | p. 15 (Figure/Table caption), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 6 (4. Experiments) |
| Baseline/ablation | As summarized in Table 3, we report the average success rate where LAGEA consistently outperforms all baselines across the four Fetch tasks. | fair input/data/compute/action matching | p. 6 (4.1.2. RESULTS ON FETCH TASKS), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 8 (4.3.3. IMPACT OF STRUCTURED FEEDBACK) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of LAGEA framework. (a) After each rollout, key-frame selection identifies causal moments and computes per-step weights ˆwt; a VLM queried on those ...
- **p. 6 / 4.1.2. RESULTS ON FETCH TASKS - extractive body cue:** This accelerated learning is driven by the dense, corrective signals from our feedback mechanism, which fosters a more effective exploration process compared to the slower, ...
- **p. 8 / 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE - extractive body cue:** Alignment enables control-relevant geometry: (a) success/failure logit margin increases over training, (b) policy success accelerates, and (c) BCE/InfoNCE objectives co-train the shared space for LAGEA.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 9. Schema for structured feedback returned by the VLM Example structured feedback is shown for two Meta-World tasks - button-press-topdown-v2 and door-open-v2 - with ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 11. Success case with structured feedback for door-open-v2-goal-observable task. high confidence, and suggested fix=(n/a). In button-press-topdown-v2, success is attributed to a secure grasp followed ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 13. Failure case with structured feedback for door-open-v2-goal-observable task. K. Ablation To quantify the contribution of each component in LAGEA, we run controlled ablations ...
- **p. 8 / 4.3.2. KEYFRAME EXTRACTION & CREDIT - extractive body cue:** LAGEA with keyframing learns the task efficiently, while the variant without keyframing catastrophically fails.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.2. Reward Generation)이다.
