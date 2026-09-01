# Method - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JO0IsGJg16; PDF retrieval source: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 6 (3.5. Data Collection and Implementation Details)): The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states m, and the observations o.

## Method Body Digest

- **p. 4 / 3.1. Overview - extractive PDF cue:** The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states ...
- **p. 4 / 3.1. Overview - extractive PDF cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** In our implementation, we use the proprioceptive states m as the condition input.
- **p. 5 / 3.1. Overview - extractive PDF cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...
- **p. 6 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations Figure 3.
- **p. 5 / 3.1. Overview - extractive PDF cue:** Training follows standard VQ-VAE objectives (Van Den Oord et al., 2017), combining reconstruction losses with codebook and commitment regularization terms: Lvis = ∥ˆct+h -ct+h∥1 + ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** The overall objective integrates reconstruction and alignment losses from different data sources.
- **p. 4 / 3.1. Overview - extractive PDF cue:** By employing an alignment regularization loss, our design provides complementary guidance for action prediction and enables learning from heterogeneous sources, such as actionless human demonstrations.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Addressing the limitations of unimodal representations and inspired by human supramodal cognition, we propose X Robotic Model 1 (XR-1) to achieve cross-data exploitation and cross-embodiment ...
- **p. 4 / 3.1. Overview - extractive PDF cue:** We introduce XR-1, a scalable framework for cross-robot VLA learning (Figure 2), structured in three stages.

## Source Evidence Cues

- **p. 4 / 3.1. Overview - extractive PDF cue:** The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states ...
- **p. 4 / 3.1. Overview - extractive PDF cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** In our implementation, we use the proprioceptive states m as the condition input.
- **p. 5 / 3.1. Overview - extractive PDF cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...
- **p. 6 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations Figure 3.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 3); 3. Methodology (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction ... | p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ... | p. 4 (3.1. Overview), p. 5 (3.1. Overview) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In our implementation, we use the proprioceptive states m as the condition input. | p. 5 (3.1. Overview), p. 5 (3.1. Overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1. Overview - extractive PDF cue:** Training follows standard VQ-VAE objectives (Van Den Oord et al., 2017), combining reconstruction losses with codebook and commitment regularization terms: Lvis = ∥ˆct+h -ct+h∥1 + ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** The overall objective integrates reconstruction and alignment losses from different data sources.
- **p. 4 / 3.1. Overview - extractive PDF cue:** By employing an alignment regularization loss, our design provides complementary guidance for action prediction and enables learning from heterogeneous sources, such as actionless human demonstrations.
- **p. 4 / 3.1. Overview - extractive PDF cue:** By progressing from the unified representation to task-specific refinement, this design ensures scalability and adaptability.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | inference, step, policy, receives, language, instruction, multimodal, observations, where, denotes, RGB, images, external, robot-mounted | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | inference, step, policy, receives, language, instruction, multimodal, observations, where, denotes | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, Robotic, Model, XR-1, scalable, three-stage, framework | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Training, follows, standard, VQ-VAE, objectives, Van, Den, Oord, combining, reconstruction | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Overview - extractive PDF cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **p. 4 / 3.1. Overview - extractive PDF cue:** The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** In our implementation, we use the proprioceptive states m as the condition input.
- **p. 5 / 3.1. Overview - extractive PDF cue:** The policy π(·) follows a standard VLA design with a VLM F(·) and an action head H(·).
- **p. 2 / 1. Introduction - extractive PDF cue:** Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors ...
- **p. 2 / 1. Introduction - extractive PDF cue:** XR-1 outperforms state-of-the-art baselines such as π0.5, π0, RDT, UniVLA, and GR00T-N1.5 across challenging scenarios involving bimanual collaboration, dexterous manipulation, deformable objects, contact-rich interactions, dynamic ...
- **p. 3 / 1. Introduction - extractive PDF cue:** XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations while an alignment loss enforces consistent multimodal embeddings across embodiments via UVMC. • We validate ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Given two frames ct and ct+h, the vision encoder Evis(·) produces a latent code zvis = Evis(ct, ct+h), which compresses temporal changes ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To encode temporal visual variations in the vision branch, we adopt an asymmetric VQ-VAE (Zhu et al., 2023c) structure tailored for future-frame ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Overview - extractive PDF cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** motion, decoder, Dmo, then, takes, latent, embedding, optional, conditions, input, language, instruction, proprioceptive, states, observations, inference, step, policy, receives, multimodal.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 3); 3. Methodology (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer ... | p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments) |
| Action / skill decoding | Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, ... | p. 24 (Figure/Table caption), p. 7 (4.2. Results on Real-World Robotic Tasks) |
| Receding execution / feedback | As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8 | p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Unseen scenario task setup on Dual-Arm Franka. embodiment performance, are provided in Appendix E. Lightweight Models. To validate the applicability of our methods ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We first analyze the scaling behavior with respect to the volume of Stage-1 pretraining data, using the full XR-1 model without any subsequent fine-tuning.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** To disentangle the contribution of each component in XR1, we conduct ablations on six manipulation tasks using the Dual-Arm UR-5e.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, we also conduct ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Additional experimental results and analysis for the UVMC ablation study, as well as for Ego4D and crossembodied knowledge transfer ablations on enhanced single7
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** We also provide a lightweight variant, XR-1-Light, built upon SwitchVLA (Li et al., 2025a), which uses Florence-2 (Xiao et al., 2024) to reduce computational cost ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 14. Ablation study of UVMC. Exp. Codebook Category×Embed.Dim UVMC Token Stage-1&2&3 DUR-Clean DUR-Find

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 6 (3.5. Data Collection and Implementation Details), objective p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview), temporal p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.5. Data Collection and Implementation Details), p. 5 (3.5. Data Collection and Implementation Details), p. 6 (4.1. Experiment Setup), p. 6 (3.5. Data Collection and Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
