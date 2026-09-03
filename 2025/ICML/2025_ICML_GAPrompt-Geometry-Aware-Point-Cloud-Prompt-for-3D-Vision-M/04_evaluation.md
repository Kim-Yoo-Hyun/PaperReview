# Evaluation - GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4SsNofUQf1; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168191. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Quantitative Analysis), p. 7 (4.2. Quantitative Analysis), p. 8 (4.3. Ablation Study), p. 13 (Figure/Table caption), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study)): In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** The ScanObjectNN (Uy et al., 2019) is a highly challenging 3D dataset comprising 15K real-world objects across 15 categories.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The samples are drawn from the test split of the ScanObjectNN dataset, demonstrating its broad generalization capability across unseen data.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Note that our experiments on dataset ScanObjectNN sample 6
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The raw point clouds are noisy and scattered, reflecting the inherent complexity of real-world data.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Comparisons of PEFT methods from NLP and 2D Vision on the hardest variant of ScanObjectNN.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** ModelNet40 (Wu et al., 2015) comprises 12,311 pristine 3D CAD models across 40 categories, with complete, uniform, and noise-free point clouds that simplify the task.
- **p. 5 / 3.4. Analysis and Discussion - extractive body cue:** The objective of our method is to facilitate task-specific model adaptation through the integration of geometricaware prompt mechanisms.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Since voting (Liu et al., 2019) is time-consuming, we focus on reporting overall accuracy without it.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Quantitative Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | p. 7 (4.2. Quantitative Analysis) |
| 4.2. Quantitative Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, our method GAPrompt achieves the highest accuracy among all the parameter-efficient fine-tuning methods for 3D vision models. | p. 7 (4.2. Quantitative Analysis) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | This suggests that the Point Shift Prompter can enhance the geometric features of the point cloud at the input level, thereby contributing to improved ... | p. 8 (4.3. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10. Ablation study on different input for downstream head. C.2. Analysis on Adapter Enhancing Factor βa. As shown in Figure 8, we conduct ... | p. 13 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate the performance of our proposed GAPrompt on the point cloud classification task. | p. 6 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** The ScanObjectNN (Uy et al., 2019) is a highly challenging 3D dataset comprising 15K real-world objects across 15 categories.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The samples are drawn from the test split of the ScanObjectNN dataset, demonstrating its broad generalization capability across unseen data.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Note that our experiments on dataset ScanObjectNN sample 6
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The raw point clouds are noisy and scattered, reflecting the inherent complexity of real-world data.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Comparisons of PEFT methods from NLP and 2D Vision on the hardest variant of ScanObjectNN.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** ModelNet40 (Wu et al., 2015) comprises 12,311 pristine 3D CAD models across 40 categories, with complete, uniform, and noise-free point clouds that simplify the task.
- **p. 5 / 3.4. Analysis and Discussion - extractive body cue:** The objective of our method is to facilitate task-specific model adaptation through the integration of geometricaware prompt mechanisms.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our GAPrompt compares to full fine-tuning and existing PEFT methods. We compare the classification accuracy on the hardest variant of ScanObjectNN (Uy et ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Methods for adapting pre-trained 3D vision models. (a) Fine-tuning updates entire model parameters. (b) Prompt-based methods adapt the model to downstream tasks by ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The overall pipeline of GAPrompt. The raw input point clouds are processed by Point Shift Prompter, generating instance- specific shape features and shifted ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Classification on three variants of the ScanObjectNN and the ModelNet40, including the number of trainable parameters (Param) and overall accuracy (Acc). We report ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparisons of PEFT methods from NLP and 2D Vision on the hardest variant of ScanObjectNN.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. The effect of components in our GAPrompt. Point Prompt PS-Prompter Prompt Propagation Acc. ✓
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on Point Shift Prompter. Shift Head Prompt Enhance Adapter Enhance Acc. ✓
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Ablation study of Prompt Propagation mechanism and prompt enhancing factor βp. Effect of Point Shift Prompter Components. As shown in Table 4, we ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The ScanObjectNN (Uy et al., 2019) is a highly challenging 3D dataset comprising 15K real-world objects across 15 categories. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study) |
| Task/environment | The samples are drawn from the test split of the ScanObjectNN dataset, demonstrating its broad generalization capability across unseen data. | reset, timeout, object/scene variation | p. 8 (4.3. Ablation Study), p. 6 (4.1. Experimental Settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1. Point Prompt), p. 5 (3.2. Point Shift Prompter) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Since voting (Liu et al., 2019) is time-consuming, we focus on reporting overall accuracy without it. | definition/direction/unit from same section | p. 7 (4.1. Experimental Settings) |
| As shown in Table 1, our method GAPrompt achieves the highest accuracy among all the parameter-efficient fine-tuning methods for 3D vision models. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Analysis) |
| We visualize the attention scores of the [CLS] token to other point cloud tokens. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Basically, we only use the Shift Head to produce shifted point clouds as input for the encoder, attaining 88.23% accuracy. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Figure 9. The t-SNE visualizations from the test sets of ScanObjectNN (PB T50 RS) using a pre-trained Point-FEMAE with different tuning strategies. We extract ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1. Our GAPrompt compares to full fine-tuning and existing PEFT methods. We compare the classification accuracy on the hardest variant of ScanObjectNN (Uy ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Classification on three variants of the ScanObjectNN and the ModelNet40, including the number of trainable parameters (Param) and overall accuracy (Acc). | definition/direction/unit from same section | p. 6 (3.4. Analysis and Discussion) |
| We evaluate the performance of our proposed GAPrompt on the point cloud classification task. | definition/direction/unit from same section | p. 6 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | comparison identity and matched condition | p. 7 (4.2. Quantitative Analysis) |
| For a fair comparison, we employ identical data augmentation to the full fine-tuning method for each baseline. | comparison identity and matched condition | p. 6 (4. Experiments) |
| We utilize four pretrained models Point-MAE (Pang et al., 2022), ReCon (Qi et al., 2023), Point-GPT (Chen et al., 2024) and PointFEMAE (Zha et ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| Following baselines, we sample 1024 points per instance. | comparison identity and matched condition | p. 7 (4.1. Experimental Settings) |
| Ablation study of Prompt Propagation mechanism and prompt enhancing factor βp. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |
| As shown in Figure 4, we conduct ablation experiments on prompt propagation settings and prompt enhancing factor βp. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct ablation studies on the most challenging PB T50 RS variant based on Point-FEMAE to investigate the rationalization and effectiveness of our GAPrompt. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Figure 4. Ablation study of Prompt Propagation mechanism and prompt enhancing factor βp. Effect of Point Shift Prompter Components. As shown in Table 4, ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The effect of components in our GAPrompt. | component/input/data sensitivity | p. 7 (4.2. Quantitative Analysis) |
| Table 1. Classification on three variants of the ScanObjectNN and the ModelNet40, including the number of trainable parameters (Param) and overall accuracy (Acc). We ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 1. Our GAPrompt compares to full fine-tuning and existing PEFT methods. We compare the classification accuracy on the hardest variant of ScanObjectNN (Uy ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| The attention mechanism with prompt integration can be formally expressed as follows: oi = Attn.(WQhi, WKhi, WV hi), (17) ˆoi = Attn.(WQhi, WK[pi, hi], ... | component/input/data sensitivity | p. 5 (3.4. Analysis and Discussion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision ... | In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Quantitative Analysis), p. 7 (4.2. Quantitative Analysis), p. 8 (4.3. Ablation Study), p. 13 (Figure/Table caption), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study) |
| Primary metric/result | As shown in Table 1, our method GAPrompt achieves the highest accuracy among all the parameter-efficient fine-tuning methods for 3D vision models. | numeric claim only at cited anchor | p. 7 (4.2. Quantitative Analysis) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Point-MAE 22.1 85.18 Linear Probing 0.3 75.99 Prefix Tuning 0.7 77.72 VPT 0.4 81.09 Adapter Tuning 0.9 83.93 LoRA 0.9 81.74 SSF 0.4 82.58 AdapterFormer ...
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Following baselines, we sample 1024 points per instance.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The key distinction of our approach lies in the point-level operation, addressing the limitations of previous prompting 5 | p. 5 (3.4. Analysis and Discussion) |
| body limitation/failure cue | In contrast, IDPT, DAPT, and Point-PEFT fall short of full fine-tuning performance due to their limited ability to capture geometric information from point clouds. | p. 7 (4.2. Quantitative Analysis) |
| body limitation/failure cue | Figure 2. Methods for adapting pre-trained 3D vision models. (a) Fine-tuning updates entire model parameters. (b) Prompt-based methods adapt the model to downstream tasks ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | These objects consist of indoor scene data obtained by scanning, exhibiting characteristics such as cluttered backgrounds and occlusions. | p. 6 (4.1. Experimental Settings) |
| body limitation/failure cue | ModelNet40 (Wu et al., 2015) comprises 12,311 pristine 3D CAD models across 40 categories, with complete, uniform, and noise-free point clouds that simplify the ... | p. 7 (4.1. Experimental Settings) |
| body limitation/failure cue | Intuitively, it is because this setting brings more randomness and results in more robust convergence. | p. 8 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The hyperparameters are set as βa = 0.5, βp = 0.5 and P = 20. | p. 6 (4. Experiments) |
| Basically, we only use the Shift Head to produce shifted point clouds as input for the encoder, attaining 88.23% accuracy. | p. 8 (4.3. Ablation Study) |
| Following the original architecture of the pre-trained model, the prompted point cloud is encoded into Lt point tokens h1 by the token embedding module. | p. 4 (3.1. Point Prompt) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 3.4. Analysis and Discussion - extractive body cue:** The key distinction of our approach lies in the point-level operation, addressing the limitations of previous prompting 5
- **p. 7 / 4.2. Quantitative Analysis - extractive body cue:** In contrast, IDPT, DAPT, and Point-PEFT fall short of full fine-tuning performance due to their limited ability to capture geometric information from point clouds.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Methods for adapting pre-trained 3D vision models. (a) Fine-tuning updates entire model parameters. (b) Prompt-based methods adapt the model to downstream tasks by ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** These objects consist of indoor scene data obtained by scanning, exhibiting characteristics such as cluttered backgrounds and occlusions.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** ModelNet40 (Wu et al., 2015) comprises 12,311 pristine 3D CAD models across 40 categories, with complete, uniform, and noise-free point clouds that simplify the task.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Intuitively, it is because this setting brings more randomness and results in more robust convergence.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 7 (4.1. Experimental Settings), p. 7 (4.1. Experimental Settings), metrics p. 7 (4.1. Experimental Settings), p. 7 (4.2. Quantitative Analysis), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 13 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 7 (4.2. Quantitative Analysis), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), results p. 7 (4.2. Quantitative Analysis), p. 7 (4.2. Quantitative Analysis), p. 8 (4.3. Ablation Study), p. 13 (Figure/Table caption), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
