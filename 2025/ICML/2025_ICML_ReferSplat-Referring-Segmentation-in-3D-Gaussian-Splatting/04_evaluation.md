# Evaluation - ReferSplat: Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=reuShgiHdg; PDF retrieval source: https://openreview.net/pdf/646ff3c7806367b3d28461db1cfc8b52b4856ec6.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study)): Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024).

## Evaluation Body Digest

- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** The following ablation studies are conducted on the ramen and kitchen scenes on the Ref-LERF dataset.
- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** This demonstrates that Ref-LERF places a stronger emphasis on spatial reasoning and detailed object understanding compared to previous datasets.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We conduct experiments on the ramen scene from the Ref-LERF dataset using the same NVIDIA A6000 GPU to compare the computational cost of our ReferSplat ...
- **p. 8 / 4.4. Results on the Ref-LERF Dataset - extractive PDF cue:** R3DGS result on the Ref-LERF dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** 4, removing components fp,i and fp,w,i from Eq.7 results in performance dropping below the baseline, indicating that vanilla cross-attention alone is ineffective for our task.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** In contrast, alternative approaches-such as using the top-1 prediction, propagating the first-frame mask with SAM2 (Ravi et al., 2025), or selecting masks solely based on ...
- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** The average IoU (mIoU) is calculated between the masks rendered from the text response on the 3D Gaussians and the GT object masks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Ref-LERF Dataset and Evaluation Metrics (p. 6); 4.2. Implementation Details (p. 6); 4.4. Results on the Ref-LERF Dataset (p. 8); 4.5. 3D Open-Vocabulary Segmentation Result (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024). | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2 show that our method significantly outperforms all baselines, demonstrating that the proposed 3D Referring Feature Fields effectively models the relationship between 3D Gaussians ... | p. 7 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | When integrating all components (index 3), referred to as ReferSplat, we achieve a substantial performance gain, reaching a new state-of-the-art. | p. 7 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results show that BERT consistently outperforms CLIP. | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** The following ablation studies are conducted on the ramen and kitchen scenes on the Ref-LERF dataset.
- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** This demonstrates that Ref-LERF places a stronger emphasis on spatial reasoning and detailed object understanding compared to previous datasets.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We conduct experiments on the ramen scene from the Ref-LERF dataset using the same NVIDIA A6000 GPU to compare the computational cost of our ReferSplat ...
- **p. 8 / 4.4. Results on the Ref-LERF Dataset - extractive PDF cue:** R3DGS result on the Ref-LERF dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** 4, removing components fp,i and fp,w,i from Eq.7 results in performance dropping below the baseline, indicating that vanilla cross-attention alone is ineffective for our task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Referring 3D Gaussian Splatting Segmentation (R3DGS) aims at segmenting the target objects described by a given natural language descriptions within a 3D Gaussian ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 2021; Kirillov et al., 2023) as ground ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the proposed approach ReferSplat. Firstly, to infuse language-awareness into the 3D Gaussians, we introduce a new property called referring features, constructing ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Dataset analysis of our constructed Ref-LERF.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Ablation study on our method. PCMI, and GTCL de- note components of Position-aware Cross-Modal Interaction, and Gaussian-Text Contrastive Learning, respectively. Components
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study on Baseline Configuration.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study on Pseudo Mask Generation.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study on Cross-Modal Interaction Design.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes. | embodiment, simulator version and control stack | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study) |
| Task/environment | The following ablation studies are conducted on the ramen and kitchen scenes on the Ref-LERF dataset. | reset, timeout, object/scene variation | p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.3. 3D Gaussian Referring Fields), p. 4 (3.3. 3D Gaussian Referring Fields) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, alternative approaches-such as using the top-1 prediction, propagating the first-frame mask with SAM2 (Ravi et al., 2025), or selecting masks solely based ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| The average IoU (mIoU) is calculated between the masks rendered from the text response on the 3D Gaussians and the GT object masks. | definition/direction/unit from same section | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics) |
| These findings underscore our superiority. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Furthermore, as illustrated in Fig. | definition/direction/unit from same section | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics) |
| Therefore, our proposed method is crucial for accurate R3DGS. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Although this improves performance, it remains less effective than our attention-based position modeling. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Figure 3. Overview of the proposed approach ReferSplat. Firstly, to infuse language-awareness into the 3D Gaussians, we introduce a new property called referring features, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, which is our constructed Referring Feature Fields. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| 2 show that our method significantly outperforms all baselines, demonstrating that the proposed 3D Referring Feature Fields effectively models the relationship between 3D Gaussians ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| This demonstrates that Ref-LERF places a stronger emphasis on spatial reasoning and detailed object understanding compared to previous datasets. | comparison identity and matched condition | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics) |
| Results show that BERT consistently outperforms CLIP. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |
| ReferSplat outperforms 2D-based methods like Table 7. | comparison identity and matched condition | p. 8 (4.4. Results on the Ref-LERF Dataset) |
| Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 2021; Kirillov et al., 2023) as ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct ablation experiments to evaluate the effectiveness of different components. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| 4, removing components fp,i and fp,w,i from Eq.7 results in performance dropping below the baseline, indicating that vanilla cross-attention alone is ineffective for our ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| We study the effect of the referring feature dimension dr in Tab. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| Ablation study on number of feature dims. | component/input/data sensitivity | p. 8 (4.4. Results on the Ref-LERF Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), aims at segmenting objects in a 3D Gaussian scene ... | Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024). | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |
| Primary metric/result | 2 show that our method significantly outperforms all baselines, demonstrating that the proposed 3D Referring Feature Fields effectively models the relationship between 3D Gaussians ... | numeric claim only at cited anchor | p. 7 (4.3. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Ref-LERF Dataset and Evaluation Metrics - extractive PDF cue:** Each scene contains approximately five expressions per object, with 236 language descriptions used for training and 59 for testing, totaling 295 descriptions for 59 objects.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 2021; Kirillov et al., 2023) as ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | 1) Our current method does not account for dynamic factors, which are crucial for real-world applications. | p. 9 (6. Limitation and Future Work) |
| body limitation/failure cue | 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual grounding. | p. 9 (6. Limitation and Future Work) |
| body limitation/failure cue | Our 3D Gaussian Referring Fields enable the model to recognize occluded or non-visible objects by leveraging multi-view 3D scene knowledge-an inherent limitation of 2D-based ... | p. 8 (4.4. Results on the Ref-LERF Dataset) |
| body limitation/failure cue | Smaller dimensions (e.g., 1 or 4) lack the capacity to store discriminative features, while larger dimensions (e.g., 32) introduce redundancy and noise, degrading performance. | p. 8 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We optimize the Gaussian referring features for 45,000 iterations, using a learning rate of 0.0025, while other parameters, such as the MLP, are trained ... | p. 7 (4.2. Implementation Details) |
| ReferSplat also has the shortest training time, thanks to a lightweight preprocessing pipeline that avoids costly operations like language feature compression (LangSplat) or mask ... | p. 8 (4.3. Ablation Study) |
| Training is conducted on an NVIDIA RTX A6000 GPU. | p. 7 (4.2. Implementation Details) |
| Choice of Language Encoder. we conduct experiments comparing BERT and CLIP embeddings for language features in R3DGS in Tab. | p. 8 (4.3. Ablation Study) |
| In our framework, the referring feature encodes semantic and referring information, allowing us to compute the text response for each Gaussian by measuring similarity ... | p. 4 (3.3. 3D Gaussian Referring Fields) |
| 3.3, we extract word features fw and a sentence embedding fe from the referring expression Tl using a text encoder. | p. 3 (3.2. Problem Statement and Method Overview) |
| The color at a given pixel v, denoted as C(v), is computed by blending the contributions of all Gaussians according to their opacity. | p. 3 (3.1. Preliminaries) |
| The response on the 2D image plane at pixel v, denoted as M(v), serves as both the projected text response and the rendered segmentation ... | p. 4 (3.3. 3D Gaussian Referring Fields) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 2021; Kirillov et al., 2023) as ground ...
- **p. 9 / 6. Limitation and Future Work - extractive PDF cue:** 1) Our current method does not account for dynamic factors, which are crucial for real-world applications.
- **p. 9 / 6. Limitation and Future Work - extractive PDF cue:** 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual grounding.
- **p. 8 / 4.4. Results on the Ref-LERF Dataset - extractive PDF cue:** Our 3D Gaussian Referring Fields enable the model to recognize occluded or non-visible objects by leveraging multi-view 3D scene knowledge-an inherent limitation of 2D-based methods.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Smaller dimensions (e.g., 1 or 4) lack the capacity to store discriminative features, while larger dimensions (e.g., 32) introduce redundancy and noise, degrading performance.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 8 (4.3. Ablation Study), p. 8 (4.4. Results on the Ref-LERF Dataset), p. 7 (4.3. Ablation Study), metrics p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), baselines p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 8 (4.3. Ablation Study), p. 8 (4.4. Results on the Ref-LERF Dataset), p. 2 (Figure/Table caption), results p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
