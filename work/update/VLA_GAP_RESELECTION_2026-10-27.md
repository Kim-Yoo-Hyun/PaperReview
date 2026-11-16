# GAP-S2 — VLA 공백 재선별

- Reviewed: 2026-10-27 KST
- 작업: **DONE**. 비실험 문헌·공개 source 심사이며 정책 실행, 설치, 학습, GPU/Docker 점검은 하지 않았다.
- 결과: 세 질문 중 **신규 방법 채택 0개**, 추가 대조할 **조건부 평가 질문 1개**. 그 질문도 `REVISE/HOLD`이며 신규성·효과가 확인된 연구 후보는 아니다.
- 다음: **GAP-TERM1 — 자율 종료 평가의 직접 선행·비교 계약 심사**. 새 stop head나 benchmark 구현에 착수하지 않는다.
- [Source·판정·검증 ledger](../sources/vla_gap_reselection_review_2026-10-27.json) · [canonical 질문](../../synthesis/04_vla_generalist.md#gap-termination-2026) · [TODO](../../TODO.md)

## 1. 범위와 근거 수준

[Buildup guide](../../research/IDEA_BUILDUP_GUIDE.md)의 단계 0–6을 적용했다. 기존 [16개 후보](../research_candidates/summaries/README.md), [GAP-S1](./VLA_GAP_SELECTION_REVIEW_2026-10-24.md), [통합 공백 조사](./INTEGRATED_GAP_REVIEW_2026-10-23.md), 직전 [AUTH4](./VLA_CONTACT_AUTHORIZATION_BASELINE_REVIEW_2026-10-27.md)의 종료·보류 이유부터 대조했다. 방법을 정한 뒤 빈칸을 찾지 않고, 단순 대안과 최신 반례에 따라 질문을 축소했다.

2024–2026 공개 문헌 중 양팔 action 의존성, 암기와 일반화 평가, 종료 판단을 검색했다. 핵심 비교는 **12편: 공식 게재 6편, preprint/제출본 6편**이다. 공식 게재는 RSS 2024, ICLR 2025/2026, ICCV 2025, CVPR 2026을 포함한다. 모든 venue·2024–2026 전체 논문을 전수 조사한 것은 아니다. 2026년에 공개된 ICLR 2027 제출본은 최신 충돌 확인에 포함했으며 accepted paper로 세지 않았다.

12편 중 registry identity가 연결되는 것은 5편이다. 나머지 7편은 조사 ledger에만 기록했다. 이번 작업은 신규 등록·tier/reading status 변경이 아니다. `TwinVLA`, `Echo` 등의 정확한 제목과 distinctive phrase를 기존 manifest에서 대조했다. 공식 abstract 확인, 지정 본문 구간 확인, source 정적 확인을 별도 기록하며 전체 정독으로 표시하지 않는다.

## 2. 근거를 통해 이미 알려진 것

| ID / 논문 | 확인된 status·범위 | 이번 질문에 주는 답과 한계 |
|---|---|---|
| P1 / [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html) | ICLR 2025; 공식 abstract, registry pr-0083 | 양팔의 다봉 action 분포와 공통 action 표현 자체는 이미 연구 대상이다. 이번에 동일 정보·데이터 조건의 모든 ablation을 재검증한 것은 아니다. |
| P2 / [TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html) | ICLR 2026; [v2 §3–4, §5.7–6](https://arxiv.org/html/2511.05275v2) 지정 구간 | 단일 팔 정책 두 개의 joint attention과 양팔 적응이 직접 선행이다. §5.7은 순차적으로 구성요소를 제거하므로 모든 효과를 독립 factorial 인과 효과로 읽지 않는다. |
| P3 / [Diffusion-Based Imaginative Coordination for Bimanual Manipulation](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_Diffusion-Based_Imaginative_Coordination_for_Bimanual_Manipulation_ICCV_2025_paper.html) | ICCV 2025; 공식 indexed abstract·bibliography | 미래 영상과 action의 공동 학습을 통한 협응도 선행이다. CVF 직접 열기는 403으로, 검색에 노출된 공식 내용만 사용했다. 전체 실험표 대조는 하지 않았다. |
| P4 / [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://roboticsproceedings.org/rss20/p133.html) | RSS 2024; 공식 abstract, pr-1046 | 환경 perturbation과 sim–real 연결의 체계적 평가는 기존 문제 설정이다. 새 perturbation 목록만으로 기여가 생기지 않는다. |
| P5 / [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) | CVPR 2026; 공식 indexed abstract·bibliography, pr-1045 | 다양한 perturbation에 대한 VLA 취약성 평가가 이미 있다. CVF 직접 열기 403; 공식 검색 내용과 기존 identity를 대조했다. |
| P6 / [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827) | 2025 preprint, v2 2026-05-25; abstract, pr-1054 | 목표·초기 상태·지시·환경 변화와 암기 문제를 직접 제기한다. 극단적인 성능 저하를 본문 task validity 감사 없이 오염의 증거로 채택하지 않는다. |
| P7 / [Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative](https://proceedings.iclr.cc/paper_files/paper/2026/hash/122ea6470232ee5e79a2649243348005-Abstract-Conference.html) | ICLR 2026; 공식 abstract | 희소 데이터에서 action 재사용이 유용할 수 있고 ALT가 강한 비교 대상이라는 반대 근거다. 모든 VLA가 암기한다는 일반 결론은 아니다. |
| P8 / [ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](https://arxiv.org/abs/2601.16667) | 2026 preprint, v3; abstract, pr-0981 | 시각 실패에도 상태 진행을 따라 완료처럼 행동하는 현상·benchmark·방법이 이미 있다. False completion 일반론을 새 공백으로 삼지 않는다. |
| P9 / [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/html/2608.16172v1) | 2026 preprint; 방법, inference algorithm, evaluation controls, final-state 기준 지정 구간 | Stop과 action-prefix의 공동 선택 및 최종 상태 평가는 직접 선행이다. 공개 README에는 학습·평가 코드가 미공개로 표시되어 본문과 실행 자산을 구별했다. |
| P10 / [Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models](https://arxiv.org/html/2610.31569v1) | 2026-10-22 preprint; §3.2·A.10 지정 구간, simulation source | Stop/failure 차원을 action과 함께 예측한다. A.10의 시뮬레이션 신호는 rollout을 종료하지 않는다. 신호 정확도와 자율 종료 효과를 구별해야 한다. |
| P11 / [SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation](https://arxiv.org/html/2609.32698v1) | 2026 preprint; abstract·Appendix B 지정 구간 | Termination head와 VLM을 공통 trajectory에서 비교한다. Appendix B는 oracle-controlled composite execution이며, 그 감사가 온라인 복합 과제의 효과를 입증하지 않는다고 명시한다. |
| P12 / [Every Failure Is a Timeout: Failure-Mode Homogeneity Makes Robot Policy Evaluators Unverifiable](https://openreview.net/forum?id=8GyKjbTQUd) | 2026 공개, **ICLR 2027 under review**, OpenReview API version 2의 abstract/metadata만 확인 | 종료 길이의 outcome 누출, fixed-horizon logging, achievement/terminal success 차이를 이미 주장한다. 따라서 이 세 가지 자체는 남은 신규성으로 쓰지 않는다. 본문·공개 interface 범위는 미확인이다. |

P12는 discovery index에서 발견한 뒤 공식 [OpenReview search API](https://api2.openreview.net/notes/search?term=Every%20Failure%20Is%20a%20Timeout&limit=3)의 정확한 forum ID로 확인했다. Forum·본문 web 접근은 실패했다. Anonymous 제출본의 저자나 채택 여부를 추정하지 않았으며 index의 acceptance 예측은 근거에서 제외했다.

추가 반례로 [Good AI Labs의 자사 protocol 기록](https://www.goodailabs.com/blog/four-ways-to-grade-the-same-robot/)은 최초 달성·유지·hands-off 평가를 이미 구별한다. Peer-reviewed paper가 아니며 저자 자신도 checkpoint가 달라 점수 차이를 protocol 효과로 귀속할 수 없다고 설명한다. 이 글은 새로운 metric이라는 주장을 피하기 위한 공개 선례로만 사용한다.

## 3. 세 질문의 채택 심사

### A. 양팔의 개별 유효 행동이 결합되면 왜 실패하는가

**질문:** 두 개의 협응 mode가 모두 가능한 장면에서 각 팔의 marginal 예측을 결합하면 서로 모순되는 선택이 생기는가? Joint action 분포를 모델링하면 충분한가?

연구자 사고실험으로, 유효한 joint mode가 `(L1,R1)`과 `(L2,R2)`뿐이고 둘의 확률이 같다면 독립 marginal sampling은 네 조합 중 두 조합을 잘못 짝짓는다. 이 1/2는 설정에서 계산되는 값이며 실제 VLA의 실패율이 아니다. 두 head가 있다는 사실만으로 실제 정책이 conditional independence를 가정한다고 판단해서도 안 된다.

가장 강한 비교는 처음부터 **joint action head**, 공통 latent/mode를 공유하는 decoder, 동일 데이터와 controller를 쓰는 단순 IL이다. 같은 seed만 넣는 것이 유효한 공동 분포를 보장하지도 않는다. RDT·TwinVLA·P3가 이미 다봉 행동과 협응을 다루므로 “두 팔을 연결한다”는 제안은 직접 충돌한다. TwinVLA의 module 제거 결과만으로 marginal mismatch를 별도 원인으로 확정할 수 없다.

**판정: 현재 일반 방법 NO-GO.** 새 mechanism을 채택하려면 joint baseline 이후에도 남는 오류, 서로 다른 mode의 실제 관측·행동 witness, 사전에 정의한 coupling 강도에 따른 차별적 예측이 필요하다. 이번 조사에서는 확보하지 못했다. 이 결과는 양팔 연구 분야 전체의 가치 판단이 아니다.

### B. 높은 VLA benchmark 성적은 암기·데이터 누출인가

**질문:** 엄격한 scene/task/episode split에서 정책의 순위가 유지되는가? 어떤 overlap이 일반화 평가를 왜곡하는가?

세 개념을 분리한다. `학습 trajectory 재사용`, `test 자료의 학습 유입`, `새 조건에서 실패`는 동의어가 아니다. 성공적인 retrieval은 정당한 정책일 수 있고(P7), 성능 저하는 입력 변화·실행 불가능한 목표·데이터 coverage 부족으로도 생긴다. 모델 출력이 지시 교란에 둔감하다는 사실도 곧바로 pretraining contamination을 증명하지 않는다.

필수 단순 대안은 episode/scene/asset 계보의 그룹 split·중복 제거, 의미와 실행 가능성을 보존하는 목표 교환, 동일 관측을 받는 nearest-neighbor/ALT와 BC다. P4–P7의 기존 benchmark·진단 이후 어떤 새로운 deployment 판단이 바뀌는지 먼저 특정해야 한다. 비공개 pretraining corpus의 오염은 registry metadata만으로 식별할 수 없다.

**판정: 일반 robustness/암기 benchmark의 신규 채택 NO-GO.** 오염이라고 이름 붙이는 대신 데이터 계보 확인과 task validity를 선행해야 한다. 현재는 선행 평가를 다른 task에 반복하는 것 이상의 조건부 주장을 확보하지 못했다.

### C. 목표 달성과 스스로 끝내는 능력을 같은 성공으로 보고 있는가

**넓은 방법은 이미 존재한다.** Stop head·진행 신호·false-completion 보정·종료와 chunk의 공동 선택은 P8–P11과 충돌한다. “최초 성공과 최종 성공이 다르다”, “고정 길이로 기록하자”, “종료 시점이 judge에 정답을 누출한다”도 P12와 공개 선례가 있다.

**남겨 둔 질문:** action policy의 가중치·관측·예산을 고정한 상태에서, 공통의 관측 기반 종료기와 각 정책의 native 종료기를 바꾸면 **자율적으로 유효하게 완료하는 정책의 상대 순위**가 달라지는가? 그 차이는 task의 goal 유지 요구·관측 가능성에 따라 예측되며, 단순 threshold·hysteresis·고정 종료 시간 이후에도 남는가?

이것은 새로운 metric이나 stop architecture 제안이 아니다. 정책을 고를 때 reachability 성적만으로 충분한 조건과 종료기까지 함께 평가해야 하는 조건을 구별하려는 **조건부 평가 질문**이다. P12 본문의 동일 비교 여부를 아직 배제하지 못했으므로 신규성은 미확정이다.

**판정: 방법 채택 NO-GO, 좁힌 평가 질문 REVISE/HOLD.** 세 방향 중 추가 대조할 이유가 가장 구체적이지만 주력 연구로 선정하지 않았다. CPU/GPU 부족 때문에 내린 판정이 아니다.

## 4. 공개 source로 확인한 실제 경계

5개 repository revision의 source/doc **10개를 임시로 읽었다**. 실행하거나 import하지 않았다. 일부 파일은 interface 문맥 확인용이며 전체 repository audit가 아니다. Revision·파일 hash·확인 구간은 ledger에 기록한다.

| Source | 확인 구간 | 의미 |
|---|---|---|
| [OpenVLA runner](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/experiments/robot/libero/run_libero_eval.py#L186) | 186–238 | 환경 `done` 뒤 성공을 세고 종료한다. 이 action-policy runner의 평가 계약이며 모든 VLA 구현에 대한 주장이 아니다. |
| [LIBERO step](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/bddl_base_domain.py#L800) | 800–809, wrapper 87–104, tabletop 135–158 | 이 revision의 `done`은 `_check_success()`로 덮어쓴다. Tabletop은 goal predicate의 conjunction을 검사한다. Generic Gym의 timeout semantics를 그대로 대입하지 않는다. 개별 predicate의 안정성 요구는 아직 미감사다. |
| [Echo runner](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/echo/evaluation/evaluate.py#L92) | 92–119, 196–224 | Pending action을 실행하면서 success event와 SS/FS를 저장한다. 신호로 멈추지 않으며 `terminal_success`도 이미 기록한다. 단순히 해당 필드를 추가하는 것은 새 기여가 아니다. |
| [Echo protocol](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/docs/evaluation.md#L52) | 52–60, 92–96, 129–160 | 모든 trial의 고정 horizon continuation, first-event 성공, held signal과 평가 window를 구별한다. 공개 기록을 자율 종료 실험으로 읽으면 안 된다. |
| [SparkVLA release](https://github.com/huhuhushou/SparkVLA/blob/ae90ec94ccc77a1e6745e4f5bcc94e05502d8cbf/README.md#L23) | 17–32 | 이 revision은 training/evaluation/checkpoint 미공개 checklist다. 본문이 존재해도 실행 packet은 별도다. |
| [TwinVLA interface](https://github.com/jellyho/TwinVLA/blob/d632d9378f3dbd7a9a32854d21b1642c6939f1f6/twinvla/model/twinvla.py#L99) | 99–124; action_heads 79–135 | 양 wrist·proprio·instruction 입력과 action 생성 문맥만 확인했다. 이것만으로 전체 twin backbone의 확률 factorization을 판정하지 않는다. |

**Version 차이:** Echo 논문 A.10은 baseline을 최초 성공에 종료한다고 쓰지만, 이번 공개 protocol은 모든 trial을 끝까지 실행한다고 설명한다. Runner도 후자의 loop다. 논문 결과를 현재 source의 재현 결과로 치환하지 않는다. 비교할 때 본문 version·code revision·checkpoint와 logging mode를 각각 고정해야 한다.

**평가 의미:** simulator truth로 종료하는 것은 목표 도달 능력을 측정하는 합법적인 protocol이다. 이를 곧바로 잘못된 평가나 학습 데이터 누출로 부르지 않는다. 자율 종료 능력을 주장할 때 무엇이 추가로 검증되어야 하는지가 질문이다.

## 5. 남은 질문의 반증 가능한 비교 초안

아래는 연구자 설계 초안이다. 구현·fixture·정책 결과가 없다.

`G(s_t)`를 독립 evaluator의 goal truth로 놓는다. 다음을 분리한다.

- **도달:** 동일 horizon 안에서 한 번이라도 `G(s_t)=1`인가.
- **끝 시점 유지:** 선언한 종료 규칙 아래 끝 상태에서 `G`가 성립하는가.
- **자율 완료:** policy-visible 정보로 success를 선언하고, task에 맞게 미리 정한 종료 후 controller/관측 구간에서도 필요한 goal을 유지하는가.

Holding 과제에서 무조건 gripper를 열거나 동력을 끄면 task 자체를 바꾼다. Placement·hold·articulation의 유효 종료 action과 유지 시간은 개별 계약이어야 한다. 동일 물리 시간을 맞추고 추가 query·판정 비용도 센다. Privileged truth는 evaluator/oracle reference에만 둔다.

| 경쟁 설명 | 구별할 비교 / 기각 기준 |
|---|---|
| H1: 행동 정책과 종료기의 결합 때문에 선택 순위가 달라진다 | 최소 두 frozen action policy × 공통 관측 기반 종료기/native 종료기를 교차 비교. Common detector에 단순 threshold와 hysteresis를 포함하고, horizon과 초기 상태·task별 controller를 맞춘다. 순위 변화가 없거나 사전 실용 차이 기준보다 작으면 이 주장을 채택하지 않는다. |
| H0: 충분히 보정한 공통 종료기 하나로 차이가 설명된다 | 같은 observer·라벨·tuning budget의 공통 종료기가 native 방식의 이득을 제거하면 별도 방법을 제안하지 않는다. Fixed deadline도 포함한다. |
| H2: goal 정의·종료 행동·시간 단위가 다른 것이 원인이다 | Predicate·holding/placement 의미·query 전후 시점·latched/current truth를 먼저 맞춘다. 차이가 사라지면 정책의 종료 능력 문제로 해석하지 않는다. |
| H3: 정보 부족으로 성공 여부가 관측 불가능하다 | 같은 허용 관측에서 성공/실패를 구분하는 witness가 없으면 새 head 효과를 주장하지 않는다. 독립 history 관측의 정당성을 먼저 확인한다. |

핵심 예상은 **정책×종료기 interaction이 goal 유지 요구가 다른 조건에서 달라진다**는 것이다. 이는 예측이지 사실이 아니다. 단순한 최초/최종 성공 차이만 관측되면 P12·기존 protocol의 재확인 수준으로 축소한다. 순위 반전만 찾을 때까지 task를 바꾸는 post-hoc 탐색은 허용하지 않는다. 정량 effect threshold·표본 단위·task 선정은 아직 고정하지 않았다.

저장 continuation에서 `어느 시점에 멈췄을 것인가`는 계산할 수 있어도 **실제로 멈춘 뒤의 상태**는 그 trajectory의 반사실이다. 추가적인 동역학·controller 조건 없이 offline prefix 절단을 closed-loop 자율 완료 결과라고 부를 수 없다. 이번에는 그 재분석도 실행하지 않았다.

## 6. 과거 후보를 다시 이름 붙이지 않았는가

| 비교 | 이번 범위에서 제외한 재명명 |
|---|---|
| 양팔 ↔ E1·D2·E2 | 좌표/effect 정렬, grasp–transport planning, latency/chunk 최적화로 바뀌면 기존 gate로 돌린다. Joint dependency만 독립 질문으로 심사했으나 단순 joint baseline 이후 gap 미확보다. |
| 일반화 ↔ DATA-TRANSFER·C6 | 데이터 selector나 통계적 checkpoint selection을 새 benchmark로 포장하지 않는다. 이번에는 contamination을 입증하지 않았다. |
| 종료 ↔ C4·C5·RP-2·D3 | Reward-label audit, reset 효율, recovery option 학습, 비가역 사건 뒤 지시 변경을 제안하지 않는다. 고정 지시의 evaluation stop contract만 남긴다. |
| 종료 ↔ E2·AUTH | Horizon 적응이나 목표 보호 guard를 제안하지 않는다. 외부 성공 판정기의 성능 향상 자체도 이미 선행이 있다. |

기존 모든 HOLD/NO-GO/RETIRED와 DATA-TRANSFER N3, AUTH-R1의 새 증거 gate를 유지한다.

## 7. 다음 TODO와 중단 조건

**GAP-TERM1의 목적은 연구 후보 승격 여부를 결정하는 비실험 심사**다. 이번 질문을 기정사실로 두고 설계 문서만 늘리지 않는다.

1. P12 본문의 공개 primary text/interface, Echo와 SEES의 평가 조건을 직접 비교한다. P12의 본문을 확보하지 못하면 `ABSTRACT_ONLY` 경계를 유지하고 신규성을 미확정으로 둔다. PDF local cache·dataset payload를 내려받지 않는다.
2. 현재 확인된 두 runner의 `success/current goal/declared stop/horizon`을 구별하고, placement와 holding 등 task 의미가 다른 최소 비교의 predicate·controller 계약을 실제 source에 연결한다. 명목상 두 과제가 있다는 이유로 feasible witness로 승격하지 않는다.
3. 같은 정보·라벨·tuning/시간 예산의 공통 detector·hysteresis·fixed deadline 이후 남을 예측과 필요 artifact를 한 장에 고정한다. P12가 같은 policy×stop 비교까지 다루거나 남는 차이가 단순 metric 변경뿐이면 **독립 후보 미선정으로 종료**한다. 접근 불가 source를 반복 조회하거나 GPU 확보로 우회하지 않는다.

이 단계 이후에만 질문의 연구 가치와 실행 자격을 다시 판단한다. 현재 자율 종료 성능·순위 변화·새 방법의 이득은 전부 미측정이며 외부 연구자 피드백도 없다.

## 8. 저장소 검증

`py_compile`, tier builder, `git diff --check`를 통과했고 repository audit는 오류 0·경고 0이다. Registry 1,072편·표준 노트 5,360개·active/history tracker 344/47행과 CORE 47·NEXT 297·REFERENCE 486·ARCHIVE 242를 유지했다. Canonical 6파일의 hash, 작업과 무관한 기존 dirty 634파일, 기존 missing 10경로를 보존했다.

기존 수동 문서 9개를 갱신하고 이 report와 ledger 2개를 추가했다. 임시 source/doc 10개와 metadata 3개는 hash 기록·확인 후 삭제했다. PDF·weights·dataset 저장, 연구 코드 실행·설치, 새 registry 등록과 reading 상태 승격은 없다. 세부 결과는 [ledger](../sources/vla_gap_reselection_review_2026-10-27.json)의 `validation`에 있다.
