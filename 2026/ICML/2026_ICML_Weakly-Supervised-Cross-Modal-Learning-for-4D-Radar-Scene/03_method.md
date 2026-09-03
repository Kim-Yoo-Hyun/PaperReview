# Method - Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MCu8SOjPad; PDF retrieval source: https://openreview.net/pdf/ed47436b3c090baac63dc92adf3fafca0e15cc01.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 3 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions), p. 5 (3.2. Instance-aware Loss Functions), p. 6 (3.3. Rigid Static Loss)): Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1.

## Method Body Digest

- **p. 4 / 3.1. IterFlow - extractive body cue:** Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1.
- **p. 4 / 3.1. IterFlow - extractive body cue:** With set abstraction in (Qi et al., 2017a;b), the ball query-based cross-frame correlation feature is then computed as: ck i = max l (MLP(concat yl∈NL ...
- **p. 3 / 3.1. IterFlow - extractive body cue:** To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To address this problem, we introduce an instance-level flow smoothness loss Lis.
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To mitigate this issue, we propose calculating the Chamfer loss exclusively between point pairs that belong to the same instance, utilizing the pointwise instance label ...
- **p. 6 / 3.3. Rigid Static Loss - extractive body cue:** Quantitative Evaluation on Network Architecture and Loss Scalability on VoD validation set.
- **p. 3 / 3. Method - extractive body cue:** The overall architecture of our proposed method comprises an iterative scene flow estimation network, termed IterFlow (Fig.
- **p. 3 / 3. Method - extractive body cue:** Subsequently, auxiliary 2D image and odometry are used to construct three losses for optimizing the predicted flows: Ltotal = Lstat + Lic + Lis.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only ...
- **p. 3 / 3.1. IterFlow - extractive body cue:** To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene ...
- **p. 3 / 3. Method - extractive body cue:** Every radar point consists of five attributes: its 3D coordinates, radar cross-section (RCS), and relative radial velocity (RRV).

## Source Evidence Cues

- **p. 4 / 3.1. IterFlow - extractive body cue:** Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1.
- **p. 4 / 3.1. IterFlow - extractive body cue:** With set abstraction in (Qi et al., 2017a;b), the ball query-based cross-frame correlation feature is then computed as: ck i = max l (MLP(concat yl∈NL ...
- **p. 3 / 3.1. IterFlow - extractive body cue:** To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To address this problem, we introduce an instance-level flow smoothness loss Lis.
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To mitigate this issue, we propose calculating the Chamfer loss exclusively between point pairs that belong to the same instance, utilizing the pointwise instance label ...
- **p. 6 / 3.3. Rigid Static Loss - extractive body cue:** Quantitative Evaluation on Network Architecture and Loss Scalability on VoD validation set.
- **p. 3 / 3. Method - extractive body cue:** The overall architecture of our proposed method comprises an iterative scene flow estimation network, termed IterFlow (Fig.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1. | p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | With set abstraction in (Qi et al., 2017a;b), the ball query-based cross-frame correlation feature is then computed as: ck i = max ... | p. 4 (3.1. IterFlow), p. 3 (3.1. IterFlow) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed ... | p. 3 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive body cue:** Subsequently, auxiliary 2D image and odometry are used to construct three losses for optimizing the predicted flows: Ltotal = Lstat + Lic + Lis.
- **p. 3 / 3. Method - extractive body cue:** Here Lstat denotes the rigid static loss defined in Sec.
- **p. 4 / 3.1. IterFlow - extractive body cue:** Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1.
- **p. 4 / 3.1. IterFlow - extractive body cue:** The process of the kth scene flow iteration is depicted on the left and the detailed loss formulation process in the training stage is given ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To address this problem, we introduce an instance-level flow smoothness loss Lis.
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** With assistance from 2D semantic information, our instance-aware Chamfer loss Lic (Eq.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Instance-aware Loss Functions), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | features, fused, form, GRU, input, hidden, state, updated, follows, Conv1d, hk-1, tanh, where, weight | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | features, fused, form, GRU, input, hidden, state, updated, follows, Conv1d | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Given, high, cost, high-performance, LiDAR, sensors, novel, setting, weakly, supervised | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Subsequently, auxiliary, image, odometry, construct, three, losses, optimizing, predicted, flows | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. IterFlow - extractive body cue:** These features are fused to form the GRU input xk, and the hidden state is updated as follows: zk = σ(Conv1d([hk-1, xk], Wz)) (2) rk ...
- **p. 6 / 3.3. Rigid Static Loss - extractive body cue:** R represents radar point clouds input.
- **p. 2 / 1. Introduction - extractive body cue:** IterFlow is lightweight, featuring iterative flow refinement scheme and ball query-based cross-frame correlation, both tailored to the challenging radar domain. • We design two novel ...
- **p. 3 / 3. Method - extractive body cue:** Following previous label-free settings (Ding et al., 2023; Wu et al., 2025; Zhai et al., 2025), while data from other modalities may be accessible during ...
- **p. 4 / 3.1. IterFlow - extractive body cue:** Each pointwise feature φ(xi) ∈Et and φ(yi) ∈Et+1 consists of the original input 3D position and the feature dimension C.
- **p. 6 / 3.3. Rigid Static Loss - extractive body cue:** In the Category (Cat.) column, existing methods are classified depending on the input modality used in their original work.
- **p. 2 / 1. Introduction - extractive body cue:** Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This is because IterFlow adopts a more concise yet effective ball query-based cross-frame correlation design, rather than the original KNN-based and multi-scale ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The coordinates of points in the source and target frame are denoted as xi ∈Pt and yi ∈Pt+1, respectively. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | IterFlow is implemented in PyTorch (Paszke et al., 2019) and trained for 150 epochs with a batch size of 8. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4. Experiments - extractive body cue:** IterFlow is implemented in PyTorch (Paszke et al., 2019) and trained for 150 epochs with a batch size of 8.
- **p. 3 / 3. Method - extractive body cue:** During training, the consecutive radar point clouds Pt and Pt+1 are fed into IterFlow to generate the final scene flow prediction FK ∈RN1×3 after K ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, warped, estimated, scene, flow, then, calculate, chamfer, loss, abstraction, ball, query-based, cross-frame, correlation, feature, computed, MLP, concat, address, limitations.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene ... | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Semantic / temporal fusion | For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD ... | p. 6 (4. Experiments), p. 6 (4.1. Main Results) |
| Robot query / planning handoff | The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static ... | p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation Study on Loss Terms on VoD validation set. Lsc is the soft chamfer loss without instance-aware guidance and Lss is the KNN-based ...
- **p. 7 / 4.1. Main Results - extractive body cue:** Note that fully-supervised methods are trained with the radar scene flow ground truth derived from the annotated 3D tracking boxes provided by the dataset, and ...
- **p. 6 / 4. Experiments - extractive body cue:** B.2 in the appendix for hyperparameter sensitivity analysis of L, R and K. officially released YOLO11-l (Khanam & Hussain, 2024) model and the huge version ...
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** Second, we examine the effectiveness of Lis by removing it from total loss.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 7. Ablation on iteration steps K and ball query hyperparameters L and R. When L varies, R = 1m; when R varies, L = ...
- **p. 6 / 4. Experiments - extractive body cue:** In addition, for the cross-modal supervised CMFlow (Ding et al., 2023), we generate extra required optical flow labels and pseudo scene flow labels by adopting ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Visualization of failure cases on VoD validation set. Each row displays a driving scenario and regions with large scene flow estimation errors are ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 3 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions), p. 5 (3.2. Instance-aware Loss Functions), p. 6 (3.3. Rigid Static Loss), objective p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions), p. 5 (3.2. Instance-aware Loss Functions), temporal p. 7 (4.1. Main Results), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
