# Evaluation - JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnuB0Nlbd5; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS)): Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a single RGB input, demonstrating the effectiveness of our ...

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Following established methods (Zhang et al., 2025b; Li et al., 2025c; Li, 2025; Chu et al., 2025), we conducted experiments on two of the most ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In real-world experiments, we use the Unitree Go2 as the robotic platform, equipped with an Insta360 X5 camera to capture front RGB.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 MAIN RESULTS Results on VLN-CE benchmark.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** External data includes any sources beyond the standard R2R/RxR-CE datasets (e.g., EnvDrop, DAgger, general VQA, etc.).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (2025b) ✓ 4.98 64.2 56.9 51.9 „ 26330K JanusVLN (Ours) ✓ 4.78 65.2 60.5 56.8 10692K Table 2: Comparison with SOTA methods on VLN-CE RxR ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Furthermore, as the memory size increases, the inference overhead of VGGT grows exponentially, rendering it impractical for real-world applications.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a single RGB ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Against methods employing explicit textual cognitive maps (e.g., MapNav) or historical frames (e.g., NaVILA, StreamVLN), JanusVLN achieves improvements of 20.8, 10.8, and 3.6, respectively, ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | When the spatial geometric encoder VGGT in JanusVLN is replaced by other visual encoders (e.g., DINOv2 (Oquab et al., 2023), and SigLIP 2 (Tschannen ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This approach significantly reduces inference overhead by 69%-90% while also yielding a slight performance improvement, thereby demonstrating the effectiveness of the implicit neural memory. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on ... | p. 6 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Following established methods (Zhang et al., 2025b; Li et al., 2025c; Li, 2025; Chu et al., 2025), we conducted experiments on two of the most ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In real-world experiments, we use the Unitree Go2 as the robotic platform, equipped with an Insta360 X5 camera to capture front RGB.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 MAIN RESULTS Results on VLN-CE benchmark.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** External data includes any sources beyond the standard R2R/RxR-CE datasets (e.g., EnvDrop, DAgger, general VQA, etc.).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (2025b) ✓ 4.98 64.2 56.9 51.9 „ 26330K JanusVLN (Ours) ✓ 4.78 65.2 60.5 56.8 10692K Table 2: Comparison with SOTA methods on VLN-CE RxR ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Furthermore, as the memory size increases, the inference overhead of VGGT grows exponentially, rendering it impractical for real-world applications.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: JanusVLN, using RGB-only video, decouples visual semantics and spatial geometry to construct novel, fixed-size dual implicit memory. This memory is incrementally updated during ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The framework of JanusVLN. Given an RGB-only video stream and navigation instruc- tions, JanusVLN utilizes a dual-encoder to separately extract visual-semantic and spatial-geometric ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Inference time com- parison for the current frame of varying sequence lengths. Building upon the dual implicit memory paradigm, we propose JanusVLN in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative results of JanusVLN on real-world. Real-world evaluation setup. In real-world experiments, we use the Unitree Go2 as the robotic platform, equipped with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Comparison with SOTA methods on VLN-CE R2R Val-Unseen split. External data includes any sources beyond the standard R2R/RxR-CE datasets (e.g., EnvDrop, DAgger, general ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Comparison with SOTA methods on VLN-CE RxR Val-Unseen split.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: The ablation experiments of each component of the proposed JanusVLN.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Comparison between additional, different semantic encoders and spatial encoder. Encoder NEÓ OSÒ SRÒ SPLÒ JanusVLN w/o extra encoder 6.58

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019). | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | Following established methods (Zhang et al., 2025b; Li et al., 2025c; Li, 2025; Chu et al., 2025), we conducted experiments on two of the ... | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 4 (3 METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3 METHOD), p. 5 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Removing the spatial memory led to a substantial drop in the SPL score from 49.2 to 40.9. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Among these, SR and SPL are widely regarded as the primary metrics, reflecting task completion and path efficiency, respectively Wei et al. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Notably, even without any additional data, JanusVLN* still outperforms the aforementioned methods that rely on partial extra data by a margin of 3.7-18.8 in ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| By leveraging the spatial-geometric memory within dual implicit memory, JanusVLN effectively enhances its spatial reasoning, enabling the successful completion of these challenging tasks. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| JanusVLN runs on a remote server with an A10 GPU to continuously process RGB and instructions, returning the inference results to the robot for ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Depth S.RGB NEÓ OSÒ SRÒ SPLÒ External Data HPN+DN [ICCV21] (Krantz et al., 2021) ✓ ✓ ✓ 6.31 40.0 36.0 34.0 - CMA [CVPR22] ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Finally, the simultaneous removal of both memory modules leads to a near-collapse in model performance. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Notably, even without any additional data, JanusVLN* still outperforms the aforementioned methods that rely on partial extra data by a margin of 3.7-18.8 in ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Furthermore, JanusVLN outperforms SOTA methods that use additional 3D depth data, such as g3DLF and NaVid-4D, by 12.6-16.7, indicating its ability to effectively enhance ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| (2025b) ✓ 4.98 64.2 56.9 51.9 „ 26330K JanusVLN (Ours) ✓ 4.78 65.2 60.5 56.8 10692K Table 2: Comparison with SOTA methods on VLN-CE ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Ablation of the dual implicit memory. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| For more ablation studies, please refer to the supplementary material. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We provide an ablation study in Table 4 to investigate the effect of introducing additional encoders. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| This suggests that the dual implicit memory, as a novel memory paradigm, can effectively replace conventional textual cognitive maps and historical frames. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Notably, even without any additional data, JanusVLN* still outperforms the aforementioned methods that rely on partial extra data by a margin of 3.7-18.8 in ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| The ablation study for dual implicit memory is presented in Table 3. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| We present the ablation studies on memory size in Table 5. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| First, as shown in the first row, with a memory of 8 frames, the original VGGT model without caching necessitates re-computation of the entire ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN. | Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a single RGB ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Primary metric/result | Against methods employing explicit textual cognitive maps (e.g., MapNav) or historical frames (e.g., NaVILA, StreamVLN), JanusVLN achieves improvements of 20.8, 10.8, and 3.6, respectively, ... | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We set the initial and sliding window size to 8 and 48 frames.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Memory Size Inference Time NEÓ OSÒ SRÒ SPLÒ VGGT (8) 268 ms 5.99 56.2 50.2 45.0 VGGT (32) 1549 ms 5.66 56.8 51.2 47.6 Cached ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** First, as shown in the first row, with a memory of 8 frames, the original VGGT model without caching necessitates re-computation of the entire sequence ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** This results in an inference overhead of 268 ms.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** As the memory size increases, JanusVLN's performance progressively improves, saturating at 48 frames.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Performance on various instruction lengths/complexity. larger-scale external datasets, akin to the approaches of StreamVLN and NaVILA, is reserved for future work to ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Finally, when we omit the preservation of the initial window's KV, a slight performance degradation is observed, indicating that the first few frames of ... | p. 10 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is trained for one epoch, during which we exclusively fine-tune the LLM and the projection layer with learning rates of 2e-5 and ... | p. 7 (4 EXPERIMENTS) |
| Encoder NEÓ OSÒ SRÒ SPLÒ JanusVLN w/o extra encoder 6.58 54.3 47.0 40.9 JanusVLN w/ extra DINOv2 6.44 55.4 47.5 41.5 JanusVLN w/ extra ... | p. 9 (4 EXPERIMENTS) |
| Memory Size Inference Time NEÓ OSÒ SRÒ SPLÒ VGGT (8) 268 ms 5.99 56.2 50.2 45.0 VGGT (32) 1549 ms 5.66 56.8 51.2 47.6 ... | p. 9 (4 EXPERIMENTS) |
| JanusVLN runs on a remote server with an A10 GPU to continuously process RGB and instructions, returning the inference results to the robot for ... | p. 7 (4 EXPERIMENTS) |
| In contrast, our approach avoids reprocessing historical frames, causing its inference time to increase only marginally and thereby demonstrating excellent efficiency. | p. 6 (3 METHOD) |
| To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research ... | p. 4 (3 METHOD) |
| As our focus is on feature extraction, which embeds 3D geometry prior information, rather than directly outputting 3D attributes, we leverage the encoder and ... | p. 4 (3 METHOD) |
| Gt " DecoderpCrossAttnpEncoderpxtq, tMinitial, Mslidinguqq. | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 21 / Figure/Table caption - extractive body cue:** Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 8: Performance on various instruction lengths/complexity. larger-scale external datasets, akin to the approaches of StreamVLN and NaVILA, is reserved for future work to construct ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Finally, when we omit the preservation of the initial window's KV, a slight performance degradation is observed, indicating that the first few frames of memory ...

- **Evidence anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), baselines p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
