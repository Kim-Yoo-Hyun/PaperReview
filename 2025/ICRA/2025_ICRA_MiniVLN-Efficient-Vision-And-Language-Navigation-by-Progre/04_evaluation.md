# Evaluation - MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.18800v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (Figure/Table caption)): 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL).

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** On the R2R datasets, the results, as shown in Figure 4, reveal that the non-distilled model achieves an SR of only 74.16 and an SPL ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Id Ablation Validation Seen Validation Unseen text pano fuse SR SPL SR SPL #1 ✓ ✓ ✓ 78.35 70.69 78.80 70.17 #2 ✓ ✓ 76.79 ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Method Validation Unseen Test Unseen Param(M)↓ SR↑ SPL↑ RGS↑ RGSPL↑ SR↑ SPL↑ RGS↑ RGSPL↑ HAMT [4] 32.95 30.20 18.92 17.28 30.40 26.67 14.88 13.08 170.39 ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** This dataset offers a challenging testbed for vision-and-language navigation tasks.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL).
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Remote Grounding Success (RGS) and its path-length penalized version (RGSPL) evaluate object localization accuracy.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** KDWeight Validation Seen Validation Unseen SR SPL SR SPL 0.01 76.30 69.49 76.76 67.89 0.1 78.35 70.69 78.80 70.17 1 76.98 69.78 78.20 69.94 Additionally, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. When ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL). | p. 5 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. ... | p. 1 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, these results are achieved with MiniVLN being only about one-ninth the size of the models listed in Table II. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Figure 5, the results indicate that MiniVLN achieves over three times the inference speed compared to the teacher model. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | On both datasets, MiniVLN exhibits an inference speed that is more than three times faster than ScaleVLN. improvement attained through our distillation approach. | p. 6 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** On the R2R datasets, the results, as shown in Figure 4, reveal that the non-distilled model achieves an SR of only 74.16 and an SPL ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Id Ablation Validation Seen Validation Unseen text pano fuse SR SPL SR SPL #1 ✓ ✓ ✓ 78.35 70.69 78.80 70.17 #2 ✓ ✓ 76.79 ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Method Validation Unseen Test Unseen Param(M)↓ SR↑ SPL↑ RGS↑ RGSPL↑ SR↑ SPL↑ RGS↑ RGSPL↑ HAMT [4] 32.95 30.20 18.92 17.28 30.40 26.67 14.88 13.08 170.39 ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** This dataset offers a challenging testbed for vision-and-language navigation tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. When ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. The overview of two-stage knowledge distillation process for VLN. In the pre-training phase, fine-grained knowledge is distilled, while navigation-specific knowledge is learned during ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Overall framework of MiniVLN. The yellow box represents the teacher model, while the blue box denotes the student model. The orange arrows represent ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Ablation of two-stage distillation on the R2R dataset. MiniVLN maintains performance comparable to the teacher model while achieving approximately 4% higher performance than ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. The inference time comparison between ScaleVLN and MiniVLN with CPU. On both datasets, MiniVLN exhibits an inference speed that is more than three ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the R2R datasets, the results, as shown in Figure 4, reveal that the non-distilled model achieves an SR of only 74.16 and an ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Task/environment | Id Ablation Validation Seen Validation Unseen text pano fuse SR SPL SR SPL #1 ✓ ✓ ✓ 78.35 70.69 78.80 70.17 #2 ✓ ✓ ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (IV. METHOD), p. 4 (IV. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL). | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Remote Grounding Success (RGS) and its path-length penalized version (RGSPL) evaluate object localization accuracy. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| KDWeight Validation Seen Validation Unseen SR SPL SR SPL 0.01 76.30 69.49 76.76 67.89 0.1 78.35 70.69 78.80 70.17 1 76.98 69.78 78.20 69.94 ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Id Pre-train Fine-tune Validation Unseen SR SPL RGS RGSPL #1 ✓ ✓ 54.30 42.02 35.16 27.06 #2 ✓ ✗ 54.13 38.64 31.89 22.93 #3 ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Fig. 2. The overview of two-stage knowledge distillation process for VLN. In the pre-training phase, fine-grained knowledge is distilled, while navigation-specific knowledge is learned ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| As shown in Figure 1, MiniVLN outperforms all previous state-of-theart (SoTA) methods on the R2R dataset, with only 12% (22M) of the parameters compared ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Comparisons with State-of-the-Arts 1) Results on R2R: As shown in Table I, in the test unseen setting, MiniVLN achieves a SR of 77.59 and ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| As shown in Figure 5, the results indicate that MiniVLN achieves over three times the inference speed compared to the teacher model. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Fig. 2. The overview of two-stage knowledge distillation process for VLN. In the pre-training phase, fine-grained knowledge is distilled, while navigation-specific knowledge is learned ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| The inference time comparison between ScaleVLN and MiniVLN with CPU. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, ablation experiments on the REVERIE dataset, detailed in Table III, illustrate the contributions of each stage of the distillation process, highlighting the effectiveness ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Ablation Study 1) The Effect of Two-Stage Distillation: To demonstrate the effectiveness of our two-stage distillation process, we conduct experiments using TinyBERT with the ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Method Validation Unseen Test Unseen Param(M)↓ SR↑ SPL↑ RGS↑ RGSPL↑ SR↑ SPL↑ RGS↑ RGSPL↑ HAMT [4] 32.95 30.20 18.92 17.28 30.40 26.67 14.88 13.08 ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Fig. 4. Ablation of two-stage distillation on the R2R dataset. MiniVLN maintains performance comparable to the teacher model while achieving approximately 4% higher performance ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Fig. 2. The overview of two-stage knowledge distillation process for VLN. In the pre-training phase, fine-grained knowledge is distilled, while navigation-specific knowledge is learned ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 3. Overall framework of MiniVLN. The yellow box represents the teacher model, while the blue box denotes the student model. The orange arrows ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • ... | 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL). | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Primary metric/result | Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The associated expert paths consist of six or seven nodes, covering a total distance of approximately 10 meters.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Agents follow 4 to 7 step trajectories and must select the correct object from predefined bounding boxes at the end of the path.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The inference time comparison between ScaleVLN and MiniVLN with CPU. | p. 6 (V. EXPERIMENTS) |
| Deployment To simulate deployment, we run the complete inference process of the model on the Intel i9-14900HX CPU of a mobile laptop. | p. 6 (V. EXPERIMENTS) |
| 3) Training Details: We trained on the R2R dataset for 200,000 iterations with a batch size of 16, and on the REVERIE dataset for ... | p. 5 (V. EXPERIMENTS) |
| Text Encoder Distillation The agent begins navigation by receiving a textual instruction I. | p. 4 (IV. METHOD) |
| Both the coarse- and finescale cross-model encoders include NX = 4 cross-model transformer blocks. | p. 4 (IV. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 3 (Figure/Table caption), baselines p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (Figure/Table caption), p. 6 (V. EXPERIMENTS), results p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
