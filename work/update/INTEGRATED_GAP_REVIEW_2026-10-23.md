# VLA를 포함한 2024–2026 연구 공백 후보 통합 검토

- 조사일: **2026-10-23 KST** / 작업: **GAP-V2**
- 목적: VLA를 포함해 기존 다분야 질문을 함께 비교하고, 다음 문헌 심화 대상을 고른다.
- 질문의 canonical 내용: 각 [synthesis Open Questions](../../synthesis/README.md). 이 문서는 날짜별 조사 기록이며 새 gap registry·읽기 우선순위 source가 아니다.
- [이번 30건 source ledger](../sources/integrated_gap_review_2026-10-23.json) · [직전 VLA 46건 조사](./VLA_GAP_SCOUT_2026-10-23.md) · [다분야 40건 조사](./BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md) · [buildup guide](../../research/IDEA_BUILDUP_GUIDE.md)
- 후속 판정: 아래는 GAP-V2 시점의 선택 기록이다. [GAP-R2 직접 비교](./CONTACT_INTERFACE_REVIEW_2026-10-23.md) 후 CONTACT는 **REVISE / 진단 후보 HOLD**, 다음 활성 작업은 GAP-W2로 바뀌었다.

## 1. 이번 판단

**VLA 네 축과 다른 분야 아홉 축, 총 13개 질문을 같은 기준으로 비교했다.** 모두가 새로 발견한 공백이라는 뜻은 아니다. 접촉은 앞선 질문을 보강했고, latent action·memory·continual retention의 세 질문을 추가했다. Memory와 retention은 직접 선행과의 중복이 커 현재 보류로 남긴다.

다음 문헌 심화에서는 **VLA 접촉 센싱의 필요 조건 → 3D 지도의 실제 충돌 위험 → 데이터 선택 효과의 policy 간 전달**을 먼저 비교할 만하다. 앞의 두 질문은 manipulation과 navigation에 각각 연결된다. **System identification의 오류 유형 구분**도 후속 비교 대상으로 유지한다. 이 순서는 연구 성공 확률이나 읽기 tier가 아니라 현재 근거와 비교 설계의 구체성에 따른 잠정 작업 제안이다.

VLA만 고른다면 **GAP-CONTACT**를 먼저 검토하고, **GAP-LATENT**는 가까운 연구가 이미 답한 범위를 더 확인한 뒤 판단한다. “VLA에 메모리/촉각/RL을 붙인다”는 조합만으로 주제를 확정하지 않는다. RL은 새로운 정보를 수집하거나 policy를 개선하는 수단일 수 있지만 모든 후보의 필수 구성 요소가 아니다.

## 2. 범위와 확인 깊이

