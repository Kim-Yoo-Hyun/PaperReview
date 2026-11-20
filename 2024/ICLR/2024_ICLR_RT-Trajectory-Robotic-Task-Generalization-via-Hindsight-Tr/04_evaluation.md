# Evaluation - RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.01977; PDF retrieval source: https://arxiv.org/pdf/2311.01977. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES)): Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are described in App. B.3. The resulting ...

## Evaluation Body Digest

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Can RT-Trajectory generalize to tasks beyond those contained in the training dataset?
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Our real robot experiments aim to study the following questions: 1.
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** Note that we observe that our evaluated policies can have non-zero success rates on the scenes where we fail to find a successful episode during ...
- **p. 14 / B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** Given the current robot camera image, a user can drag and move the mouse to draw curves on the canvas.
- **p. 14 / B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** As the main trajectory generation method we study is user-specified trajectory drawings, we develop a graphical user interface (GUI) for users to draw trajectory sketches.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen motions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are described ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5); A EXPERIMENT DETAILS (p. 14); A.3 QUANTITATIVE RESULTS FOR UNSEEN TASKS (p. 14); B IMPLEMENTATION DETAILS FOR DIFFERENT INPUT MODALITIES (p. 14); B.4 IMPLEMENTATION DETAILS FOR RT-1-Goal (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Example RT-Trajectory evaluations in realistic scenarios involving (a) novel articulated objects requiring new motions, (b) manipulation on new surfaces in new buildings ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 14: Evaluation trajectories for new skills and their 10 closest trajectories from the training set. Each row shows three frames of a skill ... | p. 17 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Success rates for unseen tasks when conditioning with human drawn sketches. B IMPLEMENTATION DETAILS FOR DIFFERENT INPUT MODALITIES B.1 GUI FOR HUMAN-DRAWN ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Can RT-Trajectory generalize to tasks beyond those contained in the training dataset?
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Our real robot experiments aim to study the following questions: 1.
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** Note that we observe that our evaluated policies can have non-zero success rates on the scenes where we fail to find a successful episode during ...
- **p. 14 / B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** Given the current robot camera image, a user can drag and move the mouse to draw curves on the canvas.
- **p. 14 / B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** As the main trajectory generation method we study is user-specified trajectory drawings, we develop a graphical user interface (GUI) for users to draw trajectory sketches.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We propose RT-Trajectory, a framework for utilizing coarse trajectory sketches for policy conditioning. We train on hindsight trajectory sketches (top left) and evaluate ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: The choice of robot policy representation balances specification detail and focusing policies on "what to do" compared with "how to do it". Policy ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of the two hindsight trajectory sketch representations we study. Given (a) an example robot trajectory, we extract (b) gripper interaction markers, (c) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of trajectory sketches overlaid on the initial image for 7 unseen skills. From left to right: Place Fruit, Upright and Move, Fold ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen motions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Trajectory from human demonstration video to fold a towel. From left to right, the first 4 images show the human demonstration, and the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are described ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Example trajectory from image generation models. From left to right, the first image shows the overlaid trajectory sketch, and the next 4 images ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Can RT-Trajectory generalize to tasks beyond those contained in the training dataset? | embodiment, simulator version and control stack | p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Task/environment | For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory ... | reset, timeout, object/scene variation | p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 5 (4 EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 4 (3 METHOD), p. 3 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4: Success rates for unseen tasks when conditioning with human drawn sketches. B IMPLEMENTATION DETAILS FOR DIFFERENT INPUT MODALITIES B.1 GUI FOR HUMAN-DRAWN ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Note that we observe that our evaluated policies can have non-zero success rates on the scenes where we fail to find a successful episode ... | definition/direction/unit from same section | p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Figure 13: Left: The GUI for users to draw trajectory sketches given the robot's current camera image. The 2D trajectory is directly drawn by ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 8: Example RT-Trajectory evaluations in realistic scenarios involving (a) novel articulated objects requiring new motions, (b) manipulation on new surfaces in new buildings ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper interactions of query trajectories to the first gripper ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 12: We visualize the distribution of Fr´echet distances of query trajectories to the most similar training trajectories, as measured by motion similarity. The ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper interactions of query trajectories to the first gripper ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Figure 2: The choice of robot policy representation balances specification detail and focusing policies on "what to do" compared with "how to do it". ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 9: Each row contains 4 instances of an initial image of an evaluation rollout super-imposed with the executed evaluation trajectory (red) compared with ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 12: We visualize the distribution of Fr´echet distances of query trajectories to the most similar training trajectories, as measured by motion similarity. The ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Table 3: The list of unseen evaluation tasks with their descriptions and example language instructions. Language instructions are only used for language-conditioned baselines. "Count" ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Table 2: The list of seen training tasks with their descriptions and example language instructions. Language instructions are only used for language-conditioned baselines. "Count" ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization. | Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Primary metric/result | Figure 8: Example RT-Trajectory evaluations in realistic scenarios involving (a) novel articulated objects requiring new motions, (b) manipulation on new surfaces in new buildings ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests an intriguing opportunity: if a trajectory-conditioned ... | p. 8 (3. What emergent capabilities are enabled by RT-Trajectory?) |
| body limitation/failure cue | Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a few remaining limitations. | p. 9 (3. What emergent capabilities are enabled by RT-Trajectory?) |
| body limitation/failure cue | 5 CONCLUSION AND LIMITATIONS In this work, we propose a novel policy-conditioning method for training robot manipulation policies capable of generalizing to tasks and ... | p. 9 (3. What emergent capabilities are enabled by RT-Trajectory?) |
| body limitation/failure cue | Figure 20: Example of retry behavior. The first image is the trajectory sketch generated from the CaP overlaid on the initial observation. The remaining ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | With little to moderate trajectory prompt engineering, we find that RT-Trajectory is able to successfully perform a variety of tasks requiring novel motion generalization ... | p. 8 (3. What emergent capabilities are enabled by RT-Trajectory?) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| RT-Trajectory policies used for evaluation are trained with different random seeds and evaluated with the saved trajectory sketches as conditioning. | p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory ... | p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| During inference time, the user or a high-level planner is presented an initial image observation from the robot camera, and creates a rough 2D ... | p. 3 (3 METHOD) |
| Similarly, we can find the key time steps for the opening action. | p. 4 (3 METHOD) |
| Thus, we explore visual markers that explicitly highlight the time steps when the gripper begins to grasp and release objects. | p. 4 (3 METHOD) |
| Prompting LLMs with Code as Policies Large Language Models have demonstrated the ability to write code to perform robotics tasks (Liang et al., 2022). | p. 5 (3 METHOD) |
| We study 4 different methods to generate trajectory sketches: human drawings, human videos, prompting LLMs with Code as Policies, and image generation models. | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests an intriguing opportunity: if a trajectory-conditioned robot ...
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a few remaining limitations.
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** 5 CONCLUSION AND LIMITATIONS In this work, we propose a novel policy-conditioning method for training robot manipulation policies capable of generalizing to tasks and motions ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 20: Example of retry behavior. The first image is the trajectory sketch generated from the CaP overlaid on the initial observation. The remaining images ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** With little to moderate trajectory prompt engineering, we find that RT-Trajectory is able to successfully perform a variety of tasks requiring novel motion generalization and ...

- **Evidence anchors reviewed:** datasets p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 14 (B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES), p. 14 (B.1 GUI FOR HUMAN-DRAWN TRAJECTORY SKETCHES), metrics p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 10 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 14 (Figure/Table caption), p. 14 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
