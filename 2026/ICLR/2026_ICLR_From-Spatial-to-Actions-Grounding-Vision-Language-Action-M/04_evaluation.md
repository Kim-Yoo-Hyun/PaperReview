# Evaluation - From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fzmittHfq3; PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments)): 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data.
- **p. 10 / 4 Experiments - extractive body cue:** To evaluate the modality transferability of FALCON, we conduct extensive experiments on both the CALVIN benchmark and real-world tasks to demonstrate the benefits of additional ...
- **p. 9 / 4 Experiments - extractive body cue:** Base Tasks contains a total of nine distinct task suites, encompassing language grounding (cluttered scenes with random distractors) and semantic understanding (unseen object poses).
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Real-World Experiments To enable a more comprehensive evaluation, we conduct a series of carefully designed real-world experiments covering diverse object manipulation scenarios with varying ...
- **p. 17 / C Implementation Details - extractive body cue:** For SimplerEnv and the real-world benchmark, both the VLM and ESM receive a single-step third-view image, and an MLP-based action predictor predicts an action chunk ...
- **p. 7 / 4 Experiments - extractive body cue:** For simulation, we evaluate on the widely used benchmarks CALVIN [26] and SimplerEnv [20].
- **p. 7 / 4 Experiments - extractive body cue:** For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a red ...
- **p. 9 / 4 Experiments - extractive body cue:** Cup height change Larger Block Smaller Block put the tomato on the plate that is between the blue and red car place the fruit that ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); C Implementation Details (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves SOTA performance in both the ABC→D and ABCD→D settings, significantly outperforming all 7 | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, FALCON achieves the highest performance across all settings, significantly outperforming the second-best model by 27.5% in Simple and 27% in Unseen Average. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1), FALCON achieves an impressive success rate of 80%, while other models demonstrate near-zero success. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data.
- **p. 10 / 4 Experiments - extractive body cue:** To evaluate the modality transferability of FALCON, we conduct extensive experiments on both the CALVIN benchmark and real-world tasks to demonstrate the benefits of additional ...
- **p. 9 / 4 Experiments - extractive body cue:** Base Tasks contains a total of nine distinct task suites, encompassing language grounding (cluttered scenes with random distractors) and semantic understanding (unseen object poses).
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Real-World Experiments To enable a more comprehensive evaluation, we conduct a series of carefully designed real-world experiments covering diverse object manipulation scenarios with varying ...
- **p. 17 / C Implementation Details - extractive body cue:** For SimplerEnv and the real-world benchmark, both the VLM and ESM receive a single-step third-view image, and an MLP-based action predictor predicts an action chunk ...
- **p. 7 / 4 Experiments - extractive body cue:** For simulation, we evaluate on the widely used benchmarks CALVIN [26] and SimplerEnv [20].
- **p. 7 / 4 Experiments - extractive body cue:** For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a red ...
- **p. 9 / 4 Experiments - extractive body cue:** Cup height change Larger Block Smaller Block put the tomato on the plate that is between the blue and red car place the fruit that ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | To evaluate the modality transferability of FALCON, we conduct extensive experiments on both the CALVIN benchmark and real-world tasks to demonstrate the benefits of ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 5 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Methodology), p. 5 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Notably, on the challenging task Open Top Drawer and Place Apple, most baselines show near-zero success rates. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Success rates for individual variants and sub-tasks are provided in Appendix I.2. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| This method achieves the highest task success rates while remaining both simple and computationally efficient, as it introduces no additional parameters. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| 7), increasing task success rates from 60% to 80% in scenarios involving objects of varying heights. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| The results underscore the effectiveness of a straightforward, parameter-free fusion strategy for combining spatial and semantic representations in VLA models. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Rel: computes the average absolute relative error between prediction and ground truth. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Our method achieves SOTA performance in both the ABC→D and ABCD→D settings, significantly outperforming all 7 | comparison identity and matched condition | p. 7 (4 Experiments) |
| FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Notably, baseline methods such as RoboVLM often struggle with objects of varying sizes. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 5, FALCON demonstrates superior spatial understanding, outperforming all existing policies across the evaluated tasks. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 5, under identical input conditions, FALCON outperforms Kosmos-VLA in the ABCD→D setting. | comparison identity and matched condition | p. 10 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To verify the effectiveness of our strategy for injecting 3D information into the action head, we evaluate a variant following the approach of most ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| Kosmos-VLA (w/ rgb-d) is a point cloud-based variant where the ESM is replaced by a lightweight point cloud encoder [46] while retaining other parts. | component/input/data sensitivity | p. 11 (4 Experiments) |
| Success rates for individual variants and sub-tasks are provided in Appendix I.2. | component/input/data sensitivity | p. 9 (4 Experiments) |
| 4.3 In-Depth Analysis Table 4 Ablation studies on spatial token injection methods and fusion strategies. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Kosmos-VLA (w/ rgb) is a 2D VLA without ESM. | component/input/data sensitivity | p. 11 (4 Experiments) |
| All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved ... | 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Primary metric/result | Our method achieves SOTA performance in both the ABC→D and ABCD→D settings, significantly outperforming all 7 | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive body cue:** Each task is evaluated over 10 different scene layouts with 10 trials, resulting in a total of 90 rollouts.
- **p. 17 / C Implementation Details - extractive body cue:** 7, on the CALVIN benchmark, the VLM receives side and wrist camera images with a history length of 16 frames, while the ESM processes third-view ...
- **p. 17 / C Implementation Details - extractive body cue:** FALCON requires ∼12.8 GB of GPU memory and runs at approximately 57 Hz on a single NVIDIA RTX 4090 GPU during real-world evaluation.
- **p. 5 / 3 Methodology - extractive body cue:** The overall loss function is defined as: L = t+C-1 X i=t MSE(ˆai,pose, ai,pose) + λ · BCE(ˆai,gripper, ai,gripper), (2) where the MSE term penalizes ...
- **p. 17 / C Implementation Details - extractive body cue:** 7, on the CALVIN benchmark, the VLM receives side and wrist camera images with a history length of 16 frames, while the ESM processes third-view ...
- **p. 17 / C Implementation Details - extractive body cue:** FALCON requires ∼12.8 GB of GPU memory and runs at approximately 57 Hz on a single NVIDIA RTX 4090 GPU during real-world evaluation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task ... | p. 9 (4 Experiments) |
| body limitation/failure cue | In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding. | p. 11 (5 Conclusion) |
| body limitation/failure cue | Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks. | p. 11 (5 Conclusion) |
| body limitation/failure cue | For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a ... | p. 7 (4 Experiments) |
| body limitation/failure cue | In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios. | p. 9 (4 Experiments) |
| body limitation/failure cue | 4, this approach results in significant performance degradation compared to the standard FALCON paradigm. | p. 10 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Abbreviations: Ep: Epochs, Iters: Iterations Experiment Name Action Predictor Window Size Chunk Size VLM Input View ESM Input View Batch Size Learning Rate Total ... | p. 17 (C Implementation Details) |
| Each task is evaluated over 10 different scene layouts with 10 trials, resulting in a total of 90 rollouts. | p. 9 (4 Experiments) |
| Rel: computes the average absolute relative error between prediction and ground truth. | p. 11 (4 Experiments) |
| Kosmos-VLA (w/ rgb-d) is a point cloud-based variant where the ESM is replaced by a lightweight point cloud encoder [46] while retaining other parts. | p. 11 (4 Experiments) |
| FALCON requires ∼12.8 GB of GPU memory and runs at approximately 57 Hz on a single NVIDIA RTX 4090 GPU during real-world evaluation. | p. 17 (C Implementation Details) |
| Through a spatial encoder Espl(·), it outputs a set of spatial tokens Tspl, encoding global 3D geometric priors essential for scene understanding. | p. 4 (3 Methodology) |
| (1) This setting spans diverse applications from service robots following language commands to industrial manipulators performing instruction-driven assembly, where robust performance in unstructured environments ... | p. 4 (3 Methodology) |
| Concurrently, the Embodied Spatial Model encodes a third-view image I3rd t and optional geometric inputs into spatial tokens Tspl. | p. 5 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.
- **p. 11 / 5 Conclusion - extractive body cue:** In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding.
- **p. 11 / 5 Conclusion - extractive body cue:** Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks.
- **p. 7 / 4 Experiments - extractive body cue:** For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a red ...
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.
- **p. 10 / 4 Experiments - extractive body cue:** 4, this approach results in significant performance degradation compared to the standard FALCON paradigm.

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 17 (C Implementation Details), p. 7 (4 Experiments), metrics p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), baselines p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), results p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
