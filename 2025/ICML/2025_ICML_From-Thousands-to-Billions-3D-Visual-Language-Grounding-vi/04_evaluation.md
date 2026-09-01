# Evaluation - From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=w8MCYYAvQD; PDF retrieval source: https://openreview.net/pdf/21179c3beadd60cefe77bfd16b2313dc4b83a1fe.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 2 (1. Introduction), p. 9 (Figure/Table caption)): Table 8: Comparison to 3D pseudolabels. A mask decoder trained on top of frozen LIFT-GS features matches and even outperforms a decoder trained on top of lifted 3D pseudolabels (voxel-pooled ...

## Evaluation Body Digest

- **p. 1 / 1. Introduction - extractive PDF cue:** Although this provides good generalization, performance degrades with more detailed descriptions typical of real-world queries, as illustrated in Figure 3.
- **p. 1 / Abstract - extractive PDF cue:** Remarkably, pretraining effectively multiplies finetuning datasets by 2×, demonstrating strong scaling properties that suggest 3D VLG currently operates in a severely data-scarce regime.
- **p. 2 / 1. Introduction - extractive PDF cue:** LIFT-GS achieves state-of-the-art performance on standard 3D VLG benchmarks, with 25.7% mAP on open-vocabulary instance segmentation (vs.
- **p. 2 / 1. Introduction - extractive PDF cue:** More importantly, we observe that across data scales for SFT, pretraining effectively "multiplies" the finetuning dataset by approximately a constant factor (2x).
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: 3D Referential Grounding. We report top-1 accuracy with various IoU thresholds (0.25, 0.5). SR3D NR3D ScanRefer
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at high ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Fine-tune Data Scaling. We show how Grounding Accuracy changes with increasing Data Ratio from 0.1 to 1.0. Finetuning Data Scaling We observe that ...
- **p. 2 / 1. Introduction - extractive PDF cue:** LIFT-GS shows using SAM, CLIP, and LLMs to generate 2D supervision. • State-of-the-art performance in realistic evaluations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 7); 4.2. Evaluation on 3D Vision-Language Grounding (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8: Comparison to 3D pseudolabels. A mask decoder trained on top of frozen LIFT-GS features matches and even outperforms a decoder trained on ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. It significantly outperforms its counterpart trained from scratch (LIFT-GS-Scratch mAP +3.2%). | p. 7 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs. | p. 1 (Abstract) |
| 1. Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | LIFT-GS achieves SOTA results using sensor point clouds common in embodied settings, with detailed ablations revealing scaling properties. | p. 2 (1. Introduction) |

## Dataset / Benchmark Role

- **p. 1 / 1. Introduction - extractive PDF cue:** Although this provides good generalization, performance degrades with more detailed descriptions typical of real-world queries, as illustrated in Figure 3.
- **p. 1 / Abstract - extractive PDF cue:** Remarkably, pretraining effectively multiplies finetuning datasets by 2×, demonstrating strong scaling properties that suggest 3D VLG currently operates in a severely data-scarce regime.
- **p. 2 / 1. Introduction - extractive PDF cue:** LIFT-GS achieves state-of-the-art performance on standard 3D VLG benchmarks, with 25.7% mAP on open-vocabulary instance segmentation (vs.
- **p. 2 / 1. Introduction - extractive PDF cue:** More importantly, we observe that across data scales for SFT, pretraining effectively "multiplies" the finetuning dataset by approximately a constant factor (2x).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: LIFT-GS Overview. We train a powerful 3D vision lan- guage grounding model (i.e., 3D mask decoder) with point clouds and language as inputs ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: 3D Referential Grounding. For each mentioned in- stance in a text description, predict a 3D mask and map it to corresponding text tokens. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: 3D grounding with CLIP-style (dual-decoder) method. Grounding heatmaps from a representative approach (Guo et al., 2024). Heatmaps are computed using dot product similarity ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4: SAM-CLIP Pseudo-Label Generation. We lever- age powerful 2D foundation models to generate pseudo language queries, i.e., CLIP embeddings, along with their corresponding ground-truth ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5: Architecture Design. LIFT-GS predicts 3D Gaussian Splatting G and 3D masks M given a point cloud P and language query embeddings Q as ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6: Zero-Shot 3D Segmentation. Trained using only 2D pseudo-labels, LIFT-GS can localize objects in 3D from real text inputs in a zero-shot manner. From ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Open-Vocabulary 3D Instance Segmentation. We evaluate our model on ScanNet200 by using category names as text queries and compare it against SOTA models.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. It significantly outperforms its counterpart trained from scratch (LIFT-GS-Scratch mAP +3.2%).

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Although this provides good generalization, performance degrades with more detailed descriptions typical of real-world queries, as illustrated in Figure 3. | embodiment, simulator version and control stack | p. 1 (1. Introduction), p. 1 (Abstract) |
| Task/environment | Remarkably, pretraining effectively multiplies finetuning datasets by 2×, demonstrating strong scaling properties that suggest 3D VLG currently operates in a severely data-scarce regime. | reset, timeout, object/scene variation | p. 1 (Abstract), p. 2 (1. Introduction) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Abstract), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: 3D Referential Grounding. We report top-1 accuracy with various IoU thresholds (0.25, 0.5). SR3D NR3D ScanRefer | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 7: Fine-tune Data Scaling. We show how Grounding Accuracy changes with increasing Data Ratio from 0.1 to 1.0. Finetuning Data Scaling We observe ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Although this provides good generalization, performance degrades with more detailed descriptions typical of real-world queries, as illustrated in Figure 3. | definition/direction/unit from same section | p. 1 (1. Introduction) |
| LIFT-GS shows using SAM, CLIP, and LLMs to generate 2D supervision. • State-of-the-art performance in realistic evaluations. | definition/direction/unit from same section | p. 2 (1. Introduction) |
| LIFT-GS achieves state-of-the-art performance on standard 3D VLG benchmarks, with 25.7% mAP on open-vocabulary instance segmentation (vs. | definition/direction/unit from same section | p. 2 (1. Introduction) |
| Figure 8: Finetunning Data Scaling on Open Vocabulary 3D Instance Segmentation. We show how mAP changes along with increasing Data Ratio from 0.1 to ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| [The] [bookshelf][near] [the] [table] [besides] [the] [wall] 3D Grounding Model 2D VLM Model 2D Grounding Loss 3D Segments Point Cloud Rendered Grounding Figure 1: ... | definition/direction/unit from same section | p. 1 (1. Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3: Comparison with other Pretraining Baseline. LIFT-GS clearly outperforms Ponder-v2 and its variant Ponder-v2†, which is trained on the same SAM-CLIP features as ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 8: Comparison to 3D pseudolabels. A mask decoder trained on top of frozen LIFT-GS features matches and even outperforms a decoder trained on ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs. | comparison identity and matched condition | p. 1 (Abstract) |
| LIFT-GS shows using SAM, CLIP, and LLMs to generate 2D supervision. • State-of-the-art performance in realistic evaluations. | comparison identity and matched condition | p. 2 (1. Introduction) |
| Table 1. It significantly outperforms its counterpart trained from scratch (LIFT-GS-Scratch mAP +3.2%). | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| LIFT-GS achieves SOTA results using sensor point clouds common in embodied settings, with detailed ablations revealing scaling properties. | comparison identity and matched condition | p. 2 (1. Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This somewhat counterintuitive observation indeed matches empirical data scaling laws for pretraining in other modalities (Hernandez et al., 2021), and the fact that this ... | component/input/data sensitivity | p. 2 (1. Introduction) |
| Table 3: Comparison with other Pretraining Baseline. LIFT-GS clearly outperforms Ponder-v2 and its variant Ponder-v2†, which is trained on the same SAM-CLIP features as ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Remarkably, pretraining effectively multiplies finetuning datasets by 2×, demonstrating strong scaling properties that suggest 3D VLG currently operates in a severely data-scarce regime. | component/input/data sensitivity | p. 1 (Abstract) |
| We train a powerful 3D vision language grounding model (i.e., 3D mask decoder) with point clouds and language as inputs by learning from 2D ... | component/input/data sensitivity | p. 1 (1. Introduction) |
| This approach could enable training 3D models without any 3D mask annotations. | component/input/data sensitivity | p. 2 (1. Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show how differentiable rendering enables training 3D models with 2D losses, eliminating dependence on scarce 3D annotations. • Demonstrating a pseudo-labeling strategy for ... | Table 8: Comparison to 3D pseudolabels. A mask decoder trained on top of frozen LIFT-GS features matches and even outperforms a decoder trained on ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 2 (1. Introduction), p. 9 (Figure/Table caption) |
| Primary metric/result | Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 2 / 1. Introduction - extractive PDF cue:** More importantly, we observe that across data scales for SFT, pretraining effectively "multiplies" the finetuning dataset by approximately a constant factor (2x).
- **p. 2 / 1. Introduction - extractive PDF cue:** More importantly, we observe that across data scales for SFT, pretraining effectively "multiplies" the finetuning dataset by approximately a constant factor (2x).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | From this perspective, the dual-encoder approach falls short of 3D grounding as it contradicts a core grounding requirement. | p. 1 (1. Introduction) |
| body limitation/failure cue | We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision. | p. 1 (Abstract) |
| body limitation/failure cue | Second, this allows us to overcome fundamental scaling limitations by training a large transformer decoder instead of previous dual-encoder approaches (as shown in Fig ... | p. 2 (1. Introduction) |
| body limitation/failure cue | Figure 3: 3D grounding with CLIP-style (dual-decoder) method. Grounding heatmaps from a representative approach (Guo et al., 2024). Heatmaps are computed using dot product ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Third, the approach is highly practical: LIFT-GS operates directly on raw point clouds from sensors, such as the outputs from SLAM or SfM systems, ... | p. 2 (1. Introduction) |
| From this perspective, the dual-encoder approach falls short of 3D grounding as it contradicts a core grounding requirement. | p. 1 (1. Introduction) |
| This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic. | p. 1 (Abstract) |
| Second, this allows us to overcome fundamental scaling limitations by training a large transformer decoder instead of previous dual-encoder approaches (as shown in Fig ... | p. 2 (1. Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / 1. Introduction - extractive PDF cue:** From this perspective, the dual-encoder approach falls short of 3D grounding as it contradicts a core grounding requirement.
- **p. 1 / Abstract - extractive PDF cue:** We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- **p. 2 / 1. Introduction - extractive PDF cue:** Second, this allows us to overcome fundamental scaling limitations by training a large transformer decoder instead of previous dual-encoder approaches (as shown in Fig 3) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: 3D grounding with CLIP-style (dual-decoder) method. Grounding heatmaps from a representative approach (Guo et al., 2024). Heatmaps are computed using dot product similarity ...

- **PDF anchors reviewed:** datasets p. 1 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), metrics p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), baselines p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 1 (Abstract), p. 2 (1. Introduction), p. 7 (Figure/Table caption), p. 2 (1. Introduction), results p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 2 (1. Introduction), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
