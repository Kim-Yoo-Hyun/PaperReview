# Evaluation - DexterityGen: Foundation Controller for Unprecedented Dexterity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://roboticsconference.org/2026/program/papers/103/; PDF retrieval source: https://roboticsconference.org/2026/program/papers/103/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption)): 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when using it to solve certain tasks, Before ‘evaluation, ...

## Evaluation Body Digest

- **p. 7 / B. Simulated Experiments - extractive body cue:** ‘We have demonstrated that our system can provide effective assistance through simulated validation. ‘Then, we further design several tasks for benchmarking in the real world.
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows).
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** We collect a total of 1 x 10? transitions as our simulation dataset, equivalent to 31.7 years of real world experience.
- **p. 8 / B. Simulated Experiments - extractive body cue:** During the manipulation procedure, the user can still have a sense of agency over the robot hand and complete a complex task.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In this paper, we use Allegro Hand as our manipulator and we attach the Allegro Hand to a Franka-panda robot arm.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In the teleoperation experiments in real world, we use a retargeting-based system to control the robot with human hand,
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We obtain the 6D human wrist pose Via the Vive tracking system and use it to control the robot arm separately.
- **p. 8 / B. Simulated Experiments - extractive body cue:** + In-hand Regrasping We define this task as a harder version of object reorientation.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** B. Large-Scale Behavior Dataset Generation (p. 5); IV. EXPERIMENTS (p. 6); B. Simulated Experiments (p. 7); B. Implementation of Anygrasp-to-Anygrasp (p. 12); C. Boosting Dataset Diversity with Diverse Rewards (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Simulated Experiments | EMPIRICAL / SIMULATION | 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when using it ... | p. 8 (B. Simulated Experiments) |
| B. Simulated Experiments | EMPIRICAL / SIMULATION | This explains why the user can achieve a much higher success rate in these dexterous tasks. | p. 8 (B. Simulated Experiments) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | figure, DexGen can successfully improve the performance of these polici | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | duration by 10-100x and even help an extremely perturbed policy to achieve success where the baseline fails. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | In the experiments, we first validate the effectiveness of DexGen through simulated experiments, demonstrating its ability to enhance the robustness and success rate of ... | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / B. Simulated Experiments - extractive body cue:** ‘We have demonstrated that our system can provide effective assistance through simulated validation. ‘Then, we further design several tasks for benchmarking in the real world.
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows).
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** We collect a total of 1 x 10? transitions as our simulation dataset, equivalent to 31.7 years of real world experience.
- **p. 8 / B. Simulated Experiments - extractive body cue:** During the manipulation procedure, the user can still have a sense of agency over the robot hand and complete a complex task.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In this paper, we use Allegro Hand as our manipulator and we attach the Allegro Hand to a Franka-panda robot arm.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In the teleoperation experiments in real world, we use a retargeting-based system to control the robot with human hand,
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We obtain the 6D human wrist pose Via the Vive tracking system and use it to control the robot arm separately.
- **p. 8 / B. Simulated Experiments - extractive body cue:** + In-hand Regrasping We define this task as a harder version of object reorientation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce DexterityGen (DexGen) as a foundation controller that achieves unprecedented dexterous manipulation behavior with teleoperation. DexGen is a generative model that can ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Dataset: The Anygrasp-to-Anygrasp dataset generation pipeline is designed for the generative pretraining of DexGen. For a wide variety of objects, we extensively search ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows). DexGen controller learns the dataset action distribution (purple shaded area) at ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Real world experimental setup based on Allegro Hand with a Franka Panda Arm (Left). We use human teleoperation (Right) as a proxy for ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Part of our real world testing objects, which are rot present in our pretraining dataset. We include objects of different sizes, masses, and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Results of simulation evaluation. We use DexGen to correct several noi
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 9: DexGen can maximally preserve input action while cor- recting dangerous actions. DexGen can reject users' behavior (open up the palm) and keep holding ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Diffusion Model in DexGen Controller. We use a standard U-Net based diffusion model with FiLM conditioning.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ‘We have demonstrated that our system can provide effective assistance through simulated validation. ‘Then, we further design several tasks for benchmarking in the real ... | embodiment, simulator version and control stack | p. 7 (B. Simulated Experiments), p. 5 (B. Large-Scale Behavior Dataset Generation) |
| Task/environment | 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows). | reset, timeout, object/scene variation | p. 5 (B. Large-Scale Behavior Dataset Generation), p. 5 (B. Large-Scale Behavior Dataset Generation) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In the experiments, we first validate the effectiveness of DexGen through simulated experiments, demonstrating its ability to enhance the robustness and success rate of ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when using it ... | definition/direction/unit from same section | p. 8 (B. Simulated Experiments) |
| This explains why the user can achieve a much higher success rate in these dexterous tasks. | definition/direction/unit from same section | p. 8 (B. Simulated Experiments) |
| figure, DexGen can successfully improve the performance of these polici | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| In contrast, With the assistance of DexGen, we can partially recover the performance of this noisy expert. | definition/direction/unit from same section | p. 7 (B. Simulated Experiments) |
| Fig. 3: Dataset: The Anygrasp-to-Anygrasp dataset generation pipeline is designed for the generative pretraining of DexGen. For a wide variety of objects, we extensively ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Each generated grasp is defined as a tuple (hand joint position, object pose). | definition/direction/unit from same section | p. 5 (B. Large-Scale Behavior Dataset Generation) |
| We first generate a set ‘of object grasps using Grasp Analysis and Rapidly-exploring Random Tree (RRT) [31], similar to the Manipulation RRT procedure [25]. | definition/direction/unit from same section | p. 5 (B. Large-Scale Behavior Dataset Generation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the baseline, our system can successfully help the user to solve many tasks in various challenging setups. | comparison identity and matched condition | p. 8 (B. Simulated Experiments) |
| ss ¥.075.075) esueas.15) mut uo.05) wo muiuoo.r.0 ous ovaten) "Ou (# Gens) ~~ Basen Owaten) Baseline Gea) | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| duration by 10-100x and even help an extremely perturbed policy to achieve success where the baseline fails. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| We observe that humans can hardly use the baseline teleoperation system to solve the tasks above. | comparison identity and matched condition | p. 8 (B. Simulated Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We find that without our assistance, the noisy ‘expert has much more frequent failures. | component/input/data sensitivity | p. 7 (B. Simulated Experiments) |
| Fig. 3: Dataset: The Anygrasp-to-Anygrasp dataset generation pipeline is designed for the generative pretraining of DexGen. For a wide variety of objects, we extensively ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows). | component/input/data sensitivity | p. 5 (B. Large-Scale Behavior Dataset Generation) |
| To achieve this, we require a large~ scale behavior dataset to pretrain our DexGen model, ensuring ‘comprehensive coverage of the state space. | component/input/data sensitivity | p. 5 (B. Large-Scale Behavior Dataset Generation) |
| Fig. 7: Part of our real world testing objects, which are rot present in our pretraining dataset. We include objects of different sizes, masses, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| "Motivated by these observations, in this paper, we propose | 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when using it ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Primary metric/result | This explains why the user can achieve a much higher success rate in these dexterous tasks. | numeric claim only at cited anchor | p. 8 (B. Simulated Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** We collect a total of 1 x 10? transitions as our simulation dataset, equivalent to 31.7 years of real world experience.
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** Generating this dataset (by rolling out trained RL. policies) requires 300 GPU hours.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** duration by 10-100x and even help an extremely perturbed policy to achieve success where the baseline fails.
- **p. 12 / B. Implementation of Anygrasp-to-Anygrasp - extractive body cue:** 3 Noes = random([2,3,4)) 4 Point P, Normal n « SampleSurface(M, Npee)- Sif GraspAnalysis(P,n) then
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** We train these models with the AdamW optimizer (35, 29] for 15 epochs using 96 GPUs, which takes approximately 3 days.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** Here a is 4 parameter of the strength of the guidance to be tuned, which ‘we will study in experiments.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We find that without our assistance, the noisy ‘expert has much more frequent failures. | p. 7 (B. Simulated Experiments) |
| body limitation/failure cue | We record the average number of critical failures (drop the object) and the number of goal achievements within a certain time of different policies | p. 7 (B. Simulated Experiments) |
| body limitation/failure cue | We report success rate (SR) and time-to-fall (ITF) / Holding Time metric which is normalized by the test episode length. | p. 8 (B. Simulated Experiments) |
| body limitation/failure cue | The raw teleoperation baseline fails completely on those tasks, while our method can help the teleoperation policy to achieve both stability and success in ... | p. 8 (B. Simulated Experiments) |
| body limitation/failure cue | Fig. 1: We introduce DexterityGen (DexGen) as a foundation controller that achieves unprecedented dexterous manipulation behavior with teleoperation. DexGen is a generative model that ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | To enhance the robustness of our policy, we randomly adjust the wrist to different poses throughout the process, in addition to employing. commonly used ... | p. 5 (B. Large-Scale Behavior Dataset Generation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| dimension of action space is bounded by [-1, 1] and these noises ruin the expert action most of the time, We measure the average ... | p. 7 (IV. EXPERIMENTS) |
| We describe its implementation as follows, | p. 12 (B. Implementation of Anygrasp-to-Anygrasp) |
| Generating this dataset (by rolling out trained RL. policies) requires 300 GPU hours. | p. 5 (B. Large-Scale Behavior Dataset Generation) |
| The total sampling time is around 27ms (37H2) on 4 Lambda workstation equipped with an NVIDIA RTX 4090 GPU. | p. 6 (C. DexGen Model Architecture) |
| We train these models with the AdamW optimizer (35, 29] for 15 epochs using 96 GPUs, which takes approximately 3 days. | p. 6 (C. DexGen Model Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / B. Simulated Experiments - extractive body cue:** We find that without our assistance, the noisy ‘expert has much more frequent failures.
- **p. 7 / B. Simulated Experiments - extractive body cue:** We record the average number of critical failures (drop the object) and the number of goal achievements within a certain time of different policies
- **p. 8 / B. Simulated Experiments - extractive body cue:** We report success rate (SR) and time-to-fall (ITF) / Holding Time metric which is normalized by the test episode length.
- **p. 8 / B. Simulated Experiments - extractive body cue:** The raw teleoperation baseline fails completely on those tasks, while our method can help the teleoperation policy to achieve both stability and success in diverse ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce DexterityGen (DexGen) as a foundation controller that achieves unprecedented dexterous manipulation behavior with teleoperation. DexGen is a generative model that can ...
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** To enhance the robustness of our policy, we randomly adjust the wrist to different poses throughout the process, in addition to employing. commonly used domain ...

- **Evidence anchors reviewed:** datasets p. 7 (B. Simulated Experiments), p. 5 (B. Large-Scale Behavior Dataset Generation), p. 5 (B. Large-Scale Behavior Dataset Generation), p. 8 (B. Simulated Experiments), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (B. Simulated Experiments), p. 4 (Figure/Table caption), baselines p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (B. Simulated Experiments), results p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** figure, DexGen can successfully improve the performance of these polici (p. 7, IV. EXPERIMENTS).
- **Metric evidence:** In the experiments, we first validate the effectiveness of DexGen through simulated experiments, demonstrating its ability to enhance the robustness and success rate of extremely suboptimal policies. (p. 6, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** Compared to the baseline, our system can successfully help the user to solve many tasks in various challenging setups. (p. 8, B. Simulated Experiments).
- **Failure/negative evidence:** We find that without our assistance, the noisy ‘expert has much more frequent failures. (p. 7, B. Simulated Experiments).
