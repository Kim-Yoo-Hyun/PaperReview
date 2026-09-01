# Method — VGGT: Visual Geometry Grounded Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF 또는 공식 full-text source의 method/formulation 관련 본문 cue를 검토해 pipeline과 interface를 구조화했다. tracker의 reading status/evidence는 이 migration에서 변경하지 않았다.

## Method in One Sentence

3D-inductive optimization pipeline을 large feed-forward Transformer의 joint multi-view prediction으로 reformulate한다.

## Design Rationale

pairwise reconstruction은 image 수가 늘면 post-processing/fusion과 optimization이 필요하고, classical bundle adjustment는 latency가 크다.

## Source Evidence Cues

- We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ...
- We compare our alternating-attention architecture against two variants: one using only global self-attention and another employing cross-attention. well, excelling on challenging out-of-domain examples, such as oil paintings, non-overlapping ...
- Introduction We consider the problem of estimating the 3D attributes of a scene, captured in a set of images, utilizing a feedforward neural network.
- Even so, visual geometry still plays a major role in 3D reconstruction, which increases complexity and computational cost.
- **Source anchor:** 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.

## Pipeline

| Module | Purpose | Input | Operation | Output | Interface / expected benefit | Evidence |
|---|---|---|---|---|---|---|
| Geometry extraction | image/point input에서 3D structure를 복원 | image set를 sequence/tokens로 입력한 Transformer가 모든 view에 대한 camera parameters, dense point maps/depth와 cross-view tracks를 공동 출력한다. | depth, pose, point, Gaussian 또는 correspondence representation을 추정. Source method cue: We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig. | geometric state/map | occlusion과 metric spatial relation을 노출 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |
| Semantic / temporal fusion | geometry에 language/semantic/state를 정렬 | geometric state와 text/visual feature/history | feature lifting, scene graph, map update 또는 temporal fusion. Source method cue: Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ... | queryable semantic 3D state | robot task와 open vocabulary를 연결 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |
| Robot query interface | 3D state를 planner/policy가 소비 | map/feature와 task query | grounding, target selection, collision/free-space 또는 action cue 생성. Source method cue: We compare our alternating-attention architecture against two variants: one using only global self-attention and another employing cross-attention. well, excelling on challenging out-of-domain examples, such as oil paintings, non-overlapping ... | goal/pose/path/action input | downstream behavior를 통해 perception value를 검증 | 본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요 |

## Objective / Update Rule

- **Primary objective:** multi-view geometric supervision에서 camera/point/depth/track prediction error를 공동으로 최소화한다.
- **State/model bridge:** image set를 sequence/tokens로 입력한 Transformer가 모든 view에 대한 camera parameters, dense point maps/depth와 cross-view tracks를 공동 출력한다.
- **Constraint or regularization boundary:** 입력 images가 충분한 overlap과 공통 scene geometry를 갖고 camera/projective ambiguity를 학습된 convention으로 해소해야 한다.
- **Optimization/update:** module별 update와 optimizer/gain/solver의 exact choice는 아래 formal cue와 source anchor를 기준으로 확인한다; 근거 없는 수치·optimizer는 추가하지 않았다.
- **Source:** method/formulation cue: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요

## Variables and Parameters

| Symbol / parameter | Type / unit | Meaning | Used in | Source |
|---|---|---|---|---|
| I / P | image/point cloud | raw visual geometry | feature extraction | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요 |
| T / G | pose/map/scene graph | world-coordinate structure | fusion/query | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요 |
| z | semantic feature | open-vocabulary or task representation | grounding | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요 |
| r / a | robot query/action | downstream target or motion cue | robot interface | domain-normalized interface notation from the reviewed problem/method cue; exact equation/notation: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요 |

## Observation–State–Action Interface

- **Observation / input:** RGB-D, image set, point cloud, depth와 camera pose
- **State / latent representation:** geometry, map, object/relationship state
- **Action / output:** point map, pose, scene graph, affordance 또는 query result
- **Planner–controller / policy–environment interface:** multi-view images → camera/point/depth/track state → mapping, localization or collision-aware planning다.

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
- **Verified formulation bridge:** image set를 sequence/tokens로 입력한 Transformer가 모든 view에 대한 camera parameters, dense point maps/depth와 cross-view tracks를 공동 출력한다.
- **Source location:** method/formulation cue: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요

## Evaluation Link

> **Reading rule:** 아래 표는 04의 baseline/ablation cue를 method module에 연결하는 audit link다. 새로운 결과 수치를 주장하지 않으며, 원래의 protocol과 값은 [04_evaluation.md](./04_evaluation.md)에 둔다.

| Method module | What the evaluation should isolate | Baseline / ablation link | Evidence |
|---|---|---|---|
| Geometry extraction | occlusion과 metric spatial relation을 노출 | The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. | 04_evaluation.md cue; exact table/section 확인 필요 |
| Semantic / temporal fusion | robot task와 open vocabulary를 연결 | Baseline: The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.; module removal/variant cue: 04_evaluation.md에 module ablation이 기록되지 않음 — 본문 확인 필요 | 04_evaluation.md cue; exact table/section 확인 필요 |
| Robot query interface | downstream behavior를 통해 perception value를 검증 | Execution/recovery ablation: 04_evaluation.md에 module ablation이 기록되지 않음 — 본문 확인 필요; protocol cue: The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ... | 04_evaluation.md cue; exact table/section 확인 필요 |

- **Protocol / metric cue:** The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ...
- **Metric cue:** accuracy mAP
- **Dataset / benchmark cue:** ScanNet Replica

## Failure and Ablation Link

| Strong assumption | Why it matters to method | Failure / stress test |
|---|---|---|
| training 3D data가 deployment camera/scene distribution을 충분히 cover | metric geometry generalization을 위해 필요 | domain shift·dynamic object는 inconsistent map |
| single forward pass의 correspondence가 geometry ambiguity를 해소 | post-processing 제거를 위해 필요 | textureless/repetitive scene은 scale/pose ambiguity |

- **Ablation to request if absent:** remove the paper-specific core module while holding input, data, compute, horizon and controller interface fixed.
- **Failure evidence location:** [04_evaluation.md](./04_evaluation.md)의 failure/limitation 및 reproducibility cue; 현재 note에 새로운 failure claim을 만들지 않는다.

## Reproduction Checklist

1. [ ] 01 overview와 source anchor에서 observation/state/action, exact notation과 model assumptions를 확인한다.
2. [ ] Pipeline의 각 module을 input/output contract와 함께 구현하고, source-specific equation/solver/decoder를 고정한다.
3. [ ] Training/offline setup, inference rate, horizon, memory, compute budget을 분리해 기록한다.
4. [ ] 04의 baseline과 module-removal/variant ablation을 같은 task, data, seed, budget으로 실행한다.
5. [ ] primary metric뿐 아니라 failure mode, latency, assumption sensitivity와 closed-loop recovery를 보고한다.

## Verification Questions

- **Equation/source:** method/formulation cue: 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; equation 번호/page는 원문과 대조 필요
- **Module attribution:** 04의 baseline/ablation이 어느 pipeline module을 실제로 제거·대체하는가?
- **Runtime:** action horizon/chunk, memory window, inference rate와 low-level control rate가 각각 얼마인가?
- **Evidence boundary:** 현재 evidence level에서 직접 확인되지 않은 exact value, negative result, reproducibility detail을 추가하지 않았는가?
