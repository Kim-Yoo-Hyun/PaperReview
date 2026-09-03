# SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, semantic reasoning, Planning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This brittleness stems from two fundamental limitations in current VLA architectures.를 문제로 두고, Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have emerged as a promising paradigm where pretrained Vision-Language Models (VLMs) serve as System 2 for high-level reasoning, connected to action experts ...
- **p. 1 / Abstract - extractive body cue:** However, current works fail to genuinely leverage VLM capabilities: VLMs produce latent embeddings that lack semantic interpretability, providing ambiguous and unstable guidance to downstream policies, ...
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce SemanticVLA, which leverages VLM reasoning through synergistic dual-path design.
- **p. 1 / Abstract - extractive body cue:** Explicit trace reasoning generates interpretable spatial waypoints as textual coordinate sequences through the VLM's native language interface, directly reusing its pretrained spatial grounding to provide ...
- **p. 1 / Abstract - extractive body cue:** Latent action tokens complement trace reasoning by learning compact visuomotor primitives grounded in visual observations, providing more fine-grained action †Corresponding authors. representations beyond pure coordinate ...
- **p. 2 / 1. Introduction - extractive body cue:** This brittleness stems from two fundamental limitations in current VLA architectures.

## Core Idea

- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **p. 2 / 1. Introduction - extractive body cue:** By bridging VLM reasoning and action control through semantically explicit trace and compact latent action tokens, our approach enables genuine reasoning rather than action memorization.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce SemanticVLA, a dual-path reasoning framework that synergistically combines explicit trace reasoning and latent action planning.
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 4 / 3.2. VLM Co-training with Trace and Latent Action - extractive body cue:** This synergy enables latent tokens to compensate for trace's coordinate imprecision through learned visual attention to task-relevant context, while trace scaffolding filters visual variations to ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** Following established architectures [4, 11], the decoder predicts velocity fields through cross-attention between latent and visual features, generating actions via iterative denoising.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** We extract DINOv2 [42] features hvisual from observations ot, ot+H, then combine with trace codebook entry ctrace qtrace through fusion encoder ϕfused enc employing cross-attention, ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to condition the flow ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For latent action guidance, we obtain hidden states Ea = {hq1, . . . , hqN } from the VLM's final layer, encoding multimodal reasoning over visual observations, spatial plans, and language ... | image/video, language instruction, proprioception과 history | p. 5 (3.3. Flow Matching Action Decoding), p. 5 (3.3. Flow Matching Action Decoding) |
| State/latent | latent, action, guidance, obtain, hidden, states, hqN, VLM, final, layer, encoding, multimodal | language-grounded task state와 action-policy context | p. 5 (3.3. Flow Matching Action Decoding), p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.2. VLM Co-training with Trace and Latent Action) |
| Output/action | The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to condition the flow matching action decoder for continuous robot control. ... | continuous action, pose 또는 action chunk | p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.2. VLM Co-training with Trace and Latent Action), p. 4 (3.1. Semantic Latent Action Tokenizer) |
| Objective/outcome | The training objective of latent action tokenizer LLAT combines: LLAT = La vq + Ltrace recon + Lvisual recon (3) where La vq = ∥sg(ϕfused enc (·)) -ca qa∥2 + β∥ϕfused enc ... | instruction following, task success, generalization과 latency | p. 4 (3.1. Semantic Latent Action Tokenizer), p. 3 (3.1. Semantic Latent Action Tokenizer), p. 4 (3.2. VLM Co-training with Trace and Latent Action) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **p. 2 / 1. Introduction - extractive body cue:** By bridging VLM reasoning and action control through semantically explicit trace and compact latent action tokens, our approach enables genuine reasoning rather than action memorization.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce SemanticVLA, a dual-path reasoning framework that synergistically combines explicit trace reasoning and latent action planning.
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 4 / 3.2. VLM Co-training with Trace and Latent Action - extractive body cue:** This synergy enables latent tokens to compensate for trace's coordinate imprecision through learned visual attention to task-relevant context, while trace scaffolding filters visual variations to ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive body cue:** As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories.
- **p. 6 / 4.1. Simulation Benchmarks - extractive body cue:** SemanticVLA achieves 65.1% average success rate, outperforming competitive baselines and demonstrating effective transfer of trace-guided spatial understanding across manipulation primitives.
- **p. 7 / 4.3. Instruction Variance Robustness - extractive body cue:** Dashed bars: success rates with original instructions; Solid bars: rephrased instructions with similar task semantics. across perturbations, only 9.4% on LIBERO and significantly outperforming baselines ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks) |
| Embodiment/environment | Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable performance under instruction variation ... | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 6 (4.1. Simulation Benchmarks) |
| Dataset/benchmark | We further conduct real-world experiments using a Franka Research 3 robot arm with Franka hand and two Intel RealSense D435 cameras. | role, split, size and leakage | p. 5 (4. Experiments), p. 6 (4.1. Simulation Benchmarks), p. 6 (4.2. Real-world Robotics Evaluation), p. 7 (4.3. Instruction Variance Robustness) |
| Metric | Solid lines: success rate (right yaxis); Dashed lines: latent prediction accuracy (left y-axis). training. | definition, denominator, direction and uncertainty | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 5 (4. Experiments) |
| Baseline/ablation | As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | fair input/data/compute/action matching | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks), p. 7 (4.3. Instruction Variance Robustness) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce a ...
- **p. 8 / 5. Conclusion - extractive body cue:** We believe this synergistic fusion of explicit trace and latent action tokens pathways provides a promising and principled approach to designing more effective VLA architectures ...
- **p. 5 / 4. Experiments - extractive body cue:** Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable performance ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. SemanticVLA Architecture Overview. Our dual-path framework synergistically combines explicit trace reasoning and implicit latent action planning. The VLM processes visual observations and language ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive body cue:** SimplerEnv [32] probes cross-domain robustness through visual appearance shifts on short-horizon WidowX tasks.
- **p. 6 / 4.1. Simulation Benchmarks - extractive body cue:** Reasoningenhanced approaches such as ThinkAct, MolmoAct, and Magma substantially outperform direct action prediction models including OpenVLA and RT-1-X, confirming the importance of structured reasoning for ...
- **p. 7 / 4.3. Instruction Variance Robustness - extractive body cue:** Following recent robustness protocols [17, 18], we test on instruction perturbations across LIBERO and SimplerEnv.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This brittleness stems from two fundamental limitations in current VLA architectures.를 문제로 두고, Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.1. Semantic Latent Action Tokenizer), p. 5 (3.3. Flow Matching Action Decoding), p. 3 (3.1. Semantic Latent Action Tokenizer) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
