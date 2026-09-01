# Evaluation - ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vQFw9ryKyK; PDF retrieval source: https://openreview.net/pdf/e349d69236fa6d97f504e96881ee34405d7de516.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS)): On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods especially at success rate.

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** The HM3D dataset offers high-fidelity reconstructions of 20 entire buildings, including 80 training scenes and 20 validation scenes.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 EXPERIMENTAL SETUP AND METRICS We evaluate the effectiveness and navigation efficiency of our proposed method using the Habitat v3.0 simulator (Puig et al., 2023) ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** provides 40 high-quality synthetic scenes, comprising 110 training scenes and 40 validation scenes.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** For the data collection of the Where2Imagine module, we leveraged human demonstration trajectories from the MP3D (Chang et al., 2017) dataset within the habitat-web project ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** First, some object instances are neglected for marking by the simulator, and therefore a successfully trajectory is wrongly considered as a failure (a.k.a. false failure) ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Notably, both the success rate and SPL exhibit obvious improvements, obtaining 62.0% and 59.0% at success rate respectively on H3MD and HSSD benchmarks, which further ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** The differences between the datasets result in a certain degree of variability.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Specifically, we modified the final output layers of the ResNet18 and ViT to fit our dataset, allowing parameter updates during training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A.3 TRAINING DATASET FOR WHERE2IMAGINE (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods especially at ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Moreover, ImagineNav achieves the highest success rate and SPL on the HSSD dataset. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Further incorporating Where2Image improve success rate from 55.0 to 64.0, and from 49.0 to 56.0 under settings of ‘NVS' and ‘w/o NVS', respectively. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Notably, both the success rate and SPL exhibit obvious improvements, obtaining 62.0% and 59.0% at success rate respectively on H3MD and HSSD benchmarks, which ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | The results in Table 4 show that the ResNet-18, when trained from scratch, achieves the best performances in both relative wayopint prediction and ObjectNav ... | p. 10 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** The HM3D dataset offers high-fidelity reconstructions of 20 entire buildings, including 80 training scenes and 20 validation scenes.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 EXPERIMENTAL SETUP AND METRICS We evaluate the effectiveness and navigation efficiency of our proposed method using the Habitat v3.0 simulator (Puig et al., 2023) ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** provides 40 high-quality synthetic scenes, comprising 110 training scenes and 40 validation scenes.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** For the data collection of the Where2Imagine module, we leveraged human demonstration trajectories from the MP3D (Chang et al., 2017) dataset within the habitat-web project ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** First, some object instances are neglected for marking by the simulator, and therefore a successfully trajectory is wrongly considered as a failure (a.k.a. false failure) ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Notably, both the success rate and SPL exhibit obvious improvements, obtaining 62.0% and 59.0% at success rate respectively on H3MD and HSSD benchmarks, which further ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** The differences between the datasets result in a certain degree of variability.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Specifically, we modified the final output layers of the ResNet18 and ViT to fit our dataset, allowing parameter updates during training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The comparison between the conventional LLM-based navigation pipeline and our Imag- ineNav pipeline. The traditional LLM-based navigation framework, illustrated on the left, relies ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The overall pipeline of our mapless, open-vocabulary navigation framework. At each it- eration, the agent captures a panoramic view of its surroundings. In ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: An example of the VLM analysis. By examining different future-view scenarios, the VLM pinpoints the direction most likely to incorporate the target object ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: ImagineNav: Comparison with previous work. The Where2Imagine model with T=11, utilizing ResNet-18 trained from scratch and GPT-4o-mini as the VLM, was evaluated over ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualization of the synthesized image observations at future navigation waypoints pre- dicted by the imagination module. It can be seen that there exists ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: ImagineNav: ablation study on the imagination module. ‘Imagination' refers to whether the future imagi- nations are used as visual prompts of the VLM. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of the navigation trajectory. The top and bottom rows respectively show the complete top-down trajectories of successful and unsuccessful examples. 4.6 ANALYSIS ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 3: Where2Imagine: the influence of sampling step T on navigation perfor- mance. T HM3D Success Rate SPL

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The HM3D dataset offers high-fidelity reconstructions of 20 entire buildings, including 80 training scenes and 20 validation scenes. | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | 4.1 EXPERIMENTAL SETUP AND METRICS We evaluate the effectiveness and navigation efficiency of our proposed method using the Habitat v3.0 simulator (Puig et al., ... | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS), p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the performance in terms of Success Rate (SR), defined as the proportion of episodes where the agent's distance to the target object ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| VLM HM3D Success Rate SPL LLaVa 44.0 21.6 GPT-4-Turbo 63.0 29.4 GPT-4o-mini 64.0 28.3 We conducted a comparative evaluation of the effects of different ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Backbone Params Flops Loss HM3D Success Rate SPL ResNet-18 (TFS) 11.4M 1.8G 0.12 64.0 28.3 ResNet-18 (FT) 11.4M 1.8G 0.24 61.0 29.7 ViT (TFS) ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Moreover, ImagineNav achieves the highest success rate and SPL on the HSSD dataset. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Notably, both the success rate and SPL exhibit obvious improvements, obtaining 62.0% and 59.0% at success rate respectively on H3MD and HSSD benchmarks, which ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ ✗ 43.0 24.7 ✓ ✗ ✗ 55.0 27.6 ✓ ✓ ✗ 64.0 28.3 ✓ ✗ ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| As shown in Table 3, the best success rate and SPL are obtained when T is set to 11. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 5: Visualization of the navigation trajectory. The top and bottom rows respectively show the complete top-down trajectories of successful and unsuccessful examples. 4.6 ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Method Open-Vocabulary Mapless HM3D HSSD Success Rate SPL Success Rate SPL FBE (Topiwala et al., 2018) ✗ ✗ 33.7 15.3 36.0 17.7 SemExp (Chaplot ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| ImagineNav uses NVS model to generate novel view images, while ImagineNav-Oracle uses real images of the candidate points. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| We compared different backbones to evaluate their impacts on both the relative waypoint prediction and final navigation performances. | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| Figure 3: An example of the VLM analysis. By examining different future-view scenarios, the VLM pinpoints the direction most likely to incorporate the target ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 8: The visualization of the relative pose predicted by the Where2Imagine module and poses sampled at 60° intervals with 2.0m radius. The upper ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| 4.4 ABLATION STUDY ON MAIN COMPONENTS Table 2: ImagineNav: ablation study on the imagination module. ‘Imagination' refers to whether the future imaginations are used ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ ✗ 43.0 24.7 ✓ ✗ ✗ 55.0 27.6 ✓ ✓ ✗ 64.0 28.3 ✓ ✗ ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Moreover, for models of the same architecture, it is possible to opt for more cost-effective variants without compromising navigation performance, thus enabling more resource-efficient ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Table 2: ImagineNav: ablation study on the imagination module. ‘Imagination' refers to whether the future imagi- nations are used as visual prompts of the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Furthermore, since the pretrained NVS is directly employed without finetunned on the HM3D and HSSD datasets, we see a disparity between 7 | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| 4.7 ANALYSIS OF VLM PLANNER Table 5: Effect of different VLM. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Each variant was tested for 100 epochs under conditions where the agent had access to real panoramic observations. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We propose a mapless navigation approach ImagineNav. | On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods especially at ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Primary metric/result | Moreover, ImagineNav achieves the highest success rate and SPL on the HSSD dataset. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The Where2Imagine model with T=11, utilizing ResNet-18 trained from scratch and GPT-4o-mini as the VLM, was evaluated over 200 epochs on the HM3D and HSSD ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** When it is removed, we feed current observations into VLM for deciding the best exploration direction, and set the next waypoint 2 meters away from ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Here, the distance of 2 meters is considered as it is comparable to that generated by T=11. ‘NVS' indicates whether the image is captured from ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Each variant was tested for 100 epochs under conditions where the agent had access to real panoramic observations.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Each variant was tested for 100 epochs.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The ‘MoveAhead' action moves the agent forward by 0.25m, while the rotational actions ‘TurnLeft' and ‘TurnRight' rotate the agent by 30 degrees.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also present some failure examples at the bottom of Figure 5. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | We identified three key factors contributing to these navigation failures. | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The Where2Imagine model with T=11, utilizing ResNet-18 trained from scratch and GPT-4o-mini as the VLM, was evaluated over 200 epochs on the HM3D and ... | p. 7 (4 EXPERIMENTS) |
| Each variant was tested for 100 epochs under conditions where the agent had access to real panoramic observations. | p. 9 (4 EXPERIMENTS) |
| Backbone Params Flops Loss HM3D Success Rate SPL ResNet-18 (TFS) 11.4M 1.8G 0.12 64.0 28.3 ResNet-18 (FT) 11.4M 1.8G 0.24 61.0 29.7 ViT (TFS) ... | p. 10 (4 EXPERIMENTS) |
| Each episode has a maximum limit of 500 steps. | p. 4 (3 METHODOLOGY) |
| The task is considered successful if the agent reaches the target object with a geodesic distance smaller than a defined threshold (e.g., 1m) and ... | p. 4 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We also present some failure examples at the bottom of Figure 5.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We identified three key factors contributing to these navigation failures.

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 6 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
