# E1 해석적 검사와 주장–증거 계약

- 날짜: 2026-10-22. 이 문서의 도출은 **연구자 분석**이다. 수치 실험·정책 실행 결과가 아니다.
- 현재 결론: 물리 효과의 의미는 중요하지만 그것만으로 forgetting estimator나 새 replay 방법이 정당화되지는 않는다.

## A. 선형 효과 변환은 가중 잔차다

고정된 상태·시간 간격에서 유효 action vector가 a, 정책 복원값이 â라고 하자. 효과 표현이 `e = G a + c`, 양의 준정부호 metric이 W라면

`d_effect² = (G â − G a)ᵀ W (G â − G a) = (â − a)ᵀ GᵀWG (â − a)`.

따라서 이 경우 effect score는 기존 action residual의 weighted quadratic metric이다. G가 고정이면 새 selector의 알고리즘적 새로움은 여기서 나오지 않는다. State-dependent G이면 metric도 state-dependent가 되지만, 그것만으로 새 contribution이 성립하지는 않는다. Nonlinear map은 국소 Jacobian 근사만 가능하고 contact·큰 회전에 전역 선형식을 적용할 수 없다.

Invertible coordinate change `a′=T a`에서는 predictor와 mask/normalizer, metric `W′=T⁻ᵀWT⁻¹`, noise covariance를 함께 옮기면 같은 물리 비교를 보존할 수 있다. 두 좌표계에 각각 isotropic noise를 새로 넣으면 일반적인 T에 대해 같은 noising process가 아니다. 따라서 ranking 차이가 나도 물리 충돌 때문인지 noise/normalization 변경 때문인지 분리해야 한다. 이는 분석상 control이며 학습된 VLA의 equivariance를 가정하지 않는다.

G가 non-injective면 `Gv=0`인 차이가 사라진다. 같은 EE motion이어도 nullspace의 joint limit·self collision·force 차이가 안전/성공에 중요할 수 있다. Gripper/object/contact 정보를 버린 거리로 모든 행동의 동등성을 주장하지 않는다.

## B. 같은 행동 잔차로 망각 방향을 알 수 없다

SGD의 작은 new-data update `θ′=θ−ηg_new`에 대해

`L_old(θ′) − L_old(θ) = −η g_oldᵀg_new + O(η²)`.

Adam·momentum에는 optimizer state와 update direction이 추가된다. 즉 output error뿐 아니라 parameter Jacobian·optimizer가 필요하다.

해석적 반례: scalar model `fθ(x)=θx`, squared loss `½(f−y)²`, 초기 θ=0, old sample `(x,y)=(1,1)`을 둔다. New sample은 `(1,1)` 또는 `(-1,1)`이다. 두 경우의 new prediction=0, target=1, signed residual=−1로 동일하다. Identity effect map에서도 score는 같다. 그러나 new SGD 후 θ는 각각 `+η`, `−η`가 된다.

- 첫 경우 old loss는 `½(1−η)²`; `0<η<2`에서 감소한다.
- 둘째는 `½(1+η)²`; η>0에서 증가한다.

이는 **잔차/효과 거리만을 충분한 망각 통계로 보는 보편 주장**의 반례다. 실제 pretrained VLA의 forgetting을 입증하거나, latent overlap까지 사용하는 Memory Anchors 전체를 반박하는 결과는 아니다. 조건부 통계 예측 H1은 여전히 열린 질문이다.

이 때문에 [MIR의 가상 업데이트 기준](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html)을 강한 대안으로 둔다. MIR도 surrogate loss를 측정하므로 closed-loop 성공의 oracle은 아니다. Memory Anchors가 이미 MIR를 비교했다는 사실은 [직접 선행](./CLOSEST_WORK.md)에 반영했다.

## C. 기록된 다음 상태는 실행하지 않은 행동의 결과가 아니다

Dataset의 `(s,a,s_next)`는 a를 실행한 전이다. 정책이 다른 â를 제시하면 `effect(s,â)`는 관측되지 않는다. 기록된 `s_next`를 â의 결과로 대입하거나, FK로 목표 joint pose를 EE pose로 바꾼 것을 실제 도달 결과라고 간주할 수 없다.

