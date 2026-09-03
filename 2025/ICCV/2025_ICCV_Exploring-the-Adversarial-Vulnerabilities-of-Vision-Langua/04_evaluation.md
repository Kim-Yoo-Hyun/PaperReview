# Evaluation - Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Main Result), p. 8 (4.3. Main Result), p. 8 (4.4. Diagnostic Experiment), p. 6 (4.2. Experiment Setup), p. 5 (4.1. Implementation Details), p. 5 (4. Experiments)): Specifically, while attacking DoF1 and DoF1∼3 in the Simulation setup, UADA and UPA achieve NAD of 21.0% and 14.5%, significantly outperforming UMA scenarios with increments of 6.9% and 3.1%, respectively.

## Evaluation Body Digest

- **p. 6 / 4.3. Main Result - extractive body cue:** The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger action discrepancies within ...
- **p. 6 / 4.2. Experiment Setup - extractive body cue:** BridgeData V2 [69] is a real-world dataset comprising 24 diverse environments and 13 distinct skills, such as grasping, placing, and object rearrangement, with a total ...
- **p. 7 / 4.3. Main Result - extractive body cue:** These findings underscore a pressing security concern during the deployment of generalist robots, especially when considering application scenes that require reliable operations [11, 68].
- **p. 8 / 4.3. Main Result - extractive body cue:** Crucially, we observed that the induced erratic movements (similar to simulation scenario) of the robot during successful attacks pose significant risks to human safety and ...
- **p. 5 / 4.1. Implementation Details - extractive body cue:** 1: Input: X: dataset; δ: patch; Lo: attack objective; F: VLA model; T (·): transformations; φ, ψ: transformation parameters; T: attack steps; k: inner-loop steps.
- **p. 7 / 4.3. Main Result - extractive body cue:** This observation underscores the importance of task-specific considerations when designing adversarial attacks on robotic systems.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** To improve the robustness of our attack under real-world scenarios, we employ random geometric transformations T  (·), (shx, shy, θ)  in line 6 ...
- **p. 8 / 4.6. Systemic Discussion - extractive body cue:** Sematic-rich patches. noteworthy observation is that some of these patches bear a striking resemblance to the structural joints of a robotic arm.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 4); 4.1. Implementation Details (p. 5); 4.2. Experiment Setup (p. 6); 4.3. Main Result (p. 6); 4.4. Diagnostic Experiment (p. 8); 4.5. Robustness Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Main Result | EMPIRICAL / REAL-ROBOT OR HARDWARE | Specifically, while attacking DoF1 and DoF1∼3 in the Simulation setup, UADA and UPA achieve NAD of 21.0% and 14.5%, significantly outperforming UMA scenarios with ... | p. 6 (4.3. Main Result) |
| 4.3. Main Result | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as ... | p. 8 (4.3. Main Result) |
| 4.4. Diagnostic Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that NAD first improves when inner-loop steps continue to increase. | p. 8 (4.4. Diagnostic Experiment) |
| 4.2. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, building on the concept of Success Rate (SR) introduced in LIBERO [44], we adopt Failure Rate (FR), defined as 1-SR, as the primary ... | p. 6 (4.2. Experiment Setup) |
| 4.1. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | To improve the robustness of our attack under real-world scenarios, we employ random geometric transformations T  (·), (shx, shy, θ)  in line ... | p. 5 (4.1. Implementation Details) |

## Dataset / Benchmark Role

