# Method — EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF 또는 공식 full-text source의 method/formulation 관련 본문 cue를 검토해 pipeline과 interface를 구조화했다. tracker의 reading status/evidence는 이 migration에서 변경하지 않았다.

## Method in One Sentence

semantic 3D reconstruction을 offline post-processing이 아닌 online feed-forward embodied perception state로 reformulate한다.

## Design Rationale

offline open-vocabulary 3DGS는 complete image set와 expensive optimization에 의존해 exploration 중 즉시 쓸 수 없고, pure 2D features는 spatial consistency가 약하다.

## Source Evidence Cues

- We use the official training split for the training and select 4 scenes for the evaluation.
- To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
- By following , we use 100 scenes for training and sample 10 scenes for testing.
- Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an online manner.
- **Source anchor:** 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.

## Pipeline

| Module | Purpose | Input | Operation | Output | Interface / expected benefit | Evidence |
|---|---|---|---|---|---|---|
| Geometry extraction | image/point input에서 3D structure를 복원 | 300개 이상 streaming image와 pose를 입력으로 online sparse coefficient field가 3D Gaussians와 CLIP global codebook을 연결해 geometry, color와 semantic field를 갱신한다. | depth, pose, point, Gaussian 또는 correspondence representation을 추정. Source method cue: We use the official training split for the training and select 4 scenes for the evaluation. | geometric state/map | occlusion과 metric spatial relation을 노출 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |
| Semantic / temporal fusion | geometry에 language/semantic/state를 정렬 | geometric state와 text/visual feature/history | feature lifting, scene graph, map update 또는 temporal fusion. Source method cue: To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ... | queryable semantic 3D state | robot task와 open vocabulary를 연결 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |
| Robot query interface | 3D state를 planner/policy가 소비 | map/feature와 task query | grounding, target selection, collision/free-space 또는 action cue 생성. Source method cue: By following , we use 100 scenes for training and sample 10 scenes for testing. | goal/pose/path/action input | downstream behavior를 통해 perception value를 검증 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |

## Objective / Update Rule

- **Primary objective:** novel-view/color/depth reconstruction과 2D·3D semantic segmentation/query consistency를 공동으로 높이며 frame-wise processing latency를 제한한다.
- **State/model bridge:** 300개 이상 streaming image와 pose를 입력으로 online sparse coefficient field가 3D Gaussians와 CLIP global codebook을 연결해 geometry, color와 semantic field를 갱신한다.
- **Constraint or regularization boundary:** camera pose/stream alignment, incremental memory budget과 sparse semantic coefficients를 유지하면서 scene 전체를 누적해야 한다.
- **Optimization/update:** module별 update와 optimizer/gain/solver의 exact choice는 아래 formal cue와 source anchor를 기준으로 확인한다; 근거 없는 수치·optimizer는 추가하지 않았다.
- **Source:** method/formulation cue: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요

## Variables and Parameters

| Symbol / parameter | Type / unit | Meaning | Used in | Source |
|---|---|---|---|---|
| I / P | image/point cloud | raw visual geometry | feature extraction | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요 |
| T / G | pose/map/scene graph | world-coordinate structure | fusion/query | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요 |
| z | semantic feature | open-vocabulary or task representation | grounding | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요 |
| r / a | robot query/action | downstream target or motion cue | robot interface | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요 |

## Observation–State–Action Interface

- **Observation / input:** RGB-D, image set, point cloud, depth와 camera pose
- **State / latent representation:** geometry, map, object/relationship state
- **Action / output:** point map, pose, scene graph, affordance 또는 query result
- **Planner–controller / policy–environment interface:** streaming images/poses → online semantic 3DGS → open-vocabulary query/scene state → navigation or manipulation feedback다.

## Temporal and Runtime Contract

- **Horizon:** single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요.
- **Inference/control rate:** per-frame/streaming inference와 downstream policy/control rate가 분리된다.
- **History / memory:** camera poses, map/scene graph/Gaussian state와 temporal feature.
- **Compute / latency dependency:** 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다.

## Training vs Inference