SPACE의 Δpose→command adapter를 역행렬로 뒤집는 것도 검증된 forward dynamics model을 자동 제공하지 않는다. Rank, conditioning, operating region, controller·contact dependence를 확인해야 한다. [원 adapter의 정의](https://arxiv.org/html/2606.24049v1#S4.S2).

H1을 실행하려면 (i) 두 정책 모두 native하게 **achieved-effect label을 예측하도록 정의된 모델**이거나, (ii) 각 command의 결과를 예측하는 calibrated forward map이 필요하다. 전자는 action target·학습 방법을 바꾸므로 selector-only 비교가 아니고, 후자는 추가 data·오차·비용을 모두 기록한다. GT simulator나 미래 상태를 쓰면 privileged diagnostic으로 표시한다. 현재 어느 경로도 qualified하지 않았다.

## D. 반증 가능한 비교

| Case | 고정 / 변화 | 갈리는 예측 | 현재 |
|---|---|---|---|
| D0 표현-only | 같은 물리 trajectory·robot, 알려진 frame/unit 표현만 변경 | 일관된 noise·metric 변환 후에도 score가 다른지. 차이가 전처리로 사라지면 구현 문제 | 분석 완료, native 미실행 |
| D1 실제 robot | 같은 goal·가능한 effect와 scene strata, robot만 변경 | H1: 정상 정렬 이후 효과 score에 retention 추가 예측력이 있음. H0/H3: aligned 잔차·MIR/분리 head로 충분 | 후보 packet 미확보 |
| D2 실제 task conflict | 같은 robot·interface, 목표 행동 변경 | 기존 AnchorER가 다루는 현상을 재확인하는 positive control | task/checkpoint 미선정 |
| D3 loss–behavior 분리 | 동일 adaptation stream과 old episode evaluation | score/old loss는 변해도 성공이 유지되면 능력 망각으로 부르지 않음 | 미실행 |
| D4 selector 개입 | H1이 지지된 조건, 같은 replay/학습 예산 | 효과-aware 선택이 강한 기준 이후 old retention을 개선하고 new competence를 유지 | H1 이전에는 구현하지 않음 |

## E. 정보·시점·예산 계약

**최초 대상은 stage 단위 supervised adaptation이다.** 관측은 RGB·instruction·native proprio·robot ID이며 필요한 frame/time/mask metadata를 모든 baseline에 동일 제공한다. Action은 각 로봇의 검증된 command interface다. 새로운 teacher/reward/RL은 없다. 입력을 바꾸지 않는 진단부터 시작한다.

Boundary 진단은 old policy를 고정하고 같은 new-data probe와 old candidate pool을 쓴다. Aligned action residual, 유효한 effect residual, virtual-update old-loss change를 비교한다. 마지막 항목은 **MIR-style boundary diagnostic**이며 매 update 검색하는 원 MIR 전체와 동일하다고 부르지 않는다. Sample-level effect score는 task–robot-level 성공 감소에 연결할 때 task를 넘어선 held-out 평가를 사용한다.

Replay 실험으로 진행하면 원 AnchorER, uniform, robot/task-balanced, asymmetric replay, MIR의 timing을 보존한 대조, frozen encoder/robot별 head·adapter를 포함한다. 구조를 바꾼 방법은 전체 저장 parameter와 routing 비용도 센다. 정확한 flow estimator가 없으면 구현을 추정해서 원 논문 재현으로 표시하지 않는다.

| 예산/정보 | 계약 |
|---|---|
| 과거 candidate 접근 | 첫 진단은 **과거 archive 접근 허용** 조건. 모든 selector에 같은 과거 data를 허용하고 archive bytes·재처리 비용을 보고한다. 이를 bounded total-memory 주장으로 포장하지 않는다 |
| Resident-only 설정 | 후속 별도 조건. 모든 방법의 candidate pool을 resident buffer로 제한. Archive를 요구하는 방법의 변형은 adaptation이라고 표시하고 원 방법과 구분 |
| Replay 저장량 | Index JSON 수가 아니라 재생에 필요한 RGB/state/action payload bytes, cache/embedding/model 보관 비용 |
| 학습 노출 | 같은 new demonstration와 고정 총 optimizer step, new/replay step schedule·batch 크기. Selector 간에는 같은 old 노출 횟수, 선택 identity만 변화 |
| Replay ratio ablation | Ratio가 달라지면 총 step·new 노출·old 노출을 모두 동시에 동일하게 할 수 없다. Equal-total-compute와 equal-new-exposure 비교를 별도 보고 |
| 선택 비용 | Embedding 전체 재계산, denoise, 가상 update/backward, forward map의 calibration·추론을 포함. Equal-update 결과와 equal-wall-time 결과를 구분 |
| 데이터/평가 정보 | Train/validation만 selection/tuning. 미래 task 통계·test success를 보지 않음. Robot ID·실제 허용 센서는 모든 방법 동일 |
| Timing | Data boundary 선정과 update-wise 선정의 차이·갱신 빈도를 명시. 미래 policy loss/성공으로 과거 buffer를 고르지 않음 |
| 전체 joint training | 전체 data와 별도 학습 예산을 쓰는 reference. 실용 replay와 동일 자원 baseline으로 표시하지 않음 |

## F. 성공·실패 해석

Primary는 로봇별 old-task 성공의 before/after 변화와 new-task 성공을 함께 보고한다. Old/new 평균만으로 trade-off를 숨기지 않는다. Episode/scene/task–robot split과 학습 순서, 반복 seed를 사전에 정하고 main test에서 최악 pair를 골라 주장을 만들지 않는다. Progress score는 binary success와 분리한다.

H1: held-out retention 예측에서 aligned residual·task/robot difficulty·MIR 이후 추가 설명력이 없으면 effect 설명을 채택하지 않는다. Native paired 평가와 uncertainty가 필요하다. 상관만으로 원인이라고 부르지 않는다.

H2: 개선이 추가 update·archive 접근·forward-model 정보·new-task 희생으로 설명되거나 balanced/adapter 기준과 비용상 동등하면 새 selector를 채택하지 않는다. H1만 지지되면 반복 가능한 진단과 실무 선택에 도움이 될 때만 연구 범위를 유지한다.

표본 수·효과 크기·noninferiority margin은 qualified task와 variance를 확보한 뒤 main test 전에 고정한다. 현재 임의 수치를 만들어 executable protocol이 완성되었다고 표시하지 않는다. 모든 성능칸은 미측정이며 [재개 명세](./EVIDENCE_REQUIREMENTS.json)의 gate가 먼저다.
