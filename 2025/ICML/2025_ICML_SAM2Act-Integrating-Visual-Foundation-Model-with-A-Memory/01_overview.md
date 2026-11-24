# SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/fang25c.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168185. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Haoquan Fang, Markus Grotz, Wilbert Pumacay, Yi Ru Wang, Dieter Fox, Ranjay Krishna, Jiafei Duan
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning
- Official paper: https://proceedings.mlr.press/v267/fang25c.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25c/fang25c.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

SAM2Act는 다중 시점 시각 특징을 쓰는 조작 정책이며, SAM2Act+는 이전 관측이 필요한 과제를 위해 공간 기억을 추가한 모델이다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation systems operating in diverse, dynamic environments must exhibit three critical abilities: multitask interaction, generalization to unseen scenarios, and spatial memory.
- **p. 1 / Abstract - extractive body cue:** While significant progress has been made in robotic manipulation, existing approaches often fall short in generalization to complex environmental variations and addressing memorydependent tasks.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce SAM2Act, a multi-view robotic transformerbased policy that leverages multi-resolution upsampling with visual representations from largescale foundation model.
- **p. 1 / Abstract - extractive body cue:** SAM2Act achieves a state-of-the-art average success rate of 86.8% across 18 tasks in the RLBench benchmark, and demonstrates robust generalization on The Colosseum benchmark, with ...
- **p. 1 / Abstract - extractive body cue:** Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite these advances, important challenges remain, including improving multitask performance, enhancing generalization to novel environment configurations, and integrating memory mechanisms for tasks requiring episodic recall.
- **p. 1 / 1. Introduction - extractive body cue:** Significant progress has been made in robotic manipulation through prior work.

## Core Idea

- **p. 3 / 4. Method - extractive body cue:** Our method, SAM2Act, enables precise 3D manipulation with strong generalization across environmental and objectlevel variations.
- **p. 2 / 1. Introduction - extractive body cue:** First, we introduce a novel model formulation that leverages visual foundation models to solve high-precision, memorydependent manipulation tasks.
- **p. 6 / 4. Method - extractive body cue:** SAM2Act+: Action Memory Architecture for Improved Spatial Awareness in Past Observations To extend the SAM2Act architecture (Section 4.1) with memory-based capabilities inspired by SAM2, we ...
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SAM2Act, a multi-view robotics transformerbased policy that enhances feature representation by integrating multi-resolution upsampling with visual embeddings from large-scale foundation models.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose MemoryBench, a evaluation benchmark for assessing spatial memory in behavior cloning models.
- **p. 6 / 4. Method - extractive body cue:** SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of steps N, number ...
- **p. 4 / 4. Method - extractive body cue:** These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations.
- **p. 4 / 4. Method - extractive body cue:** The coarse and fine SAM2Act Modules share the same architecture, with the fine branch generating additional features to predict actions beyond translation, while the coarse ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These embeddings, generated at three resolution levels, are combined with virtual images containing RGB, depth, 3D translation coordinates, and language instructions before being fed into the multi-view transformer. | image/video, language instruction, proprioception과 history | p. 4 (4. Method), p. 4 (4. Method) |
| State/latent | embeddings, generated, three, resolution, levels, combined, virtual, images, containing, RGB, depth, translation | language-grounded task state와 action-policy context | p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method) |
| Output/action | These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations. | continuous action, pose 또는 action chunk | p. 4 (4. Method), p. 5 (4. Method), p. 6 (4. Method) |
| Objective/outcome | To adapt the SAM2 image encoder to our domain, we finetune it using Low-Rank Adaptation (LoRA) (Hu et al., 2021) with a default rank of 16, which enables domain adaptation with minimal ... | instruction following, task success, generalization과 latency | p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method) |

## Main Claims and Actual Contribution

- 고해상도 시각 정보를 복원하는 다중 해상도 정책을 구성한 뒤, 기억 인코더·저장소·주의 모듈을 더해 과거 장면을 검색하도록 확장했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=6)
- 기본 정책은 RLBench와 Colosseum에서 조작과 교란 강건성을 평가하고, 기억 확장은 공간 기억과 이전 행동 회상이 필요한 MemoryBench에서 시험했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/fang25c/fang25c.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (5.2. Performances Across 18 RLBench Tasks) |
| Embodiment/environment | We benchmark SAM2Act in both simulated and real-world environments. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Dataset/benchmark | We validate SAM2Act in real-world scenarios using a Franka Emika Panda robot with a Robotiq 2F-85 gripper and a exocentric Intel RealSense D455 depth sensor (more in Appendix I). | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Metric | Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations without perturbations. | definition, denominator, direction and uncertainty | p. 8 (5.3. Semantic Generalization across Tasks), p. 7 (5.2. Performances Across 18 RLBench Tasks), p. 7 (5.1. Experimental Setup) |
| Baseline/ablation | Our method, SAM2Act, outperforms all baselines, achieving a significant performance margin of 5.8% over RVT-2 (Goyal et al., 2024), the prior state-of-the-art 3D keyframe-based BC policy. | fair input/data/compute/action matching | p. 7 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 8 (5.5. Real-robot Evaluations) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.4. Performance on MemoryBench - extractive body cue:** In Table 3, we evaluate SAM2Act+ against SoTA 3D BC model, RVT-2 on MemoryBench, training all models in a single-task setting to isolate memory-related challenges ...
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act generalize ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Simulation and Real Tasks. We demonstrate the effectiveness of SAM2Act+ in solving memory-based tasks by evaluating it against baselines on the three benchmark ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these components ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Each task undergoes 10 in-distribution and 10 out-of-distribution trials, including environmental perturbations, measuring total success.
- **p. 7 / 5.3. Semantic Generalization across Tasks - extractive body cue:** However, to truly assess generalization performance, policies must remain robust against both environmental and objectlevel perturbations.
- **p. 8 / 5.5. Real-robot Evaluations - extractive body cue:** We compare RVT2 against SAM2Act for the first three tasks and SAM2Act+ on the last real-world tasks (indicated with *), evaluating performance both in-distribution and ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4. Method)이다.
