# Method - Dexterous World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.2. Scene-Action-Conditioned Video Diffusion)): (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F = {C, H}1:F , while po θ is ...

## Method Body Digest

- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F = {C, H}1:F ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** Importantly, we instantiate the generative process as a latent video diffusion model [36] conditioned on two egocentric signals: (1) a static-scene video, Π(S0; C1:F ), ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The model then simulates the resulting environment states induced by the hand action inputs under the same camera views, V1:F = Π(S0 + ∆S1:F ; ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** For each prerecorded action sequence in TRUMANS, we render three synchronized outputs: (1) the interaction video captures the full human-scene interaction from the moving egocentric ...
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** However, since this dynamics model is still required to generate S0 as part of the output conditioned on the action sequence, it becomes vulnerable to ...
- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The training objective follows the standard latent diffusion loss [36]: LLDM = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t / cs, ch)∥2 2 i .
- **p. 6 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** reconstructed scene is then rendered along the recorded camera trajectory during interaction, yielding paired static-scene videos aligned with the corresponding ground-truth interaction sequences.
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** This coupling of scene generation and dynamics breaks causal consistency, making accurate dynamic modeling difficult.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.
- **p. 2 / 1. Introduction - extractive body cue:** (2) We propose a conditioning scheme that leverages static scene videos and egocentric hand motions to model interaction-induced residual dynamics.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** 2 for the overview of our framework.

## Source Evidence Cues

- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F = {C, H}1:F ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** Importantly, we instantiate the generative process as a latent video diffusion model [36] conditioned on two egocentric signals: (1) a static-scene video, Π(S0; C1:F ), ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The model then simulates the resulting environment states induced by the hand action inputs under the same camera views, V1:F = Π(S0 + ∆S1:F ; ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** For each prerecorded action sequence in TRUMANS, we render three synchronized outputs: (1) the interaction video captures the full human-scene interaction from the moving egocentric ...
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** However, since this dynamics model is still required to generate S0 as part of the output conditioned on the action sequence, it becomes vulnerable to ...
- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The training objective follows the standard latent diffusion loss [36]: LLDM = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t / cs, ch)∥2 2 i .
- **p. 6 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** reconstructed scene is then rendered along the recorded camera trajectory during interaction, yielding paired static-scene videos aligned with the corresponding ground-truth interaction sequences.
- **Detected method headings:** 3. Method (p. 3); 3.1. Formulation of Dexterous World Models (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F ... | p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Importantly, we instantiate the generative process as a latent video diffusion model [36] conditioned on two egocentric signals: (1) a static-scene video, ... | p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | The model then simulates the resulting environment states induced by the hand action inputs under the same camera views, V1:F = Π(S0 ... | p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 5 (3.3. Paired Interaction Video Dataset Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The training objective follows the standard latent diffusion loss [36]: LLDM = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t / cs, ch)∥2 2 i .
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** This coupling of scene generation and dynamics breaks causal consistency, making accurate dynamic modeling difficult.
- **p. 4 / 3.1. Formulation of Dexterous World Models - extractive body cue:** This structure defines a clear causal process: manipulation drives state transitions in the world, and the camera trajectory determines how these changes appear visually.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** This approximation grounds the dynamics in embodied perception, enforcing a causal relation where manipulation modifies the visual state of the scene, while the camera trajectory ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (3.2. Scene-Action-Conditioned Video Diffusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, model, simplified, visual, outcome, conditionally, independent, action, input, image, given, known, dynamics, entire | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | observation, model, simplified, visual, outcome, conditionally, independent, action, input, image | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, introduce, Dexterous, World, Models, DWM, formulation | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | training, objective, follows, standard, latent, diffusion, loss, LLDM, Ez0, coupling | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** The observation model can be simplified to po θ  V1:F / S0, ∆S1:F , C1:F  , as the visual outcome V1:F is conditionally independent ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** For each prerecorded action sequence in TRUMANS, we render three synchronized outputs: (1) the interaction video captures the full human-scene interaction from the moving egocentric ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, most video models [3, 42, 52] accept only textual instruction as "action input".
- **p. 2 / 1. Introduction - extractive body cue:** Under this initialization, using the static scene video as input establishes a base output that preserves the egocentric camera motion and scene appearance without introducing ...
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F = {C, H}1:F ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The model then simulates the resulting environment states induced by the hand action inputs under the same camera views, V1:F = Π(S0 + ∆S1:F ; ...
- **p. 4 / 3.1. Formulation of Dexterous World Models - extractive body cue:** We instantiate it as a video diffusion model conditioned on the egocentric projections of the static scene and hand trajectories. where S0 remains fixed and ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We explore two variants: AdaLN (Global), which aggregates pose features over the entire sequence to provide a single global embedding, and AdaLN ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Given a static 3D scene S0 and a sequence of embodied actions A1:F , the model generates a temporally coherent video that ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The training objective follows the standard latent diffusion loss [36]: LLDM = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t / cs, ch)∥2 2 i .
- **p. 6 / 4. Experiments - extractive body cue:** We use CogVideoX [52] for denoising and set the noise strength to 0.75 with 50 inference steps.
- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** During inference, the model iteratively denoises zt to obtain ˆz0, which is decoded by VAE into a realistic interaction video.
- **p. 5 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The model operates in the latent space of a pretrained video variational autoencoder (VAE) [22, 52], which encodes an input video into latent tensors z0 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Here, dynamics, model, samples, scene, action-induced, changes, given, actions, while, observation, maps, latent, world, states, visual, frames, Importantly, instantiate, generative.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Formulation of Dexterous World Models (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Despite real-world scenes with dynamic view being completely unseen during training, and the absence of any training samples involving opening a window, ... | p. 6 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Filtering / recovery | Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. | p. 6 (4.1. Comparison), p. 6 (4.1. Comparison) |
| Monitoring / re-entry | Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world ... | p. 8 (4.2. Qualitative Results), p. 6 (4.1. Comparison) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation on hand-motion conditioning. We demonstrate the effectiveness of spatially aligned hand-mesh conditioning.
- **p. 6 / 4. Experiments - extractive body cue:** We set the mask as ones and finetune the model with our dataset without the hand-mesh video condition.
- **p. 6 / 3.4. Action Evaluation with DWM - extractive body cue:** This formulation enables goal-driven action selection via simulation, without requiring explicit reward functions or real-world trials.
- **p. 7 / 4.2. Qualitative Results - extractive body cue:** Without hand-motion input, DWM simulates navigation only.
- **p. 7 / 4.2. Qualitative Results - extractive body cue:** Without hand motion conditioning, DWM operates as a pure navigator.
- **p. 8 / 4.2. Qualitative Results - extractive body cue:** Ablation on training data composition.
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** Under this setup, the egocentric static scene video is time-invariant: Π(S0; Ct) = Π(S0; C0) = V0, ∀t ∈{1, . . . , F}.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.2. Scene-Action-Conditioned Video Diffusion), objective p. 5 (3.2. Scene-Action-Conditioned Video Diffusion), p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), temporal p. 8 (4.3. Ablation Study), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.1. Formulation of Dexterous World Models), p. 5 (3.2. Scene-Action-Conditioned Video Diffusion), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
