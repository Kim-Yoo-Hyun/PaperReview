# Evaluation - XSkill: Cross Embodiment Skill Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.09955. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4 Evaluation), p. 6 (4 Evaluation)): [XSkill] achieves 70.2% and 60% success (Tab.

## Evaluation Body Digest

- **p. 6 / 4 Evaluation - extractive body cue:** During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: ...
- **p. 6 / 4 Evaluation - extractive body cue:** We test XSkill on both simulated and real-world environments: • Franka Kitchen: is a simulated kitchen environment [71] that includes 7 sub-tasks and is accompanied ...
- **p. 7 / 4 Evaluation - extractive body cue:** For instance, the robot struggles to complete tasks involving grasping the cloth followed by closing the drawer, since no such transition dynamics are present in ...
- **p. 7 / 4 Evaluation - extractive body cue:** 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines.
- **p. 6 / 4 Evaluation - extractive body cue:** The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...
- **p. 6 / 4 Evaluation - extractive body cue:** If the robot executes an undemonstrated sub-task, the episode ends.
- **p. 7 / 4 Evaluation - extractive body cue:** [XSkill] achieves 70.2% and 60% success (Tab.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 4 Evaluation (p. 6); A.3 Additional Experiment Results (p. 15); A.4 Implementation Details (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | [XSkill] achieves 70.2% and 60% success (Tab. | p. 7 (4 Evaluation) |
| 4 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. | p. 7 (4 Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Transfer & Composition: During inference, a human demonstration of a new task is given, XSkill first extracts a sequence of skills, which ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for ... | p. 8 (Figure/Table caption) |
| 4 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. | p. 6 (4 Evaluation) |

## Dataset / Benchmark Role

- **p. 6 / 4 Evaluation - extractive body cue:** During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: ...
- **p. 6 / 4 Evaluation - extractive body cue:** We test XSkill on both simulated and real-world environments: • Franka Kitchen: is a simulated kitchen environment [71] that includes 7 sub-tasks and is accompanied ...
- **p. 7 / 4 Evaluation - extractive body cue:** For instance, the robot struggles to complete tasks involving grasping the cloth followed by closing the drawer, since no such transition dynamics are present in ...
- **p. 7 / 4 Evaluation - extractive body cue:** 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Cross Embodiment Skill Discovery. XSkill first learns a cross-embodiment skill representation space (XSkill Space on the left). During inference, given a human demonstration ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Transfer & Composition: During inference, a human demonstration of a new task is given, XSkill first extracts a sequence of skills, which can ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Evaluation Environments. Evaluation protocol. During inference, the robot is required to accomplish the sub-tasks in the same order as demonstrated in the prompt ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: XSkill embedding. (a) We utilize t-SNE visualization to showcase the alignment of skill representa- tions among various embodiments when in contact with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Simulation Result (%) Same Cross Embodiment Avg Execution speed × 1 × 1 × 1.3 × 1.5 / GCD Policy 91.4
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld ... | embodiment, simulator version and control stack | p. 6 (4 Evaluation), p. 6 (4 Evaluation) |
| Task/environment | We test XSkill on both simulated and real-world environments: • Franka Kitchen: is a simulated kitchen environment [71] that includes 7 sub-tasks and is ... | reset, timeout, object/scene variation | p. 6 (4 Evaluation), p. 7 (4 Evaluation) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (3 Approach), p. 3 (3 Approach) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. | definition/direction/unit from same section | p. 6 (4 Evaluation) |
| Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| If the robot executes an undemonstrated sub-task, the episode ends. | definition/direction/unit from same section | p. 6 (4 Evaluation) |
| [XSkill] achieves 70.2% and 60% success (Tab. | definition/direction/unit from same section | p. 7 (4 Evaluation) |
| Additionally, we visualize the projected prototypes for human and robot completion of the same task in Fig. | definition/direction/unit from same section | p. 7 (4 Evaluation) |
| Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. | comparison identity and matched condition | p. 7 (4 Evaluation) |
| The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. | comparison identity and matched condition | p. 6 (4 Evaluation) |
| We compare XSkill with the following baselines: • GCD Policy: Instead of using skill-conditioned policy, we compare to a goal-conditioned diffusion policy π(at/st, gt), ... | comparison identity and matched condition | p. 6 (4 Evaluation) |
| Consequently, the performance of [XSkill] with cross-embodiment prompts only drops around 5%, compared to using the same embodiment prompt (Tab. | comparison identity and matched condition | p. 7 (4 Evaluation) |
| Figure 3: Transfer & Composition: During inference, a human demonstration of a new task is given, XSkill first extracts a sequence of skills, which ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation study on K, time contrastive loss, and more implementation details can be found in the supplementary material. | component/input/data sensitivity | p. 6 (4 Evaluation) |
| Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| NN-composition: XSkill removing skill alignment transformer. | component/input/data sensitivity | p. 6 (4 Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the ... | [XSkill] achieves 70.2% and 60% success (Tab. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4 Evaluation), p. 6 (4 Evaluation) |
| Primary metric/result | 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. | numeric claim only at cited anchor | p. 7 (4 Evaluation) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Evaluation - extractive body cue:** We test XSkill on both simulated and real-world environments: • Franka Kitchen: is a simulated kitchen environment [71] that includes 7 sub-tasks and is accompanied ...
- **p. 7 / 4 Evaluation - extractive body cue:** 14.60s Probability 0 1 Probability 0 1 33.64s Turn on Light Close Drawer Open Oven Grasp Cloth Robot Human (a) t-SNE Visualization of Skill Space ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The ablation study on K, time contrastive loss, and more implementation details can be found in the supplementary material. | p. 6 (4 Evaluation) |
| TCN: Same as the GCD Policy above but replacing the video encoder with pre-trained Time-Contrastive Network (TCN)[67]. • XSkill w. | p. 6 (4 Evaluation) |
| Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision backbone and ... | p. 4 (3 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...

- **PDF anchors reviewed:** datasets p. 6 (4 Evaluation), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 7 (4 Evaluation), metrics p. 6 (4 Evaluation), p. 8 (Figure/Table caption), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 3 (Figure/Table caption), baselines p. 7 (4 Evaluation), p. 6 (4 Evaluation), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 5 (Figure/Table caption), p. 3 (Figure/Table caption), results p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4 Evaluation), p. 6 (4 Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
