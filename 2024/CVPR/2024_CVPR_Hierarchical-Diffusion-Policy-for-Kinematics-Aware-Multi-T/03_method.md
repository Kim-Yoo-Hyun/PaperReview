# Method - Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Diffusion Models), p. 5 (4.3. Low-Level RK-Diffuser), p. 5 (4.3. Low-Level RK-Diffuser), p. 4 (4.1. Dataset Preparation), p. 4 (4. Hierarchical Diffusion Policy), p. 6 (4.3. Low-Level RK-Diffuser)): The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta (x^0) ] \ge \mathbb {E}_q\left [\log \frac {p_\theta ...

## Method Body Digest

- **p. 3 / 3.1. Diffusion Models - extractive PDF cue:** The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta (x^0) ] \ge ...
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** The low-level RK-Diffuser takes as input the start pose, the end pose, the RGB-D image of the first step observation, a vector of the robot ...
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** For the RGB-D image, we first convert it to a point cloud in the world frame and extract the features with PointNet++ [29]; for the ...
- **p. 4 / 4.1. Dataset Preparation - extractive PDF cue:** Each demonstration ξ = {ademo, odemo}, consists of an expert trajectory ademo and resulting observation odemo.
- **p. 4 / 4. Hierarchical Diffusion Policy - extractive PDF cue:** Here, a consists of a trajectory ajoint = {a(0), a(1), . . . , a(T)} and gripper opening / closing action agrip, where T is ...
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** In RK-Diffuser, we propose to add an additional conditional variable for each sub-trajectory, a trajectory rank rξ = dEuclidean dtravel , where dEuclidean is the ...
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** During training, most of the manipulation algorithms use sampling-based motion planners whose trajectories might be sub-optimal.
- **p. 4 / 4.2. High-Level Next-Best Pose Agent - extractive PDF cue:** The network is optimised by behaviour cloning losses, i.e., cross-entropy losses in the discrete action space \ma t hcal {L}_ \mat hrm {high} = - ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce a novel kinematics-aware low-level agent, Robot Kinematics Diffuser (RK-Diffuser), a diffusion-based policy [5] that directly generates the moThis CVPR paper is the Open ...
- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce HDP, a hierarchical agent for robotic manipulation.
- **p. 4 / 4.1. Dataset Preparation - extractive PDF cue:** Each demonstration ξ = {ademo, odemo}, consists of an expert trajectory ademo and resulting observation odemo.

## Source Evidence Cues

