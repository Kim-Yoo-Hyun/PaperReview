# Insights — AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these problems, we propose a stereo decoupled auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM).
- **p. 6 / Method - extractive body cue:** Then, we evaluate on our self-collected dataset, which consists of six sequences captured using a ZED 2i stereo camera.
- **p. 6 / Method - extractive body cue:** Given its demonstrated superior performance in handling complex real-world scenarios and stereo setups in recent literature [14, 37], DROID-SLAM provides a reliable benchmark for assessing ...
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive body cue:** To mitigate this limitation, we propose a time-aware sliding window coarse-to-fine strategy.
- **p. 6 / Method - extractive body cue:** For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames.
- **p. 6 / Method - extractive body cue:** For quantitative evaluation, we adopt the trajectory from the SOTA learning-based stereo SLAM system DROID-SLAM [34] as the reference.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method), p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 6 (Method)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** However, such coupled methods suffer from key limitations in localization robustness and real-time performance.
- **p. 2 / 1. Introduction - extractive body cue:** However, traditional handcrafted feature-based SLAM system lacks robustness to AE-induced illumination variations, leading to reduced localization accuracy and degraded appearance reconstruction quality in exposure-varying scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** For instance, MonoGS [26] adjusts image brightness via two exposure parameters, yet it fails to model complex AE mechanisms.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. ...
- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments show the IRL module significantly improves localization accuracy and robustness.
- **p. 8 / 5. Conclusion - extractive body cue:** It adopts a decoupled pipeline enabling illumination-robust localization and auto-exposurerobust photorealistic mapping.
- **Boundary to test:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. '-' denotes no results, as we use ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map per-image radiance maps to RGB images, enabling ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |
| Failure/limitation | Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. '-' denotes no results, as we use ... | p. 6 (Figure/Table caption), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Brightness adjustment is modeled as Vout = AVint, where Vint and Vout are the input and output brightness of a pixel, respectively, and A is the scaling factor which is randomly sampled ...를 Most 3DGS-based visual SLAM methods assume that input images strictly satisfy photometric consistency.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. '-' denotes no results, as we use ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map per-image radiance maps to RGB images, enabling ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, geometry, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. '-' denotes no results, as we use ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios..
3. Compare against the body-reported baseline or a matched simpler baseline: We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], representative decoupled 3DGS-based methods; 3) Ours + HDR-GS, a variant ....
4. Report the body metric and its denominator/aggregation: Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework..
5. Re-run the body-reported ablation/failure condition: The ablation results are reported in Table 3 within Row (1) (i.e., without CTFO, CEN and IRL) corresponds to the original Photo-SLAM [14]..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (Method), p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization); the primary result is directionally consistent at p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, main, contributions mechanism이 We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; ... 대비 Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework.을 개선하고, Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