이번 pass에는 **30편**을 근거 목록으로 남겼다. 2024년 6편, 2025년 6편, 2026년 18편이다. 2024–2025는 generalist policy와 representation/control의 기반, 2026은 직접 충돌과 평가 경계에 집중했다. CoRL 2024 논문은 PMLR 출판 연도 2025와 구분했다. [공식 volume 정보](https://proceedings.mlr.press/v270/).

| 이번 확인 | 건수 | 해석 |
|---|---:|---|
| 공식 proceedings 또는 공식 conference paper | 20 | 19 proceedings + MemoryVLA 공식 paper/header/listing 1 |
| 저자에게서만 venue 확인 | 1 | Navigation OmniVLA의 ICRA 2026. 독립 공식 acceptance 확인과 분리 |
| 확인 범위에서 preprint / venue 미확정 | 9 | 최신 direct collision 확인용. top-tier 게재로 계산하지 않음 |
| 지정 HTML 본문 구간 대조 | 6 | Latent-action study, MIKASA-VLA, memory intervention, forgetting 저항성, 실제 continual VLA, PHASER |
| Abstract·공식 색인 중심 | 24 | 일부 supplement snippet/project/repository를 보조 확인했으나 본문 전체 정독으로 올리지 않음 |
| Registry identity 연결 | 14 | 제목/arXiv ID로 연결. 나머지 16편은 최종 admission 중복 심사 전의 미연결 자료 |

기존 registry 1,037편의 metadata·synthesis·후보 판정을 참조했다. 이전 GAP-R1의 46편, GAP-W1의 40편과 이번 30편에는 중복이 있으므로 **합계를 unique 논문 수나 정독 수로 표시하지 않는다**. 현재 2024–2026 registry 항목 757편 전체를 새로 읽은 것도 아니다.

직전 조사까지 합친 공식 출처 범위는 CVPR·ICCV·ECCV·NeurIPS·ICLR·ICML·CoRL·RSS·ICRA·IROS·T-RO 등이다. 이번 추가는 VLA 직접 선행을 중심으로 한다. IJRR·Science Robotics까지 균등하게 조사했다고 할 수 없고, journal 근거는 conference보다 적다. NeurIPS 2026의 기존 근거는 공식 program abstract이며 최종 proceedings와 구분한다. 모든 venue를 전수 조사한 systematic review는 아니다.

검색은 분야/현상에 year·venue를 결합한 뒤 exact title → 공식 출처 → 직접 선행의 본문/부록으로 좁혔다. 최신 preprint도 신규성 충돌을 놓치지 않기 위해 남겼다. Awesome list·검색 요약은 발견에만 사용하고, 논문 결론은 primary source로 대조했다. 홈페이지의 code 링크를 실제 자산의 완전 공개·실행 가능성으로 해석하지 않았다.

## 3. 2024 → 2025 → 2026의 문제 변화

아래는 직접 citation chain을 확정한 것이 아니라 연구 문제의 변화에 대한 합성이다.

| 축 | 2024 기반 | 2025 전개 | 2026과 연결되는 경계 |
|---|---|---|---|
| Generalist / embodiment | [OpenVLA](https://proceedings.mlr.press/v270/kim25c.html), [Octo](https://www.roboticsproceedings.org/rss20/p090.html), [CrossFormer](https://proceedings.mlr.press/v270/doshi25a.html), [HPT](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html) | 공개 policy를 adaptation·hierarchy·새 benchmark로 비교 | 로봇 수만 늘리는 주장보다 어떤 관측/행동/데이터 조건에서 전이가 성립하는지 필요 |
| Video / latent action | [HRP](https://www.roboticsproceedings.org/rss20/p068.html)의 human affordance | [LAPA](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html), [UniVLA](https://www.roboticsproceedings.org/rss21/p014.html), [LAOM](https://proceedings.mlr.press/v267/nikulin25a.html) | [ViPRA](https://proceedings.iclr.cc/paper_files/paper/2026/hash/707e34efcabd2b9375f7a64019600aa8-Abstract-Conference.html), [VILA](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html), [design/proxy 비교](https://arxiv.org/abs/2608.19613). 단순 영상 사전학습·view invariance·metric 비교는 이미 존재 |
| Contact / estimation | [Visuotactile estimation/control, CoRL 2024](https://proceedings.mlr.press/v270/ferrandis25a.html) | [ForceVLA, NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/8633b46e12cc5f2ee1f05a6ca2c65b38-Abstract-Conference.html) | [ForceVLA2, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html), distillation·alignment·[ContactBench](https://arxiv.org/abs/2610.24512). 센싱 정보와 controller 효과의 조건부 비교가 필요 |
| Navigation / geometry | [CG-SLAM, ECCV 2024](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php) | [NaVILA, RSS 2025](https://www.roboticsproceedings.org/rss21/p018.html), [Splat-Nav, T-RO 2025](https://doi.org/10.1109/tro.2025.3552348) | [VGGT outlier view rejection, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Emergent_Outlier_View_Rejection_in_Visual_Geometry_Grounded_Transformers_CVPR_2026_paper.html). VLA의 의미 목표와 실제 swept volume의 안전은 별개 |
| Long horizon / memory | Generalist policy와 language interface | [VLABench, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf) | [MemoryVLA, ICLR 2026](https://openreview.net/pdf?id=54U3XHf7qq), [RoboMME, ICML 2026](https://proceedings.mlr.press/v306/dai26c.html), [MIKASA-VLA](https://arxiv.org/abs/2610.00604). Memory 설계뿐 아니라 평가도 이미 연구됨 |

## 4. VLA 공백 후보 네 가지

### V1. GAP-CONTACT — 접촉 정보를 언제 실제로 측정해야 하는가?

**질문:** 관측 이력만으로 구별하기 어려운 조건에서, force/tactile 센싱이 필요한 경우와 더 좋은 학습·controller로 충분한 경우를 예측할 수 있는가?

Force fusion·hybrid control·force distillation·tactile-force alignment는 이미 제안됐다. 따라서 센서 추가의 평균 성능 향상을 다시 보이는 것보다, **어떤 개입에 투자해야 하는지 다른 task에서도 예측**해야 가치가 생긴다. 접촉 부위를 못 보는 센서, 입력 경로, timestamp와 controller를 함께 살핀다. [ForceVLA2 공식 근거](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html), [TaF-VLA primary abstract](https://arxiv.org/abs/2601.20321).

최소 비교는 vision/history-only, force-supervised distillation, 실행 중 실측 force/tactile, 단순 compliance/force controller다. 동일 backbone·task·학습량·시간 예산과 정책/하위 controller의 정보 접근을 맞춘다. 동일 조건의 공정 비교가 불가능하면 논문 간 점수를 직접 비교하지 않는다.

**판단:** VLA의 첫 문헌 심화 대상으로 유지. Hardware와 동기화된 센서 log가 주요 자원이며 GPU만으로 충분하지 않다. 기존 관측 가능성·고전 제어의 알려진 설명만 재확인되면 방법 주장을 축소한다. [완전한 비교·중단 조건](../../synthesis/03_manipulation_contact.md#gap-contact-2026).

### V2. GAP-LATENT — 영상 행동 표현의 순위는 물리 조건이 바뀌어도 유지되는가?

**질문:** 시각적으로 좋은 latent action이 새로운 접촉 dynamics나 action decoder에서도 좋은가? 동일 예산에서 visual/semantic 개선과 실제 action/contact supervision 중 어느 것이 필요한가?

이것은 “영상에서 action을 배운다” 또는 “distractor를 제거한다”는 제안이 아니다. [LAOM, ICML 2025](https://proceedings.mlr.press/v267/nikulin25a.html), [VILA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html), [What Matters for Latent Actions](https://arxiv.org/abs/2608.19613)가 직접 비교 대상이다.

**판단:** 조건부 두 번째 VLA 문헌 후보. 기존 empirical study의 held-out 조건과 proxy/decoder 비교를 먼저 대조해야 한다. Representation probe를 control success로 대체하지 않는다. Full pretraining이 필요하면 비용이 커지므로 공개 checkpoint 기반 최소 비교가 가능한지부터 확인한다. 기존 E1과 같은 effect-alignment 질문으로 수렴하면 재명명하지 않는다. [상세 질문](../../synthesis/04_vla_generalist.md#gap-latent-2026).

### V3. GAP-MEMORY — 기억이 부족한가, 실행 방식이 맞지 않는가?

**질문:** 기억해야 하는 시간·정보 유형·action chunk를 독립적으로 바꾸면 어떤 memory 효과가 남는가?

[MIKASA-Robo-VLA §5.3–5.4](https://arxiv.org/html/2610.00604v1)가 실제로 이 confound를 명시하고, [RoboMME, ICML 2026](https://proceedings.mlr.press/v306/dai26c.html)는 memory 설계의 task 의존성을 비교한다. 더구나 [Beyond Success Rate](https://arxiv.org/html/2610.23372v1)가 memory content intervention과 decision/execution 분리까지 제안한다.

**판단:** 분야 질문은 유효하지만 **현재 독립 신규 방법 후보는 보류**. Oracle cue에도 실패하는 task, history leakage, chunk/control 차이를 제거하는 비교부터 필요하다. 새 memory module이나 단순 ablation benchmark를 만들면 선행 반복일 가능성이 높다. [상세 반증 조건](../../synthesis/04_vla_generalist.md#gap-memory-2026).

### V4. GAP-RETENTION — 제대로 구성한 replay 이후에도 남는 문제는 무엇인가?

**질문:** 고정 전체 memory·compute에서 task stream이 달라져도 replay recipe가 충분한지 미리 구별할 수 있는가?

[ICML 2026 forgetting 저항성 연구](https://proceedings.mlr.press/v306/liu26bu.html)와 [real-world continual VLA §5–6](https://arxiv.org/html/2605.26820v1)는 서로 상충한다고 보기 어렵다. 후자도 적절한 replay와 action normalization으로 큰 망각을 완화한다. [PHASER](https://arxiv.org/html/2606.03598v1)는 phase coverage·interference까지 직접 다룬다.

**판단:** 일반 “망각 방지” 방법 주제로는 보류. Normalizer 수정, 충분한 ER, phase-aware replay가 답하지 못하는 **다른 예측**이 있어야 한다. VLM의 언어 능력 보존과 robot motor skill 보존을 섞지 않는다. 여러 task order·seed·backbone의 반복 학습이 필요해 비용도 크다. [상세 조건](../../synthesis/04_vla_generalist.md#gap-retention-2026).

기존 **GAP-DATA**의 재주석/대안 행동/새 시연 선택은 ECT와의 직접 충돌 때문에 보류를 유지한다. 위 13개에 새로운 후보로 다시 세지 않았다. 일반 instruction grounding, skill handoff, action timing도 기존 문헌·D2/D3/E2의 gate를 우회하지 않는다.

## 5. 다른 분야 아홉 질문을 함께 비교

다음은 직전 GAP-W1의 근거를 재사용한 요약이다. 새 본문 정독으로 표시하지 않는다. 각 링크에는 알려진 답, 연구자 질문, 대안, 반증과 자원 조건이 있다.

| 후보 / 분야 | 좁힌 질문 | 대표 근거와 이미 답한 부분 | 현재 판단 |
|---|---|---|---|
| [GEOMETRY / 3D·navigation](../../synthesis/07_robotics_3d_perception.md#gap-geometry-2026) | 지도에서 빠진 장애물과 pose 오차를 구별해 실제 false-free-space 위험을 줄일 수 있는가? | CG-SLAM(ECCV 2024), VGGT(CVPR 2025), Splat-Nav(T-RO 2025), outlier rejection(CVPR 2026). Reconstruction·map-relative safety만으로 실공간 보장을 얻지 못함 | **우선 심화**. Unknown-space/margin baseline으로 충분한지 먼저 확인 |
| [DATA-TRANSFER / ML·robot IL](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026) | Policy A에서 좋은 training subset이 B에서도 좋은 조건은? | Data Scaling Laws·What Matters in Large-Scale Data(ICLR 2025), DataMIL(ICLR 2026). 선택 방법의 존재보다 policy 변경 후 utility 전달이 질문 | **우선 심화**. 선택 비용·data pool·중복·학습 예산을 고정 |
| [SYSID / sim-to-real](../../synthesis/05_world_models_safety.md#gap-sysid-2026) | 재보정할 parameter 오류인가, 빠진 state/model class 오류인가? | SPI-Active(CoRL 2025), online KF(IROS 2025), robust contact control(RSS 2026), ASTRA(저자 RA-L/IROS 2026 표기) | 후속 심화 유지. Delay/history 보정으로 충분하면 축소 |
| [DEFORM / 변형체·inverse physics](../../synthesis/03_manipulation_contact.md#gap-deform-2026) | 같은 형상에서 재질과 고정 조건의 모호성을 task에 필요한 만큼만 해소할 probe는? | JIGGLE(RSS 2024), PGND(RSS 2025), task-level ILC(RSS 2026) | 조건부 유망. 물성/고정 GT와 hardware 필요 |
| [CAUSAL / offline RL](../../synthesis/02_rl_il_offline.md#gap-causal-2026) | Coverage 부족과 숨은 교란을 분리해 policy 선택에 쓸 수 있는가? | Confounded OPE(AISTATS 2024), two-way deconfounder(NeurIPS 2024), confounding-robust RL(NeurIPS 2025) | 이론/진단 후보. Bound가 넓어 결정을 못 바꾸면 실용 주장 약함 |
| [WM / world models](../../synthesis/05_world_models_safety.md#gap-wm-2026) | Planner의 최적화 범위가 바뀔 때 현실 decision 실패를 예측할 수 있는가? | General Agents Need World Models(ICML 2025), environment queries(ICML 2026), Imperfect World Models(2026 preprint) | 조건부. Exploitation 발견 자체는 이미 알려짐 |
| [PLAN / interactive control](../../synthesis/01_planning_control.md#gap-plan-2026) | 상대 반응 모드가 갑자기 바뀔 때 calibration과 진행/안전을 유지할 조건은? | Conformal crowd safety(CoRL 2025), Who Moved My Distribution?(2025 preprint) | 조건부. Predictor·latency·기존 adaptive CP가 대안 |
| [HRI / 협업·multi-agent](../../synthesis/01_planning_control.md#gap-hri-2026) | 사람이 늦거나 틀리게 응답할 때 어떤 도움 형태가 task 성과와 부담에 유리한가? | RCIP(RSS 2024), PARTNR(ICLR 2025), UPS(RSS 2026), LLawCo(ICML 2026) | 참여자/상호작용 데이터 조건부. 단순 clarify 규칙과 비교 |
| [THERMAL / 지속 운용](../../synthesis/06_locomotion_whole_body.md#gap-thermal-2026) | Payload·ambient·task switching 아래 처리량과 열 제약을 함께 유지할 조건은? | Cooling hardware(Humanoids 2025), thermal-aware/residual RL(2026 preprints) | Hardware 확보 전 보존. Derating/rest schedule가 강한 대안 |

대표 primary 근거: [DataMIL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html), [SPI-Active](https://proceedings.mlr.press/v305/sobanbabu25a.html), [PGND](https://www.roboticsproceedings.org/rss21/p036.html), [confounded OPE](https://proceedings.mlr.press/v238/kausik24a.html), [world-model queries](https://proceedings.mlr.press/v306/warrier26a.html), [conformal crowd safety](https://proceedings.mlr.press/v305/yao25a.html), [UPS](https://roboticsproceedings.org/rss22/p142.html). 전체 40건의 source별 status와 본문 구간은 [GAP-W1 ledger](../sources/broad_gap_scout_2026-10-23.json)를 따른다.

### Navigation을 빠뜨리지 않기 위한 연결

NaVILA는 언어/공간의 중간 행동을 locomotion policy로 실행한다. 따라서 “VLA와 low-level RL을 계층으로 결합”하는 방향 자체는 새롭지 않다. [NaVILA, RSS 2025](https://www.roboticsproceedings.org/rss21/p018.html).

Navigation에서 우선 볼 질문은 **VLA가 고른 목표/경로에 대해 지도 누락이 실제 robot footprint·swept volume에서 어떤 실패를 만드는가(GEOMETRY)**, **상대가 ego 행동에 반응할 때 calibrated local decision이 유지되는가(PLAN)**다. High-level language success와 low-level feasibility를 별도 outcome으로 둔다. 이 연결은 연구자 해석이며 NaVILA의 확인된 실패 결과로 주장하지 않는다. 의미 정보가 실제 선택을 바꾸지 않는 setup이면 VLA를 억지로 넣지 않고 navigation/control 문제로 남긴다. Mobile-manipulation handoff로 바뀌면 MoTo·RoboCombine·기존 D2와 대조한다.

## 6. 먼저 검토할 이유와 자원 제약

| 질문 | 연구 가치가 생길 조건 | 가장 먼저 할 비실험 작업 | 이후 필요한 자원 |
|---|---|---|---|
| CONTACT | 다른 task에서 센싱/학습/controller 투자 선택을 예측 | ForceVLA/2·AT/FD-VLA·TaF-VLA·ContactBench의 입력/coverage/rate 비교표 | 동기화 force/tactile·task log, hardware 또는 물리 조건이 명확한 simulator, Docker |
| GEOMETRY | map score가 아닌 실제 collision 판단이 바뀜 | Map-relative guarantee와 unknown-space·pose/scale·GT 정의 비교 | Geometry GT·센서 trajectory·collision evaluator; GPU inference 필요 여부 확인 |
| DATA-TRANSFER | 비싼 subset selection을 다른 learner에서도 재사용할 조건을 밝힘 | DataMIL 등 selection의 learner 의존성·split·compute·episode identity 감사 | 공통 dataset과 최소 두 policy, 반복 fine-tuning GPU |
| SYSID | parameter 조정과 모델 변경 중 선택을 바꿈 | Active ID·history abstraction·classical control의 가정/관측 비교 | Native telemetry·time alignment·dynamics model, 실제 transfer에는 robot |
| LATENT | representation 순위의 전달/역전이 실제 추가 supervision 선택을 바꿈 | 가장 가까운 네 방법의 action label·decoder·proxy·held-out 범위 감사 | 공개 checkpoint/decoder, 적합한 task data; 새 대규모 pretraining은 비용 큼 |

공개 code가 있다는 것, 데이터가 있다는 것, 공정한 실험이 실행 가능하다는 것은 각각 다르다. 지금은 문헌·source interface 비교를 더 진행할 수 있다. 실험 단계에서는 로컬 Docker만 사용하며 GPU 부족을 임의의 host/MPS/cloud 실행으로 우회하지 않는다.

## 7. 다음 buildup과 기존 후보 중복 검사

**다음 TODO는 GAP-R2의 CONTACT 본문/부록/code 비교**다. 추가된 TaF-VLA와 2024 visuotactile estimator/control도 대안에 포함한다. 다음 결과물은 논문마다 policy input, training supervision, low-level sensor access, timing, task/초기화, split, outcome, 공개 자산을 출처 위치와 함께 채운 표다. 빈칸은 추정하지 않는다.

그 표에서 공정한 비교가 가능한 task와 기존 방법과 갈리는 예측이 하나라도 남는지로 **심화 / 진단으로 축소 / 보류**를 판정한다. 현재 요청은 후보 조사이므로 실험 packet 구축이나 본격 학습은 시작하지 않았다. GAP-W2의 GEOMETRY·SYSID·DATA-TRANSFER는 후속 비교로 유지한다. LATENT는 직접 충돌 심사 대기다.

| 현재 질문 | 과거 후보와 겹칠 위험 | 유지할 경계 |
|---|---|---|
| CONTACT | C1 관측 선택, D1 식별 가능성 | 센서 정보와 controller 개입의 필요 조건이 중심. learned selector나 state correction으로 자동 전환 금지 |
| LATENT | E1 effect/embodiment alignment, 초기 RL 전이 | Video representation과 supervision 비용이 중심. 정상 정렬 이후 effect 전이로 수렴하면 E1 gate 적용 |
| MEMORY | C1, E2, RP-3 | 평가 confound의 비교만 남김. selector·chunk method·persistent memory 재개 아님 |
| RETENTION | E1, 초기 robot 간 RL 개선 | task stream의 replay recipe 경계이며 cross-robot transfer 효과 미검증 |
| DATA-TRANSFER | GAP-DATA/ECT, 초기 RL 전이 | 고정 data pool의 subset utility가 learner 변경에 전달되는지 질문. relabel/수집 결정이나 RL gain 전이가 아님 |
| GEOMETRY / SYSID | D1 관측 보정 | 지도 누락/모델 클래스에 대한 진단이며 D1 기존 설계 NO-GO/HOLD 자동 해제 없음 |

이 주제들은 선행의 limitation만으로 선택된 완성된 thesis가 아니다. **문제 근거 → 강한 대안 → 구별되는 예측 → 최소 반증** 순으로 좁힐 후보들이다.

## 8. 이번 source 목록

V-ID는 이번 조사 기록용이다. 정식 registry paper_id가 아니며 등록 여부를 읽기 상태로 해석하지 않는다. PDF 링크는 remote source이며 로컬 PDF를 저장하지 않았다.

| ID | 논문 / 확인 상태 | 확인 깊이 |
|---|---|---|
| V01 | [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) — CoRL 2024 | abstract/공식 색인 중심 |
| V02 | [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) — RSS 2024 | abstract/공식 색인 중심 |
| V03 | [Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation](https://proceedings.mlr.press/v270/doshi25a.html) — CoRL 2024 | abstract/공식 색인 중심 |
| V04 | [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html) — NeurIPS 2024 | abstract/공식 색인 중심 |
| V05 | [HRP: Human affordances for Robotic Pre-training](https://www.roboticsproceedings.org/rss20/p068.html) — RSS 2024 | abstract/공식 색인 중심 |
| V06 | [Latent Action Pretraining from Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html) — ICLR 2025 | abstract/공식 색인 중심 |
| V07 | [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](https://www.roboticsproceedings.org/rss21/p014.html) — RSS 2025 | abstract/공식 색인 중심 |
| V08 | [Latent Action Learning Requires Supervision in the Presence of Distractors](https://proceedings.mlr.press/v267/nikulin25a.html) — ICML 2025 | abstract/공식 색인 중심 |
| V09 | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://www.roboticsproceedings.org/rss21/p018.html) — RSS 2025 | abstract/공식 색인 중심 |
| V10 | [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf) — ICCV 2025 | abstract/공식 색인 중심 |
| V11 | [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://papers.nips.cc/paper_files/paper/2025/hash/8633b46e12cc5f2ee1f05a6ca2c65b38-Abstract-Conference.html) — NeurIPS 2025 | abstract/공식 색인 중심 |
| V12 | [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) — CVPR 2026 | abstract/공식 색인 중심 |
| V13 | [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321) — arXiv 2026 / venue 미확정 | abstract/공식 색인 중심 |
| V14 | [ViPRA: Video Prediction for Robot Actions](https://proceedings.iclr.cc/paper_files/paper/2026/hash/707e34efcabd2b9375f7a64019600aa8-Abstract-Conference.html) — ICLR 2026 | abstract/공식 색인 중심 |
| V15 | [Learning to Act Robustly with View-Invariant Latent Actions](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html) — CVPR 2026 | abstract/공식 색인 중심 |
| V16 | [Vision-Language Models Unlock Task-Centric Latent Actions](https://arxiv.org/abs/2601.22714) — arXiv 2026 / venue 미확정 | abstract/공식 색인 중심 |
| V17 | [What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613) — arXiv 2026 / venue 미확정 | 지정 HTML 구간 |
| V18 | [MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation](https://openreview.net/pdf?id=54U3XHf7qq) — ICLR 2026 | abstract/공식 색인 중심 |
| V19 | [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://arxiv.org/abs/2610.00604) — arXiv 2026 / venue 미확정 | 지정 HTML 구간 |
| V20 | [Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems](https://arxiv.org/abs/2610.23372) — arXiv 2026 / venue 미확정 | 지정 HTML 구간 |
| V21 | [MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](https://arxiv.org/abs/2606.09827) — arXiv 2026 / venue 미확정 | abstract/공식 색인 중심 |
| V22 | [μVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models](https://arxiv.org/abs/2606.12497) — arXiv 2026 / venue 미확정 | abstract/공식 색인 중심 |
| V23 | [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](https://proceedings.mlr.press/v306/liu26bu.html) — ICML 2026 | 지정 HTML 구간 |
| V24 | [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820) — arXiv 2026 / venue 미확정 | 지정 HTML 구간 |
| V25 | [PHASER: Phase-Aware and Semantic Experience Replay for Vision-Language-Action Models](https://arxiv.org/abs/2606.03598) — arXiv 2026 / venue 미확정 | 지정 HTML 구간 |
| V26 | [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html) — ICLR 2026 | abstract/공식 색인 중심 |
| V27 | [VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling](https://openaccess.thecvf.com/content/CVPR2026/html/Li_VLA_Models_Are_More_Generalizable_Than_You_Think_Revisiting_Physical_CVPR_2026_paper.html) — CVPR 2026 | abstract/공식 색인 중심 |
| V28 | [OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation](https://prism.robotics.princeton.edu/publications/omnivla-omni-modal-vision-language-action-model-robot-navigation) — ICRA (author-reported) 2026 | abstract/공식 색인 중심 |
| V29 | [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://proceedings.mlr.press/v306/dai26c.html) — ICML 2026 | abstract/공식 색인 중심 |
| V30 | [Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions](https://proceedings.mlr.press/v270/ferrandis25a.html) — CoRL 2024 | abstract/공식 색인 중심 |

## 9. 저장소 변경과 검증

정식 신규 논문 등록·tier 변경·읽기 상태 승격은 없다. 기존의 1,037편과 CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242를 유지한다. 이전 dirty worktree의 PDF 노트 교정과 문헌 조사 결과를 보존했다.

이번에는 이 보고서·source ledger·VLA/접촉 synthesis·navigation 문서·TODO만 갱신한다. Local PDF·package·실험 container를 만들지 않았고 Git commit/push도 수행하지 않았다. 최종 생성/무결성 검증 결과는 아래에 기록한다.

- 검증: `py_compile`, tier 생성, 전체 repository audit, `git diff --check` 통과. 오류·경고 0.
- Manifest·tier·active/inactive reading CSV의 SHA256이 작업 전과 일치한다. Source ID/title 중복·연도/건수·canonical anchor·registry overview 경로도 확인했다. [검증 기록과 hash](../sources/integrated_gap_review_2026-10-23.json).
