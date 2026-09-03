# Evaluation - SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.12168; PDF retrieval source: https://arxiv.org/pdf/2401.12168. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 7 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.2. Effect of Spatial VQA Data to General VQA)): Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions.

## Evaluation Body Digest

- **p. 8 / 4. Experiments - extractive body cue:** It shows state-of-the-art performance in OKVQA benchmark, as well as being capable of robot planning tasks.
- **p. 9 / 4.2. Effect of Spatial VQA Data to General VQA - extractive body cue:** We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table.
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** We train VLMs using the noisy datasets and evaluate them using a human annotated quantitative spatial VQA benchmark for manipulation.
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** Therefore, we leverage our robotic manipulation dataset, which provides near-groundtruth depth information captured using a depth camera.
- **p. 11 / 4.5. Spatial Reasoning Unlocks Novel Applications - extractive body cue:** Weconduct a real robot experiment where we specify a task in nature language and ask SpatialVLM to annotate a reward for each frame in a ...
- **p. 7 / 4. Experiments - extractive body cue:** We train our model using a mixture of PaLM-E training set and our spatial VQA dataset.
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** Such visual question-answer pairs can be easily mixed together with other captioning or question answering datasets and use the same training objectives.
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** Thanks to the diversity of object captions and distance units, our synthetic dataset features significant diversity in terms of object description, question type and phrasing.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.2. Large-Scale Spatial Reasoning VQA Dataset (p. 5); 4. Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Spatial VQA performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions. | p. 9 (4.1. Spatial VQA performance) |
| 4.1. Spatial VQA performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is shown that SpatialVLM is able to achieve significantly higher accuracy compared to all baselines that are not trained using the synthetic spatial ... | p. 8 (4.1. Spatial VQA performance) |
| 4.1. Spatial VQA performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | Therefore, to evaluate the performance of the VLMs, we use human raters to determine if an answer is correct, and show the success rates ... | p. 8 (4.1. Spatial VQA performance) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | GPT-4V1 GPT-4V is a version of GPT-4 [51] that supports multimodal input, it achieves state-of-the-art performance in many vision-language tasks. | p. 7 (4. Experiments) |
| 4.2. Effect of Spatial VQA Data to General VQA | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, our model achieves comparable performance as PaLM 2-E on the OKVQA benchmark, in which limited spatial reasoning questions are included, and performs slightly ... | p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |

## Dataset / Benchmark Role

- **p. 8 / 4. Experiments - extractive body cue:** It shows state-of-the-art performance in OKVQA benchmark, as well as being capable of robot planning tasks.
- **p. 9 / 4.2. Effect of Spatial VQA Data to General VQA - extractive body cue:** We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table.
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** We train VLMs using the noisy datasets and evaluate them using a human annotated quantitative spatial VQA benchmark for manipulation.
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** Therefore, we leverage our robotic manipulation dataset, which provides near-groundtruth depth information captured using a depth camera.
- **p. 11 / 4.5. Spatial Reasoning Unlocks Novel Applications - extractive body cue:** Weconduct a real robot experiment where we specify a task in nature language and ask SpatialVLM to annotate a reward for each frame in a ...
- **p. 7 / 4. Experiments - extractive body cue:** We train our model using a mixture of PaLM-E training set and our spatial VQA dataset.
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** Such visual question-answer pairs can be easily mixed together with other captioning or question answering datasets and use the same training objectives.
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** Thanks to the diversity of object captions and distance units, our synthetic dataset features significant diversity in terms of object description, question type and phrasing.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It shows state-of-the-art performance in OKVQA benchmark, as well as being capable of robot planning tasks. | embodiment, simulator version and control stack | p. 8 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |
| Task/environment | We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table. | reset, timeout, object/scene variation | p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.3. Learning Spatial Reasoning), p. 1 (Body text (section not recovered)) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.1. Spatial Grounding from 2D Images) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Therefore, to evaluate the performance of the VLMs, we use human raters to determine if an answer is correct, and show the success rates ... | definition/direction/unit from same section | p. 8 (4.1. Spatial VQA performance) |
| First, we use the success rate of the VLM to produce a number to reflect if the VLM is able to understand the quantitative ... | definition/direction/unit from same section | p. 8 (4.1. Spatial VQA performance) |
| Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions. | definition/direction/unit from same section | p. 9 (4.1. Spatial VQA performance) |
| To better understand our model's performance and limitations, we visualized the relative error against the ground truth value in Fig. | definition/direction/unit from same section | p. 9 (4.1. Spatial VQA performance) |
| 5), which further demonstrates the data accuracy. | definition/direction/unit from same section | p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers) |
| In Figure 6, each dot illustrates an object location and their color indicates the annotated reward. | definition/direction/unit from same section | p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications) |
| SinceSpatialVLMisabletoquantitativelyestimatedistancesorsizesfromimage, it'suniquelysuitedasadenserewardannotator. | definition/direction/unit from same section | p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications) |
| Our model achieves 8.4% accuracy for predicting a value 0.9× to 1.1× range of human annotation. | definition/direction/unit from same section | p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures ... | comparison identity and matched condition | p. 7 (4. Experiments) |
| Our proposed method outperform baselines on binary predicate prediction tasks by a large margin owing to the addition of synthetic data. | comparison identity and matched condition | p. 8 (4. Experiments) |
| It is shown that SpatialVLM is able to achieve significantly higher accuracy compared to all baselines that are not trained using the synthetic spatial ... | comparison identity and matched condition | p. 8 (4.1. Spatial VQA performance) |
| We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table. | comparison identity and matched condition | p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |
| A PaLM 2-E model trained with SpatialVLM data improves VQA v2 performance by 2.4% compared to a model with the same number of parameters, ... | comparison identity and matched condition | p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |
| GPT-4V1 GPT-4V is a version of GPT-4 [51] that supports multimodal input, it achieves state-of-the-art performance in many vision-language tasks. | comparison identity and matched condition | p. 7 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Due to the shared network architecture and training procedure with SpatialVLM, vanilla PaLM 2-E naturally serves as the baseline to study the effect of ... | component/input/data sensitivity | p. 8 (4. Experiments) |
| Effect of Visual Transformer (ViT) Encoder in Spatial Reasoning Does a frozen ViT (trained on contrastive objective) encode enough information to perform spatial reasoning? | component/input/data sensitivity | p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |
| To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures ... | component/input/data sensitivity | p. 7 (4. Experiments) |
| We used PaLI-X 55B variant in our experiments. | component/input/data sensitivity | p. 8 (4. Experiments) |
| We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table. | component/input/data sensitivity | p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |
| This seem to suggest that VLMs are generally underfitting in the distribution of tasks close to spatial reasoning, and can benefit from spatial VQA ... | component/input/data sensitivity | p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities. | Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 7 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |
| Primary metric/result | It is shown that SpatialVLM is able to achieve significantly higher accuracy compared to all baselines that are not trained using the synthetic spatial ... | numeric claim only at cited anchor | p. 8 (4.1. Spatial VQA performance) |

