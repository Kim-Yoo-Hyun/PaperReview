# Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=P64X2q1n1H.
> PDF retrieval source: https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=P64X2q1n1H
- Full-text retrieval: https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite their effectiveness, existing CoT-based methods face two fundamental challenges.를 문제로 두고, Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual and visual modalitie ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception ...
- **p. 1 / Abstract - extractive body cue:** We propose Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multimodal CoT reasoning into continuous latent representations for embodied action.
- **p. 1 / Abstract - extractive body cue:** LaRA-VLA performs unified reasoning and prediction in latent space, eliminating explicit CoT generation at inference time and enabling efficient, actionoriented control.
- **p. 1 / Abstract - extractive body cue:** To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and ...
- **p. 1 / Abstract - extractive body cue:** We construct two structured CoT datasets and evaluate LaRA-VLA on both simulation benchmarks and long-horizon real-robot manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Despite their effectiveness, existing CoT-based methods face two fundamental challenges.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** To predict visual goal information, we introduce a dedicated <img next> token to represent predicted visual latents, which enables explicit supervision and alignment during early-stage ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...
- **p. 4 / 3. Method - extractive body cue:** In this section, we present the complete pipeline of our Latent Reasoning VLA (LaRA-VLA) framework.
- **p. 6 / 3.3. Training Procedures - extractive body cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.
- **p. 5 / 3.3. Training Procedures - extractive body cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** Specifically, action generation is performed by a 16-layer Diffusion Transformer composed of alternating self-attention and cross-attention layers, which conditions on the learned latent representations to ...
- **p. 5 / 3.3. Training Procedures - extractive body cue:** Embodied reasoning is modeled as a sequence of continuous latent states, and discrete CoT tokens are progressively replaced by latent representations during training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Vision-Language-Action (VLA) models have emerged as a promising direction for scalable, general-purpose robotic manipulation (Kim et al., 2025b; Bai et al., 2025b), as they aim to end-to-end map rich multimodal observations and ... | image/video, language instruction, proprioception과 history | p. 1 (1. Introduction), p. 4 (3.3. Training Procedures) |
| State/latent | Vision-Language-Action, VLA, models, have, emerged, promising, direction, scalable, general-purpose, robotic, manipulation, Kim | language-grounded task state와 action-policy context | p. 1 (1. Introduction), p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures) |
| Output/action | Given input images and a language instruction, the image encoder first maps the visual observation to a sequence of visual tokens, denoted as v, while the instruction text is tokenized into textual ... | continuous action, pose 또는 action chunk | p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures) |
| Objective/outcome | Concretely, action tokens are trained using an autoregressive objective, similar to Equation 1, yielding the action-token loss Lact-dis. | instruction following, task success, generalization과 latency | p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 4 (3.3. Training Procedures) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** To predict visual goal information, we introduce a dedicated <img next> token to represent predicted visual latents, which enables explicit supervision and alignment during early-stage ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...
- **p. 4 / 3. Method - extractive body cue:** In this section, we present the complete pipeline of our Latent Reasoning VLA (LaRA-VLA) framework.
- **p. 6 / 3.3. Training Procedures - extractive body cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.
- **p. 8 / 4.2. Real-World Experiments - extractive body cue:** As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T N1.5 ...
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7. Latent collapse analysis. corruption, but LaRA-VLA consistently maintains higher success rates across all perturbation types and severity lev- els. These results indicate that ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2. Real-World Experiments), p. 7 (4.1. Simulation Experiments) |
| Embodiment/environment | We evaluate the effectiveness of LaRA-VLA and the overall system through a comprehensive set of experiments spanning both simulation benchmarks and real-world robotic manipulation tasks. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments) |
| Dataset/benchmark | Based on these benchmarks, we construct two training datasets, LIBERO-LaRA and Bridge-LaRA, which are used to train LaRA-VLA. | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments), p. 7 (4.1. Simulation Experiments), p. 6 (4. Experiments) |
| Metric | On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on the Long suite, demonstrating strong object-centric reasoning and ... | definition, denominator, direction and uncertainty | p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments) |
| Baseline/ablation | (Section 4.1) • How well does LaRA-VLA perform on long-horizon real-world manipulation tasks compared to state-of-the-art approaches? | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Analysis - extractive body cue:** This suggests that the learned latent space does not collapse or become highly unstable under visual perturbations.
- **p. 9 / 5. Limitations - extractive body cue:** Although LaRA-VLA achieves fast inference and strong performance through latent chain-of-thought reasoning, several limitations remain and warrant further investigation.
- **p. 9 / 5. Limitations - extractive body cue:** Improving training efficiency while preserving stable latent reasoning remains an important direction for future work.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Robustness under visual perturbations. We report task success rates under Gaussian blur and Gaussian noise with two severity levels. H and L denote ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 12. Prompt for subtask description generation. actions without attending to explicit CoT-related tokens. Table 9 reports the results on four SimplerEnv tasks. Training with ...
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 12. Target Object Bounding Boxes. Guided by the semantic anchors, we perform open-vocabulary spatial grounding using GroundingDINO (Liu et al., 2024) and SAM3 (Carion ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite their effectiveness, existing CoT-based methods face two fundamental challenges.를 문제로 두고, Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual and visual modalitie ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training Procedures), p. 4 (3.2. Model Architecture), p. 5 (3.3. Training Procedures), p. 4 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
