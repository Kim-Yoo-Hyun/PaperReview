# Evaluation - SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 6 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 1 (Figure/Table caption)): Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%).

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** We use two popular benchmark datasets to evaluate our 3DVG approach.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** ScanRefer [5] provides 51,500 natural language descriptions across 800 ScanNet scenes, each specifying a target object's spatial context.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Finally, high-quality rendering provides clearer information about object boundaries, textures, and colors, helping models more accurately identify and distinguish objects, Our current use of point ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** 2 shows the performance of different approaches on the Nr3D dataset, in which the ground-truth instance mask is also provided.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Static views - Center2Corner, Edge2Center, and Corner2Center - lack flexibility and struggle in complex scenes.
- **p. 7 / 4.2. Comparative Study - extractive body cue:** Ablation study on different components in our framework on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; "FAM": Fusion Alignment ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential for ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This result underscores the importance of flexible and context-aware view selection strategy in 3D scene understanding.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparative Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%). | p. 7 (4.2. Comparative Study) |
| 4.2. Comparative Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential ... | p. 7 (4.2. Comparative Study) |
| 4.2. Comparative Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving competitive results ... | p. 6 (4.2. Comparative Study) |
| 4.3. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | By dynamically adjusting perspective based on the query, our method shows consistent improvement, particularly in "Hard" (4.4%) and "Dependent" (5.7%). | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | To assess the potential limitations of our framework and guide future improvements, we conducted an error analysis on 185 randomly selected samples across 10 ... | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** We use two popular benchmark datasets to evaluate our 3DVG approach.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** ScanRefer [5] provides 51,500 natural language descriptions across 800 ScanNet scenes, each specifying a target object's spatial context.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Finally, high-quality rendering provides clearer information about object boundaries, textures, and colors, helping models more accurately identify and distinguish objects, Our current use of point ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** 2 shows the performance of different approaches on the Nr3D dataset, in which the ground-truth instance mask is also provided.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Static views - Center2Corner, Edge2Center, and Corner2Center - lack flexibility and struggle in complex scenes.
- **p. 7 / 4.2. Comparative Study - extractive body cue:** Ablation study on different components in our framework on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; "FAM": Fusion Alignment ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Effectiveness of SeeGround: Different from previous SoTA, our method associates 2D visual cues - color, texture, viewpoint, spatial position, orientation, and state - ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Illustrative example of different perspective selection strategies. Our "Query-Aligned" method dynamically adapts the viewpoint to match the spatial context of the query, enhancing ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Visualization of scene details from different viewpoints. The Bird's Eye View (a) captures the entire scene layout but lacks object-specific detail, while the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluations of 3DVG on ScanRefer [5] validation set. Results are reported for "Unique" (scenes with a single target object) and "Multiple" (scenes with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Performance on Nr3D [1] validation set. Queries are la- beled as "Easy" (one distractor) or "Hard" (multiple distractors), and as "View-Dependent" or "View-Independent" ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative Results. Rendered images are presented, including the incorrectly identified objects (Orange) and correctly identified objects (Green). Key visual cues are underlined.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on different components in our frame- work on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use two popular benchmark datasets to evaluate our 3DVG approach. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Task/environment | ScanRefer [5] provides 51,500 natural language descriptions across 800 ScanNet scenes, each specifying a target object's spatial context. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Methodology), p. 4 (3.1. Multimodal 3D Representation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential ... | definition/direction/unit from same section | p. 7 (4.2. Comparative Study) |
| This result underscores the importance of flexible and context-aware view selection strategy in 3D scene understanding. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| These results demonstrate that our method maintains high accuracy with partial text, underscoring the importance of 43% 24% 12% 12% 9% Rel. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| 3(a)) provides the basic location of objects but achieves low accuracy. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Nr3D [1], part of ReferIt3D, includes 41, 503 queries, collected via a two-player reference game to enhance description precision. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3. Illustrative example of different perspective selection strategies. Our "Query-Aligned" method dynamically adapts the viewpoint to match the spatial context of the query, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 2. Performance on Nr3D [1] validation set. Queries are la- beled as "Easy" (one distractor) or "Hard" (multiple distractors), and as "View-Dependent" or ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving competitive results ... | comparison identity and matched condition | p. 6 (4.2. Comparative Study) |
| Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%). | comparison identity and matched condition | p. 7 (4.2. Comparative Study) |
| Using the same model, our approach outperforms ZSVG3D across all difficulty levels, confirming its effectiveness independently of model choice. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| Figure 3. Illustrative example of different perspective selection strategies. Our "Query-Aligned" method dynamically adapts the viewpoint to match the spatial context of the query, ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Ablation studies are conducted on the Nr3D validation set [1]. | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| In contrast, LLM performance degrades without the anchor. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on different components in our framework on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; "FAM": Fusion ... | component/input/data sensitivity | p. 7 (4.2. Comparative Study) |
| Ablation studies are conducted on the Nr3D validation set [1]. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| Ablation study on using (a) different projection methods (ours vs. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| In contrast, LLM performance degrades without the anchor. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| Figure 7. An example of the robustness of the proposed frame- work in identifying the ‘cabinet' by leveraging visual context, even when key information ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG. | Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%). | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 6 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 1 (Figure/Table caption) |
| Primary metric/result | While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential ... | numeric claim only at cited anchor | p. 7 (4.2. Comparative Study) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** The camera captures images of the room at a resolution of 1000×1000 pixels, with the top 0.3 m of the scene excluded to account for ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Overall Center2Corner 49.5 31.4 35.1 42.9 40.2 Edege2Center 51.0 32.7 36.6 44.2 41.5 Corner2Center 49.8 33.4 35.5 44.5 41.3 Bird's Eye View 53.4 33.9 36.9 ...
- **p. 6 / 3.3. Fusion Alignment Module - extractive body cue:** Results are reported for "Unique" (scenes with a single target object) and "Multiple" (scenes with distractors of the same class) subsets, along with overall performance. ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual ... | p. 7 (4.3. Ablation Study) |
| body limitation/failure cue | Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation and height. | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | Current viewpoint selection strategies also fall short in handling complex scenarios like "when the window is on the left" or "upon entering from the ... | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Visualization of scene details from different viewpoints. The Bird's Eye View (a) captures the entire scene layout but lacks object-specific detail, while ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | In the Easy and Hard categories, our method reaches 54.5% and 38.3%, showing robustness across varying scene complexities. | p. 7 (4.2. Comparative Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our method is more robust than prior art. use ZSVG3D's program generation prompt with Qwen2VL, keeping other steps identical. | p. 8 (4.3. Ablation Study) |
| Additionally, the OLT enables the model to retrieve spatial information efficiently, avoiding complex spatial relationship calculations in later steps. | p. 3 (3.1. Multimodal 3D Representation) |
| The subsequent perspective selection steps then proceed as described earlier. | p. 5 (3.2. Perspective Adaptation Module) |
| These points are then projected onto the 2D image plane using the precomputed camera parameters Rc and Tc, and visual markers are placed at ... | p. 5 (3.3. Fusion Alignment Module) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Ablation Study - extractive body cue:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation and height.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Current viewpoint selection strategies also fall short in handling complex scenarios like "when the window is on the left" or "upon entering from the door".
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Visualization of scene details from different viewpoints. The Bird's Eye View (a) captures the entire scene layout but lacks object-specific detail, while the ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** In the Easy and Hard categories, our method reaches 54.5% and 38.3%, showing robustness across varying scene complexities.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 7 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 7 (4.2. Comparative Study), metrics p. 7 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 6 (4.1. Experimental Settings), p. 4 (Figure/Table caption), baselines p. 6 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 7 (4.3. Ablation Study), p. 5 (Figure/Table caption), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), results p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 6 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
