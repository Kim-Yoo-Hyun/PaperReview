# C2 빌드업 1차 최종 판단

- 기준일: **2026-10-21 KST**
- 결론: **현재 C2를 본격 연구 주제로 채택하지 않는다. 현 설계의 1차 검증은 NO-GO로 종료한다.**
- 완료 범위: 직접 충돌 문헌·공개 코드·실제 데이터·reference runtime의 채택 전제 검사.
- 미검증 범위: VLA policy competence, RL의 상대 성능, 다양한 로봇으로의 일반화. 이를 부정한 결과는 아니다.
- 근거: [문헌 대조](./C2_REVIEW.md) · [Docker 1차 검증 결과](../../experiments/vla_rl_c2_first_pass/RESULTS.md) · [설계와 사전 중단 기준](./C2_PROTOCOL.md).

## 1. 연구로 발전시킬 가치에 대한 답

**문제의 중요성은 있지만, 현재 제안은 독립된 top-tier 연구로 발전시키기 위한 근거가 약하다.** “수행 방식을 따르는 VLA에 RL을 적용한다”는 넓은 기여는 제외한다. 엄격한 데이터·보상 통제 아래 RL의 추가 가치를 확인하는 질문은 유용한 진단이지만, 그 검사를 가능하게 하는 전제가 성립하지 않았고 새 메커니즘도 관찰하지 못했다.

| 판단 축 | 이번에 확보한 근거 | 연구 판단 |
|---|---|---|
| 문제의 중요성 | Goal 성공과 지시된 실행 조건의 만족이 다를 수 있으며 직접 관련 연구가 존재 | 문제 자체는 의미 있음 |
| 차별성 | ExecVLA의 execution 표현, RoboFollow의 지시 평가, CounterAlign의 counterfactual reward+offline RL, dependency-coverage 분석과 겹침 | 넓은 방법 기여는 부족 |
| 남길 지식 | 동일 coverage/data/labels에서 RL과 SFT·return weighting의 차이 | 결과가 나오면 가치가 있지만 아직 측정되지 않은 진단 가설 |
| 데이터에서의 식별 | 50개 training trace의 경유 조건은 재계산 가능. 그러나 4개 training task 중 1개에만 해당 증거가 있고 완전한 goal/orientation 판정은 미확보 | 원래 조합 비교 계약 불성립 |
| 실행 비용 | 현재 ARM64 Docker의 reference dependency/GPU 경로 실패, compatible trained checkpoint 미식별 | 구현보다 데이터·환경 복구가 먼저 필요한 상태 |
| 연구축과의 연결 | 한 ALOHA arm의 작은 task 집합만 검토 | 다양한 로봇을 다루는 연구로의 연결도 아직 가설 |

위 판단은 정성적인 투자 권고다. Acceptance 확률이나 수치 점수로 표현하지 않는다. **추가 GPU가 생기더라도 차별성과 데이터 식별 문제는 별도로 남는다.** 현재 컴퓨터의 제약만으로 과학적 가치를 판단한 것이 아니다.

## 2. 선행 연구를 넘어서지 못한 부분

