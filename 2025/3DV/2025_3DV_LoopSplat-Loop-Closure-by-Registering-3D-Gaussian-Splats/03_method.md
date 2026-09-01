# Method - LoopSplat: Loop Closure by Registering 3D Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=0CNSbBa85A&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (Method), p. 6 (Method), p. 7 (4.3. Rendering), p. 7 (4.3. Rendering)): We compare LoopSplat with state-of-theart coupled RGB-D SLAM methods, categorized into two groups based on the underlying scene representation: (i) Neural implicit fields: MIPS-Fusion [77], GO-SLAM [101], and Loopy-SLAM [40], ...

## Method Body Digest

- **p. 6 / Method - extractive PDF cue:** We compare LoopSplat with state-of-theart coupled RGB-D SLAM methods, categorized into two groups based on the underlying scene representation: (i) Neural implicit fields: MIPS-Fusion [77], ...
- **p. 6 / Method - extractive PDF cue:** Tracking accuracy is measured by the root mean square absolute trajectory error (ATE RMSE) [73].
- **p. 7 / 4.3. Rendering - extractive PDF cue:** 6 reports our rendering performance on training views.
- **p. 7 / 4.3. Rendering - extractive PDF cue:** Gray indicates evaluation on submaps instead of a global map. margin over baselines that employ implicit neural representations.
- **p. 6 / Method - extractive PDF cue:** Runtime is reported as average per-frame tracking and map optimization time, as well as loop edge registration runtime.
- **p. 7 / 4.3. Rendering - extractive PDF cue:** To conduct a fair comparison, we merge all the submaps into a global one and optimize the global map with estimated cameras pose, to avoid ...
- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time compared ...
- **p. 7 / 4.3. Rendering - extractive PDF cue:** It is noteworthy that both the NeRF-based LoopySLAM and Point-SLAM methods require ground truth depth input to guide the depth rendering, whereas our method, leveraging ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module.
- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose a dense RGB-D SLAM system that uses submaps of 3D Gaussians for local frame-to-model tracking and dense mapping and is ...
- **p. 6 / 4.1. Tracking - extractive PDF cue:** We note that the ground truth poses in ScanNet, derived from BundleFusion [18], appear to have limited accuracy: visual inspection suggests that our method achieves ...

## Source Evidence Cues

- **p. 6 / Method - extractive PDF cue:** We compare LoopSplat with state-of-theart coupled RGB-D SLAM methods, categorized into two groups based on the underlying scene representation: (i) Neural implicit fields: MIPS-Fusion [77], ...
- **p. 6 / Method - extractive PDF cue:** Tracking accuracy is measured by the root mean square absolute trajectory error (ATE RMSE) [73].
- **p. 7 / 4.3. Rendering - extractive PDF cue:** 6 reports our rendering performance on training views.
- **p. 7 / 4.3. Rendering - extractive PDF cue:** Gray indicates evaluation on submaps instead of a global map. margin over baselines that employ implicit neural representations.
- **Detected method headings:** Method (p. 6); Method (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We compare LoopSplat with state-of-theart coupled RGB-D SLAM methods, categorized into two groups based on the underlying scene representation: (i) Neural implicit ... | p. 6 (Method), p. 6 (Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Tracking accuracy is measured by the root mean square absolute trajectory error (ATE RMSE) [73]. | p. 6 (Method), p. 7 (4.3. Rendering) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 6 reports our rendering performance on training views. | p. 7 (4.3. Rendering), p. 7 (4.3. Rendering) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / Method - extractive PDF cue:** Runtime is reported as average per-frame tracking and map optimization time, as well as loop edge registration runtime.
- **p. 7 / 4.3. Rendering - extractive PDF cue:** To conduct a fair comparison, we merge all the submaps into a global one and optimize the global map with estimated cameras pose, to avoid ...
- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time compared ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | noteworthy, NeRF-based, LoopySLAM, Point-SLAM, methods, require, ground, truth, depth, input, guide, rendering, whereas, leveraging | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | noteworthy, NeRF-based, LoopySLAM, Point-SLAM, methods, require, ground, truth, depth, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, LoopSplat, coupled, RGB-D, SLAM, system, Gaussian, Splatting, featuring, novel | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Runtime, reported, average, per-frame, tracking, optimization, time, well, loop, edge | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 4.3. Rendering - extractive PDF cue:** It is noteworthy that both the NeRF-based LoopySLAM and Point-SLAM methods require ground truth depth input to guide the depth rendering, whereas our method, leveraging ...
- **p. 6 / Method - extractive PDF cue:** Rendering quality is evaluated by comparing full-resolution rendered images to input training views in terms of PSNR, SSIM [84], and LPIPS [100].
- **p. 7 / 4.2. Reconstruction - extractive PDF cue:** LoopSplat falls behind Loopy-SLAM [40] and Point-SLAM [63], but note that the latter two require ground truth depth to determine where to sample points during ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address limitations of current systems, we seek a coupled SLAM system that avoids saving all mapped input frames and is able to extract loop ...
- **p. 6 / Method - extractive PDF cue:** LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world datasets, with a dedicated ablation study for loop ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Importantly, we show that traditional point cloud registration techniques are not suitable to derive the loop edge constraints from 3D Gaussians and propose a new ...
- **p. 1 / 1. Introduction - extractive PDF cue:** On the other hand, all coupled 3DGS SLAM methods lack strategies for achieving global consistency on the map and the poses, which leads to an ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Per-frame runtime is calculated as the total optimization time divided by the sequence length, profiled on a RTX A6000 GPU. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These re-integration techniques need to save all mapped frames in memory, which limits their scalability. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | These re-integration techniques need to save all mapped frames in memory, which limits their scalability. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.3. Rendering - extractive PDF cue:** 6 reports our rendering performance on training views.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** compare, LoopSplat, state-of-theart, coupled, RGB-D, SLAM, methods, categorized, groups, underlying, scene, representation, Neural, implicit, fields, MIPS-Fusion, GO-SLAM, Loopy-SLAM, incorporate, loop.
- **Relevant PDF headings:** Method (p. 6); Method (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Additionally, we require the least GPU memory to process a room-sized scene. | p. 7 (4.4. Memory and Runtime Analysis), p. 5 (Figure/Table caption) |
| Semantic / temporal fusion | Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art ... | p. 6 (Figure/Table caption), p. 5 (4. Experiments) |
| Robot query / planning handoff | Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 8. Ablation Study on 3DGS Registration. The num- bers are computed based on average performance of 8 scenes on Replica [71]. Mul. Opt. denotes ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world datasets, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7. Runtime and Memory Usage on Replica office 0. Per-frame runtime is calculated as the total optimization time di- vided by the sequence length, ...
- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time compared ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the NeRF-based ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that LoopSplat ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by our ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (Method), p. 6 (Method), p. 7 (4.3. Rendering), p. 7 (4.3. Rendering), objective p. 6 (Method), p. 7 (4.3. Rendering), p. 7 (4.4. Memory and Runtime Analysis), temporal p. 8 (4.5. Ablations), p. 2 (1. Introduction), p. 2 (2. Related Work), p. 6 (Method), p. 6 (Method), p. 7 (4.4. Memory and Runtime Analysis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
