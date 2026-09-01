# Evaluation - ConceptFusion: Open-set Multimodal 3D Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.07241; PDF retrieval source: https://arxiv.org/pdf/2302.07241. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), p. 9 (Figure/Table caption), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can)): By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy.

## Evaluation Body Digest

- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** This real-world dataset comprises 3D scans of 78 commonly found household and office objects on a tabletop surface (see Fig.
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Zero-shot tabletop rearrangement: To evaluate the applicability of ConceptFusion to real-world robotic interaction, we conduct experiments on a zero-shot tabletop rearrangement task with a UR5e ...
- **p. 6 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Experimental setup: Our experimental benchmark comprises of sequences from multiple publicly available datasets, and sequences we collect.
- **p. 6 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The benchmark comprises 20 indoor (apartment-scale) scenes from ScanNet [61, 62], Replica [63], and self-captured sequences; 5 outdoor (urban driving) scenes; 20 indoor (tabletop) scenes ...
- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** This task is extremely challenging due to the versatility of objects present in the dataset, ranging from extremely small objects (e.g., a 4-gram sachet of ...
- **p. 10 / VI. OUTLOOK - extractive body cue:** In each scenario, the robot is equipped with the task of finding an object of interest that is not in its map, because it is ...
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The robot is provided with rearrangment goals involving novel objects.
- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The robot arm then computes a motion plan (using the AIRobot library [69]) to push the object to the specified target region (i.e., to the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. THE ConceptFusion APPROACH | EMPIRICAL / REAL-ROBOT OR HARDWARE | By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy. | p. 6 (IV. THE ConceptFusion APPROACH) |
| 4) What previously infeasible downstream use-cases can | EMPIRICAL / REAL-ROBOT OR HARDWARE | We see that, each component of the proposed method results in clear, significant improvement in performance. | p. 10 (4) What previously infeasible downstream use-cases can) |
| 4) What previously infeasible downstream use-cases can | EMPIRICAL / REAL-ROBOT OR HARDWARE | Here, we again observe that ConceptFusion outperforms other finetuned foundation models by a significant margin in terms of both 3D mIoU and detection accuracy. | p. 8 (4) What previously infeasible downstream use-cases can) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 10: Integration of a large-language model (LLM) based planner in-the-loop. We illustrate two scenarios from the AI2-THOR [65] interactive household simulator. The GenericLLM-Agent ... | p. 9 (Figure/Table caption) |
| 4) What previously infeasible downstream use-cases can | EMPIRICAL / REAL-ROBOT OR HARDWARE | The full system achieves the best performance. | p. 10 (4) What previously infeasible downstream use-cases can) |

## Dataset / Benchmark Role

- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** This real-world dataset comprises 3D scans of 78 commonly found household and office objects on a tabletop surface (see Fig.
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Zero-shot tabletop rearrangement: To evaluate the applicability of ConceptFusion to real-world robotic interaction, we conduct experiments on a zero-shot tabletop rearrangement task with a UR5e ...
- **p. 6 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Experimental setup: Our experimental benchmark comprises of sequences from multiple publicly available datasets, and sequences we collect.
- **p. 6 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The benchmark comprises 20 indoor (apartment-scale) scenes from ScanNet [61, 62], Replica [63], and self-captured sequences; 5 outdoor (urban driving) scenes; 20 indoor (tabletop) scenes ...
- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** This task is extremely challenging due to the versatility of objects present in the dataset, ranging from extremely small objects (e.g., a 4-gram sachet of ...
- **p. 10 / VI. OUTLOOK - extractive body cue:** In each scenario, the robot is equipped with the task of finding an object of interest that is not in its map, because it is ...
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The robot is provided with rearrangment goals involving novel objects.
- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The robot arm then computes a motion plan (using the AIRobot library [69]) to push the object to the specified target region (i.e., to the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: ConceptFusion presents an approach to build open-set multimodal 3D maps from RGB images and depth estimates from additional sources such as depth/stereo cameras ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: ConceptFusion constructs pixel-aligned features fP by: processing input images to generate generic (class-agnostic) object masks (regions) ri, computing a bounding box for each ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: For each image, the global (fG) and local (fL) features are fused to obtain our pixel-aligned features (f P ). Top-Left: We first ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Our approach to computing pixel-aligned features is adept at capturing long-tailed and fine-grained concepts. The plots to the right show the similarity scores ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: 3D spatial reasoning abilities: A key benefit of lifting foundation features to 3D is the ability to reason about spatial attributes. For example, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Sample sequences from the UnCoCo dataset we captured to evaluate long-tailed reasoning over open-set multimodal 3D maps. To the right, we show sample ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Text queries over ScanNet [61]: ConceptFusion is able to handle long-form text queries and accurately localize objects referenced by the query. In the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world tabletop rearrangement experiments. The robot is provided with rearrangment goals involving novel objects. (Top row) push goldfish to the right of the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This real-world dataset comprises 3D scans of 78 commonly found household and office objects on a tabletop surface (see Fig. | embodiment, simulator version and control stack | p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can) |
| Task/environment | Zero-shot tabletop rearrangement: To evaluate the applicability of ConceptFusion to real-world robotic interaction, we conduct experiments on a zero-shot tabletop rearrangement task with a ... | reset, timeout, object/scene variation | p. 8 (4) What previously infeasible downstream use-cases can), p. 6 (4) What previously infeasible downstream use-cases can) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Accuracy (%) IoU source-ambiguous Random 7.14% N/A AudioCLIP [8] 23.81% N/A ConceptFusion 64.29% 0.287 ecological Random 5.56% N/A AudioCLIP [8] 22.22% N/A ConceptFusion 66.67% ... | definition/direction/unit from same section | p. 6 (IV. THE ConceptFusion APPROACH) |
| Each entry showcases success rates over specific query types (25 queries per type). | definition/direction/unit from same section | p. 10 (VI. OUTLOOK) |
| 3D mIoU IoU >0.15 IoU >0.25 IoU >0.5 LSeg-3D 0.128 25% 16.66% 9.72% Supervised OpenSeg-3D 0.289 43.05% 36.11% 27.78% MaskCLIP-3D 0.091 25.97% 9.09% 1.30% ... | definition/direction/unit from same section | p. 6 (IV. THE ConceptFusion APPROACH) |
| Fig. 10: Integration of a large-language model (LLM) based planner in-the-loop. We illustrate two scenarios from the AI2-THOR [65] interactive household simulator. The GenericLLM-Agent ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| 10, while the GenericLLM-Agent is able to generate seemingly plausible subgoals to achieve the task, the lack of knowledge of the map inhibits its ... | definition/direction/unit from same section | p. 10 (VI. OUTLOOK) |
| Fig. 4: Our approach to computing pixel-aligned features is adept at capturing long-tailed and fine-grained concepts. The plots to the right show the similarity ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| For each technique evaluated, we report the 3D mean intersection-over-union (IoU) metric, and also detection accuracies at IoU thresholds of 0.15, 0.25, and 0.5. | definition/direction/unit from same section | p. 7 (4) What previously infeasible downstream use-cases can) |
| Here, we again observe that ConceptFusion outperforms other finetuned foundation models by a significant margin in terms of both 3D mIoU and detection accuracy. | definition/direction/unit from same section | p. 8 (4) What previously infeasible downstream use-cases can) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: Text queries over ScanNet [61]: ConceptFusion is able to handle long-form text queries and accurately localize objects referenced by the query. In ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| MaskCLIP is the closest zero-shot baseline; we outperform it by a large margin. | comparison identity and matched condition | p. 8 (4) What previously infeasible downstream use-cases can) |
| The results are presented in Table VII, and compared against a baseline approach that uses only the pointcloud obtained by backprojecting a single RGB-D ... | comparison identity and matched condition | p. 10 (VI. OUTLOOK) |
| We therefore implement two baseline approaches that leverage LSeg and OpenSeg features respectively, and apply our feature fusion technique to obtain | comparison identity and matched condition | p. 6 (4) What previously infeasible downstream use-cases can) |
| We see that ConceptFusion outperforms all other approaches by a significant margin. | comparison identity and matched condition | p. 7 (4) What previously infeasible downstream use-cases can) |
| Furthermore, ConceptFusion is competitive to privileged baselines for this task. | comparison identity and matched condition | p. 8 (4) What previously infeasible downstream use-cases can) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The "Remove uniqueness term..." variant fuses features computed from individual masks with those computed over the entire image, but does not account for mask ... | component/input/data sensitivity | p. 10 (4) What previously infeasible downstream use-cases can) |
| However, for all other results presented in this paperunless otherwise specified-the language queries are directly fed into the CLIP text encoder without any preprocessing. | component/input/data sensitivity | p. 6 (IV. THE ConceptFusion APPROACH) |
| By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy. | component/input/data sensitivity | p. 6 (IV. THE ConceptFusion APPROACH) |
| Ablation analyses Pixel-alignment design choices: We evaluate the design choices made in our pixel-alignment scheme on the Scan | component/input/data sensitivity | p. 9 (4) What previously infeasible downstream use-cases can) |
| Ablation performed on the Replica [63] dataset. | component/input/data sensitivity | p. 10 (VI. OUTLOOK) |
| 11: The zero-shot nature of our approach allows integration with newer off-the-shelf foundation models without the need for finetuning. | component/input/data sensitivity | p. 11 (VI. OUTLOOK) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local ... | By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), p. 9 (Figure/Table caption), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can) |
| Primary metric/result | We see that, each component of the proposed method results in clear, significant improvement in performance. | numeric claim only at cited anchor | p. 10 (4) What previously infeasible downstream use-cases can) |

