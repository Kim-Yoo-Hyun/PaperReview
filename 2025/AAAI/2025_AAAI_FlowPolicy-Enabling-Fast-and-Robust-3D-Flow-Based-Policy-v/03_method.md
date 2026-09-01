# Method - FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33617; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33617. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (Abstract), p. 3 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 5 (Abstract)): In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can generate robust robotic actions with ...

## Method Body Digest

- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** Therefore, we propose FlowPolicy, a conditional consistency flow matching model, which guarantees the generation of high-quality actions while also accomplishing one-step inference for realtime applications.
- **p. 1 / Abstract - extractive body cue:** Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.
- **p. 4 / Abstract - extractive body cue:** Depending on the consistency training and condition representation, FlowPolicy can generate high-quality actions in one-step inference and accomplish complex manipulation tasks.
- **p. 5 / Abstract - extractive body cue:** In the inference process, the noise trajectories are sampled from the source distribution a0 ∈asrc and then predicted by a flow model to obtain action ...
- **p. 1 / Abstract - extractive body cue:** 2023) defines policy learning as a conditional denoising diffusion process over the robot action space, conditioned on 2D observation features.
- **p. 5 / Abstract - extractive body cue:** We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report the success rate (%) with standard deviation. ‘∗' indicates that the ...

## Design Rationale

- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** To address this issue, we propose FlowPolicy, a real-time 3D policy generation framework based on consistency flow matching.
- **p. 3 / Abstract - extractive body cue:** Method Our method expects a limited number of expert demonstrations to teach an agent to learn a policy π : O =⇒A, i.e., mapping from ...

## Source Evidence Cues

- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** Therefore, we propose FlowPolicy, a conditional consistency flow matching model, which guarantees the generation of high-quality actions while also accomplishing one-step inference for realtime applications.
- **p. 1 / Abstract - extractive body cue:** Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.
- **p. 4 / Abstract - extractive body cue:** Depending on the consistency training and condition representation, FlowPolicy can generate high-quality actions in one-step inference and accomplish complex manipulation tasks.
- **p. 5 / Abstract - extractive body cue:** In the inference process, the noise trajectories are sampled from the source distribution a0 ∈asrc and then predicted by a flow model to obtain action ...
- **p. 1 / Abstract - extractive body cue:** 2023) defines policy learning as a conditional denoising diffusion process over the robot action space, conditioned on 2D observation features.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual ... | p. 2 (Abstract), p. 3 (Abstract) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Therefore, we propose FlowPolicy, a conditional consistency flow matching model, which guarantees the generation of high-quality actions while also accomplishing one-step inference ... | p. 3 (Abstract), p. 1 (Abstract) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to ... | p. 1 (Abstract), p. 3 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / Abstract - extractive body cue:** We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report the success rate (%) with standard deviation. ‘∗' indicates that the ...
- **p. 2 / Abstract - extractive body cue:** 2022), another class of generative model frameworks that directly defines probability paths via Ordinary Differential Equations (ODEs) to transform between noise and data samples, has ...
- **p. 3 / Abstract - extractive body cue:** In this work, we explore the feasibility of applying FM to 3D robot manipulation and hope to achieve real-time generation through consistency constraints.
- **p. 2 / Abstract - extractive body cue:** Denoising Diffusion Probabilistic Models (DDPMs) (Ho, Jain, and Abbeel 2020) generate a clean sample from noise by solving a Stochastic Differential Equation (SDE).
- **p. 3 / Abstract - extractive body cue:** Consistency-FM directly defines a straight-line flow from any time to the same endpoint and imposes constraints on its velocity values.
- **p. 4 / Abstract - extractive body cue:** ates the probabilistic path pt under two marginal constraints, pt=0 = p0 and pt=1 = p1.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, FlowPolicy, conditions, observed, point, cloud, where, consistency, flow, matching, directly, defines, straight-line, flows | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Specifically, FlowPolicy, conditions, observed, point, cloud, where, consistency, flow, matching | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | summary, main, contributions, threefold, first, flow-based, policy, generation, framework, conditions | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | evaluate, tasks, Adroit, Metaworld, across, random, seeds, report, success, rate | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action ...
- **p. 3 / Abstract - extractive body cue:** Visual observations include the robot state and scene point clouds, and actions are usually sequences of trajectories of the robot to accomplish a specific task.
- **p. 5 / Abstract - extractive body cue:** Additionally, our model employs an observation horizon of two steps, signifying that it leverages the point clouds from the two most recent time frames as ...
- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.
- **p. 1 / Abstract - extractive body cue:** 2023) defines policy learning as a conditional denoising diffusion process over the robot action space, conditioned on 2D observation features.
- **p. 2 / Abstract - extractive body cue:** FlowPolicy allows for the fastest possible generation of target actions by directly defining straight-line flow conditions on the initial 3D point clouds.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Additionally, our model employs an observation horizon of two steps, signifying that it leverages the point clouds from the two most recent ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Define at to be the interpolated trajectory between the source and destination trajectories at the transmission time step t. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report inference time per step (ms) with standard deviation. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / Abstract - extractive body cue:** Therefore, we propose FlowPolicy, a conditional consistency flow matching model, which guarantees the generation of high-quality actions while also accomplishing one-step inference for realtime applications.
- **p. 1 / Abstract - extractive body cue:** Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action ...
- **p. 4 / Abstract - extractive body cue:** Depending on the consistency training and condition representation, FlowPolicy can generate high-quality actions in one-step inference and accomplish complex manipulation tasks.
- **p. 5 / Abstract - extractive body cue:** In the inference process, the noise trajectories are sampled from the source distribution a0 ∈asrc and then predicted by a flow model to obtain action ...
- **p. 5 / Abstract - extractive body cue:** Each task is run repeatedly under three different random seeds, and their means and variances as well as inference times are calculated.
- **p. 6 / Abstract - extractive body cue:** During the training phase, the weights are updated using the AdamW optimizer with a learning rate of 1e-4 and a batch size of 128.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, main, contributions, threefold, first, flow-based, policy, generation, framework, conditions, visual, representation, generate, robust, robotic, actions, demonstrations, namely, FlowPolicy, significantly.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Experiments Dataset and Implementation Details Simulation Benchmarks We choose two preeminent environmental simulators, Adroit (Rajeswaran et al. | p. 5 (Abstract), p. 5 (Abstract) |
| Grasp / trajectory generation | We also compared state-of-the-art 2D-based approaches, including diffusion policy (DP) (Chi et al. | p. 5 (Abstract), p. 6 (Abstract) |
| Contact execution / correction | Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as ... | p. 7 (Abstract), p. 7 (Abstract) |

## Failure and Ablation Link

- **p. 3 / Abstract - extractive body cue:** More importantly, Consistency-FM can be trained to produce a robust flow model without the aid of distillation, which is valuable to robots performing unseen tasks, ...
- **p. 4 / Abstract - extractive body cue:** 2024) is a generalized method for efficiently learning straight-line flows without approximating the entire probabilistic path.
- **p. 7 / Abstract - extractive body cue:** We further conduct ablation studies to verify the influence of the number of expert demonstrations.
- **p. 7 / Abstract - extractive body cue:** Ablation Studies on Expert Demonstrations The success rate of the agent in accomplishing tasks depends on the number and quality of expert demonstrations, where the ...
- **p. 3 / Abstract - extractive body cue:** Finally, we describe the design details of each component.
- **p. 6 / Abstract - extractive body cue:** Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete the ...
- **p. 7 / Abstract - extractive body cue:** DP3 unsuccessfully picks up the red cube and fails the task.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (Abstract), p. 3 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 5 (Abstract), objective p. 5 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), temporal p. 5 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 5 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
