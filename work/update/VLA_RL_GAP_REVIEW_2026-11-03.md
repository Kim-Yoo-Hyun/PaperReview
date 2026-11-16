# VLA + RL 연구 공백 재탐색 — 2024–2026 문헌 비교

- 조사일: 2026-11-03 KST / 작업: `GAP-VRL-S1`, 후속 `R1`·`R2`·`P0-PREP`·`N1`
- 목적: 석사 과정에서 명확한 기여를 만들 수 있는 **VLA + RL** 질문을 찾는다. 성능 개선·학습 데이터·배포 제어·통합 시스템을 모두 검토한다.
- 범위: registry 1,090편의 metadata 검색과 관련 기존 합성/후보 검토, 외부 공식 proceedings·program·저자 본문 확인. 전체 1,090편 정독이나 모든 venue의 전수조사가 아니다.
- 초기 S1은 34편, R1은 누적 38편이었다. R2는 선택한 학습 규칙의 직접 선행 4편을 보완해 **당시 누적 42편(등록 16·외부 26)**이다. 2018 Q-filter foundation 1편은 2024–2026 trend 수와 분리한다. 후속 [REG-R8](./REGISTRY_BUILDUP_AUDIT_2026-11-03.md)에서 직접 선행 8편을 등록해 현재 연결은 등록 24·외부 18편이다. 당시 집계와 최신 identity 연결은 source ledger의 `scope` / `registry_sync`로 구분한다. 확인 깊이·버전·code 범위는 source ledger에 기록했다. FIRe 제출과 MiDAS workshop/preprint를 main-conference acceptance로 세지 않으며 본문 선택 절 확인은 사용자 정독 status가 아니다.
- 근거별 확인 깊이·registry identity·누락 후보·접근 제한: [단일 source ledger](../sources/vla_rl_gap_review_2026-11-03.json).
- 현행 질문의 위치: [VLA Open Questions](../../synthesis/04_vla_generalist.md#gap-vla-rl-2026-11). 이 문서는 날짜별 비교 근거이며 별도의 우선순위 registry가 아니다.
- 완료 범위: S1–R2 문헌·비교 설계, 후속 N1 내부 비실험 검토 및 읽기 전용 local Docker 확인. **정책 실행·학습·GPU allocation·성능 측정·실제 외부 피드백은 없다.** 후보의 신규성·효과·채택 가능성은 미입증이다.
- **현재 결론:** [내부 비실험 buildup 완료](#nonexperimental-completion), 탐색 유지. 독립적인 VLA 업데이트 후 residual 재사용 비용을 묻되 Q-filter 조합 자체의 신규성을 주장하지 않는다. 현재 local Docker는 NVIDIA 조건 미충족이며 [내용·재현 방법](../research_topics/vla_residual_update/내용/README.md)으로 통합했다. 다음은 호환 컴퓨터에서 미구현 image/adapter부터 완성하는 `GAP-VRL-P0`다.

## 1. 이번에 우선 탐색할 질문

**우선순위 1은 ‘VLA를 독립적으로 개선한 뒤, 기존 residual을 적은 추가 학습으로 재사용하면서 새 VLA의 이득도 보존할 수 있는가?’다.** R1에서 동일 residual의 backbone 전이와 base/editor 공동 학습 선행을 확인했다. 따라서 전이 가능성 자체보다 기존 보정의 필요성이 달라진 조건에서의 적응 비용과 개선 보존을 묻는다. 아직 독립 방법 기여가 입증된 주제는 아니다.

**우선순위 2는 ‘목표별 데이터 coverage가 달라질 때 counterfactual RL 보상의 유효성이 유지되는가?’다.** 단순한 언어 무시·잘못된 negative 문제는 이미 다뤄졌다. 목표가 달라도 같은 초기 행동이 유효한 사례에서, 관측·행동 이웃을 이용하는 필터가 데이터 구성에 얼마나 의존하는지를 좁혀 묻는다.

| 순서 | 공백 후보 / 공식 용어 중심 설명 | 기대 기여 | 석사 관점 판단 |
|---|---|---|---|
| 1 | **Residual policy adaptation across VLA updates** — 독립적인 기반 VLA 업데이트 이후 RL 보정의 적응 | 새 base 이득을 보존하며 추가 학습 비용을 낮추는 방법 | R1: 좁혀서 탐색 유지. 동일 가중치 전이 자체는 FIRe와 겹침. 공개 A/B 후보 확보, 효과·native 호환성 미검증 |
| 2 | **Coverage-aware counterfactual reward learning** — 목표별 coverage를 고려한 반사실 보상 학습 | 보상 label의 신뢰도와 offline policy 개선을 연결하는 방법·분석 | 데이터/보상 단계에서 싸게 탐색 가능. CounterAlign과 차이가 좁아 직접 충돌 위험은 1번보다 큼 |
| 예비 A | **Observation-constrained RL-to-VLA distillation** — 학생 관측으로 실행 가능한 RL 교사 행동의 생성 | RL-generated data의 유용성을 높이는 teacher objective·데이터 생성 | 기존 privileged distillation/부분 관측 선행 및 과거 GAP-CF와 중복이 크다. 새 관측 비교가 있어야 발전 |
| 예비 B | **Independent validation for model-based VLA RL** — world model과 보상 모델의 공동 오류를 분리한 검증 | 상상 rollout의 신뢰도와 실제 task 만족을 연결하는 학습·검증 | 최신 직접 충돌이 많고 모델/실환경 비용이 높다. 현재 주력으로 추천하지 않음 |

이는 **탐색 순서**다. 네 후보를 모두 새 연구 프로젝트나 실험 대기로 등록하지 않는다. 단순 baseline이 있다는 이유로 1·2번을 포기하지 않으며, 그 baseline이 실제로 충분한지는 작은 비교로 판단한다.

## 2. 실제로 확인한 연구 흐름

### 2.1 조합 자체를 새 기여로 잡기 어려운 영역

| 이미 연구된 축 | 2024–2026 직접 근거 | 이번에 새로 주장하지 않을 것 |
|---|---|---|
| VLA 직접 RL post-training | [ConRFT, RSS 2025](https://www.roboticsproceedings.org/rss21/p019.html), [SimpleVLA-RL, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) | VLA에 RL을 적용하면 성공률이 좋아진다는 조합 자체 |
| RL 교사·specialist로 VLA 데이터 생성 | [HumanVLA, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html), [RLDG, RSS 2025](https://www.roboticsproceedings.org/rss21/p028.html), [PLD, ICLR 2026 공식 program](https://iclr.cc/virtual/2026/poster/10008318) | RL-generated data 또는 generalist–specialist–distillation 파이프라인 그 자체 |
| Frozen VLA + residual 제어 | [Object-Centric Residual RL, CoRL 2026 accepted](https://openreview.net/forum?id=tAXtXe4Oqd), [VLaRL, 2026 preprint](https://arxiv.org/abs/2609.30868) | 객체 pose나 latent로 residual을 학습하고 sim-to-real로 배포한다는 조합 |
| World model 안에서 VLA 개선 | [VLA-MBPO, ICML 2026](https://proceedings.mlr.press/v306/zhang26ez.html), [VLAW, ICML 2026](https://proceedings.mlr.press/v306/guo26i.html), [RehearseVLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) | 상상 데이터로 실제 interaction 비용을 줄이거나 world model을 계속 개선하는 발상 |
| Recovery·long-horizon credit | [RePO-VLA](https://neurips.cc/virtual/2026/poster/153104), [OGPO](https://neurips.cc/virtual/2026/poster/152279), [PAPO-VLA](https://neurips.cc/virtual/2026/poster/149215), [LiFT](https://neurips.cc/virtual/2026/poster/151131), 모두 NeurIPS 2026 공식 program | 실패 prefix 재활용·goal relabeling·중요 decision의 advantage·분기 rollout 자체 |
| Offline value 기반 flow policy 개선 | [VISTA, NeurIPS 2026](https://neurips.cc/virtual/2026/poster/148918) | Critic의 보수적 국소 지도·BC anchor·빠른 action generator의 결합 자체 |
| 언어·세부 지시를 반영한 학습 | [CounterAlign, CoRL 2026 accepted](https://openreview.net/forum?id=AY4totylcx), [FineVLA, NeurIPS 2026](https://neurips.cc/virtual/2026/poster/154540) | 언어를 보상에 넣거나 세부 지시 annotation을 제공한다는 발상 |
| VLA 고수준 판단 + RL 이동 제어 | [NaVILA, RSS 2025](https://www.roboticsproceedings.org/rss21/p018.html), [TIC-VLA, ICML 2026](https://proceedings.mlr.press/v306/huang26cd.html) | Navigation과 RL의 계층적 결합 또는 추론 지연을 고려하는 제어 자체 |
| 실제 로봇의 RL 안정화·효율화 | [HIL-SERL, Science Robotics 2025](https://doi.org/10.1126/scirobotics.ads5033), [RL-100, Science Robotics 2026](https://doi.org/10.1126/scirobotics.aed6267) | Human intervention·offline→online RL·고주파 diffusion 정책 개선 자체 |

### 2.2 최신 충돌을 빼놓으면 생기는 잘못된 gap

- [MERL, 2026-10 preprint](https://arxiv.org/abs/2610.16517)은 world model/reward proxy의 갱신과 신뢰도에 따른 상상 비율·horizon·replay 가중치를 이미 다룬다. ‘불확실하면 상상 rollout을 줄인다’는 제안은 충분히 새롭지 않다.
- [RAW-Dream, NeurIPS 2026](https://neurips.cc/virtual/2026/poster/153917)은 task-agnostic world model·VLM 보상·dual-noise 검증을 다룬다. 목표마다 모델을 새로 만드는 비용만 지적하는 것도 부족하다.
- [SOLE-R1, NeurIPS 2026](https://neurips.cc/virtual/2026/poster/153893)은 부분 관측·분포 변화에서의 video-language reward와 reward hacking을 직접 대상으로 삼는다. 보상 모델의 취약성을 모두 미해결 영역으로 쓰지 않는다.
- [EXPLORE, NeurIPS 2026](https://neurips.cc/virtual/2026/poster/153607)는 배포 시 action-chunk 탐색과 online RL을 다룬다. Test-time RL 자체가 새 방향인 것은 아니다.

이 표는 각 방법이 관련 문제를 **완전히 해결했다**는 뜻도 아니다. 이미 제시된 방법을 강한 비교 대상으로 포함하고, 그 평가 범위를 넘어서는 질문을 명시하자는 의미다.

<a id="residual-transfer"></a>

## 3. 우선순위 1 — VLA 업데이트 후 residual RL 정책의 재사용

### 근거와 남는 질문

Object-Centric Residual RL은 현재 base action·객체 pose·proprioception을 residual에 제공한다. Sim/real VLA를 같은 시연 행동으로 정렬하고, deployment에서는 같은 residual을 real VLA에 연결한다. 서로 다른 VLA backbone의 결과와 residual rollout을 이용한 base SFT도 제시한다. 따라서 **base action conditioning·base 교체·self-improvement를 처음 제안한다고 할 수 없다.** [본문 §3.1–3.4, §5.1·5.4](https://arxiv.org/html/2606.18953v1)

PLD는 frozen base 위에서 residual specialist를 배우고, deployment 상태에 맞춘 hybrid rollout을 수집한 뒤 generalist를 SFT한다. 이미 state-distribution mismatch를 줄이는 설계다. 다만 확인한 자료로는 **base를 반복 개선한 후 기존 residual 가중치를 그대로 연결하는 교차 비교**의 범위를 확정하지 못했다. [PLD 본문 §3, 부록 B·C](https://arxiv.org/html/2511.00091v1)

**질문:** 같은 robot/controller에서 base VLA를 A에서 B로 개선했을 때, A용으로 학습한 residual의 추가 이득은 유지되는가? 유지·퇴행을 결정하는 것은 base action의 분포인가, 방문 상태의 변화인가, 아니면 둘의 결합인가?

위는 S1의 탐색 질문이다. **R1 보완:** Object-Centric의 backbone 간 동일 가중치 여부는 여전히 미확정이지만 FIRe 저자 project는 같은 residual의 backbone 전이를 명시한다. EXPO 계열의 공동 학습도 있으므로 질문을 아래 [독립 업데이트·이득 보존·적응 비용](#residual-r1)으로 좁힌다. 선행에 실험이 없다는 포괄적 결론은 내리지 않는다.

### 방법으로 발전시킬 수 있는 지점

- 한 base에 대한 고정 correction보다 **여러 base가 만드는 행동 조건에 적응하는 residual**을 학습한다는 가설.
- 가벼운 gain/clip 재조정으로 해결되지 않는 경우에만 base-action 변화와 상태 변화를 분리한 조건화·학습 분포·재학습 전략을 설계한다.
- 기여의 목표는 단일 checkpoint에서 더 높은 성공률뿐 아니라, **base upgrade 횟수가 늘 때 추가 RL interaction을 얼마나 재사용할 수 있는가**다.

단순히 policy ID를 입력하거나 base ensemble로 domain randomization하는 것만으로 기여를 확정하지 않는다. 그런 단순 대안의 효과와 한계를 먼저 비교한다. Residual이 base를 무시하고 독립 specialist가 되는 경우에는 VLA 기반 개선이라는 해석도 약해진다.

### 가장 작은 판별 비교

| 고정할 것 | 비교할 것 | 관측·해석 |
|---|---|---|
| 같은 embodiment·task·action units·normalizer·control rate·observation | A, A+residual-A, B, B+residual-A | B 자체의 이득과 residual의 추가 이득 분리. A+residual-A가 유효하지 않으면 전이 질문을 시험할 수 없음 |
| 같은 초기 상태·평가 예산 | B+gain-adjusted residual-A, B+retrained residual-B | 단순 보정 대안과 목표 base 전용 재학습의 비교. 재학습 비용도 계산 |
| 공유 상태 집합과 실제 closed-loop rollout을 구분 | 동일 상태의 action shift, 정책별 방문 상태 변화 | Offline action 차이를 native 성공의 대체 지표로 쓰지 않음 |
| 평가용 B를 학습 base 집합에서 제외 | 여러 base로 학습한 residual vs 단일 base residual | Base 다양성 학습의 일반화인지 B를 미리 본 효과인지 분리 |

성공률 외에는 task 실패 종류·불필요한 correction·완료 시간·새 RL 환경 step/실시간·reset/human 비용을 기록한다. Gain 튜닝은 calibration에서 하고 최종 비교 task/seed로 튜닝하지 않는다. 초기 탐색은 한 robot과 두 base로 시작할 수 있다. 범용 방법을 주장할 때 여러 독립 base 업데이트와 task에서 확인해야 한다.

**축소/중단:** gain/clip만으로 충분하거나 현재 base action 입력만으로 잘 전이되면 복잡한 새 residual 방법을 만들지 않는다. 이 경우의 유용한 결론은 저비용 재사용의 조건이다. 반대로 반복적인 negative transfer가 있고 작은 개선이 재학습 비용을 낮추면 방법·시스템 연구로 발전시킨다.

**자원 판단:** frozen VLA inference와 작은 residual RL로 시작할 여지는 있지만 필요한 GPU 메모리·처리량은 미측정이다. 큰 VLA 두 개를 새로 학습하는 설계는 우선 피하고, 호환되는 공개 base checkpoint 쌍부터 확인한다. 이번에는 image/adapter/실행 packet을 만들지 않았다.

<a id="counterfactual-coverage"></a>

## 4. 우선순위 2 — 데이터 coverage에 따른 반사실 보상의 신뢰도

### 먼저 수정한 초기 가설

‘다른 지시를 붙였다고 항상 잘못된 행동은 아니다’는 이미 CounterAlign이 명시한 문제다. 이 논문은 관측·행동 기반 유사도 필터와 jointly relabeled tuple의 nnPU 학습을 쓴다. 특히 부록의 instruction similarity는 단순 텍스트 거리와 다르며, 해당 목표의 시연 집합에서 **관측 유사도 × 행동 유사도의 최댓값**을 구한다. [§1·3.2와 부록 식 (7)–(10), Algorithm 1](https://arxiv.org/html/2608.21740v1)

따라서 공유 prefix를 인정하는 보상, state-aware 필터, false-negative 완화 자체를 새 방법으로 제시하지 않는다. 또한 이 논문은 action relabel 뒤 대응 next state가 없다는 점을 이미 구분한다. 임의 action을 바꾼 tuple을 정상 Bellman transition처럼 사용하는 비교를 만들지 않는다.

### 더 좁은 질문

**같은 원 tuple과 실제 행동 의미를 유지하면서 목표별 시연 coverage가 바뀌면, negative 선정과 보상 신뢰도가 얼마나 달라지고 그 변화가 offline RL의 지시 준수에 영향을 주는가?**

연구자 해석으로 다음을 도출한다. 고정 feature와 query에서 후보 집합에 항목을 더하면 max similarity는 감소하지 않는다. 하지만 중간 범위 threshold를 사용하는 negative 채택 여부는 진입하거나 이탈할 수 있다. 이는 **선정 규칙의 수학적 성질**이며, CounterAlign이 실제로 오류를 내거나 성능이 감소한다는 실험 결과가 아니다. Exact duplicate를 더하는 것만으로 max 값이 바뀌는 것도 아니다. 중복·표본 수·유효 coverage·다양성을 분리해야 한다.

가능한 차이는 ‘shared prefix를 모른다’가 아니라 **관측되지 않은 유효 대안과 부적합 행동을 유한한 시연 coverage에서 얼마나 구별할 수 있는가**다. 잘 관측된 목표와 희소한 목표에서 동일 threshold·class prior가 충분한지를 먼저 확인한다.

### 탐색과 기여의 경계

1. 공개 task 정의상 두 목표에 공통으로 유효한 초기 행동과, 실제로 목표를 구분해야 하는 행동을 소수 확보한다. 서로 다른 episode의 영상 유사성만으로 유효성을 단정하지 않는다.
2. Reward/discriminator용 reference pool만 조절하고 actor 학습 transition·query 집합을 고정하여 필터 효과를 먼저 분리한다. 실제 policy 학습용 데이터까지 바꾼 비교는 별도의 효과다.
3. 원 CounterAlign 필터+nnPU, goal-balanced subsampling, 단순 threshold calibration, ambiguous tuple 제외를 비교한다. **이미 존재하는 강한 필터를 제거한 약한 baseline을 주 비교로 쓰지 않는다.**
4. 명백한 valid/invalid/판정 불가를 구분해 label error·보상 구분·지시별 편차를 본다. 이후에만 동일 actor budget의 BC/return-weighted imitation/offline RL에서 native 행동 차이를 확인한다.

방법 발전 가능성은 coverage에 따른 confidence/negative weighting 또는 추가 관측이 필요한 tuple의 선택이다. 그러나 일반적인 PU learning·class imbalance·noisy-label 학습과의 차이를 별도 확인해야 한다. 작은 label 감사가 곧 offline RL 성능 향상인 것은 아니다.

**축소/중단:** CounterAlign 필터+nnPU 또는 단순 목표 균형만으로 충분하면 새 reward 방법의 동기가 약하다. 반대로 같은 의미의 valid action이 sparse goal에서 일관되게 오판되고 native 학습까지 바꾼다면 명확한 방법 기여로 이어질 수 있다. GPU 확보 전에는 task/label 정의와 공개 implementation 확인을 진행할 수 있다.

## 5. 예비 후보와 우선순위를 낮춘 이유

### A. 학생 관측으로 실행 가능한 RL 교사의 학습

HumanVLA의 privileged teacher→VLA distillation, RLDG의 action/state coverage 분석, PLD의 deployment-aligned rollout이 이미 선행한다. Object-Centric Residual RL도 privileged-state distillation의 손실을 비교한다. 위 방법들이 모두 학생의 정보 부족을 무시한다고 말할 수 없다.

남는 조건부 질문은 **동일 학생 관측에서 구별할 수 없는 상황에 교사가 서로 다른 action을 요구하는 경우, 학생에게 실행 가능한 teacher behavior를 RL 단계부터 만들면 같은 데이터 예산의 distillation이 나아지는가**다. RL은 교사의 성공률뿐 아니라 배포 관측에서의 실행 가능성을 최적화하는 역할이 된다.

가장 단순한 비교는 history 추가, 관측 일치 teacher, DAgger, ambiguity filtering이다. 교사 정보가 실제로 부족한지, 단순 시각 표현·학습 오차인지 먼저 구분해야 한다. **기존 GAP-CF의 부분 관측 질문과 겹치므로 새 독립 주제로 자동 등록하지 않는다.** 학습 가능한 teacher objective와 새로운 matched 사례가 확보될 때 예비 후보로 재검토한다.

### B. World model과 보상 모델의 공동 오류에 대한 독립 검증

VLA-MBPO·VLAW·RehearseVLA에 더해 MERL·RAW-Dream·SOLE-R1까지 고려하면 ‘신뢰도가 낮은 imagination을 거른다’는 수준은 포화되어 있다. 남는 질문은 **모델의 일관성과 보상 예측이 함께 틀리는 상황에서, 독립적으로 관측한 task 만족이 RL 업데이트의 방향을 추가로 바꾸는가**다.

World model confidence·reward score·독립 실제 task 관측을 분리한 비교가 필요하다. 단순 주기적 real validation과 더 짧은 rollout도 기준선이다. Independent check를 붙이는 파이프라인만으로 새 기여가 되는 것은 아니다. 어떤 오류가 상관되어 있고 고정 real-interaction 예산에서 어느 자료가 가장 유용한지를 보여야 한다.

기존 C4 reward audit·GAP-WM과 연결되고 여러 모델 및 실제 interaction이 필요하다. **질문 중요성은 높지만 현재 석사 주력 후보로는 실행 비용과 충돌 위험이 크다.**

### Navigation을 별도 1순위로 만들지 않은 이유

NaVILA는 VLA 중간 명령과 RL locomotion을 결합하고, TIC-VLA는 비동기 의미 추론 지연과 online RL을 다룬다. 여기에 장기 task 연결을 붙이는 일반 제안은 기존 HANDOFF 및 [Foresight Residual RL preprint](https://arxiv.org/abs/2607.16506)의 terminal-state 가치 문제와 겹친다. 이번 조사에서 manipulation의 1·2번보다 더 분명하고 저비용인 새 navigation 질문을 확보하지 못했다. Navigation의 가치가 낮다는 판단은 아니다.

## 6. 기존 후보와의 관계

| 기존 연구 | 이번과의 관계 | 유지할 경계 |
|---|---|---|
| 초기 cross-embodiment RL transfer | 1번도 transfer를 묻지만 **동일 robot의 base update**부터 다룸 | 다른 로봇으로의 RL 이득 전이를 입증했다는 뜻이 아님. 기존 RETIRED 유지 |
| HANDOFF | 정책 교체가 다른 모듈에 영향을 준다는 상위 문제는 공유 | 기존은 nav→manipulation 종료/도착 조건, 새 1번은 학습된 action residual과 base의 결합. 같은 질문으로 확인되면 통합 |
| REVISION·SET | 2번은 언어 정합과 연결 | 실행 중 지시 교체나 수량 반복이 아니라 **offline reward supervision**의 coverage를 연구 |
| RETRIEVAL | 데이터 pool 구성의 영향이라는 분석 습관은 공유 | Inference context 선택과 reward-training negative 생성은 다른 단계. 단지 pool을 늘린 실험만으로 별도 기여를 주장하지 않음 |
| C2·E1·GAP-CF | 정보/coverage·replay 문제와 연관 | 이전 label/identity/관측 요건과 NO-GO/HOLD를 무효화하지 않음 |
| C4·GAP-WM | 예비 B의 직접 선행 내부 검토 | 보상 검증을 새 이름으로 재개하지 않음 |
| C3·E2·CODEC1 | action interface·시간 단위는 공정 비교의 조건 | 이번 RL 탐색으로 기존 token/timing 연구의 결론을 변경하지 않음 |

기존 5개 주제의 문서·실험 준비를 보존했다. 다만 **현재 새 탐색의 첫 TODO는 VLA+RL의 1번 후보**이며, ‘항상 REVISION만 다음에 실행한다’는 이전 운영 추천이 이번 주제 탐색을 제한하지 않는다.

<a id="source-boundary"></a>

## 7. 출처 확인의 범위와 남은 일

- 2024–2026 공식 학회·저널 및 최신 preprint를 구분했다. NeurIPS 2026는 공식 program/abstract에 등재된 논문이다. CoRL 2026는 [공식 accepted papers](https://www.corl.org/program/accepted-papers)에서 Object-Centric Residual RL·CounterAlign을 exact title과 forum ID로 확인했다. 학회 개최 전이므로 발표 완료와 혼동하지 않는다.
- CounterAlign은 기존 registry의 `pr-1033`이며 CoRL status가 확인된다. 검색에서 arXiv가 먼저 나왔다는 이유로 신규 논문이나 미채택 preprint로 중복 등록하지 않는다.
- Object-Centric Residual RL, CounterAlign, PLD, VLaRL은 관련 방법/평가/한계의 **선택 절**을 확인했다. 모든 부록·code를 완전 정독했다고 표시하지 않는다. 나머지는 주로 공식 abstract/program 및 저자 project 수준이다.
- Science Robotics publisher 본문은 접근 제한이 있어 HIL-SERL은 저자 project, RL-100은 저자 arXiv와 publication metadata를 구분했다. 두 논문은 robot RL 근거이며 모두 language-conditioned VLA라고 분류하지 않는다. RA-L은 GRAD-NAV++의 publisher 검색 metadata까지 확인했으나 본문/abstract 페이지는 JS 차단으로 핵심 gap 근거에 포함하지 않았다.
- PLD의 공식 ICLR program과 저자 project를 확인했으나 공개 training repository는 식별하지 못했다. Object-Centric Residual RL·CounterAlign도 현재 확인한 자료에서 실행 가능한 전체 release를 확정하지 못했다. **미식별과 미공개를 구분한다.** R1에서는 관련 부록과 공개 code 여부를 추가 확인했고, 접근할 수 없는 최종 본문·미식별 release의 불확실성을 §10에 남겼다.
- VLA-MBPO는 공식 ICML proceedings를 venue 근거로 삼았다. 검색되는 다른 PDF의 ICLR 표기는 version/동명 충돌 가능성이 있어 미해결 source anomaly로 기록했다. 별도 논문을 추가하거나 registry venue를 임의 변경하지 않았다.
- CVPR·NeurIPS·ICLR·ICML·RSS·CoRL과 robot RL journal 근거를 중심으로 비교했다. ICRA는 registry의 SERL 등 배경 계보를 확인했으며, ICCV/ECCV/IROS/T-RO/IJRR 전체를 이번에 전수 검토했다고 주장하지 않는다. 후보별 direct collision 검토를 우선했다.

## 8. S1에서 정한 R1 완료 기준

**`GAP-VRL-R1`: 아래 검토를 수행했으며 결과와 남은 불확실성은 §10에 기록했다.**

1. Object-Centric Residual RL·PLD·VLaRL 및 인접 residual policy transfer 연구의 최종 본문/부록/공개 code에서 base freeze, 교체 방식, 동일 residual 가중치 여부, self-improvement 후 재평가를 표로 확정한다.
2. 같은 robot/controller의 공개 checkpoint 두 개가 동일 입출력을 갖는지 확인한다. 아직 없는 checkpoint·Docker image·코드 기능을 있다고 가정하지 않는다.
3. `A → B` 교체에서 무엇이 새로운지 한 문장으로 쓰고, base-action shift와 visitation shift를 구분하는 최소 비교를 정한다. Gate를 지나기 위한 대량 문서·전체 실험 manifest부터 만들지 않는다.
4. 선행에 같은 비교가 있으면 남은 조건을 좁히거나 후보 2로 이동한다. 불명확하다는 이유만으로 논문 가치가 없다고 결론내리지 않는다.

후보 2는 CounterAlign의 filter/nnPU와 데이터 coverage 대조를 먼저 구성한다. 실제 실험으로 넘어갈 때만 현재 컴퓨터의 local Docker/GPU를 확인하고, 가능한 조건이면 최소 검증을 실행한다. 자원이 부족하면 clone 후 재개 준비를 한다. **이번 결과는 후보 선정에 필요한 근거이며 full buildup 완료 또는 신규 방법 GO가 아니다.**

## 9. S1 저장소 반영·검증

다주제 조사 문서와 단일 source ledger를 추가하고, canonical Open Questions·TODO·운영 초점을 연결했다. Paper 신규 등록·tier/읽기 status 승격·기존 실험 판정 변경은 없다. Generator compile/재생성, repository audit, staged/unstaged whitespace 검사가 통과했다. Audit은 1,090편·5,450개 표준 노트에서 오류·경고 0이다. 기존 노트·registry·tracker·연구/실험 파일 5,782개의 hash와 staged index를 보존했다. Source key·registry identity·신규 JSON/공백 검사도 통과했으며 상세 결과는 source ledger의 `validation`에 기록했다.

<a id="residual-r1"></a>

## 10. R1 결과 — 직접 선행과 공개 checkpoint

R1은 `CONTINUE_EXPLORATION_NARROWED`로 완료했다. Object-Centric·FIRe의 residual 전이, EXPO 계열의 공동 적응을 반영하여 단순 VLA 간 전이의 최초 주장을 버리고 독립 checkpoint 교체 후 재사용 비용으로 질문을 좁혔다. 공개 A/B revisions·같은 normalizer·parameter key를 확인했지만 exact-parent·native IO·residual checkpoint는 미확인이었다.

상세 직접 비교는 [주제 내용](../research_topics/vla_residual_update/내용/README.md), checkpoint/source는 [재현 방법](../research_topics/vla_residual_update/재현%20방법/README.md#checkpoints)으로 통합했다. 당시 검증·준비 범위는 원장의 `r1_review`에 보존한다.

<a id="residual-r2"></a>

## 11. R2 결과 — 비교 계약과 적응 규칙

R2는 `DESIGN_READY_EXPLORATION_NATIVE_UNVERIFIED`로 완료했다. 한 LIBERO task에서 actor만 이전하고, 새 critic·동결 A encoder·공통 old data를 사용하며 gain/warm/fresh/단일 Q-filter/imitation 대조와 예산을 고정했다. 규칙 자체의 신규성은 미확정이며 학습·정책 결과는 없었다.

설명은 [내용 §3–7](../research_topics/vla_residual_update/내용/README.md), 단일 기계 계약은 [source 원장](../sources/vla_rl_gap_review_2026-11-03.json)의 `r2_review.comparison_contract`에 있다. 기존 보고서의 R1/R2 중복 본문을 이 주제의 `내용/`·`재현 방법/`으로 이동했다. 당시 audit와 5,994개 파일·staged index 보존 결과는 원장의 `r2_review.validation`에 유지한다.

<a id="nonexperimental-completion"></a>

## 12. 비실험 buildup 종료와 local Docker 확인

2026-11-03 후속 요청으로 `GAP-VRL-P0-PREP`의 자원 확인과 `GAP-VRL-N1`의 내부 비실험 보완을 완료했다. 현재 Darwin arm64·local Docker Desktop Linux aarch64·7.65 GiB, NVIDIA runtime 미표시 및 사용자 비-NVIDIA 설명으로 target CUDA 조건 미충족을 확인했다. 새 allocation container·다운로드·추론·학습은 실행하지 않았다. [정확한 command/관측 및 재개 계획](../research_topics/vla_residual_update/재현%20방법/RESUME_PLAN.json).

추가 검토에서 base-action 입력 분포 변화·critic 추정 오차·단순 gain/모방 대안을 명시하고 A bootstrap과 B 적응의 target을 구분했다. 원 SETUP의 unpinned 의존성과 driver/CUDA 표기를 검토하여 검증된 lock으로 잘못 전달하지 않도록 했다. [Guide 단계 0–8 완료 범위·주장–증거·독립 검토 질문](../research_topics/vla_residual_update/내용/README.md#nonexperimental-completion)을 작성했다.

**현재 판단:** 작은 비교를 할 가치가 있는 탐색 후보. 가능한 내부 비실험 검토는 완료했으며 실제 효과·독립 기여·외부 피드백은 미확인이다. 다음은 호환 NVIDIA 컴퓨터에서 미구현 image/adapter/assets부터 완성하는 `GAP-VRL-P0`다. GPU 확보만으로 실행 준비/연구 가치가 자동 확정되지 않는다. 같은 metadata/문헌 집계나 현재 실패 조건의 GPU probe를 반복하지 않는다.

Registry·tier·사용자 reading status는 바꾸지 않았다. 새 논문 등록 없이 generator compile/재생성·JSON 참조/예산·whitespace·repository audit를 통과했다. Audit은 **1,090편·5,450 notes·오류 0·경고 0**, 보호 대상 기존 파일 5,991개와 staged index는 그대로다. 상세는 source 원장의 `nonexperimental_completion.validation`에 기록했다. Runtime/정책 효과 검증을 의미하지 않는다.
