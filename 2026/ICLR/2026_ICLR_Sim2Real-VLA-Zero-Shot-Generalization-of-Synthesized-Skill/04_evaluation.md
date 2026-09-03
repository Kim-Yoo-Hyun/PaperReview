# Evaluation - Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H4SyKHjd4c; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247063. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 24 (Figure/Table caption), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 23 (Figure/Table caption)): Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 illustrates the generalization ability of Sim2Real-VLA ...

## Evaluation Body Digest

- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Given either an egocentric video of a human manipulating objects or teleoperated demonstrations performed in the real environment, we project both the actions and object ...
- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Each detected object is then matched to its corresponding "digital cousin"-a visually and functionally similar asset from our simulation dataset.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions.
- **p. 18 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Task: {task_description} Target object list: {object_list} Instructions:
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Regarding visual observation masking, the mask prediction module utilizes a standard CNN-based architecture to process raw visual inputs and yield stable object masks.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 illustrates ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at 5 ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9: Analysis of Training Dynamics and Efficiency. (a-b) Training curves of Sim2Real VLA under different data strategies. The Sim-then-Real (10 eps) strategy yields the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A DETAILS OF SETTING AND IMPLEMENTATION FOR SIM2REAL-VLA (p. 16); A.8 REAL-WORLD EXPERIMENT SETUP (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at ... | p. 24 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 9: Analysis of Training Dynamics and Efficiency. (a-b) Training curves of Sim2Real VLA under different data strategies. The Sim-then-Real (10 eps) strategy yields ... | p. 25 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 9: Success Rates with Few-Shot Real Data. Comparison across Sim Only, Real Only (10 demos), and Sim-then-Real (5/10 demos) strategies. Note the non-monotonic ... | p. 24 (Figure/Table caption) |
| A.1 MODEL ARCHITECTURE & KEY PARAMETERS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Empirical evaluations demonstrate that this binding strategy significantly outperforms alternative architectures. | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |

## Dataset / Benchmark Role

- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Given either an egocentric video of a human manipulating objects or teleoperated demonstrations performed in the real environment, we project both the actions and object ...
- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Each detected object is then matched to its corresponding "digital cousin"-a visually and functionally similar asset from our simulation dataset.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions.
- **p. 18 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** Task: {task_description} Target object list: {object_list} Instructions:
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Regarding visual observation masking, the mask prediction module utilizes a standard CNN-based architecture to process raw visual inputs and yield stable object masks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The pipeline of our Sim2Real-VLA model consists of two main components: a planning system ( Section 4.1) that enables embodied reasoning through a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: The set of DR features for characterizing the Sim2Real generalization gap in robotic manipulation tasks (Xie et al., 2024). Level Domain Randomization (DR) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: An example of the DR flow (left three images) and the chain of affordances (right three images) generated in the simulated environment for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: An example of our data generation pipeline, which projects scenes and action trajectories from heterogeneous sources (videos or teleoperation) into the simulated environment, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Task descriptions with decomposed action steps and arm type. Task Steps Arm Type Single-Arm Water Pour (1) Grasp bottle →(2) Move bottle to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Robotic manipulation performance (mean ± 95% confidence interval) across different long horizon tasks. Tasks Singe-Arm Water Pouring (200) Dual-Arm Water Pouring (250) Table ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 illustrates ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Number of successful/total trials across different manipulation tasks and domain gaps. Task / Domain Gap Original

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Given either an egocentric video of a human manipulating objects or teleoperated demonstrations performed in the real environment, we project both the actions and ... | embodiment, simulator version and control stack | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| Task/environment | Each detected object is then matched to its corresponding "digital cousin"-a visually and functionally similar asset from our simulation dataset. | reset, timeout, object/scene variation | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 9: Analysis of Training Dynamics and Efficiency. (a-b) Training curves of Sim2Real VLA under different data strategies. The Sim-then-Real (10 eps) strategy yields ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| Table 8: Comparison between the joint-learning baseline and the proposed arm-decoupling design on two manipulation tasks. We report success rates in simulation and the ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Table 9: Success Rates with Few-Shot Real Data. Comparison across Sim Only, Real Only (10 demos), and Sim-then-Real (5/10 demos) strategies. Note the non-monotonic ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| In such cases, the reward function can be interpreted as R(s, a) = 1 if the robot successfully completes the task, and R(s, a) ... | definition/direction/unit from same section | p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |
| Table 10: Mean IoU between segmentation outputs across six tasks. "real vs. sim" compares masks predicted on real vs. simulated images under matched robot ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| When more detailed or nuanced reward structures are needed, AI agents can design sophisticated reward functions (Ma et al., 2024a). | definition/direction/unit from same section | p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 9: Success Rates with Few-Shot Real Data. Comparison across Sim Only, Real Only (10 demos), and Sim-then-Real (5/10 demos) strategies. Note the non-monotonic ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Figure 5: Visualization of attention maps and relevant robot motions during robotic manipulation. Figure 5 visualizes the attention maps of Sim2Real-VLA's action transformer blocks ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 8: Comparison between the joint-learning baseline and the proposed arm-decoupling design on two manipulation tasks. We report success rates in simulation and the ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Empirical evaluations demonstrate that this binding strategy significantly outperforms alternative architectures. | comparison identity and matched condition | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Figure 9: Analysis of Training Dynamics and Efficiency. (a-b) Training curves of Sim2Real VLA under different data strategies. The Sim-then-Real (10 eps) strategy yields ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: The pipeline of our Sim2Real-VLA model consists of two main components: a planning system ( Section 4.1) that enables embodied reasoning through ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 5: Visualization of attention maps and relevant robot motions during robotic manipulation. Figure 5 visualizes the attention maps of Sim2Real-VLA's action transformer blocks ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| These refined action chunks are tokenized by a pretrained FAST tokenizer and embedded. | component/input/data sensitivity | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| A pretrained validation model is also needed in affordance chain inferrence. | component/input/data sensitivity | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| These functions are crucial for reinforcement learning (RL), particularly following Supervised Fine-Tuning (SFT) of VLA models. | component/input/data sensitivity | p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture. | Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 24 (Figure/Table caption), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 23 (Figure/Table caption) |
| Primary metric/result | Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at ... | numeric claim only at cited anchor | p. 24 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** For the training protocol, we implement a cosine-annealing learning rate schedule with a maximum value of 1e-5 across 40,000 epochs, incorporating exponential moving average (EMA) ...
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** The training configuration utilizes a batch size of 8, requiring approximately 36 GPU hours to complete under these specified conditions.
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** For the training protocol, we implement a cosine-annealing learning rate schedule with a maximum value of 1e-5 across 40,000 epochs, incorporating exponential moving average (EMA) ...
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** The training configuration utilizes a batch size of 8, requiring approximately 36 GPU hours to complete under these specified conditions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For unsuccessful trials where the robot fails to complete the task, we report the predefined maximum step limit as an upper bound. | p. 8 (1 INTRODUCTION) |
| body limitation/failure cue | However, in cases where three-view images capture only partial scene information (e.g., occluded object surfaces), or when the retrieved scene fails to semantically align ... | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| body limitation/failure cue | Besides, we also experiment Sim2Real-VLA robustness to the combination of these gaps. | p. 8 (1 INTRODUCTION) |
| body limitation/failure cue | These results indicate that the model maintains stable performance and demonstrates strong robustness to real-world differences. | p. 9 (1 INTRODUCTION) |
| body limitation/failure cue | These findings point toward a promising paradigm shift: building robotic foundation models that are trained entirely in simulation, yet are robust to realistic deployment. | p. 10 (1 INTRODUCTION) |
| body limitation/failure cue | Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions. | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training configuration utilizes a batch size of 8, requiring approximately 36 GPU hours to complete under these specified conditions. | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| For the training protocol, we implement a cosine-annealing learning rate schedule with a maximum value of 1e-5 across 40,000 epochs, incorporating exponential moving average ... | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Regarding the model architecture, we employ DiNOv2 as the visual encoder and T5-XXL as the language encoder. | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions. | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 1 INTRODUCTION - extractive body cue:** For unsuccessful trials where the robot fails to complete the task, we report the predefined maximum step limit as an upper bound.
- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** However, in cases where three-view images capture only partial scene information (e.g., occluded object surfaces), or when the retrieved scene fails to semantically align with ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Besides, we also experiment Sim2Real-VLA robustness to the combination of these gaps.
- **p. 9 / 1 INTRODUCTION - extractive body cue:** These results indicate that the model maintains stable performance and demonstrates strong robustness to real-world differences.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** These findings point toward a promising paradigm shift: building robotic foundation models that are trained entirely in simulation, yet are robust to realistic deployment.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions.

- **Evidence anchors reviewed:** datasets p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 18 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), metrics p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 23 (Figure/Table caption), p. 24 (Figure/Table caption), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), baselines p. 24 (Figure/Table caption), p. 9 (Figure/Table caption), p. 23 (Figure/Table caption), p. 24 (Figure/Table caption), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 25 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 24 (Figure/Table caption), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 23 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
