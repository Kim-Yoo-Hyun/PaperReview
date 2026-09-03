# Evaluation - SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (46 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kmv7yg6QXv; PDF retrieval source: https://arxiv.org/pdf/2502.13143. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 22 (Figure/Table caption)): SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new benchmark Open6DOR V2.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Real-world Language-Grounded Object Manipulation Tasks and Evaluations We construct 60 real-world tasks involving over 100 objects, following the Open6DOR benchmark [25].
- **p. 9 / 4 Experiments - extractive body cue:** Our PointSO model, integrated within the SOFAR system, demonstrates strong performance in both simulated and real-world robotic manipulation tasks.
- **p. 8 / 4 Experiments - extractive body cue:** 4.4 Simulation Object Manipulation Evaluation on SIMPLER [62] We conduct quantitative evaluations of SOFAR's zero-shot execution performance on Google Robot tasks & Widow-X tasks and ...
- **p. 9 / 4 Experiments - extractive body cue:** The benchmark includes two tracks: position and orientation, covering tasks such as object counting, spatial relations, and objectfacing direction.
- **p. 7 / 4 Experiments - extractive body cue:** 4.3 6-DoF Object Rearrangement Evaluation on Open6DOR V2 To evaluate 6-DoF object rearrangement capabilities, we extend the original Open6DOR benchmark [25], which primarily focuses on ...
- **p. 8 / 4 Experiments - extractive body cue:** We present success rates for the "Variant Aggregation" and "Visual Matching" approaches.
- **p. 8 / 4 Experiments - extractive body cue:** We report both the final success rate ("Success") along with partial success (e.g., "Grasp Spoon").

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); B Additional Experiments (p. 22); B.1 Articulated Objects Manipulation Evaluation (p. 22); B.4 Long Horizon Object Manipulation Experiment (p. 23); B.5 Close-Loop Execution Experiment (p. 23); B.6 In the Wild Evaluation of Semantic Orientation (p. 23); 4. Experimental result reproducibility (p. 41); 7. Experiment statistical significance (p. 42); 8. Experiments compute resources (p. 43).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | SOFAR achieves the best performance, demonstrating strong spatial understanding and zero-shot generalization. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We note that certain objects are intrinsically difficult to manipulate, suggesting the need for more robust policies incorporating prehensile grasping and adaptive strategies to ... | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Visualization of OrienText300K data construction and validation results. In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning ... | p. 3 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead. | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new benchmark Open6DOR V2.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Real-world Language-Grounded Object Manipulation Tasks and Evaluations We construct 60 real-world tasks involving over 100 objects, following the Open6DOR benchmark [25].
- **p. 9 / 4 Experiments - extractive body cue:** Our PointSO model, integrated within the SOFAR system, demonstrates strong performance in both simulated and real-world robotic manipulation tasks.
- **p. 8 / 4 Experiments - extractive body cue:** 4.4 Simulation Object Manipulation Evaluation on SIMPLER [62] We conduct quantitative evaluations of SOFAR's zero-shot execution performance on Google Robot tasks & Widow-X tasks and ...
- **p. 9 / 4 Experiments - extractive body cue:** The benchmark includes two tracks: position and orientation, covering tasks such as object counting, spatial relations, and objectfacing direction.
- **p. 7 / 4 Experiments - extractive body cue:** 4.3 6-DoF Object Rearrangement Evaluation on Open6DOR V2 To evaluate 6-DoF object rearrangement capabilities, we extend the original Open6DOR benchmark [25], which primarily focuses on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We introduce the concept of Semantic Orientation, which refers to natural language- grounded object orientations, such as the "cutting" direction of a knife ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Representation comparison between semantic orientation and others. 1
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of OrienText300K data construction and validation results. In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: PointSO model architecture. 3D and Language Embeddings Given an object's point cloud X = {xi ∈R3/i = 1, 2, . . . , ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Overview of SOFAR system. Given RGB-D images and language instructions, SOFAR first leverages a VLM to identify relevant object phrases and semantic orientations. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative results of real world language-grounded manipulation. SOFAR can generalize across various embodiments, tasks and environments. 77.1 70.4 33.3 4.2 44.4 3.7
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: Quantitative evaluation of zero-shot real-world language-grounded rearrangement. We design 60 diverse real-world tasks involving over 100 diverse objects (detailed in Table 13). nodes ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 6-DoF object rearrangement evaluation on Open6DOR [25].

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new benchmark Open6DOR ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | 4.1 Real-world Language-Grounded Object Manipulation Tasks and Evaluations We construct 60 real-world tasks involving over 100 objects, following the Open6DOR benchmark [25]. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (Abstract), p. 4 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (1 Introduction), p. 5 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We present success rates for the "Variant Aggregation" and "Visual Matching" approaches. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We report both the final success rate ("Success") along with partial success (e.g., "Grasp Spoon"). | definition/direction/unit from same section | p. 8 (4 Experiments) |
| PointSO still has an accuracy rate of 60% even under a 5° threshold. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| As reported in Table 3, the accuracy at the 45° threshold reflects the model's resilience to these corruptions. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Our PointSO model, integrated within the SOFAR system, demonstrates strong performance in both simulated and real-world robotic manipulation tasks. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 12: Long-horizon object manipulation experiment of our SOFAR. B.4 Long Horizon Object Manipulation Experiment Fig. 12 illustrates the execution performance of our model ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 3: Visualization of OrienText300K data construction and validation results. In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead. | comparison identity and matched condition | p. 7 (4 Experiments) |
| As shown in Tables 4 and 5, despite the training data for Octo and OpenVLA including Google Robot tasks, SOFAR demonstrates superior zero-shot performance ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| For perception tasks, we adopt the original Open6DOR [25] evaluation protocol and compare with the same baselines. | comparison identity and matched condition | p. 8 (4 Experiments) |
| SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement. | comparison identity and matched condition | p. 9 (4 Experiments) |
| We evaluate SOFAR on 6-DoF SpatialBench against several VLMs and comparable methods as baselines, as presented in Table 6. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Table 7: Zeroshot articulate object manipulation evaluation within the SAPIEN [123] simulator using PartNet-Mobility Dataset. Notably, while the baseline methods use distinct training and ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 11: Ablation study of multi-modal fusion in PointSO. All experiments are conducted with the PointSO-Base variant. Fusion Method 45° 30° 15° 5° | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| The tasks are divided into three tracks-position, orientation, and comprehensive & 6-DoF-each with simple and hard variants. | component/input/data sensitivity | p. 7 (4 Experiments) |
| We train different model variants on OrienText300K, and the results in Table 2 report performance across different angular thresholds ranging from 45° to 5°. | component/input/data sensitivity | p. 7 (4 Experiments) |
| We present success rates for the "Variant Aggregation" and "Visual Matching" approaches. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Figure 3: Visualization of OrienText300K data construction and validation results. In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 7: Zeroshot articulate object manipulation evaluation within the SAPIEN [123] simulator using PartNet-Mobility Dataset. Notably, while the baseline methods use distinct training and ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction. | SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 22 (Figure/Table caption) |
| Primary metric/result | SOFAR achieves the best performance, demonstrating strong spatial understanding and zero-shot generalization. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Real-world Language-Grounded Object Manipulation Tasks and Evaluations We construct 60 real-world tasks involving over 100 objects, following the Open6DOR benchmark [25].
- **p. 4 / 1 Introduction - extractive body cue:** Quality Validation To validate annotation quality, we construct a validation set containing 208 samples with manually labeled filtering criteria and semantic orientation labels, respectively.
- **p. 5 / 1 Introduction - extractive body cue:** 3.1 Scene Graph with 6-DoF Information To integrate both the positional & orientational interaction relationships of objects, we use a scene graph with 6-DoF information ...
- **p. 6 / 1 Introduction - extractive body cue:** 77.1 70.4 33.3 4.2 44.4 3.7 43.3 77.1 63.0 30.6 12.5 50.0 11.1 45.0 81.3 81.5 44.4 20.8 50.0 22.2 53.9 85.4 85.2 52.8 29.2 ...
- **p. 7 / 1 Introduction - extractive body cue:** Method Position Track Rotation Track 6-DoF Track Time Cost (s) Level 0 Level 1 Overall Level 0 Level 1 Level 2 Overall Position Rotation Overall ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following a single-step execution failure to approximately ... | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 16: Failure case distribution analysis of our SOFAR. C | p. 24 (Figure/Table caption) |
| body limitation/failure cue | We employ OMPL [103] to generate a collision-free trajectory, initializing joint positions at the midpoint to ensure smooth and safe motion. | p. 6 (1 Introduction) |
| body limitation/failure cue | To evaluate the robustness of PointSO under such conditions, we introduce three types of input perturbations: random rotations, partial single-sided observations, and Gaussian noise. | p. 7 (4 Experiments) |
| body limitation/failure cue | Table 3: Semantic Orientation evaluation of robustness. Single-View: randomly select a camera viewpoint within the unit sphere and generate a single FoV viewpoint in ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| SOFAR: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation Zekun Qi13∗ Wenyao Zhang237∗ Yufei Ding34∗ Runpei Dong5 Xinqiang Yu3 Jingwen Li4 Lingyun Xu4 Baoyu ... | p. 1 (Body text (section not recovered)) |
| For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group ... | p. 4 (1 Introduction) |
| 4, PointSO takes the object's 3D point clouds and a language description as inputs, and predicts the corresponding semantic orientation. "Drilling" "Handle" "top" Transformer ... | p. 4 (1 Introduction) |
| 3.2 Spatial-Aware Task Reasoning We encode the 6-DoF scene graph G into descriptive language and input it to the VLM alongside the RGB image ... | p. 5 (1 Introduction) |
| To guide the VLM in generating such transformations from language instructions, we adopt a CoT reasoning process [119] that decomposes the reasoning into three ... | p. 5 (1 Introduction) |
| Given the initial state ci and Si, the full 6-DoF transformation Pi is computed. | p. 6 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown ...
- **p. 8 / 4 Experiments - extractive body cue:** Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following a single-step execution failure to approximately achieve ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 16: Failure case distribution analysis of our SOFAR. C
- **p. 6 / 1 Introduction - extractive body cue:** We employ OMPL [103] to generate a collision-free trajectory, initializing joint positions at the midpoint to ensure smooth and safe motion.
- **p. 7 / 4 Experiments - extractive body cue:** To evaluate the robustness of PointSO under such conditions, we introduce three types of input perturbations: random rotations, partial single-sided observations, and Gaussian noise.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Semantic Orientation evaluation of robustness. Single-View: randomly select a camera viewpoint within the unit sphere and generate a single FoV viewpoint in polar ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), metrics p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 22 (Figure/Table caption), results p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 22 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
