# 접촉 관계 탐색

2026-11-18: 직접 선행의 정식 paper-note와 publication 경계는 [REG-R17 등록](../../../update/REGISTRY.md#reg-r18)으로 연결했다. 아래 연구 판단·실행 준비 상태는 유지한다.

Updated: 2026-11-17 KST. **N1/N2·P0 실행 준비 완료 / 좁은 탐색 CONTINUE, native 검증 대기.** 근거 성숙도는 `CURATION-HYPOTHESIS`다. 독립 신규성·정책 효과·실제 외부 피드백은 미확인이다. [재현 방법·공개 source 검사](../재현%20방법/README.md) · [단일 근거 원장](../../../sources/new_field_scout_2026-11-17.json)의 `relation_n1`/`relation_n2`/`relation_p0_preparation` · [선정 이력](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/NEW_FIELD_SCOUT_2026-11-17.md#relation-exploration) · [TODO](../../../../TODO.md).

## 지금의 판단

**계속 볼 가치가 있으나, ‘접촉을 보존하는 상관 잡음’만으로는 새 방법이 아니다.** Lattice는 상태에 따른 행동 간 공분산을 학습하고, RL-SCT는 작업 단계별 제약 전환까지 제공한다. 따라서 남길 질문은 **같은 VLA의 시각·지시 표현으로 현재 필요한 양팔 결합 정도를 학습하는 구조가 generic covariance와 수작업 단계 규칙보다 적은 상호작용으로 유용한 경험을 얻는가**다. 기존 기법을 VLA에 붙였다는 사실을 기여로 세지 않는다.

범위도 줄였다. 처음부터 모든 손–물체 관계와 물체 pose/Jacobian을 영상으로 추정하는 graph를 만들지 않는다. 첫 방법은 **두 end-effector의 상대 운동을 결합할지 완화할지 학습하는 하나의 연속 weight**다. 관계는 실제 접촉 상태의 정답 label이 아니라 탐색을 조절하는 변수이며, 물리적으로 해석 가능한지 별도로 확인한다. 성능이 있어도 weight가 접촉 확률이라고 자동 해석하지 않는다.

## 한 페이지 논문 이야기 — 결과 칸은 미확인

- **문제:** 두 팔이 같은 물체를 다루는 동안 독립적인 탐색이 접촉을 깨뜨려 유효한 학습 경험을 줄일 수 있다. 한 손을 놓거나 서로 다른 물체를 움직일 때는 결합이 방해될 수도 있다. 이 실패의 실제 빈도와 비용은 아직 측정하지 않았다.
- **방법 기여 가설:** 로봇 기구학으로 정한 상대 운동의 민감도에, VLA 표현에서 학습한 task/state별 결합 weight를 적용해 **확률적 actor의 탐색 공분산**을 만든다. 평균 action을 생성하는 action expert와 weight head를 같은 RL 목적함수로 갱신한다.
- **예상 새 지식:** 단순 시간 상관이나 잡음 크기 조절로 설명되지 않는, 관계 조건부 탐색의 sample-efficiency 이득과 그 적용 조건. 추가 perception 모델·수작업 단계 라벨 없이 가능한지 확인한다.
- **필요한 결과:** 같은 물리 시간·상호작용·데이터 예산에서 학습 곡선 개선, 관계를 해제하는 단계의 방해 감소, generic covariance·수작업 전환 대비 추가 이득. 현재 모두 미측정이다.
- **가장 큰 위험:** 일반 covariance 또는 gripper/phase 규칙으로 충분할 수 있다. 또 접촉 제약보다 기본 grasp 능력 부족이 병목일 수 있다. 각각 방법 수정과 base competence 확보의 문제로 구별한다.

## 직접 선행의 본문·구현 대조

| 선행 | 실제 확인한 범위와 이미 해결된 것 | 남는 비교 / 확보하지 못한 것 |
|---|---|---|
| [StructRL: Structured Action-Space Exploration…](https://arxiv.org/html/2608.15139v1), 2026 preprint | §4.2–4.3·Appendix C/D. 실행 action에 학습 scale·시간 AR(1) 잡음을 주며 last-step replay 사용. 저자 project HTML도 확인 | 공간적 관계 bias를 추가할 이유를 검증해야 함. Project에는 코드 링크를 식별하지 못함. 검색에서 나오는 `amazon-science/StructRL`은 **다른 논문**인 2609.36352이며 이 방법의 코드로 쓰지 않음 |
| [Lattice, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b0ca717599b7ba84d5e4f4c8b1ef6657-Abstract-Conference.html) | §4와 [공개 distribution 코드](https://github.com/amathislab/lattice/blob/846d02fa993b9b80ce5ecb806463e0a05711bad3/src/models/distributions.py#L257). Latent noise가 full covariance를 만들고 state dependence·시간 상관·log-probability를 다룸 | **행동 간 상관을 RL로 학습하는 것 자체는 신규성이 아님.** 같은 VLA feature를 받는 Lattice형/Cholesky covariance를 강한 비교군으로 둠. 원 benchmark에서 VLA/양팔 관계의 효과까지 검증한 것으로 확대하지 않음 |
| [RL-SCT, Autonomous Robots 2024](https://link.springer.com/article/10.1007/s10514-024-10164-6) | §3–4. Input mapping·active constraint뿐 아니라 FSM과 기하 임계값에 따른 **phase별 제약 전환**을 명시 | R2의 ‘고정 template 대 관계 전환’ 구도를 교정. 수작업 전환도 baseline이다. 독립 공개 구현은 이번 검색에서 식별하지 못했으므로 미공개라고 단정하지 않음 |
| [SOE](https://arxiv.org/html/2509.19292v1), 2025 arXiv | III–IV 및 [실제 DPExt 경로](https://github.com/EricJin2002/SOE/blob/9b5be5a7be16c39e8aa5314aad4bff29c6c81261/src/policy/dp_ext.py#L118), transport config, multi-round script. Latent VIB 탐색 후 성공 rollout을 원 시연과 합쳐 모방 갱신 | PPO/VLA policy-gradient baseline과 동일한 학습이라고 쓰지 않음. 성공 데이터 재학습도 별도 대안. 저자 repo는 ICRA 2026을 표방하지만 공식 proceedings acceptance를 확인하지 못했으므로 venue 확정 보류 |
| [Extracting Bimanual Synergies, IROS 2017](https://research.vu.nl/en/publications/extracting-bimanual-synergies-with-reinforcement-learning/) | 연구기관 서지와 저자 연구실 설명, 공식 IROS digest. Trial-and-error로 양팔 synergy를 학습하는 선행 | ‘양팔 결합을 RL로 학습’도 새 주장이 아님. 원 PDF 전체는 웹 도구에서 열리지 않아 상세 formulation은 미확인. 원문 미확인을 선행 부재로 사용하지 않음 |
| [Constrained Bimanual Planning, ICRA 2024](https://arxiv.org/abs/2309.08770) / [GAP, CVPR 2026](https://github.com/Chongyang-99/GAP) | R2의 상대 pose 제약·3D/action 공동 예측 비교를 유지 | 기하 제약이나 3D 표현을 새 기여로 주장하지 않음. 이번 방법은 일반 6D pose 추정기·world model 신설을 요구하지 않음 |

SOE source에서 처음 발견한 `mi_dp_v2.py`를 paper 구현으로 추정하지 않았다. 실제 `transport_soe.json`은 `DPExt`를 선택하고, `dp_ext.py`의 detached readout·Gaussian latent·별도 loss/backward 경로를 확인했다. 실행은 하지 않았다. Source scope와 license 확인 범위는 원장과 재현 문서에 있다.

## 최소 사례와 실패할 수 있는 사례

| 역할 | 선택한 공개 task | 이 task로 확인할 수 없는 것 |
|---|---|---|
| 결합이 유용할 수 있는 사례 | RoboTwin `lift_pot`: 양팔로 냄비를 들어 올리며 높이·자세·양쪽 TCP와 annotation point 거리를 평가 | **배치·한 손 해제가 없다.** 거리 조건은 실제 접촉 force를 증명하지 않음 |
| 관계 완화가 필요한 사례 | `handover_block`: script에 받는 손 grasp→주는 손 open→물러남→배치가 있음 | 기본 success는 최종 위치와 오른쪽 gripper open이며, 실제 handover/contact 순서를 강제하지 않음. 별도 evaluator event를 기록해야 함 |
| 불필요한 결합의 반례 | `pick_dual_bottles`: 양손이 서로 다른 병을 집고 이동 | 단일 물체 task와 물체/난이도가 달라 **task 간 차이만으로 인과효과를 주장할 수 없음** |

R2의 ‘상자 공동 운반→배치→한 손 해제’를 이미 확보한 공개 task라고 쓰지 않는다. 초기에는 위 세 task로 현상과 기본 능력을 확인한다. 동일 scene에서 지시만 바꾼 hold/release 조건은 아직 구현·시연이 없으며, 그 비교 전에는 **언어 이해 향상**을 주장하지 않는다.

Actor는 RGB·지시·명령 상태와 실제 관절 측정을 사용한다. Object ID·정답 pose·contact pair·script phase·미래 성공은 evaluator/oracle에만 둔다. 중도 실패를 제외하지 않고 full-start 결과를 주 결과로 삼는다. 양손 grasp 이후 상태의 진단은 별도이며, 그 구간까지 도달하지 못한 rollout을 성공률 분모에서 지우지 않는다.

## 확률적 actor 설계 — P0 구현의 논리 계약

이 절의 식은 **제안 설계**이며 기존 공분산/RL 수학을 새 정리로 주장하지 않는다.

1. 입력 `o`는 세 RGB·지시·checkpoint가 사용하는 14D 상태, `q`는 별도로 읽은 실제 12개 arm joint 위치다. `q`는 모든 learned baseline에도 제공한다. 기존 14D 상태가 drive target을 담는 경로를 확인했으므로 그것을 실제 `q`로 대체했다고 가정하지 않는다.
2. 고정 prior의 flow 초기 noise `ξ`를 샘플하고 `μθ(o,ξ)`를 ODE로 계산한다. 같은 초기 noise를 저장해 재채점한다. 우선 **전체 ODE 재계산/gradient**를 기준 설계로 두고 last-step surrogate를 무심코 정확한 policy gradient로 부르지 않는다. 계산 부담은 별도 측정한다.
3. `J_rel(q)`는 두 TCP의 상대 pose 변화에 대한 **12개 joint의 기구학적 민감도**다. 미지 물체의 동역학 Jacobian이 아니다. Translation/rotation 단위와 normalizer·joint sign flip을 반영한 `J̃ = W J_rel D`를 쓴다. N2에서 relative body-frame·quantile inverse의 `D`·진단용 `W`를 [명세](../재현%20방법/README.md#n2-interface)했다. 실제 URDF/FK 수치 대조는 미실행이며, 명령 감도를 접촉 중 실제 운동 감도로 간주하지 않는다.
4. 공유 action-expert feature로 `λ = λ_max sigmoid(fφ(hθ,q))`를 예측한다. `M = I₁₂ + λ J̃ᵀJ̃`, `C = (1−η)·12 M⁻¹ / tr(M⁻¹) + ηI₁₂`, `Σ_arm = σ²C`로 둔다. `0<η<1`, `λ_max` 유한, `σ>0`이며 수치는 dev calibration에서 고정한다. `M`과 `C`는 양의 정부호, `tr(C)=12`이므로 λ가 총 분산을 0으로 줄이는 해는 막는다. 다만 **정규화 좌표에서의 같은 분산이 같은 물리 움직임을 보장하지는 않는다.**
5. Gripper 두 축은 동일한 독립 연속 잡음으로 두고 모든 군에 같은 크기/변환을 사용한다. 총 14D Gaussian을 `[L6,Lgrip,R6,Rgrip]`으로 배치한다. 관계 head로 gripper 탐색량까지 줄이지 않는다. Arm 12D에만 관계를 넣어 처음부터 모든 상관구조를 학습하는 부담을 줄인다.
6. `u ∼ N(μθ(o,ξ), Σφ(o,q,ξ))`를 **정규화된 raw action**으로 저장한 뒤 checkpoint의 inverse normalization·delta→absolute·gripper 변환과 공통 controller에 전달한다. `log p(u|o,q,ξ)`는 Cholesky 분해로 계산한다. `p(ξ)`는 parameter-independent라 ratio에서 소거된다. 이는 `(ξ,u)`를 포함한 augmented action 정책의 likelihood이며, **ξ를 적분한 물리 action marginal density가 아니다.**
7. Clipping/비선형 gripper 변환 뒤 action을 원 Gaussian에 다시 넣어 log-probability를 계산하지 않는다. Raw `u`와 최종 command를 모두 기록하고 deterministic downstream mapping을 환경 interface로 취급한다. 물리 좌표 density를 주장하려면 별도 Jacobian/경계 확률 처리가 필요하다.

초기 제어는 checkpoint의 full prediction horizon을 보존하고 **실행 prefix K=1**로 모든 군을 맞춰 재관측한다. 시간 상관은 이 첫 비교에서 제거해 공간적 결합만 묻는다. 이후 K>1 비교를 추가할 때 chunk covariance·중간 종료 mask·관계 전환 시점까지 다시 정의한다. Network horizon과 실제 실행 길이를 혼동하지 않는다.

RL은 sparse task success를 사용한 PPO를 기준으로, action expert와 covariance head를 함께 갱신한다. Vision-language backbone은 우선 고정하고 critic은 동일한 관측을 사용하되 공유 actor feature로의 value gradient를 막는다. N2에서 feature는 마지막 Euler vector-field 평가의 첫 action-token hidden state로 정했다. 학습 module whitelist·raw-sample 고정·전체 ODE backward 경로를 P0 adapter에 작성했으나 실제 gradient 검사는 미실행이다. PPO trainer/critic은 아직 구현하지 않았다. 단일 정책 배포·action-expert 공동 갱신·전체 backbone 공동 갱신을 구별한다.

## 최소 비교와 판단 규칙

| 비교군 | 같은 조건으로 맞출 것 | 주장을 바꾸는 결과 |
|---|---|---|
| 원 SFT, diagonal endpoint-noise RL | 같은 base, task seed, controller, executed prefix, reward. SFT와 RL의 수집비 차이 별도 보고 | Grasp 자체가 거의 안 되면 관계 학습 효과를 평가할 수 없으므로 base/data 문제로 수정 |
| Lattice형 또는 generic full covariance | 동일 RGB/지시/q·action expert·training budget. Head parameter 수와 계산량 보고 | Generic covariance로 설명되면 explicit relation bias의 독립 기여가 약함 |
| 고정 관계, gripper/TCP 근접도에 따른 수작업 전환 | 동일 관측만 사용. 정답 object contact를 읽는 rule은 oracle로 분리 | 수작업 전환으로 충분하면 관계 head를 추가할 이유가 줄어듦 |
| 제안 λ와 vision 제거·task-ID/phase-rule·shuffled geometry | 동일 평균 정책 갱신, 실제 물리 탐색량과 contact 유지율 함께 측정 | 언어/영상 제거에도 같으면 그 modality 기여를 주장하지 않음. 단순 task lookup이면 범위 축소 |
| 성공 데이터 선택 후 BC | 같은 원 시연과 총 rollout 예산. 성공이 없던 수집도 비용에 포함 | 이득이 좋은 데이터 수집/재모방만으로 설명되면 RL 고유 이점은 미지지. SOE 자체를 PPO로 바꿔 원 논문 baseline이라고 부르지 않음 |

주 지표는 **누적 환경 상호작용 및 simulated physical time 대비 성공률 AUC**, 고정 예산 후 성공률, reset/시연/추가 annotation/학습·추론 시간이다. RoboTwin의 각 target은 TOPP와 물리 substeps를 거쳐 실행되므로 한 target=고정 시간이라고 놓지 않는다. Joint noise energy만 맞추지 말고 TCP 이동·물체 이동·접촉 이탈도 보조 기록한다. 더 작은 잡음 sweep은 dev에서만 선택하며 held-out에서 유리한 noise 값을 사후 선택하지 않는다.

작은 pilot은 3 task의 공개 train/eval seed pool을 분리하고 dev에만 수치/허용치를 정한다. 학습 pilot의 seed 수·episode 상한은 native IO와 base competence를 확인한 뒤 비용에 맞춰 고정한다. 현재 확증용 통계적 power를 확보했다고 표시하지 않는다. 평균 차이만 아니라 seed/episode 변동과 신뢰구간을 보고한다.

**계속/수정 기준:** 관계를 유지하는 구간과 풀어야 하는 구간에서 예측한 차이가 나타나고 강한 단순 대안보다 이득이 남으면 방법 개발을 확대한다. Fixed rule/generic covariance가 같거나 더 좋으면 더 복잡한 head를 억지로 붙이지 않는다. 기본 정책·normalizer·contact evaluator가 잘못되면 먼저 실행 계약을 수정하며 가설 반증으로 세지 않는다.

## 비실험 buildup 완료 범위와 남은 것

가이드의 문제/독자·가까운 선행·단순 대안·한 페이지 이야기·비교 설계·실행 부담 검토를 수행했다. 그 결과 초기 질문을 위와 같이 줄였다. 외부 연구자의 실제 피드백은 받지 않았으며 내부 논리 검토로만 표시한다. 후보 탐색을 중단해야 한다는 뜻은 아니다.

- **완료:** 직접 선행 formulation/식별 가능한 code 대조, 세 공개 task와 성공 조건 확인, actor 입력·공분산·likelihood의 설계, 비교군/해석 기준, source/checkpoint/asset metadata 고정. N2는 loader 선택·입출력 순서·contact witness·시간/로그·최소 실행 상한과 실패 후 분기까지 완료했다. P0-PREP에서 portable Docker recipe·launcher·actor/simulator adapter·제어 검사 코드를 작성하고 정적 컴파일했다.
- **미완료:** 단일 VLA의 task별 기본 능력, 작성한 head/gradient·실제 qpos/FK/contact 코드의 native 검증, checkpoint 구조·의미 호환, evaluator의 전체 contact event 구현/교정, 학습 trainer·GPU 시간/성능.
- **중요한 실행 발견:** 공개 π₀.₅ multitask 후보는 있으나 RLinf의 adjust_bottle recipe에 바로 교체할 수 있다고 확인하지 못했다. Horizon·normalizer asset ID·학습 fork가 다르다. 자세한 차이는 재현 문서에 통합했다.

<a id="n2-result"></a>
## N2 결과가 연구 판단에 주는 의미

**방법 탐색은 계속하되, 다음 판단은 최소 구현에서 얻는다.** 원 Motus 학습 fork는 확인되지 않아 공개 OpenPI로 재구성한 baseline을 먼저 strict load/IO 검증한다. 원 논문 재현이라는 주장은 하지 않는다. 구조 호환 실패 또는 후속 기본 능력 부족이면 모든 비교군의 공통 SFT/data 확보가 필요해질 수 있다. Source 불확실성만으로 지금 대규모 SFT를 시작할 이유는 없다.

두 실행상 혼동도 제거했다. π₀.₅ state는 정규화 후 언어 토큰에 들어가므로 actual qpos로 임의 교체하지 않는다. 공개 `sample_actions`의 no-grad/detach 경로는 학습용으로 다시 구현해야 한다. RoboTwin RL 경로에는 정지 명령의 작은 random perturbation과 긴 TOPP 궤적의 downsampling이 있으므로, actor 탐색 효과와 controller 효과를 분리하도록 공통 controller 변경·로그를 명세했다. 세부 근거는 [N2 source 계약](../재현%20방법/README.md#n2-interface)에 연결한다.

Contact witness는 native 성공과 별도이며 잘못된 API·없는 event를 실패 label로 만들지 않는다. 한 명령으로 전체 handover나 연구 가설을 검증할 수 없으므로 최초 P0는 loader/관측/명령/재채점, 선택적 backward1회·optimizer0회로 제한했다. 실제 성능과 generic covariance·phase-rule 대비 추가 이득이 미확인이라는 연구상 한계는 GPU 유무와 별개다.

<a id="p0-preparation-result"></a>
## P0 실행 준비 결과

Portable Docker recipe·strict loader·전체 Euler/공분산/재채점·선택적 gradient·FK/contact 기록·전역 physics budget을 구현했다. OpenPI와 simulator의 요구 package 차이는 같은 container 내 두 Python 환경으로 분리했다. 관측당 relative FK25회, 총75회로 N2의 모호한 계산 상한을 실행 전에 명확히 했으며 query/physics 상한은 유지했다. [구현 파일과 재개 명령](../재현%20방법/README.md#p0-preparation).

**이 준비는 기여의 근거를 추가한 실험 결과가 아니다.** 현재 새 launcher도 로컬 daemon 연결 실패(exit3)에서 차단됐다. Docker 제어 검사9개·image build·weight load·physics·gradient는 미실행이다. Native 호환 문제와 generic covariance/phase-rule 이후 남는 연구상 이득은 별개의 미해결 문제다. 작고 통제된 탐색을 진행할 가치는 유지하지만, 논문으로 발전시킬 가치가 입증된 상태는 아니다.

**다음 TODO는 GAP-RELATION-EXPLORE-P0 — NATIVE_RESOURCE_WAIT.** 호환 NVIDIA 컴퓨터의 로컬 Docker에서 최소 loader/IO/FK/contact/raw 재채점·선택적 backward를 검증한다. 이후에만 기본 능력·positive event 교정·비교 학습 pilot을 구체화한다. 현재는 구현된 P0의 검증 대기이며 검증된 학습 실행 환경으로 세지 않는다.
