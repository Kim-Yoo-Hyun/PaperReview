# Evaluation - Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.13705; PDF retrieval source: https://arxiv.org/pdf/2304.13705. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS)): ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), or uniformly in ...
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** Data Collection For all 6 real-world tasks, we collect demonstrations using ALOHA teleoperation.
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** To teleoperate in simulation, we use the "leader robots" of ALOHA to control the simulated robot, with the operator looking at the real-time renderings of ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** For ease of reproducibility, we build two simulated fine manipulation tasks in MuJoCo [63], in addition to 6 real-world tasks with ALOHA.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** For each of the 6 real-world tasks, we illustrate the initializations and the subtasks.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** The left arm then opens its gripper to release the tape (Subtask#4 Hang). #1 #2 #3 init. #1 #2 #3 init. #1 #2 #3 init. ...
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** For real-world tasks, we run one seed and evaluate with 25 trials.
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** We report the success rate of the 3 remaining real-world tasks in Table II.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task. | p. 9 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on ... | p. 10 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method ACT reaches 84% success for Cup Open, 20% for Thread Velcro, 64% for Prep Tape and 92% for Put On Shoe, again ... | p. 9 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, ACT significantly outperforms previous methods. | p. 8 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Open Cup (real) Thread Velcro (real) Prep Tape (real) Put On Shoe (real) Tip Over Grasp Open Lid Lift Grasp Insert Grasp Cut Handover ... | p. 8 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), or uniformly in ...
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** Data Collection For all 6 real-world tasks, we collect demonstrations using ALOHA teleoperation.
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** To teleoperate in simulation, we use the "leader robots" of ALOHA to control the simulated robot, with the operator looking at the real-time renderings of ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** For ease of reproducibility, we build two simulated fine manipulation tasks in MuJoCo [63], in addition to 6 real-world tasks with ALOHA.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** For each of the 6 real-world tasks, we illustrate the initializations and the subtasks.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** The left arm then opens its gripper to release the tape (Subtask#4 Hang). #1 #2 #3 init. #1 #2 #3 init. #1 #2 #3 init. ...
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** For real-world tasks, we run one seed and evaluate with 25 trials.
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** We report the success rate of the 3 remaining real-world tasks in Table II.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: ALOHA : A Low-cost Open-source Hardware System for Bimanual Teleoperation. The whole system costs <$20k with off-the-shelf robots and 3D printed components. Left: ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Left: Camera viewpoints of the front, top, and two wrist cameras, together with an illustration of the bimanual workspace of ALOHA. Middle: Detailed ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Architecture of Action Chunking with Transformers (ACT). We train ACT as a Conditional VAE (CVAE), which has an encoder and a decoder. Left: ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 5: We employ both Action Chunking and Temporal Ensembling when applying actions, instead of interleaving observing and executing. rable to a single research arm ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Real-World Task Definitions. For each of the 6 real-world tasks, we illustrate the initializations and the subtasks.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 7: Simulated Task Definitions. For each of the 2 simulated tasks, we illustrate the initializations and the subtasks. Cube Transfer (sim) Bimanual Insertion (sim) ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on the ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Fig. 9: Teleoperation task examples with ALOHA. We include videos on the project website. incoming observations (images and joints) are fed into the model in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), or uniformly ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Task/environment | Data Collection For all 6 real-world tasks, we collect demonstrations using ALOHA teleoperation. | reset, timeout, object/scene variation | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Open Cup (real) Thread Velcro (real) Prep Tape (real) Put On Shoe (real) Tip Over Grasp Open Lid Lift Grasp Insert Grasp Cut Handover ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| Cube Transfer (sim) Bimanual Insertion (sim) Slide Ziploc (real) Slot Battery (real) Touched Lifted Transfer Grasp Contact Insert Grasp Pinch Open Grasp Place Insert ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| For these tasks, we only compare with BeT, which has the highest task success rate so far. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| We report the success rate on both scripted data (left of separation bar) and human data (right of separation bar). | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| For this task to be successful, the robot must use visual feedback to correct for perturbations with each grasp, as even a few millimeters ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Fig. 1: ALOHA : A Low-cost Open-source Hardware System for Bimanual Teleoperation. The whole system costs <$20k with off-the-shelf robots and 3D printed components. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task. | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |
| Overall, ACT significantly outperforms previous methods. | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| We only compare with the best performing baseline BeT. tape dispenser. | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| For the two simulated tasks with scripted or human data, ACT outperforms the best previous method in success rate by 59%, 49%, 29%, and ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our ablations in Subsection VI-A also shows that chunking can significantly improve these prior methods when incorporated. | component/input/data sensitivity | p. 9 (V. EXPERIMENTS) |
| Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| The visual feature extractor is a pretrained ResNet finetuned on demonstration data with unsupervised learning. | component/input/data sensitivity | p. 9 (V. EXPERIMENTS) |
| Fig. 1: ALOHA : A Low-cost Open-source Hardware System for Bimanual Teleoperation. The whole system costs <$20k with off-the-shelf robots and 3D printed components. ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm. | ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Primary metric/result | Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Tasks All 8 tasks require fine-grained, bimanual manipulation, and are illustrated in Figure 6.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), or uniformly in ...
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** For the two simulated tasks, we report [training with scripted data / training with human data], with 3 seeds and 50 policy evaluations each.
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** For the real-world tasks, we report training with human data, with 1 seed and 25 evaluations.
- **p. 8 / V. EXPERIMENTS - extractive PDF cue:** Each episode takes 8-14 seconds for the human operator to perform depending on the complexity of the task, which translates to 400-700 time steps given ...
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** For simulated tasks, we average performance across 3 random seeds with 50 trials each.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | The failure modes we observe are 1) at stage 2, the right arm closes its gripper too early and fails to grasp the tail ... | p. 9 (V. EXPERIMENTS) |
| body limitation/failure cue | Because of the cup's small size, the grippers cannot grasp the body of the cup by just approaching it from the side. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | The left arm then lays the tape segment flat on the surface of the box while the right gripper pushes down on the tape ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 10: Image observation examples for 5 real-world tasks. The 4 columns are [top camera, front camera, left wrist camera, right wrist camera] respectively. ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | In contrast, VINN retrieves ground-truth actions from the dataset and does not suffer from this issue. | p. 9 (VI. ABLATIONS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For real-world tasks, we run one seed and evaluate with 25 trials. | p. 9 (V. EXPERIMENTS) |
| For simulated tasks, we average performance across 3 random seeds with 50 trials each. | p. 9 (V. EXPERIMENTS) |
| The training takes around 5 hours on a single 11G RTX 2080 Ti GPU, and the inference time is around 0.01 seconds on the ... | p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Similar to Thread Velcro, this task requires multiple steps of delicate coordination between the two arms. | p. 6 (V. EXPERIMENTS) |
| For the real-world tasks, we report training with human data, with 1 seed and 25 evaluations. | p. 8 (V. EXPERIMENTS) |
| For the two simulated tasks, we report [training with scripted data / training with human data], with 3 seeds and 50 policy evaluations each. | p. 8 (V. EXPERIMENTS) |
| In our implementation, we fix the chunk size to be k: every k steps, the agent receives an observation, generates the next k actions, ... | p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| A naïve implementation of action chunking can be suboptimal: a new environment observation is incorporated abruptly every k steps and can result in jerky ... | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure.
- **p. 9 / V. EXPERIMENTS - extractive PDF cue:** The failure modes we observe are 1) at stage 2, the right arm closes its gripper too early and fails to grasp the tail of ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Because of the cup's small size, the grippers cannot grasp the body of the cup by just approaching it from the side.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** The left arm then lays the tape segment flat on the surface of the box while the right gripper pushes down on the tape to ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Fig. 10: Image observation examples for 5 real-world tasks. The 4 columns are [top camera, front camera, left wrist camera, right wrist camera] respectively. We ...
- **p. 9 / VI. ABLATIONS - extractive PDF cue:** In contrast, VINN retrieves ground-truth actions from the dataset and does not suffer from this issue.

- **PDF anchors reviewed:** datasets p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), metrics p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption), p. 6 (V. EXPERIMENTS), baselines p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), results p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
