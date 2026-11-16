# GAP-S1 — VLA 중심 공백 검토의 중간 종합과 연구 선택

- 완료: 2026-10-24 KST. **이번 비교에서 본격 buildup을 이어갈 후보는 채택하지 않는다.** 기존 질문의 문헌적 가치와 HOLD는 보존한다. VLA 분야 전체의 NO-GO나 모든 후보의 실험적 기각을 뜻하지 않는다.
- 범위: 기존 **13개 질문 렌즈 + 별도로 보존한 GAP-DATA**를 비교했다. 과거 16개 후보는 중복·재개 경계를 확인하는 자료다. 이를 합쳐 독립 연구 후보 30개로 세지 않는다.
- 근거: 기존 지정 본문·code 심사와 P4 저장 결과를 재사용했다. 이번 외부 확인은 결정에 직접 관련된 공식 paper 페이지 5건, preprint abstract 1건, GitHub README 4개 revision에 한정한다. 2024–2026 전수 조사나 새 full-text 정독이 아니다. [Source·revision·확인 깊이·검증 ledger](../sources/vla_gap_selection_review_2026-10-24.json).
- 실험·학습·runtime qualification·PDF/dataset/checkpoint 다운로드·신규 논문 등록·읽기 상태 승격은 없다. 실제 외부 연구자 피드백도 아직 없다.

## 1. 선택하지 않은 이유와 판단의 경계

VLA와 가까운 **데이터 선택의 정책 간 전달, latent action의 물리 조건 전이, world-model 선택 오차**를 상세 비교했다. 세 질문 모두 답에 따라 실제 설계 선택이 달라질 수 있다. 그러나 현재 남은 문장은 각각 “정책에 따라 다르다”, “물리 조건이 바뀌면 decoder만으로 부족할 수 있다”, “후보를 고르면 모델 오차를 이용할 수 있다” 수준이다. 해당 현상 자체는 선행 연구가 이미 다룬다. **어떤 관측 가능한 조건에서 어느 대안이 더 유효할지 구별하는 예측과, 그 예측을 좁은 비용으로 시험할 구체적 비교가 함께 준비되지 않았다.** 이는 현재 제안에 대한 연구 투자 판단이다.

공개 코드가 있다는 이유로 GO로 올리지 않았고, 완성된 공개 데이터가 없다는 이유만으로 탈락시키지도 않았다. 새 수집·fixture·adapter가 필요해도 질문이 분명하고 비용과 비교가 구체적이면 pilot 후보가 될 수 있다. 이번에는 문헌 충돌을 피한 뒤 남는 추가 지식을 먼저 특정할 필요가 있다. GPU만 확보해도 이 문제가 해결되지는 않는다.

| 판단 종류 | 현재 해당 사례 | 의미 |
|---|---|---|
| 넓은 주장이 기존 연구와 충돌 | 데이터 전이, latent supervision, WM 검증, memory/retention 등 | 그 넓은 문장을 독립 기여로 다시 제안하지 않음. 조건부 질문까지 해결됐다는 뜻은 아님 |
| 비교 자료의 충분성 미확보 | CAUSAL·DEFORM의 현재 공개 자산 설계, CONTACT 등 | 현재 자료를 모으는 방식은 종료/보류. 효과가 없다는 실험 증거는 아님 |
| 사전 예측에 반하는 bounded 결과 | PLAN의 GAP-P4 | 이 pilot의 joint gate 실패. navigation 전체·native VLA에 일반화하지 않음 |
| 실행 자원·현실 수집 미확보 | THERMAL, 실제 contact/HRI, native VLA 경로 | 과학적 가치와 실행 준비도는 별도. 장치 확보가 신규성 증거는 아님 |

## 2. 13개 질문과 기존 DATA 질문 비교

아래는 날짜별 **선택 심사 기록**이며 새 gap registry나 읽기 우선순위가 아니다. 질문·원래 판정의 canonical 위치는 각 링크의 synthesis다. 부담은 현재 설계에서 필요한 작업의 상대적 설명이며 실측 GPU 시간이나 비용 견적이 아니다.

