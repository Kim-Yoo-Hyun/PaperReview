# D2 주장–증거 계약 — 비실험 설계

- 작성: 2026-10-22 KST
- 연결: [현재 판단](./README.md), [문헌과 확인 경계](./CLOSEST_WORK.md)
- 아래 수식과 비교 규칙은 연구자 분석이다. 새로운 정리·논문 결과·실행된 실험으로 제시하지 않는다. `executable=false`; runtime/checkpoint/task/split manifest는 생성하지 않았다.

## 1. 기하학과 정책 능력을 분리하는 연구자 분석

로봇 configuration을 \(q\), robot geometry를 \(R(q)\), object-local 강체 형상을 \(O\), end-effector의 world transform을 \(T_{WE}(q)\), 파지에 고정된 object-to-end-effector transform을 \(T_{EO}(g)\)라 두면 보호할 형상은

\[
 B(q,g)=R(q)\cup T_{WE}(q)T_{EO}(g)O.
\]

장애물 집합 \(\mathcal M\)에 대해 \(B(q_t,g)\cap\mathcal M=\varnothing\)을 경로 전체에서 만족시키는 것은 attached-object collision planning의 형태다. 파지 후 slip·재파지가 없고 geometry/transform이 맞다는 가정이 필요하다. 접촉해야 하는 target/support를 모두 장애물로 처리하면 task 자체를 금지하므로 contact role도 고정해야 한다.

평면의 긴 직사각형을 통로 방향과 각도 \(\theta\)로 운반하면 횡방향 폭은 \(L|\sin\theta|+w|\cos\theta|\)다. 통로 폭을 \(c\), 양쪽 여유를 \(m\)이라 할 때 \(L|\sin\theta|+w|\cos\theta|\le c-2m\)은 그 자세로 통과할 때의 단순 필요 조건이다. 로봇 몸체·코너 회전·접근 경로·IK까지 보장하지 않는다. 파지의 회전 변화는 \(\theta\), 병진 변화는 손에 대한 object offset을 바꾼다. **이 식은 VLA 실험이나 새 contribution이 아니다.** 기존 기하학 대안이 강함을 확인하는 예시다.

다음 두 quantity는 구분한다.

\[
F(g,s)=\mathbf1\{\exists\text{ admissible grasp-to-goal trajectory under }g,s\},
\qquad
U_\pi(g,h)=\Pr(\text{safe final placement}\mid g,h,\pi).
\]

\(F\)는 모델 가정하의 존재성이고 \(U_\pi\)는 관측 history \(h\), 특정 정책과 실행 조건의 성공 확률이다. 계산 예산이 \(b\)인 planner의 실패 \(\hat F_b=0\)을 \(F=0\)으로 바꾸지 않는다. 충돌 없는 witness 경로를 찾은 경우에도 실제 실행은 별도다. 반대로 정책 실패만으로 경로가 없다고 라벨링하지 않는다.

서로 다른 파지에 동일한 hand path를 강제로 사용하면 selection의 효과와 execution 제한을 혼동한다. 비교할 grasp 후보 집합과 downstream executor를 명시하고, planner의 선택 이득과 executor 교체 이득을 분리한다.

## 2. 아직 입증되지 않은 주장과 필요한 비교

| 주장 후보 | 필요한 증거 | 배제할 설명 | 철회/축소 조건 |
|---|---|---|---|
| Native VLA의 transport 실패가 attached geometry와 관련된다 | 파지·형상 조건을 바꾼 paired outcome, clean competence, 실제 object/contact event | 기본 집기 실패, GT geometry 제공, 잘못된 frame | 물체 모델을 같은 정보로 추가하면 설명됨 → geometry baseline 결과로 축소 |
| 이후 경로를 고려한 선택이 local shield보다 필요하다 | 안전한 시작 뒤 transport/place가 갈리는 후보와 global baseline | local shield에만 regrasp/회전 금지 | Global planner가 충분 → 새 planning claim 중단 |
| 학습한 선택이 유효하다 | 동일 후보·geometry·예산에서 단순 ranker 및 planner와 비교 | 후보/label/compute 증가, training-scene 누출 | 선택 이득이 없거나 정보 차이로 설명됨 → method NO-GO |
| RL이 추가로 필요하다 | 동일 데이터의 BC/return-weighted imitation, supervised outcome ranking, 기존 residual/foresight와 비교 | successful-data filtering, reward shaping, 강한 executor 교체 | RL 이후 잔여 이득이 없으면 RL claim 철회 |
| 다른 로봇에 재사용된다 | 두 native executor의 competence·관측·action/head/cost를 고정한 평가 | 동일 플랫폼 두 대, oracle geometry, target robot 추가학습량 | 서로 다른 embodiment 계약이 없으면 transfer 주장 제외 |

Fixed grasp를 한번 고르는 문제는 contextual ranking/bandit으로도 표현된다. 상호작용 중 관측·재파지·route 선택의 순차적 효과를 확보하기 전에는 RL을 기본 방법으로 정하지 않는다. Foresight objective 자체도 기존 직접 선행이 있다.

## 3. 비교 집합과 공정성

최소 비교 역할은 다음과 같다. 모든 이름은 재구현 완료를 의미하지 않는다.

