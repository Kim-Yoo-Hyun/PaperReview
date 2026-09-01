# Evaluation - ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings)): Quantitative results on Nr3D (Table 1) show that ViewSRD achieves a 5.2% accuracy gain over the best prior method, CoT3DRef, under identical settings.

## Evaluation Body Digest

- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors.
- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** ScanRefer [6] provides 51,583 free-form descriptions for 11,046 objects across 800 ScanNet scenes, incorporating spatial and attribute-level references to support 3DVG.
- **p. 7 / 4.3. Analysis of Anchors - extractive PDF cue:** Performance (%) of SRD module improves MVT [18], BUTD-DETR [21] and EDA [42] on ScanRefer [6] dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** We evaluate the effect of varying view counts on 3DVG performance using the Nr3D dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** To assess the contribution of each component within ViewSRD, we conducted detailed ablation studies on the Nr3D dataset [1].
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** LLM decoupler Accuracy OpenChat [40] 69.6% DeepSeek-R1 [28] 69.9% Qwen-Plus [46] 70.5% Qwen-Turbo [46] 70.7% views, performance improves from 64.4% (1 view) to 67.7% (2 ...
- **p. 7 / 4.3. Analysis of Anchors - extractive PDF cue:** Notably, our approach achieves higher accuracy in multianchor queries than in single-anchor ones, demonstrating that when properly processed, multi-anchor information enhances 3DVG performance rather than ...
- **p. 7 / 4.3. Analysis of Anchors - extractive PDF cue:** The results presented in Table 2 underscore the effectiveness of our approach, particularly in multi-anchor scenarios, where our method successfully disentangles spatial relationships by explicitly ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiment Settings (p. 6); 4.2. 3D Visual Grounding Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. 3D Visual Grounding Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitative results on Nr3D (Table 1) show that ViewSRD achieves a 5.2% accuracy gain over the best prior method, CoT3DRef, under identical settings. | p. 7 (4.2. 3D Visual Grounding Results) |
| 4.3. Analysis of Anchors | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, our approach achieves higher accuracy in multianchor queries than in single-anchor ones, demonstrating that when properly processed, multi-anchor information enhances 3DVG performance rather ... | p. 7 (4.3. Analysis of Anchors) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results indicate that as an LLM's ability to disentangle complex sentence structures improves, it becomes more effective at isolating and extracting relevant information, ... | p. 8 (4.5. Ablation Study) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | LLM decoupler Accuracy OpenChat [40] 69.6% DeepSeek-R1 [28] 69.9% Qwen-Plus [46] 70.5% Qwen-Turbo [46] 70.7% views, performance improves from 64.4% (1 view) to 67.7% ... | p. 8 (4.5. Ablation Study) |
| 4.1. Experiment Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | For Nr3D and Sr3D, grounding accuracy is measured by the percentage of correctly matched boxes [18, 36]. | p. 6 (4.1. Experiment Settings) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors.
- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** ScanRefer [6] provides 51,583 free-form descriptions for 11,046 objects across 800 ScanNet scenes, incorporating spatial and attribute-level references to support 3DVG.
- **p. 7 / 4.3. Analysis of Anchors - extractive PDF cue:** Performance (%) of SRD module improves MVT [18], BUTD-DETR [21] and EDA [42] on ScanRefer [6] dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** We evaluate the effect of varying view counts on 3DVG performance using the Nr3D dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** To assess the contribution of each component within ViewSRD, we conducted detailed ablation studies on the Nr3D dataset [1].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. (a) Previous 3DVG methods struggle with ambiguities from complex multi-anchor queries and perspective shifts. (b) ViewSRD addresses this by using the SRD module ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of ViewSRD. We begin by employing the Simple Relation Decoupling (SRD) module to decompose complex multi- anchor queries into multiple simpler single-anchor ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the SRD Module pipeline. tiple simpler single-anchor queries, enhancing the text en- coder's ability to comprehend and process relational infor- mation. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization Results of the 3D Visual Grounding Results. For the presented 3D scenes, we utilize green, red, blue, and yellow boxes to represent ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance (%) comparison on Nr3D [1] and Sr3D [1].
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance (%) comparison on Nr3D [1] with new cri- terions Multi-Anc and Single-Anc.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Performance (%) of SRD module improves MVT [18], BUTD-DETR [21] and EDA [42] on ScanRefer [6] dataset.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation studies on Nr3D [1]. All components contribute to final performance(%). Component Overall Easy Hard View Dep. View Indep.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors. | embodiment, simulator version and control stack | p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings) |
| Task/environment | ScanRefer [6] provides 51,583 free-form descriptions for 11,046 objects across 800 ScanNet scenes, incorporating spatial and attribute-level references to support 3DVG. | reset, timeout, object/scene variation | p. 6 (4.1. Experiment Settings), p. 7 (4.3. Analysis of Anchors) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| LLM decoupler Accuracy OpenChat [40] 69.6% DeepSeek-R1 [28] 69.9% Qwen-Plus [46] 70.5% Qwen-Turbo [46] 70.7% views, performance improves from 64.4% (1 view) to 67.7% ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Notably, our approach achieves higher accuracy in multianchor queries than in single-anchor ones, demonstrating that when properly processed, multi-anchor information enhances 3DVG performance rather ... | definition/direction/unit from same section | p. 7 (4.3. Analysis of Anchors) |
| The results presented in Table 2 underscore the effectiveness of our approach, particularly in multi-anchor scenarios, where our method successfully disentangles spatial relationships by ... | definition/direction/unit from same section | p. 7 (4.3. Analysis of Anchors) |
| For Nr3D and Sr3D, grounding accuracy is measured by the percentage of correctly matched boxes [18, 36]. | definition/direction/unit from same section | p. 6 (4.1. Experiment Settings) |
| Accuracy comparison when replacing different LLMs in SRD module on Nr3D [1]. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Figure 1. (a) Previous 3DVG methods struggle with ambiguities from complex multi-anchor queries and perspective shifts. (b) ViewSRD addresses this by using the SRD ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We use AdamW [30] with a learning rate of 0.0005. | definition/direction/unit from same section | p. 6 (4.1. Experiment Settings) |
| Figure 2. Overview of ViewSRD. We begin by employing the Simple Relation Decoupling (SRD) module to decompose complex multi- anchor queries into multiple simpler ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare ViewSRD with recent state-of-the-art approaches to evaluate its effectiveness on 3DVG. | comparison identity and matched condition | p. 6 (4.2. 3D Visual Grounding Results) |
| Under viewdependent evaluation, it further outperforms CoT3DRef by 6.7%, demonstrating the effectiveness of CCVTs in aligning textual and visual spaces and modeling viewpointsensitive relations ... | comparison identity and matched condition | p. 7 (4.2. 3D Visual Grounding Results) |
| In contrast, existing methods such as MVT [18] and CoT3DRef [2], which do not account for the necessity of spatial relationship decoupling, exhibit a ... | comparison identity and matched condition | p. 7 (4.3. Analysis of Anchors) |
| Ablation of view numbers on Nr3D [1]. | comparison identity and matched condition | p. 8 (4.4. SRD Enhances Other 3DVG Methods) |
| Accuracy comparison when replacing different LLMs in SRD module on Nr3D [1]. | comparison identity and matched condition | p. 8 (4.5. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess the contribution of each component within ViewSRD, we conducted detailed ablation studies on the Nr3D dataset [1]. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| We evaluate the effect of varying view counts on 3DVG performance using the Nr3D dataset. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| Moreover, under viewpoint shifts, CoT3DRef struggles to maintain alignment, whereas ViewSRD reliably grounds targets by capturing spatial relations invariant to viewpoint changes (e.g., "The ... | component/input/data sensitivity | p. 7 (4.2. 3D Visual Grounding Results) |
| This decoupling mechanism reduces ambiguity in multi-anchor descriptions, enhances target grounding, and serves as a model-independent preprocessing step, ensuring seamless compatibility with various 3DVG ... | component/input/data sensitivity | p. 7 (4.4. SRD Enhances Other 3DVG Methods) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively ... | Quantitative results on Nr3D (Table 1) show that ViewSRD achieves a 5.2% accuracy gain over the best prior method, CoT3DRef, under identical settings. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings) |
| Primary metric/result | Notably, our approach achieves higher accuracy in multianchor queries than in single-anchor ones, demonstrating that when properly processed, multi-anchor information enhances 3DVG performance rather ... | numeric claim only at cited anchor | p. 7 (4.3. Analysis of Anchors) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors.
- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** ScanRefer [6] provides 51,583 free-form descriptions for 11,046 objects across 800 ScanNet scenes, incorporating spatial and attribute-level references to support 3DVG.
- **p. 6 / 4.1. Experiment Settings - extractive PDF cue:** All experiments are implemented in PyTorch and run on a single RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation of ViewSRD is its assumption that complex queries can be fully decomposed without overlapping relationships. | p. 8 (5. Conclusion) |
| body limitation/failure cue | While the decomposition into overlapping relations does not degrade performance, it diminishes the intended benefits of simplification. | p. 8 (5. Conclusion) |
| body limitation/failure cue | These results confirm the robustness and generalizability of our approach across diverse scenario. | p. 7 (4.2. 3D Visual Grounding Results) |
| body limitation/failure cue | In contrast, ViewSRD correctly grounds targets by decomposing complex queries and leveraging robust spatial relationships between targetanchor pairs. | p. 7 (4.2. 3D Visual Grounding Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are implemented in PyTorch and run on a single RTX 4090 GPU. | p. 6 (4.1. Experiment Settings) |
| We use AdamW [30] with a learning rate of 0.0005. | p. 6 (4.1. Experiment Settings) |
| We take the average of these dot products across different sentences and compute a corresponding probability distribution using the softmax function. | p. 5 (3.3. Multi-view Textual-Scene Interaction Module) |
| To achieve this, we employ PointNet++ [35] as the scene encoder, computing scene features 𝐹𝑉𝑛for each viewpoint, where 𝑛∈𝑁denotes the scene index across 𝑁viewpoints. | p. 5 (3.3. Multi-view Textual-Scene Interaction Module) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** A limitation of ViewSRD is its assumption that complex queries can be fully decomposed without overlapping relationships.
- **p. 8 / 5. Conclusion - extractive PDF cue:** While the decomposition into overlapping relations does not degrade performance, it diminishes the intended benefits of simplification.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive PDF cue:** These results confirm the robustness and generalizability of our approach across diverse scenario.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive PDF cue:** In contrast, ViewSRD correctly grounds targets by decomposing complex queries and leveraging robust spatial relationships between targetanchor pairs.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings), p. 7 (4.3. Analysis of Anchors), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), metrics p. 8 (4.5. Ablation Study), p. 7 (4.3. Analysis of Anchors), p. 7 (4.3. Analysis of Anchors), p. 6 (4.1. Experiment Settings), p. 8 (4.5. Ablation Study), p. 1 (Figure/Table caption), baselines p. 6 (4.2. 3D Visual Grounding Results), p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors), p. 8 (4.4. SRD Enhances Other 3DVG Methods), p. 8 (4.5. Ablation Study), results p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
