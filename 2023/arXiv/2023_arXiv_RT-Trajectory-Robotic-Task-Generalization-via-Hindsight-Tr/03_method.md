# Method - RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.01977; PDF retrieval source: https://arxiv.org/pdf/2311.01977. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 3 (3 METHOD), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD)): We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive PDF cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 3 / 3 METHOD - extractive PDF cue:** We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive PDF cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive PDF cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.
- **p. 5 / 3 METHOD - extractive PDF cue:** In our work, we use a PaLM-E style (Driess et al., 2023) model that generates vector-quantized tokens derived from ViT-VQGAN (Yu et al., 2022) that ...
- **p. 5 / 3 METHOD - extractive PDF cue:** By using this prompt, the LLM writes code to generate a series of 3D poses - originally intended to be executed with a motion planner, ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, we propose to use a coarse trajectory as a middle-ground solution between expressiveness and ease of use.
- **p. 3 / 3 METHOD - extractive PDF cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive PDF cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 3 / 3 METHOD - extractive PDF cue:** We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive PDF cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive PDF cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.
- **p. 5 / 3 METHOD - extractive PDF cue:** In our work, we use a PaLM-E style (Driess et al., 2023) model that generates vector-quantized tokens derived from ViT-VQGAN (Yu et al., 2022) that ...
- **p. 5 / 3 METHOD - extractive PDF cue:** By using this prompt, the LLM writes code to generate a series of 3D poses - originally intended to be executed with a motion planner, ...
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers. | p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3). | p. 3 (3 METHOD), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save ... | p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHOD - extractive PDF cue:** Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and ...
- **p. 5 / 3 METHOD - extractive PDF cue:** We follow a similar recipe as described in (Gonzalez Arenas et al., 2023) to build a prompt which contains text descriptions about the objects in ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Given (a) an example robot trajectory, we extract (b) gripper interaction markers, (c) temporal progress along the 2D end-effector waypoints, and (d) end-effector height.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Human, Demonstration, Videos, Hand-object, Interaction, First-person, alternative, input, Behavior, Cloning, Pomerleau, following, RT-1, framework | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Human, Demonstration, Videos, Hand-object, Interaction, First-person, alternative, input, Behavior, Cloning | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | main, contribution, novel, policy, conditioning, framework, RT-Trajectory, fosters, task, generalization | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Behavior, Cloning, Pomerleau, following, RT-1, framework, Brohan, minimizing, log-likelihood, predicted | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHOD - extractive PDF cue:** Human Demonstration Videos with Hand-object Interaction First-person human demonstration videos are an alternative input.
- **p. 5 / 3 METHOD - extractive PDF cue:** Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Each episode τ contains a sequence of pairs of observations ot and actions at: τ ={(ot,at)}.
- **p. 3 / 3 METHOD - extractive PDF cue:** 3.1 OVERVIEW Our goal is to learn a robotic control policy that is able to utilize a 2D coarse trajectory sketch image as its conditioning.
- **p. 15 / B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES - extractive PDF cue:** The 2D trajectory is directly drawn by manual input, which can then be annotated with interaction markers or waypoints corresponding to user-specified heights.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This is often reflected with the type of generalization exhibited in different conditioning mechanisms - for example, if the policy is conditioned on natural language ...
- **p. 3 / 3 METHOD - extractive PDF cue:** During inference time, the user or a high-level planner is presented an initial image observation from the robot camera, and creates a rough 2D trajectory ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Color Grading To express relative temporal motion, which encodes such as velocity and direction, we also explore using the red channel of ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | Concretely, given the proprioceptive information recorded in the episode, we obtain the 3D position of the robot end-effector center defined in the ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | The trajectory sketch is concatenated with each RGB image along the feature dimension in the input sequence (a history of 6 images), ... | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 METHOD - extractive PDF cue:** We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive PDF cue:** RT-Trajectory policies used for evaluation are trained with different random seeds and evaluated with the saved trajectory sketches as conditioning.
- **p. 3 / 3 METHOD - extractive PDF cue:** During inference time, the user or a high-level planner is presented an initial image observation from the robot camera, and creates a rough 2D trajectory ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, three, basic, elements, constructing, trajectory, representation, format, Trajectories, Color, Grading, Interaction, Markers, then, train, transformer-based, control, policy, conditioned, sketches.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | Can RT-Trajectory generalize to tasks beyond those contained in the training dataset? | p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Coverage / augmentation | Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper interactions of query trajectories to the ... | p. 10 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Downstream learning interface | Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 22 / Figure/Table caption - extractive PDF cue:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive PDF cue:** We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests an intriguing opportunity: if a trajectory-conditioned robot ...
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive PDF cue:** Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a few remaining limitations.
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive PDF cue:** 5 CONCLUSION AND LIMITATIONS In this work, we propose a novel policy-conditioning method for training robot manipulation policies capable of generalizing to tasks and motions ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Figure 20: Example of retry behavior. The first image is the trajectory sketch generated from the CaP overlaid on the initial observation. The remaining images ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive PDF cue:** With little to moderate trajectory prompt engineering, we find that RT-Trajectory is able to successfully perform a variety of tasks requiring novel motion generalization and ...
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive PDF cue:** If all attempts fail, we just save the trajectory sketch from the last episode.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 METHOD), p. 3 (3 METHOD), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), objective p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), temporal p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 15 (B.4 IMPLEMENTATION DETAILS FOR RT-1-Goal), p. 5 (3 METHOD), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
