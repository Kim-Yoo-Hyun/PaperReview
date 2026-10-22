# D1-L4 — OFT 후보의 비실험 검증 계약

- 현재 실행 판단은 [N1–N4 재심사](./NONEXPERIMENTAL_REVIEW.md)를 우선한다. 기존 설계는 보존하되 method NO-GO·진단 HOLD로 자동 실행 queue에서 제외했다. G1은 competence·corruption/goal 반응 screening이며 유용한 proprioception의 필요성 입증과 구별한다. R2 연구 재심사 후에만 runtime qualification을 재검토한다.
- 작성: 2026-10-22 KST. 설계 버전 `d1-l4-v1`.
- 상태: **L4 문서·명세 완료 / native 실행 HOLD / 신규 방법 REVISE**. 모든 수치·조건은 아래 source 사실을 제외하면 연구자가 정한 pilot 설계이며 측정 결과가 아니다.
- 입력: [task 감사](./TASK_OBSERVABILITY_AUDIT.md), [주장·기각 계약](./CLAIM_EVIDENCE_CONTRACT.md), [baseline 방법 감사](./BASELINE_METHOD_AUDIT.md).
- 생성물: [PILOT_SPEC.json](./PILOT_SPEC.json), [추가 source identity](./contract_sources_2026-10-22.json), [문서 검증](VALIDATION.md#stage-4). Spec은 `executable=false`; runner·split ledger·실행 환경을 생성했다는 뜻이 아니다.
- E1 후속: [실제 Docker resource preflight](../../experiments/vla_d1_e1_preflight/RESULTS.md)를 수행했다. G0 전체 미충족·G1 미실행이며 normalizer 작은 파일 hash만 추가 확보했다. 아래 pilot 수치·조건을 실행 결과로 해석하지 않는다.

## 1. 이번에 고정한 범위

**OFT의 유용한 state/goal 사용이 확인된 task에서, report 오류를 고치는 연산이 정상적인 물리 변화에도 유익한가? 단순한 고정·causal 재보정으로 충분한가?**

Primary 후보는 proprio-enabled OpenVLA-OFT LIBERO-Goal의 task **0(서랍), 8(접시 위 bowl)**, language contrast는 **1(stove 위 bowl)**이다. Task 7은 보조 후보로 남기며 기본 실행 수에 포함하지 않는다. Task 정의와 정책 revision은 [기존 후보 명세](./TASK_CANDIDATES.json)를 그대로 참조한다. π0.5의 철회한 state 보정 경로를 다시 켜지 않는다.

최초 비교는 report-only orientation bias와 정상 controller로 만든 **초기 로봇 자세 변화**로 제한한다. 이 둘은 별도 intervention strata다. 전체 RGB/state/history가 같은 원인 쌍, 외력에 의한 contact disturbance, actuator 고장, absolute-orientation task를 확보했다고 주장하지 않는다. 후자의 조건들은 별도 qualification 뒤에만 추가한다. 첫 비교에서도 실제 행동 차이·관측 cue·강한 baseline 이후 gap이 없으면 D1 method 방향을 중단한다.

L4는 buildup 가이드의 6단계 최소 검증 설계와 내부 반박을 마무리한다. 7단계의 native 정책 evidence와 8단계 외부 피드백은 남아 있다. 현재 문헌 준비를 더 반복하는 것만으로 연구 가치 판정을 올리지 않는다.

## 2. Source에서 추가로 확인한 함정

| 확인 사실 | 계약에 반영한 결정 |
|---|---|
| OFT는 reset→initial state 설정→10회 wait 뒤 정책을 호출한다. Goal horizon은 300 action, 기본 queue는 8이다. 별도 JSON initial-state 경로는 expert 실패 기록을 건너뛴다 | Native qualification은 기본 `.pruned_init` 경로를 사용한다. Expert 성공 여부를 분할·유효성 기준으로 쓰지 않고 모든 시도와 제외 사유를 기록한다. [공식 eval source](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/libero/run_libero_eval.py#L278) |
| `set_init_state`는 simulator state 복원과 observable 갱신을 수행한다 | 이 호출만으로 policy queue·estimator·RNG·controller memory의 복원을 주장하지 않는다. [LIBERO wrapper](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/env_wrapper.py#L118) |
| 후보 robosuite의 flat state에는 time/qpos/qvel만 있고, LIBERO reset은 fixture의 model `body_pos/body_quat`도 바꾼다 | qpos hash만 같은 장면으로 인정하지 않는다. 실제 model 배치·camera·controller state까지 검사한다. [직렬화](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/utils/binding_utils.py#L213), [fixture 초기화](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/bddl_base_domain.py#L731) |
| 영 회전 command는 OSC의 직전 orientation goal을 유지할 수 있다 | Neutral command를 물리 정지·controller reset이라고 부르지 않는다. 속도·goal·접촉을 확인한다. [OSC source](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/controllers/osc.py#L257) |
| Native helper는 environment seed를 0으로 설정한다 | Native qualification은 env seed 0, policy seed 7을 명시한다. 같은 seed 또는 task별 같은 index가 동일 scene을 보장한다는 가정은 제외한다. [공식 helper](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/libero/libero_utils.py#L18) |

추가로 확인한 8개 text의 hash와 검토 line 범위는 source JSON에 있다. 이는 해당 조합의 runtime 호환성이나 OFT 논문 실험의 정확한 LIBERO revision을 입증하지 않는다.

## 3. 오류 위치·frame·실제 물리 변화

### R: policy report만 바꾸는 조건

Simulation 관측을 deepcopy한 **policy 전용 사본**에서 EEF body quaternion을 회전행렬 `R`로 읽고 `R_report = B R`, `B = Exp(theta [axis]×)`로 바꾼다. World-axis left multiplication이며 controller의 grip-site orientation, 실제 robot joints, RGB, position·gripper 값은 바꾸지 않는다. Native xyzw quaternion→axis-angle 변환 **이전**, proprio q01/q99 normalization **이전**에 개입한다. Axis-angle 성분에 theta를 단순 가산하지 않는다. 보정은 반대로 report 사본에서 실행한 뒤 기존 preprocessing을 한 번만 통과한다.

- G1 state-use screening: world-z `+0.10 rad`, 최초 query부터 episode 끝까지 고정. 이 특정 오류의 utility 검사이지 모든 state component의 중요도 검사가 아니다.
- G2 development 후보: world-z `theta ∈ {−0.20, −0.10, +0.10, +0.20} rad`, onset query 0. 값은 작은 후보 grid이며 실제로 task를 어렵게 만드는지는 미검증이다.
- Native state/raw corrected state/normalized state와 clip mask를 evaluator가 기록한다. Clip 때문에 서로 다른 입력이 같은 tensor가 되면 해당 state-use 해석은 실패한다. Clipping 발생 episode 자체를 성능 계산에서 몰래 제외하지 않는다.
- 회전 convention round trip, `B⁻¹ B R`, quaternion 부호 동등성, body/site 고정 변환, model과 controller world frame을 G0에서 확인한다. 이 항목의 실제 수치 오차는 아직 없다.
- Report fault의 GT B를 쓰는 D0는 privileged restoration이다. R에서 clean 입력을 복원하여 B0 수준으로 돌아오는 것은 구현 sanity check이며 관측만으로 fault를 알아냈다는 증거가 아니다.

### P: 정상 controller를 통한 초기 자세 변화

G2에서 모든 arm은 native 10 wait 후 **14-step 공통 길이의 prelude**를 갖는다. Nominal/R arm은 native dummy command `[0,0,0,0,0,0,−1]` 14회다. P arm은 환경에 전달하는 OSC command `[0,0,0,0,0,a,−1]` 4회, 이어 dummy 10회다. Development `a ∈ {−0.10,+0.10}`이며 7번째 값은 환경의 gripper-open convention이다. 이 명령에는 VLA의 gripper 재변환을 다시 적용하지 않는다.

`a`는 정규화된 action 성분이다. 후보 native rotation scaling을 적용한 목표 increment와 실제 자세 변화량은 다르다. 실제 body/site 회전·translation·velocity·contact를 측정하고 그 값으로 stratum을 설명한다. 이 설계는 qpos teleport나 외력 주입이 아니며 **정상적인 시작 자세 변화에 대한 robustness**만 시험한다. Native controller feedback은 계속 참 simulator state를 받는다. P에서 D0 true-state는 B0 입력과 같으므로 특별한 복구 oracle이 되지 않는다.

Prelude를 policy/history module에 보여 주지 않는다. 첫 query를 episode-local step 0으로 두고 모든 방법에 같은 post-prelude packet과 빈 history를 제공한다. 이는 숨겨진 고장 시점의 추론 문제가 아니라 초기 조건의 일반화 검사다. Extra prelude가 있는 G2 nominal B0를 별도로 qualification하여 G1 native 결과와 섞지 않는다.

**P 유효성 gate:** 모든 값 finite, joint range 내, 금지된 robot-scene/self contact 없음, 초기 terminal goal false, 사전 정의한 BDDL init 관계 유지, settle 마지막 5 step에서 arm 회전 joint `max |qvel| ≤ 0.05 rad/s`, gripper slide joint `max |qvel| ≤ 0.005 m/s`, movable object 선속도 norm `≤0.01 m/s`·각속도 norm `≤0.05 rad/s`. Forbidden contact는 모든 contact가 아니라 robot-외부 물체/fixture 및 허용되지 않은 self pair이며 table-object support는 허용한다. Geometry-ID 분류표는 runtime manifest에서 실제 model 이름에 맞춰 생성·검토해야 한다. 성공이나 방법별 결과를 보고 유효성 기준을 바꾸지 않는다.

이 tolerance는 pilot 설계값이지 안전성 보증이 아니다. 한 부호에서 20개 development unit 중 18개 미만이 유효하거나 실제 자세 변화가 사실상 없으면 그 P branch를 중단한다. `d_SO3(R_after,R_before) ≥0.02 rad`를 최소 노출 기준으로 둔다. 탈락분을 쉬운 reset으로 교체하지 않고 전체 예정 분모와 valid 분모를 함께 보고한다. 방법 실행 중 생긴 충돌·joint violation은 invalid reset으로 지우지 않고 실패·harm으로 센다.

### 후속으로만 허용할 개입

Camera extrinsic/RGB shift, target object 이동, actuator gain·delay, controller feedback corruption, 외력은 별도 branch다. 각각 observation/render, model/body, action→actuation, controller-state 경로를 바꾸므로 R/P와 합쳐 sensor 오류로 label하지 않는다. 힘·토크 크기·주입 body·접촉 타이밍은 **미고정이며 실행 금지**다. Target 이동은 goal relevance 검사에 쓸 수 있지만 robot report bias와 matched cause pair라고 부르지 않는다.

R의 mid-episode onset은 G2/G3 통과 후 별도 extension으로만 연다. Development query 4/9, holdout 6/13 후보이며 query 직전부터 지속한다. 8-action queue 중간에 추가 관측·조기 재호출을 제공하지 않는다. Onset 전 종료는 `not_exposed`로 기록하고 다른 onset으로 재추첨하지 않는다. P는 이 동적 onset 대조에 포함하지 않는다.

## 4. Paired reset과 goal contrast

Pair ID는 `(physical_initial_group, task_goal, policy_seed, intervention, magnitude/onset)`다. 비교 방법마다 새 process/environment에서 동일 source state와 seed로 reset→restore→wait→필요한 prelude를 재생한다. Controller goal·interpolator·time counter·observable cache·policy queue·estimator/history·named RNG를 새로 초기화한다. 중간 비교가 필요하면 episode 처음부터 같은 command prefix를 replay하며, flat simulator snapshot만 복사하여 branching하지 않는다. Replay 후 prefix 일치가 검증되기 전에는 paired rollout으로 집계하지 않는다.

G0에서 동일조건 replay를 3회 검사한다. Source XML/model의 joint/body 순서·fixture/camera pose·controller configuration은 같아야 한다. 숫자 state/controller goal·time의 최대 절대 차이는 `1e−8`, native RGB pixel과 policy packet은 동일해야 한다는 초기 기준을 둔다. 검사 시점은 **방법별 보정을 넣기 전의 공통 시작점/재생 prefix**이며, 서로 다른 closed-loop 정책의 이후 상태를 같게 요구하지 않는다. Task 8/1에서는 의도한 instruction/evaluator goal 차이를 제외한 물리 상태·RGB/state 일치를 검사한다. 이 기준을 만족하지 못하면 nondeterminism 원인을 기록하고 paired 설계를 HOLD한다. 더 넓은 tolerance가 필요한 경우 outcome 비교 **이전**에 spec version을 바꾼다. 여기서 tolerance는 결정 규칙이며 달성했다는 결과가 아니다.

Task 8/1 contrast는 동일한 물리 scene을 두 evaluator에서 각각 `On bowl plate`/`On bowl stove-region`으로 평가한다. Source의 동일 `:init` 구조만으로 reset 동일성을 인정하지 않는다. Joint mapping·model fixture·rendered scene·양쪽 init predicate가 호환되어야 하고 **양쪽 terminal goal 모두 false**여야 한다. Task 8에서 나온 공통 source state를 1에도 적용할 수 있는지는 G0에서 검사한다. 실패하면 shared-scene goal contrast는 HOLD하며 다른 index를 같다고 간주하지 않는다.

각 goal에서 native prompt와 상대 goal의 prompt를 비교한다. Evaluator는 원래 goal을 유지하여 instruction utility를 측정한다. 이는 의도적인 wrong-instruction negative control이며 정상 정책 benchmark 점수가 아니다. Task ID나 BDDL predicate는 evaluator-private이며 policy에는 native instruction 문자열만 제공한다.

## 5. 분할·seed·선택 방지

Initial-state payload를 확보한 뒤 **outcome을 보기 전에** 이름 기준으로 canonical physical state와 fixture/model 정보를 묶어 group digest를 만든다. Time과 task language를 제외하고 robot/object joint·velocity·fixture/camera/model identity를 포함한다. 같은 물리 상태의 task 8/1·fault·method·seed 변형은 한 group이다. 정확한 중복뿐 아니라 동일 source-state에서 파생된 기록을 같은 group으로 묶는다. 이것만으로 근접 상태의 독립성이나 unseen-task generalization이 성립하지는 않는다.

Group은 `SHA256("d1-l4-v1|" + group_digest)` 순으로 정렬한다. Task 0 pool과 shared 8/1 pool 각각 **calibration 8 group, development 20 group, 나머지 sealed holdout**으로 나눈다. 서로 다른 pool에서 같은 physical group이 발견되면 전역 단일 split 배정을 우선하여 재조정하고 realised ledger에 남긴다. 이 변경은 성능을 보기 전 수행한다. Confirmatory holdout에는 pool별 최소 20 unique group이 필요하다. 수가 부족하면 calibration/dev를 보고 난 뒤 잘라 쓰지 않고 G4를 HOLD한다. 현재 cardinality·indices·digest·payload hash는 모두 미확보다.

- Native qualification: environment seed 0, policy/global seed 7. Method 순서·bootstrap용 master seed 20261022; 해시 기반 named streams를 분리하여 method의 query 수가 fault/order RNG를 바꾸지 않게 한다.
- 첫 pilot은 하나의 policy seed다. 다른 seeds를 독립 initial-state sample로 부풀리지 않는다. Robustness seed 17/27은 G4 설계 때만 추가한다.
- Calibration은 task별 8 clean B0 episode **모두**를 사용한다. 실패 trajectory도 버리지 않는다. Reference는 정규화한 초기 quaternion `q`의 `sum(q qᵀ)` 최대 eigenvector를 회전행렬로 변환하여 만들고 task별·pooled reference를 구별한다. 이는 port의 평균 연산 선택이며 원논문 구현을 확인했다는 뜻이 아니다. 최대 eigenvalue가 중복되어 평균이 비유일하면 reference qualification을 중단한다. G2 reference는 동일한 neutral prelude를 사용한 calibration episode에서 다시 구하며 비용도 따로 센다.
- Holdout 후보: R world-z `±0.15/±0.25 rad`, P prelude `a=±0.15`. 처음부터 magnitude shift와 initial-state shift를 함께 묶은 결과만 내지 않고 같은 magnitude의 unseen initial-state test도 별도로 둔다. Task holdout은 아직 확보하지 않았으므로 C5의 광범위 일반화 claim은 열지 않는다.
- Holdout 접근·분석 전 표본 수, task별 aggregation, primary comparison, 최소 효과/clean non-inferiority margin, CI·다중 비교 처리 계획을 development 비용·discordance에 근거해 별도 freeze한다. 현재 숫자는 null이다. 최소 20 group은 충분한 power 보증이 아니다. 이 후속 freeze는 G4의 실행 gate이며 L4 문서 누락을 숨긴 완료 표시는 아니다.

## 6. 정보·계산 예산과 비교 연산

공통 packet은 native agentview/wrist RGB 2장, native instruction, 8D state다. Evaluator가 가진 full obs/object pose·정답 fault label/onset/B·future outcome·true uncorrupted state는 배포 방법에 전달하지 않는다. Native image flip/resize/crop·state normalization·gripper mapping을 보존한다. Policy proposal은 기존 7D OSC action 8개이며 모든 correction은 **정책 입력 사본의 orientation만** 바꾼다. 새 action primitive나 probe action을 추가하면 별도 연구 조건이다.

| 비용 tier | 허용 정보·호출 | 해당 비교 |
|---|---|---|
| A: 최초 비교 | 8 environment action마다 RGB/state 1회 갱신, 최근 query packet 최대 4개와 그 사이 command/time prefix, policy forward 최대 1회/query | B0, B1a diagnostic, B3-task/causal, B5-M2-style port, D0 privileged |
| B: 추가 query | 관측 횟수는 A와 동일, 동일 packet 변형에 최대 8 forward/query | G-PSMR M1/M3 및 query-matched B0 ensemble control. A와 동일 compute라고 부르지 않음 |
| T: 학습/외부 estimator | 별도 data/update/estimator 호출 및 latency ledger 필요 | B1b/B2 learned history/B4 GAP/B6 augmentation/ReViP·vision-pose baseline. G1 전에는 실행하지 않음 |

B0는 native current-only이며 unused history를 억지로 model에 넣지 않는다. B2의 learned history는 matched architecture/data와 repeated-current control을 갖춰야 하므로 A에 조용히 포함하지 않는다. B3가 prefix를 사용하면 K=1 제거 대조를 둔다. Privileged D0의 정보 이득을 A의 공정한 승리로 세지 않는다.

G1 native: 10 wait+최대 300 policy action, 최대 `ceil(300/8)=38` query. G2: 여기에 14 prelude step 추가. 20 Hz는 simulator control rate이며 실제 20 Hz inference를 달성했다는 뜻이 아니다. Simulator는 query 중 진행하지 않는 synchronous 평가로 고정한다. Forward 수, estimator CPU/GPU time, peak memory, query latency p50/p95, 전체 wall time, calibration trajectory 수, reset/환경 action 수를 보고한다. Hard wall-time cap은 runtime 측정 전 미고정이다. 따라서 이 단계에서 real-time deployment나 compute-equal latency 우월성을 주장하지 않는다.

### 가장 작은 baseline 묶음

- **B0:** qualified frozen OFT.
- **B1a:** normalized proprio를 0으로 고정하는 OOD diagnostic. 성능 하락만으로 state의 유용성/vision-only trained policy 열세를 단정하지 않는다.
- **B3-task/B5-M2-style:** calibration reference `C`, initial report `P0`, fixed gate `d_SO3(P0,C)≥0.07`, gate ON이면 `C P0⁻¹ Pt`. Task별 reference와 pooled reference를 각각 보고한다. Source의 suite-clean 25개와 다른 calibration budget이므로 **paper-style port**이며 G-PSMR 정확 재현이 아니다. Initial calibration·rotation 구현의 원 release는 R1 대기다.
- **B3-causal (설계 대조):** 위 task reference로 초기화한다. 이전 corrected orientation과 지난 queue의 실제 전달 rotational command를 이용해 command-based prediction `Qk`를 만들고, 현재 corrected report와 SO(3) residual을 계산한다. Residual이 calibration clean residual의 threshold를 넘으면 bias estimate를 `Bhat=Pk Qk⁻¹`로 갱신하여 이후 `Bhat⁻¹ Pt`를 전달한다. Threshold 후보는 calibration residual의 q95/q99/max 각각에 0.02 rad를 더한 3개뿐이다. Development clean success, R success 순서의 lexicographic 기준으로 선택하고 tie는 큰 threshold를 고른다. Test threshold tuning과 oracle onset reset은 금지한다.
- **D0:** R branch에서 evaluator의 B를 역적용하는 correctness diagnostic. True-state/oracle-cause/추가 정보를 쓴 variant를 각각 표시한다.

Command prediction은 마지막 corrected orientation에서 실제 queue의 rotation increments를 순서대로 left-compose하는 단순 모델이다. Zero rotation에서는 추가 회전을 넣지 않는다. 실제 controller tracking·zero-command의 이전 goal 유지·body/site 오차를 정확히 예측하는 estimator가 아니다. Calibration에서 residual과 false correction을 먼저 확인한다. B3-causal의 초기 gate가 닫히면 `Bhat=I`로 시작하고 이후 query에서 갱신할 수 있다. 3개 threshold의 development 평가 비용도 모두 기록하며 선택된 한 variant의 비용만 보고하지 않는다. 이 대조의 실패만으로 vision-based residual/kinematics 기반 강한 단순 방법 전체를 배제하지 않는다. 그런 방법의 qualified 구현이 없으면 **G3 미충족**으로 남기고 learned method 우월성 결론을 내리지 않는다.

## 7. 순차 gate·지표·기각

| Gate | 사전에 정한 pilot 기준 | 실패 시 결정 |
|---|---|---|
| G0 | 환경·payload·input/action transform identity, frame/round-trip, 3회 paired replay, 8/1 shared-scene compatibility, native smoke | Resource 부재는 HOLD. Transform/reset 불일치는 구현 수정 뒤 재검사; 기존 결과를 paired evidence로 쓰지 않음 |
| G1a | Development 20 group에서 B0 clean task 0/8 각각 ≥16/20. Goal contrast claim은 task 1도 ≥16/20 | 해당 checkpoint/task 조합 qualification 실패. 작은 새 policy나 task 사후 교체로 통과 처리하지 않음 |
| G1b | 0/8의 +0.10 rad R screening에서 native-clean 성공 수가 corrupt보다 각각 ≥4/20 많고, inverse injection은 native tensor를 복원. 8/1 각각 correct prompt가 swapped prompt보다 ≥4/20 net success 많음 | 충분한 orientation/goal utility를 이 설계에서 확보하지 못한 것. 무용성 증명은 아니며 해당 D1 pilot HOLD/범위 축소 |
| G2 | Neutral-prelude B0 ≥16/20 유지, P validity·exposure gate 통과. R에서 correction의 이득과 P에서 그 연산의 harm을 paired outcomes로 확인 | 두 종류에서 동일 correction이 충분하거나 task utility 차이가 없으면 cause-conditioned 필요성 주장 기각. P 유효성 실패를 policy 실패와 분리 |
| G3 | Qualified B0/B3/B5 및 필요 시 strong vision residual·training 대조가 설명하지 못하는 gap과 관측 가능한 cue가 함께 남음 | 단순 대안으로 충분하면 신규 방법 NO-GO. 비교 구현 미비는 미검증이며 새 방법 승리 아님 |
| G4 | Sealed holdout과 사전 확정한 효과·불확실성·clean 유지 기준 | Pilot 숫자만으로 일반화/논문 가치 확정 금지 |

G1의 4/20(20pp)은 제한된 pilot에서 뚜렷한 현상이 있는지 확인하기 위한 **투자 판단 threshold**다. 유의성 검정·최종 효과 크기가 아니며 작은 효과가 없다는 증거도 아니다. G1 기본 비용 상한은 native clean 60 episode(0/8/1), R screening 40(0/8), goal swap 40(8/1)으로 **140 episode**, 여기에 calibration 24개·smoke/replay는 별도 기록한다. Gate 실패 시 뒤쪽 실행을 생략하고 task 7을 자동 대체 투입하지 않는다. 실제 실행 수는 현재 0이다.

G2는 development 20 group의 task 0/8에서 clean 1, R 4, P 2 조건이다. Full grid를 시행하면 method당 최대 280 episode이며 qualification 실패 시 즉시 중단한다. G0/G1 전에는 이 sweep을 예약·실행하지 않는다. G2 탐색 결과의 크기에 통계적 유의성을 붙여 최종 채택하지 않는다.

Primary는 native LIBERO goal success와 baseline 대비 paired success difference다. 같은 task/group/condition에서 `recovered=(baseline fail, method success)`, `harmful=(baseline success, method fail)`을 센다. Harmful 비율은 전체 유효 pair와 baseline-success pair를 각각 분모로 보고하고 후자가 0이면 N/A다. 방법에 따라 물리 궤적이 갈라지는 것은 closed-loop outcome의 일부이며 이를 동일 trajectory의 반사실이라고 부르지 않는다.

Invalid reset, simulator exception, method exception, timeout, not-exposed를 별도 ledger로 남긴다. Method 실행 후 실패를 pair 제외로 처리하지 않는다. Infrastructure 오류는 쌍 전체의 incomplete로 표시하고 사전 재시도 규칙을 run manifest에 고정한 뒤 같은 ID로만 재시도한다. Reported 성공률에 incomplete를 숨기지 않는다. Native success predicate 외에 persistence를 추가하고 싶으면 별도 metric으로 둔다. 최종 성공까지 시간과 correction-trigger 지연을 구분하며 ground-truth onset 기준 latency는 evaluator만 계산한다.

G2의 방향성 비교는 **특정 correction 선택의 utility**를 말한다. 최적 행동이 다르다거나 원인 분류가 반드시 필요하다는 결론은 아니다. 관측 cue의 식별 가능성과 그 cue를 활용한 행동 이득은 각각 별도 검증한다. Frame별 sample 수를 표본 수로 세지 않고 physical group을 의존성 단위로 삼으며 task 0/8 결과를 우선 따로 보고한다.

## 8. 실행 전 남은 artifact와 결론

| 이미 생성·확정한 것 | 아직 생성·검증하지 않은 것 |
|---|---|
| Source task/policy revision, intervention 설계·후보 값, reset/split/budget/gate 규칙, JSON spec | 호환 Docker image digest·dependency lock, weight/action head/proprio projector/normalizer hash, initial-state payload·실제 split ledger |
| Shared-reset 검증 절차와 source 누락 위험 기록 | Render/controller/state 실제 일치, task competence·orientation/goal utility, P 물리 validity·cue visibility |
| 최소 대조 연산과 원논문 port 경계 | Runner·baseline 구현 및 qualification, vision residual 자산, 실험 log·통계 결과, final holdout analysis freeze |

**D1-E1은 resource preflight 후 WAITING_RESOURCE**다. 현재 컴퓨터 Docker에서 qualified native 실행 경로가 새로 확보되면 G0 나머지→G1을 수행한다. 동일 자원 조건의 검사를 반복하지 않으며 정책 효과는 HOLD다. G-PSMR/GAP/ReViP 미확보 source는 D1-R1, 실제 외부 반박은 D1-F1에 남는다. 문헌·계약 작업 L1–L4는 완료했지만 **새 VLA/RL 방법으로 발전시킬 가치가 확인된 상태는 아니다**. RL의 필요성이나 다른 로봇 일반화는 아직 주장 범위에 없다.
