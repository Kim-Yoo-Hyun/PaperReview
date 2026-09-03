# Evaluation - DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2603.00926v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (IV. EXPERIMENTS)): Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized diffusion-based action models tailored for arm ...

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Simulated Evaluations We first evaluate our method using the SIMPLER simulation [14], a suite of open-source simulated environments designed to mirror common real-world robot manipulation ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our real-world dataset is collected under diverse object placements and lighting conditions.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Furthermore, we fine-tune our DAM-VLA model on both simulated and real-world datasets.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For real-world evaluation, we construct a pick-and-place scenario in which a Franka robot is teleoperated to pick up a cup and place it into a ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The success rate of task completion is used as the evaluation metric for all VLA models.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Moreover, in the VA setting, our success rate markedly exceeds competitors, demonstrating DAM-VLA mitigates performance degradation in dynamic environments.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Method / Google(VA) Success Rates on Different Tasks Avg PCC MN OCD ODPA RT-1 [3] 90% 46% 35% 3% 44% RT-1-X [44] 49% 33% 29% ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized diffusion-based ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized ... | p. 1 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model achieves the highest average success rate of 71%, outperforming competing methods by a substantial margin. | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. We conduct 50 evaluation trials with randomized initial furniture placements. As shown in Table IV are the success rates of each step ... | p. 6 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Method / Google(VA) Success Rates on Different Tasks Avg PCC MN OCD ODPA RT-1 [3] 90% 46% 35% 3% 44% RT-1-X [44] 49% 33% ... | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2: We identify three distinctions between the arm movement and the gripper manipulation using the task of placing a carrot on a plate ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Simulated Evaluations We first evaluate our method using the SIMPLER simulation [14], a suite of open-source simulated environments designed to mirror common real-world robot manipulation ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our real-world dataset is collected under diverse object placements and lighting conditions.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Furthermore, we fine-tune our DAM-VLA model on both simulated and real-world datasets.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For real-world evaluation, we construct a pick-and-place scenario in which a Franka robot is teleoperated to pick up a cup and place it into a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized diffusion-based ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: We identify three distinctions between the arm movement and the gripper manipulation using the task of placing a carrot on a plate as ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. The ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Illustration of the dual-scale action weighting mech- anism. The trajectory weight highlights critical manipulation phases via asymmetrical Gaussian distributions. Within each predicted chunk, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: The entire process of the "One-Leg" assembly task in the FurnitureBench environment. Method / FurnitureBench Success Rates at Each Step 1 2 3 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. We conduct 50 evaluation trials with randomized initial furniture placements. As shown in Table IV are the success rates of each step of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: The evaluation encompasses both in-distribution and out-of-distribution scenarios. The in-distribution setting includes variations in object positions and lighting conditions consistent with the training ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulated Evaluations We first evaluate our method using the SIMPLER simulation [14], a suite of open-source simulated environments designed to mirror common real-world robot ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | Our real-world dataset is collected under diverse object placements and lighting conditions. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The success rate of task completion is used as the evaluation metric for all VLA models. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Moreover, in the VA setting, our success rate markedly exceeds competitors, demonstrating DAM-VLA mitigates performance degradation in dynamic environments. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Method / Google(VA) Success Rates on Different Tasks Avg PCC MN OCD ODPA RT-1 [3] 90% 46% 35% 3% 44% RT-1-X [44] 49% 33% ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4: Illustration of the dual-scale action weighting mech- anism. The trajectory weight highlights critical manipulation phases via asymmetrical Gaussian distributions. Within each predicted ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 2: We identify three distinctions between the arm movement and the gripper manipulation using the task of placing a carrot on a plate ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 5. We conduct 50 evaluation trials with randomized initial furniture placements. As shown in Table IV are the success rates of each step ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| For a fair comparison, we also fine-tune the OpenVLA and CogACT baselines using the identical datasets. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Our model achieves the highest average success rate of 71%, outperforming competing methods by a substantial margin. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Section IV-D provides an ablation study to analyze the contribution of each component in our framework. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Section IV-D provides an ablation study to analyze the contribution of each component in our framework. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Method / Google(VA) Success Rates on Different Tasks Avg PCC MN OCD ODPA RT-1 [3] 90% 46% 35% 3% 44% RT-1-X [44] 49% 33% ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| For the Google robot, evaluations are conducted under both Visual Matching (VM) and Variant Aggregation (VA) settings across four tasks, whereas the WidowX robot ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs ... | Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | Our model achieves the highest average success rate of 71%, outperforming competing methods by a substantial margin. | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 3 / III. METHOD - extractive body cue:** The action space at = [δx, δθ, sgrip] corresponds to the gripper with 7 degrees of freedom (DoF), where δx represents the relative translation offsets ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 6: The evaluation encompasses both in-distribution and out-of-distribution scenarios. The in-distribution setting includes variations in object positions and lighting conditions consistent with the ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Additionally, both models receive random noise nrand as input to facilitate the diffusion process. | p. 4 (III. METHOD) |
| body limitation/failure cue | Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model ... | p. 4 (III. METHOD) |
| body limitation/failure cue | To assess robustness, we divide the evaluation into in-distribution and out-ofdistribution scenarios, as illustrated in Figure 6. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The fine-tuning process adopts the same hyperparameters as pre-training: a learning rate of 2 × 10-5 and a batch size of 256, utilizing 8 ... | p. 5 (IV. EXPERIMENTS) |
| Our VLA model is trained using a constant learning rate of 2 × 10-5 and a batch size of 256 on 8 NVIDIA H100 ... | p. 5 (IV. EXPERIMENTS) |
| We conduct 50 evaluation trials with randomized initial furniture placements. | p. 6 (IV. EXPERIMENTS) |
| Notably, we follow CogACT [12] in determining the number of trials conducted in SIMPLER. | p. 6 (IV. EXPERIMENTS) |
| In Figure 3, the architecture of DAM-VLA is shown to consist of three key components: 1) A vision-language model, that encodes information from observation ... | p. 3 (III. METHOD) |
| The corresponding hyperparameters w1, w2, and w3 are set to 1.0, 1.0, and 0.0001, respectively. | p. 4 (III. METHOD) |
| The total loss is computed as a weighted sum of the movement loss, the manipulation loss, and the classification loss. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: The evaluation encompasses both in-distribution and out-of-distribution scenarios. The in-distribution setting includes variations in object positions and lighting conditions consistent with the training ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. The ...
- **p. 4 / III. METHOD - extractive body cue:** Additionally, both models receive random noise nrand as input to facilitate the diffusion process.
- **p. 4 / III. METHOD - extractive body cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To assess robustness, we divide the evaluation into in-distribution and out-ofdistribution scenarios, as illustrated in Figure 6.

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
