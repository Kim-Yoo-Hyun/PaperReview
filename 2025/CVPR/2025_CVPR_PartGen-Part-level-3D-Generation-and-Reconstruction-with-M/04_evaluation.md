# Evaluation - PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation), p. 7 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction), p. 8 (4.4. Applications), p. 6 (Figure/Table caption)): Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object. This view is then processed ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** For all experiments, we use 100 held-out objects from the dataset described in Sec.
- **p. 8 / 4.4. Applications - extractive PDF cue:** Real-world 3D object decomposition.
- **p. 8 / 4.4. Applications - extractive PDF cue:** PartGen can also decompose real-world 3D objects.
- **p. 6 / 4.1. Part Segmentation - extractive PDF cue:** First, we fine-tune SAM2's mask decoder on our dataset, given the ground-truth masks and randomly selected seed points for different views.
- **p. 7 / 4.1. Part Segmentation - extractive PDF cue:** This is primarily because of the ambiguity of the segmentation task, which is better captured by our generator-based approach.
- **p. 7 / 4.2. Part completion and reconstruction - extractive PDF cue:** The latter is an important metric since the completion task is highly ambiguous, which motivates evaluating semantic similarity.
- **p. 7 / 4.1. Part Segmentation - extractive PDF cue:** We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J.
- **p. 6 / 4.1. Part Segmentation - extractive PDF cue:** We then match these segments to the ground-truth segments Mk and report mean Average Precision (mAP).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the ... | p. 4 (Figure/Table caption) |
| 4.1. Part Segmentation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J. | p. 7 (4.1. Part Segmentation) |
| 4.1. Part Segmentation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in the table, mAP results for our method are much higher than others, including SAM2 fine-tuned on our data. | p. 7 (4.1. Part Segmentation) |
| 4.2. Part completion and reconstruction | EMPIRICAL / REAL-ROBOT OR HARDWARE | We further provide qualitative results in Fig. | p. 8 (4.2. Part completion and reconstruction) |
| 4.4. Applications | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6, demonstrating that PartGen is successful in this case too. | p. 8 (4.4. Applications) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** For all experiments, we use 100 held-out objects from the dataset described in Sec.
- **p. 8 / 4.4. Applications - extractive PDF cue:** Real-world 3D object decomposition.
- **p. 8 / 4.4. Applications - extractive PDF cue:** PartGen can also decompose real-world 3D objects.
- **p. 6 / 4.1. Part Segmentation - extractive PDF cue:** First, we fine-tune SAM2's mask decoder on our dataset, given the ground-truth masks and randomly selected seed points for different views.
- **p. 7 / 4.1. Part Segmentation - extractive PDF cue:** This is primarily because of the ambiguity of the segmentation task, which is better captured by our generator-based approach.
- **p. 7 / 4.2. Part completion and reconstruction - extractive PDF cue:** The latter is an important metric since the completion task is highly ambiguous, which motivates evaluating semantic similarity.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce PartGen, a pipeline that generates compositional 3D objects similar to a human artist. It can start from text, an image, or ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Training data. We obtain a dataset of 3D objects de- composed into parts from artist-created assets. These come ‘natu- rally' segmented into parts ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Examples of automatic multi-view part segmentations. By running our method several times, we obtain diverse segmentations, covering the space of artist intents better ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Segmentation results. SAM2∗is fine-tuned on our data and SAM2† is fine-tuned for multi-view segmentation. Ours Sample 1 Ours Sample 2 Ours Sample 3 ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative results of part completion. The images with blue borders are the inputs. Our algorithm produces various plausible completions across different runs. Even ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Part completion results. We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J. Then, we evaluate 3D ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Examples of applications. PartGen can effectively generate or reconstruct 3D objects with meaningful and realistic parts in different scenarios: a) Part-aware text-to-3D generation; ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For all experiments, we use 100 held-out objects from the dataset described in Sec. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 8 (4.4. Applications) |
| Task/environment | Real-world 3D object decomposition. | reset, timeout, object/scene variation | p. 8 (4.4. Applications), p. 8 (4.4. Applications) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J. | definition/direction/unit from same section | p. 7 (4.1. Part Segmentation) |
| We then match these segments to the ground-truth segments Mk and report mean Average Precision (mAP). | definition/direction/unit from same section | p. 6 (4.1. Part Segmentation) |
| Both joint multi-view reasoning and contextual part completion are important for good performance. | definition/direction/unit from same section | p. 8 (4.2. Part completion and reconstruction) |
| 4.1) and part completion and reconstruction (Sec. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| View completion J 3D reconstruction S Method Compl. | definition/direction/unit from same section | p. 7 (4.1. Part Segmentation) |
| 6, demonstrating that PartGen is successful in this case too. | definition/direction/unit from same section | p. 8 (4.4. Applications) |
| Figure 1. We introduce PartGen, a pipeline that generates compositional 3D objects similar to a human artist. It can start from text, an image, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation. | comparison identity and matched condition | p. 6 (4.1. Part Segmentation) |
| The completion algorithm and its baselines are treated as a black box ˆJ = B(I ⊙M, I) that predicts the completed multi-view image ˆJ. | comparison identity and matched condition | p. 7 (4.2. Part completion and reconstruction) |
| Multi-view Context CLIP↑LPIPS↓ PSNR↑CLIP↑ LPIPS↓PSNR↑ Oracle ( ˆJ = J) GT - - 1.0 0.0 ∞ 0.957 0.027 18.91 PartGen ( ˆJ = B(I ... | comparison identity and matched condition | p. 7 (4.1. Part Segmentation) |
| 2, our model largely surpasses the baselines. | comparison identity and matched condition | p. 8 (4.2. Part completion and reconstruction) |
| We also compare to an oracle ( ˆJ = J), that uses complete groundtruth parts, providing the upper bound on part reconstruction performance, where ... | comparison identity and matched condition | p. 8 (4.2. Part completion and reconstruction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 7, a variant of our method enables effective editing of the shape and texture of parts based on textual prompts. | component/input/data sensitivity | p. 8 (4.4. Applications) |
| We then compare ˆL = S k Ψ( ˆJk) to the whole-object reconstruction ˆL = Ψ(I), i.e. without decomposing the object into parts, using ... | component/input/data sensitivity | p. 8 (4.3. Reassembling parts) |
| We fine-tune SAM2 in two different ways. | component/input/data sensitivity | p. 6 (4.1. Part Segmentation) |
| We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation. | component/input/data sensitivity | p. 6 (4.1. Part Segmentation) |
| As shown in the table, mAP results for our method are much higher than others, including SAM2 fine-tuned on our data. | component/input/data sensitivity | p. 7 (4.1. Part Segmentation) |
| Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively. | Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation), p. 7 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction), p. 8 (4.4. Applications), p. 6 (Figure/Table caption) |
| Primary metric/result | We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J. | numeric claim only at cited anchor | p. 7 (4.1. Part Segmentation) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Multi-view part segmentation - extractive PDF cue:** Given this mapping, we render the segmentation map as a multi-view RGB image C ∈[0, 1]3×2H×2W (Fig.
- **p. 5 / 3.5. Training data - extractive PDF cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 5 / 3.5. Training data - extractive PDF cue:** The segmentation diffusion network is trained on the dataset of pairs {(In, Mn)}N n=1, where the segmentation map M = [M k]S k=1 is a ...
- **p. 6 / 3.5. Training data - extractive PDF cue:** Automatic Seeded Method mAP50↑mAP75↑mAP50↑ mAP75↑ Part123 [40] 11.5 7.4 10.3 6.5 SAM2† [67] 20.3 11.8 24.6 13.1 SAM2∗[67] 37.4 27.0 44.2 30.1 SAM2 [67] 35.3 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, ... | p. 6 (4.1. Part Segmentation) |
| body limitation/failure cue | We then compare ˆJ to the ground-truth render J using Peak Signalto-Noise Ratio (PSNR) of the foreground pixels, Learned Perceptual Image Patch Similarity (LPIPS) ... | p. 7 (4.2. Part completion and reconstruction) |
| body limitation/failure cue | 6, PartGen can effectively generate 3D objects with distinct and completed parts, even in challenging cases with heavy occlusions, such as the gummy bear. | p. 8 (4.4. Applications) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| First, we fine-tune SAM2's mask decoder on our dataset, given the ground-truth masks and randomly selected seed points for different views. | p. 6 (4.1. Part Segmentation) |
| The other is seeded segmentation, where we assume that users provide a point as an additional input for a specific mask. | p. 6 (4.1. Part Segmentation) |
| For seeded segmentation, we simply return the regions that SAM2 outputs for the given seed point. | p. 7 (4.1. Part Segmentation) |
| For automatic segmentation, we seed SAM2 with a set of query points spread over the object, obtaining three different regions for each seed point. | p. 7 (4.1. Part Segmentation) |
| Detailed implementation of part reassembling is included in the sup. mat. | p. 8 (4.3. Reassembling parts) |
| Starting from the multi-view image I of a 3D object L, we run the segmentation algorithm to obtain segmentation ( ˆ M 1, . ... | p. 8 (4.3. Reassembling parts) |
| Then, we obtain Φseg by fine-tuning Φ to: (1) take as conditioning the multi-view image I, and (2) generate the color-coded multi-view segmentation map ... | p. 4 (3.2. Multi-view part segmentation) |
| To extract the segments at test time, we sample the colorcoded segmentation map C and simply quantize it based on the reference colors c1, ... | p. 4 (3.2. Multi-view part segmentation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Part Segmentation - extractive PDF cue:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the ...
- **p. 7 / 4.2. Part completion and reconstruction - extractive PDF cue:** We then compare ˆJ to the ground-truth render J using Peak Signalto-Noise Ratio (PSNR) of the foreground pixels, Learned Perceptual Image Patch Similarity (LPIPS) [97], ...
- **p. 8 / 4.4. Applications - extractive PDF cue:** 6, PartGen can effectively generate 3D objects with distinct and completed parts, even in challenging cases with heavy occlusions, such as the gummy bear.

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 8 (4.4. Applications), p. 8 (4.4. Applications), p. 6 (4.1. Part Segmentation), p. 7 (4.1. Part Segmentation), p. 7 (4.2. Part completion and reconstruction), metrics p. 7 (4.1. Part Segmentation), p. 6 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction), p. 6 (4. Experiments), p. 7 (4.1. Part Segmentation), p. 8 (4.4. Applications), baselines p. 6 (4.1. Part Segmentation), p. 7 (4.2. Part completion and reconstruction), p. 7 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction), p. 8 (4.2. Part completion and reconstruction), results p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation), p. 7 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction), p. 8 (4.4. Applications), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
