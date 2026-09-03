# Evaluation - Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33610; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33610. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation)): The results indicate that IALP achieves a success rate of over 80% in all long-term tasks.

## Evaluation Body Digest

- **p. 7 / Problem Formulation - extractive body cue:** While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to factors ...
- **p. 3 / Problem Formulation - extractive body cue:** We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information.
- **p. 7 / Problem Formulation - extractive body cue:** Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all ...
- **p. 5 / Problem Formulation - extractive body cue:** For at predicate, we assume the robot will reach the target position after executing the action to move to the object.
- **p. 5 / Problem Formulation - extractive body cue:** 2023) is used to generate several potential grasps for the robot, with LangSAM masks filtering the object-related grasps.
- **p. 6 / Problem Formulation - extractive body cue:** We investigated the capability of the LLM planner to perform zero-shot planning for long-horizon tasks based on the robot's perception and a pre-built voxel map.
- **p. 6 / Problem Formulation - extractive body cue:** The robot employed the adjust action to modify its position, head tilt, and pane orientation several times to make the manipulated object feasible to grasp ...
- **p. 3 / Problem Formulation - extractive body cue:** The robot is equipped with a primitive action library Lψ, which is inherently imperfect and frequently cause unforeseen situations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Problem Formulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results indicate that IALP achieves a success rate of over 80% in all long-term tasks. | p. 7 (Problem Formulation) |
| Problem Formulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a result, the success rate is substantially lower than that of other configurations. | p. 7 (Problem Formulation) |
| Problem Formulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The Planning Objective The objective is to find a sequence of actions {a1, · · · , aH}, denoted as a1:H, that can achieve ... | p. 3 (Problem Formulation) |
| Problem Formulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which ... | p. 3 (Problem Formulation) |
| Problem Formulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | To achieve this, we constructed a voxel map to provide a static representation of the current environment, employing the natural language mapping approach proposed ... | p. 5 (Problem Formulation) |

## Dataset / Benchmark Role