- **Training / offline setup:** visual/3D/text supervision 또는 pretrained encoder adaptation; exact split 확인 필요.
- **Inference / online execution:** scene observation을 map/feature로 변환해 planner/policy query를 제공한다.
- **Boundary to keep separate:** training throughput, policy inference rate, low-level actuator rate와 feedback latency를 하나의 숫자로 합치지 않는다. paper-specific values는 본문 확인 필요.

## Method-Specific Formal Details

- **Canonical equation/law cue:** 정확한 method-specific equation/loss/control law는 아래의 verified formulation bridge와 source cue를 기준으로 본문에서 대조한다. 현재 note는 근거 없는 수식 번호나 hyperparameter를 추가하지 않는다.
- **Verified formulation bridge:** 300개 이상 streaming image와 pose를 입력으로 online sparse coefficient field가 3D Gaussians와 CLIP global codebook을 연결해 geometry, color와 semantic field를 갱신한다.
- **Source location:** method/formulation cue: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요

## Evaluation Link

> **Reading rule:** 아래 표는 04의 baseline/ablation cue를 method module에 연결하는 audit link다. 새로운 결과 수치를 주장하지 않으며, 원래의 protocol과 값은 [04_evaluation.md](./04_evaluation.md)에 둔다.

| Method module | What the evaluation should isolate | Baseline / ablation link | Evidence |
|---|---|---|---|
| Geometry extraction | occlusion과 metric spatial relation을 노출 | 04_evaluation.md에 method-specific baseline이 기록되지 않음 — 본문 확인 필요 | 04_evaluation.md cue; exact table/section 확인 필요 |
| Semantic / temporal fusion | robot task와 open vocabulary를 연결 | Baseline: 04_evaluation.md에 method-specific baseline이 기록되지 않음 — 본문 확인 필요; module removal/variant cue: 04_evaluation.md에 module ablation이 기록되지 않음 — 본문 확인 필요 | 04_evaluation.md cue; exact table/section 확인 필요 |
| Robot query interface | downstream behavior를 통해 perception value를 검증 | Execution/recovery ablation: 04_evaluation.md에 module ablation이 기록되지 않음 — 본문 확인 필요; protocol cue: To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ... | 04_evaluation.md cue; exact table/section 확인 필요 |

- **Protocol / metric cue:** To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
- **Metric cue:** mIoU mAP
- **Dataset / benchmark cue:** ScanNet ScanNet200

## Failure and Ablation Link

| Strong assumption | Why it matters to method | Failure / stress test |
|---|---|---|
| streaming view와 pose가 scene coverage를 빠르게 제공 | online reconstruction을 위해 필요 | long-tail unseen area와 pose drift는 holes/semantic misalignment |
| CLIP codebook이 robot query vocabulary를 cover | open-vocabulary indexing을 위해 필요 | fine-grained affordance·part relation은 부족 |

- **Ablation to request if absent:** remove the paper-specific core module while holding input, data, compute, horizon and controller interface fixed.
- **Failure evidence location:** [04_evaluation.md](./04_evaluation.md)의 failure/limitation 및 reproducibility cue; 현재 note에 새로운 failure claim을 만들지 않는다.

## Reproduction Checklist

1. [ ] 01 overview와 source anchor에서 observation/state/action, exact notation과 model assumptions를 확인한다.
2. [ ] Pipeline의 각 module을 input/output contract와 함께 구현하고, source-specific equation/solver/decoder를 고정한다.
3. [ ] Training/offline setup, inference rate, horizon, memory, compute budget을 분리해 기록한다.
4. [ ] 04의 baseline과 module-removal/variant ablation을 같은 task, data, seed, budget으로 실행한다.
5. [ ] primary metric뿐 아니라 failure mode, latency, assumption sensitivity와 closed-loop recovery를 보고한다.

## Verification Questions

- **Equation/source:** method/formulation cue: 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; equation 번호/page는 원문과 대조 필요
- **Module attribution:** 04의 baseline/ablation이 어느 pipeline module을 실제로 제거·대체하는가?
- **Runtime:** action horizon/chunk, memory window, inference rate와 low-level control rate가 각각 얼마인가?
- **Evidence boundary:** 현재 evidence level에서 직접 확인되지 않은 exact value, negative result, reproducibility detail을 추가하지 않았는가?
