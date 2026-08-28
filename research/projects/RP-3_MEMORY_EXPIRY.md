# RP-3 Phase-Aware Memory Expiry

- Status: `SCOPED / NEXT`
- Updated: 2026-08-28 KST
- Parent idea: [I-03 Phase-aware spatial memory with learned expiry](../RESEARCH_IDEAS.md#i-03-phase-aware-spatial-memory-with-learned-expiry)
- Primary gap: [G-04 Persistent spatial memory staleness and uncertainty](../RESEARCH_GAPS.md#g-04-persistent-spatial-memory의-staleness와-uncertainty)
- Primary environment: `RoboCasa` dynamic manipulation tasks
- Secondary transfer: `RLBench` state-change task subset
- Hypothesis evidence: `UNTESTED`
- Novelty status: `CONDITIONALLY_FIT` — persistent memory, sparse retrieval, drift mitigation, memory-trap rollback은 이미 존재한다. novelty는 item-level validity·unsafe-action risk calibration과 selective expiry/verification이 closed-loop safety–success trade-off를 개선할 때만 성립한다.

이 프로젝트는 새로운 3D map이나 대형 VLA를 만드는 연구가 아니다. frozen visuomotor/VLA policy와 고정 memory representation 위에서, **현재 task phase가 바뀐 뒤 어떤 memory item을 계속 믿고, 갱신하고, 폐기하고, 다시 관측해야 하는지**를 결정하는 lightweight memory supervisor를 검증한다.

## 0. 연구 범위와 시스템 경계

| 구분 | RP-3가 다루는 것 | 현재 주장하지 않는 것 |
|---|---|---|
| 입력 | observation/action history, retrieved memory items, age, geometric confidence, non-privileged progress/phase proxy | simulator object state·instance ID·perturbation label을 inference input으로 사용하는 것 |
| 출력 | queried memory item별 `RETAIN`, `REFRESH`, `EXPIRE`, `VERIFY` 결정과 calibrated validity/risk | 새로운 low-level robot controller나 foundation memory backbone 학습 |
| 실행층 | 고정 downstream policy에 노출할 memory set과 추가 관측 여부 제어 | 모든 mapping drift, SLAM loop closure, active perception을 한 번에 해결하는 것 |
| 1차 검증 | RoboCasa의 relocation·removal·phase transition·delayed observation | simulator 결과만으로 real-world lifelong memory safety를 보장하는 것 |
| 후속 검증 | RLBench transfer 또는 제한된 real setup | base policy·memory encoder·task를 동시에 바꾸며 expiry 효과를 주장하는 것 |

RP-3의 closed loop는 다음과 같다.

`observation → persistent memory → task-relevant retrieval → validity/risk supervisor → memory action → downstream policy → environment transition → memory update`

첫 실험에서는 전역 memory의 모든 항목을 조합적으로 관리하지 않는다. 현재 instruction/subgoal이 조회한 top-k object·region·state item만 supervision과 expiry decision의 대상이다. 이 제한으로 method gain을 memory search-space 증가가 아니라 validity decision에 귀속한다.

## 1. 연구 질문과 claim ladder

### 핵심 질문

> object relocation·removal·drawer/receptacle state transition 뒤 memory item의 validity와 그 item을 사용할 때의 unsafe-action probability를 calibration해 `retain / refresh / expire / verify`를 선택하면, persistent memory·fixed TTL·similarity refinement·sparse retrieval·rollback보다 stale-memory-induced unsafe action을 줄이면서 task success와 observation budget을 유지할 수 있는가?

### 검증 가설

- **H0 — Memory-causality precondition:** 동일 world state에서 fresh-oracle, stale-persistent, masked-memory branch의 action/outcome이 구분된다. stale memory가 no-memory보다 해롭지 않거나 fresh memory가 유용하지 않으면 expiry project를 진행하지 않는다.
- **H1 — Validity calibration:** phase·age·geometric confidence를 사용하는 supervisor는 fixed TTL 또는 confidence-only baseline보다 memory validity와 unsafe-use risk의 Brier/ECE·selective risk를 개선한다.
- **H2 — Closed-loop safety:** shift episode에서 제안 supervisor는 strongest non-privileged baseline보다 stale-memory-induced unsafe action을 줄이고 Memory-Shift Completion Rate를 높인다.
- **H3 — Observation-cost gate:** H2의 이득은 verify/re-scan 횟수와 latency를 무제한으로 늘려 얻은 것이 아니며, 같은 verification budget에서 유지된다.
- **H4 — Generalization:** task 또는 state-change family를 hold-out해도 validity calibration과 safety–success gain이 유지된다.

### 세부 연구 질문

- **RQ0 — Downstream memory use:** base policy가 retrieved memory를 실제 action에 사용하는가? oracle fresh memory와 no-memory가 동률이면 policy interface가 병목이다.
- **RQ1 — Staleness harm:** stale item을 노출한 branch가 masked/fresh branch보다 empty grasp, invalid placement, collision 또는 progress regression을 더 자주 만드는가?
- **RQ2 — Phase의 필요성:** age·similarity가 같아도 subgoal/scene-state transition 이후 최적 memory action이 달라지는가?
- **RQ3 — Expire와 verify의 구분:** 불확실한 item을 항상 삭제하거나 항상 다시 관측하는 것보다 calibrated selective decision이 유리한가?
- **RQ4 — 병목 분해:** state-change detection, item association, validity calibration, downstream policy sensitivity 중 무엇이 safety–success trade-off를 제한하는가?
- **RQ5 — 전이성:** 동일 supervisor가 unseen object category, task template, perturbation family 또는 RLBench adapter로 옮겨가는가?

### Claim ladder

| Level | 주장 | 필요한 증거 |
|---|---|---|
| `C0` | dynamic-memory perturbation·branch evaluator | reproducible state change, memory provenance, branch equivalence, unsafe-action annotation |
| `C1` | calibrated memory expiry/verification이 fixed update rule보다 유리 | H0 통과, H1/H2, verification-budget matching, oracle decomposition |
| `C2` | state-change/task family 일반화 | hold-out family 또는 RLBench에서 frozen supervisor transfer |
| `C3` | real-world memory safety improvement | 실제 perception/association error와 physical safety metric을 포함한 별도 검증 |

현재 목표는 `C1`이다. H0가 성립하지 않으면 method를 만들지 않고 memory-causality/evaluation 결과 또는 downstream policy-interface 문제로 축소한다.

## 2. Novelty boundary와 논문 기반

### 이미 해결된 범위

- persistent multi-view spatial memory와 dynamic refinement 자체는 SOMA가 다룬다.
- state-aware scene graph와 observed transition update 자체는 MomaGraph가 다룬다.
- task-relevant sparse retrieval과 accumulated drift 완화는 Memory Retrieval/HALO가 직접 탐색한다.
- memory trap detection과 high-affordance rollback은 Affordance Field Intervention이 다룬다.
- open-set 3D feature fusion과 semantic map construction은 ConceptFusion 계열의 범위다.

따라서 RP-3는 “memory가 stale해진다”, “retrieval이 필요하다”, “rollback을 추가한다”, “3D memory를 만든다”를 contribution으로 주장하지 않는다. 남은 연구 단위는 다음 세 가지의 결합이다.

1. task-retrieved **item-level validity probability**,
2. 해당 item을 policy에 노출할 때의 **unsafe-action probability**,
3. validity·risk·phase·observation cost에 따른 **selective retain/refresh/expire/verify decision**.

### 방법론과 평가에서 차용할 요소

| 근거 | 차용하는 요소 | 그대로 주장하지 않을 부분 | Evidence level |
|---|---|---|---|
| [POMDP](../../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) | hidden world state 대신 history-conditioned belief를 쓰는 formulation | finite memory가 true state를 복원한다는 가정 | registry foundation |
| [ConceptFusion](../../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) | object/region feature와 geometry를 가진 persistent map interface | open-set representation accuracy가 control safety를 보장한다는 해석 | registry anchor; note maturity `UNREAD` |
| [MomaGraph](../../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | observed state-transition graph와 state-aware update | graph reasoning 성능을 expiry calibration 결과로 해석하는 것 | G-04 full-text audit |
| [SOMA / Spatial Memory for OOV Manipulation](../../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) | multi-view persistent memory, dynamic refinement, RoboCasa evaluation cue | SOMA-style refinement가 item validity를 calibration한다고 가정하는 것 | G-04 full-text audit |
| [Memory Retrieval/HALO](../../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | task-relevant sparse retrieval과 drift-aware comparison | full method·수치·limitation을 정독 전에 확정하는 것 | `SOURCE-VERIFIED / CURATION_ONLY` |
| [Affordance Field Intervention](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Affordance_Field_Intervention_Enabling_VLAs_to_Escape_Memory_Traps_in_CVPR_2026_paper.html) | memory-trap detection과 rollback intervention baseline | rollback이 item-level expiry·risk calibration을 해결한다는 해석 | `SOURCE-VERIFIED` |

HALO와 AFI는 direct counter-evidence이므로 strong baseline family로 다루되, 저자 코드·input·intervention contract를 동일 조건으로 맞추지 못하면 `-style` adaptation과 원 논문의 reported result를 구분한다.

## 3. Benchmark와 base-policy 결정

### Benchmark 선택

| 항목 | RoboCasa | RLBench | 결정 |
|---|---|---|---|
| state transition | drawer/receptacle/object state를 포함한 household manipulation | 다양한 task와 object-state variation | RoboCasa를 primary로 사용 |
| perturbation/restore | simulation state와 object pose/state mutation 필요 | secondary adapter에서 같은 taxonomy 재현 | Phase 0에서 restore·mutation validity 확인 |
| memory relevance | OOV·multi-step·scene state를 가진 task family 구성 가능 | simpler transfer와 task-family holdout 가능 | RLBench는 C2 transfer |
| base policy | frozen compatible checkpoint 또는 고정 visuomotor/VLA adapter 필요 | 동일 memory supervisor를 policy-specific adapter로 연결 | policy competence gate 후 진행 |

Primary task는 공식 이름을 문서에서 추정해 고정하지 않는다. Phase 0에서 다음 네 **task template**에 해당하는 RoboCasa task와 compatible checkpoint를 찾아 `rp3_task_manifest_v1.json`에 exact ID·environment commit·checkpoint hash를 기록한다.

1. object retrieval after initial scan,
2. drawer/cabinet state transition 후 grasp 또는 placement,
3. multi-object task 중 target/receptacle relocation,
4. out-of-view placement 또는 delayed re-observation.

### Base-policy 계약

- base policy, visual encoder, action horizon, controller, memory injection point를 모든 baseline에서 고정한다.
- 최초 후보는 기존 RoboCasa-compatible visuomotor/VLA checkpoint다. compatible VLA가 없으면 고정 BC/diffusion-policy checkpoint로 C1을 검증하되, 결과를 VLA 일반화로 표현하지 않는다.
- persistent memory representation은 한 종류로 고정한다. map encoder를 baseline마다 다시 학습하지 않는다.
- Phase 0 task는 clean current-view 조건에서 충분한 successful rollout을 확보하고, oracle fresh memory가 no-memory보다 유용한 경우에만 채택한다.
- base-policy competence가 낮아 clean failure가 shift failure보다 지배적이면 task를 바꾸거나 checkpoint를 개선한 뒤 새 manifest version으로 재시작한다.

## 4. Memory state와 selective decision

### Memory item schema

각 queried item은 다음 정보를 가진다.

```text
m_i(t) = {
  item_id, semantic_feature, pose_or_region,
  observed_state, geometric_confidence,
  last_seen_step, age, observation_source,
  retrieval_score, phase_at_write, provenance
}
```

simulator instance ID, true pose/state, perturbation cause는 label/evaluator에만 존재하며 inference schema에 넣지 않는다. association 결과가 바뀌면 새 item과 기존 item의 merge/split provenance를 보존한다.

### Memory action semantics

| Action | 고정 의미 | 비용 |
|---|---|---|
| `RETAIN` | item을 수정 없이 downstream policy context에 유지 | 추가 관측 없음 |
| `REFRESH` | 현재 observation에 item이 보일 때 feature·pose·state를 갱신 | 현재 frame 처리 비용 |
| `EXPIRE` | item을 invalid/unsafe로 mask하고 policy context에서 제거 | information coverage 감소 |
| `VERIFY` | 사전 등록한 camera/view action 또는 extra observation으로 item을 확인한 뒤 refresh/expire | verify call, observation step, latency |

`VERIFY`가 oracle teleport camera나 privileged state query를 사용하면 `VERIFY^oracle`로 분리한다. non-privileged P1은 모든 baseline과 같은 camera/view interface와 verification budget을 사용한다.

### 최소 formulation

```text
h_t = f(o_1:t, a_1:t-1, progress_t, phase_t)
v_i = P(memory_item_i is valid | h_t, m_i(t))
u_i = P(unsafe downstream action if item_i is exposed | h_t, m_i(t))
c_i(d) = expected observation, latency, and coverage cost for decision d

d_i* = argmin_d E[L_task(d)] + λu · u_i(d) + λcᵀ · c_i(d)
       where d ∈ {RETAIN, REFRESH, EXPIRE, VERIFY}
```

`phase_t`는 simulator task stage가 아니라 observation/action history와 progress proxy에서 추정한 non-privileged latent다. oracle phase는 O1 upper bound에서만 사용한다. 첫 implementation은 top-k item마다 독립 decision을 하고, joint combinatorial memory management는 범위 밖으로 둔다.

### 학습 target과 calibration

- `y_valid,i`: current world에서 item의 instance/state/pose가 사전 tolerance 안에 여전히 유효한지.
- `y_unsafe,i`: 동일 state의 short-horizon branch에서 item을 노출했을 때 invalid grasp/place, collision, unreachable action 또는 progress regression이 발생하는지.
- `y_decision,i`: fixed decision library를 branch-sweep했을 때 safety gate를 만족하며 task loss와 observation cost가 가장 작은 action set.
- validity/risk head는 fit split에서 학습하고 temperature/isotonic calibration은 calibration split에서만 고정한다.
- test의 oracle state와 branch outcome은 evaluation/O2에만 사용하고 head fitting·threshold tuning에 재사용하지 않는다.

## 5. Perturbation·label·data protocol

### Controlled memory-shift taxonomy

| Shift family | 조작 | stale memory가 만드는 대표 위험 | 적용 phase |
|---|---|---|---|
| `RELOCATION` | target 또는 receptacle을 reachable한 다른 pose로 이동 | old pose로 reach/grasp/place | pre-grasp, transport, pre-place |
| `REMOVAL_REAPPEARANCE` | item을 scene에서 제거하거나 다른 view에 재등장 | empty grasp, duplicate/false association | post-scan, between-subgoals |
| `STATE_TRANSITION` | drawer/door/receptacle의 open/closed 또는 occupancy 상태 변경 | invalid approach·placement·collision | subgoal transition |
| `DELAY_DROPOUT` | observation 또는 memory update를 N step 지연·누락 | old state 유지, late refresh | transition 직후 |
| `ASSOCIATION_NOISE` | feature/pose perturbation으로 merge/swap 유도 | wrong-object action | Phase 2 sensitivity |

각 family는 S1/S2 severity를 사전 등록한다. arbitrary wall-clock percentage 대신 `post_scan`, `pre_grasp`, `post_grasp`, `pre_place`, `between_subgoals` landmark에서 삽입한다. task semantics와 맞지 않는 cell은 `not_applicable`로 manifest에 남긴다.

### Unsafe-action operational definition

unsafe action은 단순한 최종 task failure가 아니다. evaluator가 다음 event 중 하나를 관찰할 때 기록한다.

- 제거되거나 이동한 item의 old pose에 대한 empty grasp/reach,
- closed·occupied·invalid receptacle에 대한 placement/approach,
- wrong instance 선택 또는 duplicate memory association에 따른 action,
- collision·joint/workspace safety predicate violation,
- 이미 달성한 progress를 되돌리는 task-invalid action.

`stale-memory-induced` attribution은 동일 environment/policy state에서 stale branch는 위 event를 만들고 fresh-oracle 또는 memory-masked branch는 만들지 않는 paired case로 제한한다. evaluator-only oracle을 써서 attribution하되 P1 input에는 넣지 않는다.

### Data layer와 provenance

| Layer | 생성물 | 역할 |
|---|---|---|
| `M0-clean` | clean base-policy rollout과 current-view observation | competence·clean non-degradation |
| `M1-memory` | memory write/retrieve/update stream | item age, source, phase, association provenance |
| `M2-shift` | controlled state-change event stream | onset, severity, oracle current state |
| `M3-branch` | same-state fresh/stale/masked/decision branch outcome | H0, unsafe-use attribution, oracle decision set |
| `M4-transfer` | held-out task/family 또는 RLBench rollout | C2 generalization |

모든 artifact에는 `environment_commit`, `task_id`, `base_policy_hash`, `memory_encoder_hash`, `supervisor_id`, `shift_recipe`, `onset_state_hash`, `decision_budget`, `seed`, `schema_version=rp3.memory.v1`을 기록한다.

### Split 계약

- `fit`: task template 2개와 state-change family 일부. validity/risk head 학습.
- `calibration`: 별도 task template 1개 또는 disjoint initial state와 seed. threshold와 calibration만 결정.
- `confirmatory-test`: hold-out task template 1개와 최소 한 개 unseen shift family/landmark. 학습·threshold 변경 금지.
- exact task, initial state, shift recipe, seed는 `rp3_split_v1.json`과 `rp3_factor_manifest_v1.json`에 고정한다.
- 동일 `(task, onset_state_hash, shift, severity, seed)`는 split을 넘지 않는다.

## 6. Baseline, oracle, ablation

### 실행 baseline

| ID | Memory policy | Decision | 검증 목적 |
|---|---|---|---|
| B0 | current-view only | memory를 사용하지 않음 | memory utility와 base competence |
| B1 | persistent memory | 모든 retrieved item `RETAIN` | stale-memory negative control |
| B2 | fixed TTL | age threshold를 넘으면 `EXPIRE` | 가장 단순한 expiry baseline |
| B3 | confidence-only | geometric/retrieval confidence threshold | phase 없이 uncertainty만으로 충분한지 |
| B4 | SOMA-style refinement | visible item refresh와 similarity-based refinement | dynamic refinement strong baseline |
| B5 | HALO-style sparse retrieval | task-relevant top-k retrieval, 별도 expiry 없음 | retrieval만으로 staleness가 해결되는지 |
| B6 | AFI-style rollback | trap detector가 recent high-affordance state로 rollback | 사후 intervention과 사전 expiry 비교 |
| B7 | verify-all | 불확실한 retrieved item을 항상 `VERIFY` | observation을 많이 쓰는 ceiling/비용 baseline |
| P1 | phase-aware calibrated supervisor | `RETAIN/REFRESH/EXPIRE/VERIFY` 선택 | 제안 방법 |

B4–B6는 저자 구현을 동일 policy/environment에 이식할 수 있을 때만 원 method 이름으로 부른다. 그렇지 않으면 구현 차이를 명시한 `-style adaptation`으로 보고한다. 모든 방법은 같은 base policy, memory encoder, retrieved top-k, camera interface, horizon, verify budget을 공유한다.

### Oracle decomposition

| ID | 제공하는 oracle | 해석 |
|---|---|---|
| O0 | fresh current-world memory | memory representation과 downstream policy의 ceiling |
| O1 | true phase·item validity, learned decision cost | state-change/validity inference 병목 분리 |
| O2 | same-state decision branch sweep의 best feasible action | 현재 decision library의 empirical upper bound |
| O3 | true validity로 stale item mask, 추가 verify 없음 | expiry 자체의 maximum value와 verification 필요성 분리 |

O0–O3는 privileged diagnostic이며 P1의 일반 baseline이나 state-of-the-art 비교에 넣지 않는다.

### 필수 ablation

| ID | 제거/변경 요소 | 검증하는 주장 |
|---|---|---|
| A1 | phase/progress feature 제거 | phase transition 정보의 필요성 |
| A2 | item age 제거 | temporal staleness의 필요성 |
| A3 | geometric/retrieval confidence 제거 | association·geometry uncertainty의 필요성 |
| A4 | unsafe-use head 제거하고 validity만 사용 | downstream action risk를 별도 예측할 필요성 |
| A5 | `VERIFY` 제거 | expire 대 active confirmation의 구분 |
| A6 | calibration 제거, raw score threshold | calibrated selective decision의 필요성 |
| A7 | branch-derived unsafe target 없이 item-validity target만 사용 | closed-loop action label의 필요성 |

A1–A7은 같은 split, head capacity, training budget, memory/verify interface에서 실행한다. 제거해도 P1과 동률인 component는 contribution에서 제외한다.

## 7. Metric과 통계

### Memory-causality prerequisite

- **Fresh-memory utility:** O0와 B0의 task success/action quality 차이.
- **Stale-memory harm:** B1과 B0/O3의 unsafe-action 및 success 차이.
- **Branch disagreement:** 동일 onset에서 fresh, stale, masked branch의 first action target 또는 short-horizon outcome이 달라지는 비율.
- **Oracle expiry value:** O2/O3와 strongest fixed baseline 사이의 safety–success–observation-cost gap.

이 값이 실질적으로 구분되지 않으면 P1을 학습하지 않는다.

### Primary outcome과 safety gate

**Memory-Shift Completion Rate (MSCR)**

```text
MSCR = mean[goal_success ∧ within_horizon ∧ within_verify_budget ∧ no_safety_violation | memory-shift episode]
```

**Stale-Memory-Induced Unsafe Action Rate (SMUAR)**

```text
SMUAR = mean[paired stale branch unsafe ∧ fresh/masked branch safe | valid paired branch]
```

P1은 strongest non-privileged baseline보다 MSCR을 개선하면서 SMUAR을 낮추거나 최소한 악화시키지 않아야 한다. 하나만 개선되면 safety–success Pareto 결과로 제한해 해석한다.

### Secondary metric

- item validity Brier score, ECE, AUROC/AUPRC,
- unsafe-use Brier/ECE와 risk–coverage curve,
- stale retain, false expire, unnecessary refresh/verify rate,
- task success, empty grasp, invalid placement, collision, progress regression,
- verify call, extra observation step, camera/view travel proxy, p50/p95 latency,
- task/shift/severity/onset별 MSCR·SMUAR와 worst-group 성능,
- memory size, retrieval top-k, update frequency, supervisor compute.

### 비교와 confidence interval

- 같은 `task × initial state × shift × severity × onset × seed`를 paired block으로 사용한다.
- primary effect는 `ΔMSCR`와 `ΔSMUAR`의 absolute percentage point 및 95% paired cluster-bootstrap CI로 보고한다.
- initial practical margin은 `ΔMSCR ≥ +5 pp`, `ΔSMUAR ≤ -5 pp` 또는 safety non-inferiority upper margin `+1 pp`, clean success 하락 `≤3 pp`다. 이는 문헌 상수가 아니라 Phase 1 전 고정할 내부 decision margin이다.
- H1 calibration metric과 H2 primary outcome을 분리하고, secondary multiple comparison은 Holm correction과 raw subgroup count를 함께 보고한다.
- Phase 0 variance는 confirmatory trial 수 산정에만 사용하며 결과를 본 뒤 margin·test split을 변경하지 않는다.

### Protocol validity

- **state mutation validity:** perturbation이 의도한 object/state만 바꾸고 task가 여전히 사전 정의된 recoverability 범위에 있는 비율.
- **branch equivalence:** decision 직전 environment, policy/controller, observation, memory hash가 의도한 memory branch 차이 외에는 일치하는 비율.
- **memory provenance completeness:** write/retrieve/refresh/expire/verify event가 item ID와 source를 보존한 비율.
- **unsafe annotation agreement:** task predicate와 branch outcome evaluator가 unsafe event를 일관되게 판정하는 비율.
- **replay determinism:** 같은 onset hash와 seed에서 action/outcome이 tolerance 안에서 재현되는 비율.

invalid episode를 조용히 제거하지 않고 수와 사유를 flow table로 보고한다.

## 8. 실험 단계

### Phase 0 — Memory-causality pilot

첫 산출물은 learned supervisor가 아니라 **20–50개 valid memory-shift onset의 paired branch table**이다.

1. 2개 task template에서 clean/current-view competence와 memory retrieval을 확인한다.
2. `RELOCATION`, `REMOVAL_REAPPEARANCE`, `STATE_TRANSITION`, `DELAY_DROPOUT`의 S1 onset을 수집한다.
3. 동일 state에서 B0 no-memory, B1 stale-persistent, O0 fresh memory, O3 oracle mask를 실행한다.
4. fresh-memory utility, stale-memory harm, branch disagreement, oracle expiry value를 계산한다.
5. H0를 통과한 경우에만 P1 validity/risk head와 four-way decision을 구현한다.

### Phase 1 — Minimum decision experiment

| Factor | Pilot value |
|---|---|
| task templates | 4개; exact RoboCasa ID는 manifest에 고정 |
| shift family | relocation, removal/reappearance, state transition, delay/dropout |
| severity | S1, S2 |
| initial states | task당 10개를 시작점으로 하고 Phase 0 variance로 확정 |
| split | 2 fit / 1 calibration / 1 holdout task, unseen landmark/family 포함 |
| systems | B0–B7, P1, O0–O3, A1–A7 중 사전 등록 shortlist |
| budgets | native horizon 고정, verify call `{0, 1, 2}` sensitivity |

Phase 1은 method selection용 development 결과다. B4–B6 재현 여부, threshold, top-k, practical margin은 confirmatory test 전에 고정한다.

### Phase 2 — Confirmatory RoboCasa

- Phase 1에서 고정한 base policy·memory encoder·supervisor를 유지한다.
- task 또는 shift family를 완전히 hold-out하고 strongest baseline, P1, O1/O2, 핵심 ablation만 실행한다.
- clean, ID shift, unseen shift를 분리해 MSCR/SMUAR, calibration, verify cost, latency, worst-group table을 보고한다.
- recipe·threshold·unsafe definition을 바꾸면 `rp3.memory.v2`로 올리고 Phase 1과 confirmatory 결과를 섞지 않는다.

### Phase 3 — RLBench transfer

- RoboCasa taxonomy를 relocation, object removal, articulated-state transition, delayed observation으로만 변환하고 benchmark-specific oracle field는 supervisor input에서 제외한다.
- RoboCasa에서 학습한 supervisor의 frozen zero-shot 결과와 RLBench calibration-only 결과를 분리한다.
- 동일 base-policy family를 사용할 수 없으면 memory supervisor만 transfer하고 policy change를 별도 factor로 보고한다.
- C2는 최소 한 개 unseen task/shift family에서 calibration과 MSCR/SMUAR 방향이 유지될 때만 주장한다.

### Phase 4 — Optional real-robot validation

- bounded relocation, target removal, drawer state change처럼 손상 위험이 낮은 perturbation부터 사용한다.
- simulator supervisor의 zero-shot, calibration-only, real-data fine-tuned 결과를 분리한다.
- empty grasp, invalid placement, collision/contact, emergency stop, operator intervention, verify latency를 기록한다.
- 실제 trial이 없으면 C3와 physical safety claim은 `NOT_RUN`으로 둔다.

## 9. Reject / revise 기준

| 결과 | 결정 |
|---|---|
| O0 fresh memory가 B0 no-memory보다 유용하지 않음 | `REJECT memory-interface claim`: downstream policy가 memory를 사용하지 않음 |
| B1 stale memory가 B0/O3보다 해롭지 않음 | `REJECT expiry claim`: 선택한 task/shift에서 staleness가 action bottleneck이 아님 |
| O2/O3도 fixed TTL·confidence baseline보다 낫지 않음 | decision library 또는 perturbation이 차별적 가치를 만들지 못함 |
| B2 fixed TTL 또는 B3 confidence-only가 P1과 동률 | learned phase-aware contribution을 제거하고 단순 rule로 축소 |
| A1 no-phase가 P1과 동률 | phase-aware claim을 제거하고 uncertainty/age calibration으로 축소 |
| A4 no-risk-head 또는 A7 validity-only가 P1과 동률 | unsafe-action modeling claim을 제거하고 item validity 문제로 축소 |
| verify-all B7만 이기고 matched verify budget에서 P1 이득이 없음 | selective supervisor claim 기각; observation policy 문제로 이동 |
| MSCR은 오르지만 SMUAR 또는 clean success gate 실패 | safety claim 기각; task-performance-only 결과로 `REVISED` |
| calibration split에서는 좋지만 hold-out family ECE/selective risk 악화 | cross-family claim 기각; family-specific calibration으로 축소 |
| P1 latency가 policy deadline을 넘고 latency-matched gain이 사라짐 | online supervisor claim 철회 |
| test task·seed·threshold가 fit/calibration에 재사용됨 | confirmatory 결과 무효; 새 protocol version으로 재실행 |

## 10. 필요한 코드·데이터·연산 자원

### 코드

- pinned RoboCasa/robosuite environment와 exact task configuration,
- frozen base-policy rollout adapter와 memory injection hook,
- persistent object/region memory store와 task-relevant retrieval interface,
- state-change perturbation/landmark wrapper,
- environment·policy·memory branch snapshot/restore runner,
- `rp3.memory.v1` JSONL logger와 artifact store,
- validity/risk calibration, paired-bootstrap, selective-risk evaluator,
- optional RLBench adapter.

### 데이터

- clean base-policy rollout과 retrieved memory stream,
- controlled memory-shift event와 oracle current-world annotation,
- same-state fresh/stale/masked/decision branch table,
- item validity, unsafe-use, decision cost target,
- `rp3_task_manifest_v1.json`, `rp3_split_v1.json`, `rp3_factor_manifest_v1.json`, `rp3_protocol_v1.yaml`,
- system별 paired MSCR/SMUAR, calibration, verify cost, latency table.

### 연산 및 저장 계획

- frozen policy와 memory feature cache를 우선 사용하고 foundation model full fine-tuning은 범위 밖이다.
- single GPU에서 validity/risk head를 학습하며, 실제 memory와 throughput은 Phase 0에서 측정한다.
- rollout 수보다 same-state branch와 image/depth/memory artifact가 저장량을 결정하므로 첫 20–50 onset에서 episode size를 측정한다.
- 환경 dependency는 pinned environment/container로 고정하고 project artifact에는 commit·checkpoint·schema hash를 남긴다.

## 11. 즉시 구현 순서

1. RoboCasa task와 compatible base-policy 후보를 감사하고 exact environment/checkpoint를 고정한다.
2. 2개 pilot task에서 clean competence, oracle fresh-memory utility, memory injection이 action을 바꾸는지 확인한다.
3. `rp3.memory.v1` logger와 environment/policy/memory branch snapshot test를 구현한다.
4. 네 S1 shift family에서 20–50개 valid onset을 수집한다.
5. B0, B1, O0, O3 paired branch로 H0 memory-causality gate를 판단한다.
6. gate를 통과하면 B2 fixed TTL, B3 confidence-only, B7 verify-all을 먼저 고정한다.
7. phase/context encoder와 item validity·unsafe-use head를 학습해 P1/O1/O2를 실행한다.
8. SOMA/HALO/AFI-style baseline과 A1–A7을 같은 memory·observation budget으로 비교한다.
9. Phase 1 gate를 통과한 경우에만 confirmatory RoboCasa와 RLBench transfer로 확장한다.
