# 계산 예산과 배포 목표를 고려한 다중 과제 VLA 강화학습

- Updated: 2026-11-09 KST
- 작업용 영문 제목: **Task Allocation for Multi-Task VLA Reinforcement Learning under Fixed Deployment Objectives and Compute Budgets**. 발표 논문·검증된 방법 이름이 아니다.
- 상태: **N2-R1 비실험 보완·P0 준비 완료 / 예비 분석 후보 / native P0 자원·구현 대기**. 11/09 Robotics 중심 요청에 따라 활성 검토 순서를 [접촉 적응 문헌 검토](../../../update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md#robotics-reorientation)로 전환했다. 과제 배분은 일반 다중 과제 RL에도 적용돼 로봇 고유성은 상대적으로 약하며, 아래 최초 선택 이유와 실행 자료는 보존한다. 새 알고리즘 기여·정책 효과는 미입증. 기존 9개 주제의 판정·투자 순위를 대체하지 않는다.
- [출처·코드 revision·검증 원장](./sources.json) · [Docker 재개·실제 확인 범위](../재현%20방법/README.md) · [최초 공백 조사](../../../update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md)

## 문제와 선택 이유

하나의 VLA에 여러 조작 과제를 RL로 학습시킬 때, 다음 경험을 어느 과제에서 모을지 결정해야 한다. 같은 episode 수라도 실제 환경 호출·정책 추론·학습 계산량은 다를 수 있다. 배포 시 필요한 과제별 중요도를 바꾸지 않으면서 주어진 자원 안에서 학습을 더 잘할 수 있는지 알아보려는 문제다.

직접적인 독자는 여러 과제를 하나의 정책으로 후학습시키는 로봇 연구자다. 답을 알면 더 비싼 curriculum을 구현할지, 단순 균등 배분을 사용할지, 먼저 계산 낭비를 줄일지의 결정이 바뀐다. 추론 시에는 같은 VLA가 직접 행동하며 상위 planner와 별도 RL controller를 연결할 필요가 없다.

| 비교 | 이 후보 | 물리 일반화 후보 |
|---|---|---|
| 남길 기여 | 과제 수집·목적 가중치·실제 비용의 효과를 분리하는 분석; 조건이 확인되면 방법 확장 | RL 학습 진행과 물리 강건성의 조건 분석 |
| 처음 바꿀 요소 | 공개 VLA trainer의 task sampler와 logging/weighting | 물리 perturbation과 평가의 타당성·학습 checkpoint |
| 검증 부담 | 여러 학습 run은 필요하나 동일 simulator/robot에서 시작 가능 | 접촉 파라미터의 물리 타당성·controller 동등성, 강한 sim-to-real 주장에는 실물 필요 |
| 현재 한계 | 일반 allocation은 이미 선행이 강함; 비용 차이·성능 차이 미측정 | 대규모 직접 선행 연구가 있고 새 분석의 차별성·실물 자원이 모두 미확인 |
| 선택 | 최초 scout 당시 우선 선택; 현재 예비 분석 | 예비 경로 유지 |

이 선택은 석사 기간의 검증 부담과 사용자의 단일 VLA+RL 선호를 고려한 판단이다. top-tier 채택 확률을 계산한 것이 아니며, 수집 배분 효과가 중요하지 않으면 복잡한 scheduler 개발을 중단한다.

## 가까운 선행과 이번에 확인한 차이

아래는 지정 본문 구간·공개 코드의 정적 검토다. 사용자 reading status나 논문 전체 정독을 의미하지 않는다. 원문 수식/구현을 그대로 실험에 쓰기 전에는 수치·배치 교정이 필요하다.

| 선행 | 이미 해결한 범위 | 이번 질문에 주는 제약 |
|---|---|---|
| [VIP, ICLR 2026 §5.2](https://arxiv.org/html/2602.01601v3#S5.SS2) | prompt별 rollout 수를 제한된 총량 안에서 gradient variance 기준으로 배분 | 일반 variance 기반 allocation은 신규 기여 아님. 가변 group size는 VLA GRPO의 추정량도 바꿀 수 있어 단순 이식 불가 |
| [DRATS, NeurIPS 2026 채택 프로그램](https://neurips.cc/virtual/2026/poster/152819), [§4·App. F.1](https://arxiv.org/html/2605.14350v1) | worst reference-return gap에 기반한 task sampling; 재수집과 objective reweighting도 직접 비교 | “둘을 처음 분리한다”는 주장 폐기. 배포 평균 목적과 minimax 목적을 혼동하지 말 것. 확인한 논문·저자 publication page에서는 공식 구현을 식별하지 못함 |
| [VLA-RL §3.5](https://arxiv.org/html/2505.18719v1)·공개 코드 | 성공률에 따른 curriculum과 VLA online RL | 공개 wrapper는 고정 task 안의 초기 상태를 선택한다. 과제 간 배분과 비교하려면 선택 단위를 명시해야 함 |
| [SimpleVLA-RL, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) | VLA trajectory sampling·병렬 rollout | 확인한 LIBERO 경로에서 환경 step은 active episode만, model forward는 전체 batch에 수행. Episode 길이만으로 GPU 비용을 추정하지 못함 |
| [RLinf-VLA, RSS 2026](https://roboticsproceedings.org/rss22/p089.html)·공개 코드 | VLA RL infrastructure, rendering/inference/training 자원 배분 | 고정 rollout 길이·종료 mask·reward filtering·loss reduction까지 확인해야 같은 budget/학습 목표 비교가 됨 |
| [DyGRO-VLA, ICML 2026](https://proceedings.mlr.press/v306/lin26af.html) | 다중 과제 표현과 RL residual 최적화 | 다중 과제 VLA 일반화 자체는 새 질문이 아님. 첫 비교에서는 표현/잔차 구조를 추가하지 않음 |
| [PCM, arXiv 2026](https://arxiv.org/abs/2605.16154) | outcome 정보를 이용한 chunk별 gradient 계산 배분 | 수집보다 학습 계산이 지배적인 설정이 이미 보고됨. Task allocation만으로 end-to-end 속도가 크게 개선된다고 전제하지 않음. Main-conference 논문으로 분류하지 않음 |
| [MPTS, Nature Communications 2026](https://doi.org/10.1038/s41467-026-74004-0) | 비싼 task difficulty 평가를 예측 모델로 줄이는 active task selection | “난이도 예측으로 평가 비용을 줄인다”도 일반적 신규성 없음 |
| [Active Experiment Selection, CoRL 2025](https://proceedings.mlr.press/v305/anwar25a.html) | robot policy **평가**의 cost-aware trial selection | 평가 오차를 줄이는 것과 정책을 학습해 성능을 높이는 것을 구별. C6 재개 경로로 바꾸지 않음 |

### 공개 코드에서 실제로 확인한 사항

1. **선택 단위와 논문–코드 차이.** VLA-RL `envs/wrappers.py:183–211`은 task별 state의 성공률과 0.5의 거리에 반비례하는 가중치를 사용한다. `envs/libero_env.py`는 미리 배정된 task의 초기 상태 sampler를 호출한다. 반면 논문 Eq. (4)의 `exp((0.5-s)/tau)`는 양의 tau에서 s에 대해 단조 감소하므로 “0.5 부근 선호”라는 설명과 같은 식이 아니다. 이는 해당 버전의 식/공개 코드 차이이며 원 실험의 실행 경로·오류율을 판정한 것이 아니다. 재현 baseline은 공개 구현 계보와 선택 단위를 정확히 표시한다. [고정 코드](https://github.com/GuanxingLu/vlarl/blob/212379e840376e07505cba398c0c587d96a13678/envs/wrappers.py#L183)
2. **유효 행동 수와 실제 계산량의 차이.** SimpleVLA-RL의 LIBERO loop는 active index로 환경 전송을 제한하지만 고정 max-step loop에서 전체 입력 batch로 inference한다. RLinf의 확인한 LIBERO config는 512 steps, 8-action chunk, auto-reset=false이며 worker는 고정 chunk 수를 돈다. `chunk_step`도 종료 시점 이후 슬롯을 학습 mask로 구별하면서 환경 step loop를 수행한다. 이는 정적 호출 구조의 사실이다. 실제 소요 시간·낭비 비율은 측정하지 않았다. [SimpleVLA-RL loop](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/rollout/rob_rollout.py#L769) · [RLinf chunk](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/envs/sim/libero/libero_env.py#L933)
3. **설정 이름만으로 loss를 판단하지 않음.** RLinf config의 `token-mean`만 보면 충분하지 않다. Embodied actor가 valid length를 전달하고 loss 함수가 `masked_mean_ratio`로 집계를 바꾸는 경로가 있다. 따라서 “긴 episode가 무조건 더 큰 가중치”라고 단정하지 않는다. 별도로 reward group filtering이 있고, group size=8의 GRPO는 같은 초기 조건에 묶인 trajectory를 사용한다. Native 식을 고정한 채 task-level weighting을 추적해야 한다. [actor](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/workers/actor/embodied_fsdp_actor_worker.py#L240) · [loss](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/algorithms/losses.py#L235)
4. **공개 과제 경로는 있지만 native 사례는 없음.** LIBERO-Goal 10개 task 이름과 RLinf의 `libero_goal_grpo_openvlaoft.yaml`을 확인했다. 기본 config는 ordered reset을 사용하므로 새 확률 sampler가 config 변경만으로 이미 구현돼 있다고 말할 수 없다. P0-PREP에서 단일 sampler와 actor-facing sidecar를 작성했지만, task/initial-state ID와 선택 확률을 실제 worker rollout→batch→loss 전체 경로로 전달하는 통합은 미구현이다. [task 목록](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/benchmark/libero_suite_task_map.py#L26)

## 좁힌 연구 질문과 가설

**주 질문:** 동일한 배포 task 분포와 기준 학습 목적을 유지했을 때, 적응형 과제 배분이 균등 배분보다 단일 VLA의 학습을 효율적으로 만드는 조건은 무엇인가? 특히 과제 평균 성공률이 초기 상태별 group 학습 신호를 잘못 요약할 때, 배분의 효과와 실제 환경·추론·학습 비용은 어떻게 달라지는가?

첫 기여 유형은 **평가·실증 분석**이다. 일반 curriculum이나 비용으로 나눈 score를 새 알고리즘으로 주장하지 않는다. 결과가 반복 가능한 조건을 드러내고 단순 배분이 부족할 때만 방법 기여를 검토한다.

| 경쟁 가설 | 구별할 관측 | 결과에 따른 판단 |
|---|---|---|
| 더 필요한 task에 경험을 배분하는 효과가 남는다 | 고정 배포 목표의 비교에서도 동일 실제 예산하 held-out 성능 향상 | 배분 예측 변수·조건 분석을 확장 |
| 목표 비중·gradient scale/variance·optimizer 영향이 섞여 있다 | 같은 q의 weight 변경과 같은 기대 목표의 재수집/재가중 결과를 대조 | Weight 보정 후 이득 소멸만으로 목표 변경을 원인으로 단정하지 않음. 아래 N2-R1 식별 경계 적용 |
| 이득의 대부분은 비용 분모·실행 방식의 차이다 | 유효 step 이득과 실제 호출·wall-time 이득이 어긋남 | 비용 측정/실행 조건을 기여로 검토. 단순 구현 수정이면 독립 논문으로 과장하지 않음 |
| 단순 배분이 충분하다 | Uniform·inverse-cost·기존 curriculum 사이에 재현되는 중요 차이가 없음 | 복잡한 allocator 중단, 기존 주제의 운영 기준으로 보존 |

<a id="n2-contract"></a>
## N2 비교 계약 — 2026-11-09

이번 단계는 공개 코드·metadata의 정적 대조와 수작업 논증이다. Native loss/gradient 실행·정책 학습은 하지 않았다. 첫 비교는 **RLinf + OpenVLA-OFT + LIBERO-Goal**로 좁혔고, 코드·checkpoint·초기 상태 파일 identity는 [재현 방법](../재현%20방법/README.md#n2-interface)과 [단일 원장](./sources.json)의 `n2`에 연결했다.

### 목표와 선택 단위

배포 지표는 10개 task에 균등한 `p_i=0.1`을 적용한 자율 성공률 `D(theta)=sum_i p_i SR_i(theta)`다. Task별·worst-task 성공은 보조 지표다. 처음에는 같은 robot·controller·성공 조건·512-step horizon을 유지한다. 다른 embodiment·navigation·새 task 일반화는 이 비교의 주장이 아니다.

선택 단위는 **task i → 해당 task의 RL-train 초기 상태 z → 같은 z에서 8개 rollout으로 구성된 group**이다. Task는 복원 추출하고 z는 train ID에서 균등 추출한다. Group별 실제 `q_i`를 뽑기 전에 저장하며 결과를 보고 해당 draw를 제거하거나 다시 뽑지 않는다. q는 학습 그래프에서 분리한다. 현재 upstream의 전체 reset-ID 균등 추출은 task별 state 수가 다르면 task 균등과 같지 않으므로 대체가 필요하다.

### Native loss의 집계와 보정 위치

[RLinf actor](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/workers/actor/embodied_fsdp_actor_worker.py#L235)는 종료 마스크와 길이 `L_j`를 계산한 **뒤** reward filter를 적용한다. Filter는 row를 삭제하거나 통과할 때까지 재수집하지 않고 mask를 바꾼다. [loss](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/algorithms/losses.py#L235)는 길이 비율 `L_j/H`로 집계를 보정한다. 아래 식은 동일 H·group size·action dimension, 전체 chunk를 같은 비중으로 처리하는 batch 조건에서 이 경로를 풀어 쓴 것이다. 임의의 다른 trainer에 적용되는 일반식은 아니다.

- `m⁰_jt`: first-terminal 행동까지 포함한 유효 mask, `L_j=sum_t m⁰_jt`, `H=512`, `d=7`.
- `A_j=(R_j−group_mean)/(group_sample_std+10⁻⁶)`; group size 8. 현재 GRPO 경로는 group 안에서 정규화한다.
- `ell_jta=max(−A_j rho_jta, −A_j clip(rho_jta,0.8,1.28))`. `rho`는 action logprob ratio이며 task 확률 보정과 별개다.
- Native reducer: `J=(1/(B H d)) sum_jta [H/L_j · F_g · m⁰_jt · ell_jta] = (1/B) sum_j [F_g/(L_j d) · sum_ta m⁰_jt ell_jta]`.
- Task 보정군: 같은 식의 **각 group 손실에 `w_g=p_i/q_i`를 한 번** 곱한다. Elementwise PPO clipping 이후·scalar reduction 이전에 적용하고 `loss_mask_sum`, reward, group 표준편차, action ratio를 바꾸지 않는다. `sum(w)`로 다시 나누거나 task weight를 clipping하지 않는다.

여기서 `B`는 뽑은 전체 rollout 수다. 필터된 group만의 수로 분모를 바꾸면 다른 objective가 된다. 동일한 크기의 microbatch·rank를 평균하고 gradient accumulation을 한 번 나눌 때 위 집계와 맞는다. 불균등 shard나 누락 chunk는 별도 가중치가 필요하므로 첫 검사는 동일 크기로 한정한다. `L_j=0`, 확률/ID 누락, 잘못된 group 조합은 비교를 중단할 구현 오류이며 silent 재수집으로 숨기지 않는다.

**첫 주 비교는 `filter_rewards=false`, KL/entropy/value/SFT 추가 loss=0**으로 고정한다. Native filter 0.5–4.5는 binary return `{0,5}`·G=8이면 성공 k=1…7 group만 남긴다. k=0·8은 중심화 advantage가 0이므로 이 제한된 actor-only 조건에서는 filter 해제와 같은 손실이 된다. Shaping·다른 reward·추가 loss까지 같은 효과라고 일반화하지 않는다. Native filter를 켠 비교는 mask와 원 분모를 보존하는 별도 호환성 검사다.

`p/q`의 기대값 관계는 **현재 behavior policy에서 정의한 고정 surrogate**에만 적용된다. 성공률의 unbiased gradient, Adam 이후의 동일 기대 parameter update, 정책이 달라진 두 run의 동일 학습 경로를 보장하지 않는다. 같은 q라도 optimizer 비선형성과 학습 이력은 남는다.

### 손계산으로 확인한 경계

아래는 식의 예시이며 데이터·실행 결과가 아니다. 단순화를 위해 H=4, d=1인 두 trajectory를 사용한다.

| 사례 | 손계산 | 의미 |
|---|---|---|
| A 유효 loss `[1,3]`, 길이2; B `[4,4,4,4]`, 길이4 | Native: `(2+6+0+0+4+4+4+4)/8=3`. 유효 token 전체 평균은 `20/6=10/3` | Native를 단순 token 평균으로 대체하면 estimator가 바뀜 |
| 위 A의 group을 mask=0 | Native 전체 슬롯 분모 유지: `16/8=2`; 남은 B만 평균하면4 | Mask와 row 삭제/재정규화는 다름 |
| Task loss 평균 A=2, B=4; p=(1/2,1/2), q=(3/4,1/4) | 보정 없는 기대 loss=5/2; w=(2/3,2)이면 `(3/4)(2/3)2+(1/4)2·4=3` | 분포 보정의 기대값 관계 |
| 같은 q에서 우연히 A/B 한 개씩 뽑힘 | 비정규화 추정량=14/3, self-normalized 값=7/2, 목표 기대값=3 | 한 batch의 정확한 일치를 요구하지 않음; self-normalization도 다른 추정량 |

향후 Docker tensor 검사에서는 위 수치뿐 아니라 shuffle·rank split·epoch reshape 이후의 ID/weight 정렬과 gradient를 확인한다. 이번에 tensor 검사를 통과했다고 기록하지 않는다.

### 배분 규칙과 비교군

첫 규칙은 단순 frontier score로 정했다. Task별 최근 **최대 32개 complete train group**에서 성공 수를 k, rollout 수를 n이라고 할 때 `s_i=(1+k)/(2+n)`, `a_i=s_i(1−s_i)`, `q_i=0.2 p_i+0.8 a_i/sum a`다. 이 smoothing을 group 내부 상관을 무시한 정교한 posterior로 해석하지 않는다. `q_i≥0.02`, `p_i/q_i≤5`이며 coverage floor는 유한 run에서 모든 task가 관측된다는 보장은 아니다. 실측 draw 수와 weight ESS를 보고한다. Rule/계수는 효과를 보지 않고 고른 운영 초안이며 최적성 주장이 아니다.

| 군 | Task 수집 | Loss weight | 해석 |
|---|---|---|---|
| U | p로 복원 추출 | 1 | 균등 기준선 |
| Q-native | 공통 calibration으로 만든 **고정 q** | 1 | 목표의 task 비중 변경을 포함한 배분 |
| Q-fixed | Q-native와 같은 q·task/state draw schedule | p/q | 기준 surrogate의 task 비중 유지 |
| C-fixed — 조건부 | `q_i=0.2 p_i+0.8 (1/c_i)/sum(1/c)` | p/q | c는 calibration의 group당 실제 simulator control API 호출 수; 단순 비용 대안 |

N2 최초 calibration 초안은 동일 SFT에서 task당 train 초기 상태1개·8 rollout, 총80 rollout이었다. **아래 N2-R1에서 상태 이질성 진단에는 task당2 state×2 group, 총320 rollout을 권고하도록 보완했다.** 80 rollout만으로 진행할 때는 한 상태의 탐색으로 해석한다. Selector/cost 추정에만 사용하고 gradient에는 넣지 않는다. Task/state·sampling seed와 q를 저장하고 Q-native/Q-fixed의 후속 paired draw schedule을 고정한다. **두 군은 각자의 현재 정책으로 새 trajectory를 생성**한다. 같은 행동 데이터로 학습하는 비교가 아니다. Calibration 효과의 불확실성은 training seed별로 별도 calibration을 반복해 반영한다. Q/C에는 필요한 calibration 비용을 전부 청구하며 U에는 필요 없는 비용을 억지로 청구하지 않는다. 공유 수집을 실제로 한 번 했더라도 독립 알고리즘 비용에는 각 방법의 요구량을 계산한다.

첫 학습 비교의 후보 shape는 **8 groups×8 rollout=64 envs, rollout_epoch=1, H=512, C=8 → 4,096 chunk rows/update**, global batch=4,096·microbatch=32·update_epoch=1이다. Upstream의 rollout_epoch=16/global batch=16,384에서 바뀌므로 논문 원 결과의 faithful reproduction이라고 부르지 않는다. Full-parameter 학습 후보이며 VRAM/시간은 아직 검증하지 않았다. 메모리 때문에 LoRA로 바꾼다면 모든 군에 같은 별도 계약을 적용한다.

첫 bounded learning pilot은 native 검증 후 **최대16 updates·training seeds 0/1/2**로 제안한다. 이는 power 계산이나 큰 학습의 실행 승인이 아니다. 초기 checkpoint·4/8/16 update의 고정 평가와 비용 축의 결과를 보되 최고 test checkpoint를 선택하지 않는다. 첫 실행 자원 측정 후 공통 resource cap을 봉인하며 cap 안의 마지막 checkpoint를 비교한다. 비용이 서로 다르면 update 16끼리의 비교를 동일 계산 예산 결과라고 부르지 않는다.

C의 c가 모두 같으면 수식상 q=p다. 현재 고정 512-step loop에서는 유효 episode 길이 차이만으로 c 차이를 만들 수 없으므로 C를 독립 알고리즘처럼 중복 실행하지 않는다. Reset/정착 호출이 실제로 다르면 그 차이를 기록한 뒤 비교한다. Mixed batch wall time을 임의로 task별 시간으로 나눠 c에 넣지 않는다.

**적응형 q 갱신은 후속 확장**이다. 각 update가 모두 끝난 뒤 과거 train 결과만으로 다음 q를 계산하며 dev/eval 결과는 입력하지 않는다. 정책별 이력으로 q가 갈라지는 비교는 전체 adaptive 알고리즘 효과다. 고정 q에서 가중치 효과를 분리한 결과와 혼합하지 않는다. 원형 DRATS의 minimax 목적이나 VIP의 가변 group size도 첫 비교와 다르므로 위 군을 해당 논문의 재현으로 이름 붙이지 않는다.

### 평가 분할과 비용 기준

Pinned LIBERO-Goal의 각 task에 공개 초기 상태 50개가 있다는 공식 설명을 출발점으로 **row 0–29 RL-train / 30–39 dev·P0 / 40–49 eval**을 정했다. Payload는 아직 decode하지 않았으므로 실제 row 수·hash·중복 여부를 확인한 분할 manifest는 미생성이다. Docker 준비 시 row 수가 다르거나 split 사이 같은 상태가 확인되면 결과를 보기 전에 계약을 수정하고 새 hash를 남긴다. 다른 task 간 공유 layout 자체는 오류가 아니지만 독립 scene 일반화로 주장하지 않는다.

Checkpoint 통계의 `num_trajectories=10`과 `traj1` 이름은 원 시연 ID를 알려 주지 않는다. 따라서 **RL 적응 단계에서 분리한 초기 상태**라고만 부르며 pretraining/SFT와 완전히 독립인 평가나 unseen-task 성능으로 표현하지 않는다. 평가는 task당 eval 상태10개, 공통 sampling seeds 100/101/102·temperature1.6, 성공은 첫 종료까지의 simulator predicate로 정한다. 10 task 평균이 주 지표이고 training seed가 독립 run 단위다. 300개 평가 trajectory를 300개의 독립 학습 실험으로 세지 않는다.

실제 환경 비용의 주 분모는 **개별 simulator control API 호출 합계**다. Constructor/reset/정착·실패 시도·terminal 뒤 호출도 포함한다. 물리 integrator substep은 별도 counter이며 control call과 같은 단위가 아니다. 정책 forward 호출/실제 batch 슬롯, backward 처리 chunk/action-token 슬롯, optimizer updates, GPU-hours, end-to-end wall time을 함께 기록한다. CUDA 비동기·worker overlap 때문에 stage 시간 합계를 전체 wall time으로 대체하지 않는다. 학습·selector calibration 비용은 효율 지표에, 고정 평가·설치/asset 준비는 별도 비용에 기록하고 전체 연구 소요도 제공한다. 실제 비용 계측치는 아직 없다.

<a id="nonexperimental-review"></a>
## 추가 비실험 검토 — GAP-ALLOC-N2-R1 / 2026-11-09

[7단계 buildup 가이드](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)에 따라 새 근거·반례가 바꾸는 부분만 보완했다. 아래 식과 예시는 **수작업 논증**이며 simulator·정책·합성 데이터 실험 결과가 아니다. P0 실행 코드·source/checkpoint pin·24개 제어 검사의 의미는 그대로 유지한다.

### 1. 추가 선행으로 좁힌 기여

| 직접 대조 | 이번에 확인한 범위 | 우리 주장에 적용할 제한 |
|---|---|---|
| [VIP §4, Assumption4.1·Prop.4.2–4.3](https://arxiv.org/html/2602.01601v3#S4), ICLR2026 | Dr.GRPO/RLOO의 projected-gradient 분산을 reward/score-function 관련 가정하에 분석하고 prompt별 rollout 수를 배분 | 우리의 std-normalized GRPO·고정 G8·실제 다차원 gradient에 `s(1−s)`가 곧 최적 score라는 보장을 옮길 수 없음 |
| [DRATS App.F.1](https://arxiv.org/html/2605.14350v1#A6.SS1), [NeurIPS2026 공식 목록](https://neurips.cc/Downloads/2026) | 같은 목표의 resampling/reweighting과 gradient-estimate 정확도를 이미 비교 | Sampling과 weighting의 차이 자체는 새 기여 아님. 단순히 VLA로 다시 실행하는 것을 넘어 로봇 조건에서 판단을 바꾸는 근거 필요 |
| [SimpleVLA-RL §3.3](https://arxiv.org/html/2509.09674v1#S3.SS3), ICLR2026 | 혼합 outcome group을 채울 때까지 재수집하는 dynamic sampling을 설명 | 고정 전체 batch에서 mask만 바꾸는 우리 RLinf 경로와 다름. 주 비교를 SimpleVLA 원 결과 재현이라고 부르지 않으며 rejection/re-fill 비용은 별도 비교 |
| [Prism-GRPO §4.1–4.2·App.C/F](https://arxiv.org/html/2608.17423v1), **arXiv2026** | 같은 scene의 동일 outcome group에 실행 quality reward와 RLOO를 적용. Within/between-scene 차이·refill 구현·rollout/시간 비용도 분석 | Zero-advantage group·scene 이질성·비용 문제를 처음 발견했다는 주장 제외. Binary reward를 유지하는 task 배분과 다른 개입이며 이후 강한 대안 |
| [VSR §2·App.B.1–B.4](https://arxiv.org/html/2610.15888v1), **arXiv2026** | State proposal의 reward variance·gradient scale 조건과 prefix replay를 다룸 | State variance/Neyman allocation 또는 역확률 보정의 재발견은 기여 아님. 우리는 intermediate-state reset을 도입하지 않고 task→공통 초기 상태 분포를 유지 |

Prism-GRPO·VSR은 이번 검색에서 공식 채택 venue를 확인하지 못했으므로 preprint로 취급한다. SimpleVLA 방법 대조는 지정 arXiv v1 구간이며 [공식 ICLR 페이지](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)는 게재 상태 확인에 사용했다. 최종본 전체와의 동일성을 확인한 것은 아니다. 신규 발견 자료는 단일 source 원장에 저장했고 이번에는 registry 신규 등록·읽기 상태 변경을 하지 않았다.

### 2. 중요한 반례: 과제 평균 성공률과 group의 학습 신호는 다르다

`u_i(z)=Pr(success | task i, initial state z, fixed policy)`와 `s_i=E_z u_i(z)`를 구별한다. z는 이미지 한 장이 아니라 instruction·물리 상태·controller 상태를 포함한 reset 조건이다. P0의 RGB hash 일치는 입력 확인이며 전체 상태 동등성의 증명은 아니다. N2의 Laplace 추정값은 유한 표본 운영값이며 아래 식의 population success와 동일하다고 가정하지 않는다. Binary reward·같은 초기 상태·조건부 독립 rollout G개에서 혼합 outcome이 나올 확률은

`r_i = E_z[1 − u_i(z)^G − (1−u_i(z))^G]`.

총분산 항등식은 `s_i(1−s_i) = E_z[u_i(z)(1−u_i(z))] + Var_z[u_i(z)]`다. Task 평균의 frontier score는 **상태 간 난이도 차이**도 크게 평가한다. 그러나 같은 z의 group advantage는 **상태 내 outcome 차이**를 필요로 한다. G≥2에서 함수 `1−u^G−(1−u)^G`는 concave이므로 `r_i ≤ 1−s_i^G−(1−s_i)^G`다. Task 평균만 대입하면 혼합 group 빈도를 과대평가할 수 있다.

| 이론적 두 task | 평균 성공률 | G8 혼합 group 확률 | 직접적인 binary GRPO 신호 |
|---|---|---|---|
| 모든 초기 상태에서 u=1/2 | 1/2 | `1−2(1/2)^8=127/128` | 비영 advantage가 생길 수 있음 |
| 초기 상태의 절반은 u=0, 나머지는 u=1 | 1/2 | 0 | 모든 group의 advantage0 |

이는 측정된 LIBERO 현상이 아니라 **task 평균만으로 signal을 식별할 수 없다는 반례**다. 첫 task에서도 gradient의 상쇄·clipping·다른 task와의 간섭이 있어 혼합 group이 성능 향상을 보장하지 않는다. 두 번째 task의 직접 신호는 task 재배분만으로 생기지 않지만, 다른 task로부터의 공유 표현 전이가 미래의 u를 바꿀 가능성은 남는다. Reward/critic/초기 상태 개입을 추가해야만 한다고 미리 결론 내리지 않는다.

따라서 현재 frontier rule은 **단순 비교 baseline**이며 검증된 allocator가 아니다. 새로 확인할 관측은 task별 평균 SR뿐 아니라 `task/state/policy version별 attempted groups, mixed groups, 실제 비용, advantage 분포`다. 상태별 신호를 고려하는 score가 필요할지는 이 차이가 실제로 존재하고 단순 배분 이후에도 중요할 때 판단한다. 위 항등식 자체의 신규성을 주장하지 않는다.

### 3. p/q 보정의 정확한 의미와 인과 해석 수정

고정 behavior policy·고정 평가 θ에서 task i의 **완전한 group loss gradient**를 `g_i`라 하고 `M_i=E||g_i||²`, `μ=Σ_i p_i E[g_i]`라 하자. 각 group을 i.i.d. q로 뽑고 group size·state 분포·loss를 유지하면 `ĝ=(1/n)Σ(p_i/q_i)g_i`에 대해

`E ĝ = μ`, `tr Cov(ĝ) = (1/n)[Σ_i p_i² M_i/q_i − ||μ||²]`.

이는 기존 importance-sampling 항등식을 이 비교에 적용한 것이며 새 정리가 아니다. **같은 기대 surrogate gradient라도 분산이 달라지고 Adam·global gradient clipping 이후 업데이트도 달라진다.** Equal-cost·coverage 제약 없는 이 식의 최소점은 `q_i ∝ p_i√M_i`지만, M을 모르는 현재 `s(1−s)`에 최적성이 생기지 않는다. 가변 cost·고정 wall-time·random stopping에는 이 equal-n 해를 그대로 적용하지 않는다. 비용이 같으면 C-fixed가 U와 같다는 기존 판단을 유지한다.

| 비교 | 답할 수 있는 것 | 단독으로 답할 수 없는 것 |
|---|---|---|
| Q-fixed − U | 같은 목표의 기대 surrogate를 유지한 task 배분 절차의 전체 효과 | 순수 variance 감소·Adam 이력·교차 task 전이 중 어느 것이 원인인지 |
| Q-native − Q-fixed | 같은 q에서 가중치 규칙을 바꾼 전체 효과 | 효과 차이의 전부가 목표 비중 변경 때문이라는 인과적 분해 |
| U-qweight − U (조건부 추가) | U 데이터에 q/p를 적용해 q 목표를 유도하는 대조 | Q-native와 실제 trajectory·optimizer 이력의 일치 |
| Q-native − U-qweight | 같은 기대 q surrogate에서 재수집과 재가중 비교 | DRATS에 없던 일반 원리나 VLA 고유 현상의 자동 입증 |

U-qweight는 처음부터 네 군 sweep을 요구하는 필수 gate가 아니다. **목표 변경을 원인으로 주장하려 할 때** 추가한다. 이때 같은 checkpoint·같은 저장 group에서 각 weight의 loss/gradient norm·clip 전후를 비교하고, update 효과를 비교하려면 모델과 optimizer state를 모두 복제한다. 동일 RNG seed만으로 optimizer state가 같아지지 않는다. 이 진단은 미구현·미실행이며 P0에 포함하지 않는다. 전역 gradient clipping 설정·실제 적용률은 P1에서 명시할 추가 구현 항목이다.

### 4. Calibration·단순 기준선·유한 표본 보완

**Calibration 수정 제안:** 이전 task당1 state×1 group(총80 rollout)은 task 내 이질성을 볼 수 없다. P1을 설계할 때 **task당 train row2개×독립 group2개×G8 = 총320 rollout**으로 교체하는 것을 권고한다. 각 training seed마다 state 두 개를 train0–29에서 비복원 선택하고 ID/seed를 결과 전에 고정한다. State 내부에서는 같은 정책·같은 초기 상태를 유지한다. 이것도 task 분포를 정밀 추정하는 크기는 아니다. 자원이80 rollout만 허용하면 작은 탐색은 가능하되 task 전체 난이도·heterogeneity 추정 주장을 하지 않는다. 어느 경우든 Q/C의 calibration 비용을 모두 부과하고 P0 범위는 늘리지 않는다.

초기 calibration만으로 미래 학습 구간의 난이도를 예측했다고 주장하지 않는다. 동일 checkpoint에서 **q 추정에 쓰지 않은 train 상태**로 예측을 확인하는 진단은 이후 조건부 후속이다. Dev/eval 결과로 q·온도·score를 선택하지 않는다. 정책 버전이 다른 group을 섞어 상태 이질성으로 해석하지 않는다.

**추가 단순 baseline:** U는 8개 task-group을 복원 추출하므로 한 update의 기대 distinct-task 수가 `10[1−(9/10)^8]≈5.70`이다. 같은64 rollouts에서 **10개 중8개 task를 균등 비복원 선택해 각각 group8**을 모으는 `U-distinct`는 성공률 predictor 없이 coverage 변동을 줄인다. 고정 θ에서 group 평균은 여전히 균등 task surrogate를 추정한다. Task 포함 확률은8/10이며 비복원 설계의 dependence/inclusion probability를 기록해야 한다. 각 draw의 조건부 확률을 p/q adapter에 그대로 넣거나 복원 sampler의 q metadata를 재사용하면 안 된다. P1용 별도 설계이고 미구현이다. 실제 c가 같아 C가 U로 퇴화하면, 독립된 C run보다 이 baseline을 먼저 비교한다. 초기 U/Q 두 군 탐색의 필수 진입 조건은 아니다.

**Coverage와 유효 표본:** q floor0.02·16 updates×8groups=128 draws에서도 특정 task의 미관측 확률은 고정 q=0.02일 때 `(0.98)^128≈7.5%`다. Weight ESS는 group 단위 `(Σ_g w_g)²/Σ_g w_g²`로 기록하며 같은 group의8 rollout이나 반복된 action token을 독립 배분 표본으로 세지 않는다. ESS는 gradient 방향·지원 범위의 충분성을 보장하지 않는다. 미관측 task·all-zero-advantage task가 있으면 제외하지 않고 함께 보고한다.

### 5. 분석 계획·중단 판단과 논문 규모

- **주 비교:** 고정 p와 공통 control-call 예산에서 Q-fixed와 U의 배포 평균 성공률 차이. Task별 결과·worst-task·GPU-hours·wall time을 함께 보고하되 주 metric을 사후 교체하지 않는다. 인공 return P0와 실제 정책 비교는 별개다.
- **비용 비교:** 학습+필요 calibration의 동일한 사전 예산 B에서 마지막 완성 checkpoint를 사용한다. B는 native 자원 측정 후 eval 결과를 보기 전에 정한다. 완료된 checkpoint의 실제 비용·남은 budget slack도 공개하고 시간축 보간이나 최고 test checkpoint 선택을 하지 않는다. 제어 호출 수의 개선을 GPU 시간 개선이라고 바꾸지 않는다.
- **통계 단위:** 같은10 task의 고정 평가 분포를 대상으로 training seed별 paired 차이를 먼저 계산한다. 세 training seed의900개 평가 trajectory를900개 독립 학습 반복으로 취급하지 않는다. 초기3 seed에서는 개별 차이·평균·범위를 보여 주고, 좁은 CI·유의하지 않음을 동등성 증거로 쓰지 않는다. 평가 seed/초기 상태는 두 군에서 맞추되 동일 물리 trajectory라고 부르지 않는다. [RL 소수 run 평가 근거](https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html)
- **탐색 우선순위용 기준:** 평균 SR 차이3 percentage points를 후속 투자용 잠정 관심 크기로 둔다. 이는 검정력 계산·실용성의 보편 기준·채택 기준이 아니다. 세 paired seed가 모두 같은 양의 방향이고 평균이 이를 넘으면 확인 실험 우선순위를 높인다. 부호가 섞이거나 불확실성이 크면 미확정이며 효과 없음으로 판정하지 않는다. 이 기준을 바꾸면 새 eval을 보기 전 이유를 기록한다.

| 후속 관측 | 다음 판단 |
|---|---|
| 평균 SR은 비슷한데 상태별 mixed-group 빈도가 다르고 frontier의 순위 예측이 실패 | 상태 이질성을 설명 변수로 분석. 별도 상태에서 예측이 유지되는지 확인 후 단순 score 대조; 새 방법 GO는 아님 |
| Q-fixed가 U를 이기지만 U-distinct와 차이가 불명확 | 우선 coverage 변동 설명. 더 복잡한 predictor 개발을 미룸 |
| Q-native만 개선 | 목표/가중치·gradient scale·optimizer 설명을 추가 대조. “배분의 순수 효과”로 쓰지 않음 |
| 같은 control-call budget 이득은 있으나 GPU/wall-time 이득 없음 | Interaction efficiency로 범위 제한. 전체 계산 효율 주장은 보류 |
| 직접 신호가 없거나 모든 방법 차이가 작고 불확실 | 비용 상한에서 진단 종료. Reward/critic/다른 상태 개입은 별도 가설; 단순 task 재배분의 반복 sweep은 하지 않음 |
| 반복 가능한 중요한 차이가 강한 단순 기준선 이후에도 남음 | 새로운 training seeds와 한 추가 suite 또는 다른 checkpoint 중 하나로 우선 확장. 필요한 범위를 선택하고 처음부터 다중 로봇/실물 전체를 요구하지 않음 |

**석사 논문으로 남길 수 있는 이야기:** task 평균 curriculum 지표가 로봇의 초기 상태별 group 신호와 실제 비용을 언제 잘못 예측하며, 그 차이가 정책 학습과 알고리즘 선택을 바꾸는지 설명하는 실증 연구다. 중요한 효과와 범위가 확인되면 가벼운 배분 방법으로 확장할 수 있다. 반례·수식만 남거나 기존 논문의 현상을 한 checkpoint에서 다시 보인 정도이면 독립 top-tier 논문의 근거는 약하다. 현재는 **작은 분석 탐색 계속 / 독립 방법 기여 미확정**으로 유지한다.

**구현 공수·외부 비판:** P0 이후 첫 구현 점검의 산출물은 실제 worker→actor metadata 정렬·native loss 일치, 그다음 실제 calibration/cost 기록이다. 첫 구현 주가 끝나면 남은 의존성을 검토하며 무기한 trainer 이식을 하지 않는다. 개인 일정·GPU-hours 추정은 미정이다. 독립 연구자에게 받을 핵심 질문은 “DRATS/VIP/Prism/VSR 이후 어떤 새 결정을 바꾸는가?”, “task 평균 대 상태 내 신호 차이가 실제 allocator 선택에 중요한가?”, “U-distinct와 optimizer 설명으로 충분하지 않은가?”다. 질문만 작성했고 외부 전달·응답 수신은 없었다.

**이번 비실험 종료점:** 직접 선행·반례·해석 수정·비교/통계 설계는 보완했다. 실제 상태별 signal·학습 이득·cost·외부 비판은 미확인이다. 이를 메우려고 같은 요약을 다시 쓰지 않으며, 다음 실행은 기존 bounded P0다. P1 보완안을 현재 P0의 실행 승인·구현 완료로 바꾸지 않는다.

## 한 페이지 논문 이야기

**문제:** 여러 과제를 학습하는 VLA RL의 효율을 비교할 때, 수집 배분과 목적 가중치·실제 계산 비용의 차이가 한 성공률 곡선에 섞일 수 있다.

**선행과 차이:** Adaptive task sampling·variance allocation·resampling 대 reweighting은 이미 존재한다. 우리는 단일 VLA의 고정 배포 목표 아래, 실제 로봇 rollout의 종료·batch·loss 처리까지 맞추었을 때 어떤 학습 효율 결론이 유지되는지 묻는다.

**기여 후보:** task 평균 성공률과 초기 상태별 group 신호의 차이가 실제 배분 선택을 바꾸는 조건, 같은 목표·실제 예산하 학습 효과, 단순 coverage 기준선 이후 남는 설명. **현재 결과 칸은 미확인**이다. Source의 구현 차이는 동기와 설계 근거이지 정책 이득·연구 현상의 입증이 아니다.

**Top-tier로 발전시키는 데 필요한 것:** 널리 사용하는 설정에서 결론을 바꿀 만큼 중요한 현상, seed/task 조건을 바꿔도 유지되는 설명, 강한 단순 대안과 비교한 새 지식이다. 코드상 분모 하나의 수정이나 기존 sampler의 VLA 적용만 남으면 독립 방법 연구의 근거가 약하다.

## 비실험 buildup 상태와 다음 단계

| 가이드 단계 | 현재 완료한 것 | 남은 증거/구현 |
|---|---|---|
| 1. 문제·독자 | 고정 배포 목표하 실제 예산의 학습 효율 | 사용 가능한 GPU/기간·실측 중요성 |
| 2. 가까운 선행 | N1–N2 source + N2-R1 VIP/DRATS/SimpleVLA 지정 본문·Prism/VSR 대조 | Native 실행 일치·필요 시 최종본/전체 baseline 구현 |
| 3. 질문·대안 | 상태 내/상태 간 신호 반례·p/q 기대값/분산 경계·optimizer 대안 | 실제 현상 빈도·효과 방향/크기 |
| 4. 논문 이야기 | 결과를 비운 문제–차이–기여 | 실증 결과·외부 독자 반론 |
| 5. 최소 비교 | 고정 q·calibration 보완·U-distinct/재가중 조건부 대조·seed 단위 분석/판단 규칙 | State hash·native 교정·resource cap 실측·P1 구현 |
| 6. 실행 부담 | Immutable image/source·checkpoint identity·recipe·sampler/actor-facing sidecar·loss/IO fixture·launcher 작성, Docker 제어24검사 통과 | Full-parameter VRAM fit·native image/import/payload·tensor/IO/gradient, 전체 worker/channel 연결 |
| 7. 외부 비판 | 검토 질문 준비 | 독립 피드백 미수신 |

외부 검토 질문과 미수신 상태는 위 N2-R1의 구현 공수·외부 비판 항목에 통합했다.

**N2 결론:** 내부 비실험 비교 설계는 정리됐다. Task 배분의 기대 손실 보정과 비용 비교는 조건부로 구체화할 수 있지만, simulator/model을 통과하는 데이터 정렬·수치·행동은 미검증이다. 새 scheduler를 개발하기보다 **작은 native 검사를 거쳐 분석 후보의 실제 효과를 판단**한다. GPU 부족뿐 아니라 강한 직접 선행·미확인된 잔여 효과가 기여의 한계다. 작은 탐색을 계속할 가치는 유지한다.

**P0-PREP 실제 결과:** 현재 Mac ARM64의 local Docker GPU allocation은 exit125, 새 launcher의 자원 검사는 exit3으로 차단됐다. 기존 Docker image에서 stdlib 제어 검사24개를 통과했다. Source/image identity·recipe·sampler/actor-facing sidecar·native loss/gradient fixture를 작성했지만 torch tensor·native model/simulator 실행은0이다. **자원 미충족은 연구 가설의 반증이 아니며 제어 검사 통과도 정책 효과의 증거가 아니다.** [실제 결과·실행 경계](../재현%20방법/README.md#preparation-history)

**다음 GAP-ALLOC-P0:** 실행 파일을 포함한 revision을 호환 local Linux x86-64/NVIDIA 컴퓨터로 전달한 뒤 `check → build → prepare → p0`. 이 단계는 두 task의 짧은 fragment·인공 return으로 IO/metadata/gradient 연결만 검사한다. 전체 EnvWorker/collector 연결·adaptive history·P1 학습 비교는 별도 미구현이다. [상한·재개 방법](../재현%20방법/README.md#resume)을 따르며 N2/준비 완료만으로16-update pilot을 시작하지 않는다. 같은 비실험 요약을 반복하는 N3는 추가하지 않는다.
