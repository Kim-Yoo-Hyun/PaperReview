# C6 재개 조건과 재사용할 평가 설계

- 현재 상태: **독립 신규 방법 채택 NO-GO; 구현/학습 미착수**.
- 아래는 새 증거가 생겼을 때 사용할 protocol이다. 실행 가능한 project manifest가 만들어졌다는 의미가 아니다.

## 남겨 둘 검증 질문

> 동일 VLA의 RL update 강도가 증가할 때, 학습 reward와 연결된 evaluator의 checkpoint 오차가 독립 evaluator보다 체계적으로 커지는가? Task mixture·support shift·측정 잡음을 맞춘 뒤에도 차이가 남고, 기존 calibration·순차 검정으로 충분히 설명되지 않는가?

이 질문도 신규성이 확인된 기여가 아니다. Reward exploitation과 일반적인 OOD/선택 잡음을 분리해야 한다. Frozen checkpoint 사이의 상관관계는 진단 근거일 뿐, 학습 과정의 인과 증거가 아니다. 인과 claim에는 같은 native initialization·budget 아래 학습 reward/evaluator 결합을 바꾸는 controlled contrast가 추가로 필요하다.

## 첫 번째 작업: 실제 자료의 한 run을 완전히 연결

완전한 한 run을 확보하기 전에는 새 selector를 구현하지 않는다. 최초 필요한 항목은 다음과 같다.

- Robot/environment ID와 code commit, native checkpoint hash·parent·RL update step·training seed.
- VLA-visible observation, action representation, chunk length, control rate, evaluation horizon/termination.
- Training reward와 evaluator의 이름/version/hash, 학습 데이터·검증 데이터 identity/overlap.
- Trial별 checkpoint, task/scene/start ID, simulator seed 또는 real session/block, independent outcome, evaluator score, invalid/timeout/reset 처리.
- Fixed target task weights, 시행당 rollout/reset 시간, human intervention 시간. 서로 다른 비용 단위를 합쳐 쓰지 않는다.
- Selector-visible set, tuning/calibration set, 잠근 reference set의 disjoint IDs와 접근 시점.

Artifact 상태: **환경/실제 checkpoint 목록/구체적 seed·split/run manifest/JSON schema·validator/native runtime report 모두 미생성**. 이번에 생성한 것은 source/data 검사 script와 provenance report다.

## 평가 contract

Checkpoint 집합은 selection 시작 전에 고정한다. `J(pi)`는 고정한 task distribution과 horizon에서의 독립 outcome 기댓값이다. 평가기는 후보 hash, 사전 허용한 offline score·과거 trial outcome·잔여 budget만 본다. 다음 선택은 trial 또는 사전에 고정한 block이 끝난 뒤에만 한다. Test outcome으로 정책을 다시 학습하거나 후보를 추가하지 않는다.

Primary metric은 budget별 **selection regret** `max_pi J(pi) - J(selected)`다. Reference의 경험적 최대값은 true oracle가 아니므로, 유한 표본 불확실성과 여러 candidate를 비교한 효과를 함께 보고한다. 미결정을 허용하면 기존 정책을 유지했을 때의 regret와 미결정 비율을 포함한다. 승인한 사례만 골라 평균내지 않는다.

Secondary는 **기준 정책보다 실제로 나쁜 checkpoint를 승인한 비율**, trial/robot time, human time, 미결정률이다. 승인 비율의 분모는 전체 독립 selection run으로 고정한다. 독립 reference에서도 좋고 나쁨을 구분할 수 없는 경우 unresolved로 별도 계수한다. “실패를 검출하지 못함”을 비열등성 증명으로 바꾸지 않는다.

## 빠질 수 없는 비교

| 비교 | 역할 |
|---|---|
| 마지막 checkpoint, offline score 최대값 | Zero-online-budget anchor |
| Uniform task-stratified evaluation | 단순하고 강한 allocation baseline |
| Standard best-arm racing, A-OPS | 기성 fixed-budget selection과 OPE prior 활용 |
| STEP / N-SCORE + 다중 비교 보정 | Binary/bounded outcome에서 개선·하락 판단의 기성 기준 |
| S02 task-cost-aware selection | Task 전환 비용이 실제 주요 비용일 때 |
| Sim2Val/SureSim 계열 | Paired surrogate/real data와 해당 가정이 충족될 때 |
| RACE 또는 fixed learned evaluator + 동일 검정 | Ranking signal과 통계적 승인 절차의 기여를 분리 |

동일 candidate set·공개 정보·target distribution·online budget·reference set을 사용한다. Calibration label 비용도 포함한다. 단순 estimator의 budget에 더 많은 실측을 주거나 learned method에 reference를 유출하지 않는다.

초기 baseline은 각 정책에 독립적으로 뽑은 target-distribution trial을 사용한다. 동일 start를 공유하는 paired evaluation은 별도 진단으로 가능하지만, **within-pair dependence를 허용하는 검정**을 사용해야 한다. N-SCORE/STEP의 가정을 확인하지 않고 common-random-number 결과에 그대로 적용하지 않는다. Adaptive task selection도 원하는 target mean을 보존하는 추정·검정이 필요하다. Anytime-validity는 arbitrary distribution shift나 무제한 policy 재설계의 면허가 아니다.

## Ablation과 기각

1. Shared reward/evaluator와 independently trained evaluator를 나누되 training-data overlap을 기록한다.
2. 같은 budget에서 offline signal 없음 / signal만 / 실측 보정 / 기성 순차 검정을 비교한다.
3. Fixed task weights와 empirical mixture를 구분하고, OOD distance·policy divergence·task 난도를 통제한다.
4. 반증 가능한 해석을 먼저 고정한다. 기존 method로 오류가 해소되거나 target 평가의 잡음 이내이면 새 방법을 만들지 않는다.
5. 하나의 evaluator·task에만 성립하면 범용 VLA 결론을 제거한다. 한 robot에서 증거를 얻기 전에 다양한 embodiment/navigation으로 확장하지 않는다.

실용적으로 의미 있는 gap, 최종 candidate 수·trial budget·task/seed split은 실제 데이터 구조를 확인한 뒤 **outcome을 분석하기 전에** 고정해야 한다. 지금 임의 수치를 넣고 preregistration이 끝났다고 표시하지 않는다.

## 현재 다음 행동의 우선순위

C6의 새 학습은 다음 TODO가 아니다. 후속 정책 연구에서 위 baseline을 평가 도구로 사용한다. C6 자체는 native RL provenance와 독립 outcome이 갖춰진 자료, 그리고 기존 비교법을 넘는 실패 조건이 새로 생길 때만 재개한다. C5의 reset ledger나 C4의 reward-label acquisition을 동시에 학습시키며 scope를 넓히지 않는다.
