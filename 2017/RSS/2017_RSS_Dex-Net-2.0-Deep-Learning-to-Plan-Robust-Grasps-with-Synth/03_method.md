# Method - Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.09312; PDF retrieval source: https://arxiv.org/pdf/1703.09312. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (V. GRASP PLANNING)): The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.

## Method Body Digest

- **p. 5 / V. GRASP PLANNING - extractive body cue:** The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.
- **p. 5 / V. GRASP PLANNING - extractive body cue:** The set C is a discrete set of antipodal candidate grasps [6] sampled uniformly at random in image space for surface normals defined by the ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Let y = RH×W + be a 2.5D point cloud represented as a depth image with height H and width W taken by a camera ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Let p(S, u, x, y) be a joint distribution on grasp success, grasps, states, and point clouds modeling imprecision in sensing and control.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper we instead consider predicting grasp success directly from depth images by training a deep Convolutional Neural Network (CNN) on a massive dataset ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that the Dex-Net 2.0 grasp planner is 3× faster than the registration-based method, 93% successful on objects seen in training (the highest of ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Learning Q rather than directly learning the policy allows us to enforce task-specific constraints without having to update the learned model.

## Source Evidence Cues

- **p. 5 / V. GRASP PLANNING - extractive body cue:** The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig. | p. 5 (V. GRASP PLANNING) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig. | p. 5 (V. GRASP PLANNING) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig. | p. 5 (V. GRASP PLANNING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / V. GRASP PLANNING - extractive body cue:** The set C is a discrete set of antipodal candidate grasps [6] sampled uniformly at random in image space for surface normals defined by the ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (V. GRASP PLANNING), p. 5 (V. GRASP PLANNING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | learn, function, takes, input, candidate, grasp, depth, image, outputs, estimate, robustness, probability, success, under | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | learn, function, takes, input, candidate, grasp, depth, image, outputs, estimate | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | primary, contributions, Dexterity, Network, Dex-Net, dataset, associating, million, point, clouds | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | discrete, antipodal, candidate, grasps, sampled, uniformly, random, image, space, surface | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Let y = RH×W + be a 2.5D point cloud represented as a depth image with height H and width W taken by a camera ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Let p(S, u, x, y) be a joint distribution on grasp success, grasps, states, and point clouds modeling imprecision in sensing and control.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper we instead consider predicting grasp success directly from depth images by training a deep Convolutional Neural Network (CNN) on a massive dataset ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...
- **p. 5 / V. GRASP PLANNING - extractive body cue:** The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | We used TensorFlow [1] with a batch size of 128, a momentum term of 0.9, and an exponentially decaying learning rate with ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Due to the memory and time requirements of training SVMs, we compared synthetic classification performance across methods on the smaller Adv-Synth dataset. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | Due to the memory and time requirements of training SVMs, we compared synthetic classification performance across methods on the smaller Adv-Synth dataset. | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Each method was run for 50 trials (5 per object). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / VI. EXPERIMENTS - extractive body cue:** All experiments ran on a Desktop running Ubuntu 14.04 with a 2.7 GHz Intel Core i5-6400 Quad-Core CPU and an NVIDIA GeForce 980, and we ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Pretraining does not appear to affect performance. cient of µ = 0.5 in 50 physical trials per object in Train (400 datapoints).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Dex-Net, grasp, planner, uses, robust, grasping, policy, argmaxu, illustrated, Fig, discrete, antipodal, candidate, grasps, sampled, uniformly, random, image, space, surface.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a ... | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Grasp / trajectory generation | Grasp Planning Methods Used for Comparison We compared a number of grasp planning methods on simulated and real data. | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Contact execution / correction | We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision. | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / VI. EXPERIMENTS - extractive body cue:** We also trained several variants to evaluate sensitivity to several parameters: Dataset Size.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Amount of Pretraining We trained three GQ-CNNs on the synthetic dataset of adversarial training objects (Adv-Synth) to study the effect of pretraining with Dex-Net for ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** A human operator was required to reset the object in the workspace on each trial, and therefore blinded operators from which grasp planning method was ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Pretraining does not appear to affect performance. cient of µ = 0.5 in 50 physical trials per object in Train (400 datapoints).
- **p. 8 / I. Failure Modes - extractive body cue:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of ...
- **p. 8 / I. Failure Modes - extractive body cue:** A second type of failure occured due to collisions with the object.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. (Top) For each object, we sample hundreds ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (V. GRASP PLANNING), objective p. 5 (V. GRASP PLANNING), temporal p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 4 (IV. LEARNING A GRASP ROBUSTNESS FUNCTION), p. 5 (IV. LEARNING A GRASP ROBUSTNESS FUNCTION), p. 5 (IV. LEARNING A GRASP ROBUSTNESS FUNCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
