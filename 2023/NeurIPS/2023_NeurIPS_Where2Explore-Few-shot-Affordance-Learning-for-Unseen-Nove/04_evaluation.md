# Evaluation - Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.07473; PDF retrieval source: https://arxiv.org/pdf/2309.07473. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 5 (Figure/Table caption)): For both the F-score and sample success rate, we use the average score of the four different training category combinations.

## Evaluation Body Digest

- **p. 9 / 5 Experiments - extractive body cue:** Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp Manipulation After Exploration ...
- **p. 7 / 5 Experiments - extractive body cue:** Compared with PointEncoder, we show that our framework better understands the semantic information for manipulation than a pre-trained encoder, even if it is trained on ...
- **p. 6 / 5 Experiments - extractive body cue:** We also perform few-shot learning on each novel category separately to match the real-world scenario.
- **p. 6 / 5 Experiments - extractive body cue:** Following Where2Act and AdaAfford [25, 35], we abstract away the robot arm and only use a Franka Panda flying gripper as the robot actuator.
- **p. 7 / 5 Experiments - extractive body cue:** We select PointEncoder to compare our framework with a network pre-trained on large-scale datasets.
- **p. 8 / 5 Experiments - extractive body cue:** We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario.
- **p. 9 / 5 Experiments - extractive body cue:** In this visualization, for objects in the simulator, the action directions are set to the normal direction of each point.
- **p. 8 / 5 Experiments - extractive body cue:** 5.4 Qualitative Results and Analysis Affordance Similarity Where2Act strategy Affordance Similarity AdaAfford strategy Affordance Similarity AdaAfford strategy Affordance Similarity Pushing Pulling Where2Act strategy Figure 4: ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 6); B More Experimental Results and Analysis (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our framework also achieves comparable performance compared with Full-data, which is trained on all categories with abundant data. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We calculate the sample success rate by randomly selecting one action predicted as successful by the affordance module, performing the interaction, and observing the ... | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately ... | p. 8 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Affordance on novel object Similarity on novel object Exploration on novel object Affordance after exploration Affordance on novel object Similarity on novel object Exploration ... | p. 9 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 5 Experiments - extractive body cue:** Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp Manipulation After Exploration ...
- **p. 7 / 5 Experiments - extractive body cue:** Compared with PointEncoder, we show that our framework better understands the semantic information for manipulation than a pre-trained encoder, even if it is trained on ...
- **p. 6 / 5 Experiments - extractive body cue:** We also perform few-shot learning on each novel category separately to match the real-world scenario.
- **p. 6 / 5 Experiments - extractive body cue:** Following Where2Act and AdaAfford [25, 35], we abstract away the robot arm and only use a Franka Panda flying gripper as the robot actuator.
- **p. 7 / 5 Experiments - extractive body cue:** We select PointEncoder to compare our framework with a network pre-trained on large-scale datasets.
- **p. 8 / 5 Experiments - extractive body cue:** We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario.
- **p. 9 / 5 Experiments - extractive body cue:** In this visualization, for objects in the simulator, the action directions are set to the normal direction of each point.
- **p. 8 / 5 Experiments - extractive body cue:** 5.4 Qualitative Results and Analysis Affordance Similarity Where2Act strategy Affordance Similarity AdaAfford strategy Affordance Similarity AdaAfford strategy Affordance Similarity Pushing Pulling Where2Act strategy Figure 4: ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Where2Explore framework. Our model, solely trained on training categories (Top Left) and having never seen mugs, utilizes the underlying similarity in local geometries ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Method overview: We first employ affordance learning on the affordance category to form our supporting set (Left). Then, we estimate the semantic similarity ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Cross-category similarity learning. We use a similarity module to predict the similarity conditioned on specific actions (Middle). While the affordance category is used ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Few-shot learning on novel categories using different interaction budget (1, 2, 5). Table 1 shows the results of few-shot learning on novel categories ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Evaluation of few-shot learning on different categories separately (5 interaction budget) F-score Sample successful rate
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of different exploration strategies on novel objects. The action directions are set to the normal direction of each point in this visualization. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Pushing (top) and pulling (middle and bottom) affordance and similarity prediction on novel object categories. Although Affordance fails to directly generalize to novel ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp Manipulation After ... | embodiment, simulator version and control stack | p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | Compared with PointEncoder, we show that our framework better understands the semantic information for manipulation than a pre-trained encoder, even if it is trained ... | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4 Method), p. 4 (4 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4 Method), p. 5 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For both the F-score and sample success rate, we use the average score of the four different training category combinations. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Following Where2Act [25] and AdaAfford [35], we use the F-score, balancing the precision and recall, to evaluate the predictions of the visual affordance and ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Table 2: Evaluation of few-shot learning on different categories separately (5 interaction budget) F-score Sample successful rate | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 3: Cross-category similarity learning. We use a similarity module to predict the similarity conditioned on specific actions (Middle). While the affordance category is ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| We also conduct ablation studies to prove the efficiency of our exploration strategy. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| We also perform few-shot learning on each novel category separately to match the real-world scenario. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Affordance on novel object Similarity on novel object Exploration on novel object Affordance after exploration Affordance on novel object Similarity on novel object Exploration ... | definition/direction/unit from same section | p. 9 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 1: Few-shot learning on novel categories using different interaction budget (1, 2, 5). Table 1 shows the results of few-shot learning on novel ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We set up three baselines for comparisons. | comparison identity and matched condition | p. 6 (5 Experiments) |
| 5.2 Baselines, Ablations, and Metrics Baselines and Ablations. | comparison identity and matched condition | p. 7 (5 Experiments) |
| For baselines, we train the models using all training objects in training categories, whereas we divide the training categories into two parts to train ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| Our framework also achieves comparable performance compared with Full-data, which is trained on all categories with abundant data. | comparison identity and matched condition | p. 8 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Besides, we compare to ablated versions of our method to verify our exploration strategy: • No-explore (lower bound): our affordance model directly evaluated on ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| We also conduct ablation studies to prove the efficiency of our exploration strategy. | component/input/data sensitivity | p. 6 (5 Experiments) |
| 5.2 Baselines, Ablations, and Metrics Baselines and Ablations. | component/input/data sensitivity | p. 7 (5 Experiments) |
| Finally, we test our fine-tuned model on unseen instances in novel categories to demonstrate that our model learns the general semantic and geometric information. | component/input/data sensitivity | p. 6 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 5 (Figure/Table caption) |
| Primary metric/result | Our framework also achieves comparable performance compared with Full-data, which is trained on all categories with abundant data. | numeric claim only at cited anchor | p. 8 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Method - extractive body cue:** The encoder will output a per-point feature of 128 dimensions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. | p. 8 (5 Experiments) |
| body limitation/failure cue | Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on ... | p. 9 (5 Experiments) |
| body limitation/failure cue | While affordance fails to directly generalize to novel objects (Left), the similarity module can still discover areas that contain uncertain yet important semantic information ... | p. 9 (5 Experiments) |
| body limitation/failure cue | Table 4: Few-shot learning on novel categories using different interaction budget (1, 2, 5). B More Experimental Results and Analysis We visualize more similarity-guided ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Compared to the AdaAfford, our results suggest that instance-level exploration strategies which focus on dynamic information for a single object fail to generalize well ... | p. 7 (5 Experiments) |
| body limitation/failure cue | Compared with other exploration strategies Explore-random and Explore-noSim that fail to discover important local areas, our strategy is dramatically more effective and efficient. | p. 8 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We select PointEncoder to compare our framework with a network pre-trained on large-scale datasets. | p. 7 (5 Experiments) |
| This baseline uses the pre-trained transformer encoder to extract features for few-shot affordance learning. | p. 7 (5 Experiments) |
| The Accu is computed using the accuracy in predicting the affordance score of an action during training. | p. 5 (4 Method) |
| The encoder will output a per-point feature of 128 dimensions. | p. 6 (4 Method) |
| We employ Multilayer Perceptrons (MLP) with one hidden layer of size 128 to implement both decoders. | p. 6 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Experiments - extractive body cue:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.
- **p. 9 / 5 Experiments - extractive body cue:** Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on them ...
- **p. 9 / 5 Experiments - extractive body cue:** While affordance fails to directly generalize to novel objects (Left), the similarity module can still discover areas that contain uncertain yet important semantic information to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Few-shot learning on novel categories using different interaction budget (1, 2, 5). B More Experimental Results and Analysis We visualize more similarity-guided exploration ...
- **p. 7 / 5 Experiments - extractive body cue:** Compared to the AdaAfford, our results suggest that instance-level exploration strategies which focus on dynamic information for a single object fail to generalize well across ...
- **p. 8 / 5 Experiments - extractive body cue:** Compared with other exploration strategies Explore-random and Explore-noSim that fail to discover important local areas, our strategy is dramatically more effective and efficient.

- **PDF anchors reviewed:** datasets p. 9 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (5 Experiments), p. 6 (5 Experiments), baselines p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments), results p. 7 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
