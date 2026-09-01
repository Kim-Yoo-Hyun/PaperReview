# Evaluation - AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption)): It can reflect how much improvement our method achieves.

## Evaluation Body Digest

- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream tasks ...
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** In practice, during testing, we manually place the robot in an ideal initial configuration (e.g., already grasping the stamp) to evaluate these two models' capability ...
- **p. 5 / 4.1. Setup - extractive body cue:** The robot is required to stamp within a designated region.
- **p. 5 / 4.1. Setup - extractive body cue:** The robot is required to rotate a lid to open a container.
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** We report the success rate of each subtask, reflecting the progress.
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** Furthermore, when compared with policies that incorporate tactile feedback like VTLA and RDP, our model still achieves superior performance in contact-rich phase manipulation, validating the ...
- **p. 5 / 4.1. Setup - extractive body cue:** Insufficient compliance could result in collisions with the neck of the vase. d).
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary across ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.2. Contact-rich Task Evaluation (p. 5); 4.3. Modality-agnostic Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Contact-rich Task Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | It can reflect how much improvement our method achieves. | p. 5 (4.2. Contact-rich Task Evaluation) |
| 4.2. Contact-rich Task Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | During the contact-rich stage, AT-VLA achieves an improvement over them, clearly demonstrating the necessity of tactile signals for complex manipulation tasks. | p. 6 (4.2. Contact-rich Task Evaluation) |
| 4.2. Contact-rich Task Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, when compared with policies that incorporate tactile feedback like VTLA and RDP, our model still achieves superior performance in contact-rich phase manipulation, validating ... | p. 6 (4.2. Contact-rich Task Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. AT-VLA improves upon previous VLA approaches in contact-rich tasks by introducing Adaptive Tactile Injection, which balances pretrained knowledge with the learning of ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream tasks ...
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** In practice, during testing, we manually place the robot in an ideal initial configuration (e.g., already grasping the stamp) to evaluate these two models' capability ...
- **p. 5 / 4.1. Setup - extractive body cue:** The robot is required to stamp within a designated region.
- **p. 5 / 4.1. Setup - extractive body cue:** The robot is required to rotate a lid to open a container.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. AT-VLA improves upon previous VLA approaches in contact-rich tasks by introducing Adaptive Tactile Injection, which balances pretrained knowledge with the learning of newly ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Framework of AT-VLA. The tactile gate adaptively determines whether tactile tokens should be used as conditional inputs for action generation within the Action ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary across ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluation in contact-rich tasks. We report the success rate of each subtask, reflecting the progress. Unzip Bag Stamp
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Modality-agnostic evaluation.The AT-VLA variants with (w/.) and without (w/o.) tactile input share identical model weights, differing only in whether tactile information is provided ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing modalities ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study. Each variant selectively removes or changes components to assess their contributions. Components Tactile Format Tasks Tactile Gate Adaptive Cross Attention

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream ... | embodiment, simulator version and control stack | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Task/environment | In practice, during testing, we manually place the robot in an ideal initial configuration (e.g., already grasping the stamp) to evaluate these two models' ... | reset, timeout, object/scene variation | p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the success rate of each subtask, reflecting the progress. | definition/direction/unit from same section | p. 6 (4.2. Contact-rich Task Evaluation) |
| Furthermore, when compared with policies that incorporate tactile feedback like VTLA and RDP, our model still achieves superior performance in contact-rich phase manipulation, validating ... | definition/direction/unit from same section | p. 6 (4.2. Contact-rich Task Evaluation) |
| Insufficient compliance could result in collisions with the neck of the vase. d). | definition/direction/unit from same section | p. 5 (4.1. Setup) |
| Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. AT-VLA improves upon previous VLA approaches in contact-rich tasks by introducing Adaptive Tactile Injection, which balances pretrained knowledge with the learning of ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Framework of AT-VLA. The tactile gate adaptively determines whether tactile tokens should be used as conditional inputs for action generation within the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, ... | comparison identity and matched condition | p. 6 (4.2. Contact-rich Task Evaluation) |
| As shown in Table 1, our model outperforms all baseline methods. | comparison identity and matched condition | p. 6 (4.2. Contact-rich Task Evaluation) |
| We compare with four SOTA baselines: 1. | comparison identity and matched condition | p. 5 (4.2. Contact-rich Task Evaluation) |
| 2. π0.5 [6] is a state-of-the-art VLA model consisting of both pretraining and post-training stages. | comparison identity and matched condition | p. 5 (4.2. Contact-rich Task Evaluation) |
| Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Table 3. Ablation study. Each variant selectively removes or changes components to assess their contributions. Components Tactile Format Tasks Tactile Gate Adaptive Cross Attention | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablation study. Each variant selectively removes or changes components to assess their contributions. Components Tactile Format Tasks Tactile Gate Adaptive Cross Attention | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Modality-agnostic evaluation.The AT-VLA variants with (w/.) and without (w/o.) tactile input share identical model weights, differing only in whether tactile information is provided during ... | component/input/data sensitivity | p. 6 (4.3. Modality-agnostic Evaluation) |
| Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, ... | component/input/data sensitivity | p. 6 (4.2. Contact-rich Task Evaluation) |
| This task demands precise force and motion coordination to ensure smooth rotation without slipping. | component/input/data sensitivity | p. 5 (4.1. Setup) |
| Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of ... | It can reflect how much improvement our method achieves. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | During the contact-rich stage, AT-VLA achieves an improvement over them, clearly demonstrating the necessity of tactile signals for complex manipulation tasks. | numeric claim only at cited anchor | p. 6 (4.2. Contact-rich Task Evaluation) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Setup - extractive body cue:** For each task, we collect 30-50 demonstrations and test in 15 trials.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** In this way, the fast stream leverages the pretrained representations from the slow stream to ensure reliable visual perception, while simultaneously reacting to tactile dynamics ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where ... | p. 6 (4.2. Contact-rich Task Evaluation) |
| body limitation/failure cue | Failure to do so may cause the zipper to get stuck or jammed. b). | p. 5 (4.1. Setup) |
| body limitation/failure cue | We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their ... | p. 6 (4.2. Contact-rich Task Evaluation) |
| body limitation/failure cue | Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Future work may explore scaling this framework to more complex tasks and diverse real-world environments, further advancing general-purpose embodied intelligence. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Insufficient compliance could result in collisions with the neck of the vase. d). | p. 5 (4.1. Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Since the official implementation is not publicly available, we replicate it based on the DexVLA [39] codebase, which also builds upon Qwen2-VL. | p. 6 (4.2. Contact-rich Task Evaluation) |
| For each task, we collect 30-50 demonstrations and test in 15 trials. | p. 5 (4.1. Setup) |
| We use the hardware, AgiBot Genie1, featuring dual 7-DoF arms, equipped with a front-view camera and two cameras mounted on the wrist. | p. 5 (4.1. Setup) |
| To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder. | p. 4 (3.1. Framework of AT-VLA) |
| The tactile encoder is a lightweight module composed of several MLP layers, designed to ensure fast inference while efficiently processing tactile signals. | p. 4 (3.1. Framework of AT-VLA) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the ...
- **p. 5 / 4.1. Setup - extractive body cue:** Failure to do so may cause the zipper to get stuck or jammed. b).
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their core ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing modalities ...
- **p. 8 / 5. Conclusion - extractive body cue:** Future work may explore scaling this framework to more complex tasks and diverse real-world environments, further advancing general-purpose embodied intelligence.
- **p. 5 / 4.1. Setup - extractive body cue:** Insufficient compliance could result in collisions with the neck of the vase. d).

- **PDF anchors reviewed:** datasets p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup), p. 5 (4.1. Setup), metrics p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.2. Contact-rich Task Evaluation), p. 5 (4.2. Contact-rich Task Evaluation), p. 4 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
