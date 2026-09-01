# Evaluation - Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 8 (4.4. Ablation Study)): The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance.

## Evaluation Body Digest

- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** This dataset comprises 40,000 objects with ambiguous class definitions and diverse shapes, presenting a significant generalization hurdle.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** The second dataset employed originates from [7], encompassing 1650 ShapeNet [3] objects that span six categories: bowls, bottles, cameras, jars, guitars, and mugs.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Experimental results for different numbers of touches on dataset ShapeNet.
- **p. 7 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** Comparison of touch exploration on dataset ABC.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Ablation study results on dataset ABC.
- **p. 7 / 4.3. Evaluation on Policy - extractive PDF cue:** The former policy selects one of the available actions at random while the latter results in uniform coverage of the target object.
- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** Especially on the visual-tactile 3D reconstruction task, we obtain a very low CD error, which validates the multi-modal fusion ability of our model.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Settings (p. 5); 4.2. Evaluation on Reconstruction Performance (p. 6); 4.3. Evaluation on Policy (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance. | p. 7 (4.4. Ablation Study) |
| 4.2. Evaluation on Reconstruction Performance | EMPIRICAL / SOURCE-REPORTED EVALUATION | The latter method (we called ActiveVT here) proposes an active touch sensing for 3D reconstruction method to improve the reconstruction performance. | p. 6 (4.2. Evaluation on Reconstruction Performance) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 4, we add our proposed modules one by one to validate that each sub-module succeeds to improve the performance. | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Initially, limited information makes determining the overall global shape challenging, but with more grasp actions, our method effectively improves the reconstruction quality. | p. 8 (4.4. Ablation Study) |
| 4.2. Evaluation on Reconstruction Performance | EMPIRICAL / SOURCE-REPORTED EVALUATION | The quantitative results are reported in Table 2. | p. 6 (4.2. Evaluation on Reconstruction Performance) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** This dataset comprises 40,000 objects with ambiguous class definitions and diverse shapes, presenting a significant generalization hurdle.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** The second dataset employed originates from [7], encompassing 1650 ShapeNet [3] objects that span six categories: bowls, bottles, cameras, jars, guitars, and mugs.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Experimental results for different numbers of touches on dataset ShapeNet.
- **p. 7 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** Comparison of touch exploration on dataset ABC.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Ablation study results on dataset ABC.
- **p. 7 / 4.3. Evaluation on Policy - extractive PDF cue:** The former policy selects one of the available actions at random while the latter results in uniform coverage of the target object.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. (1) Exploring the target object and capturing the tactile image to reconstruct the 3D shape. We trained a diffusion model to obtain a ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. We pretrained (a) the shape encoder and decoder, (b) the touch CNN model that is used for touch chart prediction, and (c) the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Touch shape fusion module. The black arrows indicate the flow of the shape decoder, while the red arrows represent the flow after incorporating ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Experimental results for different settings and different numbers of grasps on dataset ABC. The evaluation metric is CD (lower is better).
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Experimental results for different numbers of touches on dataset ShapeNet. OursT and OursT V respectively represent our methods under the tactile only and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results of ActiveVT [34] and ours. While ActiveVT struggles with visualizations and detail preservation, our method excels in maintaining global shape accuracy ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison of touch exploration on dataset ABC. Num- bers represent a ratio (%) between CD after 5 actions and initial CD (with zero ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. The evolution of the reconstructed shape with an increasing number of grasps (in the tactile only setting). Initially, limited information makes determining the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing. | embodiment, simulator version and control stack | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 5 (4.1. Experimental Settings) |
| Task/environment | This dataset comprises 40,000 objects with ambiguous class definitions and diverse shapes, presenting a significant generalization hurdle. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 4 (3. Method), p. 2 (1. Introduction) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 4 (3.1. Touch-conditioned Diffusion Model), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Especially on the visual-tactile 3D reconstruction task, we obtain a very low CD error, which validates the multi-modal fusion ability of our model. | definition/direction/unit from same section | p. 6 (4.2. Evaluation on Reconstruction Performance) |
| While ActiveVT struggles with visualizations and detail preservation, our method excels in maintaining global shape accuracy across diverse structures, ensuring satisfactory local details. | definition/direction/unit from same section | p. 7 (4.2. Evaluation on Reconstruction Performance) |
| The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| In this section, we describe the experiment settings and then compare our model with the state-of-art touch-based 3D reconstruction methods and validate our policy ... | definition/direction/unit from same section | p. 5 (4. Experiment) |
| The former is a common 3D reconstruction metric for measuring the point-wise distance between two pointsets. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Figure 1. (1) Exploring the target object and capturing the tactile image to reconstruct the 3D shape. We trained a diffusion model to obtain ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. We pretrained (a) the shape encoder and decoder, (b) the touch CNN model that is used for touch chart prediction, and (c) ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of ... | comparison identity and matched condition | p. 7 (4.3. Evaluation on Policy) |
| As [34], we set two baseline methods, Random and Even. | comparison identity and matched condition | p. 7 (4.3. Evaluation on Policy) |
| Figure 1. (1) Exploring the target object and capturing the tactile image to reconstruct the 3D shape. We trained a diffusion model to obtain ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Through the ablation study, we validate the necessity of each module. | comparison identity and matched condition | p. 5 (4. Experiment) |
| For touch sensing, we adopt the setting of TouchSDF [7], which involves capturing tactile images by poking the target object, ensuring a fair comparison. | comparison identity and matched condition | p. 6 (4.2. Evaluation on Reconstruction Performance) |
| Ablation study results on dataset ABC. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Through the ablation study, we validate the necessity of each module. | component/input/data sensitivity | p. 5 (4. Experiment) |
| We design the ablation study to further validate the necessity of our proposed reconstruction modules. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Ablation study results on dataset ABC. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| The evaluation metric is EMD (lower is better). touch shape fusion can be trained concurrently since they do not share any components. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| Figure 2. We pretrained (a) the shape encoder and decoder, (b) the touch CNN model that is used for touch chart prediction, and (c) ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing ... | The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 8 (4.4. Ablation Study) |
| Primary metric/result | The latter method (we called ActiveVT here) proposes an active touch sensing for 3D reconstruction method to improve the reconstruction performance. | numeric claim only at cited anchor | p. 6 (4.2. Evaluation on Reconstruction Performance) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** This dataset comprises 40,000 objects with ambiguous class definitions and diverse shapes, presenting a significant generalization hurdle.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** After the diffusion model training finished, we conducted policy training in silmulation environment [34] for 200 epochs with a learning rate of 0.0003 and batch ...
- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** To calculate the Chamfer Distance (CD) for our SDF volume, we run marching cubes to get the object meshes and extract 30,000 points from each ...
- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive PDF cue:** The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of ... | p. 7 (4.3. Evaluation on Policy) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| After the diffusion model training finished, we conducted policy training in silmulation environment [34] for 200 epochs with a learning rate of 0.0003 and ... | p. 6 (4.1. Experimental Settings) |
| The diffusion model was trained for 1 million iterations with an initial learning rate of 0.00001 and batch size of 12, while the touch ... | p. 6 (4.1. Experimental Settings) |
| Instead, we utilize the shape decoder and shape fusion only at the final time step, thereby achieving a separation of shape decoder and shape ... | p. 5 (3.3. Policy Training) |
| We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion ... | p. 5 (3.3. Policy Training) |
| We also train a vision-conditioned diffusion model (V represents the visual only setting) with a contrastive visual encoder. | p. 7 (4.4. Ablation Study) |
| Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of ... | p. 7 (4.3. Evaluation on Policy) |
| CL represents the contrastive encoder and Fusion represents the touch shape fusion module respectively. | p. 8 (4.4. Ablation Study) |
| Following SDFusion [5], we employ the volumetric Truncated Signed Distance Field (T-SDF) to model the distribution across 3D shapes and a 3D variant of ... | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Evaluation on Policy - extractive PDF cue:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison ...

- **PDF anchors reviewed:** datasets p. 6 (4.2. Evaluation on Reconstruction Performance), p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Evaluation on Reconstruction Performance), p. 8 (4.4. Ablation Study), metrics p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study), p. 5 (4. Experiment), p. 6 (4.1. Experimental Settings), p. 1 (Figure/Table caption), baselines p. 7 (4.3. Evaluation on Policy), p. 7 (4.3. Evaluation on Policy), p. 1 (Figure/Table caption), p. 5 (4. Experiment), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 8 (4.4. Ablation Study), results p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
