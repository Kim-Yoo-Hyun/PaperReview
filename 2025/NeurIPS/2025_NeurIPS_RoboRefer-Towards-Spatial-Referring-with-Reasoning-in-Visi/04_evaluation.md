# Evaluation - RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (71 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ; PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption)): By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D boxes under occlusion in cluttered scenes, ...

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes.
- **p. 9 / 4 Experiments - extractive body cue:** 4.4 Simulator and Real-world Evaluation for Robotics RoboRefer can be integrated into the system as a useful tool.
- **p. 48 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Stage Categories Datasets SFT (D.A) Spatial RefSpatial (RGB-D) SFT (S.U.E) Spatial RefSpatial (RGB), RefSpatial (RGB-D), SAT [4], EmbSpatial [22] General COCO [150], GQA [18], OCR-VQA ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Single-step Spatial Understanding We evaluate on public single-step spatial understanding benchmarks, including CV-Bench [15], the BLINK [16] validation split, RoboSpatial [2] configuration part, SAT ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Multi-step Spatial Referring We first evaluate current robotic referring benchmarks, namely RoboRefIt [140] (location) and Where2Place [5]/RoboSpatial [2] (placement), all limited to 2 reasoning ...
- **p. 9 / 4 Experiments - extractive body cue:** Spatial referring from RoboRefer is crucial for real-world robots.
- **p. 10 / 4 Experiments - extractive body cue:** We also present RefSpatial, a large-scale, well-designed dataset for SFT and RFT training, with RefSpatial-Bench, a benchmark tailored to evaluate spatial referring.
- **p. 45 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** The RefSpatial-Bench benchmark evaluates spatial referring with reasoning in complex 3D indoor scenes through two tasks: Location Prediction and Placement Prediction, each comprising 100 samples.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); B Implementation Details and Samples of RefSpatial Dataset (p. 20); B Implementation Details and Samples of RefSpatial Dataset (p. 22); C Implementation Details and Samples of RefSpatial-Bench (p. 45).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D ... | p. 9 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model achieves comparable or slightly superior results, corroborating insights from SpatialVLM [6] and SpatialRGPT [1]. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results indicate that depth improves single-step spatial understanding, consistent with MM-Spatial [3], and yields greater gains in multi-step spatial referring. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For metrics, we report the average success rate of predicted points within the mask. | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes.
- **p. 9 / 4 Experiments - extractive body cue:** 4.4 Simulator and Real-world Evaluation for Robotics RoboRefer can be integrated into the system as a useful tool.
- **p. 48 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Stage Categories Datasets SFT (D.A) Spatial RefSpatial (RGB-D) SFT (S.U.E) Spatial RefSpatial (RGB), RefSpatial (RGB-D), SAT [4], EmbSpatial [22] General COCO [150], GQA [18], OCR-VQA ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Single-step Spatial Understanding We evaluate on public single-step spatial understanding benchmarks, including CV-Bench [15], the BLINK [16] validation split, RoboSpatial [2] configuration part, SAT ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Multi-step Spatial Referring We first evaluate current robotic referring benchmarks, namely RoboRefIt [140] (location) and Where2Place [5]/RoboSpatial [2] (placement), all limited to 2 reasoning ...
- **p. 9 / 4 Experiments - extractive body cue:** Spatial referring from RoboRefer is crucial for real-world robots.
- **p. 10 / 4 Experiments - extractive body cue:** We also present RefSpatial, a large-scale, well-designed dataset for SFT and RFT training, with RefSpatial-Bench, a benchmark tailored to evaluate spatial referring.
- **p. 45 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** The RefSpatial-Bench benchmark evaluates spatial referring with reasoning in complex 3D indoor scenes through two tasks: Location Prediction and Placement Prediction, each comprising 100 samples.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Spatial referring in complex 3D environments demands not only precise single-step spatial understanding but also multi-step spatial reasoning to resolve intricate references step-by-step, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of RoboRefer. RoboRefer can perform single-step precise spatial understanding from RGB(D) inputs with spatially constrained instructions (enabled by the SFT stage introducing ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: RefSpatial: 2.5M data samples from 2D/3D/Simulated sources, with 31 spatial relations. distinct spatial relations (See Fig. 3 (c)), fostering precise spatial understanding during ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance on the single-step spatial understanding benchmarks across different model types. Top-1 & Top-2 accuracies are represented using bold text, and underlines.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Performance on current referring and multi-step spatial referring benchmarks. L. and P. denote our benchmark's Location and Placement parts; U. indicates unseen compositional ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Performance on general referring benchmarks. B. and P. denote Bounding Box and Point. Top-1/2 accuracies are indicated by bold/underlined text.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Performance on general VLM benchmarks. We also show the advantage of dedicated depth encoder (E. = Encoder). We use the same evaluation protocol ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | 4.4 Simulator and Real-world Evaluation for Robotics RoboRefer can be integrated into the system as a useful tool. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 48 (C Implementation Details and Samples of RefSpatial-Bench) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Method), p. 7 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Method CV-Bench [15] BLINKval [16] RoboSpatial [2] SAT [4] EmbSpatial [22] 2D-Relation 3D-Depth 3D-Distance 2D-Relation 3D-Depth Qwen-2.5-VL-7B (base) 82.15 60.17 69.00 64.34 60.98 49.59 ... | definition/direction/unit from same section | p. 23 (B.1.1 Multi-Stage Image Filtering) |
| For metrics, we report the average success rate of predicted points within the mask. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest to the mug nearest 0.00 0.00 ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Table 10: We report the success rates (%) of real-world evaluation performance when using depth from DepthAnything V2 and Real Camera. Real-world Task Depth ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Process reward advances the accuracy of intermediate perception. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Below are examples to illustrate the expected format: • [Position] [the second largest cup]: [(0.245, 0.147)] • [Orientation] [the handle of the second largest ... | definition/direction/unit from same section | p. 50 (C Implementation Details and Samples of RefSpatial-Bench) |
| Figure 33: Map Visualization (RViz). E.4 Simulation Evaluation We use the same evaluation protocol of Open6DOR V2 introduced in SoFar [7], following the official ... | definition/direction/unit from same section | p. 52 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Though prior work[1] adopts a shared encoder, it (1) requires over twice as much RGBonly data compared to spatial-related data for co-training; (2) targets ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| 3, our method surpasses baselines, indicating that our dataset not only supports 3D spatial referring but also enhances 2D referring performance. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 4, we assess how spatial and depth information influences overall VQA performance by comparing RoboRefer-2B-SFT with the baseline NVILA-2B [38], trained on standard VQA ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Figure 7: Object detection comparison: Florence-2 (above), GroundingDINO+RAM (below) 3D-aware information Extraction. To further extract 3D-aware information from 2D images, we adopt UniDepth V2 ... | comparison identity and matched condition | p. 26 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess this, we fine-tune NVILA-2B [38] on RefSpatial without the depth encoder, followed by continued RFT. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Moreover, our 2B variant outperforms NVILA-2B by 21.7% (absolute). | component/input/data sensitivity | p. 8 (4 Experiments) |
| 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. | component/input/data sensitivity | p. 8 (4 Experiments) |
| These findings indicate that although VLMs often struggle with spatial reasoning, targeted spatial VQA training, especially with combined RGB and RGB-D data enriched by ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| 4.5 Ablation Study Table 7: Ablation Studies. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Table 2: Performance on current referring and multi-step spatial referring benchmarks. L. and P. denote our benchmark's Location and Placement parts; U. indicates unseen ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward ... | By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption) |
| Primary metric/result | Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** Over 70% requires multi-step reasoning (up to 5 steps), including precise ground-truth masks.
- **p. 9 / 4 Experiments - extractive body cue:** 5, integrating RoboRefer with an open-loop policy enables rapid updates at 2.5 Hz.
- **p. 45 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** The RefSpatial-Bench benchmark evaluates spatial referring with reasoning in complex 3D indoor scenes through two tasks: Location Prediction and Placement Prediction, each comprising 100 samples.
- **p. 45 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Moreover, to evaluate the effectiveness of the RFT training strategy, we further select 77 samples from these 200 samples and define it as the Unseen ...
- **p. 46 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Unseen Set: This set comprises 77 samples from the Location/Placement task, specifically designed to evaluate model generalization after SFT/RFT training on RefSpatial, as it includes ...
- **p. 46 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Empirically, we find that beyond 5 steps, additional qualifiers yield diminishing returns in narrowing the search space.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to ... | p. 52 (C Implementation Details and Samples of RefSpatial-Bench) |
| body limitation/failure cue | 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 I Licenses 54 | p. 21 (B.3.5 Question-Answer Pair Generation) |
| body limitation/failure cue | G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations. | p. 54 (C Implementation Details and Samples of RefSpatial-Bench) |
| body limitation/failure cue | 33 B.2.3 Addressing Limitations: Object Annotation and Bounding Box Filtering . . | p. 20 (B.2.2 Inherent Challenges and Limitations in CA-1M) |
| body limitation/failure cue | Thus, a failed match implies that the model cannot accurately refer to the object linguistically, and no reward is assigned. | p. 50 (C Implementation Details and Samples of RefSpatial-Bench) |
| body limitation/failure cue | B.2): This section outlines the 3D data selection process from CA1M [136], discusses its limitations and mitigation strategies, and presents methods for enriched scene ... | p. 22 (B Implementation Details and Samples of RefSpatial Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is conducted for two epochs with a batch size of 1 per GPU and 8 outputs in GRPO. | p. 49 (C Implementation Details and Samples of RefSpatial-Bench) |
| The 2B variant is trained with a batch size of 7 per GPU, and the 8B variant with 3, both for one epoch. | p. 48 (C Implementation Details and Samples of RefSpatial-Bench) |
| We use a batch size of 6 per GPU for the 2B model and 2 for the 8B model. | p. 49 (C Implementation Details and Samples of RefSpatial-Bench) |
| (All) 200 17.11 D Implementation Details for RoboRefer D.1 Architecture We adopt NVILA [38] as base model, including a visual encoder, an LLM, and ... | p. 47 (C Implementation Details and Samples of RefSpatial-Bench) |
| The reward is computed only for steps annotated as key steps in RefSpatial. | p. 50 (C Implementation Details and Samples of RefSpatial-Bench) |
| E Experimental Setting and Details E.1 Experiments Compute Resources We conduct experiments on an A100 GPU cluster, with each node equipped with 8 GPUs. | p. 50 (C Implementation Details and Samples of RefSpatial-Bench) |
| We employ a maximum learning rate of 1e-4, a weight decay of 0, and a warm-up ratio of 0.03. | p. 48 (C Implementation Details and Samples of RefSpatial-Bench) |
| We also show the advantage of dedicated depth encoder (E. = Encoder). | p. 8 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 52 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion ...
- **p. 21 / B.3.5 Question-Answer Pair Generation - extractive body cue:** 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 I Licenses 54
- **p. 54 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations.
- **p. 20 / B.2.2 Inherent Challenges and Limitations in CA-1M - extractive body cue:** 33 B.2.3 Addressing Limitations: Object Annotation and Bounding Box Filtering . .
- **p. 50 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Thus, a failed match implies that the model cannot accurately refer to the object linguistically, and no reward is assigned.
- **p. 22 / B Implementation Details and Samples of RefSpatial Dataset - extractive body cue:** B.2): This section outlines the 3D data selection process from CA1M [136], discusses its limitations and mitigation strategies, and presents methods for enriched scene graph ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 9 (4 Experiments), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), metrics p. 23 (B.1.1 Multi-Stage Image Filtering), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 23 (Figure/Table caption), p. 10 (4 Experiments), baselines p. 8 (4 Experiments), p. 10 (4 Experiments), p. 8 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 26 (Figure/Table caption), results p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (71 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT stage enables strong spatial understanding. ... (p. 8, Figure/Table caption).
- **Metric evidence:** Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest to the mug nearest 0.00 0.00 80.00 the camera and place it ... (p. 9, 4 Experiments).
- **Baseline/ablation evidence:** 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. (p. 8, 4 Experiments).
- **Failure/negative evidence:** Another major limitation of CA-1M is the lack of semantic labels for most annotated objects. (p. 34, B.2.2 Inherent Challenges and Limitations in CA-1M).
