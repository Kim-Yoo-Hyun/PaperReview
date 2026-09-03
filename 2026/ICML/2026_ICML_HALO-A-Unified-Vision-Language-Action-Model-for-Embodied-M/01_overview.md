# HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=lduY9csXqw.
> PDF retrieval source: https://openreview.net/pdf/f0a4b4b3d1775cb04d6e602c68bf3c4914033562.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=lduY9csXqw
- Full-text retrieval: https://openreview.net/pdf/f0a4b4b3d1775cb04d6e602c68bf3c4914033562.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion and contact.를 문제로 두고, To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but often struggle in long-horizon or out-of-distribution scenarios due to the lack of explicit mechanisms ...
- **p. 1 / Abstract - extractive body cue:** Recent works introduce textual chain-ofthought or visual subgoal prediction within VLA models to reason, but still fail to offer a unified human-like reasoning framework for ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning through a sequential process of textual task reasoning, ...
- **p. 1 / Abstract - extractive body cue:** We instantiate HALO with a Mixture-of-Transformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts while allowing seamless cross-expert collaboration.
- **p. 1 / Abstract - extractive body cue:** To enable HALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will ...
- **p. 1 / 1. Introduction - extractive body cue:** Recent work has sought to address this limitation by introducing intermediate reasoning processes like human.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.
- **p. 2 / 1. Introduction - extractive body cue:** Third, we propose a carefully designed training recipe that combines broad generalization with embodied reasoning specialization.
- **p. 1 / 1. Introduction - extractive body cue:** This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios-such as novel layouts, unfamiliar objects, or contact-rich interactions-where successful execution depends more on deliberation and ...
- **p. 5 / 3.4. Training Recipe - extractive body cue:** This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k (Liu et al., ...
- **p. 6 / 3.4. Training Recipe - extractive body cue:** Crucially, we employ a dual-path visual pathway that integrates complementary semantic and spatial representations: a ViT branch first captures high-level semantic context, while a VAE ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks.
- **p. 4 / 3.2. Unified Architecture - extractive body cue:** By default, the model operates as an auto-regressive planner; however, the generation of specific tokens (e.g., ⟨visual start⟩or ⟨action start⟩) triggers the routing of hidden ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Let τ = {(ot, l, at)}T t=1 denote a trajectory, comprising visual observations ot ∈O, language instructions l ∈L, and continuous actions at ∈A.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks. | image/video, language instruction, proprioception과 history | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| State/latent | Traditional, VLA, models, typically, learn, monolithic, policy, ot-k, directly, maps, history, observations | language-grounded task state와 action-policy context | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.3. EM-CoT Data Pipeline) |
| Output/action | Let τ = {(ot, l, at)}T t=1 denote a trajectory, comprising visual observations ot ∈O, language instructions l ∈L, and continuous actions at ∈A. | continuous action, pose 또는 action chunk | p. 3 (3.1. Problem Formulation), p. 5 (3.3. EM-CoT Data Pipeline), p. 2 (1. Introduction) |
| Objective/outcome | The fine-tuning objective minimizes the joint loss: Lft = Lr + Lˆo + La, (5) where Lr, Lˆo, and La represent the losses for textual reasoning, visual subgoal generation, and action prediction, ... | instruction following, task success, generalization과 latency | p. 6 (3.4. Training Recipe), p. 5 (3.3. EM-CoT Data Pipeline), p. 5 (3.4. Training Recipe) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.
- **p. 2 / 1. Introduction - extractive body cue:** Third, we propose a carefully designed training recipe that combines broad generalization with embodied reasoning specialization.
- **p. 1 / 1. Introduction - extractive body cue:** This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios-such as novel layouts, unfamiliar objects, or contact-rich interactions-where successful execution depends more on deliberation and ...
- **p. 5 / 3.4. Training Recipe - extractive body cue:** This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k (Liu et al., ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves ...
- **p. 6 / 4. Experiments - extractive body cue:** Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative EM-CoT ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** On fine-grained tasks such as "Blocks Ranking Size" and "Stamp Seal," HALO achieves a multi-fold increase in success rates compared to baselines, demonstrating its ability ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** While π0 and RDT-1B exhibit some degree of robustness, they plateau at significantly lower performance levels, whereas HALO continues to improve as it incorporates more ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.5. Real-World Results), p. 6 (4. Experiments) |
| Embodiment/environment | The simulation dataset contains 2,500 expert demonstrations (50 per task) collected in clean environments, while the real-world dataset consists of 320 demonstrations (80 per task). | hardware/simulator version and reset protocol | p. 7 (4.1. Experiment Settings), p. 7 (4.2. Simulation Results) |
| Dataset/benchmark | Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative EM-CoT reasoning, particularly under novel settings; (iii) w ... | role, split, size and leakage | p. 7 (4.1. Experiment Settings), p. 7 (4.2. Simulation Results), p. 6 (4. Experiments), p. 8 (4.5. Real-World Results) |
| Metric | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves the highest success rates across all tasks. | definition, denominator, direction and uncertainty | p. 8 (4.5. Real-World Results), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |
| Baseline/ablation | It can be observed that HALO consistently outperforms all competitive baselines across both Easy and Hard settings. | fair input/data/compute/action matching | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.5. Real-World Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Ablation Study - extractive body cue:** Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational requirement ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** Particularly, the consistent huge relative performance gap (i.e., 73.5% and 62.0%) between HALO and π0 especially on Hard tasks indicates that HALO can also handle ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Attention Masking Strategy for EM-CoT. (1) Spa- tial and semantic tokens utilize bidirectional attention within frames. (2) Noise tokens attend bidirectionally to each ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** These results underscore the effectiveness and robustness of HALO for complex robotic manipulation.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion and contact.를 문제로 두고, To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.4. Training Recipe) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
