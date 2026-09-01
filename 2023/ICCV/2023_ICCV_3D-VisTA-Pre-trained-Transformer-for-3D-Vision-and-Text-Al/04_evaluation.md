# Evaluation - 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.04352; PDF retrieval source: https://arxiv.org/pdf/2308.04352. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 6 (5.1. Experimental Settings), p. 7 (5.2. Downstream Task Results), p. 7 (5.2. Downstream Task Results), p. 8 (Figure/Table caption), p. 8 (5.4. Qualitative Studies and Additional Results)): Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves competitive results with SOTA on Nr3D ...

## Evaluation Body Digest

- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** We evaluate our model on three datasets for this task: ScanRefer [8], Nr3D, and Sr3D [1].
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** On the ScanRefer dataset, we also incorporate PointGroup [28] for comparison with previous approaches.
- **p. 6 / 5.2. Downstream Task Results - extractive PDF cue:** Of note, 3DVisTA is trained on these datasets simply using the task losses, without any auxiliary losses or optimization tricks,
- **p. 8 / 5.4. Qualitative Studies and Additional Results - extractive PDF cue:** Besides, pre-training enhances the capability of aligning long text with 3D scenes, as evidenced by the larger improvement over longer queries in Fig.
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Mask3D significantly improves the grounding accuracy by providing more accurate object proposals.
- **p. 7 / 5.2. Downstream Task Results - extractive PDF cue:** Each entry denotes "test w/ object" / "test w/o object".
- **p. 7 / 5.2. Downstream Task Results - extractive PDF cue:** 3D-VisTA sets a new record for these 3D-VL tasks and may inspire future research on 3D-VL pre-training.
- **p. 8 / 5.4. Qualitative Studies and Additional Results - extractive PDF cue:** This is very helpful when the model needs to distinguish the target object from multiple instances of the same class.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Experimental Settings (p. 5); 5.2. Downstream Task Results (p. 6); 5.4. Qualitative Studies and Additional Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves ... | p. 6 (Figure/Table caption) |
| 5.1. Experimental Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | Mask3D significantly improves the grounding accuracy by providing more accurate object proposals. | p. 6 (5.1. Experimental Settings) |
| 5.2. Downstream Task Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Pre-training on ScanScribe significantly improves the performance of 3D-VisTA. | p. 7 (5.2. Downstream Task Results) |
| 5.2. Downstream Task Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Pretraining improves the results of most question types. | p. 7 (5.2. Downstream Task Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: The performance gap between scratch and pre-training over different sentence lengths (≤15, ≤30, > 30) in ScanRefer. of pre-training, even in the ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** We evaluate our model on three datasets for this task: ScanRefer [8], Nr3D, and Sr3D [1].
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** On the ScanRefer dataset, we also incorporate PointGroup [28] for comparison with previous approaches.
- **p. 6 / 5.2. Downstream Task Results - extractive PDF cue:** Of note, 3DVisTA is trained on these datasets simply using the task losses, without any auxiliary losses or optimization tricks,
- **p. 8 / 5.4. Qualitative Studies and Additional Results - extractive PDF cue:** Besides, pre-training enhances the capability of aligning long text with 3D scenes, as evidenced by the larger improvement over longer queries in Fig.
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Mask3D significantly improves the grounding accuracy by providing more accurate object proposals.
- **p. 7 / 5.2. Downstream Task Results - extractive PDF cue:** Each entry denotes "test w/ object" / "test w/o object".
- **p. 7 / 5.2. Downstream Task Results - extractive PDF cue:** 3D-VisTA sets a new record for these 3D-VL tasks and may inspire future research on 3D-VL pre-training.
- **p. 8 / 5.4. Qualitative Studies and Additional Results - extractive PDF cue:** This is very helpful when the model needs to distinguish the target object from multiple instances of the same class.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Overall framework of our 3D-VisTA pipeline. We col- lect diverse prompts, scene graphs, 3D scans, and objects to con- struct ScanScribe dataset. Through ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: The comparison between 3D-VisTA and other models w.r.t. tasks, auxiliary losses, and task-specific architectures."VG" stands for visual grounding, "QA" for question an- swering, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 2: The comparison between ScanScribe and other 3D-VL datasets. "VG" stands for Visual Grounding, "QA" for Question Answer- ing, "SR" for Situated Reasoning, and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The model architecture of our 3D-VisTA, which includes text encoding, scene encoding, and multi-modal fusion modules. 3D-VisTA is pre-trained by self-supervised learning objectives, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 3: The composition of ScanScribe. ∗We only use Objaverse to provide candidate object replacement for the 3D scenes in other two datasets; thus no ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves competitive ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5: Grounding accuracy (%) on ScanRefer with detected object proposals. "Det." represents the 3D object detection module used in the model. "VN" stands for ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 6: Captioning results on Scan2Cap dataset. "C" stands for "CIDEr", "B-4" for "BLEU-4", "M" for "METEOR", and "R" for "ROUGE", respectively. "@0.25" and "@0.5" ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our model on three datasets for this task: ScanRefer [8], Nr3D, and Sr3D [1]. | embodiment, simulator version and control stack | p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings) |
| Task/environment | On the ScanRefer dataset, we also incorporate PointGroup [28] for comparison with previous approaches. | reset, timeout, object/scene variation | p. 5 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.4. Self-supervised Pre-training), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Mask3D significantly improves the grounding accuracy by providing more accurate object proposals. | definition/direction/unit from same section | p. 6 (5.1. Experimental Settings) |
| For Nr3D/Sr3D, we follow ReferIt3D [1] to use ground-truth object masks and report the results as the grounding accuracy, i.e., whether the model correctly ... | definition/direction/unit from same section | p. 5 (5.1. Experimental Settings) |
| Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 3: The performance of finetuning 3D-VisTA using various amounts of training data. indicating that 3D-VisTA is a very simple yet effective architecture for ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5: The performance gap between scratch and pre-training over different sentence lengths (≤15, ≤30, > 30) in ScanRefer. of pre-training, even in the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 7: Answer accuracy on ScanQA using object proposals from Mask3D. Each entry denotes "test w/ object" / "test w/o object". | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 9: Ablation studies of 3D-VisTA w.r.t. Transformer depth, pre- training objectives, and pre-training data. We report the grounding accuracy on ScanRefer for Visual ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The learning rate is set to 1e-4, with a warmup of 3,000 steps, and cosine decay. | definition/direction/unit from same section | p. 5 (5.1. Experimental Settings) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3D-VisTA achieves competitive results with SOTA on Nr3D and outperforms SOTA on Sr3D. | comparison identity and matched condition | p. 6 (5.1. Experimental Settings) |
| In this section, we discuss the experimental results of the downstream tasks and compare the proposed 3D-VisTA model with the state-of-the-art (SOTA) methods. | comparison identity and matched condition | p. 6 (5.2. Downstream Task Results) |
| The pre-trained 3D-VisTA outperforms SOTA by a large margin. | comparison identity and matched condition | p. 7 (5.2. Downstream Task Results) |
| In ablation studies, we use ground-truth masks in all tasks for simplicity. | comparison identity and matched condition | p. 5 (5.1. Experimental Settings) |
| On the ScanRefer dataset, we also incorporate PointGroup [28] for comparison with previous approaches. | comparison identity and matched condition | p. 5 (5.1. Experimental Settings) |
| Table 2: The comparison between ScanScribe and other 3D-VL datasets. "VG" stands for Visual Grounding, "QA" for Question Answer- ing, "SR" for Situated Reasoning, ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In ablation studies, we use ground-truth masks in all tasks for simplicity. | component/input/data sensitivity | p. 5 (5.1. Experimental Settings) |
| Figure 2: The model architecture of our 3D-VisTA, which includes text encoding, scene encoding, and multi-modal fusion modules. 3D-VisTA is pre-trained by self-supervised learning ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Of note, 3DVisTA is trained on these datasets simply using the task losses, without any auxiliary losses or optimization tricks, | component/input/data sensitivity | p. 6 (5.2. Downstream Task Results) |
| Table 9: Ablation studies of 3D-VisTA w.r.t. Transformer depth, pre- training objectives, and pre-training data. We report the grounding accuracy on ScanRefer for Visual ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Both pre-training and fine-tuning are conducted on a single NVIDIA A100 80GB GPU. | component/input/data sensitivity | p. 5 (5.1. Experimental Settings) |
| Pretraining improves the results of most question types. | component/input/data sensitivity | p. 7 (5.2. Downstream Task Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text. | Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 6 (5.1. Experimental Settings), p. 7 (5.2. Downstream Task Results), p. 7 (5.2. Downstream Task Results), p. 8 (Figure/Table caption), p. 8 (5.4. Qualitative Studies and Additional Results) |
| Primary metric/result | Mask3D significantly improves the grounding accuracy by providing more accurate object proposals. | numeric claim only at cited anchor | p. 6 (5.1. Experimental Settings) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** The pre-training runs for 30 epochs with a batch size of 128.
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** The learning rate is set to 1e-4, with a warmup of 3,000 steps, and cosine decay.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The pre-training runs for 30 epochs with a batch size of 128. | p. 5 (5.1. Experimental Settings) |
| The learning rate is set to 1e-4, with a warmup of 3,000 steps, and cosine decay. | p. 5 (5.1. Experimental Settings) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results), p. 8 (5.4. Qualitative Studies and Additional Results), p. 6 (5.1. Experimental Settings), p. 7 (5.2. Downstream Task Results), metrics p. 6 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results), p. 7 (5.2. Downstream Task Results), p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings), p. 3 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 6 (5.1. Experimental Settings), p. 7 (5.2. Downstream Task Results), p. 7 (5.2. Downstream Task Results), p. 8 (Figure/Table caption), p. 8 (5.4. Qualitative Studies and Additional Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
