# Evaluation - VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8e6f3d53b2bef98fce17e699557f5f11-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8e6f3d53b2bef98fce17e699557f5f11-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 2 (Figure/Table caption)): Results indicate that our method attains high success rates on complex tasks with a single human video demonstration, and increasing the number of videos yields performance gains.

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** To assess our approach on challenging robotic manipulation tasks, the RLBench [65] benchmark is utilized for simulation tasks.
- **p. 7 / 4 Experiments - extractive body cue:** GraphIRL is trained in simulators with paired robot videos, Demo2code and our method learns skills with human videos in real-world experiments and robot videos in ...
- **p. 9 / 4 Experiments - extractive body cue:** These scenarios encompass: (I) The task execution may exceed the hardware limitations of the physical robot, inducing inverse kinematics (IK) errors.
- **p. 9 / 4 Experiments - extractive body cue:** Since the training datasets for VLMs exhibit a significant lack of data related to robot dynamics, these models lack associated knowledge, exhibiting a limited capacity ...
- **p. 8 / 4 Experiments - extractive body cue:** Experiments are conducted in real-world unseen environments, utilizing distinct viewpoints, as shown in Figure 4, where the first angle serves as the default perspective used ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.3 Real-world Long-Horizon Tasks Experimental setup.
- **p. 15 / A Implementation details - extractive body cue:** In human-object interaction grounding module, the Tokenize Anything [44] model is employed during task recognition to improve fine-grained scene understanding ability.
- **p. 15 / A Implementation details - extractive body cue:** The robotic arm's motion planning is facilitated by the integration of the MoveIt module, renowned for its comprehensive motion planning capabilities, and the OMPL [58] ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); A Implementation details (p. 15); B Experimental Setup (p. 15); B.2 Real-world experimental setup (p. 15); 4. Experimental Result Reproducibility (p. 24); 7. Experiment Statistical Significance (p. 25); 8. Experiments Compute Resources (p. 26).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results indicate that our method attains high success rates on complex tasks with a single human video demonstration, and increasing the number of videos ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Quantitative results, presented in Table 2, demonstrate that VLMimic clearly outperforms other methods across all tasks, particularly in the "unseen" environment (UE). | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method, learned with only 5 human videos, obviously outperforms R3M-DP and DP by over 61% in overall performance, despite both being trained on ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experimental results, as depicted in Table 3, obviously exhibit a substantial enhancement achieved by our method over baseline methods. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Variants compare constraints exclusively utilizing either visualized interactions or keypoints exhibit decreased success rates. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** To assess our approach on challenging robotic manipulation tasks, the RLBench [65] benchmark is utilized for simulation tasks.
- **p. 7 / 4 Experiments - extractive body cue:** GraphIRL is trained in simulators with paired robot videos, Demo2code and our method learns skills with human videos in real-world experiments and robot videos in ...
- **p. 9 / 4 Experiments - extractive body cue:** These scenarios encompass: (I) The task execution may exceed the hardware limitations of the physical robot, inducing inverse kinematics (IK) errors.
- **p. 9 / 4 Experiments - extractive body cue:** Since the training datasets for VLMs exhibit a significant lack of data related to robot dynamics, these models lack associated knowledge, exhibiting a limited capacity ...
- **p. 8 / 4 Experiments - extractive body cue:** Experiments are conducted in real-world unseen environments, utilizing distinct viewpoints, as shown in Figure 4, where the first angle serves as the default perspective used ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.3 Real-world Long-Horizon Tasks Experimental setup.
- **p. 15 / A Implementation details - extractive body cue:** In human-object interaction grounding module, the Tokenize Anything [44] model is employed during task recognition to improve fine-grained scene understanding ability.
- **p. 15 / A Implementation details - extractive body cue:** The robotic arm's motion planning is facilitated by the integration of the MoveIt module, renowned for its comprehensive motion planning capabilities, and the OMPL [58] ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of our VLMimic. (a) Typical VIL methods struggle to generalize to unseen environments, and (b) current methods naively utilize VLMs as planners, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of our VLMimic. (a) The human-object interaction grounding module parses videos into multiple segments and captures object-centric movements. Then, (b) a skill ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of Human-object interaction grounding module. (a) It recognizes tasks and related objects from human videos, (b) parses videos into multiple segments based ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rates on RLbench. "Obs-act", "Template", and "Video" indicate paired observation- action sequences, code templates, and videos performing subtasks. Methods R3M-DP DP GraphIRL ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Success rates on real-world manipulation experiments. "Obs-act", "Template", and "Video" indicate paired observation-action sequences, code templates, and videos performing subtasks. "SE" and "UE" ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Success rates on long-horizon tasks. "Obs-act", "Template", and "Video" indicate observation- action sequences, code templates, and videos performing tasks. Methods Type of demos ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Robustness against viewpoint variance. Methods Viewpoint 1 Viewpoint 2 Viewpoint 3 Viewpoint 4 Ours 0.71(±0.15)
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Configuration of various viewpoints. Open microwave Chemistry experiment Open oven Collision IK Error IK Error

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To assess our approach on challenging robotic manipulation tasks, the RLBench [65] benchmark is utilized for simulation tasks. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | GraphIRL is trained in simulators with paired robot videos, Demo2code and our method learns skills with human videos in real-world experiments and robot videos ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Results indicate that our method attains high success rates on complex tasks with a single human video demonstration, and increasing the number of videos ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Success criteria are human-evaluated and the success rate is calculated from 10 randomized object positions and orientations. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Variants compare constraints exclusively utilizing either visualized interactions or keypoints exhibit decreased success rates. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Table 1: Success rates on RLbench. "Obs-act", "Template", and "Video" indicate paired observation- action sequences, code templates, and videos performing subtasks. Methods R3M-DP DP ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| 4.4 Robustness against viewpoint variance The keypoint-centric representation approach enables our method to tolerate different observational perspectives. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The performance of VLMimic on long-horizon tasks is quantitatively evaluated by its successful completion of six distinct tasks, each comprising at least five subtasks. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| VLMimic is compared with five representative methods: (1) R3M-DP that utilizes the pre-trained R3M visual representation [13] with the state-of-the-art (SOTA) diffusion policy [7]; ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Upon action completion, the real-time object positions are used to assess task success until manual confirmation or a preset time is reached. | definition/direction/unit from same section | p. 15 (A Implementation details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| VLMimic is compared with five representative methods: (1) R3M-DP that utilizes the pre-trained R3M visual representation [13] with the state-of-the-art (SOTA) diffusion policy [7]; ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Quantitative results, presented in Table 2, demonstrate that VLMimic clearly outperforms other methods across all tasks, particularly in the "unseen" environment (UE). | comparison identity and matched condition | p. 7 (4 Experiments) |
| Our method, learned with only 5 human videos, obviously outperforms R3M-DP and DP by over 61% in overall performance, despite both being trained on ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Since baseline methods struggle to complete long-horizon tasks in the UE setting, experiments are conducted in the SE setting. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Experimental results, as depicted in Table 3, obviously exhibit a substantial enhancement achieved by our method over baseline methods. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Visual comparison facilitates semantic contrast in VLM, while keypoint values provide fine-grained geometric information. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Variants that exclusively reason semantic constraints or directly obtain geometric constraints without semantic analysis, lead to diminished performance. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Table 5: Ablation experiments with VLMimic on real-world manipulation experiments. "SE" and "UE" are seen and unseen environments. Default settings are marked in gray ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| We investigate the capacity of VLMimic to acquire skills from a limited collection of video demonstrations, without requiring additional training. | component/input/data sensitivity | p. 7 (4 Experiments) |
| The second variant employs the DBScan clustering algorithm to group grasp poses and derive constraints as bounded regions. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Figure 7: Visualization of the wash-pan task. • Make cucumber slices (Make slices) - Initial state: The refrigerator is to the left of the ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Figure 1: Illustration of our VLMimic. (a) Typical VIL methods struggle to generalize to unseen environments, and (b) current methods naively utilize VLMs as ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows: (I) We propose VLMimic, a novel visual imitation learning framework empowered by VLMs, to learn generalizable ... | Results indicate that our method attains high success rates on complex tasks with a single human video demonstration, and increasing the number of videos ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 2 (Figure/Table caption) |
| Primary metric/result | Quantitative results, presented in Table 2, demonstrate that VLMimic clearly outperforms other methods across all tasks, particularly in the "unseen" environment (UE). | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** Our method, learned with only 5 human videos, obviously outperforms R3M-DP and DP by over 61% in overall performance, despite both being trained on 100 ...
- **p. 15 / A Implementation details - extractive body cue:** In manipulation constraint learning, keypoints are obtained by uniformly sampling 10 points.
- **p. 15 / A Implementation details - extractive body cue:** In manipulation constraint learning, keypoints are obtained by uniformly sampling 10 points.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Examples of failure cases. 4.5 Real-world failure cases Figure 5 elucidates scenarios that present significant challenges for resolution through VLM reasoning. These ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Open microwave Chemistry experiment Open oven Collision IK Error IK Error Figure 5: Examples of failure cases. | p. 9 (4 Experiments) |
| body limitation/failure cue | Thus, we leverage VLMs to detect and address failures during execution by providing them with perceptual results, such as object pose and robot end-effector ... | p. 6 (X Y) |
| body limitation/failure cue | In case of failure detection, object and gripper poses are employed for failure reasoning, where the gripper poses are estimated using the attatched QR ... | p. 15 (A Implementation details) |
| body limitation/failure cue | Despite the ability of VLMs to generate effective constraints, environmental noise, such as trajectory estimation errors, impedes successful task execution. | p. 6 (X Y) |
| body limitation/failure cue | To demonstrate the robustness of our method to varying viewpoints. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| VLMimic is compared with five representative methods: (1) R3M-DP that utilizes the pre-trained R3M visual representation [13] with the state-of-the-art (SOTA) diffusion policy [7]; ... | p. 6 (4 Experiments) |
| We modify it to integrate the analysis results from GPT-4V for Robotics [33], enabling it to transcribe videos into code. | p. 7 (4 Experiments) |
| Compared to CaP and demo2code, our method demonstrates an improvement exceeding 27%, highlighting the significant performance enhancements facilitated by the VLMimic framework. | p. 7 (4 Experiments) |
| Overall R3M-DP Obs-act 100 0.10 0.30 0.20 0.10 0.00 0.10 0.13(±0.09) DP Obs-act 100 0.00 0.20 0.10 0.00 0.10 0.00 0.07(±0.07) GraphIRL Video 100 ... | p. 8 (4 Experiments) |
| These scenarios encompass: (I) The task execution may exceed the hardware limitations of the physical robot, inducing inverse kinematics (IK) errors. | p. 9 (4 Experiments) |
| The effects of these design decisions are assessed by measuring the success rate on realworld manipulation tasks, which is computed across 10 randomized object ... | p. 9 (4 Experiments) |
| These segmentation maps are then utilized to predict object-centric pose sequences using codes generated by VLMs. | p. 15 (A Implementation details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Examples of failure cases. 4.5 Real-world failure cases Figure 5 elucidates scenarios that present significant challenges for resolution through VLM reasoning. These scenarios ...
- **p. 9 / 4 Experiments - extractive body cue:** Open microwave Chemistry experiment Open oven Collision IK Error IK Error Figure 5: Examples of failure cases.
- **p. 6 / X Y - extractive body cue:** Thus, we leverage VLMs to detect and address failures during execution by providing them with perceptual results, such as object pose and robot end-effector trajectories, ...
- **p. 15 / A Implementation details - extractive body cue:** In case of failure detection, object and gripper poses are employed for failure reasoning, where the gripper poses are estimated using the attatched QR scan.
- **p. 6 / X Y - extractive body cue:** Despite the ability of VLMs to generate effective constraints, environmental noise, such as trajectory estimation errors, impedes successful task execution.
- **p. 8 / 4 Experiments - extractive body cue:** To demonstrate the robustness of our method to varying viewpoints.

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 7 (Figure/Table caption), p. 8 (4 Experiments), p. 8 (4 Experiments), baselines p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), results p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Experimental results, as depicted in Table 3, obviously exhibit a substantial enhancement achieved by our method over baseline methods. (p. 8, 4 Experiments).
- **Metric evidence:** Our method, learned with only 5 human videos, obviously outperforms R3M-DP and DP by over 61% in overall performance, despite both being trained on 100 robot demonstrations. (p. 7, 4 Experiments).
- **Baseline/ablation evidence:** VLMimic is compared with five representative methods: (1) R3M-DP that utilizes the pre-trained R3M visual representation [13] with the state-of-the-art (SOTA) diffusion policy [7]; (2) Diffusion Policy (DP) [7], a ... (p. 6, 4 Experiments).
- **Failure/negative evidence:** Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational ... (p. 23, 2. Limitations).