- Numeric sentences retained from the body:
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** 20 centimeters Figure 3 / Example data entries from the synthetic dataset.
- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** We found that SpatialVLM does well on medium range scenes like those with objects 1-10 meters from the camera.
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive body cue:** In fact, human sometimes tend to give noisy estimations, as they prefer to round an estimation of 0.8 meter to 1 meter.
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** Since the objects in the manipulation VQA datasets are within 1 meter range, we added the mean squared error (MSE) as a 10
- **p. 11 / 4.5. Spatial Reasoning Unlocks Novel Applications - extractive body cue:** A large language model, in this case GPT-4, when equipped with SpatialVLM as a spatial reasoning submodule, can perform complex spatial reasoning tasks, such as ...
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive body cue:** 20 centimeters Figure 3 / Example data entries from the synthetic dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, we find that state-of-the-art VLM GPT-4V often refrain from generating answers about distance in SI units with a disclaimer text "I'm sorry, but ... | p. 9 (4.1. Spatial VQA performance) |
| body limitation/failure cue | To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures ... | p. 7 (4. Experiments) |
| body limitation/failure cue | VLM answers that fall into half to twice of the ground truth value to represent how accurate the VLM's estimates are. | p. 9 (4.1. Spatial VQA performance) |
| body limitation/failure cue | We train both models for 70k steps, and evaluate percentages of answers from both models that fall into various ranges of the ground truth ... | p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |
| body limitation/failure cue | 5 compares how different Gaussian noise standard deviations affect the overall VLM performance on quantitative spatial VQA. | p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers) |
| body limitation/failure cue | It is shown that VLMs trained on datasets of different noise levels achieve similar spatial reasoning accuracy. | p. 11 (4.4. Effect of Noisy Quantitative Spatial Answers) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| An encoder-decoder VLM trained on multi-lingual corpora, it shows state-of-the-art performance on captioning and visual-question answering tasks. | p. 8 (4. Experiments) |
| As discussed in Section 4.1 the monocular depth estimation is one of the steps in the data generation pipeline that induce the most noises. | p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers) |
| We train both models for 70k steps, and evaluate percentages of answers from both models that fall into various ranges of the ground truth ... | p. 10 (4.2. Effect of Spatial VQA Data to General VQA) |
| This natural proficiency in direct spatial reasoning tasks contrasts with the current limitations of VLMs and thus prevents them from accomplishing real-world tasks that ... | p. 2 (1. Introduction) |
| Semantic Filtering While internet-scale image-captioning datasets have been widely used in VLM training [12], many images in these datasets are not suitable for synthesizing ... | p. 4 (3.1. Spatial Grounding from 2D Images) |
| Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic segmentation and ... | p. 4 (3. SpatialVLM) |
| Chain-of-Thought Spatial Reasoning Many real-world tasks require multiple steps of spatial reasoning. | p. 6 (3.3. Learning Spatial Reasoning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** Additionally, we find that state-of-the-art VLM GPT-4V often refrain from generating answers about distance in SI units with a disclaimer text "I'm sorry, but I ...
- **p. 7 / 4. Experiments - extractive body cue:** To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures in ...
- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** VLM answers that fall into half to twice of the ground truth value to represent how accurate the VLM's estimates are.
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive body cue:** We train both models for 70k steps, and evaluate percentages of answers from both models that fall into various ranges of the ground truth value ...
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** 5 compares how different Gaussian noise standard deviations affect the overall VLM performance on quantitative spatial VQA.
- **p. 11 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** It is shown that VLMs trained on datasets of different noise levels achieve similar spatial reasoning accuracy.

- **Evidence anchors reviewed:** datasets p. 8 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers), p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications), p. 7 (4. Experiments), metrics p. 8 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 9 (4.1. Spatial VQA performance), p. 9 (4.1. Spatial VQA performance), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers), p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications), baselines p. 7 (4. Experiments), p. 8 (4. Experiments), p. 8 (4.1. Spatial VQA performance), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.2. Effect of Spatial VQA Data to General VQA), p. 7 (4. Experiments), results p. 9 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 7 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.2. Effect of Spatial VQA Data to General VQA).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