- **p. 6 / 4.3. Main Result - extractive body cue:** The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger action discrepancies within ...
- **p. 6 / 4.2. Experiment Setup - extractive body cue:** BridgeData V2 [69] is a real-world dataset comprising 24 diverse environments and 13 distinct skills, such as grasping, placing, and object rearrangement, with a total ...
- **p. 7 / 4.3. Main Result - extractive body cue:** These findings underscore a pressing security concern during the deployment of generalist robots, especially when considering application scenes that require reliable operations [11, 68].
- **p. 8 / 4.3. Main Result - extractive body cue:** Crucially, we observed that the induced erratic movements (similar to simulation scenario) of the robot during successful attacks pose significant risks to human safety and ...
- **p. 5 / 4.1. Implementation Details - extractive body cue:** 1: Input: X: dataset; δ: patch; Lo: attack objective; F: VLA model; T (·): transformations; φ, ψ: transformation parameters; T: attack steps; k: inner-loop steps.
- **p. 7 / 4.3. Main Result - extractive body cue:** This observation underscores the importance of task-specific considerations when designing adversarial attacks on robotic systems.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** To improve the robustness of our attack under real-world scenarios, we employ random geometric transformations T  (·), (shx, shy, θ)  in line 6 ...
- **p. 8 / 4.6. Systemic Discussion - extractive body cue:** Sematic-rich patches. noteworthy observation is that some of these patches bear a striking resemblance to the structural joints of a robotic arm.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall Adversarial Framework. The robot captures an input image, processes it through a vision-language model to generate tokens representing actions, and then uses ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative Results of adversarial vulnerabilities over OpenVLA-7B [34] and OpenVLA-7B-LIBERO [34] with objectives of UADA, UPA, and TMA, respectively. We visualize the overall ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Untargeted Results. We report FR and NAD in LIBERO simulation. ∗denotes the in-domain victim model and dataset aligned with the patch generation model ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Targeted Manipulation Attack Results. Failure Rate (FR, ↑) and its standard deviation across tasks within LIBERO [44] suite are reported. The performance of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative Results of the physical world. The first/sec- ond row show benign and adversarial cases respectively. Real-world Performance. In addition to the digital ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Impact of Inner-loop, Patch Size and Defense Discussion. The figure shows how varying Inner-loop affects NAD in UADA, and patch sizes affect L1 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Patch Visualization. Sematic-rich patches. noteworthy observation is that some of these patches bear a striking resemblance to the structural joints of a robotic ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger action discrepancies ... | embodiment, simulator version and control stack | p. 6 (4.3. Main Result), p. 6 (4.2. Experiment Setup) |
| Task/environment | BridgeData V2 [69] is a real-world dataset comprising 24 diverse environments and 13 distinct skills, such as grasping, placing, and object rearrangement, with a ... | reset, timeout, object/scene variation | p. 6 (4.2. Experiment Setup), p. 7 (4.3. Main Result) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as ... | definition/direction/unit from same section | p. 8 (4.3. Main Result) |
| Figure 5. Impact of Inner-loop, Patch Size and Defense Discussion. The figure shows how varying Inner-loop affects NAD in UADA, and patch sizes affect ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Furthermore, building on the concept of Success Rate (SR) introduced in LIBERO [44], we adopt Failure Rate (FR), defined as 1-SR, as the primary ... | definition/direction/unit from same section | p. 6 (4.2. Experiment Setup) |
| Figure 2. Overall Adversarial Framework. The robot captures an input image, processes it through a vision-language model to generate tokens representing actions, and then ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Subsequently, we evaluate the performance of generated adversarial patches on victim models (i.e., OpenVLA LIBERO variants) trained on different tasks suites to rigorously prove ... | definition/direction/unit from same section | p. 6 (4.2. Experiment Setup) |
| This observation underscores the importance of task-specific considerations when designing adversarial attacks on robotic systems. | definition/direction/unit from same section | p. 7 (4.3. Main Result) |
| These findings underscore a pressing security concern during the deployment of generalist robots, especially when considering application scenes that require reliable operations [11, 68]. | definition/direction/unit from same section | p. 7 (4.3. Main Result) |
| We incorporate two key modifications to enhance the training stability of the generated patch. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, we adapt prior work in adversarial learning as one of our baseline methods [66]. | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| We generate random noise patches as an additional baseline, representing an unstructured intervention without any learned adversarial intent. | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| In this section, we first detail the implementation of our adversarial framework and baseline methods in §4.1. | comparison identity and matched condition | p. 4 (4. Experiments) |
| The observed trend suggests larger patches give adversaries more optimization space to influence the model, aligning with prior work [12, 81]. | comparison identity and matched condition | p. 8 (4.4. Diagnostic Experiment) |
| Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as ... | comparison identity and matched condition | p. 8 (4.3. Main Result) |
| Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Subsequently, we evaluate the performance of generated adversarial patches on victim models (i.e., OpenVLA LIBERO variants) trained on different tasks suites to rigorously prove ... | component/input/data sensitivity | p. 6 (4.2. Experiment Setup) |
| To evaluate the effectiveness of our methods, we craft adversarial patches using three distinct generating setups: Simulation Setting involves a model trained in a ... | component/input/data sensitivity | p. 6 (4.2. Experiment Setup) |
| Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as ... | component/input/data sensitivity | p. 8 (4.3. Main Result) |
| (a) Impact of Inner-loop, (b) Impact of Patch Size and (c-f) the effect of four different defenses on failure rates. generated with UADA demonstrated ... | component/input/data sensitivity | p. 8 (4.3. Main Result) |
| We then conduct diagnostic experiments (§4.4) to analyze the impact of key components. | component/input/data sensitivity | p. 5 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom. | Specifically, while attacking DoF1 and DoF1∼3 in the Simulation setup, UADA and UPA achieve NAD of 21.0% and 14.5%, significantly outperforming UMA scenarios with ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Main Result), p. 8 (4.3. Main Result), p. 8 (4.4. Diagnostic Experiment), p. 6 (4.2. Experiment Setup), p. 5 (4.1. Implementation Details), p. 5 (4. Experiments) |
| Primary metric/result | Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as ... | numeric claim only at cited anchor | p. 8 (4.3. Main Result) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Experiment Setup - extractive body cue:** BridgeData V2 [69] is a real-world dataset comprising 24 diverse environments and 13 distinct skills, such as grasping, placing, and object rearrangement, with a total ...
- **p. 6 / 4.2. Experiment Setup - extractive body cue:** Each suite consists of 10 tasks, with each task executed for 50 trials, resulting in a total of 500 rollouts, following Kim et al.
- **p. 7 / 4.3. Main Result - extractive body cue:** Victim Model Objective Action(s) NAD(%) Spatial△ Object△ Goal△ Long∗ Avg Benign - - 15.3±10.2% 11.6±10.0% 20.8±12.0% 46.3±18.6% 23.5% Random Noise 28.8±24.2% 14.8±7.9% 21.0±15.5% 48.4±14.8% 28.3% ...
- **p. 7 / 4.3. Main Result - extractive body cue:** Victim Model Objective Action(s) NAD(%) Spatial△ Object△ Goal△ Long△ Avg Benign - - 15.3±10.2% 11.6±10.0% 20.8±12.0% 46.3±18.6% 23.5% Random Noise 28.8±24.2% 14.8±7.9% 21.0±15.5% 48.4±14.8% 28.3% ...
- **p. 7 / 4.3. Main Result - extractive body cue:** The evaluation encompassed 100 trials across three distinct tasks: object grasping, placement, and manipulation.
- **p. 3 / 3.1. Preliminary - extractive body cue:** In this work, we focus on a 7 degree-of-freedoms (DoFs) robotic arm [23].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively. | p. 6 (4.3. Main Result) |
| body limitation/failure cue | For UADA and UPA, our methods effectively amplify action discrepancies, leading to a notable transfer attack ability in increasing failure rates (see Tab. | p. 6 (4.3. Main Result) |
| body limitation/failure cue | Failure Rate (FR, ↑) and its standard deviation across tasks within LIBERO [44] suite are reported. | p. 7 (4.3. Main Result) |
| body limitation/failure cue | This failure can be attributed to the fact that DoF4 controls the orientation along the x-axis, which can be redundant DoF in tasks. | p. 7 (4.3. Main Result) |
| body limitation/failure cue | The figure shows how varying Inner-loop affects NAD in UADA, and patch sizes affect L1 distance and the failure rates in TMA, both targeting ... | p. 8 (4.3. Main Result) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this section, we first detail the implementation of our adversarial framework and baseline methods in §4.1. | p. 4 (4. Experiments) |
| The implementation of our adversarial patch attack pipeline is detailed in Algorithm 1. | p. 5 (4.1. Implementation Details) |
| 1: Input: X: dataset; δ: patch; Lo: attack objective; F: VLA model; T (·): transformations; φ, ψ: transformation parameters; T: attack steps; k: inner-loop ... | p. 5 (4.1. Implementation Details) |
| Each suite consists of 10 tasks, with each task executed for 50 trials, resulting in a total of 500 rollouts, following Kim et al. | p. 6 (4.2. Experiment Setup) |
| Regarding the task execution evaluation, we take the maximum steps of each task suite in the LIBERO training dataset as the timeout failure condition ... | p. 6 (4.2. Experiment Setup) |
| The evaluation encompassed 100 trials across three distinct tasks: object grasping, placement, and manipulation. | p. 7 (4.3. Main Result) |
| We attribute this phenomenon to the efficacy of the adversarial patch in perturbing the model's spatial perception, inducing a consistent deviation from the intended ... | p. 7 (4.3. Main Result) |
| We discuss the impact of inner-loop steps to model performance in Fig. | p. 8 (4.4. Diagnostic Experiment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ...
- **p. 6 / 4.3. Main Result - extractive body cue:** Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively.
- **p. 6 / 4.3. Main Result - extractive body cue:** For UADA and UPA, our methods effectively amplify action discrepancies, leading to a notable transfer attack ability in increasing failure rates (see Tab.
- **p. 7 / 4.3. Main Result - extractive body cue:** Failure Rate (FR, ↑) and its standard deviation across tasks within LIBERO [44] suite are reported.
- **p. 7 / 4.3. Main Result - extractive body cue:** This failure can be attributed to the fact that DoF4 controls the orientation along the x-axis, which can be redundant DoF in tasks.
- **p. 8 / 4.3. Main Result - extractive body cue:** The figure shows how varying Inner-loop affects NAD in UADA, and patch sizes affect L1 distance and the failure rates in TMA, both targeting at ...

- **Evidence anchors reviewed:** datasets p. 6 (4.3. Main Result), p. 6 (4.2. Experiment Setup), p. 7 (4.3. Main Result), p. 8 (4.3. Main Result), p. 5 (4.1. Implementation Details), p. 7 (4.3. Main Result), metrics p. 8 (4.3. Main Result), p. 8 (Figure/Table caption), p. 6 (4.2. Experiment Setup), p. 3 (Figure/Table caption), p. 6 (4.2. Experiment Setup), p. 7 (4.3. Main Result), baselines p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 4 (4. Experiments), p. 8 (4.4. Diagnostic Experiment), p. 8 (4.3. Main Result), p. 1 (Figure/Table caption), results p. 6 (4.3. Main Result), p. 8 (4.3. Main Result), p. 8 (4.4. Diagnostic Experiment), p. 6 (4.2. Experiment Setup), p. 5 (4.1. Implementation Details), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