- [ExecVLA](https://arxiv.org/html/2603.17524v2)는 goal과 execution 제약을 분리하는 표현·생성을 다룬다. 이 분리 자체는 새 방법이 아니다. 현재 확인 status는 ICLR 2027 submission이며 채택으로 표기하지 않는다.
- [CounterAlign](https://arxiv.org/html/2608.21740)은 성공 시연의 counterfactual relabeling, 모호한 negative 처리, instruction-grounded reward와 offline RL을 결합한다. 이번에 확인한 경유 negative를 이용하는 것만으로 이 계보와 구별되지 않는다. [CoRL 2026 공식 forum](https://openreview.net/forum?id=AY4totylcx).
- [Diagnosing Compositional Generalization](https://arxiv.org/html/2607.29687)은 marginal/pair/dependency coverage의 효과를 이미 분석한다. 이 분석의 pretrained VLA 확장은 여지가 있지만, “VLA+RL로 바꿨다”는 사실만으로 새 지식이 되지는 않는다. [CoRL 2026 공식 forum](https://openreview.net/forum?id=gQFYIM5dJy).
- [RoboFollow](https://arxiv.org/html/2609.25636)는 같은 scene에서 지시에 따른 행동·실행을 구분하는 진단을 제공한다. 새 task 분할과 데이터 감사만으로 독립된 benchmark 기여를 주장하지 않는다. [CoRL 2026 공식 forum](https://openreview.net/forum?id=A9AQjk3dAt).

논문의 전 범위에 우리의 좁힌 비교가 없다는 부재 증명은 하지 않았다. 관련 본문·공개 interface와 현 데이터에 근거한 판단이다. 추가 검색에서 나온 latent compositional steering 계열은 실행 제약 factor holdout과 의미가 달라 직접 해결 증거로 사용하지 않았다.

## 3. 이번에 실제로 새로 확인한 것

**Negative 지원이 전혀 없다는 가정은 틀렸다.** 한 training task의 50개 경유 trace는 원래 waypoint에 모두 부합하고, 다른 training waypoint로 바꾸면 모두 위반했다. 이 부분은 재사용할 수 있다.

그러나 이 결과는 **RL 개선**이 아니라 **기존 데이터에 포함된 부분적인 supervision**이다. 전체 제약 reward의 label, 다른 training 조합의 동등한 증거, 새 scene의 실행 가능성이 확보되지 않아 원래 질문을 검증하는 학습으로 연결하지 않았다. 원 지시의 demonstrations가 모두 성공한다고 가정하더라도, 같은 시점의 goal-only/complete reward가 같다면 constraint reward의 효과를 그 원 지시 데이터만으로 구분할 수 없다. Discounted return의 길이 차이나 optimizer 변화가 이를 해결했다고 해석해서도 안 된다.

검사한 data format에서는 object pose/quaternion이 빠져 있었고, HDF5와 일부 metadata의 provenance도 동일 수준이 아니었다. 이는 **현재 C2 전용에 필요한 추가 계측**을 뜻하며, 원 benchmark의 결과가 틀렸다는 주장은 아니다. Source/episode ID와 수치는 [검증 결과](../../experiments/vla_rl_c2_first_pass/RESULTS.md)에 둔다.

## 4. 종료와 재개 조건

**이번 1차 빌드업의 산출물은 새로운 방법이 아니라, 현재 C2를 채택하지 않을 근거다.** 큰 RL 학습·CPU 이식·새 reward model 구현을 다음 TODO로 남기지 않는다. C1이나 이전 cross-embodiment 주제도 자동 재개하지 않는다.

다음 세 조건이 새로 충족될 때만 C2를 다시 연다.

1. 여러 training 조합에 대해 goal·waypoint·orientation을 각각 재판정할 trace와 동일 scene 식별자가 있고, label/coverage가 맞는 SFT·return-weighted·RL 비교가 가능하다.
2. 허용된 현재 컴퓨터의 Docker에서 native checkpoint의 task competence와 bounded evaluation 비용을 확인한다. 임의 toy head의 성공으로 대체하지 않는다.
3. 표준 방법 비교에서 반복되는 실패 구조를 발견해, CounterAlign·단순 reward 보강·data coverage로 설명되지 않는 **구체적인 예측 또는 원리**를 제시할 수 있다.

조건 3은 본격 방법 제안의 gate이며, 조건 1–2 이후 최소 진단으로 판단해야 한다. 조건 1–2만 충족하면 저비용 비교를 재개할 수 있지만 곧바로 top-tier 방법 연구를 승인하는 것은 아니다. 이 문서는 RL 효과의 반증이나 연구 분야 전체의 기각이 아니다.
