# Evaluation - LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FKi6yjXwCN; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165205. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 20 (Figure/Table caption), p. 7 (4.1. How does LOCATE 3D compare to prior methods), p. 24 (Figure/Table caption), p. 6 (4.1. How does LOCATE 3D compare to prior methods)): Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details in Table 11).

## Evaluation Body Digest

- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: 39.9% ...
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** Method Evaluation Dataset ScanNet LX3D Joint Eval SN++ ARKitScenes FRE Baselines GPT-4o VLM 37.6∗ 60.5∗ 26.8 18.9 CF + 3D-Decoder 53.8 46.1 21.8 48.9 Ablations ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** We evaluate on the validation split of the benchmarks and report top-1 accuracy without assuming ground-truth object proposals.
- **p. 5 / 3. LOCATE 3D DATASET Overview - extractive body cue:** LOCATE 3D DATASET (L3DD) is a new human-annotated referring expression dataset covering ScanNet (Dai et al., 2017), ScanNet++ (v1) (Yeshwanth et al., 2023), and ARKitScenes ...
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** Over 80 percent of ARKitScenes and ScanNet++ validation split samples were validated at least three times, and samples were only included if a majority of ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D Table 1: Results on 3D language grounding in 3D mesh and sensor point clouds (PC).
- **p. 7 / 4.1. How does LOCATE 3D compare to prior methods - extractive body cue:** LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D Table 2: Ablation study of input features and encoder configurations.
- **p. 7 / 4.2. Understanding the impact of 3D-JEPA - extractive body cue:** On this task, 3D-JEPA outperforms ConceptFusion 39% to 34%.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. LOCATE 3D DATASET Overview (p. 5); 3.1. Dataset Statistics (p. 5); 3.2. Comparison with prior datasets (p. 5); 4. Experiments and Analysis (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Evaluating LOCATE 3D in novel environments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details ... | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| 4.4. Evaluating LOCATE 3D in novel environments | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: ... | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7: Impact of LX3D train data. We report accuracy @25 IoU. ARKitScenes column contains both pretrain and val split as we saw no ... | p. 20 (Figure/Table caption) |
| 4.1. How does LOCATE 3D compare to prior methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results demonstrate that CF features consistently outperform RGB, and encoder initialization with 3DJEPA yields the best performance. | p. 7 (4.1. How does LOCATE 3D compare to prior methods) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 10: Impact of scene diversity. We train all models on SR3D+NR3D+ScanRefer and add 30K samples from L3DD. We ablate whether these extra samples ... | p. 24 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: 39.9% ...
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** Method Evaluation Dataset ScanNet LX3D Joint Eval SN++ ARKitScenes FRE Baselines GPT-4o VLM 37.6∗ 60.5∗ 26.8 18.9 CF + 3D-Decoder 53.8 46.1 21.8 48.9 Ablations ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** We evaluate on the validation split of the benchmarks and report top-1 accuracy without assuming ground-truth object proposals.
- **p. 5 / 3. LOCATE 3D DATASET Overview - extractive body cue:** LOCATE 3D DATASET (L3DD) is a new human-annotated referring expression dataset covering ScanNet (Dai et al., 2017), ScanNet++ (v1) (Yeshwanth et al., 2023), and ARKitScenes ...
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** Over 80 percent of ARKitScenes and ScanNet++ validation split samples were validated at least three times, and samples were only included if a majority of ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D Table 1: Results on 3D language grounding in 3D mesh and sensor point clouds (PC).
- **p. 7 / 4.1. How does LOCATE 3D compare to prior methods - extractive body cue:** LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D Table 2: Ablation study of input features and encoder configurations.
- **p. 7 / 4.2. Understanding the impact of 3D-JEPA - extractive body cue:** On this task, 3D-JEPA outperforms ConceptFusion 39% to 34%.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overall Architecture of LOCATE 3D, which operates in three phases. In Phase 1: Preprocessing, we construct a point cloud with "lifted" features from ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: 3D-JEPA training framework: The context encoder computes latent features from a masked point cloud. Subsequently, a predictor operates on these latent features to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: In our language-conditioned 3D mask and bounding box decoder, 3D-JEPA features are jointly processed with text and learned query embeddings by n = ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Results on 3D language grounding in 3D mesh and sensor point clouds (PC). We evaluate top-1 accuracy on the validation set without any ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Ablation study of input features and encoder con- figurations. We compare different input modalities and encoder architectures. RGB refers to raw RGB features, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Impact of 2D foundation features on LOCATE 3D. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, NR3D, ScanRefer evaluation sets. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Generalization of LOCATE 3D. We report accuracy @25 IoU. Using lifted 2D foundation features consistently im- proves results compared to RGB features, and ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 4: Overview of different masking types

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: ... | embodiment, simulator version and control stack | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Task/environment | Method Evaluation Dataset ScanNet LX3D Joint Eval SN++ ARKitScenes FRE Baselines GPT-4o VLM 37.6∗ 60.5∗ 26.8 18.9 CF + 3D-Decoder 53.8 46.1 21.8 48.9 ... | reset, timeout, object/scene variation | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 6 (4. Experiments and Analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7: Impact of LX3D train data. We report accuracy @25 IoU. ARKitScenes column contains both pretrain and val split as we saw no ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 2: Ablation study of input features and encoder con- figurations. We compare different input modalities and encoder architectures. RGB refers to raw RGB ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 8: Impact of learning rate schedule on model performance. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, NR3D, and ScanRefer ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details ... | definition/direction/unit from same section | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Table 6: Impact of decoder size on performance. We evaluate accuracy (@25 and @50 IoU) on the Joint ScanNet benchmark across different decoder sizes ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 5: Ablation study on decoder supervision and bounding box prediction head architectures. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 3: Impact of 2D foundation features on LOCATE 3D. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, NR3D, ScanRefer evaluation ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4: Generalization of LOCATE 3D. We report accuracy @25 IoU. Using lifted 2D foundation features consistently im- proves results compared to RGB features, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Notably, LOCATE 3D outperforms both baselines across most metrics, showcasing the robustness of our approach. | comparison identity and matched condition | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details ... | comparison identity and matched condition | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Despite evaluating in this more stringent setting, our model (LOCATE 3D) achieves SoTA results, even when compared to prior work that operates under refined ... | comparison identity and matched condition | p. 6 (4.1. How does LOCATE 3D compare to prior methods) |
| Table 1: Results on 3D language grounding in 3D mesh and sensor point clouds (PC). We evaluate top-1 accuracy on the validation set without ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 12: Comparison of various ablations and baselines. Metrics shown as (@25, @50) for SN Joint, SR3D, NR3D, ScanRefer, SN++, and ARKitScenes. Input Features ... | comparison identity and matched condition | p. 27 (Figure/Table caption) |
| As shown in Table 9, L3DD significantly increases the scale of existing 3D RefExp data along two key axes when compared to prior data ... | comparison identity and matched condition | p. 5 (3.2. Comparison with prior datasets) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Ablation study on decoder supervision and bounding box prediction head architectures. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Section 4.3 presents ablation studies on various components of our architecture, and Section 4.4 evaluates generalization capabilities on novel environments and robotic deployment. | component/input/data sensitivity | p. 6 (4. Experiments and Analysis) |
| Our ablation studies reveal the key components enabling this strong generalization. | component/input/data sensitivity | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| We evaluate top-1 accuracy on the validation set without any assumption of ground-truth proposals. | component/input/data sensitivity | p. 6 (4. Experiments and Analysis) |
| To tease this apart, we trained variants of LOCATE 3D using different 2D foundation features. | component/input/data sensitivity | p. 7 (4.3. LOCATE 3D ablations) |
| We find that using larger models (CLIP-L, SAM-H) improves results over smaller variants (CLIP-B, MobileSAM), suggesting benefits from scaling. | component/input/data sensitivity | p. 7 (4.3. LOCATE 3D ablations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) ... | Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 20 (Figure/Table caption), p. 7 (4.1. How does LOCATE 3D compare to prior methods), p. 24 (Figure/Table caption), p. 6 (4.1. How does LOCATE 3D compare to prior methods) |
| Primary metric/result | First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: ... | numeric claim only at cited anchor | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |

- Numeric sentences retained from the body:
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** In total, our dataset contains 131,641 samples.
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** ScanNet: 30,135 new language annotations covering 550 venues and 5,527 objects for training.
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** 4,470 new language annotations covering 130 venues and 1038 objects for validation.
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** ScanNet++: 91,846 new language annotations covering 230 venues and 13,359 objects for training.
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** 3,774 new language annotations covering 50 venues and 1,303 objects for validation.
- **p. 5 / 3.1. Dataset Statistics - extractive body cue:** ARKitScenes: 991 new language annotations covering 293 venues and 1,862 objects covering scenes used for pretraining.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations We can utilize such caching because our benchmarks operate under static (ScanNet) or quasi-static (robot) environments. | p. 8 (4.5. Computational Analysis) |
| body limitation/failure cue | Figure 8: Learning rate schedule for encoder and decoder. Fine-tuning a pre-trained encoder alongside a randomly initialized decoder requires careful balancing to prevent unstable ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | This choice better represents realworld deployment scenarios though it typically results in performance degradation due to sensor noise, missing regions, and registration errors, as ... | p. 6 (4. Experiments and Analysis) |
| body limitation/failure cue | As outlined earlier, our model is capable of working with sensor streams and does not require human intervention at test time (e.g., for mesh ... | p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| body limitation/failure cue | Table 10: Impact of scene diversity. We train all models on SR3D+NR3D+ScanRefer and add 30K samples from L3DD. We ablate whether these extra samples ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Figure 12: Examples of the Spot robot at the end of navigation task before the pick task (right) the output bounding boxes of LOCATE ... | p. 25 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training ... | p. 5 (2.3.2. TRAINING LOCATE 3D) |
| Most prior work assumes access to refined meshes and mesh (object) region proposals at training and inference time. | p. 6 (4.1. How does LOCATE 3D compare to prior methods) |
| LOCATE 3D trains the language-conditioned 3D decoder from scratch and fine-tunes the 3D-JEPA pretrained PTv3 encoder. | p. 5 (2.3.2. TRAINING LOCATE 3D) |
| (SAM-) indicates masks computed with said model. | p. 7 (4.2. Understanding the impact of 3D-JEPA) |
| For each configuration, we train the same type of decoder. | p. 7 (4.2. Understanding the impact of 3D-JEPA) |
| What is the impact of scaling the decoder? | p. 8 (4.3. LOCATE 3D ablations) |
| We evaluate three different decoder sizes. | p. 8 (4.3. LOCATE 3D ablations) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.5. Computational Analysis - extractive body cue:** Limitations We can utilize such caching because our benchmarks operate under static (ScanNet) or quasi-static (robot) environments.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Learning rate schedule for encoder and decoder. Fine-tuning a pre-trained encoder alongside a randomly initialized decoder requires careful balancing to prevent unstable gradients ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** This choice better represents realworld deployment scenarios though it typically results in performance degradation due to sensor noise, missing regions, and registration errors, as discussed ...
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** As outlined earlier, our model is capable of working with sensor streams and does not require human intervention at test time (e.g., for mesh refinement ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 10: Impact of scene diversity. We train all models on SR3D+NR3D+ScanRefer and add 30K samples from L3DD. We ablate whether these extra samples come ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 12: Examples of the Spot robot at the end of navigation task before the pick task (right) the output bounding boxes of LOCATE 3D+ ...

- **Evidence anchors reviewed:** datasets p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 6 (4. Experiments and Analysis), p. 5 (3. LOCATE 3D DATASET Overview), p. 5 (3.1. Dataset Statistics), p. 6 (4. Experiments and Analysis), metrics p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 18 (Figure/Table caption), p. 18 (Figure/Table caption), baselines p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 6 (4.1. How does LOCATE 3D compare to prior methods), p. 6 (Figure/Table caption), p. 27 (Figure/Table caption), p. 5 (3.2. Comparison with prior datasets), results p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 20 (Figure/Table caption), p. 7 (4.1. How does LOCATE 3D compare to prior methods), p. 24 (Figure/Table caption), p. 6 (4.1. How does LOCATE 3D compare to prior methods).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
