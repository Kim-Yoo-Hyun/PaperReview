# GAP-CF1 — 숨은 시연 정보와 행동 coverage를 구별할 수 있는가?

- 검토일: 2026-10-23 KST. 문헌·공개 코드 정적 검토이며 실행·학습·성능 측정은 하지 않았다.
- 작업 판정: **GAP-CF1 DONE**. 연구 판정: **일반 deconfounding 방법·단순 cue 대 시연량 비교 NO-GO / 조건부 진단 REVISE·HOLD**.
- Canonical 질문: [GAP-CAUSAL](../../synthesis/02_rl_il_offline.md#gap-causal-2026). [출처·version·code hash ledger](../sources/causal_information_coverage_review_2026-10-23.json).
- 초기 RL 전이/C2 및 기존 후보를 재개하지 않는다. Registry admission, tier, 사용자 reading status는 변경하지 않았다.
- 후속 판정: [GAP-CF2 자료 충분성 심사](./CAUSAL_DATA_SUFFICIENCY_REVIEW_2026-10-23.md)에서 현재 공개 자료 설계를 문헌 진단으로 종료했다. 아래 CF1의 조건부 HOLD/다음 TODO는 당시 판단을 보존한 기록이다.

## 1. 결론과 남길 질문

**“시연자만 아는 정보를 활용해 VLA의 교란을 제거한다”는 넓은 방향은 신규 기여로 부족하다.** 불확실성 분해, history 기반 식별, partial identification, 연속 행동 flow 정책까지 직접 선행이 있다. 특히 CIVIL은 학습 중 사람의 추가 단서와 더 많은 시연을 같은 수집 시간에서 비교했다. 따라서 “추가 정보를 기록할지 행동을 더 모을지 비교”하는 것만으로도 부족하다. [Delphic](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html), [DML-IL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html), [CFQL](https://proceedings.mlr.press/v306/li26ja.html), [CIVIL §7](https://link.springer.com/article/10.1007/s10514-026-10266-3).

남길 수 있는 질문은 **배포 정책이 볼 정보와 총 수집 비용을 고정했을 때, 추가 학습용 cue와 통제된 행동 수집 중 무엇이 정책 선택 오류를 줄일지 사전에 구별하는 조건이 있는가**다. Cue 자체가 추론 시 새 센서로 제공되면 다른 문제다. 단순 history BC·정보 정렬·표적 데이터 수집이 같은 결과를 설명하면 별도 causal 방법을 만들지 않는다. 이것은 아직 답이 없는 것으로 입증된 공백이 아니라, 추가 심사가 필요한 연구자 해석이다.

현재 주력 연구로 채택할 근거는 부족하다. 가치가 생기려면 기존 방법을 VLA에 이식하는 것보다 **어떤 추가 정보로도 해결되지 않는 support 부족과, 적은 추가 정보로 해소되는 선택 오류를 실제 자료에서 구분**해야 한다. 그 구분을 평가할 공통 데이터·정책·native evaluator 묶음은 아직 없다. GPU 확보만으로 이 문제가 해결되지는 않는다.

## 2. 조사 범위와 근거 깊이

14편: 2024–2026 공식 proceedings/journal/pre-proceedings 근거 11편, arXiv status 1편, 공식 NeurIPS 목록 등재이나 상세 status를 확정하지 않은 1편, 2019 foundation 1편이다. 12편의 지정 본문/부록을 대조했고 2편은 공식 abstract 범위다. 이는 targeted collision review이며 모든 top-tier venue의 전수 조사나 전체 증명 검증이 아니다. ArXiv 본문과 최종 proceedings의 완전한 동일성도 보장하지 않는다.

| ID | 논문·공식 status | 실제 확인 범위 | 가정·기여의 경계 |
|---|---|---|---|
| F01 | [Offline Policy Evaluation and Optimization Under Confounding](https://proceedings.mlr.press/v238/kausik24a.html), AISTATS 2024 | [공식 PDF](https://proceedings.mlr.press/v238/kausik24a/kausik24a.pdf) Table 1, §2–5, 특히 §4.1·Assumptions 4–6 | Memoryless/global/general memory를 구별. Global recovery에는 mixing·separation·coverage 등의 구조가 필요하며 reward 가정도 다른 causal RL과 같지 않음 |
| F02 | [Two-way Deconfounder for Off-policy Evaluation in Causal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ecf25e3a462e9bb1e29662dfe7258fe-Abstract-Conference.html), NeurIPS 2024 | [v1 §2·4·5.3, App A.2–3](https://arxiv.org/html/2412.05783v1) | Trajectory/time 두 latent factor, latent를 포함한 visitation 가정. §5.3에 interaction-specific 교란 위반 실험이 이미 있음 |
| F03 | [Confounding Robust Deep Reinforcement Learning: A Causal Approach](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c9a177f06ecd9892cd1664d89994fb58-Abstract-Conference.html), NeurIPS 2025 | [v1 §2–4, App B.2·G](https://arxiv.org/html/2510.21110v1) | 유한 discrete action·bounded reward·positivity. Masked Atari의 유용한 행동 support 부재와 확률적 expert 관련 실패를 직접 명시 |
| F04 | [Automatic Reward Shaping from Confounded Offline Data](https://proceedings.mlr.press/v267/li25dr.html), ICML 2025 | [v1 §2–4](https://arxiv.org/html/2505.11478v1) | Causal upper bound를 potential로 사용해 **online** 탐색을 돕는다. 복수 behavior 자료의 bound 결합도 선행에 포함 |
| F05 | [Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html), ICLR 2026 | [v2 §3–5, App D.2·E·F](https://arxiv.org/html/2502.07656v2) | DML-IL: additive noise·유한 noise horizon·유효하고 충분히 강한 history IV. 목표는 history에 조건부 평균낸 expert이며 개별 hidden state의 privileged expert와 다름 |
| F06 | [Causal Imitation for Markov Decision Processes: a Partial Identification Approach](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9f7f2f57d8eaf44b2f09020f64ff6d96-Abstract-Conference.html), NeurIPS 2024 | [공식 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f7f2f57d8eaf44b2f09020f64ff6d96-Paper-Conference.pdf) Table 1, §2.1·3.1–2 | CAIL-R/T가 요구하는 identifiable reward/transition 구분. 양쪽 모두 임의로 미식별인 경우의 expert imitation 보장으로 확대 불가 |
| F07 | [Confounded Causal Imitation Learning with Instrumental Variables](https://arxiv.org/html/2507.17309v1), arXiv 2025 | v1 §2–4 | C2L의 IV 선택은 linear/non-Gaussian 또는 nonlinear regularity 등에 의존. Linear-Gaussian 한계를 본문이 명시; 임의 robot history에서 IV를 발견한다는 보장 아님 |
| F08 | [CofactVLA: Deconfounding Vision-Language-Action Models via Counterfactual Intervention](https://arxiv.org/html/2608.04396v1), 2026 | v1 §3–4.1·App A.7; code | [공식 NeurIPS Downloads](https://neurips.cc/Downloads/2026)에 title 등재, 저자 code도 NeurIPS 표기. 상세 poster page 접근 실패로 최종 proceedings/main-track 세부 status 미확정. Model 내부 개입이며 hidden physical confounder의 식별과 구별 |
| F09 | [Causal Confusion in Imitation Learning](https://papers.nips.cc/paper_files/paper/2019/hash/947018640bf36a2bb609d3557a285329-Abstract.html), NeurIPS 2019 | 공식 abstract | 유익한 intervention·expert query와 정보 증가의 역효과는 기존 계보. 이번에 본문·code를 재검증한 것은 아님 |
| F10 | [Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html), ICLR 2024 | [arXiv v1 §3–4](https://arxiv.org/html/2306.01157v1) | 유한 표본 불확실성과 구조적 hidden-confounding 불확실성 분리의 선행. 확인 본문은 초기 version이므로 최종 구현/증명과 동일하다고 단정 안 함 |
| F11 | [Mechanistic Interpretability for Steering Vision-Language-Action Models](https://proceedings.mlr.press/v305/haon25a.html), CoRL 2025 | 공식 abstract | VLA activation steering의 관련 계보. 내부 activation의 인과 효과를 환경 action effect 식별과 혼동하지 않음 |
| F12 | [Causal Flow Q-Learning for Robust Offline Reinforcement Learning](https://proceedings.mlr.press/v306/li26ja.html), ICML 2026 | [v1 §2–4, App B](https://arxiv.org/html/2602.02847v1); code | 연속 flow 정책·pixel manipulation 직접 선행. Q ensemble의 실용적 worst-case 근사와 전체 compatible-world 식별 집합은 다름; language VLA 평가로 확대 안 함 |
| F13 | [Scalable Causal Imitation Learning](https://rlj.cs.umass.edu/2026/papers/Paper47.html), RLJ/RLC 2026 **pre-proceedings**, page TBD | [v1 §2·3.2, App G](https://arxiv.org/html/2607.17003v1); code | 알려진 causal graph·bounded extended-parent history에 따른 adjustment. Learner interaction을 쓰는 causal SQIL/IQ-Learn과 순수 offline BC를 구별 |
| F14 | [Civil: causal and intuitive visual imitation learning](https://link.springer.com/article/10.1007/s10514-026-10266-3), Autonomous Robots 2026 | Publisher §1·6–7; code | Marker/language를 학습용 feature supervision으로 사용하고 inference에는 요구하지 않음. 동일 수집 시간 비교와 부정확한 human cue 분석도 이미 존재 |

Registry의 VLA·IL foundation은 비교 배경이며 위 14편의 직접 identity match는 0건이다. 이번 외부 source ledger는 paper registry 등록이나 정독 완료가 아니다. B4MRL은 발견 페이지와 primary PDF의 venue 표기가 맞지 않아 이 검토의 공식 게재 근거에서 제외했다. Adaptive IV experimentation·initial-state intervention·관련 causal data augmentation 계보는 신규 방법 채택 전에 추가 대조해야 하며, 이번에 검토 완료한 것으로 세지 않았다.

## 3. 먼저 분리해야 하는 원인과 식별 대상

아래는 문헌 비교를 바탕으로 정한 로컬 검토 계약이다.

| 구분 | 확인할 내용 | 잘못된 대체 증거 |
|---|---|---|
| Hidden confounding | 무엇의 효과를 식별하는지 먼저 정의하고, 관측에 조건부로 action과 outcome의 공통 원인이 빠졌는지 확인 | 부분 관측·배경 shortcut·action copying을 모두 confounder로 부르기 |
| Action support | 평가 정책이 요구하는 행동이 해당 상태/숨은 조건에서 존재하는지; 연속 행동이면 어떤 overlap 가정인지 | 전체 로그에 두 action이 등장하거나 embedding density가 높은 것 |
| Finite-sample uncertainty | 같은 생성 과정에서 더 많은 표본으로 줄어드는 오차와 model misspecification | Ensemble disagreement를 모든 구조적 미식별의 calibrated interval로 해석 |
| Train-only cue | 행동 전 확보 가능한 cue를 학습에만 사용; policy input·test sensor 고정 | Future outcome label 또는 inference sensor 추가의 이득을 deconfounding이라 해석 |
| History / IV | Episode 경계·noise horizon·instrument validity/relevance를 명시 | Memory를 늘리면 자동으로 충분한 관측/유효한 IV가 된다고 가정 |
| Physical intervention | 생성 모형의 action/context 개입과 그 비용·안전 조건 | Token 삭제·activation steering을 환경의 `do(A)` 데이터로 간주 |

F02의 latent coverage, F05의 IV 가정, F13의 known graph는 같은 로그의 관측 빈도만으로 일반적으로 입증할 수 없다. F03의 support 실패와 F04의 추가 탐색은 이미 알려진 한계/해법이다. **관측 action 빈도를 맞추자 성능 차이가 사라졌다는 이유만으로 hidden confounding을 기각하는 기존 GAP-CAUSAL 문구를 수정했다.** 생성 과정과 숨은 조건별 support를 통제한 비교에서만 해당 경쟁 설명을 판정한다.

## 4. 수작업 식별 반례 — 두 행동이 모두 있어도 부족하다

아래는 식별/coverage 차이를 설명하기 위한 자체 구성 예시다. 새 정리나 실행된 실험이 아니다. `U~Bernoulli(1/2)`, 시연 행동 `A=U`, outcome `Y∈[0,1]`로 둔다.

| U | 기록 행동 A | 세계 +의 Y(0) | 세계 +의 Y(1) | 세계 −의 Y(0) | 세계 −의 Y(1) |
|---|---|---|---|---|---|
| 0 | 0 | 0.4 | 0.8 | 0.4 | 0.0 |
| 1 | 1 | 0.2 | 0.6 | 1.0 | 0.6 |

두 세계의 로그는 모두 절반씩 `(A=0,Y=0.4)`, `(A=1,Y=0.6)`이다. 그러나 고정 행동 정책의 기대값은 세계 +에서 `J(0)=0.3, J(1)=0.7`, 세계 −에서 `J(0)=0.7, J(1)=0.3`으로 역전된다. 기존 로그에 U를 뒤늦게 붙여도 반대 행동을 취한 cell이 없으므로 추가 구조 없이 point identification은 안 된다. 해당 cell의 통제된 행동 관측은 두 세계를 구분할 수 있다.

이 예시는 **hidden information과 conditional support 부재가 함께 있는 경우**다. Full support에서도 같은 현상이 발생한다는 증명이나 실제 VLA 현상의 증거로 쓰지 않는다. Cue 추가만으로 해결되는 경우와 그렇지 않은 경우를 비교해야 하는 이유를 보여준다.

## 5. 공개 코드의 가정과 경계

9개 repository revision에서 source/doc 35개를 임시 열람 대상으로 확보했다. README 9개와 핵심 코드 14개의 지정 구간을 확인했으며 나머지 12개는 경로·symbol 탐색용 context다. 모든 파일의 hash와 확인 깊이를 ledger에 기록했다. Dependencies·데이터·weight는 설치/다운로드하지 않았고 외부 코드를 import/실행하지 않았다. Revision은 검토 시점의 공개 코드이며 논문의 실제 실험 commit을 뜻하지 않는다.

| Repository / 고정 commit 앞 12자 | 확인한 계약·후속 주의점 |
|---|---|
| [off-policy](https://github.com/hetankevin/off-policy/tree/ed813bf0dd2e6504677cf0056ffd3acbf62f9000) / `ed813bf0dd2e6` | `confound_pi_R`와 `getPb_spsa`가 behavior와 latent mixture를 따로 다룬다. 제공 notebook/data pointer를 native robot 데이터로 해석하지 않음 |
| [Two-way-Deconfounder](https://github.com/fsmiu/Two-way-Deconfounder/tree/d714206e64f63e9fbacaa8a0abd37f68916c809d) / `d714206e64f6` | Dataset interface에 `cu,ct,s1,xa,ya,rs`가 있다. 인자 이름/shape만으로 실제 데이터의 hidden confounder가 관측됐다고 주장하지 않음 |
| [Causal-DQN](https://github.com/CausalAILab/Confounding-Robust-Deep-Reinforcement-Learning/tree/c9a4dfe9d471e5422f493268e106e1a174f1e72d) / `c9a4dfe9d471` | `student/dqn.py:203–239`는 teacher/random/student 분기와 `env.step`으로 replay를 채움. 기존 고정 offline 파일만 재생하는 실행 계약과 다름 |
| [Reward shaping](https://github.com/CausalAILab/Automatic-Reward-Shaping-From-Confounded-Offline-Data/tree/67f4250101b981cfaaba3a5b1210cc6a49bada83) / `67f4250101b9` | `q_ucb.py:61–85`는 `env.do(action)` online loop. Potential 생성과 실제 탐색 budget을 분리해야 함 |
| [Confounded-IL](https://github.com/shaodaqian/Confounded-IL/tree/ff0ce38c07ce8d0d959646a9a92a4de9734b0c15) / `ff0ce38c07ce` | README는 이전 workshop/title을 가리키고 명시한 `mujoco_main.py`는 tree에 없음. 존재하는 `gym_main.py:58–64`는 trajectory를 concatenate, `learner.py:368–410`은 그 배열을 shift한 뒤 row random split. Episode 경계·cross-fit 독립성 audit가 필요하며 최종 논문 재현 실패로 단정하지 않음 |
| [CFQL](https://github.com/CausalAILab/Causal-Flow-Q-Learning-for-Robust-Offline-Reinforcement-Learning/tree/1895eea5da95136652215b2b2f8367cb707355f8) / `1895eea5da95` | `en_cfd_fql.py:53–100`은 discriminator 가중치로 ensemble mean/min을 혼합하고 online에서 해제. 유한 network ensemble이 모든 인과적으로 가능한 세계를 열거한다는 증거는 아님 |
| [Scalable CIL](https://github.com/CausalAILab/Scalable-Causal-Imitation-Learning/tree/2665d73bc9c9d9c49aadd59a5f5974762a65fdc7) / `2665d73bc9c9` | `find_sequential_pi_backdoor`가 graph를 입력으로 받고 rollout은 `env.do` 사용. Graph 추정·learner interaction 비용을 공짜로 두지 않음 |
| [CofactVLA](https://github.com/zhangy0822/CofactVLA/tree/f438fa6661c541898fc87397692c8d9fec8d2c4b) / `f438fa6661c5` | `processor_pi05.py:75–81`은 task와 discretized state를 같은 text prompt에 넣고 `modeling_pi05.py:796–807,957–964`는 counterfactual branch의 token/mask 전체를 0으로 만듦. 따라서 instruction-only masking 비교는 state를 보존해야 함 |
| [CIVIL](https://github.com/CIVIL2025/Implementation/tree/785be3450b39232364fb16caf84ceeccae05dfb3) / `785be3450b39` | `civil_model.py:60–79,117–128,153–195`의 marker supervision·mask feature matching·기본 unmasked inference를 확인. 2025 공개 commit을 2026 journal의 모든 추가 평가 구현으로 간주하지 않음 |

CIVIL의 사용자 연구는 10명, 수집 round는 5분이며, 실제 정책 비교는 집계한 자료에서 BC 15개/CIVIL 13개 시연을 뽑아 약 7분에 해당하는 데이터로 학습한다. 따라서 “각 참여자의 5분짜리 개별 정책 비교”라고 기록하면 틀리다. 이 결과는 추가 cue의 일반적 가치가 전혀 연구되지 않았다는 주장을 반박하지만, 모든 task/hidden-state 조건의 최적 수집 결정을 제공하지는 않는다. [Publisher §7](https://link.springer.com/article/10.1007/s10514-026-10266-3).

## 6. 조건부 후보의 비교 계약 초안

이는 구현 명세 초안이며 executable manifest는 아니다.

| 항목 | 고정할 내용 |
|---|---|
| Primary claim | 추가 cue와 행동 수집의 이득 순위를 결정하는 사전 관측 가능한 조건이 단순 baseline을 넘어 held-out 정책 선택 오류를 예측하는가 |
| Estimand | 고정 배포 정보 집합에서 선택된 정책의 native 성공/return; 수집 방식별 이득 차이. 전체 최적 정책을 모르면 상대 baseline 차이를 optimal regret라고 부르지 않음 |
| Policy input / action | 실제 checkpoint·camera/proprio/language/history·action 단위·normalizer·controller·chunk 고정. Cue는 train-only인지 inference-visible인지 분리 |
| Decision timing | 수집 전 calibration 자료로 allocation 결정. 행동 후 outcome·test 성능·oracle U로 배치 선택 금지 |
| Minimal arms | 원자료, cue-only, support-only, 둘 모두. 같은 총 human time에서 random/targeted 수집과 비교; factorial 진단에서는 표본 수와 계산도 별도 고정 |
| Strong baselines | BC·history BC, 관측/시간 정렬 수정, 단순 task/coverage balancing, cue-supervised representation(CIVIL 계열), uncertainty/expected-cost allocation. 식별 가정이 맞는 경우에만 DML-IL/TWD/robust causal RL 비교 |
| VLA-specific controls | Instruction-only/state-only/full-text masking, proprio 보존, 추가 branch의 inference 계산 비용, 단순 dropout/augmentation. CofactVLA의 효과를 hidden U 복구로 자동 해석하지 않음 |
| Metrics / splits | Native 성공·정책 순위 오류·baseline 대비 손실; interval validity/width는 별도. Episode·demonstrator·task/context holdout, whole-episode cross-fitting, 수집 분/개입 수/compute 각각 기록 |
| Oracle | Generator의 U와 true action effect는 평가·상한 진단에만 사용. 현실 자료의 oracle 부재를 추정값으로 덮지 않음 |

**기각/축소 규칙:** (1) 동일 정보/예산의 단순 대안이 설명하면 일반 방법 NO-GO, (2) 관측 정렬·proprio 복원만으로 해결되면 시스템 진단으로 축소, (3) IV/graph 가정의 위반을 판정할 근거가 없으면 causal 식별 claim 중단, (4) cue를 추가해도 support가 없으면 cue만으로 해결한다는 주장 기각, (5) valid bound가 좁아져도 선택/성공이 안 바뀌면 실용 주장 보류, (6) oracle·future-label·test leakage에 의존하면 해당 비교 무효, (7) 기존 CIVIL/Delphic/CFQL 등과 다른 예측 없이 recipe 비교만 남으면 독립 주제로 채택하지 않는다.

## 7. Buildup 단계와 다음 TODO

| 단계 | 이번에 확인한 것 | 남은 경계 |
|---|---|---|
| 0 공백 탐색 | 숨은 정보/coverage/불확실성 종류를 분리 | 현실 VLA의 결정적 사례 미확보 |
| 1 문제 정의 | 고정 배포 정보와 budget 하의 정책 선택 | Benchmark/task/checkpoint 미선정 |
| 2 문헌 집합 | 14편 status와 버전 구분 | Targeted review이며 전수 조사 아님 |
| 3 가정·interface 비교 | 지정 본문 12편, code 계약 대조 | 최종 version/실험 commit의 완전한 일치 미검증 |
| 4 질문 도출 | 고정 정보/비용에서 cue와 행동 수집의 조건부 가치 | 새로운 조건 예측 자체는 미확정 |
| 5 직접 선행 비교 | CIVIL·DML-IL·CFQL·CofactVLA와 겹치는 주장 제외 | 추가 active allocation 계보 확인 필요 |
| 6 주장–증거 연결 | 표적 수집/history/정렬의 경쟁 설명, fairness/reject 규칙 | 실행 가능한 데이터·split·평가 묶음 없음 |
| 7 저비용 검사 | 수작업 식별 반례·공개 interface 정적 확인 | Docker runtime·base competence·정책 효과 모두 미실행 |
| 8 외부 피드백·판정 | 일반 주장 NO-GO, 진단 REVISE/HOLD | 실제 외부 연구자 피드백 없음 |

다음은 **GAP-CF2: 자료 충분성 심사**다. DROID/Bridge 계열/OXE와 CIVIL의 공개 수집 protocol·schema에서 demonstrator가 본 정보, policy observation, action 시각/의미, cue의 생성 시점, episode join, 비용·평가 경로를 조사한다. 공개 자료가 식별에 불충분하면 그 사실을 명시하고 이 branch를 문헌 진단으로 종료한다. 자료가 충분해도 단순 cue-versus-demo 비교를 넘는 예측을 정하기 전 learned method를 구현하지 않는다. Raw dataset·weight 다운로드나 실험은 다음 TODO에 포함하지 않는다.

## 8. 저장소 검증

- 변경 전 audit: 1,037편·5,185개 표준 노트, 오류 0·경고 0.
- 변경 후 `py_compile`, reading-tier 생성, repository audit, `git diff --check` 통과. 1,037편·CORE 47/NEXT 275·정독 tracker 322·history 47·표준 노트 5,185개 유지. Markdown 5,336개·링크 10,159개 검사, 오류 0·경고 0.
- 기존 dirty/untracked 356개 중 관련 문서 7개만 갱신하고 나머지 349개 hash를 보존했다. Manifest·registry meta·tier·active/history tracker의 hash도 변경 전과 같다. 신규 파일은 이 report와 source ledger 2개다.
- 임시 public source 35개는 hash 확인 후 metadata/snapshot과 함께 정리했다. 기존 논문·PDF·실험 artifact 삭제는 없다. 상세 검증 기록은 ledger에 둔다.