- **p. 3 / 3.1. Diffusion Models - extractive PDF cue:** The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta (x^0) ] \ge ...
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** The low-level RK-Diffuser takes as input the start pose, the end pose, the RGB-D image of the first step observation, a vector of the robot ...
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** For the RGB-D image, we first convert it to a point cloud in the world frame and extract the features with PointNet++ [29]; for the ...
- **p. 4 / 4.1. Dataset Preparation - extractive PDF cue:** Each demonstration ξ = {ademo, odemo}, consists of an expert trajectory ademo and resulting observation odemo.
- **p. 4 / 4. Hierarchical Diffusion Policy - extractive PDF cue:** Here, a consists of a trajectory ajoint = {a(0), a(1), . . . , a(T)} and gripper opening / closing action agrip, where T is ...
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** In RK-Diffuser, we propose to add an additional conditional variable for each sub-trajectory, a trajectory rank rξ = dEuclidean dtravel , where dEuclidean is the ...
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** During training, most of the manipulation algorithms use sampling-based motion planners whose trajectories might be sub-optimal.
- **Detected method headings:** 2.2. Diffusion Models (p. 2); 3.1. Diffusion Models (p. 3); 4. Hierarchical Diffusion Policy (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta ... | p. 3 (3.1. Diffusion Models), p. 5 (4.3. Low-Level RK-Diffuser) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | The low-level RK-Diffuser takes as input the start pose, the end pose, the RGB-D image of the first step observation, a vector ... | p. 5 (4.3. Low-Level RK-Diffuser), p. 5 (4.3. Low-Level RK-Diffuser) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | For the RGB-D image, we first convert it to a point cloud in the world frame and extract the features with PointNet++ ... | p. 5 (4.3. Low-Level RK-Diffuser), p. 4 (4.1. Dataset Preparation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.2. High-Level Next-Best Pose Agent - extractive PDF cue:** The network is optimised by behaviour cloning losses, i.e., cross-entropy losses in the discrete action space \ma t hcal {L}_ \mat hrm {high} = - ...
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** Consider, for example, that each step of the predicted trajectory has a probability p to violate the IK constraints.
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** For a trajectory of length T, the probability of the trajectory might violate the constraint is perror = 1 -(1 -p)T , and lim T ...
- **p. 4 / 4.2. High-Level Next-Best Pose Agent - extractive PDF cue:** In this work, to parameterise πhigh and fulfil this objective, we employ Perceiver-Actor (PerAct) [34].
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** Intuitively, an optimal trajectory, ignoring the kinematics constraint of the robot, should have rξ = 1.
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** This allows us to train a jointposition trajectory which better regularizes the joint positions with the kinematics as an inductive bias.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (4.2. High-Level Next-Best Pose Agent), p. 4 (4.2. High-Level Next-Best Pose Agent), p. 5 (4.3. Low-Level RK-Diffuser), p. 5 (4.3. Low-Level RK-Diffuser), p. 6 (4.3. Low-Level RK-Diffuser).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, trained, maximising, evidence, lower, bound, ELBO, math, heta, mathbb, left, frac, theta, right | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | model, trained, maximising, evidence, lower, bound, ELBO, math, heta, mathbb | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | introduce, novel, kinematics-aware, low-level, agent, Robot, Kinematics, Diffuser, RK-Diffuser, diffusion-based | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | network, optimised, behaviour, cloning, losses, cross-entropy, discrete, action, space, hcal | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Diffusion Models - extractive PDF cue:** The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta (x^0) ] \ge ...
- **p. 4 / 4. Hierarchical Diffusion Policy - extractive PDF cue:** We aim to learn a HDP policy π(a / o, l), which processes the RGB-D observation o and language instruction l, specifying the task, to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** One way of parameterising the policy is to directly map visual observations to robot commands, e.g., joint position or velocity actions [18, 22, 27, 39].
- **p. 1 / 1. Introduction - extractive PDF cue:** At the high level, HDP takes the 3D visual observations and language instructions as the inputs, and predicts a 6-DoF next-best end-effector pose.
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** The low-level RK-Diffuser takes as input the start pose, the end pose, the RGB-D image of the first step observation, a vector of the robot ...
- **p. 4 / 4.2. High-Level Next-Best Pose Agent - extractive PDF cue:** For the high-level policy ahigh = (apose, agrip) ∼πhigh(a / o, l), we utilise a next-best pose agent [17] with structured action representations.
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** For action trajectories sampled from each learned policy, a0 pose ∼pθ(a0 pose / a1 pose, Cpose) and a0 joint ∼pϕ(a0 joint / a1 joint, Cpose), ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | In addition, we aim to demonstrate the benefit of the proposed RKDiffuser against alternatives, including: (1) Planner: a hybrid planner of fixed ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Both tasks require the robot to accurately locate the target and control all its joints, especially the orientation of the wrist at ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Diffusion Models - extractive PDF cue:** The model can be trained by maximising the evidence lower bound (ELBO) \math bb {E}_ { x_ 0 }[\ log p_\t heta (x^0) ] \ge ...
- **p. 6 / 4.3. Low-Level RK-Diffuser - extractive PDF cue:** During training, most of the manipulation algorithms use sampling-based motion planners whose trajectories might be sub-optimal.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, trained, maximising, evidence, lower, bound, ELBO, math, heta, mathbb, left, frac, theta, right, label, context, decision, making, diffusion, policies.
- **Relevant PDF headings:** 2.2. Diffusion Models (p. 2); 3.1. Diffusion Models (p. 3); 4. Hierarchical Diffusion Policy (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We assume access to a multi-task dataset D = {ξi}ND i=1, containing a total of ND expert demonstrations paired with Dl = ... | p. 4 (4.1. Dataset Preparation), p. 6 (5. Experiments) |
| Grasp / trajectory generation | HDP outperforms the state-of-the-art methods across RLBench tasks. | p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments) |
| Contact execution / correction | For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP to outperform many of the ... | p. 7 (5.2. Simulation Experiments), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5. Experiments - extractive PDF cue:** In addition to this, we perform a series of ablation studies and show: (1) IK errors contribute to the majority of the failure cases of ...
- **p. 6 / 5.1. Trajectory Visualisations - extractive PDF cue:** Nevertheless, without understanding the task context, the trajectory generated by RRT will cause the lid of the box to fall from the gripper.
- **p. 7 / 5.3. Ablation Studies - extractive PDF cue:** Sampling-based motion planners might fail without understanding the task context.
- **p. 7 / 5.3. Ablation Studies - extractive PDF cue:** We perform ablation studies on the selected RLBench tasks to further understand the proposed low-level agent, RKDiffuser.
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses.
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** For RKD-RGB, we discard the depth information and use a pretrained ResNet50 to extract the image features; for RKD-ResNet, we ablate using a ResNet to ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** Although we have demonstrated some robustness of RK-Diffuser to out-of-distribution poses, the nature of behaviour cloning for longer-horizon tasks suggests that error accumulation could lead ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Diffusion Models), p. 5 (4.3. Low-Level RK-Diffuser), p. 5 (4.3. Low-Level RK-Diffuser), p. 4 (4.1. Dataset Preparation), p. 4 (4. Hierarchical Diffusion Policy), p. 6 (4.3. Low-Level RK-Diffuser), objective p. 4 (4.2. High-Level Next-Best Pose Agent), p. 5 (4.3. Low-Level RK-Diffuser), p. 5 (4.3. Low-Level RK-Diffuser), p. 4 (4.2. High-Level Next-Best Pose Agent), p. 6 (4.3. Low-Level RK-Diffuser), p. 6 (4.3. Low-Level RK-Diffuser), temporal p. 6 (5.2. Simulation Experiments), p. 8 (5.4. Real Robot Experiment), p. 6 (4.4. Practical Implementation Choices), p. 7 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 3 (3.1. Diffusion Models).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
