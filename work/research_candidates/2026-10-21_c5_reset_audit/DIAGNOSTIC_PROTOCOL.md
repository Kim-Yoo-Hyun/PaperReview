# C5 재검토 계약

- Date: 2026-10-21 KST
- 상태: **NOT IMPLEMENTATION READY**. 아래는 설계이며 실행 결과가 아니다.
- 문헌·code·sample data 감사는 완료. Native environment/checkpoint/physical reset 경로와 사건 로그는 미확정.

## 1. 서로 다른 세 가지 estimand

1. **Policy competence:** 고정 target distribution `p_target(s0, task)`에서 독립 평가한 `J_target(pi)`.
2. **Operational performance:** 실제 자율 운영에서 시간당 완료한 task, reset 성공·실패·rescue·대기 비용. 실패 reset 뒤 task를 시작하지 못하면 운영상 미완료지만, 그 상태에서 policy를 실행했을 때 실패했을 것이라고 단정하지 않는다.
3. **Learning effect:** 같은 robot-time/human-time/compute 예산에서 scheduler `m`으로 학습한 정책의 `J_target(pi_B^m) - J_target(pi_0)`.

현재 controller가 만들어낸 시작 분포 `q`에서의 성능 `J_q`도 별도로 보고한다. `J_q` 증가로 1이나 3의 개선을 대신하지 않는다. 이 구분은 EARL의 기존 deployed/continuing evaluation을 따르며 새 이론으로 주장하지 않는다. [EARL §4](https://arxiv.org/pdf/2112.09605)

## 2. 가설과 반례부터 고정

**H1, 진단 가설:** 고정 reset policy·retry cap에서 forward VLA checkpoint의 변화가 종료 상태를 바꾸고, 그 결과 목표 scene별 시작 도달 확률과 수집 비용이 달라진다.

**H2, 후속 학습 가설:** 그 변화가 단순한 curriculum 효과를 넘어, 동일 비용의 fixed-target policy improvement를 제한한다. H1만 관측하면 H2를 지지한 것이 아니다.

**H3, 개입 가설:** Task/scene quota 및 bounded retry보다 추가적인 rescue scheduling이 의미 있게 도움이 된다. H3는 H1–H2와 단순 baseline 효과를 본 뒤 심사하며 현재 새 learned method를 정의하지 않는다.

편향의 방향도 가정하지 않는다. 예를 들어 요청한 group이 `p(g)`에서 나오고 성공 reset이 group을 바꾸지 않는 단순 모형에서, acceptance `a(g)`와 frozen policy 성공률 `v(g)`를 두면:

```text
q(g) = p(g) a(g) / E_p[a]
J_q - J_p = Cov_p(a, v) / E_p[a],  E_p[a] > 0
```

이는 연구자 유도의 조건부 항등식이다. Acceptance가 쉬운 group과 양의 상관일 때만 과대평가 방향이며, 상관이 없거나 음수면 달라진다. Physical reset이 다른 group으로 이동시키면 전이 kernel을 써야 하고 이 식을 그대로 적용할 수 없다. 이 계산을 실험 증거나 신규 이론으로 제시하지 않는다.

## 3. 첫 단계: 학습 전에 사건 로그의 완전성 확인

기존 native policy와 reset controller를 모두 고정한다. 요청한 target scene은 정책 outcome을 보기 전에 정하고, 실행 여부와 관계없이 요청을 기록한다. 다음은 **생성해야 할 schema 요구사항**이며 실제 수집 schema/manifest가 생성·검증됐다는 뜻이 아니다.

| 단위 | 반드시 필요한 필드 |
|---|---|
| Run identity | run ID, robot/scene/task ID, repository commit, environment/asset version, VLA checkpoint hash, reset-controller hash, detector version |
| Requested reset | request ID, previous task episode ID, 사전 지정 target group·허용 오차, 목표 선택 확률/규칙, request time |
| Reset attempt | request ID, attempt index, primitive/goal, action 전 관측 참조, 도착 관측 참조, validity 판정과 provenance, 실제 action 수·소요 초 |
| 모든 종료 | accepted / failed / skipped / aborted / budget_exhausted, 원인, human rescue 여부·초, 요청 취소·누락 사유 |
| Task rollout | 연결된 accepted request ID, 실제 시작 관측, instruction, 정책/reward version, 독립 outcome, timeout/robot fault 구분 |
| Learning | rollout을 사용한 update index, optimizer/checkpoint lineage, replay admission/weight와 수집 시각 |
| Evaluation | p_target manifest/split ID, 사전 scene group, held-out outcome, 평가자/판정 규칙, training 사용 금지 표시 |

첫 acceptance 조건은 각 request가 terminal status 하나로 닫히고, 모든 accepted task가 reset request와 연결되는 것이다. Retry·rescue·abort가 로그에서 빠지면 다음 단계로 진행하지 않는다. `time`만 있거나 human intervention boolean만 있는 export는 충분하지 않다.

예상치 못한 irreversible state는 안전 절차에 따라 종료하고 사건을 기록한다. Request 취소를 다른 scene 성공으로 대체하여 denominator에서 숨기지 않는다. Episode video 첫 frame이 action 전 관측인지도 확인한다.

## 4. 학습 없는 진단과 학습 실험을 순서대로 분리

### Gate A — 가장 작은 현상 검사

- 같은 native VLA의 알려진 checkpoint를 고정해서 비교한다. 새로운 policy를 먼저 학습하지 않는다.
- 비교 가능한 task/scene block에서 checkpoint 순서를 무작위화한다. 실제 물리 이력이 서로 다르므로 단순히 같은 random seed라고 paired physical trial로 부르지 않는다.
- 독립 target-start 평가와 연속 자동 reset 운영을 나눠 수집한다. Evaluation의 수동 배치 시간도 기록하되 training rescue 예산과 혼합하지 않는다.
- Target group별 requested/accepted/failed/missing 비율, reset 시도 수·소요 초, 인간 개입 초와 `J_target`을 계산한다. 요청이 한 번도 없었던 group을 achieved-only 로그로 보간하지 않는다.
- Frozen policy에서도 생기는 점수 차이는 평가 selection의 진단이다. RL 학습 coverage 손실을 검증하려면 Gate B가 필요하다.

### Gate B — 단순 scheduling으로 충분한지

Native VLA + 동일 RL learner를 유지하고 다음 기존 수집 전략을 비교한다. 새 reset controller와 새 reward를 동시에 학습시키지 않는다.

| Baseline | 역할 |
|---|---|
| Native reset/scheduling | 현재 시스템 기준 |
| Task-balanced quota | Task 간 빈도 편향만 교정 |
| Scene-group quota | Task 내부 초기 조건의 부족분을 단순 보충 |
| p_target 요청 + capped retry | 목표 sampling과 실제 도달 실패를 분리 |
| Widening curriculum | MiDAS식 범위 확대의 단순 adapted baseline. 동일 physical primitives로 실행 가능한 부분만 비교 |
| Reset cost 중심 schedule | Throughput 최적화가 target coverage에 주는 영향 |
| 같은 human 예산의 직접 재배치 | 복잡한 자동 scheduling보다 사람이 부족한 scene을 배치하는 것이 나은지 |

Ideal simulator teleport는 기계적 진단용이다. 비용 없는 deployable competitor로 표기하지 않는다. MEDAL/MoReFree 전체를 새 VLA backbone에 이식한 경우 원 논문 재현과 구분하고 adapter fairness를 별도 검증해야 하므로 첫 gate에 넣지 않는다.

## 5. 입력·비용·평가를 고정하는 규칙

- Scheduler 입력: 현재 RGB/proprio에서 계산한 사전 지정 scene descriptor, instruction, 과거 request/outcome/cost. 다음 task의 정답·held-out outcome·oracle feasibility는 제외한다. Simulator hidden state는 독립 평가 label에만 쓸 수 있다.
- Decision timing: task 종료 후 다음 reset request를 선택하기 전. Retry 도중의 변경 규칙과 cap도 사전에 고정한다. 결과를 본 뒤 목표를 쉬운 것으로 다시 명명하지 않는다.
- Action set: 기존 reset primitive와 그 허용 target, 제한된 human rescue. 무제한 reset retraining이나 새 관측 장치를 공짜로 추가하지 않는다.
- Budget은 `B_robot_seconds`, `B_human_seconds`, `B_compute`의 **별도 제약**으로 둔다. Task/reset/retry/안전 복귀/대기 시간을 구분하고, ticks와 human minutes를 근거 없이 합산하지 않는다. Clock overlap도 정의한다.
- 동일 초기 checkpoint, demo/replay, learner update 규칙·reward·success detector를 사용한다. Sampling 때문에 달라지는 유효 episode 수·실제 update 수를 함께 보고한다. Setup/teleoperation 비용도 별도 공개한다.
- Primary metric: fixed-target learning improvement. Secondary: worst predeclared scene group success, coverage, invalid-start rate, aborted requests, success/hour, human seconds/task.
- Test set은 scheduler tuning에 쓰지 않는다. 독립 run/day 단위 불확실성을 보고하며, 연속 episode를 모두 독립표본으로 취급하지 않는다. Confirmatory seed/trial 수는 pilot의 variance와 사전 정한 최소 유의미 효과에 근거해 고정한다. 지금 임의 trial 수를 검증 완료 수치로 만들지 않는다.

## 6. Reject / revise 규칙

1. Complete request ledger 또는 policy/reset identity가 없으면 인과·학습 효과 claim을 보류한다. Missing run을 0점으로 채워 policy competence를 추정하지 않는다.
2. Native fixed-target 성능 개선 여지가 없으면 scheduler를 구현하지 않는다.
3. Coverage 변화가 작거나 고정 target 성능의 손실이 없으면 C5의 문제 가설을 기각한다.
4. Task/scene quota 또는 같은 비용의 수동 배치로 충분하면 새 learned scheduling method를 만들지 않는다.
5. Auto-reset 평가 점수만 달라지고 `J_target`은 같으면 평가 protocol 결과로 축소한다.
6. Reset controller를 한 번 보완하는 것으로 해결되면 general VLA RL method claim을 제거한다.
7. Achieved sample에 target support가 없으면 importance weighting으로 복원하지 않는다. Coverage 안에서도 scene descriptor만으로 모든 outcome-relevant 상태가 통제됐다는 보장은 없다.
8. 단일 robot/task에서의 현상만 있으면 다양한 robot·navigation 일반화는 주장하지 않는다.

## 7. 실제 artifact 상태

- [x] 관련 문헌·공개 code provenance
- [x] AutoEval release inventory와 bounded payload 검사
- [x] Claim/estimand·baseline·입력 경계·기각 규칙 문서
- [ ] Native environment/task/reset-controller/checkpoint 조합 확정
- [ ] 실제 reset event schema와 validator, run manifest 생성
- [ ] Frozen-policy complete-ledger pilot
- [ ] Matched-budget native VLA RL 실험
- [ ] 여러 task/robot에서의 실패 조건 재현

현재는 앞 세 항목까지다. Gate A에 필요한 자원과 complete logs가 확보되기 전에는 일반적인 학습 코드 개발로 넘어가지 않는다.
