# Evaluation - GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mN49LupE8l; PDF retrieval source: https://openreview.net/pdf/57fa2e7334b7e5972b3c62c83d3aecf630a1f0e3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (A.1 NETWORK ARCHITECTURES), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): The efficacy of these features is demonstrated on the ScanNet benchmark, where they achieve 72.5% mIoU with linear probing, substantially outperforming 2D-lifted features from models like DINOv2 (63.1% mIoU).

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 2017), a large-scale dataset of over 1,500 RGB-D scans from diverse indoor environments, and Matterport3D (Chang et ...
- **p. 15 / A.2 DATASET DETAILS AND SUBSET SELECTION - extractive PDF cue:** For all experiments, we adhere to the official training, validation, and testing splits for the ScanNetV2 and Matterport3D datasets to ensure fair comparison with prior ...
- **p. 15 / A.2 DATASET DETAILS AND SUBSET SELECTION - extractive PDF cue:** To align with the categorical diversity of each dataset, the number of clusters K is set based on the variety of real-world spaces documented in ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As shown in Table 2, GeoPurify establishes a new stateof-the-art on long-tail benchmarks like ScanNet200 and the challenging M160 split.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** This strategy yields a training set that is not merely small but is a curated distillation of the dataset's core semantic diversity.
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate our method on three prominent 3D indoor scene understanding benchmarks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Method ScanNet200 Matterport40 Matterport80 Matterport160 f-mIoU f-mAcc mIoU mAcc mIoU mAcc mIoU mAcc PLA (Ding et al., 2023) 1.8 3.1 - - - - - ...
- **p. 14 / A.1 NETWORK ARCHITECTURES - extractive PDF cue:** We hypothesize that features learned via this multi-modal, multi-task objective provide richer semantic information for 3D scene understanding than those from networks trained solely on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5); A EXPERIMENTAL SETUP AND IMPLEMENTATION DETAILS (p. 14); A.2 DATASET DETAILS AND SUBSET SELECTION (p. 15); B ADDITIONAL QUANTITATIVE RESULTS (p. 16); B.1 PER-CLASS SEGMENTATION RESULTS (p. 16); B.2 CROSS-DATASET GENERALIZATION (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.1 NETWORK ARCHITECTURES | EMPIRICAL / REAL-ROBOT OR HARDWARE | The efficacy of these features is demonstrated on the ScanNet benchmark, where they achieve 72.5% mIoU with linear probing, substantially outperforming 2D-lifted features from ... | p. 14 (A.1 NETWORK ARCHITECTURES) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 3, GeoPurify significantly outperforms existing methods in both transfer directions. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Published as a conference paper at ICLR 2026 subset (∼1.5%), GeoPurify achieves competitive, and in some cases state-of-the-art, performance without requiring large-scale 3D semantic ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The advantage is even more pronounced in the mean Accuracy (mAcc) metric, where GeoPurify attains 72.5 on ScanNetV2 and 62.4 on Matterport3D, substantially outperforming ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 4, performance improves markedly from 10 to 20 9 | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 2017), a large-scale dataset of over 1,500 RGB-D scans from diverse indoor environments, and Matterport3D (Chang et ...
- **p. 15 / A.2 DATASET DETAILS AND SUBSET SELECTION - extractive PDF cue:** For all experiments, we adhere to the official training, validation, and testing splits for the ScanNetV2 and Matterport3D datasets to ensure fair comparison with prior ...
- **p. 15 / A.2 DATASET DETAILS AND SUBSET SELECTION - extractive PDF cue:** To align with the categorical diversity of each dataset, the number of clusters K is set based on the variety of real-world spaces documented in ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As shown in Table 2, GeoPurify establishes a new stateof-the-art on long-tail benchmarks like ScanNet200 and the challenging M160 split.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** This strategy yields a training set that is not merely small but is a curated distillation of the dataset's core semantic diversity.
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate our method on three prominent 3D indoor scene understanding benchmarks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Method ScanNet200 Matterport40 Matterport80 Matterport160 f-mIoU f-mAcc mIoU mAcc mIoU mAcc mIoU mAcc PLA (Ding et al., 2023) 1.8 3.1 - - - - - ...
- **p. 14 / A.1 NETWORK ARCHITECTURES - extractive PDF cue:** We hypothesize that features learned via this multi-modal, multi-task objective provide richer semantic information for 3D scene understanding than those from networks trained solely on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The Fundamental Disconnect: Semantic Richness vs. Geometric Coherence. Left: Original RGB 3D scene. Middle: Features distilled from 2D VLMs (Zou et al., 2023) ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: GeoPurify: A Data-Efficient Pipeline for Geometric Purification of 3D Semantic Features. Our method consists of two stages. 1) Training (left, dotted path): A ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results for open-vocabulary 3D semantic segmentation on ScanNetV2 and Matterport3D. We compare GeoPurify, trained with only ∼1.5% of the 3D data, against ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Zero-shot segmentation performance on long-tail benchmarks. We report key metrics (f-mIoU, f-mAcc) on ScanNet200 and (mIoU, mAcc) on frequency-based splits of Matterport3D (top ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Zero-shot cross-dataset evaluation. Models are trained on the source dataset and evalu- ated directly on the target without fine-tuning.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation studies of GeoPurify on the ScanNetV2 validation set. We analyze the impact of our core geometric purification module, the choice of 2D ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 5: Student Network Architecture (ϕS). The network operates on sparse 3D tensors. The feature dimension is maintained at 512 throughout the body. Stage Operator ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 6: Final scene and region IDs constituting our compact training subsets for ScanNetV2 and Matterport3D. ScanNetV2 Selected Scenes Matterport3D Selected Regions scene0126 00 VzqfbhrpDEA ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Published as a conference paper at ICLR 2026 2017), a large-scale dataset of over 1,500 RGB-D scans from diverse indoor environments, and Matterport3D (Chang ... | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| Task/environment | For all experiments, we adhere to the official training, validation, and testing splits for the ScanNetV2 and Matterport3D datasets to ensure fair comparison with ... | reset, timeout, object/scene variation | p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Finally, from each resulting cluster, we select the single most exemplary scene by ranking them with a composite score, S = Hc,norm + γ ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Figure 6: Illustration of typical failure modes. From left to right: challenges with the presence of over-smoothing artifacts at object boundaries, and inherited semantic ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| We follow the evaluation protocol established in CUAO3D (Li et al., 2025) and report mean Intersection-over-Union (mIoU) and mean Accuracy (mAcc). | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| The advantage is even more pronounced in the mean Accuracy (mAcc) metric, where GeoPurify attains 72.5 on ScanNetV2 and 62.4 on Matterport3D, substantially outperforming ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| This substantial gain underscores our central hypothesis: even with a powerful semantic backbone, projected features suffer from geometric fragmentation, and an explicit purification step ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 28: Sort Clusterj in descending order by s.score. | definition/direction/unit from same section | p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| The richness-complexity score weight is held constant at γ = 0.5. | definition/direction/unit from same section | p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| As shown in Table 1, GeoPurify demonstrates exceptional performance by leveraging a curated data subset of only ∼1.5%. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our data-efficient GeoPurify is compared against other zero-shot baselines. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Figure 5: Qualitative Comparison on ScanNetV2 and Matterport3D. Visual results on chal- lenging indoor scenes. From top to bottom: Input RGB point cloud, Ground ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Published as a conference paper at ICLR 2026 subset (∼1.5%), GeoPurify achieves competitive, and in some cases state-of-the-art, performance without requiring large-scale 3D semantic ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| A baseline that directly aggregates 2D features from the X-Decoder backbone without any geometric refinement achieves 50.2 mIoU. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| 4.2 QUANTITATIVE RESULTS We evaluate GeoPurify against state-of-the-art methods on open-vocabulary and long-tail 3D segmentation benchmarks. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| The advantage is even more pronounced in the mean Accuracy (mAcc) metric, where GeoPurify attains 72.5 on ScanNetV2 and 62.4 on Matterport3D, substantially outperforming ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Models are trained on the source dataset and evaluated directly on the target without fine-tuning. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Method ScanNetV2 →Matterport3D Matterport3D →ScanNetV2 mIoU (%) mAcc (%) mIoU (%) mAcc (%) OpenScene (Peng et al., 2023) 36.0 48.0 36.5 44.0 CUA-O3D (Li ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Once this compact subset is selected, the subsequent distillation training is performed without using any 3D semantic labels, relying only on the raw point ... | component/input/data sensitivity | p. 6 (4 EXPERIMENTS) |
| Standard methods typically attempt to learn entangled geo-semantic representations from scratch, failing to generalize without sufficient data. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 subset (∼1.5%), GeoPurify achieves competitive, and in some cases state-of-the-art, performance without requiring large-scale 3D semantic ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| A variant trained using only macro-negatives results in a 1.6 mIoU performance drop to 53.5 mIoU. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We introduce GeoPurify, a data-efficient framework built on the hypothesis that beyond their semantic richness, VLM-projected features also ... | The efficacy of these features is demonstrated on the ScanNet benchmark, where they achieve 72.5% mIoU with linear probing, substantially outperforming 2D-lifted features from ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (A.1 NETWORK ARCHITECTURES), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | As shown in Table 3, GeoPurify significantly outperforms existing methods in both transfer directions. | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** We sample a highly compact subset of original training data, comprising merely 20 scenes (∼1.6%) from ScanNetV2 and 20 scene regions (∼1.3%) from Matterport3D.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Once this compact subset is selected, the subsequent distillation training is performed without using any 3D semantic labels, relying only on the raw point cloud ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** The student network is trained for 50 epochs using the AdamW optimizer with a learning rate of 1 × 10-3, which is decayed using a ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** The advantage is particularly pronounced when transferring from Matterport3D →ScanNetV2, where our method achieves 54.9 mIoU, surpassing the next-best competitor by a large margin of ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Component Setting mIoU mAcc Geometric Purification w/o Purification (Aggregated 2D features) 50.2 68.1 + GeoPurify (Ours) 55.1 72.5 2D Semantic Backbone LSeg 48.6 61.6 LSeg ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Training Subset Size We evaluate the method's sensitivity to data quantity by training on subsets of 10, 20, 30, and 50 scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Illustration of typical failure modes. From left to right: challenges with the presence of over-smoothing artifacts at object boundaries, and inherited semantic ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | First, we filter for quality, culling any scene that falls below the median value for both richness (Nc) and complexity (Hc). | p. 6 (4 EXPERIMENTS) |
| body limitation/failure cue | Without them, the model learns the global scene layout but fails to disentangle co-located surfaces. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 1: The Fundamental Disconnect: Semantic Richness vs. Geometric Coherence. Left: Original RGB 3D scene. Middle: Features distilled from 2D VLMs (Zou et al., ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | We attribute this robustness to our decoupled design. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | This robust generalization arises from the synergy between our semantic and geometric modules. | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The student network is trained for 50 epochs using the AdamW optimizer with a learning rate of 1 × 10-3, which is decayed using ... | p. 6 (4 EXPERIMENTS) |
| All experiments are conducted on a single NVIDIA L40 GPU. | p. 6 (4 EXPERIMENTS) |
| Values in bold indicate the best result for each metric among the Zero-shot and Data-Efficient Zero-shot methods. †Denotes results from the original paper's LSeg-based ... | p. 7 (4 EXPERIMENTS) |
| During inference, the Geometry-Guided Pooling leverages this unbiased structural knowledge to propagate the VLM's semantic seeds across entire geometrically coherent instances. | p. 8 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 VLM provides a high semantic ceiling, generating descriptive "semantic seeds" even for rare objects where traditional ... | p. 8 (4 EXPERIMENTS) |
| A baseline that directly aggregates 2D features from the X-Decoder backbone without any geometric refinement achieves 50.2 mIoU. | p. 9 (4 EXPERIMENTS) |
| Each iteration F (t+1) = AF (t) propagates information by one hop, meaning a point's feature after T steps is influenced by its neighbors ... | p. 9 (4 EXPERIMENTS) |
| Our code and pre-trained models will be made publicly available upon publication. | p. 14 (A EXPERIMENTAL SETUP AND IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 6: Illustration of typical failure modes. From left to right: challenges with the presence of over-smoothing artifacts at object boundaries, and inherited semantic errors ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** First, we filter for quality, culling any scene that falls below the median value for both richness (Nc) and complexity (Hc).
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Without them, the model learns the global scene layout but fails to disentangle co-located surfaces.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The Fundamental Disconnect: Semantic Richness vs. Geometric Coherence. Left: Original RGB 3D scene. Middle: Features distilled from 2D VLMs (Zou et al., 2023) ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We attribute this robustness to our decoupled design.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** This robust generalization arises from the synergy between our semantic and geometric modules.

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), baselines p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), results p. 14 (A.1 NETWORK ARCHITECTURES), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
