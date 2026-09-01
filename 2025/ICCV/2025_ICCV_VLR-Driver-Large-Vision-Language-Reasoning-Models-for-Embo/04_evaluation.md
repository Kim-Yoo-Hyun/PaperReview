# Evaluation - VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (Figure/Table caption), p. 8 (5.3. Comparisons with Existing Methods), p. 6 (4.1. Data Collection)): We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR).

## Evaluation Body Digest

- **p. 6 / 4. VLR-Driver Dataset - extractive PDF cue:** The dataset includes 20,000 sets of multi-frame, multi-angle image data collected from various road conditions such as urban, rural, and highways in the CARLA simulator, ...
- **p. 6 / 4.1. Data Collection - extractive PDF cue:** We further expanded and enriched the dataset by collecting additional data in the CARLA simulator.
- **p. 8 / 5.3. Comparisons with Existing Methods - extractive PDF cue:** We conducted comprehensive experiments with the SOTA methods including E2E and VLM in the CARLA simulator across 44 routes from the Bench2Drive benchmark.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** The dataset used was the VLR-Driver dataset that we developed.
- **p. 7 / 4.2. Data Annotation - extractive PDF cue:** Therefore, we performed secondary annotation on the dataset we collected.
- **p. 8 / 5.3. Comparisons with Existing Methods - extractive PDF cue:** In contrast, our VLR-Driver can achieve deep understanding and inference of the current scene through LLM inference, so as to make timely detours.
- **p. 7 / 5.2. Metrics - extractive PDF cue:** We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR).
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. C, L and T indicate camera, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. VLR-Driver Dataset (p. 6); 5. Experiment (p. 7); 5.1. Experimental Setup (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Metrics | EMPIRICAL / SIMULATION | We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR). | p. 7 (5.2. Metrics) |
| 5.3. Comparisons with Existing Methods | EMPIRICAL / SIMULATION | Our method achieved the best results in all abilities, thanks to the deep reflection and reasoning ability of our VLR model, which has stronger ... | p. 8 (5.3. Comparisons with Existing Methods) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1. The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. C, L and T indicate ... | p. 7 (Figure/Table caption) |
| 5.3. Comparisons with Existing Methods | EMPIRICAL / SIMULATION | In contrast, our VLR-Driver can achieve deep understanding and inference of the current scene through LLM inference, so as to make timely detours. | p. 8 (5.3. Comparisons with Existing Methods) |
| 4.1. Data Collection | EMPIRICAL / SIMULATION | We conducted data collection based on the 44 corner scene classifications provided by Bench2Drive to ensure optimal AD performance in various complex corner scenarios. | p. 6 (4.1. Data Collection) |

## Dataset / Benchmark Role

