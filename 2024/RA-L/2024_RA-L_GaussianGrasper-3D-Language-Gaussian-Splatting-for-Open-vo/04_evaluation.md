# Evaluation - GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.09637; PDF retrieval source: https://arxiv.org/pdf/2403.09637. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption)): The results of segmentation and localization are shown in Table I where our method significantly outperforms other approaches.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENT - extractive body cue:** 2) Data Collection and Processing: We first use the robot arm equipped with a Realsense D455 to scan the desktop scene from 16 viewpoints.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** We set up our system in 10 open desktop scenes with a total of 44 objects (40 are graspable) where we execute language-guided manipulation 120 ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Therefore, our method can help robots reduce the ambiguity of object perception.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** We also directly distill CLIP features into 3D Gaussian field, which takes over 70 GB of memory, making it hard to be applied to robots.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** 2) Scene updating: To validate the effectiveness of our proposed efficient scene updating, we execute an experiment whose process is (1) picking up the object ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** EACH OBJECT IS GRASPED THREE TIMES.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Method Grasping Success Rate (%) LSeg + Depth[45] 26.7 LERF + AnyGrasp[16] 55.8 Ours w/o.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The result is shown in Table II, where our method far exceeds other methods in success rate.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results of segmentation and localization are shown in Table I where our method significantly outperforms other approaches. | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Leveraging the normal filter significantly increases the success rate by 7.7%, further demonstrating the effectiveness of our proposed normal-guided grasp. | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Besides, we report the quantitative results of the grasping success rate with and without the normal filter, as shown in Table II. | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | It can be seen that our method achieves an approximate 180 × speedup over LERF. | p. 6 (IV. EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1. We present a comparison between our method, 2D feature fusion, and LERF. When given the language query "hamburger", the features extracted by ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENT - extractive body cue:** 2) Data Collection and Processing: We first use the robot arm equipped with a Realsense D455 to scan the desktop scene from 16 viewpoints.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** We set up our system in 10 open desktop scenes with a total of 44 objects (40 are graspable) where we execute language-guided manipulation 120 ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Therefore, our method can help robots reduce the ambiguity of object perception.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** We also directly distill CLIP features into 3D Gaussian field, which takes over 70 GB of memory, making it hard to be applied to robots.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** 2) Scene updating: To validate the effectiveness of our proposed efficient scene updating, we execute an experiment whose process is (1) picking up the object ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** EACH OBJECT IS GRASPED THREE TIMES.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We present a comparison between our method, 2D feature fusion, and LERF. When given the language query "hamburger", the features extracted by the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. The architecture of our proposed method. (a) is our proposed pipeline where we scan multi-view RGBD images for initialization and reconstruct 3D Gaussian ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Relevance map of the given language instructions. Our method exhibits clearer segmentation boundaries compared to LERF, which can be used to obtain more ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Compared with scanned depth and surface normal, our rendered depth and surface normal is smoother. Our method renders accurate depth and surface normal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Effectiveness of our proposed normal-guided grasp. The left column shows the top 5 grasp proposals provided by AnyGrasp. The redder the color, the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Results of scene update. We show the RGB, depth, normal, and segmentation before and after the scene update based on the language query ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) Data Collection and Processing: We first use the robot arm equipped with a Realsense D455 to scan the desktop scene from 16 viewpoints. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Task/environment | We set up our system in 10 open desktop scenes with a total of 44 objects (40 are graspable) where we execute language-guided manipulation ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Method Grasping Success Rate (%) LSeg + Depth[45] 26.7 LERF + AnyGrasp[16] 55.8 Ours w/o. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| The result is shown in Table II, where our method far exceeds other methods in success rate. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| In the segmentation task, as described in III-C1 we filter out the region whose relevance score is below 0.85 to form a predicted segmentation ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| In the localization task, following LERF, given a language instruction, if the point with the highest relevance score is in the target object, it ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| These experiments fully demonstrate the performance of our method in open-scene understanding and language-guided grasping. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| The collected images are processed by SAM and CLIP to generate segmentation maps and open-vocabulary feature maps. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| Fig. 2. The architecture of our proposed method. (a) is our proposed pipeline where we scan multi-view RGBD images for initialization and reconstruct 3D ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our baselines are Lseg [45] and LERF [16] (All mention of LERF in our experiments includes an extra depth supervision to ensure a fair ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Besides, compared with LERF, our method exhibits better segmentation boundaries. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Compared with scanned depth and surface normal, our rendered depth and surface normal is smoother. | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| Subsequently, we show the results of geometry reconstruction and conduct ablation study to demonstrate the effectiveness of our proposed normal-guided grasp. | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| Besides, we report the quantitative results of the grasping success rate with and without the normal filter, as shown in Table II. | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| Fig. 1. We present a comparison between our method, 2D feature fusion, and LERF. When given the language query "hamburger", the features extracted by ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Subsequently, we show the results of geometry reconstruction and conduct ablation study to demonstrate the effectiveness of our proposed normal-guided grasp. | component/input/data sensitivity | p. 5 (IV. EXPERIMENT) |
| Besides, we report the quantitative results of the grasping success rate with and without the normal filter, as shown in Table II. | component/input/data sensitivity | p. 7 (IV. EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field ... | The results of segmentation and localization are shown in Table I where our method significantly outperforms other approaches. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Primary metric/result | Leveraging the normal filter significantly increases the success rate by 7.7%, further demonstrating the effectiveness of our proposed normal-guided grasp. | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Experimental Setup 1) Scenes, Objects and Devices: We built a 140×70×30cm3 desktop scene with common objects in the kitchen including various food and tableware as ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** We set up our system in 10 open desktop scenes with a total of 44 objects (40 are graspable) where we execute language-guided manipulation 120 ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** In terms of computing resources, we use an NVIDIA RTX-3090 GPU to reconstruct the feature field and reconstruct geometry.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Method Viewpoints Memory Time LERF [16] 16 15GB 30min Ours 5 4GB 1min 1) Successful rate of manipulation: In this subsection, we show the result ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation is that our reconstructed scene remains static. | p. 7 (V. LIMITATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In terms of computing resources, we use an NVIDIA RTX-3090 GPU to reconstruct the feature field and reconstruct geometry. | p. 5 (IV. EXPERIMENT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. LIMITATION - extractive body cue:** One limitation is that our reconstructed scene remains static.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), metrics p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), baselines p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 1 (Figure/Table caption), results p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