- Numeric sentences retained from the body:
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Our odometry and mapping approaches run at frame-rate (15 Hz).
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** The pixel-aligned feature extraction processes run offline (10-15 seconds / image) on an NVIDIA RTX 3090 GPU.
- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Each image in this dataset has 3-5 objects; each object has one structured text query, and 540 unstructured text queries (freeform queries, crowdsourced from human ...
- **p. 10 / VI. OUTLOOK - extractive body cue:** Approach mAcc f-mIoU ConceptFusion (w/ Mask2Former [60]) 24.16 31.31 ConceptFusion (w/ SAM [57]) 31.53 38.70 spatial reasoning queries over 5 scenes from the ScanRefer validation ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Our odometry and mapping approaches run at frame-rate (15 Hz).
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** The pixel-aligned feature extraction processes run offline (10-15 seconds / image) on an NVIDIA RTX 3090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The GenericLLM-Agent fails to achieve the specified task since it does not have an explicit 3D map representation, devoiding the LLM of the requisite ... | p. 9 (4) What previously infeasible downstream use-cases can) |
| body limitation/failure cue | Limitations: The key limitations of our method are threefold. | p. 11 (VII. CONCLUSION) |
| body limitation/failure cue | Third, we anticipate ConceptFusion to inherit the limitations and biases of foundation models [5, 75], warranting further investigations for potential harm as well as ... | p. 11 (VII. CONCLUSION) |
| body limitation/failure cue | As investigated in [82, 83, 73], CLIP does not inherently capture spatial relationships or compositions. | p. 12 (VII. CONCLUSION) |
| body limitation/failure cue | However, this approach still fails for room-level containment queries of type is <OBJ> in <ROOM>); which require additional context. | p. 10 (VI. OUTLOOK) |
| body limitation/failure cue | The "Remove uniqueness term..." variant fuses features computed from individual masks with those computed over the entire image, but does not account for mask ... | p. 10 (4) What previously infeasible downstream use-cases can) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 1) Text query: qtext is computed using the corresponding CLIP text encoder Ftext. | p. 5 (IV. THE ConceptFusion APPROACH) |
| The pixel-aligned feature extraction processes run offline (10-15 seconds / image) on an NVIDIA RTX 3090 GPU. | p. 6 (IV. THE ConceptFusion APPROACH) |
| We refer to the appendix for hyperparameter values and more details. | p. 4 (IV. THE ConceptFusion APPROACH) |
| IV-B, we compute the semantic context embedding fP u,v,t ∈fP Xt for each pixel in the input image Xt. | p. 4 (IV. THE ConceptFusion APPROACH) |
| 3) Image query: qimage is computed as the image-level CLIP embedding of the query image. | p. 5 (IV. THE ConceptFusion APPROACH) |
| Our odometry and mapping approaches run at frame-rate (15 Hz). | p. 6 (IV. THE ConceptFusion APPROACH) |
| In some trials, the object set also includes distractors placed to hamper perception and/or manipulation planning. | p. 8 (4) What previously infeasible downstream use-cases can) |
| Of the approaches presented here, LSeg requires per-pixel CLIP features as labels, OpenSeg leverages per-image captions for labels, and CLIPSeg trains a shallow decoder ... | p. 8 (4) What previously infeasible downstream use-cases can) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The GenericLLM-Agent fails to achieve the specified task since it does not have an explicit 3D map representation, devoiding the LLM of the requisite context ...
- **p. 11 / VII. CONCLUSION - extractive body cue:** Limitations: The key limitations of our method are threefold.
- **p. 11 / VII. CONCLUSION - extractive body cue:** Third, we anticipate ConceptFusion to inherit the limitations and biases of foundation models [5, 75], warranting further investigations for potential harm as well as research ...
- **p. 12 / VII. CONCLUSION - extractive body cue:** As investigated in [82, 83, 73], CLIP does not inherently capture spatial relationships or compositions.
- **p. 10 / VI. OUTLOOK - extractive body cue:** However, this approach still fails for room-level containment queries of type is <OBJ> in <ROOM>); which require additional context.
- **p. 10 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The "Remove uniqueness term..." variant fuses features computed from individual masks with those computed over the entire image, but does not account for mask uniqueness ...

- **PDF anchors reviewed:** datasets p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), p. 6 (4) What previously infeasible downstream use-cases can), p. 6 (4) What previously infeasible downstream use-cases can), p. 7 (4) What previously infeasible downstream use-cases can), p. 10 (VI. OUTLOOK), metrics p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (VI. OUTLOOK), p. 6 (IV. THE ConceptFusion APPROACH), p. 9 (Figure/Table caption), p. 10 (VI. OUTLOOK), p. 4 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 8 (4) What previously infeasible downstream use-cases can), p. 10 (VI. OUTLOOK), p. 6 (4) What previously infeasible downstream use-cases can), p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), results p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), p. 9 (Figure/Table caption), p. 10 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
