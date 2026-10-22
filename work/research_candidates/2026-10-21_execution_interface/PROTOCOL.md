# C3: 실행되는 행동을 기준으로 한 VLA RL 검증

- 작성: 2026-10-21 KST. 계산 결과를 보기 전에 고정한 1차 계약.
- C1 관측 선택, C2 수행 제약, 종료된 cross-embodiment 전이 실험과 별개다.
- 질문: **서로 다른 action token이 같은 gripper 명령으로 실행될 때, token별 PPO clipping이 물리적 정책 변화와 무관하게 달라지는가? 이 현상이 실제 VLA 학습에서 중요한가?**
- 이번 실행은 첫 질문의 공개 코드·수치 검증이다. 두 번째 질문의 정책 성능을 대신하지 않는다.

## 문헌에서 이미 해결한 부분

[CAPG, ICML 2018](https://proceedings.mlr.press/v80/fujita18a.html)와 [Marginal Policy Gradients, ICLR 2019](https://arxiv.org/html/1806.05134v3)는 실행 전 action transform을 고려한 gradient와 분산 감소를 다룬다. 행동을 동치류로 묶는 원리·Rao–Blackwellization은 신규 기여가 아니다. 단순 gripper 이진화 개선을 새 RL 알고리즘으로 발표하지 않는다.

남는 후보는 **현재 token VLA의 post-training에서 이 효과가 얼마나 크며, 기존 marginalization baseline만으로 충분한지**에 대한 좁은 실증 질문이다. Flow VLA에 같은 계산을 바로 적용할 수 있다고 가정하지 않는다.

## 고정 계약

| 항목 | 내용 |
|---|---|
| 공개 구현 | PRIME-RL/SimpleVLA-RL `7c51662df27b586f9e8a1ab35fcf849f2b8852f9` |
| 대상 경로 | LIBERO OpenVLA-OFT token sampling → native unnormalization → native normalize/invert gripper → tokenwise clipped loss |
| 실행 코드 | 원본에서 AST로 선택한 utility/loss/unnormalization 함수. 거대 모델 forward는 실행하지 않음 |
| Metadata | 저자 공개 LIBERO checkpoint의 config·dataset statistics만 조회. Weight 다운로드 없음 |
| 입력 | 모든 256 token, 의도적으로 구성한 categorical distribution. 실제 checkpoint logits 아님 |
| 고정 나머지 | 한 observation에서 6개 arm 축 고정, gripper만 변화. Reward/advantage는 실행 gripper class만의 함수 |
| Estimator | native tokenwise PPO; class probability 합으로 만든 동일 PPO; unclipped score-function PG |
| Clip | 공개 LIBERO recipe의 low 0.20, high 0.28 |
| Perturbation | class mass 고정 + 내부 재분배; 실제 class mass 변화; 변환이 없는 injective negative control |
| 분산 검사 | 전체 token을 열거한 정확한 mean/variance. Uniform 및 고정 seed 0–19의 nonuniform logits, 추가 teacher-like concentration sweep |
| 지표 | 실제 class probability, token/class KL, clipped loss·clip fraction, logit gradient mean equality·variance trace |
| 제한 | CPU Docker, 최대 4 GiB/4 CPU, 모델·환경 학습 없음. Package/source cache는 container 내부 |

분포를 synthetic으로 구성하므로 sample size를 robot episode 수로 보고하지 않는다. 정확한 유한합에는 bootstrap CI를 붙이지 않는다. Seed sweep은 distribution stress test이지 학습 seed 재현이 아니다. Native loss의 clip fraction은 advantage 부호에 따라 실제 surrogate가 잘린 비율이며, 단순 ratio 범위 이탈률과 구분한다.

## 반증·판정 규칙

1. 공개 native 경로에서 여러 token이 같은 명령으로 실행되지 않으면 C3 중단.
2. Class mass 고정 시 tokenwise loss와 classwise loss가 일치하면 PPO 표현 의존성 가설 기각.
3. Unclipped estimator의 기대 gradient가 다르면 구현/가정을 수정한다. Raw token PG를 일반적으로 biased라고 주장하지 않는다.
4. Injective control에서 차이가 남으면 구현 오류로 처리한다.
5. Marginalization이 성립하려면 return과 future policy state가 동치 token 자체에 의존하지 않아야 한다. Autoregressive action token, hysteresis, variable gripper force는 별도 감사 전 합치지 않는다.
6. 1–4를 통과해도 **mechanism-only**. 실제 native logits와 rollout에서 빈도·효과가 확인되기 전에는 본격 연구 GO나 성공률 개선을 주장하지 않는다.
7. Teacher-like distribution이 거의 각 class의 한 token에 집중하면 분산 이득이 작을 수 있다. 이 음성 조건도 함께 보고한다.

## 후속 투자 gate — 이번 실행으로 완료하지 않음

- 기존 checkpoint의 실제 gripper logits, 실행 명령, advantage를 같은 rollout에서 기록.
- Native token PPO / 기존 MPG 방식 class PPO / gripper 전용 2-class head / entropy·clip sweep / 동일 데이터 BC·return weighting 비교.
- 같은 checkpoint·trajectory·sample budget·optimizer를 사용하고 arm 경로를 고정한 진단 후 전체 정책으로 확대.
- Success와 contact/release 오류를 함께 측정. 최소 2개 task family, 여러 training seed에서 paired 결과와 CI 보고.
- 실제 logits가 거의 2개 token에 집중하거나 강한 baseline으로 효과가 사라지면 연구 주제 채택 중단.
- Multi-robot 확장은 binary gripper·continuous gripper·sticky control을 구분한 뒤 검토. 과거 RL 개선 전이 주제를 재개하지 않음.
