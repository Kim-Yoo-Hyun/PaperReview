# CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2601.09512.
> PDF retrieval source: https://arxiv.org/pdf/2601.09512. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://arxiv.org/abs/2601.09512
- Full-text retrieval: https://arxiv.org/pdf/2601.09512
- Code/Project: https://tum-lsy.github.io/CLARE/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].를 문제로 두고, As our method is architecture-agnostic, we keep the following sections general.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** To teach robots complex manipulation tasks, a common approach is to fine-tune a pre-trained vision-languageaction model (VLA) on task-specific data.
- **p. 1 / Abstract - extractive body cue:** However, since this recipe updates existing representations, it is unsuitable for longterm operation in the real world, where robots must continually adapt to new tasks ...
- **p. 1 / Abstract - extractive body cue:** Existing continual learning methods for robotics commonly require storing previous data (exemplars), struggle with long task sequences, or rely on task identifiers for deployment.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- **p. 1 / Abstract - extractive body cue:** CLARE introduces lightweight modular adapters into selected VLA modules and autonomously expands the model only where necessary when learning a new task, guided by layer-wise ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].
- **p. 1 / I. INTRODUCTION - extractive body cue:** This long-term adaptability, known as continual or lifelong learning [1], remains an open challenge in robotics despite decades of research [2]-[4].

## Core Idea

- **p. 3 / IV. METHODOLOGY - extractive body cue:** As our method is architecture-agnostic, we keep the following sections general.
- **p. 5 / IV. METHODOLOGY - extractive body cue:** We found that introducing at least some new parameters per task is essential for the policy to acquire and retain novel skills.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Prior work [37], [38] has shown that a large fraction of factual associations and high-level knowledge in transformerbased LLMs is stored inside mid-layer feedforward network ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ensure they have ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Then, the routing mechanism activates only adapters from earlier stages in layer ℓ1 during training of Ai ℓ2.
- **p. 5 / IV. METHODOLOGY - extractive body cue:** As a consequence, the input features xℓ2 to layer ℓ2 when performing task Tn are different from those seen during training of Ai ℓ2.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 23: Train Dn ℓof all layers ℓ∈E from Dn via (5). consisting of camera images I1 t , . . . , INc t , proprioceptive state qt and language command l, ... | image/video, language instruction, proprioception과 history | p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP) |
| State/latent | Train, layers, consisting, camera, images, INc, proprioceptive, state, language, command, generates, action | language-grounded task state와 action-policy context | p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP) |
| Output/action | We assume the availability of a base VLA policy π0 = πθ0 with model parameters θ0 that takes as input an observation ot = (I1 t , . . . , INc ... | continuous action, pose 또는 action chunk | p. 2 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP) |
| Objective/outcome | We adopt the standard conditional flow matching loss L(θn)= Es,(A1,o),A0 | instruction following, task success, generalization과 latency | p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 3 / IV. METHODOLOGY - extractive body cue:** As our method is architecture-agnostic, we keep the following sections general.
- **p. 5 / IV. METHODOLOGY - extractive body cue:** We found that introducing at least some new parameters per task is essential for the policy to acquire and retain novel skills.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random ...
- **p. 6 / V. EVALUATION - extractive body cue:** CLARE achieves the highest overall performance, as measured by AUC, outperforming the best baseline, ER, by about 10 to 14 percentage points.
- **p. 6 / V. EVALUATION - extractive body cue:** Backbone Expandable layers AUC ↑ FWT ↑ NBT ↓ DiT-Dec Linear projection 75.1±1.3 75.0±1.4 1.9±0.4 Decoder 41.8±2.4 45.5±3.8 7.0±1.7 DiT-EncDec Encoder 65.4±2.7 66.5±2.2 1.7±1.2 Decoder ...
- **p. 7 / V. EVALUATION - extractive body cue:** CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available.
- **p. 5 / V. EVALUATION - extractive body cue:** We conduct extensive simulation and real-world experiments with a focus on the following research questions: • Q1: Which layers are best suited for expansion? • ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: CLARE sequentially adds adapters and discriminators as side branches to selected VLA modules. Top: During inference, our router activates only the most relevant ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION) |
| Embodiment/environment | We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and 2000 episodes from the DROID dataset [9]. | hardware/simulator version and reset protocol | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Dataset/benchmark | Training takes about one hour per simulation task and five hours per real-world task on an NVIDIA RTX 5090 GPU. | role, split, size and leakage | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Metric | Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random seeds, and the shaded regions indicate the ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Baseline/ablation | 5) Baselines: We include seven baselines for continual learning without oracle task IDs. | fair input/data/compute/action matching | p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. EVALUATION - extractive body cue:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.
- **p. 7 / 5. LEGO - extractive body cue:** SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous tasks.
- **p. 7 / V. EVALUATION - extractive body cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...
- **p. 6 / V. EVALUATION - extractive body cue:** As shown in Figure 4, CLARE can sequentially learn and retain 40 distinct tasks, demonstrating the scalability and robustness of our autonomous routing strategy.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].를 문제로 두고, As our method is architecture-agnostic, we keep the following sections general.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