| 역할 | 비교 목적 |
|---|---|
| Native VLA | Clean competence와 원래 실패를 확인 |
| VLA + local attached-geometry filter | Geometry 누락의 설명력. WBAG/CarryOn 역할 |
| 동일 geometry의 global planner/TAMP + VLA contact skill | Whole-route·placement feasibility의 설명력. ReKep/PDDLStream 계열 |
| 단순 analytic ranker와 supervised feasibility/outcome ranker | 학습 필요성·CE 계열 대안. Human pose prior와 planner cost ranking 포함 |
| GTP-FA 계열 grasp/execution 개선 | Failure attribution 및 후보 점수 조정의 설명력 |
| Foresight/residual 계열·BC/return weighting | RL을 제안할 때만 추가할 직접 대조 |
| Oracle geometry/확장 budget | 상한·원인 분석. 주 방법과 동등 정보 비교로 보고하지 않음 |

관측은 timestamp가 있는 RGB-D, proprioception, 언어 goal, calibration과 과거 허용 history로 한정하는 초안이다. 실제 sensor/control interface가 없는 checkpoint에 이 packet을 임의로 붙이지 않는다. Object mask·shape·grasp transform 추정은 모든 적용 가능한 비교에 공유한다. GT mesh/pose/미래 trajectory와 simulator identity는 privileged이며 별도 조건에서만 제공한다. 정책별 입력 차이가 불가피하면 두 비교군으로 분리하고 동일 정보의 우열을 주장하지 않는다.

파지 후보 생성기·후보 개수·접근/회전/재파지/중단 옵션, lift 전 결정 시점, 이후 feedback 주기를 공유한다. Selector가 실제 native policy의 행동을 어떻게 제한/조건화하는지 증명할 source가 없다면 해당 baseline은 미자격이다. Action head가 없는 mobile base 제어를 ‘VLA 출력’이라고 부르지 않는다.

비용은 online wall time, collision/IK/planner query 수, VLA 호출 수, 실제 env step, offline label 생성용 rollout 및 tuning 비용을 함께 기록한다. 한쪽만 대규모 planner label을 사용하면서 online 시간만 비교하지 않는다. 정확한 budget 값은 hardware/task qualification 뒤 결과를 보기 전에 고정한다.

## 4. Task와 평가 단위

| 문헌에서 확인한 후보 family | 사용할 수 있는 점 | 현재 qualification의 한계 |
|---|---|---|
| ReKep의 좁은 shelf/holder 배치 | 강체 방향·object clearance가 행동을 바꿀 수 있음 | 공개 demo의 privileged geometry, 완전한 VLA/mobile task 계약 없음 |
| Cooperative Grasping의 통로 운반 | grasp–route 결합이 명시됨 | 두 로봇·2D map/footprint 조건, native VLA 아님 |
| SafeLIBERO의 object collision | geometry/filter 비교의 기준 | 기본 tabletop. 이동 base·운반 경로 선택의 검증으로 대체 불가 |
| GTP-FA의 ManiSkill3 manipulation | 파지/후속 실행 분해와 VLA 비교 | 논문 recipe와 공개 실행 artifact 연결 미확보. 새 mobile benchmark로 간주하지 않음 |

최초 후보는 **길쭉한 강체의 파지 → 제한된 개구부를 통한 배치**로 좁힐 수 있다. 단, fixed-base 결과만 확보하면 manipulation 진단으로 한정한다. Mobile-navigation 또는 cross-embodiment 효과로 확대하지 않는다. 현재 실제 task ID·asset·checkpoint를 선정한 상태는 아니다.

주 outcome은 독립 evaluator가 판정하는 **최종 배치 성공 AND 금지 접촉 없음**이다. 로봇/물체 충돌, drop, route blockage, regrasp 수, clearance, 시간/경로 길이, 최종 자세 오차를 분해한다. Solver cost나 학습 classifier의 feasible label을 자기 방법의 성공 evaluator로 재사용하지 않는다. Displacement safety proxy는 정적 벽 접촉·밀리지 않는 물체의 충돌을 놓칠 수 있으므로 범위를 명시한다.

Object shape × grasp family × passage/goal의 조합을 outcome 확인 전에 나누고 동일 shape의 mesh 변형·동일 episode 인접 frame을 독립 test로 세지 않는다. Scene/seed를 묶어 paired 차이와 불확실성을 보고한다. 실패할 모든 후보도 denominator에 남기고 `no solution found / infeasible proven / invalid execution`을 구별한다. 최소 효과 크기·sample size·seed 수는 아직 정하지 않았으며 효과 수치를 만들지 않았다.

## 5. 재개 gate

- G0: 차별적 예측, 관측 cue, 허용 행동, task/source identity를 확보한다. **현재 미충족.**
- G1: G0 이후에만 현재 컴퓨터 Docker에서 runtime·reset·clean competence를 확인한다. **미실행.**
- G2: matched geometry/candidates/budget의 단순 baseline 이후 현상을 확인한다. **미실행.**
- G3: G2에서 필요성이 남을 때만 학습·RL·다른 embodiment 확장을 검토한다. **미착수.**

문서 완료는 G0 통과가 아니다. 지금의 NO-GO는 새로운 방법 투자에 대한 판단이며 D2 가설의 실험적 반증은 아니다.