- **p. 7 / Problem Formulation - extractive body cue:** While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to factors ...
- **p. 3 / Problem Formulation - extractive body cue:** We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information.
- **p. 7 / Problem Formulation - extractive body cue:** Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all ...
- **p. 5 / Problem Formulation - extractive body cue:** For at predicate, we assume the robot will reach the target position after executing the action to move to the object.
- **p. 5 / Problem Formulation - extractive body cue:** 2023) is used to generate several potential grasps for the robot, with LangSAM masks filtering the object-related grasps.
- **p. 6 / Problem Formulation - extractive body cue:** We investigated the capability of the LLM planner to perform zero-shot planning for long-horizon tasks based on the robot's perception and a pre-built voxel map.
- **p. 6 / Problem Formulation - extractive body cue:** The robot employed the adjust action to modify its position, head tilt, and pane orientation several times to make the manipulated object feasible to grasp ...
- **p. 3 / Problem Formulation - extractive body cue:** The robot is equipped with a primitive action library Lψ, which is inherently imperfect and frequently cause unforeseen situations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: The IALP system leverages the reasoning capabil- ities of LLMs and grounding mechanisms to enrich the task representation, enabling plan feasible and optimal ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Promptable and grounding mechanism-based pred- icates. fer actions for solving long-horizon tasks in a close-loop manner. Firstly, the system augments the user instruction ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The proposed IALP system is designed to complete long-horizon mobile manipulation tasks in real world environ- ment. Firstly, it constructs a PDDL problem ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 2: Preconditions and effects of actions in PDDL. obj and pla refer to the name of the object and peaceable space involved in the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: The room environment we used in our tasks. The position of the yellow star is the initial state of the robot. We exclude ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: The states, feasibility feedback, and actions during the execution of long-horizon mobile manipulation tasks.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: The token probability of action candidates generated by the LLM planner for five long-horizon tasks. Task Instruction Place box Pick the paper box ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: The five long-horizon tasks and instructions em- ployed in our experiments. tasks. For motion planning of the robotic arms, we em- ployed Pinocchio ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to ... | embodiment, simulator version and control stack | p. 7 (Problem Formulation), p. 3 (Problem Formulation) |
| Task/environment | We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information. | reset, timeout, object/scene variation | p. 3 (Problem Formulation), p. 7 (Problem Formulation) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 3 (Problem Formulation), p. 3 (Problem Formulation) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (Problem Formulation), p. 6 (Problem Formulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As a result, the success rate is substantially lower than that of other configurations. | definition/direction/unit from same section | p. 7 (Problem Formulation) |
| The results indicate that IALP achieves a success rate of over 80% in all long-term tasks. | definition/direction/unit from same section | p. 7 (Problem Formulation) |
| We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the probability of the next skill ax ... | definition/direction/unit from same section | p. 3 (Problem Formulation) |
| We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that ... | definition/direction/unit from same section | p. 5 (Problem Formulation) |
| We consider the success probability of the action sequence QH x=t p(rx / st:x, at:x) as feasibility score Sfb. | definition/direction/unit from same section | p. 3 (Problem Formulation) |
| A reward of 1 is received if the robot successfully executes with the effects representing the expected state changes. | definition/direction/unit from same section | p. 4 (Problem Formulation) |
| Thus, here we consider the feasibility score of planning single time step, i.e., Sfb = p(rt/st, at). | definition/direction/unit from same section | p. 4 (Problem Formulation) |
| This probability is independent of prior rewards r1:t-1 and actions a1:t-1. | definition/direction/unit from same section | p. 5 (Problem Formulation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list the actions ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as ... | comparison identity and matched condition | p. 3 (Problem Formulation) |
| While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to ... | comparison identity and matched condition | p. 7 (Problem Formulation) |
| We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information. | comparison identity and matched condition | p. 3 (Problem Formulation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For the system without optimal selection, denoted as IALP w/o Optimal Selection, a relatively high success rate is still maintained because feasibility checks are ... | component/input/data sensitivity | p. 7 (Problem Formulation) |
| Ablation Study on Feasibility and Optimality To evaluate the impact of feasibility feedback and optimal selection on system performance, we conducted two ablation experiments, ... | component/input/data sensitivity | p. 7 (Problem Formulation) |
| We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information. | component/input/data sensitivity | p. 3 (Problem Formulation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as ... | The results indicate that IALP achieves a success rate of over 80% in all long-term tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation) |
| Primary metric/result | As a result, the success rate is substantially lower than that of other configurations. | numeric claim only at cited anchor | p. 7 (Problem Formulation) |

- Numeric sentences retained from the body:
- **p. 7 / Problem Formulation - extractive body cue:** Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all ...
- **p. 7 / Problem Formulation - extractive body cue:** Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Planning failures occur when the planner fails to generate the correct action sequence. | p. 7 (Problem Formulation) |
| body limitation/failure cue | All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms failures. | p. 7 (Problem Formulation) |
| body limitation/failure cue | If even one skill fails, then the entire action sequence fails. | p. 3 (Problem Formulation) |
| body limitation/failure cue | For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693 | p. 4 (Problem Formulation) |
| body limitation/failure cue | The entire action sequence a1:H fails, denoted by Sfb = 0, if at least one action fails, i.e., rt = 0, ∃t ∈{1 : ... | p. 4 (Problem Formulation) |
| body limitation/failure cue | We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp. | p. 5 (Problem Formulation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For a given object language description lo, we first convert it to a semantic vector e′ o using the CLIP text encoder. | p. 5 (Problem Formulation) |
| We then compute the optimality scores Sop by summing the token log probabilities of each action's language description. | p. 5 (Problem Formulation) |
| We used three computers: one for controlling the robot with the ROS Noetic system and others for generating navigation manipulation feedback. | p. 6 (Problem Formulation) |
| Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded ... | p. 7 (Problem Formulation) |
| While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to ... | p. 7 (Problem Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 7 / Problem Formulation - extractive body cue:** All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms failures.
- **p. 3 / Problem Formulation - extractive body cue:** If even one skill fails, then the entire action sequence fails.
- **p. 4 / Problem Formulation - extractive body cue:** For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693
- **p. 4 / Problem Formulation - extractive body cue:** The entire action sequence a1:H fails, denoted by Sfb = 0, if at least one action fails, i.e., rt = 0, ∃t ∈{1 : H}.
- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.

- **Evidence anchors reviewed:** datasets p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 7 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation), metrics p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 3 (Problem Formulation), p. 4 (Problem Formulation), baselines p. 7 (Figure/Table caption), p. 3 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), results p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 7: All failure cases of predicate checking in the real- world experiments across five long-horizon tasks. recorded the success cases of the LLM planner generating executable actions, as shown ... (p. 7, Figure/Table caption).
- **Metric evidence:** We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the probability of the next skill ax is considered in terms of the ... (p. 3, Problem Formulation).
- **Baseline/ablation evidence:** Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list the actions and PDDL problems generated for the ... (p. 7, Figure/Table caption).
- **Failure/negative evidence:** Planning failures occur when the planner fails to generate the correct action sequence. (p. 7, Problem Formulation).
