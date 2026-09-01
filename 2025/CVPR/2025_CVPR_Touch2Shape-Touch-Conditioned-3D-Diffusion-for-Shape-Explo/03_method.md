# Method - Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 3 (3. Method), p. 3 (3. Method)): The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added gaussian noise, the Eω is ...

## Method Body Digest

- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then inputting them together ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then use a touchconditioned ...
- **p. 3 / 3. Method - extractive PDF cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...
- **p. 3 / 3. Method - extractive PDF cue:** Following SDFusion [5], we employ the volumetric Truncated Signed Distance Field (T-SDF) to model the distribution across 3D shapes and a 3D variant of the ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** For reward function setting, since the final output shape is not predicted, we design it to be the difference in the diffusion model's loss values.
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** The loss function for reinforcement learning is as follows: Lrl = [R + ϖ max an+1 Q(T0, ..., Tn+1, an+1) ↓Q(T0, ..., Tn, an)]2, (6) ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive PDF cue:** The touch shape fusion module is designed with two goals.

## Source Evidence Cues

- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then inputting them together ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then use a touchconditioned ...
- **p. 3 / 3. Method - extractive PDF cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...
- **p. 3 / 3. Method - extractive PDF cue:** Following SDFusion [5], we employ the volumetric Truncated Signed Distance Field (T-SDF) to model the distribution across 3D shapes and a 3D variant of the ...
- **Detected method headings:** 3. Method (p. 3); 3.1. Touch-conditioned Diffusion Model (p. 4); 3.3. Policy Training (p. 5); 4.3. Evaluation on Policy (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt ... | p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then ... | p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the ... | p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Policy Training - extractive PDF cue:** For reward function setting, since the final output shape is not predicted, we design it to be the difference in the diffusion model's loss values.
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** The loss function for reinforcement learning is as follows: Lrl = [R + ϖ max an+1 Q(T0, ..., Tn+1, an+1) ↓Q(T0, ..., Tn, an)]2, (6) ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The objective is to pulling together with matching touch-shape pairs while pushing unmatched pairs apart.
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The loss function is: Lrl = ↓log eq·kp/ε !K i=0 eq·ki/ε , (3) where q is the query feature, k is the key feature, ki ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section, employ, simulated, robotic, guided | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | main, contributions, article, follows, Touch2Shape, touch-conditioned, diffusion, model, shape, exploration | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | reward, function, setting, since, final, output, shape, predicted, design, difference | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Method - extractive PDF cue:** The policy model receives the denoised vector as input and is trained using reinforcement learning (Section 3.2).
- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we employ a simulated robotic arm guided by a trained policy model to touch the target, enabling the acquisition of tactile images ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** The loss function for reinforcement learning is as follows: Lrl = [R + ϖ max an+1 Q(T0, ..., Tn+1, an+1) ↓Q(T0, ..., Tn, an)]2, (6) ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** Subsequently, we construct an action embedding module to derive the embedding for the potential actions.
- **p. 3 / 3. Method - extractive PDF cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | Instead, we utilize the shape decoder and shape fusion only at the final time step, thereby achieving a separation of shape decoder ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | After the diffusion model training finished, we conducted policy training in silmulation environment [34] for 200 epochs with a learning rate of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive PDF cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 3 / 3. Method - extractive PDF cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** After the diffusion model training finished, we conducted policy training in silmulation environment [34] for 200 epochs with a learning rate of 0.0003 and batch ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The diffusion model was trained for 1 million iterations with an initial learning rate of 0.00001 and batch size of 12, while the touch shape ...
- **p. 5 / 3.3. Policy Training - extractive PDF cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** loss, function, diffusion, model, training, follows, Ldiff, t//2, where, added, gaussian, noise, denoising, network, touch, condition, extraction, inputs, number, timesteps.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Touch-conditioned Diffusion Model (p. 4); 3.3. Policy Training (p. 5); 4.3. Evaluation on Policy (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing. | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 5 (4.1. Experimental Settings) |
| Contact / dynamics inference | Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound ... | p. 7 (4.3. Evaluation on Policy), p. 7 (4.3. Evaluation on Policy) |
| Force-aware action correction | The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction ... | p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance) |

## Failure and Ablation Link

- **p. 5 / 4. Experiment - extractive PDF cue:** Through the ablation study, we validate the necessity of each module.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** We design the ablation study to further validate the necessity of our proposed reconstruction modules.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Ablation study results on dataset ABC.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The evaluation metric is EMD (lower is better). touch shape fusion can be trained concurrently since they do not share any components.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. We pretrained (a) the shape encoder and decoder, (b) the touch CNN model that is used for touch chart prediction, and (c) the ...
- **p. 7 / 4.3. Evaluation on Policy - extractive PDF cue:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 3 (3. Method), p. 3 (3. Method), objective p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), temporal p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 1 (2 Nanjing University of Posts and Telecommunications), p. 4 (3. Method), p. 6 (4.2. Evaluation on Reconstruction Performance).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
