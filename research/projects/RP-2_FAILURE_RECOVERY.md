# RP-2 Failure-to-Recovery Loop

- Status: `SCOPED`
- Updated: 2026-08-13 KST
- Parent ideas: [I-12 Recovery event protocol](../RESEARCH_IDEAS.md#i-12-recovery-event-protocol-for-existing-long-horizon-benchmarks) → [I-02 Risk-budgeted typed recovery](../RESEARCH_IDEAS.md#i-02-risk-budgeted-typed-recovery-for-vla)
- Primary benchmark: `LIBERO-Long` (`libero_10`)
- Secondary validation: `CALVIN` long-horizon five-subtask sequences
- Hypothesis evidence: `UNTESTED`

이 문서는 새 foundation model을 만드는 계획이 아니다. 기존 VLA와 failure detector를 고정하고, **failure가 발생한 뒤 어떤 recovery option을 선택해야 하는지**를 동일한 시간·행동·위험 예산 아래 검증하는 최소 프로젝트 명세다. I-12는 공통 측정 도구이고 I-02가 그 위에서 검증할 방법 가설이다.

## 1. 연구 질문

### 핵심 질문

> VLA의 calibrated failure alert를 `failure cause × recoverability × remaining budget`으로 해석해 recovery option을 선택하면, 같은 detector와 같은 총 실행 예산을 쓰는 abort, blind retry, binary retry/reset, privileged replan보다 recoverable failure의 최종 완료율을 높이면서 irreversible failure를 늘리지 않는가?

### 검증 가설

- **H1 — Recovery efficacy:** R1–R3 failure에서 typed selector의 Budgeted Recovery Completion Rate가 가장 강한 non-privileged baseline보다 높다.
- **H2 — Safety gate:** typed selector의 irreversible failure rate는 가장 안전한 실행 가능한 baseline보다 악화되지 않는다.
- **H3 — Clean non-degradation:** perturbation이 없는 episode에서 불필요한 intervention 때문에 native task success가 3 percentage point를 초과해 하락하지 않는다.
- **H4 — Attribution:** oracle detector와 oracle recovery type을 줘도 이득이 없으면 detector가 아니라 recovery skill library 또는 task-state interface가 병목이다.

### novelty boundary

FLARE는 이미 error를 recoverable in-distribution `Retry`와 state-breaking/out-of-distribution `Reset`으로 나누고 recovery를 수행한다. FailSafe도 failure–recovery action pair 생성 문제를 다룬다. 그러므로 이 프로젝트는 “typed recovery가 처음”이라고 주장하지 않는다. 남은 검증 단위는 다음으로 제한한다.

1. binary retry/reset보다 세분된 **operational recoverability**와 option set,
2. 모든 방법에 적용되는 **동일한 time/action/risk budget**,
3. injection, onset, detection, intervention, recovery, terminal outcome을 분리한 **event protocol**,
4. detector 오류와 selector 오류를 분리하는 **oracle decomposition**,
5. LIBERO에서 시작해 CALVIN으로 옮길 수 있는 **benchmark-independent semantics**.

## 2. 기반 논문과 차용 방법

| 근거 | 차용하는 요소 | 그대로 주장하지 않을 부분 |
|---|---|---|
| [SAFE](../../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | frozen VLA latent feature, temporal failure score, functional conformal threshold | conformal alert가 곧 원인 진단이나 recovery guarantee라는 해석 |
| [Recovery RL](../../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | task policy와 recovery policy 분리, safety critic에 의한 switching | 하나의 recovery policy가 semantic failure type 전체를 해결한다는 가정 |
| [PDDLStream](../../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | symbolic predicate와 continuous feasibility를 잇는 replanning interface | 최소 LIBERO 실험부터 전체 PDDLStream domain을 새로 구축하는 것 |
| [FurnitureBench](../../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) | final success 외 phase/skill progress 기록 | FurnitureBench 고유 taxonomy를 다른 benchmark에 그대로 이식하는 것 |
| [AtomicVLA](../../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) | CALVIN의 failure 이후 termination이 recovery 측정을 왜곡할 수 있다는 문제 제기 | benchmark 결과와 실제 recovery capability를 동일시하는 것 |
| [CALVIN](../../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) | 언어 조건 five-subtask sequence와 task oracle | 첫 실패에서 sequence를 끝내는 표준 evaluator |
| [LIBERO](../../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) | fixed initial states, BDDL goal predicate, long-horizon task suite | lifelong-learning 평균만을 recovery 성능으로 해석하는 것 |

직접적인 frontier counter-evidence도 baseline 설계에 포함한다.

- [FLARE (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html): Retry/Reset 이진 recovery dispatcher. 반드시 strong baseline 또는 privileged binary upper bound로 둔다.
- [FailSafe (arXiv 2025)](https://arxiv.org/abs/2510.01642): failure generation과 executable recovery pair. peer-reviewed 결과와 구분해 perturbation/recovery-pair 설계의 참고로만 쓴다.
- [LIBERO-Safety (ECCV 2026)](https://libero-safety.github.io/): physical/semantic safety perturbation과 violation 평가. 표준 LIBERO pilot 이후 R4 안전성 검증용 확장으로 둔다.

### 제안 method의 최소 형태

대형 VLA를 다시 학습하지 않는다.

1. SAFE 방식으로 frozen VLA feature `z_1:t`에서 alert score를 계산한다.
2. 작은 temporal head가 `p(cause, recoverability | z_1:t, progress, budget)`을 출력한다.
3. 별도 option-value head가 각 고정 recovery option의 `P(goal completion)`과 `P(irreversible event)`를 예측한다.
4. selector는 남은 budget 안에서 irreversible-risk threshold를 만족하는 option 중 completion probability가 가장 높은 것을 고른다.
5. feasible option이 없으면 `ABORT_HELP`를 선택한다.

Conformal calibration은 alert threshold에만 적용한다. distribution shift가 있는 recoverability classification이나 option-value 전체에 같은 보장을 확장해 주장하지 않는다.

## 3. Benchmark 결정

| 항목 | LIBERO-Long | CALVIN | 결정 |
|---|---|---|---|
| 초기 상태 | task별 fixed initial states | sequence별 초기 상태와 neutral reset | paired option comparison은 LIBERO가 단순 |
| 성공 판정 | BDDL goal predicate, success 시 `done` | task oracle가 start/current state 변화를 판정 | 둘 다 사용 가능 |
| 표준 horizon | config 기본 `max_steps=600` | subtask당 `EP_LEN=360` | pilot budget은 LIBERO 600-step 안에 포함 |
| failure 이후 실행 | timeout 전까지 계속 실행 가능 | 표준 sequence evaluator가 첫 failed subtask에서 반환 | CALVIN은 evaluator fork 필요 |
| 장기 구조 | `libero_10`의 multi-object/articulated tasks | 5개 instruction sequence, 1,000 sequence 표준 평가 | CALVIN이 transfer validation에 적합 |
| simulator state clone/injection | MuJoCo state와 BDDL predicate 활용 가능 | scene/task oracle adapter 필요 | I-12 구현은 LIBERO부터 시작 |

**결론:** minimum experiment는 `LIBERO-Long`으로 확정한다. CALVIN은 event schema가 안정화된 뒤 두 번째 benchmark로 추가한다. 표준 LIBERO는 실제 물리적 위해를 충분히 표현하지 못하므로 R4 결과를 real-world safety claim으로 확대하지 않고, 이후 LIBERO-Safety 또는 실제 robot safety setup에서 별도로 확인한다.

공식 구현 감사 기준은 다음과 같다.

- [LIBERO metric implementation](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/lifelong/metric.py): fixed init state, `done`, max-step rollout을 사용하는 평가 루프.
- [LIBERO repository](https://github.com/Lifelong-Robot-Learning/LIBERO/tree/8f1084e3132a39270c3a13ebe37270a43ece2a01): 이번 설계에서 감사한 upstream commit.
- [CALVIN evaluator](https://github.com/mees/calvin/blob/fa03f01f19c65920e18cf37398a9ce859274af76/calvin_models/calvin_agent/evaluation/evaluate_policy.py): `EP_LEN=360`, `NUM_SEQUENCES=1000`, 첫 failed subtask에서 sequence 반환.
- [CALVIN repository](https://github.com/mees/calvin/tree/fa03f01f19c65920e18cf37398a9ce859274af76): 이번 설계에서 감사한 upstream commit.

## 4. I-12 Recovery event schema

### 저장 단위

- 한 episode에 하나의 immutable JSONL event stream을 저장한다.
- image/state/action tensor는 별도 artifact에 저장하고 event에는 `state_ref`, `observation_ref`, `action_ref`만 남긴다.
- benchmark-native log를 덮어쓰지 않고 adapter가 공통 field로 변환한다.
- evaluator가 아는 injection 정보와 policy가 실제로 볼 수 있는 정보는 분리한다. `t_inject`, oracle cause, oracle recoverability는 selector input으로 전달하지 않는다.

### Episode header

| Field | 의미 |
|---|---|
| `schema_version` | 최초 구현은 `rp2.event.v1` |
| `episode_id` | benchmark, task, init state, perturbation, seed로 만든 고유 ID |
| `benchmark`, `suite`, `task_id` | 예: `libero`, `libero_10`, BDDL task name |
| `instruction` | 현재 language goal 또는 subtask |
| `policy_id`, `checkpoint_hash` | base policy와 exact checkpoint |
| `detector_id`, `selector_id` | detector/selector ablation 식별자 |
| `seed`, `init_state_id` | paired comparison 재현 키 |
| `perturbation_id`, `severity` | perturbation family와 level |
| `native_horizon` | LIBERO pilot은 600 |
| `budget` | `recovery_steps`, `option_calls`, `replans`, `irreversible_events` |

### Event record

```json
{
  "schema_version": "rp2.event.v1",
  "episode_id": "libero10.task04.init03.action_grasp.s1.seed07",
  "event_id": 12,
  "t_step": 184,
  "sim_time": 6.13,
  "source": "detector",
  "event_type": "failure_alert",
  "failure_cause": "execution_contact",
  "recoverability": "R2",
  "confidence": 0.83,
  "option": null,
  "state_ref": "states/episode.npz#184",
  "observation_ref": "obs/episode.zarr#184",
  "action_ref": "actions/episode.npy#184",
  "budget_before": {"recovery_steps": 120, "option_calls": 2, "replans": 1},
  "budget_after": {"recovery_steps": 120, "option_calls": 2, "replans": 1},
  "metadata": {"threshold": 0.71, "detector_score": 0.76}
}
```

필수 `source`는 `environment_oracle`, `perturbation_wrapper`, `detector`, `selector`, `policy`, `evaluator`다. 필수 `event_type`은 다음과 같다.

`episode_start`, `task_progress`, `perturbation_injected`, `failure_manifested`, `failure_alert`, `recovery_selected`, `recovery_started`, `recovery_succeeded`, `recovery_failed`, `safety_violation`, `task_success`, `abort_help`, `timeout`, `episode_end`.

### 시간 정의

| Timestamp | 정의 |
|---|---|
| `t_inject` | evaluator가 perturbation을 가한 시각. 정책에는 비공개 |
| `t_effect` | oracle predicate 또는 progress invariant가 처음 깨져 failure가 실제로 나타난 시각 |
| `t_detect` | detector score가 사전 등록 threshold를 처음 넘은 시각 |
| `t_intervene` | selector가 base action을 중단하고 recovery option을 시작한 시각 |
| `t_recovered` | task-valid/recoverable set으로 복귀한 최초 시각 |
| `t_success` | benchmark-native goal predicate가 만족된 시각 |
| `t_terminal` | success, timeout, abort/help, irreversible event 중 하나로 끝난 시각 |

`t_inject`를 failure onset으로 사용하지 않는다. perturbation이 즉시 영향을 주지 않을 수 있기 때문이다. Detection delay는 `t_detect - t_effect`로 계산하며, predictive alert는 음수가 될 수 있다.

## 5. Perturbation 및 event taxonomy

Failure cause와 recoverability는 서로 다른 축으로 저장한다.

### Failure cause

| Cause | Pilot perturbation | Onset landmark | 대표 option |
|---|---|---|---|
| `observation_visibility` | RGB blackout, target occlusion, stale frame을 N step 주입 | pre-grasp 또는 pre-place | `REOBSERVE_WAIT` |
| `execution_contact` | transport 중 gripper open, 짧은 action dropout, grasp slip | post-grasp/transport | `RETRY_CURRENT`, `RETREAT_RESET` |
| `world_state` | reachable 영역 안에서 target/receptacle displacement | pre-grasp 또는 post-subgoal | `REOBSERVE_WAIT`, `REPLAN` |
| `plan_semantic` | drawer/microwave state를 되돌리거나 다음 subgoal의 전제조건 무효화 | subgoal 사이 | `REPLAN` |
| `safety_system` | critical object를 unreachable 영역으로 이동하거나 absorbing forbidden-contact predicate 발생 | interaction 직전/직후 | `ABORT_HELP` |

각 perturbation은 `S1/S2` 두 severity를 먼저 사용한다. arbitrary wall-clock percentage가 아니라 `pre_grasp`, `post_grasp_transport`, `pre_place`, `between_subgoals`의 state/event landmark에서 주입한다. task semantics에 맞지 않는 조합은 실행하지 않고 `not_applicable`로 기록한다.

### Operational recoverability

| Class | 판정 기준 | 허용되는 최소 recovery |
|---|---|---|
| `R0` | perturbation 없음 또는 progress invariant가 깨지지 않음 | `CONTINUE` |
| `R1_LOCAL` | 같은 instruction을 유지한 continue/retry가 local budget 안에 성공 | `CONTINUE`, `RETRY_CURRENT` |
| `R2_OPTION` | reobserve, retreat 또는 controller reset 중 하나가 있어야 성공 | `REOBSERVE_WAIT`, `RETREAT_RESET` |
| `R3_REPLAN` | task는 달성 가능하지만 현재 subgoal/plan의 전제조건이 무효 | `REPLAN` |
| `R4_EXTERNAL` | 고정 option library와 budget으로 달성 불가하거나 absorbing safety event 발생 | `ABORT_HELP` |

이 label은 failure의 본질적 속성이 아니라 **현재 option library와 budget에 조건부인 실험적 속성**이다. 최종 성공 결과 하나로 사후 라벨링하지 않는다. `t_effect`의 cloned simulator state에서 각 option을 같은 seed set으로 실행하고, 성공 가능한 가장 약한 option family로 oracle class와 acceptable-option set을 만든다. injection recipe의 예상 class와 oracle sweep 결과가 다르면 둘 다 저장하고 sweep 결과를 평가 label로 사용한다.

### Recovery option library

| Option | 고정 의미 |
|---|---|
| `CONTINUE` | base policy와 hidden/cache state를 유지 |
| `RETRY_CURRENT` | environment는 reset하지 않고 policy memory만 reset한 뒤 현재 instruction 재실행 |
| `REOBSERVE_WAIT` | zero/safe hold 후 fresh observation을 받고 현재 instruction 유지 |
| `RETREAT_RESET` | 충돌 없는 사전 등록 safe pose로 retreat하고 policy memory reset |
| `REPLAN` | 현재 privileged task predicates로 미완료 goal의 새 skill/subgoal 순서를 생성 |
| `ABORT_HELP` | safe stop 후 terminal escalation. simulator reset이나 성공으로 계산하지 않음 |

Option implementation은 모든 selector에서 공유한다. typed method만 더 강한 recovery skill을 쓰는 confound를 허용하지 않는다.

## 6. Recovery budget

가중합 하나가 아니라 다음 budget vector를 모든 방법에 동일하게 적용한다.

| Budget | Pilot 값 | 규칙 |
|---|---:|---|
| native episode horizon | 600 step | recovery를 위해 추가 horizon을 주지 않음 |
| recovery execution | 120 step | `recovery_started`부터 `t_recovered` 또는 failure까지 누적 |
| option calls | 2 | retry를 반복해 horizon을 우회하지 못하게 함 |
| replans/retreat resets | 1 | expensive intervention 제한 |
| irreversible event | 0 | 한 번 발생하면 safety gate 실패 |
| human escalation | 1 terminal call | 성공은 아니지만 R4 correct decision으로 별도 기록 |

Pilot 이후 `recovery execution ∈ {60, 120, 180}` sensitivity를 수행한다. budget을 다 쓴 뒤 recovery mode를 임의로 종료해 base action으로 위장하지 못하도록, `t_recovered`는 oracle task-valid predicate로만 닫는다.

## 7. Baseline과 oracle upper bound

### 실행 baseline

| ID | System | Detector | Recovery decision | 목적 |
|---|---|---|---|---|
| B0 | Clean native policy | 없음 | `CONTINUE` | clean competence sanity check |
| B1 | Perturbed native policy | 없음 | `CONTINUE` | perturbation damage negative control |
| B2 | SAFE + abort | 동일 SAFE | alert 시 `ABORT_HELP` | detection-only safety baseline |
| B3 | SAFE + blind retry | 동일 SAFE | 모든 alert에 `RETRY_CURRENT` | 가장 단순한 recovery baseline |
| B4 | SAFE + privileged replan | 동일 SAFE | 모든 alert에 simulator predicate 기반 `REPLAN` | planning interface의 강한 privileged baseline |
| B5 | FLARE-style binary dispatcher | learned 또는 oracle-labeled | local/ID는 `RETRY_CURRENT`, state-breaking/OOD는 `RETREAT_RESET` | 이미 발표된 binary retry/reset counter-evidence |
| P1 | SAFE + typed budgeted selector | 동일 SAFE | 6개 option 중 risk-constrained 선택 | 제안 방법 |

B4는 true simulator predicate를 보므로 일반 learned baseline으로 보고하지 않고 `PRIVILEGED`로 표시한다. PDDLStream 전체 구현은 continuous collision/kinematic feasibility가 실제 병목으로 확인될 때 CALVIN 또는 phase-2 extension에서 추가한다. 최소 LIBERO pilot에서는 task-specific predicate/skill graph replan으로 범위를 제한한다.

B5의 저자 코드를 동일 조건에서 재현하지 못하면 임의 구현을 FLARE 결과라고 부르지 않는다. 대신 oracle ID/OOD label을 쓰는 `privileged binary Retry/Reset`으로 이름을 바꾸어 binary taxonomy의 upper bound로 보고한다.

### 오류 분해와 upper bound

| ID | Detector | Selector | 해석 |
|---|---|---|---|
| O1 | oracle `t_effect` | learned typed selector | selector의 순수 오류와 detector delay 분리 |
| O2 | learned SAFE | oracle acceptable-option set | detector 병목과 option 선택 병목 분리 |
| O3 | oracle `t_effect` | cloned-state option sweep | 현재 option library와 budget의 empirical upper bound |

O3는 `t_effect` state를 clone하고 각 option을 같은 rollout seed로 실행한 뒤, 다음 lexicographic rule로 고른다.

1. irreversible event가 없는 option,
2. native goal을 budget 안에 완료하는 option,
3. 추가 step과 option cost가 가장 작은 option.

O3도 skill library 밖의 행동은 만들지 못하므로 task의 절대 oracle이 아니라 **현재 recovery interface의 upper bound**다.

## 8. Primary 및 secondary metric

### Primary outcome과 safety gate

**Budgeted Recovery Completion Rate (BRCR)**

R1–R3 perturbed episode 중 native goal을 600 step 안에 만족하고, option/replan budget을 넘지 않으며, irreversible event가 없는 비율이다.

```text
BRCR = mean[goal_success ∧ within_budget ∧ no_irreversible_event | R1–R3]
```

R4는 완료가 바람직한 outcome이 아니므로 BRCR 분모에서 제외하고 별도로 보고한다.

**Safety gate — Irreversible Failure Rate (IFR)**

전체 perturbed episode 중 absorbing safety violation 또는 recovery 불가능 상태로 전이한 비율이다. BRCR이 높아도 IFR non-degradation을 만족하지 못하면 H1을 지지하지 않는다.

### Secondary metric

- clean task success와 false-intervention rate
- R4 correct abort/help rate와 unnecessary abort rate
- failure detection AUROC/AUPRC, `t_detect - t_effect`, missed-alert rate
- cause macro-F1, recoverability macro-F1, acceptable-option accuracy
- intervention-conditioned recovery success
- recovery step, option call, replan count, total execution cost
- intervention 전후 유지된 task/subgoal progress
- task, cause, severity, onset landmark별 worst-group BRCR/IFR
- timeout rate와 post-recovery re-failure rate

모든 system은 동일 `init_state_id × perturbation × seed`에서 paired 비교한다. 95% stratified bootstrap confidence interval을 task와 failure family 단위로 보고하고, 평균만으로 subgroup failure를 숨기지 않는다.

## 9. 실험 행렬

### Phase 0 — Wrapper 및 oracle audit

아래 네 `libero_10` task를 사용한다.

1. `KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it`
2. `KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it`
3. `LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket`
4. `STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy`

articulated receptacle, multi-object sequence, precise placement를 함께 포함한다. 각 task에서 clean rollout과 state landmark를 먼저 검증하고, perturbation 직후 clone/restore가 deterministic tolerance 안에서 재현되는지 확인한다.

### Phase 1 — 최소 decision experiment

| 축 | 값 |
|---|---|
| tasks | 위 4개 LIBERO-Long task |
| perturbation | observation, execution/contact, world-state, plan-semantic |
| severity | S1, S2 |
| fixed initial states | task당 10개 |
| paired scenario | `4 × 4 × 2 × 10 = 320` / system |
| systems | B1–B5, P1, O1–O3 중 구현 가능한 전부 |
| clean audit | 4 task × 10 init state / 실행 system |

R4 perturbation은 각 task/init state에 무조건 곱하지 않고 별도 diagnostic set으로 둔다. standard LIBERO의 R4 결과는 simulator-specific correct-abort 성능으로만 해석한다.

### Phase 2 — Confirmatory LIBERO

- `libero_10` 전체 10 task
- task당 공식 fixed initial state 20개
- four perturbation families × two severity
- pilot에서 사전 등록한 strongest non-privileged baseline, typed selector, O3만 실행
- 예상 paired scenario: `10 × 20 × 4 × 2 = 1,600` / system

Phase 1 결과를 본 뒤 perturbation 정의나 threshold를 바꾸면 Phase 2에는 새 version을 부여하고 pilot과 confirmatory 결과를 섞지 않는다.

### Phase 3 — CALVIN transfer

- 고정된 100개 five-subtask sequence로 먼저 검증하고 표준 1,000 sequence는 최종 확인에만 사용한다.
- sequence의 2번째 또는 3번째 subtask에 perturbation을 삽입한다.
- 첫 subtask failure에서 반환하지 않고 남은 sequence와 post-recovery progress를 계속 기록하도록 evaluator를 fork한다.
- native five-task success count와 공통 BRCR/IFR/event metric을 함께 보고한다.
- LIBERO에서 학습한 detector/selector를 그대로 적용한 zero-shot 결과와 CALVIN calibration-only 결과를 분리한다.

## 10. Reject / revise 기준

아래 수치는 Phase 1 실행 전에 고정할 초기 decision rule이다. pilot variance가 지나치게 크면 효과 방향을 보고 threshold를 바꾸지 말고 trial 수 산정만 다시 한다.

| 결과 | 결정 |
|---|---|
| O3가 B3/B4/B5보다 BRCR 5 pp 이상 높지 않음 | `REJECT recovery-interface claim`: option library가 차별적 이득을 만들지 못함 |
| O3는 이기지만 O1 learned selector가 이기지 못함 | `REVISE selector`: detector가 아니라 type/value head 또는 training label 문제 |
| O1은 이기지만 P1이 이기지 못함 | `REVISE detector`: onset delay/calibration 병목 |
| P1이 strongest non-privileged baseline보다 BRCR 5 pp 이상 개선하고 paired 95% CI가 0을 제외하며 IFR non-degradation 만족 | H1 `SUPPORTED` 후보; Phase 2 진행 |
| P1의 IFR가 baseline보다 악화 | safety gate 실패; BRCR가 높아도 `REVISED` 또는 `REJECTED` |
| clean success가 B0 대비 3 pp 초과 하락 | alert/selector가 과민함; clean non-degradation 실패 |
| binary B5와 P1 차이가 없음 | multi-type claim 축소; retry/reset taxonomy로 충분한 조건을 분석 |
| 이득이 특정 perturbation/task에만 존재 | 범용 claim을 버리고 해당 subgroup 조건부 가설로 `REVISED` |
| LIBERO에서만 성립하고 CALVIN zero-shot에서 사라짐 | benchmark-specific state interface로 축소; cross-suite claim 기각 |

5 pp와 3 pp는 문헌의 보편적 상수가 아니라 프로젝트의 초기 practical-effect/equivalence margin이다. confirmatory trial 수는 Phase 0/1 variance로 power analysis한 뒤 확정한다.

## 11. 필요한 코드·데이터·연산 자원

### 코드

- pinned LIBERO environment와 `libero_10` BDDL/fixed initial states
- SAFE feature extractor, temporal detector, conformal calibration code
- base VLA rollout adapter. 첫 구현은 SAFE가 이미 연결한 OpenVLA 계열을 우선 사용
- perturbation wrapper와 landmark detector
- simulator clone/restore 및 oracle option-sweep runner
- fixed recovery option library와 task predicate/skill graph replanner
- JSONL event logger, artifact store, metric/paired-bootstrap evaluator
- CALVIN evaluator fork. upstream early-return 동작은 보존한 별도 baseline도 함께 유지

### 데이터

- base VLA checkpoint와 LIBERO-compatible policy configuration
- LIBERO fixed initial states와 task demonstrations/checkpoints
- clean success/failure rollout for SAFE calibration
- injected rollout: detector/type/value head의 train/calibration/test는 `task × init state × perturbation seed`가 겹치지 않게 분리
- option-sweep outcome table: 각 cloned onset state에서 option별 completion, irreversible event, step cost

실제 사용자 demonstration이나 대규모 foundation pretraining은 minimum experiment에 필요하지 않다. injected failure를 학습과 평가에 모두 쓸 때 exact perturbation seed와 onset state가 split을 넘지 않게 한다.

### 환경 및 연산 계획

- LIBERO와 SAFE의 dependency 세대가 다를 수 있으므로 각각 pinned environment/container를 만들고 event schema로만 연결한다.
- headless MuJoCo/EGL, 32–64 GB system RAM, rollout artifact용 약 100 GB 여유 공간을 초기 계획값으로 둔다.
- OpenVLA-class inference는 24 GB급 GPU 1장을 최소 실용 기준으로 잡되, 실제 memory와 throughput은 checkpoint/precision으로 Phase 0에서 측정한다.
- detector/type/value head는 frozen feature를 쓰므로 단일 GPU에서 학습한다. VLA full fine-tuning은 범위 밖이다.
- 총 episode 수보다 wall-clock이 정책 inference 속도에 크게 좌우되므로 Phase 0에서 `steps/sec`, GPU memory, episode artifact size를 측정한 뒤 Phase 1 실행 시간을 산정한다.

## 12. 즉시 구현 순서

1. LIBERO upstream commit과 base policy checkpoint를 고정한다.
2. 네 pilot task의 clean success와 state landmarks를 확인한다.
3. `rp2.event.v1` logger와 clone/restore test를 먼저 작성한다.
4. 네 perturbation family의 S1만 구현하고 oracle option sweep으로 R1–R4 label이 실제로 분리되는지 확인한다.
5. B1–B4와 O3를 먼저 실행한다. 이 단계에서 option library upper bound가 없으면 learned selector를 만들지 않는다.
6. SAFE detector를 연결해 B2–B5를 고정한다.
7. 작은 cause/recoverability head와 option-value head를 학습해 P1/O1/O2를 실행한다.
8. Phase 1 decision rule을 통과한 경우에만 full LIBERO와 CALVIN으로 확장한다.
