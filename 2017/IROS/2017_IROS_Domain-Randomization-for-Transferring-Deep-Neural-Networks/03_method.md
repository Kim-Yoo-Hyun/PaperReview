# Method - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.06907; PDF retrieval source: https://arxiv.org/pdf/1703.06907. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD)): The remainder of this section describes the specific domain randomization and neural network training methodology we use.

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The remainder of this section describes the specific domain randomization and neural network training methodology we use.
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 4 / III. METHOD - extractive body cue:** In particular, we use a modified version the VGG-16 architecture [39] shown in Figure 2.
- **p. 4 / III. METHOD - extractive body cue:** For the majority of our experiments, we use weights obtained by pretraining on ImageNet to initialize the convolutional layers, which we hypothesized would be essential ...
- **p. 4 / III. METHOD - extractive body cue:** We train the detector through stochastic gradient descent on the L2 loss between the object positions estimated by the network and the true object positions ...
- **p. 3 / III. METHOD - extractive body cue:** Random textures are chosen among the following: (a) A random RGB value (b) A gradient between two random RGB values (c) A checker pattern between ...
- **p. 4 / III. METHOD - extractive body cue:** The input is an image from an external webcam downsized to (224 × 224) and the output of the network predicts the (x, y, z) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Object localization from pixels is a well-studied problem in robotics, and state-ofthe-art methods employ complex, hand-engineered image processing pipelines (e.g., [6], [5], [44]).

## Design Rationale

- **p. 4 / III. METHOD - extractive body cue:** Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in ...
- **p. 3 / III. METHOD - extractive body cue:** Our approach is to train a deep neural network in simulation using domain randomization.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The remainder of this section describes the specific domain randomization and neural network training methodology we use.
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 4 / III. METHOD - extractive body cue:** In particular, we use a modified version the VGG-16 architecture [39] shown in Figure 2.
- **p. 4 / III. METHOD - extractive body cue:** For the majority of our experiments, we use weights obtained by pretraining on ImageNet to initialize the convolutional layers, which we hypothesized would be essential ...
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | The remainder of this section describes the specific domain randomization and neural network training methodology we use. | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | In particular, we use a modified version the VGG-16 architecture [39] shown in Figure 2. | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive body cue:** We train the detector through stochastic gradient descent on the L2 loss between the object positions estimated by the network and the true object positions ...
- **p. 3 / III. METHOD - extractive body cue:** Random textures are chosen among the following: (a) A random RGB value (b) A gradient between two random RGB values (c) A checker pattern between ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, image, external, webcam, downsized, output, network, predicts, coordinates, object, interest, localization, pixels, well-studied | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | input, image, external, webcam, downsized, output, network, predicts, coordinates, object | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | avoids, calibration, precise, placement, camera, real, world, randomizing, characteristics, cameras | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | train, detector, through, stochastic, gradient, descent, loss, between, object, positions | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive body cue:** The input is an image from an external webcam downsized to (224 × 224) and the output of the network predicts the (x, y, z) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Object localization from pixels is a well-studied problem in robotics, and state-ofthe-art methods employ complex, hand-engineered image processing pipelines (e.g., [6], [5], [44]).
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Robotic control from camera pixels is attractive due to the low cost of cameras and the rich data they provide, but challenging because it involves ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent work has shown that supervised learning with deep neural networks is a powerful tool for learning generalizable representations from high-dimensional inputs [20], but deep ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To our knowledge, this is the first successful transfer of a deep neural network trained only on simulated RGB images to the real world for ...
- **p. 3 / III. METHOD - extractive body cue:** We render images using the MuJoCo Physics Engine's [45] built-in renderer.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value not recovered from the selected body cues. | Given some objects of interest {si}i, our goal is to train an object detector d(I0) that maps a single monocular camera frame ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | ReLU nonlinearities are used throughout, and max pooling occurs between each of the groupings of convolutional layers. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not recovered | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive body cue:** The remainder of this section describes the specific domain randomization and neural network training methodology we use.
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 4 / III. METHOD - extractive body cue:** For the majority of our experiments, we use weights obtained by pretraining on ImageNet to initialize the convolutional layers, which we hypothesized would be essential ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In practice, we found that adding a small amount of random noise to images at training time improves convergence and makes training less susceptible to ...
- **p. 3 / III. METHOD - extractive body cue:** Domain randomization The purpose of domain randomization is to provide enough simulated variability at training time such that at test time the model is able ...
- **p. 3 / III. METHOD - extractive body cue:** Random textures are chosen among the following: (a) A random RGB value (b) A gradient between two random RGB values (c) A checker pattern between ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** remainder, section, describes, specific, domain, randomization, neural, network, training, methodology, randomize, following, aspects, sample, during, Number, shape, distractor, objects, table.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the ... | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Rollout / target construction | Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high accuracy is achievable without it. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Policy / value update | However, using a pre-trained model can significantly improve performance when less training data is used. | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • Number ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Sensitivity to amount of texture randomization. In each case, the detector was trained using 10, 000 random object positions and combina- tions of ...
- **p. 3 / II. RELATED WORK - extractive body cue:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.
- **p. 3 / II. RELATED WORK - extractive body cue:** Our approach also does not rely on precise camera information or calibration, instead randomizing the position, orientation, and field of view of the camera in ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Adding noise during pretraining appears to have a negligible effect.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our object detectors are able to localize objects to within 1.5 cm (on average) in the real world and perform well in the presence of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), objective p. 4 (III. METHOD), p. 3 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Abstract), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
