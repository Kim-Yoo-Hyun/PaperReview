# Evaluation - PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (Figure/Table caption), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Ablation Study & Model Analysis), p. 7 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis)): Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, the previous state-of-the-art.

## Evaluation Body Digest

- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Our experiments are conducted on a popular simulation benchmark RLBench [31] which is built upon the CoppelaSim simulator.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** We train and evaluate PDFactor with the same dataset as PerAct, with 100 demonstrations for training and 25 unseen demonstrations for testing.
- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** Multi-task performance on 6 real world tasks. show that PDFactor learns manipulation tasks effectively with noisy and limited real-world demonstrations.
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We evaluate 25 episodes per task on 18 challenging tasks from RLBench and report mean and standard deviation of success rates (%) across 5 random ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We train PDFactor and RVT-2 for 18 tasks with an increasing number of demonstrations. ding.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous state-of-the-art ...
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive PDF cue:** Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiment Setup (p. 6); 4.4. Evaluation in the Real World (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison with State-of-the-Art Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, ... | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous ... | p. 8 (Figure/Table caption) |
| 4.1. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate policies by task completion success rate, which is the proportion of execution trajectories that achieve the goal conditions specified in the language ... | p. 6 (4.1. Experiment Setup) |
| 4.3. Ablation Study & Model Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The data indicates that success rate improves as model size increases, demonstrating the scalability of the proposed method. | p. 7 (4.3. Ablation Study & Model Analysis) |
| 4.3. Ablation Study & Model Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Besides, as the number of demonstrations increases, the success rate for smaller models plateaus, whereas larger models continue to improve, showing that larger PDFactor ... | p. 7 (4.3. Ablation Study & Model Analysis) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Our experiments are conducted on a popular simulation benchmark RLBench [31] which is built upon the CoppelaSim simulator.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** We train and evaluate PDFactor with the same dataset as PerAct, with 100 demonstrations for training and 25 unseen demonstrations for testing.
- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** Multi-task performance on 6 real world tasks. show that PDFactor learns manipulation tasks effectively with noisy and limited real-world demonstrations.
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We evaluate 25 episodes per task on 18 challenging tasks from RLBench and report mean and standard deviation of success rates (%) across 5 random ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We train PDFactor and RVT-2 for 18 tasks with an increasing number of demonstrations. ding.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Policy Representations. (a) Explicit policy predicts a specific action distribution along the 3D space. (b) Implicit pol- icy, e.g., energy-based and diffusion-based models, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. PDFactor Overview. The 3D point cloud reconstructed from the multi-view RGB-D images is first featurized and projected to three orthogonal views, which are ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Details of PDFactor models. serves as conditioning to regress dimension-wise scale and shift parameters \alpha , \gamma and \beta which are used to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. A subset of the evaluated 18 tasks in RLBench simulation and 6 tasks in the real world. where \ d elta \sim \mathcal ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Multi-task Performance on RLBench. We evaluate 25 episodes per task on 18 challenging tasks from RLBench and report mean and standard deviation of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation on denoising MLP depth. Inference speed is measured in FPS. 10 25 50 100 Demonstrations 0.4
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Scaling with demonstrations. We train PDFactor and RVT-2 for 18 tasks with an increasing number of demonstrations. ding. By replacing 2D standard ViT ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4. The data indicates that success rate improves as model size increases, demonstrating the scalability of the proposed method. Besides, as the number of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data. | embodiment, simulator version and control stack | p. 8 (4.4. Evaluation in the Real World), p. 6 (4.1. Experiment Setup) |
| Task/environment | Our experiments are conducted on a popular simulation benchmark RLBench [31] which is built upon the CoppelaSim simulator. | reset, timeout, object/scene variation | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 2 (1. Introduction) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We evaluate 25 episodes per task on 18 challenging tasks from RLBench and report mean and standard deviation of success rates (%) across 5 ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study & Model Analysis) |
| Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, ... | definition/direction/unit from same section | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| We evaluate policies by task completion success rate, which is the proportion of execution trajectories that achieve the goal conditions specified in the language ... | definition/direction/unit from same section | p. 6 (4.1. Experiment Setup) |
| The data indicates that success rate improves as model size increases, demonstrating the scalability of the proposed method. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study & Model Analysis) |
| 0 10 20 30 40 50 60 70 80 Training Steps (k) 0.8 0.7 0.6 0.5 Success Rate Model PDFactor-2 PDFactor-B PDFactor-S PDFactor-T RVT-2 ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study & Model Analysis) |
| Figure 1. Policy Representations. (a) Explicit policy predicts a specific action distribution along the 3D space. (b) Implicit pol- icy, e.g., energy-based and diffusion-based ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For example, in place cups task, the agent is required to have comprehensive spatial understanding and long-horizon reasoning abilities to hang mugs on the ... | comparison identity and matched condition | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| We implement a vanilla baseline where we directly train a diffusion transformer conditioned on triplane features and instructions without utilizing score matching loss. | comparison identity and matched condition | p. 6 (4.3. Ablation Study & Model Analysis) |
| We evaluate the success rate and inference speed with different diffusion steps in comparison to state-of-the-art diffusion-based method. | comparison identity and matched condition | p. 8 (4.3. Ablation Study & Model Analysis) |
| PDFactor demonstrates faster convergence with a higher performance than previous state-of-the-art RVT-2. | comparison identity and matched condition | p. 8 (4.3. Ablation Study & Model Analysis) |
| Table 3. Ablation on denoising MLP depth. Inference speed is measured in FPS. 10 25 50 100 Demonstrations 0.4 | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct an ablation study to analyze the impact of several design choices for PDFactor and report results in Tab. | component/input/data sensitivity | p. 6 (4.3. Ablation Study & Model Analysis) |
| We implement a vanilla baseline where we directly train a diffusion transformer conditioned on triplane features and instructions without utilizing score matching loss. | component/input/data sensitivity | p. 6 (4.3. Ablation Study & Model Analysis) |
| Besides, we implement a variant by replacing feature projection with point renderer in RVT [21]. | component/input/data sensitivity | p. 7 (4.3. Ablation Study & Model Analysis) |
| Variants Planning Tools Long Rotation Motion Multimodal Precision Occlusion Avg. | component/input/data sensitivity | p. 8 (4.3. Ablation Study & Model Analysis) |
| Table 3. Ablation on denoising MLP depth. Inference speed is measured in FPS. 10 25 50 100 Demonstrations 0.4 | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation. | Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (Figure/Table caption), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Ablation Study & Model Analysis), p. 7 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis) |
| Primary metric/result | Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive PDF cue:** Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, the ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We evaluate 25 episodes per task on 18 challenging tasks from RLBench and report mean and standard deviation of success rates (%) across 5 random ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We train PDFactor and RVT-2 for 18 tasks with an increasing number of demonstrations. ding.
- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** We study the performance of PDFactor in learning manipulation tasks from real-world demonstrations across 6 tasks (i.e., put fruit, push buttons, stack cups, stack blocks, ...
- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** Each task is evaluated across 10 episodes.
- **p. 6 / 3. We aim to model their joint dis - extractive PDF cue:** A subset of the evaluated 18 tasks in RLBench simulation and 6 tasks in the real world. where \ d elta \sim \mathcal {N}(\mathbf {0},\mathbf ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future works could explore recent techniques on reducing diffusive sampling steps while maintaining optimal accuracy. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Policy Representations. (a) Explicit policy predicts a specific action distribution along the 3D space. (b) Implicit pol- icy, e.g., energy-based and diffusion-based ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. PDFactor Overview. The 3D point cloud reconstructed from the multi-view RGB-D images is first featurized and projected to three orthogonal views, which ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. A subset of the evaluated 18 tasks in RLBench simulation and 6 tasks in the real world. where \ d elta \sim ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | We observe that the average success rate drops by 9%, indicating the importance of feature projection to avoid visual occlusions. | p. 7 (4.3. Ablation Study & Model Analysis) |
| body limitation/failure cue | Variants Planning Tools Long Rotation Motion Multimodal Precision Occlusion Avg. | p. 8 (4.3. Ablation Study & Model Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employ AdamW [40] optimizer with an initial learning rate 2.5 \ times 10^{-4} and a cosine scheduler with warmup in the first 2k ... | p. 6 (4.1. Experiment Setup) |
| Compared with PDFactor, the performance of the vanilla diffusion transformer drops by 15.2%, and the inference time increases significantly, potentially attributed to the explicit ... | p. 6 (4.3. Ablation Study & Model Analysis) |
| Contrary to the prevailing assumption that diffusion-based policies are slower than non-diffusion policies, our model manages to achieve a significant decrease in inference time ... | p. 8 (4.3. Ablation Study & Model Analysis) |
| We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data. | p. 8 (4.4. Evaluation in the Real World) |
| A single-layer MLP can lead to competitive results with negligible parameters and inference time increasing. | p. 7 (4.3. Ablation Study & Model Analysis) |
| 5a, we observe that PDFactor reaches convergence within approximately 30K steps. | p. 7 (4.3. Ablation Study & Model Analysis) |
| At inference time, next keyframe action is sampled via a reverse diffusion process following DDPM: \m a t hbf | p. 5 (3. We aim to model their joint dis) |
| For language instruction \protect \mathbf {l}, we use pretrained CLIP language encoder [55] to extract a sequence of N_{t} tokens following previous works [21, ... | p. 4 (3.3. Tri-Perspective View Transformer) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future works could explore recent techniques on reducing diffusive sampling steps while maintaining optimal accuracy.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Policy Representations. (a) Explicit policy predicts a specific action distribution along the 3D space. (b) Implicit pol- icy, e.g., energy-based and diffusion-based models, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. PDFactor Overview. The 3D point cloud reconstructed from the multi-view RGB-D images is first featurized and projected to three orthogonal views, which are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. A subset of the evaluated 18 tasks in RLBench simulation and 6 tasks in the real world. where \ d elta \sim \mathcal ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We observe that the average success rate drops by 9%, indicating the importance of feature projection to avoid visual occlusions.
- **p. 8 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** Variants Planning Tools Long Rotation Motion Multimodal Precision Occlusion Avg.

- **PDF anchors reviewed:** datasets p. 8 (4.4. Evaluation in the Real World), p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 8 (4.4. Evaluation in the Real World), p. 7 (4.3. Ablation Study & Model Analysis), p. 7 (4.3. Ablation Study & Model Analysis), metrics p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Study & Model Analysis), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis), baselines p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis), p. 7 (Figure/Table caption), results p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (Figure/Table caption), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Ablation Study & Model Analysis), p. 7 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
