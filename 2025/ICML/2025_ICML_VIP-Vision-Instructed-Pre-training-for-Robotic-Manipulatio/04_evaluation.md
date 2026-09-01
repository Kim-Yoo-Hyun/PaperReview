# Evaluation - VIP: Vision Instructed Pre-training for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ccUNMIbpcf; PDF retrieval source: https://openreview.net/pdf/fc80bd3b42c458d1d871411db0d2aec7f70c9c37.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis), p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness)): As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** A Franka Panda robotic arm is deployed in each simulation environment to manipulate objects, with four cameras strategically positioned to observe the scene from various ...
- **p. 5 / 4. Experiments - extractive PDF cue:** For the real environment, we conduct experiments using the Cobot Magic robot (Agilex, 2024).
- **p. 6 / 4. Experiments - extractive PDF cue:** 7, the three real-robot tasks include Pour Blueberries, Open the Lid, and Clean the Table.
- **p. 7 / 4.1. VIP Effectiveness - extractive PDF cue:** The success rates of these policies are boosted in both simulated and real robotic manipulation environments, indicating the value of incorporating more diverse training data.
- **p. 7 / 4. Experiments - extractive PDF cue:** VIP: Vision Instructed Pre-training for Robotic Manipulation Table 1.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** In this part, we study whether the data scaling law appears in the pre-training and fine-tuning procedures of robotic manipulation.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** Notably, to show the value of DINOv2 representation more clearly, when DINOv2 is not adopted, we replace the encoders in VIRT as ResNet18, the backbone ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate the effectiveness of our method in both real and simulated environments.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Method Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly. | p. 8 (4.3. Method Analysis) |
| 4.3. Method Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, we can find that increasing the fine-tuning data volume boosts execution success rates more significantly, which is because the fine-tuning data aligns ... | p. 8 (4.3. Method Analysis) |
| 4.1. VIP Effectiveness | EMPIRICAL / REAL-ROBOT OR HARDWARE | Comparing the various policies, it is found that VIRT achieves the best performance, and its inference speed is also promising. | p. 7 (4.1. VIP Effectiveness) |
| 4.1. VIP Effectiveness | EMPIRICAL / REAL-ROBOT OR HARDWARE | These policies are tested for 100 times on each task, and we report their success rates as well as inference speeds (test on a ... | p. 7 (4.1. VIP Effectiveness) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** A Franka Panda robotic arm is deployed in each simulation environment to manipulate objects, with four cameras strategically positioned to observe the scene from various ...
- **p. 5 / 4. Experiments - extractive PDF cue:** For the real environment, we conduct experiments using the Cobot Magic robot (Agilex, 2024).
- **p. 6 / 4. Experiments - extractive PDF cue:** 7, the three real-robot tasks include Pour Blueberries, Open the Lid, and Clean the Table.
- **p. 7 / 4.1. VIP Effectiveness - extractive PDF cue:** The success rates of these policies are boosted in both simulated and real robotic manipulation environments, indicating the value of incorporating more diverse training data.
- **p. 7 / 4. Experiments - extractive PDF cue:** VIP: Vision Instructed Pre-training for Robotic Manipulation Table 1.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** In this part, we study whether the data scaling law appears in the pre-training and fine-tuning procedures of robotic manipulation.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** Notably, to show the value of DINOv2 representation more clearly, when DINOv2 is not adopted, we replace the encoders in VIRT as ResNet18, the backbone ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate the effectiveness of our method in both real and simulated environments.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Visualization comparison between the action attention maps of the text instructed policy and vision instructed policy. We can observe that the text instructed ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall pipeline of VIP. The input to the pre-trained policy includes two image frames (the observation frame and future frame) and sparse point ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The conceptual diagram of sparse point flow. Consecu- tive frames in a video comprise numerous pixels and contain much redundant information for describing ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of different vision instructions. The three columns of images in the first and second rows show the world model input, future ground ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Illustrations of the Cobot Magic robot and how it is tele- operated. The robot has two master arms and two puppet arms. (a) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Illustrations of how we teleoperate the robot in Isaac Gym. We build a real-time hand pose acquisition system to map the human hand ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Illustrations of the three designed real-robot tasks, which include Pour Blueberries, Open the Lid, and Clean the Table. Move a Single Box Transport ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 8. Illustrations of the three designed simulated tasks, which include Move a Single Box, Transport the Specified Box, and Stack the Specified Boxes. of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A Franka Panda robotic arm is deployed in each simulation environment to manipulate objects, with four cameras strategically positioned to observe the scene from ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | For the real environment, we conduct experiments using the Cobot Magic robot (Agilex, 2024). | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These policies are tested for 100 times on each task, and we report their success rates as well as inference speeds (test on a ... | definition/direction/unit from same section | p. 7 (4.1. VIP Effectiveness) |
| The success rates of these policies are boosted in both simulated and real robotic manipulation environments, indicating the value of incorporating more diverse training ... | definition/direction/unit from same section | p. 7 (4.1. VIP Effectiveness) |
| As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly. | definition/direction/unit from same section | p. 8 (4.3. Method Analysis) |
| We replace the input to the trained policy as the images with the studied noise and then test the success rates on various evaluation ... | definition/direction/unit from same section | p. 8 (4.3. Method Analysis) |
| The distance between the thumb and index finger is employed to determine the opening or closing of the gripper. is integrated with four robot ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Illustrations of how we teleoperate the robot in Isaac Gym. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 1. Visualization comparison between the action attention maps of the text instructed policy and vision instructed policy. We can observe that the text ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 4. Visualization of different vision instructions. The three columns of images in the first and second rows show the world model input, future ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Among them, ConvMLP is the most commonly adopted baseline, which first extracts image feature using convolutional neural network (CNN) and then regresses actions based ... | comparison identity and matched condition | p. 7 (4.1. VIP Effectiveness) |
| Figure 3. The conceptual diagram of sparse point flow. Consecu- tive frames in a video comprise numerous pixels and contain much redundant information for ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Comparison among various instructions. | comparison identity and matched condition | p. 7 (4.1. VIP Effectiveness) |
| This part conducts an ablation study on the designs in VIRT that are not clearly analyzed before. | comparison identity and matched condition | p. 8 (4.3. Method Analysis) |
| Figure 1. Visualization comparison between the action attention maps of the text instructed policy and vision instructed policy. We can observe that the text ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 3. Ablation study on designs of VIRT. DINO Uncern Mask Move Box Transport Box Stack Boxes 0.80 0.58 0.49 ✓ 0.86 0.66 | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| After a series of twists, the robot gradually unscrews and removes the lid from the bottle. | component/input/data sensitivity | p. 6 (4. Experiments) |
| In the Pour Blueberries task, the robot needs to first remove the juicer cup from the juicer and place it on the table. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Without a special statement, the cropped image is obtained from YOLOv10-small (Wang et al., 2024). | component/input/data sensitivity | p. 7 (4. Experiments) |
| This part conducts an ablation study on the designs in VIRT that are not clearly analyzed before. | component/input/data sensitivity | p. 8 (4.3. Method Analysis) |
| Ramdomly masking pixels of input images forces the Transformer-based policy to maintain its sensitivity to local features. | component/input/data sensitivity | p. 8 (4.3. Method Analysis) |
| Figure 2. Overall pipeline of VIP. The input to the pre-trained policy includes two image frames (the observation frame and future frame) and sparse ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows. | As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis), p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness) |
| Primary metric/result | In addition, we can find that increasing the fine-tuning data volume boosts execution success rates more significantly, which is because the fine-tuning data aligns ... | numeric claim only at cited anchor | p. 8 (4.3. Method Analysis) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. VIP Effectiveness - extractive PDF cue:** Pre-train Inference Move Box Transport Box Stack Boxes F Cropped 0.87 0.64 0.50 S Cropped 0.78 0.51 0.36 F+S Text 0.85 0.19 0.06 F+S Future ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Robustness analysis of VIRT to different disturbances, e.g., brightness change, vision noise, and image blur. | p. 8 (4.3. Method Analysis) |
| body limitation/failure cue | For ConvMLP, its primary problem is its output head is a naive MLP, which is fast but fails to estimate actions precisely. | p. 7 (4.1. VIP Effectiveness) |
| body limitation/failure cue | This part analyzes the robustness of VIRT to different unseen environment disturbances. | p. 8 (4.3. Method Analysis) |
| body limitation/failure cue | According to the results, we can find that solely using a future image or sparse point flows does not lead to effective pre-training due ... | p. 7 (4.2. Instruction Comparison) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In VIP, the pre-trained model parameters are updated using AdamW (Loshchilov, 2017) and the learning rate is 1e-5. | p. 7 (4. Experiments) |
| In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) ... | p. 4 (3.1. Vision Intructed Pre-training) |
| F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T ... | p. 4 (3.1. Vision Intructed Pre-training) |
| The simulated environments are built based on Isaac Gym (Makoviychuk et al., 2021), which supports GPU-based efficient physics simulation. | p. 6 (4. Experiments) |
| VIP: Vision Instructed Pre-training for Robotic Manipulation Puppet Arms Right Camera Left Camera Front Camera Battery Computer Master Arms (a) The Cobot Magic Robot ... | p. 6 (4. Experiments) |
| ACT consists of a CNN backbone, encoders, and decoders. | p. 7 (4.1. VIP Effectiveness) |
| We mainly study the influences of three designs, i.e., initializing encoder weight with DINOv2, uncertainty in supervision loss, and randomly masking the input images. | p. 8 (4.3. Method Analysis) |
| Notably, to show the value of DINOv2 representation more clearly, when DINOv2 is not adopted, we replace the encoders in VIRT as ResNet18, the ... | p. 8 (4.3. Method Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** Robustness analysis of VIRT to different disturbances, e.g., brightness change, vision noise, and image blur.
- **p. 7 / 4.1. VIP Effectiveness - extractive PDF cue:** For ConvMLP, its primary problem is its output head is a naive MLP, which is fast but fails to estimate actions precisely.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** This part analyzes the robustness of VIRT to different unseen environment disturbances.
- **p. 7 / 4.2. Instruction Comparison - extractive PDF cue:** According to the results, we can find that solely using a future image or sparse point flows does not lead to effective pre-training due to ...

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 5 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. VIP Effectiveness), p. 7 (4. Experiments), p. 8 (4.3. Method Analysis), metrics p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness), p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis), p. 6 (4. Experiments), p. 6 (4. Experiments), baselines p. 7 (4.1. VIP Effectiveness), p. 4 (Figure/Table caption), p. 7 (4.1. VIP Effectiveness), p. 8 (4.3. Method Analysis), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis), p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
