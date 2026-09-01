# Method - 3D Equivariant Visuomotor Policy Learning via Spherical Projection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kXJd4JxF34; PDF retrieval source: https://openreview.net/pdf/20cb87b1441d2401c9489c5c43e121f801b3a4ee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4 Method), p. 17 (C Implementation of Our Policy), p. 7 (4 Method), p. 16 (C Implementation of Our Policy), p. 16 (C Implementation of Our Policy), p. 6 (4 Method)): In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.

## Method Body Digest

- **p. 4 / 4 Method - extractive PDF cue:** In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only the first 8 ...
- **p. 7 / 4 Method - extractive PDF cue:** However, our diffusion model receives a representation from the observation encoder that is equivariant to this rotation because it is constructed from invariant features (from ...
- **p. 16 / C Implementation of Our Policy - extractive PDF cue:** Our model consists of an SO(3)-equivariant observation encoder followed by an SO(3)-equivariant diffusion module, both implemented using escnn [3] and e3nn [57].
- **p. 16 / C Implementation of Our Policy - extractive PDF cue:** Given an observation x ∈X, the SO(2)-equivariant image encoder λ first maps the RGB image I into a regular representation, which is then mapped to ...
- **p. 6 / 4 Method - extractive PDF cue:** First, due to the SO(3)-equivariant encoder (Proposition 1) and the SO(3)-equivariant diffusion model (Section 4.2), our policy has end-to-end symmetry to global scene SO(3) rotations.
- **p. 4 / 4 Method - extractive PDF cue:** The observation x ∈X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈R7, including the end-effector's ...
- **p. 5 / 4 Method - extractive PDF cue:** We represent this spherical signal in the spectral domain as truncated Fourier coefficients calculated using the spherical Fourier transform (Equation 1).

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our key contributions are summarized as follows: • We introduce Image-to-Sphere Policy (ISP), the first SO(3)-equivariant policy learning framework that uses spherical projection from 2D ...
- **p. 1 / 1 Introduction - extractive PDF cue:** g Figure 1: We propose the first SO(3)-equivariant policy learning framework based on a single eyein-hand RGB image, where the predicted action sequence transforms equivariantly ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our method first projects features extracted from 2D RGB observations onto a sphere and then rotates the resulting spherical signal to compensate for camera motion.

## Source Evidence Cues

- **p. 4 / 4 Method - extractive PDF cue:** In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only the first 8 ...
- **p. 7 / 4 Method - extractive PDF cue:** However, our diffusion model receives a representation from the observation encoder that is equivariant to this rotation because it is constructed from invariant features (from ...
- **p. 16 / C Implementation of Our Policy - extractive PDF cue:** Our model consists of an SO(3)-equivariant observation encoder followed by an SO(3)-equivariant diffusion module, both implemented using escnn [3] and e3nn [57].
- **p. 16 / C Implementation of Our Policy - extractive PDF cue:** Given an observation x ∈X, the SO(2)-equivariant image encoder λ first maps the RGB image I into a regular representation, which is then mapped to ...
- **p. 6 / 4 Method - extractive PDF cue:** First, due to the SO(3)-equivariant encoder (Proposition 1) and the SO(3)-equivariant diffusion model (Section 4.2), our policy has end-to-end symmetry to global scene SO(3) rotations.
- **p. 4 / 4 Method - extractive PDF cue:** The observation x ∈X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈R7, including the end-effector's ...
- **Detected method headings:** 4 Method (p. 4); C Implementation of Our Policy (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion ... | p. 4 (4 Method), p. 17 (C Implementation of Our Policy) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only ... | p. 17 (C Implementation of Our Policy), p. 7 (4 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | However, our diffusion model receives a representation from the observation encoder that is equivariant to this rotation because it is constructed from ... | p. 7 (4 Method), p. 16 (C Implementation of Our Policy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 Method - extractive PDF cue:** We represent this spherical signal in the spectral domain as truncated Fourier coefficients calculated using the spherical Fourier transform (Equation 1).
- **p. 6 / 4 Method - extractive PDF cue:** These properties are inherently preserved without requiring additional constraints.
- **p. 7 / 4 Method - extractive PDF cue:** Under a rotation of the gripper with respect to the workspace, no a priori constraint can be placed on how the action trajectory should transform.
- **p. 6 / 4 Method - extractive PDF cue:** Since the image is recorded in the camera frame, the spherical signal is unaffected, i.e. Φ(g·x) = Φ(x), while the camera pose updates as Rx ...
- **p. 7 / 4 Method - extractive PDF cue:** The advantage is empirically validated in Section 5.
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** We train all models using the AdamW [38] optimizer with Exponential Moving Average, and adopt the DDPM [15] framework with 100 denoising steps for both ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4 Method), p. 6 (4 Method), p. 7 (4 Method), p. 6 (4 Method), p. 18 (C Implementation of Our Policy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Fourier, Coefficients, Gripper, Orientation, Figure, Overview, Image-to-Sphere, Policy, ISP, equivariant, observation, encoder, extracts, features | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Fourier, Coefficients, Gripper, Orientation, Figure, Overview, Image-to-Sphere, Policy, ISP, equivariant | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, Image-to-Sphere, Policy, ISP, first, equivariant, learning | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | represent, spherical, signal, spectral, domain, truncated, Fourier, coefficients, calculated, transform | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Background - extractive PDF cue:** Fourier Coefficients Gripper Orientation Figure 2: Overview of Image-to-Sphere Policy (ISP) (a) An SO(3)-equivariant observation encoder extracts features from the RGB input, projects them onto ...
- **p. 4 / 4 Method - extractive PDF cue:** The observation x ∈X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈R7, including the end-effector's ...
- **p. 3 / 3 Background - extractive PDF cue:** Formally, given an observation O and diffusion timestep k, the policy predicts a noise estimate ϵk from a corrupted action sequence ak = a0 + ...
- **p. 3 / 3 Background - extractive PDF cue:** Given an observation sequence O = {ot-k+1, ..., ot} at timestep t, the learned policy predicts an action chunk A = {at+1, ..., at+n}, where ...
- **p. 1 / 1 Introduction - extractive PDF cue:** g Figure 1: We propose the first SO(3)-equivariant policy learning framework based on a single eyein-hand RGB image, where the predicted action sequence transforms equivariantly ...
- **p. 5 / 4 Method - extractive PDF cue:** First, we encode the input image I from the observation x using a standard SO(2)-equivariant image encoder λ.
- **p. 5 / 4 Method - extractive PDF cue:** Equivariance Correction is similar to a canonicalization map c : X →G, where fcano = c(x)f(c(x)-1x) transforms the input to a canonical frame, then transforms ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Given an observation sequence O = {ot-k+1, ..., ot} at timestep t, the learned policy predicts an action chunk A = {at+1, ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Similarly, the noisy action chunk ak is embedded into ea ∈Ru×da×n, where da denotes the number of action feature channels and n ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Results Table 4 reports success rates over 20 trials per task. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only the first 8 ...
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** For all baselines, we retain their original hyperparameter settings for evaluation and only adjust the number of training steps to ensure consistency across methods.
- **p. 18 / C Implementation of Our Policy - extractive PDF cue:** For the real-world experiments, we use the same hyperparameters as in the simulation, except that we replace DDPM with DDIM [55] for both training and ...
- **p. 7 / 5 Experiments - extractive PDF cue:** For each task, we train three independent models with different random seeds (0, 1, and 2) for each of the 100- and 200-demonstration settings.
- **p. 8 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** We compare the ISP-SO(2) with two variants: Pretraining, which initializes the image encoder with an 8

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** following, subsections, first, describe, observation, encoder, extracts, equivariant, features, images, then, diffusion, module, cases, denoising, network, outputs, sequence, action, steps.
- **Relevant PDF headings:** 4 Method (p. 4); C Implementation of Our Policy (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark [40], which is widely used in ... | p. 7 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Action / skill decoding | Similarly, ISP-SO(2) outperforms baselines in 20 settings, which further validates the effectiveness of our design. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Receding execution / feedback | Figure 6: Real-world environments for evaluation. A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations. In each subfigure, ... | p. 9 (Figure/Table caption), p. 8 (5 Experiments) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive PDF cue:** To ensure a fair comparison, all experiments in the following sections, including ablations and method variants, consistently apply SO(2) data augmentation during training by rotating ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation study results. A red cross indicates that the corresponding module is removed in that variant. Sphere EquiEnc EquiU Sta. Cof. Nut. Squ. ...
- **p. 8 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** (3) EquiU: With or without an equivariant temporal denoising U-Net in the diffusion module.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** These results confirm the effectiveness of our equivariant design in addressing diverse manipulation challenges in the real world.
- **p. 18 / C Implementation of Our Policy - extractive PDF cue:** Specifically, we evaluated (a) a variant of our method without rotation correction that uses delta control, and (b) the original Diffusion Policy with delta control.
- **p. 7 / 5 Experiments - extractive PDF cue:** For eyein-hand control, we replace its image encoder with a standard ResNet [12], so only proprioception and denoising remain equivariant.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** ImageNet-1k [50]-pretrained equivariant ResNet-18, and Scratch, which trains the entire model from random initialization.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4 Method), p. 17 (C Implementation of Our Policy), p. 7 (4 Method), p. 16 (C Implementation of Our Policy), p. 16 (C Implementation of Our Policy), p. 6 (4 Method), objective p. 5 (4 Method), p. 6 (4 Method), p. 7 (4 Method), p. 6 (4 Method), p. 7 (4 Method), p. 17 (C Implementation of Our Policy), temporal p. 3 (3 Background), p. 17 (C Implementation of Our Policy), p. 5 (4 Method), p. 17 (C Implementation of Our Policy), p. 18 (C Implementation of Our Policy), p. 2 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
