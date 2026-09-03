# Method - DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 4 (3. Method)): Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature extractor for action policy training, and (ii) as ...

## Method Body Digest

- **p. 4 / 3.2. Policy Learning - extractive body cue:** Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature extractor for action ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** In addition, we introduce an action causal self-attention mechanism to model temporal dependencies among consecutive action tokens.
- **p. 5 / 3.2. Policy Learning - extractive body cue:** = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - \boldsymbol {\varepsilon }_{\psi ...
- **p. 4 / 3. Method - extractive body cue:** 2, DiffuView first pretrains a multi-view diffusion model to infer geometric correspondences across different camera views, enabling the encoder to capture cross view aligned representations.
- **p. 5 / 3.2. Policy Learning - extractive body cue:** Unlike vanilla self-attention, causal masking enforces an autoregressive constraint such that each action token can only attend to its preceding tokens.
- **p. 4 / 3.2. Policy Learning - extractive body cue:** After the FiLM conditioned QFormer aggregates the visual features into a compact observation embedding zobs, a diffusion policy is employed as the action head to ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** At each timestep t, the policy network εψ learns to predict the noise component based on the noisy action a(t), the timestep t, the observation ...
- **p. 4 / 3. Method - extractive body cue:** In the second stage, we utilize the pretrained perceptual foundation to extract features, which are aggregated and decoded by a diffusionbased policy network to produce ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We propose DiffuView, a novel diffusion-based representation learning framework for robotic manipulation that learns 3D consistent visual ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method consists of two stages, as illustrated in Fig.
- **p. 1 / 1. Introduction - extractive body cue:** (c) Our method leverages a multi view diffusion model that learns 3D consistent and geometry aware representations by generating novel target views conditioned on source ...

## Source Evidence Cues

- **p. 4 / 3.2. Policy Learning - extractive body cue:** Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature extractor for action ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** In addition, we introduce an action causal self-attention mechanism to model temporal dependencies among consecutive action tokens.
- **p. 5 / 3.2. Policy Learning - extractive body cue:** = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - \boldsymbol {\varepsilon }_{\psi ...
- **p. 4 / 3. Method - extractive body cue:** 2, DiffuView first pretrains a multi-view diffusion model to infer geometric correspondences across different camera views, enabling the encoder to capture cross view aligned representations.
- **Detected method headings:** 3. Method (p. 4); 3.2. Policy Learning (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature ... | p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | In addition, we introduce an action causal self-attention mechanism to model temporal dependencies among consecutive action tokens. | p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - ... | p. 5 (3.2. Policy Learning), p. 4 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Policy Learning - extractive body cue:** Unlike vanilla self-attention, causal masking enforces an autoregressive constraint such that each action token can only attend to its preceding tokens.
- **p. 5 / 3.2. Policy Learning - extractive body cue:** = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - \boldsymbol {\varepsilon }_{\psi ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | After, FiLM, conditioned, QFormer, aggregates, visual, features, compact, observation, embedding, zobs, diffusion, policy, employed | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | After, FiLM, conditioned, QFormer, aggregates, visual, features, compact, observation, embedding | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | summarize, contributions, follows, DiffuView, novel, diffusion-based, representation, learning, framework, robotic | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | Unlike, vanilla, self-attention, causal, masking, enforces, autoregressive, constraint, action, token | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Policy Learning - extractive body cue:** After the FiLM conditioned QFormer aggregates the visual features into a compact observation embedding zobs, a diffusion policy is employed as the action head to ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** At each timestep t, the policy network εψ learns to predict the noise component based on the noisy action a(t), the timestep t, the observation ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - \boldsymbol {\varepsilon }_{\psi ...
- **p. 4 / 3. Method - extractive body cue:** In the second stage, we utilize the pretrained perceptual foundation to extract features, which are aggregated and decoded by a diffusionbased policy network to produce ...
- **p. 1 / 1. Introduction - extractive body cue:** The traditional paradigm of Visual Behavior Cloning primarily focuses on extracting informative features from visual input to generate robot actions.
- **p. 2 / 1. Introduction - extractive body cue:** In the second stage, we integrate the pretrained model into an action diffusion policy network, where the learned representations serve as structured visual features to ...
- **p. 2 / 1. Introduction - extractive body cue:** Representative works such as MVP [52], 3D-MVP [38], LIFT3D [21], EmbodiedMAE [10], and CL3R [7] adopt this paradigm, where the model learns to reconstruct masked ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | To further enhance efficiency, we adopt a noise timestep conditioned Mixture-ofExperts (MoE) strategy [42]. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | At each timestep t, the router dynamically activates Top 2 experts within each MoE module on the current noise-level token η(σt), allowing ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | In our multi task action learning framework, we uses 8 layers transformer blocks with a latent dimension of 768. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Policy Learning - extractive body cue:** Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature extractor for action ...
- **p. 4 / 3. Method - extractive body cue:** 2, DiffuView first pretrains a multi-view diffusion model to infer geometric correspondences across different camera views, enabling the encoder to capture cross view aligned representations.
- **p. 6 / 4.2. Simulation Experiments - extractive body cue:** To perform the denoising process, we utilize the DDIM-solver, a numerical ODEbased sampler designed for diffusion models, and apply 10 denoising steps during inference.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Thanks, flexible, view, inference, design, pretrained, model, serve, complementary, roles, during, downstream, learning, feature, extractor, action, policy, training, viewpoint-adaptive, encoder.
- **Relevant PDF headings:** 3. Method (p. 4); 3.2. Policy Learning (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | To enable our pretraining model to generalize effectively to the visual and geometric characteristics of robotic manipulation scenes, we construct a pretraining ... | p. 5 (4.1. Pretraining Setups), p. 5 (4.1. Pretraining Setups) |
| Grasp / trajectory generation | 3, the pretrained module enables the policy to maintain stable manipulation performance under large viewpoint shifts, whereas the baseline 23606 | p. 6 (4.3. View Generalization Experiments), p. 7 (4.4. Real World Experiments) |
| Contact execution / correction | The results indicate that our method significantly improves generalization, with the DiffuView framework achieving superior performance compared to prior models. | p. 7 (4.4. Real World Experiments), p. 7 (4.3. View Generalization Experiments) |

## Failure and Ablation Link

- **p. 7 / 4.3. View Generalization Experiments - extractive body cue:** This figure illustrates the effect of our pretrained model serving as a view-adaptive module.
- **p. 7 / 4.5. Ablation Studies - extractive body cue:** To better understand the contribution of each component in our framework, we conduct ablation studies on 23607
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** 5, when the model is trained without robot centric data, the performance drops sharply, highlighting the importance of pretraining on robot centric datasets.
- **p. 5 / 4.1. Pretraining Setups - extractive body cue:** To enable our pretraining model to generalize effectively to the visual and geometric characteristics of robotic manipulation scenes, we construct a pretraining dataset composed of ...
- **p. 5 / 4.1. Pretraining Setups - extractive body cue:** Our fine-tuning dataset encompasses over 200 robotic manipulation tasks with rich and varied object interactions.
- **p. 6 / 4.3. View Generalization Experiments - extractive body cue:** 3, the pretrained module enables the policy to maintain stable manipulation performance under large viewpoint shifts, whereas the baseline 23606
- **p. 6 / 4.3. View Generalization Experiments - extractive body cue:** However, our pretrained model serves dual roles - acting as a feature extractor during the training phase, and as a view-adaptive module during inference.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 4 (3. Method), objective p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), temporal p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 6 (4.2. Simulation Experiments), p. 4 (3. Method), p. 4 (3.1. Multi-View Diffusion Pretraining), p. 6 (4.2. Simulation Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
