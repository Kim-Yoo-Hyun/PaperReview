# SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=dt940loCBT.
> PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/e185c7be603426028c32ae1003a59d78-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=dt940loCBT
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2025/file/e185c7be603426028c32ae1003a59d78-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention level [25, 26] and the unique safety를 문제로 두고, Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we introduce Safety-CHORES.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action models (VLAs) show potential as generalist robot policies.
- **p. 1 / Abstract - extractive body cue:** However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans.
- **p. 1 / Abstract - extractive body cue:** How can safety constraints be explicitly integrated into VLAs?
- **p. 1 / Abstract - extractive body cue:** We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via ...
- **p. 1 / Abstract - extractive body cue:** Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks.
- **p. 1 / 1 Introduction - extractive body cue:** However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention ...
- **p. 1 / 1 Introduction - extractive body cue:** While significant progress has been made in task performance, the explicit integration of safety mechanisms remains an open challenge.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we ...
- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are: • Integrated Safety Approach (ISA) Exploration: We conduct a comprehensive investigation into an ISA for VLA safety alignment.
- **p. 1 / 1 Introduction - extractive body cue:** Embodied AI aims to develop a generalist policy that can perform perception, interaction, reasoning, and adaptation in the physical world [1].
- **p. 33 / C.3 Model Selection - extractive body cue:** 2) Long-Horizon Reasoning: The 100-frame transformer context window (Table 6 in SPOC) allows modeling temporal dependencies critical for anticipating and avoiding cumulative safety risks during ...
- **p. 32 / C.3 Model Selection - extractive body cue:** 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.
- **p. 33 / C.3 Model Selection - extractive body cue:** We use AllenAct [85] and OmniSafe [39] as the training framework.
- **p. 32 / C.3 Model Selection - extractive body cue:** 2) Visual Encoder: A goal-conditioned transformer encoder fuses RGB observations from dual cameras (navigation and manipulation views) with language embeddings, enabling cross-modal fusion.
- **p. 33 / C.3 Model Selection - extractive body cue:** This combination of architectural strengths and training scalability makes SPOC an optimal base model for this work.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate cost ct is an aggregation of K ... | image/video, language instruction, proprioception과 history | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training) |
| State/latent | reward, function, current, state, language, instruction, total, immediate, cost, aggregation, distinct, types | language-grounded task state와 action-policy context | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 1 (1 Introduction) |
| Output/action | At each time step t, the policy considers a temporal context window defined by ht = {(ot-n, at-n), (ot-n+1, at-n+1), . . . , (ot-1, at-1), ot}, which contains the history of ... | continuous action, pose 또는 action chunk | p. 32 (C.1 Details of SafeRL Training), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | The combined loss L balances reward maximization and constraint satisfaction Lagrangian multiplier λ, where λ →0 prioritizes reward and λ →∞enforces strict constraint adherence. | instruction following, task success, generalization과 latency | p. 32 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we ...
- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are: • Integrated Safety Approach (ISA) Exploration: We conduct a comprehensive investigation into an ISA for VLA safety alignment.
- **p. 1 / 1 Introduction - extractive body cue:** Embodied AI aims to develop a generalist policy that can perform perception, interaction, reasoning, and adaptation in the physical world [1].
- **p. 33 / C.3 Model Selection - extractive body cue:** 2) Long-Horizon Reasoning: The 100-frame transformer context window (Table 6 in SPOC) allows modeling temporal dependencies critical for anticipating and avoiding cumulative safety risks during ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on these ...
- **p. 9 / 5 Experiments - extractive body cue:** The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success rate ...
- **p. 8 / 5 Experiments - extractive body cue:** 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 0.00 ...
- **p. 9 / 5 Experiments - extractive body cue:** The average changes reported at the bottom of Table 2 indicate that, the safety benefits and reasonable task performance achieved by ISA are largely preserved ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 9 (5 Experiments) |
| Embodiment/environment | 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 Safety-CHORES - CC 0.0 0.2 0.4 0.6 0.8 1.0 +0.064 ... | hardware/simulator version and reset protocol | p. 7 (5 Experiments), p. 10 (5 Experiments) |
| Dataset/benchmark | The most immediate goal is to bridge the sim-to-real gap by validating and adapting the ISA framework on complex, real-world robotic platforms. | role, split, size and leakage | p. 7 (5 Experiments), p. 10 (5 Experiments), p. 39 (C.4 Experimental Environment and Costs), p. 34 (C.4 Experimental Environment and Costs) |
| Metric | 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook-DINOv2 ... | definition, denominator, direction and uncertainty | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Baseline/ablation | ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods. | fair input/data/compute/action matching | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more ...
- **p. 10 / 6 Conclusion - extractive body cue:** Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of explicit ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 8: Setup for sim-to-real validation. The physical platform consists of dual Realman RM75- 6F arms equipped with PsiBot G0-R hands, perceived through an egocentric ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 5: GPT-4 Response. Blind Spots The robot, while executing the action move-ahead in the LivingRoom, collided with scooter. This collision with an object previously ...
- **p. 34 / C.4 Experimental Environment and Costs - extractive body cue:** Algorithm 1 Corner Safety Component Require: Agent Position p, Detection Radius r, Corner Threshold ϵ, Map Points Set S 1: Integer N ←0 2: Integer ...
- **p. 8 / 5 Experiments - extractive body cue:** For FLaRe, higher safety costs are more prevalent in task failures, suggesting that unsafe behaviors often contribute to or coincide with failure.
- **p. 8 / 5 Experiments - extractive body cue:** The upper bound of unsafe behavior severity in ISA is reduced to 1/35th of that in FLaRe, indicating a significant mitigation of catastrophic safety failures.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention level [25, 26] and the unique safety를 문제로 두고, Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we introduce Safety-CHORES.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 32 (C.3 Model Selection) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