- **p. 6 / 4. VLR-Driver Dataset - extractive PDF cue:** The dataset includes 20,000 sets of multi-frame, multi-angle image data collected from various road conditions such as urban, rural, and highways in the CARLA simulator, ...
- **p. 6 / 4.1. Data Collection - extractive PDF cue:** We further expanded and enriched the dataset by collecting additional data in the CARLA simulator.
- **p. 8 / 5.3. Comparisons with Existing Methods - extractive PDF cue:** We conducted comprehensive experiments with the SOTA methods including E2E and VLM in the CARLA simulator across 44 routes from the Bench2Drive benchmark.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** The dataset used was the VLR-Driver dataset that we developed.
- **p. 7 / 4.2. Data Annotation - extractive PDF cue:** Therefore, we performed secondary annotation on the dataset we collected.
- **p. 8 / 5.3. Comparisons with Existing Methods - extractive PDF cue:** In contrast, our VLR-Driver can achieve deep understanding and inference of the current scene through LLM inference, so as to make timely detours.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical reasoning, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Illustration of the ST-CoT reasoning process. In this sce- nario, where some vehicles are illegally parked ahead and blocking the lane, our method ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. C, L and T indicate camera, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. The comparison of advanced driving ability and experi- ence score with state-of-the-art models on the Bench2Drive bench- mark. OT, MER, EB, GW, TS, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Visual comparison between VLR-Driver and VLM- based methods. The ST-CoT guides the VLR model to approach driving decisions in a human-like spatiotemporal manner. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Tab. 2. Our method achieved the best results in all abili- ties, thanks to the deep reflection and reasoning ability of our VLR model, which ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study for each module. ID Abal. Exp. Core Metrics ↑ Advanced Driving Ability ↑ DS SR
- **p. 8 / Figure/Table caption - extractive PDF cue:** Tab. 3. The experimental configurations include four vari- ants: (1) Without utilizing our proposed spatiotemporal CoT strategy, using only a question-based approach with- out reasoning ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset includes 20,000 sets of multi-frame, multi-angle image data collected from various road conditions such as urban, rural, and highways in the CARLA ... | embodiment, simulator version and control stack | p. 6 (4. VLR-Driver Dataset), p. 6 (4.1. Data Collection) |
| Task/environment | We further expanded and enriched the dataset by collecting additional data in the CARLA simulator. | reset, timeout, object/scene variation | p. 6 (4.1. Data Collection), p. 8 (5.3. Comparisons with Existing Methods) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1. Overview), p. 2 (Front matter) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR). | definition/direction/unit from same section | p. 7 (5.2. Metrics) |
| Table 1. The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. C, L and T indicate ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| The images captured at 5 and 10 seconds afterward validate the accuracy of our decisions. | definition/direction/unit from same section | p. 8 (5.2. Metrics) |
| The comparison results of the advanced driving ability and driving experience score of each method are shown in Tab. | definition/direction/unit from same section | p. 8 (5.3. Comparisons with Existing Methods) |
| Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We conducted data collection based on the 44 corner scene classifications provided by Bench2Drive to ensure optimal AD performance in various complex corner scenarios. | definition/direction/unit from same section | p. 6 (4.1. Data Collection) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It can be seen that our method outperforms other methods in key metrics such as DS, RC, and SR, achieving first place and effectively ... | comparison identity and matched condition | p. 8 (5.3. Comparisons with Existing Methods) |
| The comparison of advanced driving ability and experience score with state-of-the-art models on the Bench2Drive benchmark. | comparison identity and matched condition | p. 7 (4.1. Data Collection) |
| The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. | comparison identity and matched condition | p. 7 (4.1. Data Collection) |
| We present comparison result in Tab. | comparison identity and matched condition | p. 8 (5.3. Comparisons with Existing Methods) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The experimental configurations include four variants: (1) Without utilizing our proposed spatiotemporal CoT strategy, using only a question-based approach without reasoning guidance. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| (4) Without Step-GRPO reinforcement learning training, using only LoRA strategies to fine-tune the model with supervision. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| Additionally, we selected over 30 scenarios where the reasoning and decision-making capabilities of AD systems are relatively limited, and used them as the visual ... | component/input/data sensitivity | p. 6 (4.1. Data Collection) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term ... | We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR). | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (Figure/Table caption), p. 8 (5.3. Comparisons with Existing Methods), p. 6 (4.1. Data Collection) |
| Primary metric/result | Our method achieved the best results in all abilities, thanks to the deep reflection and reasoning ability of our VLR model, which has stronger ... | numeric claim only at cited anchor | p. 8 (5.3. Comparisons with Existing Methods) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** The VLR-Driver model was trained on a server equipped with 8 NVIDIA A800 GPUs (each with 80G of video memory) for approximately 50 hours.
- **p. 4 / 3.1. Overview - extractive PDF cue:** We utilize Nf frame and Nv view images from the past period, with a field of view (FoV) of 70 degrees.
- **p. 4 / 3.1. Overview - extractive PDF cue:** It can be represented as V ∈ RNf ×Nv×3×H0×W0.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light ... | p. 7 (4.1. Data Collection) |
| body limitation/failure cue | Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The forward pass is computed as: y = W ′x =  W0 + α r B · A  x, (2) where y ... | p. 6 (3.3. Training Paradigm) |
| (4) We extend GRPO by introducing reasoning Step-GRPO, a supervised reasoning decision process that structures the output into multiple steps based on the CoT ... | p. 6 (3.3. Training Paradigm) |
| Specifically, we use ViT-g/14 from EVACLIP [29] as the vision encoder and LLaVA-NeXT-Video7B [50] as the VLM. | p. 7 (5.1. Experimental Setup) |
| In this study, we employ pre-trained LLaVA-NeXTVideo [50] as the VLM and CLIP [29] as the visual encoder. | p. 4 (3.1. Overview) |
| A rule-based method was used to determine the true values of future motion behaviors based on the decision choices made at earlier time steps. | p. 7 (4.2. Data Annotation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.1. Data Collection - extractive PDF cue:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical reasoning, ...

- **PDF anchors reviewed:** datasets p. 6 (4. VLR-Driver Dataset), p. 6 (4.1. Data Collection), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (5.1. Experimental Setup), p. 7 (4.2. Data Annotation), p. 8 (5.3. Comparisons with Existing Methods), metrics p. 7 (5.2. Metrics), p. 7 (Figure/Table caption), p. 8 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods), p. 3 (Figure/Table caption), p. 6 (4.1. Data Collection), baselines p. 8 (5.3. Comparisons with Existing Methods), p. 7 (4.1. Data Collection), p. 7 (4.1. Data Collection), p. 8 (5.3. Comparisons with Existing Methods), results p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (Figure/Table caption), p. 8 (5.3. Comparisons with Existing Methods), p. 6 (4.1. Data Collection).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
