# Evaluation - Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS)): However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the metric of success rate, surpassing the ...

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The real-world robot platform with a Franka Emika Panda robot, a Robotiq 2F-85 gripper and multiple RealSense D435i RGB-D cameras. patterns.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Real Robot Evaluation 1) Setup: We evaluate OC-VLA on a real-world Franka Robot setup, which comprises a 7-DoF tabletop Franka Emika Panda robot arm equipped ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For model finetuning, we fine-tune the model pretrained on the Droid dataset, using either end effector actions defined in the third-person camera coordinate or those ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Method Avg Task1 Task2 Task3 Task4 Task5 Task6 Task7 Task8 Robot Base(Fixed Camera, From Table II) 66.3% 70.0% 70.0% 90.0% 60.0% 60.0% 60.0% 60.0% 60.0% ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** ROBOT BASE AND CAMERA BASE INDICATES THE MODEL WE BUILT IN ROBOT BASE COORDINATES AND THIRD-PERSON CAMERA BASE COORDINATE FOLLOWING DITA [6], RESPECTIVELY.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each task, we conduct 10 trials and measure performance by computing the task success rate.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This evaluation benchmark is used to measure the success rate of the model across different manipulation tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that, regardless of the type of action space used, employing robot actions defined in the third-person camera coordinate frame as prediction ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This improvement is particularly pronounced in models utilizing a discrete action space, where we observe an increase in success rate of about 14%. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7. Full Pipeline of our method. We introduce OC-VLA framework, aligning the observation space and the prediction target with the camera extrinsic calibration ... | p. 11 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The real-world robot platform with a Franka Emika Panda robot, a Robotiq 2F-85 gripper and multiple RealSense D435i RGB-D cameras. patterns.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Real Robot Evaluation 1) Setup: We evaluate OC-VLA on a real-world Franka Robot setup, which comprises a 7-DoF tabletop Franka Emika Panda robot arm equipped ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For model finetuning, we fine-tune the model pretrained on the Droid dataset, using either end effector actions defined in the third-person camera coordinate or those ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Method Avg Task1 Task2 Task3 Task4 Task5 Task6 Task7 Task8 Robot Base(Fixed Camera, From Table II) 66.3% 70.0% 70.0% 90.0% 60.0% 60.0% 60.0% 60.0% 60.0% ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** ROBOT BASE AND CAMERA BASE INDICATES THE MODEL WE BUILT IN ROBOT BASE COORDINATES AND THIRD-PERSON CAMERA BASE COORDINATE FOLLOWING DITA [6], RESPECTIVELY.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA aligns ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3. Action translation between robot base coordinate and camera base coordinate. During training, actions are transformed from the robot base coordinate to the camera ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4. The real-world robot platform with a Franka Emika Panda robot, a Robotiq 2F-85 gripper and multiple RealSense D435i RGB-D cameras. patterns. This diversity ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6. Model Structure. We use the same model structure which is followed Dita to evaluate our method on both continuous action space and discrete ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7. Full Pipeline of our method. We introduce OC-VLA framework, aligning the observation space and the prediction target with the camera extrinsic calibration matrix. ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8. Visualization of the ManiSkill2 Dataset. We generate a third-view camera pool in the Simulated Environment and sample 20 cameras for each of the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Task/environment | The real-world robot platform with a Franka Emika Panda robot, a Robotiq 2F-85 gripper and multiple RealSense D435i RGB-D cameras. patterns. | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (III. METHOD), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each task, we conduct 10 trials and measure performance by computing the task success rate. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| This evaluation benchmark is used to measure the success rate of the model across different manipulation tasks. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| For models with a continuous action space, the objective is to minimize the mean squared error (MSE) between the robot's action (augmented with standard ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| As shown in the Table II, under the 10shot setting with a fixed camera viewpoint, the model finetuned using robot base coordinate actions already ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction framework. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| These models serve as baselines in our evaluation. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| The model predicts actions in the third-person camera base coordinate, while the baseline model predicts actions in the robot base coordinate. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 9. Qualitative Comparison on ManiSkill2 of OC-VLA and Baseline. OC-VLA show better performance on the grasp pose and searching for the goal point. | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| METHODS ANNOTATED WITH "(VAR)" INDICATE RESULTS OBTAINED UNDER ZERO-SHOT CAMERA EVALUATION, WHILE THOSE WITHOUT THE ANNOTATION CORRESPOND TO EVALUATIONS CONDUCTED USING THE TRAINING CAM ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For model finetuning, we fine-tune the model pretrained on the Droid dataset, using either end effector actions defined in the third-person camera coordinate or ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| As illustrated in the Figure 4, we introduce a novel, previously unseen camera mounted near Camera 1, and perform all evaluations under this new ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| METHODS ANNOTATED WITH "(VAR)" INDICATE RESULTS OBTAINED UNDER ZERO-SHOT CAMERA EVALUATION, WHILE THOSE WITHOUT THE ANNOTATION CORRESPOND TO EVALUATIONS CONDUCTED USING THE TRAINING CAM ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| For a fair performance comparison, we also fine-tune the pretrained versions of OpenVLA-OFT [2], π0 [5] on our collected datasets, using their official training ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Fig. 7. Full Pipeline of our method. We introduce OC-VLA framework, aligning the observation space and the prediction target with the camera extrinsic calibration ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| For this purpose, we choose the Droid dataset [9] for pretraining. | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions ... | However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS) |
| Primary metric/result | The results demonstrate that, regardless of the type of action space used, employing robot actions defined in the third-person camera coordinate frame as prediction ... | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The model is optimized using AdamW [61] for 30,000 steps, with learning rates of 1e -4 for both the causal Transformer and Q-Former, and 1e ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Training is conducted with a batch size of 2048 across 8 NVIDIA A100 GPUs, with 256 samples per GPU.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For closed-loop evaluation, we randomly sample 100 trajectories from the validation set for each task family, resulting in an evaluation set of 500 trajectories.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In contrast, the dataset collected with Camera 2 consists of trajectories for 8 tasks, during which we introduce slight perturbations to the camera position to ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Both models are optimized with AdamW [61] for 20,000 steps with a batch size of 512.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We fine-tune all models using 15 task demonstrations collected from Camera 1 and perform a unified evaluation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction framework. | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs to the causal transformer. | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | In this setting, the camera viewpoint remains fixed and identical throughout both the finetuning and evaluation phases. • Slight Camera Perturbations To further validate ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | To assess the model's robustness to changes in camera perspective, we conduct zero-shot evaluations using models fine-tuned with demonstrations from Camera 1. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Both models are optimized with AdamW [61] for 20,000 steps with a batch size of 512. | p. 5 (IV. EXPERIMENTS) |
| Training is conducted with a batch size of 2048 across 8 NVIDIA A100 GPUs, with 256 samples per GPU. | p. 5 (IV. EXPERIMENTS) |
| In the following, we detail the model implementations for each action space. | p. 4 (IV. EXPERIMENTS) |
| The entire transformer functions as a Diffusion Transformer (DiT) [39], which iteratively denoises the input over multiple steps to generate the final end-effector action. | p. 4 (IV. EXPERIMENTS) |
| OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera ... | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA aligns ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction framework.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs to the causal transformer.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this setting, the camera viewpoint remains fixed and identical throughout both the finetuning and evaluation phases. • Slight Camera Perturbations To further validate the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To assess the model's robustness to changes in camera perspective, we conduct zero-shot evaluations using models fine-tuned with demonstrations from Camera 1.

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 14 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), results p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. (p. 4, IV. EXPERIMENTS).
- **Metric evidence:** For each task, we conduct 10 trials and measure performance by computing the task success rate. (p. 5, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** These models serve as baselines in our evaluation. (p. 5, IV. EXPERIMENTS).
- **Failure/negative evidence:** Failures are highlighted with red circles. the same data. (p. 7, IV. EXPERIMENTS).