| 질문·기존 근거 | 남겨 볼 차별적 예측 / 가장 강한 단순 대안 | 재사용 자산과 새 작업 부담 | 가장 작은 기각 비교 / 이번 판단 |
|---|---|---|---|
| [CONTACT](../../synthesis/03_manipulation_contact.md#gap-contact-2026), [R2](./CONTACT_INTERFACE_REVIEW_2026-10-23.md) | 같은 RGB/proprio history에서 실제 요구 행동이 갈리는 조건을 센서가 구별하는가 / history·compliance controller | Force/tactile 문헌·일부 코드/데이터. 같은 task의 sensor coverage·시간·controller·실제 접촉 수집 필요: 높음 | 같은 조건에서 history나 공통 보수 행동으로 충분하면 센서 필요성 주장 축소. **REVISE/HOLD**, 결정적 사례 미확보 |
| [LATENT](../../synthesis/04_vla_generalist.md#gap-latent-2026), [L2](./LATENT_ACTION_REVIEW_2026-10-23.md) | 물리 변화에 따른 decoder-only와 representation 적응의 선택 조건 / action 정규화·supervised IDM·BC | VILA/LAOM/ViPRA 등 부분 자산. 물리 조건 조작·동일 label union·학습 비교 필요: 중간~높음 | §4의 동일 예산 비교. **일반 주장 NO-GO, 조건부 진단 HOLD** |
| [MEMORY](../../synthesis/04_vla_generalist.md#gap-memory-2026), [V2](./INTEGRATED_GAP_REVIEW_2026-10-23.md) | 기억 유형×보존 간격×chunk의 상호작용이 실행 능력과 구분되는가 / 단순 history·oracle memory | MemoryVLA/RoboMME/MIKASA 계보. 인과적 memory 조작·oracle competence·누설 통제 필요: 중간 | 기억을 줘도 못 하는 task와 정보 부족을 분리. 이미 존재하는 benchmark/개입의 반복을 넘는 예측 미확보. **HOLD** |
| [RETENTION](../../synthesis/04_vla_generalist.md#gap-retention-2026), [V2](./INTEGRATED_GAP_REVIEW_2026-10-23.md) | 공정한 replay 이후 남는 조건부 손실 / ER·normalizer·phase coverage | 공개 continual-learning 계보. stream별 반복 학습·보존/새 task 성능·전체 memory/compute 예산 필요: 높음 | 처음부터 못 배운 task의 낮은 forgetting을 제외하고 ER와 비교. **HOLD**, replay로 설명되지 않는 예측 미확보 |
| [DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026), [W2](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md) | 어느 조건에서 source subset 재사용보다 target 재선택이 필요한가 / random·diversity·success·retrieval | DataMIL/CUPID 공개 component. dataset ID 보존·두 정책 loader·선택/학습 비용 통합 필요: 중간~높음 | §3의 source/target crossed 비교. **일반 전이 NO-GO, 조건부 예측 HOLD** |
| [WM](../../synthesis/05_world_models_safety.md#gap-wm-2026), [WM1](./WORLD_MODEL_SELECTION_REVIEW_2026-10-23.md) | proposal/K 변화에 따른 선택 후 오류를 배치 전 예측하는가 / 작은 K·LCB·support 제한 | Cosmos/VeriVLA/DreamTrue 부분 자산. 같은 상태 분기·독립 outcome·완결된 rollout 평가 필요: 높음 | §5의 nested candidate 비교. **일반 방법 NO-GO, 조건부 진단 REVISE/HOLD** |
| [GEOMETRY](../../synthesis/07_robotics_3d_perception.md#gap-geometry-2026), [W2](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md) | 누락 표면과 위치 오류를 구분하면 행동 위험 예측이 달라지는가 / TSDF unknown·pose 보정·고정 inflation | PwC/Splat-Nav source. 독립 collision ground truth·고정 planner/센서 지연·scene 분리 필요: 중간~높음 | 같은 collision–progress 곡선에서 단순 보정 이후 잔여 차이. **REVISE/HOLD**, calibrated navigation 자체는 선행 |
| [SYSID](../../synthesis/05_world_models_safety.md#gap-sysid-2026), [W2](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md) | 비슷한 residual의 parameter 변화와 누락 상태가 다른 control 결정을 요구하는가 / history·lag·KF·기존 active probe | SPI-Active 등 source, CUDA 의존 component. 물리적 구별 사례·probe 비용·controller 경로 필요: 높음 | 같은 probe 비용에서 history/model-class 대안으로 설명되면 축소. **REVISE/HOLD**, native VLA 연결 미확보 |
| [CAUSAL](../../synthesis/02_rl_il_offline.md#gap-causal-2026), [CF2](./CAUSAL_DATA_SUFFICIENCY_REVIEW_2026-10-23.md) | 어떤 사전 정보 수집이 coverage보다 가치 있는가 / history·coverage·IV/delphic·CIVIL 비용 비교 | DROID/Bridge/OXE/CIVIL 부분 자료. 행동 전 cue·원본 join·비용·native outcome 새 연결 필요: 높음 | cue/demo 수집 비교 자체는 선행. **현재 공개 자료 설계 종료**, 문헌 진단 보존 |
| [DEFORM](../../synthesis/03_manipulation_contact.md#gap-deform-2026), [DE2](./DEFORMABLE_ASSET_SUFFICIENCY_REVIEW_2026-10-24.md) | material–attachment 모호성이 task별 probe 선택을 바꾸는가 / 고정 probe·feedback·ILC | AdaptiGraph/JIGGLE/PGND/DPSI 부분 자산. 독립 material/anchor·online 이력·시도 비용·task pair 필요: 높음 | 동일 물리 조건에서 간단한 feedback/probe로 충분하면 축소. **현재 공개 자산 설계 종료·진단 HOLD** |
| [PLAN](../../synthesis/01_planning_control.md#gap-plan-2026), [P4](../experiments/reactive_nav_pilot/RESULTS.md) | 반응형 상대에서 route change의 위험과 보정 악화가 함께 증가하는가 / 고정 margin·rolling quantile·wait | Docker 재분석 가능한 실제 384 branch. 현재 설계의 추가 rollout은 종료 | joint gate **실패**. **현재 진단 HOLD**, 일반 방법 NO-GO·native HOLD. 결과에 맞춘 scene/threshold 검색 안 함 |
| [HRI](../../synthesis/01_planning_control.md#gap-hri-2026), [H1](./HRI_HELP_RELIABILITY_REVIEW_2026-10-23.md) | 질문 유형/상대 조건별 정확도–지연이 도움 선택을 바꾸는가 / expected-cost threshold·conditional calibration | RCIP/UPS/PARTNR 등 계보. question–reply–time–outcome 및 participant/task holdout 필요: 높음 | no/always ask·best fixed·expected-cost와 같은 base skill/정보에서 비교. **일반 방법 NO-GO·진단 HOLD**, 실제 사람 근거 미확보 |
| [THERMAL](../../synthesis/06_locomotion_whole_body.md#gap-thermal-2026), [W1](./BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md) | 작업/휴식 배치가 지속 처리량을 바꾸는 조건 / derating·고정 rest·thermal MPC | FALCON 등 문헌. 실제 온도/전류/환경/payload/cooling·장시간 시행 필요: 매우 높음 | 같은 duty/cooling에서 처리량·열 제약 비교. **scout 가설·hardware/data HOLD**, 다른 후보 탈락만으로 승격 안 함 |
| 별도 [GAP-DATA](../../synthesis/04_vla_generalist.md#gap-data-2026), [R1](./VLA_GAP_SCOUT_2026-10-23.md) | annotation/valid action/새 demo 중 수집 전 투자 선택 / ECT·CounterAlign·CAST 계보 | Counterfactual 자료/방법은 이미 존재. action-valid counterpart·비용 연결 새 비교 필요 | “언어 반사실 supervision” 자체는 직접 충돌. **기존 보류 유지**, 새 독립 후보로 중복 집계 안 함 |

## 3. 데이터 선택 전달: 무엇이 있어야 새 질문이 되는가

**논문 근거.** DataMIL은 정책을 반영한 데이터 선택을, CUPID는 evaluation influence를 이용한 데이터 선별을 이미 제시한다. 공식 metadata는 각각 ICLR 2026과 CoRL 2025다. 기존 W2 본문 심사에서 CUPID의 DP→π0 및 ATHENA의 π0→π0.5 연결도 확인했으므로 “작은 정책으로 선택해 VLA에 전달” 자체를 기여로 쓰지 않는다. ATHENA의 저자 CoRL 표기는 독립 acceptance 확인과 구분한다. [DataMIL 공식 abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html), [CUPID proceedings](https://proceedings.mlr.press/v305/agia25a.html), [W2 지정 본문/코드 근거](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md).

**남은 연구자 질문.** Target 재선택에 비용을 쓰기 전에, source subset을 그대로 써도 되는 조건을 예측할 수 있는가? 목표는 모든 정책에서 순위가 같다는 주장이나 순위가 다르다는 관찰이 아니라 **재선택 비용을 지불할 결정을 바꾸는 조건**이다. 현재는 representation·mode·실행 능력·데이터 분포 중 무엇을 측정해 어느 방향을 예측할지 정해지지 않았다.

**최소 비교 설계의 형태 — 미실행.** 같은 pool에서 A가 선택한 `S_A`와 B가 선택한 `S_B`를 두고 `S_A→A`, `S_A→B`, `S_B→B` 및 random/diversity/success/retrieval을 비교한다. Task/scene/episode holdout, subset 크기와 action 수, 전체 학습·선택 rollout·계산 비용을 함께 고정한다. Target selector와의 차이는 최적 subset 대비 regret로 부르지 않는다. 중복 제거·task 비율·normalizer·추가 계산만으로 관찰을 설명하면 “정책별 고유 데이터 가치” 주장을 줄인다.

**자산/부담.** DataMIL README는 LIBERO의 HDF5→RLDS→MDS와 선택 뒤 Octo co-training을 안내한다. CUPID 공개 예시는 PushT/RoboMimic의 diffusion-policy 경로다. 이번 확인은 두 README와 revision이며, 여러 loader를 통과한 episode ID의 일치나 VLA 간 end-to-end 실행은 미검증이다. 새 데이터를 전부 수집하기보다 ID/loader 연결부터 재사용할 여지는 있지만, 이를 실행하면 곧 연구 기여가 생기는 것은 아니다. [DataMIL pinned README](https://github.com/UT-Austin-RobIn/datamil/blob/f8fc4abccacd1e2b070e68128a7f2bce98f4b303/README.md), [CUPID pinned README](https://github.com/agiachris/cupid/blob/2941eba9427a3398d3cbe26b10c01e3ece56bd18/README.md).

**판정:** 정책·task를 바꾸어도 검증할 수 있는 사전 조건 예측과 작은 비교 경로가 함께 제시될 때 재심사한다. 현재 두 정책 이름·예산·조건을 임의로 넣어 실행 명세를 완성하지 않는다.

## 4. Latent action: supervision 효과를 다시 발견하는가

**논문 근거.** VILA의 view-invariant 표현에는 ground-truth action sequence에 기반한 정렬이 들어간다. 기존 L2에서 LAOM의 supervision, ViPRA의 backbone 적응, Action-Similarity Transfer의 동일 label 비교·decoder 예산·decoded replay와 closed-loop 차이까지 대조했다. 따라서 “latent에 실제 action label을 넣으면 좋다”와 “decoder replay가 좋아도 policy는 실패한다” 자체는 새 결론이 아니다. [VILA CVPR 2026 공식 abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html), [L2 본문/공개 경로 심사](./LATENT_ACTION_REVIEW_2026-10-23.md).

**남은 연구자 질문.** 관측 가능한 physical response 변화 중 어떤 것은 decoder/normalizer 수정으로 충분하고, 어떤 것은 representation 적응이 필요한가? 단순히 friction axis를 추가하거나 성공 후 “이 표현이 물리를 안다”고 해석하는 것은 부족하다. 현재 두 설명이 다른 행동을 예측하는 구체적 변화 조건은 정해지지 않았다.

**최소 비교 설계의 형태 — 미실행.** 같은 task/물리 조건·label ID 합집합·history/proprio·전체 적응 예산에서 frozen representation+decoder, representation+decoder, supervised IDM, pretrained visual encoder+BC, action/controller 정규화를 비교한다. 정답 latent의 decoded replay, 예측 command, native closed-loop outcome을 분리한다. 단순 정렬·추가 label·backbone 업데이트로만 차이가 설명되면 표현의 독립적 물리 전이 주장은 축소한다. 작은 pilot의 한 물리 조건은 기제 후보를 찾는 범위이고 광범위한 조건 분류의 입증은 아니다.

**자산/부담.** VILA 공개 README는 multiview HDF5, stage-1/2 checkpoint와 diffusion-policy 연결을 안내한다. 이는 물리 조건별 matched dataset이나 native VLA 비교 packet의 완성을 뜻하지 않는다. 새 물리 변형·조건별 label 및 공정한 적응 실행이 필요하며, language가 쓰이지 않는 visuomotor 결과를 VLA generalist 결과로 부르지 않는다. [Pinned README](https://github.com/joon-stack/vila-code/blob/5f34a3b5cf4d70b585282c66df1bd88fa72e98b3/README.md).

**판정:** 정규화 이후 effect 정보의 추가 가치만 남는다면 기존 E1과 합쳐 심사한다. 새 이름으로 E1 gate를 우회하지 않는다. 현재는 조건부 진단 HOLD를 유지한다.

## 5. World model: 알려진 선택 편향 이후 무엇이 남는가

**논문 근거.** Cosmos Policy는 action/future/value와 planning을 결합한다. VeriVLA는 후보를 반복 생성하고 latent model로 progress를 비교하는 검증을 이미 제시한다. 전자는 ICLR 2026, 후자는 이번 확인에서 arXiv v1이다. 기존 WM1에서 dWorldEval의 고정 정책 순위, DreamTrue의 전체 trajectory 평가와 동일 상태 모든 branch outcome의 차이, model exploitation 선행까지 대조했다. [Cosmos 공식 발표](https://iclr.cc/virtual/2026/poster/10006732), [VeriVLA abstract](https://arxiv.org/html/2610.21985v1#abstract), [WM1 근거](./WORLD_MODEL_SELECTION_REVIEW_2026-10-23.md).

**남은 연구자 질문.** 고정 proposal에서 잘 맞는 평가기가 K/proposal을 바꾼 뒤 선택한 행동에도 신뢰할 만한가? 알려진 winner's curse를 재시연하는 대신, **언제 추가 탐색을 중단하거나 proposal을 제한해야 하는지** 예측할 조건이 있어야 한다. K가 커지면 좋은 후보도 늘어나므로 항상 성능이 나빠진다는 가정은 두지 않는다.

**최소 비교 설계의 형태 — 미실행.** 같은 observation·simulator/controller state에서 nested candidate pool을 만들고, 같은 continuation으로 후보별 독립 outcome을 얻는다. 고정 K, 작은 K, mean/LCB, support 제한·짧은 horizon을 비교한다. 후보 생성·future/value·denoising·batching·wall time·제어 공백의 비용을 포함한다. Calibration error, 선택한 후보의 outcome, pool 안의 best available outcome을 분리한다. LCB/작은 K 또는 단순 지연 차이로 충분하면 새 선택 방법의 주장은 줄인다.

**자산/부담.** Cosmos README는 base-policy와 planning 경로를 구분하며 LIBERO와 실제 ALOHA 경로를 안내한다. 기존 source의 LCB 등은 이미 강한 baseline이다. README의 단일 base inference 자원 수치를 planning/학습 전체의 비용으로 사용하지 않는다. 동일 reset·후보별 outcome·독립 evaluator·고정 budget packet은 아직 만들지 않았다. [Pinned README](https://github.com/NVlabs/cosmos-policy/blob/18a2accadf4e7a3531e56754102af5a24d2316da/README.md).

**판정:** 현재는 일반 action selection NO-GO·조건부 진단 REVISE/HOLD다. 기존 C4/C6의 reward/selection 통계 문제로 환원되는지도 먼저 확인한다.

## 6. 기존 후보와 결과를 합칠 때 지켜야 할 경계

기존 [16개 요약](../research_candidates/summaries/README.md)은 그대로 보존한다. 새 gap 이름이 과거 gate를 초기화하지 않는다.

| 기존 주제 | 이번 질문과 겹치는 부분 | 유지할 한계 |
|---|---|---|
| 초기 RL 전이·C2·E1, semantic retention scout | DATA-TRANSFER/RETENTION/LATENT/DATA | RL 전이와 imitation/선택 효과 구별, 실행 label coverage, source episode/action 정렬. 초기 RETIRED와 E1 gate NOT_MET 유지 |
| 초기 latency·RP-3·C1·E2 | MEMORY·CONTACT·HRI의 history/지연/재관측 | Base competence·실제 primitive·동일 물리 시간 필요. Temporal broad NO-GO·memory expiry RETIRED 유지 |
| RP-2·C4·C5·C6 | WM/CAUSAL의 outcome·비용·selection | 복구·reset·reward·checkpoint 선택 문제를 새 명칭으로 재개하지 않음. 비용/성공 선택·독립 평가 경계 유지 |
| D1·D2·D3 | GEOMETRY·CONTACT·DEFORM·task 변경 | Observation 변화와 보정, grasp/transport, 동일 instance의 event/continuation 능력 구별. D3 gate NOT_MET 유지 |
| C3 | LATENT/action score 해석 | 저장 logits 한 checkpoint·16개 관측의 head 진단. 학습 개선·native policy 효과의 근거로 확장하지 않음 |

**실제 부정적 결과는 범위가 좁다.** P4는 dev12/cal24/test12에서 384 branch를 실행했으며 384개 독립 scene이 아니다. 무지연 M1의 위험 interaction은 +21.25pp였지만 H5 miscoverage 변화 interaction은 −4.27pp로 joint gate가 실패했다. 반응형 절대 위험은 유지5.42%→변경3.75%로 감소했다. 이를 “반응형에서 위험이 증가했다”거나 모든 VLA 후보의 효과가 없다는 근거로 쓰지 않는다. [P4 원 결과·한계](../experiments/reactive_nav_pilot/RESULTS.md).

## 7. 종료와 다음 행동

**GAP-S1 DONE, 채택 후보 없음.** 문헌 심사 기록은 끝냈고, 연구 효과·외부 피드백·native 실험은 완료하지 않았다. 같은 source 목록을 다시 조회하는 S2나 큰 학습 sweep을 자동 생성하지 않는다.

다음은 [TODO](../../TODO.md)의 **GAP-N1 — 새 근거 기반 선택 재심사, WAITING_EVIDENCE**다. 입력은 기존 데이터일 수도 있고 구체적인 새 수집 설계일 수도 있다. 한 후보에 대해 아래를 짧게 연결할 수 있을 때 해당 canonical 질문을 재심사한다.

1. **실제 결정:** 어떤 task/로봇/실패 비용에서 어떤 선택을 바꿀 것인지. VLA의 image/language/action 경로와 controller 중 무엇이 질문에 필요한지.
2. **판단을 바꾸는 새 근거:** 행동 전 이용 가능한 정보와 가능한 행동 차이, 독립 관측 사례 또는 선행 연구가 답하지 않은 구체적 조건. 이미 심사한 metadata만 다시 제시하지 않는다.
3. **경쟁 예측:** 제안 설명과 가장 강한 단순 대안이 어느 비교에서 어떻게 다를지. 긍정 효과가 이미 확인돼야 하는 조건은 아니다.
4. **작은 검사 경로:** 재사용 artifact 또는 새 수집/fixture의 절차·범위·비용 상한, 관측/행동/시간/outcome 연결, 분모·기각 기준. 첫 pilot에 모든 일반화 축이나 완성된 학습 시스템을 요구하지 않는다.

이 입력이 준비되면 명세 심사 → 로컬 Docker qualification → native baseline → 최소 구별 실험으로 간다. GPU 확보는 qualification 단계의 조건이며 연구 선택을 대신하지 않는다. 데이터셋·benchmark·진단도 별도 기여가 될 수 있지만, 현재 판정을 바꿀 정보와 다른 연구자가 재사용할 이유를 갖춰야 한다.

## 8. 유지보수 검증

TODO, synthesis 안내, buildup 운영 규칙을 동기화했다. 필수 `py_compile`, reading-tier 생성, repository audit, `git diff --check`가 통과했다. Registry 1,037편·집중 읽기 322편·표준 노트 5,185개이며 audit 오류/경고는 0개다. Canonical 파일 6개의 hash와 재사용한 근거 32개를 보존했다. 기존 dirty 파일 413개 중 이번 작업 대상 9개만 추가 수정했고 나머지 404개 및 기존 누락 경로 5개를 보존했다. 임시 README·snapshot 정리와 명령별 결과는 [ledger의 validation](../sources/vla_gap_selection_review_2026-10-24.json)에 기록한다.
