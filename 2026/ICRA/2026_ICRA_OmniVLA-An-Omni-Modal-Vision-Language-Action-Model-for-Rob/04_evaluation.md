# Evaluation - OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2509.19480. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 3 (Dataset), p. 3 (Dataset)): Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language instructions out of the box ...

## Evaluation Body Digest

- **p. 3 / Dataset - extractive PDF cue:** Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and addressing the relative ...
- **p. 3 / Dataset - extractive PDF cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** We begin by describing our setup for evaluating omnimodal navigation on our real-world robot platforms.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** We also selected 17 environments where obstacles were placed between the robot's start and the target, making the tasks more challenging and testing the core ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language ...
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** NoMaD [9]: For 2D goal pose-conditioned navigation, we run the NoMaD policy in exploration mode to generate 30 candidate trajectories.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Network architectures for multi-modal vision-based navigation. Our design builds on existing large VLA checkpoints, adding a visual backbone and a projector to condition ...
- **p. 3 / Dataset - extractive PDF cue:** 2 illustrates the network architecture, built on top of OpenVLA [3], a 7B-parameter VLA model.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** Dataset (p. 3); IV. EXPERIMENTAL SETUP (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural ... | p. 7 (Figure/Table caption) |
| Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | Naturally, we get coverage over all modalities and datasets while using this dropout mechanism to improve training stability. | p. 3 (Dataset) |
| Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | Training on these mixed-modality batches encourages the model to better represent goal information, yielding improved representations for generalization and fine-tuning. | p. 3 (Dataset) |

## Dataset / Benchmark Role

- **p. 3 / Dataset - extractive PDF cue:** Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and addressing the relative ...
- **p. 3 / Dataset - extractive PDF cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** We begin by describing our setup for evaluating omnimodal navigation on our real-world robot platforms.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** We also selected 17 environments where obstacles were placed between the robot's start and the target, making the tasks more challenging and testing the core ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We train a highly generalizable vision-based navigation policy with flexible conditioning, leveraging over 9,500 hours of data collected across 10 different platforms. Our ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Network architectures for multi-modal vision-based navigation. Our design builds on existing large VLA checkpoints, adding a visual backbone and a projector to condition ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Overview of the robotic platforms in our evaluation. Our local PC with an NVIDIA RTX 4090 receives front-camera images and pose signals, and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualization of goal pose- and language-conditioned navigation rollouts. Conditioned on OOD language and a goal pose, our policy can perform complex, long-horizon navigation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 7: Network architecture of OmniVLA-edge based on the vision-based navigation policies. other datasets, BDD-V is larger and covers more diverse environments. However, directly using ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and addressing the ... | embodiment, simulator version and control stack | p. 3 (Dataset), p. 3 (Dataset) |
| Task/environment | Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot ... | reset, timeout, object/scene variation | p. 3 (Dataset), p. 4 (IV. EXPERIMENTAL SETUP) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (Method), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| NoMaD [9]: For 2D goal pose-conditioned navigation, we run the NoMaD policy in exploration mode to generate 30 candidate trajectories. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTAL SETUP) |
| Fig. 2: Network architectures for multi-modal vision-based navigation. Our design builds on existing large VLA checkpoints, adding a visual backbone and a projector to ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| 2 illustrates the network architecture, built on top of OpenVLA [3], a 7B-parameter VLA model. | definition/direction/unit from same section | p. 3 (Dataset) |
| While large datasets enable generalization, large-scale data collection efforts can result in more noise and therefore, be less accurate. | definition/direction/unit from same section | p. 3 (Dataset) |
| The other training settings, such as learning rate, language tokenization, normalization, and so on, are the same as the default setting in the original ... | definition/direction/unit from same section | p. 4 (Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conduct extensive real-world evaluations and compare against state-of-the-art specialist and generalist baselines. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTAL SETUP) |
| Below, we describe two baselines that differ slightly from their original implementations. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTAL SETUP) |
| Following prior work for manipulation VLAs [23], we use a form of random dropout to train on all available modalities, resulting in a more ... | comparison identity and matched condition | p. 3 (Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Training on these mixed-modality batches encourages the model to better represent goal information, yielding improved representations for generalization and fine-tuning. | component/input/data sensitivity | p. 3 (Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to ... | Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 3 (Dataset), p. 3 (Dataset) |
| Primary metric/result | Naturally, we get coverage over all modalities and datasets while using this dropout mechanism to improve training stability. | numeric claim only at cited anchor | p. 3 (Dataset) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive PDF cue:** Our training mixture consists of 9,500 hours across 10 different platforms, including humancollected data, and covers a diverse set of environments.
- **p. 3 / Dataset - extractive PDF cue:** This data is comprised of 13 publicly available datasets and contains 9,500 hours across 10 different embodiments.
- **p. 4 / Dataset - extractive PDF cue:** at 3 Hz, corresponding to 2.4 seconds for all models.
- **p. 4 / Dataset - extractive PDF cue:** In training OmniVLA with OpenVLA checkpoints on eight H100 GPUs, we use a per-GPU batch size of 7 and accumulate gradients for 4 steps, yielding ...
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** The goals were placed 5-30 meters from the robot's initial position.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** Egocentric goal image-conditioned navigation: With egocentric goal images, our policy is tasked with navigating the robot to target locations up to 3 meters away.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot ... | p. 3 (Dataset) |
| body limitation/failure cue | Since we cannot secure a sufficiently large batch size for some models even on a server with multiple GPUs, we accumulate the gradient for ... | p. 4 (Dataset) |
| body limitation/failure cue | However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires | p. 5 (V. EVALUATING OMNI-MODAL NAVIGATION) |
| body limitation/failure cue | The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity. | p. 6 (V. EVALUATING OMNI-MODAL NAVIGATION) |
| body limitation/failure cue | While large datasets enable generalization, large-scale data collection efforts can result in more noise and therefore, be less accurate. | p. 3 (Dataset) |
| body limitation/failure cue | To assess the benefit of large pre-trained models, we introduced out-of-distribution (OOD) language prompts that go beyond the instructions present in the training data. | p. 4 (IV. EXPERIMENTAL SETUP) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In training OmniVLA with OpenVLA checkpoints on eight H100 GPUs, we use a per-GPU batch size of 7 and accumulate gradients for 4 steps, ... | p. 4 (Dataset) |
| For LeLaN, CounterfactualVLA, ViNT, MBRA-pose, and MBRA-image, we use the authors' original implementation and checkpoints for evaluation. | p. 4 (IV. EXPERIMENTAL SETUP) |
| We process the robot's current visual observations using a visual encoder. | p. 3 (Dataset) |
| We modify this to add multiple goal encoders and perform modality dropout in the same way as our base model (see Appendix A). | p. 3 (Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Dataset - extractive PDF cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / Dataset - extractive PDF cue:** Since we cannot secure a sufficiently large batch size for some models even on a server with multiple GPUs, we accumulate the gradient for several ...
- **p. 5 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive PDF cue:** However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires
- **p. 6 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive PDF cue:** The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity.
- **p. 3 / Dataset - extractive PDF cue:** While large datasets enable generalization, large-scale data collection efforts can result in more noise and therefore, be less accurate.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** To assess the benefit of large pre-trained models, we introduced out-of-distribution (OOD) language prompts that go beyond the instructions present in the training data.

- **PDF anchors reviewed:** datasets p. 3 (Dataset), p. 3 (Dataset), p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), metrics p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption), p. 3 (Dataset), p. 3 (Dataset), p. 4 (Dataset), baselines p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 3 (Dataset), results p. 7 (Figure/Table caption), p. 3 (Dataset), p. 3 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
