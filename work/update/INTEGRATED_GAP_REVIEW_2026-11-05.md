# 기존·신규 VLA 연구 후보의 통합 공백 검토

- Date: 2026-11-05 KST / Work ID: GAP-INTEGRATED-R1 · REG-R9
- **현행 순위 안내 — 2026-11-07:** 아래 결론은 당시 8개 질문(CROSSPLAY 포함)의 비교다. UNIFIED 추가 후 현행 **8개 주제**의 투자 판정은 [통합 index](../research_topics/README.md#candidate-priority)를 따른다. 아래 문헌·실험·등록 이력을 소급 변경하지 않는다.
- Follow-up: **2026-11-06 GAP-INTEGRATED-N2 완료** — [학습 계보·추정 대상·재사용 판단](#integrated-n2). 앞의 11/05 등록·검증 수치는 당시 기록이며 이번에는 논문을 추가하지 않았다.
- 다음 작업의 완료 위치: [11/06 GAP-FEEDBACK-P0-PREP](../research_topics/visual_feedback/재현%20방법/README.md#preparation-history). 아래 N2 종료 시점의 미생성 기록은 역사로 보존한다. 이후 adapter/recipe 초안을 만들고 CPU 제어 검사만 수행했으며 native 검증은 미완료다.
- 범위: 기존 6개 주제와 새 FEEDBACK·CROSSPLAY 질문 **8개를 함께** 검토했다. 과거 16개 종료·보류 후보는 중복 경계를 확인했으며 전체 실험을 재심사하거나 자동 재개하지 않았다.
- 결론: **VLA+RL 중심의 주 탐색은 기존 residual 재적응, 비교 진단은 새 feedback 질문**이 적합하다. VLA 단독 대안으로 부분 지시 수정, 장기 전략 후보로 독립 partner 협력을 남긴다. 방법 GO·효과·논문 채택 가능성은 미확정이다.
- [등록 입력·source 범위](../sources/registry_admissions_2026-11-05.json) · [직전 외부 조사 원장](../sources/vla_rl_new_gap_scan_2026-11-05.json) · [기존 RL 비교 42편](../sources/vla_rl_gap_review_2026-11-03.json) · [6개 주제 원문](../research_topics/README.md)

## 1. 검토 기준과 검색 범위

사용자의 석사 연구 목표에 맞춰 **기여의 명확성·VLA+RL 적합성·행동상 중요성·구현 부담**을 함께 봤다. 문서 준비도가 높은 후보를 과학적으로 더 좋다고 보거나, GPU가 없다는 이유로 가설을 기각하지 않았다. 이미 알려진 방법이 있다는 사실은 구체적인 질문을 좁히는 근거이며 탐색 자체의 금지가 아니다.

2024–2026의 기존 OpenVLA·world-model/robot-learning 기반과 NeurIPS·CoRL·ICML·ICLR·RSS 등 공식 문헌을 이어 보았다. 이번 추가 확인은 후보별 직접 충돌과 최신 버전에 집중했다. CVPR/ICCV/ECCV/ICRA/IROS/journal 전체를 전수 검토한 결과는 아니다. 검색에는 residual base-policy transfer, instruction revision/constraints, retrieval interference, counting, cooperative VLA와 action tokenization을 사용했다. 최신 preprint는 채택 여부와 관계없이 선행 충돌 근거에 포함했다.

구체 claim마다 아래 공식 URL·원문 절을 연결한다. 새 등록 12편 중 **9편은 지정 본문 절, 3편은 공식 abstract**를 확인했다. Full-text 표시는 전체 정독·수식 증명·source code 전체 감사가 아니다. 새 구현을 제안하기 전 필요한 상세 code/interface 감사는 다음 비교에서 수행한다.

## 2. 같은 기준으로 비교한 8개 질문

| 후보 | 이미 해결·제안된 부분 | 아직 검증할 가치가 있는 좁은 질문 | 강한 단순 대안 / 설명 | 통합 판단 |
|---|---|---|---|---|
| **VRL: base 업데이트 후 residual 재적응** | Frozen VLA+residual, residual 데이터로 base 개선, base/editor 공동 학습, 여러 backbone으로 같은 residual 이식 | 독립적으로 좋아진 B 위에서 A용 residual의 과거 경험이 **교체 이후 추가 비용**을 줄이는 조건; B의 새 능력을 해치지 않는가 | B 단독, scalar gain, warm/fresh residual, Q-filter, 같은 데이터 성공 BC·return-weighted imitation | **VLA+RL 주 탐색 유지.** 기존 질문이 새 두 질문 때문에 밀릴 이유는 없음. 초기 조작 native 0·residual 유용성 미확인 |
| **FEEDBACK: RL과 유효 시각 피드백** | RL의 이동 물체 일반화, activation/attribution 진단, nuisance 정규화와 semantic calibration | 같은 data/control 조건에서 RL 변화가 운동 능력·nuisance 억제와 별개로 **새 관측을 이용한 회복**을 바꾸는가 | Clean competence, normalizer 차이, 더 많은 데이터, BC/weighted BC, 단순 augmentation | **비실험 비교 진단 우선.** 새 loss부터 만들지 않음. 공개 RL/SFT 차이만으로 RL 인과효과를 주장할 수 없음 |
| **REVISION: 부분 지시 수정** | Task/관계/순서 변경, instruction steering, How-level 반응 평가 | 여러 수정에서 **변하지 않은 제약의 유지와 명시적으로 철회된 제약의 해제**를 동시에 달성하는가 | 전체 history 재작성 H, 규칙 R, 정답 완전 지시 O, atomic 능력 A | **VLA 단독 대안 중 우선.** Broad instruction following 기여는 부족; joint outcome에서 H/R 이후 남는 현상이 필요 |
| **CROSSPLAY: 독립 partner 협력** | 분산 협력·상대 반응·VLA multi-agent RL, MARL zero-shot coordination/population training | 능력·관측을 맞춘 독립 VLA partner 사이에서 RL co-adaptation의 호환성 비용이 생기는가 | 역할 prompt, ready signal, 동일 가중치, population/FCP/Other-Play | **전략 후보.** 질문은 의미 있지만 VLA에 MARL 적용만으로 신규성 부족; 단일 양팔 task도 학습·분기 비용 큼 |
| **HANDOFF: 모바일 종료 조건 전이** | Navigation/manipulation 통합과 관측 종료 상태에 맞춘 downstream 적응 | 같은 실제 도착 상태들의 유용성 순위가 frozen A/B 교체 후 유지되며 작은 재선택이 이득인가 | 공통 geometry 규칙, B의 전반 competence, 동일 종료 선택, state 정렬 | **조건부 시스템/평가 후보.** 앞단·뒷단 interface는 중요하나 native transport·전체 state 분기와 환경 범위 부담이 큼 |
| **SET: 집합·수량 지시** | Counting·참조·조합 일반화 benchmark와 장기 기억 평가 | 기본 pick 능력 아래 exactly-k 선택 실패가 수량 해석인가, 진행 상태 유지인가 | 같은 정책의 k회 반복 R, 외부 counter, atomic/정답 reference | **작은 평가 예비.** 직접 D/R로 의미 있는 차이를 먼저 관측; 새 counting benchmark나 RL 의무 결합은 근거 약함 |
| **RETRIEVAL: bank 확장** | Task adaptation·semantic retrieval·cross-task 도움/간섭·selector 비교 | Target bank 고정 시 새 donor의 이득을 보존하면서 goal conflict를 막는가 | Goal partition, random retrieval, 동일 top-k/token, reference provenance | **낮은 우선의 조건부 진단.** Partition 이상의 도움을 보여야 독립 방법 가치가 생김 |
| **CODEC1: 실행 prefix 복원** | Reconstruction과 control 불일치·예측 가능성·token 오류·H/실행 길이 비교 | 고정 rate/H/normalizer에서 prefix metric이 실제 설정 선택을 바꾸고 행동상 이득을 주는가 | DCT/양자화 성질, token prediction 오류, control/replanning 효과 | **자료·평가 후보 보존.** 기존 CPU 결과는 독립 방법 지지 부족; GPU만 확보하면 해결되는 문제가 아님 |

위 순서는 논문 성공 확률의 수치화가 아니다. 자원 조건을 제외한 흥미와 석사 기간의 검증 부담을 같이 고려한 선택이다. VRL과 FEEDBACK을 한 방법으로 즉시 합치지도 않는다. 먼저 같은 checkpoint·관측·행동 계약을 재사용할 수 있는지만 판단한다.

## 3. 이번에 더 엄격히 대조한 직접 선행

### 3.1 VRL·FEEDBACK·REVISION의 공통 경계

[FIRe project](https://rcilab.khu.ac.kr/FIRe/)는 **동일 residual**의 GR00T·π0.5·OpenVLA 전이를 명시한다. 힘·상대 pose를 이용한 contact correction이라는 범위와 RA-L 제출·paper/code coming soon 상태를 함께 기록한다. 논문/코드가 없다고 이 선행을 무시하지 않지만, 아직 registry의 완전 paper entry로 등록하지 않았다. “여러 VLA에 적용 가능”은 VRL의 새 기여가 아니다.

[BAS-VLA §4–5·A.2.1](https://arxiv.org/html/2609.23650v1)는 task-preserving 변화와 semantic-breaking 변화를 구별하는 frozen-policy residual calibration을 제안한다. Object 교체만 아니라 destination·spatial relation·subgoal order도 평가한다. **Break 감소와 새 목표 성공을 분리**하며 New/Old/Other 결과를 별도로 보고한다. 따라서 “변화를 감지해 다른 행동을 한다”는 REVISION이나 “관련 변화에 반응·무관 변화에 불변”이라는 FEEDBACK의 넓은 설명은 새롭지 않다. REVISION은 다중 수정 이력의 유지/철회 공동 기준, FEEDBACK은 **학습 방식과 정보 가용성의 상호작용**으로 좁힌다. 읽은 절에서 이 좁은 비교가 확인되지 않았다는 뜻이며 문헌 전체에 없다고 증명한 것은 아니다.

[Not All Features v6 §4.7–4.8](https://arxiv.org/pdf/2603.19233v6)의 activation 주입 결과를 정상 정책의 관측 무시로 확대하지 않는다. 이동한 물체를 non-injected 정책은 추적한다. [VLA-Trace §3](https://arxiv.org/html/2605.30117v1)의 VLM→VLA→task-finetuned 비교도 RL/SFT matched 비교와 다르다. [Embodied Interpretability](https://proceedings.mlr.press/v306/zhang26gz.html)의 attribution은 유용한 진단이지만 abstract만으로 실제 feedback return의 대체 지표라 확정하지 않는다.

[RobustVLA Algorithm 1](https://arxiv.org/html/2511.01331v2)의 smoothness는 시간상 인접 행동 차분이 아니라 **reference policy 대비 mean action 변화**를 제약한다. 단순 관측 민감도 억제는 이미 선행이다. FEEDBACK에서 저민감도를 무조건 좋은 것으로 놓으면 새로운 연구 질문을 잃는다.

[RL4VLA README Evaluate](https://github.com/gen-robot/RL4VLA)는 warmup/RL/SFT checkpoint를 제공하지만 warmup/RL과 SFT의 unnorm_key가 다르다. Mid-episode reposition도 이미 평가한다. 세 모델 성공률 차이는 탐색에는 쓸 수 있으나 같은 데이터·interaction·normalizer를 확인하기 전에는 RL 효과 추정이 아니다. Native 코드 실행이나 weights 다운로드는 하지 않았다.

### 3.2 기존 나머지 후보를 낮추거나 유지한 이유

- **HANDOFF:** [ActiveAlign §III–V](https://arxiv.org/html/2610.23378v1)는 viewpoint 종료 상태에 맞춰 VLA를 재학습하고 matched-state/data-matched 대조도 둔다. “초기 분포가 중요하다”는 새 관찰이 아니다. 기존 Mobi-π·MoTo와 함께 봐야 한다. 남는 질문은 frozen A/B의 **동일 도착 상태 비교와 제한된 재선택 가치**다. 기존 한 scene template의 2/4/4 역할 분할은 독립 장면 일반화를 입증하지 못한다.
- **SET:** [Spa-Bench §III·V](https://arxiv.org/html/2610.12696v1)는 counting을 이미 포함한다. ClevrSkills·VLABench·RoboMME와의 경계는 기존 dossier에 유지한다. 현재 질문은 quantity benchmark 추가가 아니라 D/R 대조에서 선택/참조/진행/운동 중 어떤 병목이 남는지다. D/R이 같아도 유용한 진단일 수 있지만 그 결과 하나만으로 top-tier 기여라 주장하지 않는다.
- **RETRIEVAL:** [When Does Retrieval Help §3·D](https://arxiv.org/html/2610.05492v1)는 random 포함 selector와 다른 task 시연의 도움을 이미 비교한다. 원 RICL의 distance interpolation을 빼고 공통 buffer를 사용하므로 원 RICL 전체 결과로 합치지 않는다. 새 [RA-VLA 공식 ICML abstract](https://proceedings.mlr.press/v306/jang26c.html)는 retrieval과 grounded execution을 결합한다. 그 상세 bank 실험은 본문 추가 확인 전 부재를 주장하지 않는다. 기존 성공 시연 provenance와 평가 중복 문제는 GPU와 독립적인 미완료다.
- **CODEC1:** [ProAct §4·Appendix C.3](https://arxiv.org/pdf/2610.09170v1)는 reconstruction만 아니라 H/실행 길이와 tokenizer-free flow policy 대조까지 한다. FAST/OAT/FASTer와 함께 가장 강한 충돌이다. 남은 prefix-metric selection 질문은 좁으며, 기존 20 episode·101 window의 CPU 진단이 그것을 입증하지 않는다.

### 3.3 CROSSPLAY를 바로 1순위로 올리지 않은 이유

[CHORUS §4.2](https://arxiv.org/html/2606.12352v1)는 scripted partner 움직임에 대한 반응을 이미 평가한다. [Cooperative VLA RFT §5·C.1](https://arxiv.org/html/2609.36588v1)는 shared third-person RGB를 추가하므로 CHORUS local-only 조건과 동일하지 않다. 팀원 교체의 효과를 보고 싶다면 이 관측 차이를 먼저 없애야 한다. [LatentToM, CoRL 2025](https://proceedings.mlr.press/v305/he25a.html)의 실패·지연 대응도 선행이며 generic reactivity는 새 질문이 아니다.

독립 학습 partner 문제는 [Other-Play](https://proceedings.mlr.press/v119/hu20a.html)·[Fictitious Co-Play](https://papers.neurips.cc/paper_files/paper/2021/hash/797134c3e42371bb4979a462eb2f042a-Abstract.html)부터 존재한다. [HOLA](https://arxiv.org/abs/2607.04972), [MATE](https://arxiv.org/abs/2610.06025), [inter-seed/cross-implementation 연구](https://arxiv.org/abs/2608.03644)도 예비 원장에 남겼다. VLA의 언어·시각 prior가 기존 population training을 넘어 어떤 관습의 호환성을 제공하는지 보여야 기여가 선명해진다. 이 범위는 아직 방법 구축 전이며 숨은 partner 의도 label을 무료로 주는 비교를 피한다.

추가 artifact 대조: [LatentToM 공식 code README](https://github.com/StanfordMSL/LatentToM)도 shared third-person view 설정과 별도 camera 설정을 나눈다. Decentralized라는 이름만으로 정보 접근권이 같다고 간주하지 않는다. 공개 repository와 project를 registry에 연결했으며 실제 실행은 하지 않았다.

## 4. 과거 후보와의 관계

| 과거 축 | 새 근거가 주는 변화 | 이번 판단 |
|---|---|---|
| D1 관측 오류/실제 변화, C1 관측 선택 | BAS-VLA·RobustVLA는 넓은 calibration/robustness 동기를 더 좁힘 | FEEDBACK을 D1 방법의 이름 변경으로 재개하지 않음. RL 후학습의 행동 정보 사용이라는 다른 추정 대상을 조사 |
| C2 manner·D3 비가역 instruction | BAS-VLA·How-level은 지시 변경 범위를 넓힘 | REVISION의 유지/철회 질문과 D3 event/continuation gate를 구별. D3 gate 해제 없음 |
| E1·초기 cross-embodiment RL transfer | FIRe의 residual 이식은 새 직접 선행이지만 초기 후보의 data/control 혼입을 해소하지 않음 | VRL 첫 범위는 같은 robot/controller의 독립 base update. 과거 전이 GO로 읽지 않음 |
| C3·E2 action/time | ProAct가 H/실행 길이와 표현의 관계를 이미 비교 | CODEC1 자료는 보존; generic codec/control mismatch로 재출발하지 않음 |
| C4·GAP-WM | [DRILL](https://arxiv.org/html/2610.30814v1)이 policy utility objective를, [Trusting Imagined Futures](https://arxiv.org/abs/2611.04873)가 imagined reward audit를 직접 제안 | World-model utility/audit라는 broad idea만으로 새 후보를 추가하지 않음 |
| 나머지 C5/C6/D2/RP-2/RP-3 등 | 이번 조사는 해당 gate를 해제할 새 비교 증거를 얻지 못함 | [16개 요약](../research_candidates/summaries/README.md)의 판정 유지. 문헌 전체 재심사 완료라는 뜻 아님 |

## 5. 11/05에 정한 비실험 작업과 판단 분기

**GAP-INTEGRATED-N2:** VRL·FEEDBACK의 학습 계보/추정 대상 비교표 하나를 기존 주제·공통 source에 통합한다.

1. 기존 VRL A/B 계약과 RL4VLA warmup/SFT/RL source에서 base revision, 학습 데이터·목적함수, action/normalizer, observation·control rate를 대조한다. 이미 확인한 metadata를 재수집하는 대신 **어떤 비교가 data-matched인지 아닌지** 표시한다.
2. VRL의 효과는 B 단독 대비 transfer gain과 동일 추가 budget의 fresh residual 대비 이득을 구분한다. A 학습의 매몰 비용과 반복 base update에서의 총비용도 각각 표시한다. 실패하면 gain/BC로 충분한지 판단한다.
3. FEEDBACK은 각 checkpoint 안의 물리 변화×fresh/stale 관측 차이를 먼저 정의한다. 정상 조건의 stale penalty를 빼는 상호작용과 background-only 대조를 두고, 모델 간 차이는 탐색적 연관으로 한정한다. Frozen image 자체의 OOD 효과 때문에 동일 snapshot query 진단과 실제 rollout 성능을 구별한다.
4. 두 질문이 같은 data/adapter를 안전하게 공유할 수 있으면 진단 준비를 재사용한다. 불가능하면 억지로 융합하지 않는다. 작은 탐색에는 동일 데이터 재학습 완료를 선행 요구하지 않지만 **RL의 인과효과 주장에는** 필요하다.
5. 비교가 완성되면 새로운 문서 반복 대신 최소 pilot 또는 외부 검토로 넘어간다. 실제 외부 피드백은 아직 미수신이다. 실행 요청 시 AGENTS의 local Docker GPU 점검과 최소 실행 규칙을 적용한다.

학습 효과의 방향과 새 loss는 미리 정하지 않는다. 본 작업은 공백 재검토·registry 등록 완료이며 8개 후보의 buildup/실험을 전부 완료했다는 뜻이 아니다.

**11/06 인계:** 위 다섯 항목의 비교 검토는 [§8](#integrated-n2)에서 완료했다. 다음은 작은 관측 개입의 실행 준비이며 같은 계보 조사 반복이 아니다.

## 6. Registry 반영

**1,098 → 1,110편**, 새 표준 노트 **60개**. CORE 47 / NEXT 332 / REFERENCE 489 / ARCHIVE 242, 집중 읽기 379 / history 47. 공식 확인된 학회 7편(NeurIPS 3, ICML 2, CoRL 1, EMNLP 1), preprint 5편이다. NeurIPS는 공식 program의 채택 제목을 확인했으며 proceedings 최종 출판 완료를 뜻하지 않는다.

| ID | 논문 | 등록 venue | Tier | 확인 범위 |
|---|---|---|---|---|
| pr-1099 | [BAS-VLA](../../2026/NeurIPS/2026_NeurIPS_Beyond-Appearance-Shifts-Task-Semantic-Action-Calibration/01_overview.md) | NeurIPS 2026 | NEXT | 지정 본문 절 |
| pr-1100 | [Action Atlas](../../2026/NeurIPS/2026_NeurIPS_Not-All-Features-Are-Created-Equal-A-Mechanistic-Study-of/01_overview.md) | NeurIPS 2026 | NEXT | 지정 본문 절 |
| pr-1101 | [Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models](../../2026/ICML/2026_ICML_Embodied-Interpretability-Linking-Causal-Understanding-to/01_overview.md) | ICML 2026 | NEXT | 공식 abstract |
| pr-1102 | [RobustVLA (reinforcement post-training)](../../2025/arXiv/2025_arXiv_RobustVLA-Robustness-Aware-Reinforcement-Post-Training-for/01_overview.md) | arXiv 2025 | NEXT | 지정 본문 절 |
| pr-1103 | [LatentToM](../../2025/CoRL/2025_CoRL_Latent-Theory-of-Mind-A-Decentralized-Diffusion-Architectu/01_overview.md) | CoRL 2025 | NEXT | 공식 abstract |
| pr-1104 | [CHORUS](../../2026/arXiv/2026_arXiv_CHORUS-Decentralized-Multi-Embodiment-Collaboration-with-O/01_overview.md) | arXiv 2026 | NEXT | 지정 본문 절 |
| pr-1105 | [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](../../2026/arXiv/2026_arXiv_Cooperative-Multi-Agent-Vision-Language-Action-Models-via/01_overview.md) | arXiv 2026 | NEXT | 지정 본문 절 |
| pr-1106 | [DRILL](../../2026/NeurIPS/2026_NeurIPS_DRILL-Training-World-Models-to-Improve-Policies-Not-Predic/01_overview.md) | NeurIPS 2026 | NEXT | 지정 본문 절 |
| pr-1107 | [RA-VLA](../../2026/ICML/2026_ICML_RA-VLA-Retrieval-Augmented-VLA-for-Test-Time-Adaptation/01_overview.md) | ICML 2026 | NEXT | 공식 abstract |
| pr-1108 | [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](../../2026/arXiv/2026_arXiv_When-Does-Retrieval-Help-A-Study-of-In-Context-Adaptation/01_overview.md) | arXiv 2026 | NEXT | 지정 본문 절 |
| pr-1109 | [ProAct](../../2026/arXiv/2026_arXiv_Beyond-Reconstruction-What-Matters-in-Action-Tokenization/01_overview.md) | arXiv 2026 | NEXT | 지정 본문 절 |
| pr-1110 | [VLA-Trace](../../2026/EMNLP/2026_EMNLP_VLA-Trace-Diagnosing-Vision-Language-Action-Models-through/01_overview.md) | EMNLP 2026 | REFERENCE | 지정 본문 절 |

중복 검사에서 ActiveAlign은 기존 등록이어서 추가하지 않았다. FIRe는 project-only·paper/code 미공개여서 source 비교에만 남겼다. HOLA/MATE/TIF 등은 이번에는 원장에 보존한 인접·충돌 근거로 유지하며 모두 등록해 수를 채우지 않았다. CHORUS의 CoRL 저자 표기와 ProAct의 저자 NeurIPS 표기는 공식 exact acceptance 확인 전 registry venue로 승격하지 않았다. VLA-Trace는 이번 [공식 EMNLP](https://aclanthology.org/2026.emnlp-main.2076/) 확인으로 등록했다.

신규 NEXT 11편은 모두 사용자 status UNREAD이며 source evidence와 분리했다. 기존 사용자 읽기 입력·dirty tree·staged index·PDF·실험 결과는 보존한다. 새 host 설치·PDF/weights/assets 다운로드·실험·외부 발송·commit/push는 없다.

## 7. 검증

- 등록 dry-run: 13개 최초 후보 중 ActiveAlign 기존 중복 1개 제외. 최종 12개는 title/identifier 충돌 0으로 등록했다.
- Generator compile·재생성 및 priority reconciliation 수행. 생성된 현재 합계는 위 snapshot과 일치한다. 등록 후 신규 12편의 note-derived profile만 갱신하고 기존 profile은 보존했다.
- Repository audit: **1,110 paper / 5,550 notes / 379 active / 47 history / 5,758 Markdown / 12,000 links**, 오류 0·경고 0. Comparison matrix의 기존 completed 5행을 보존했다.
- 전체 5,550개 표준 노트의 C0/C1 제어문자 검사: 잔여 0. 새 12개 폴더는 표준 노트 60개·PDF 0개다.
- 기존 active 368행·history 47행의 status, evidence, 날짜와 사용자 분석 필드: **차이 0**. 신규 NEXT 11행은 UNREAD다.
- 작업 시작 snapshot 대비 기존 파일 변경은 관련 문서·생성 view·registry·generator **30개**에 한정됐다. 기존 파일 삭제 0, 기존 paper note 변경 0. Git staged binary diff는 시작 시점과 동일하다.
- `git diff --check` 통과. Host package/weights/assets 설치·정책 실험·외부 전송은 수행하지 않았다.

<a id="integrated-n2"></a>

## 8. 11/06 학습 계보·추정 대상 대조 — GAP-INTEGRATED-N2

**결론:** VRL은 주 탐색으로 유지하고 FEEDBACK은 별도 비교 진단으로 준비한다. 두 실험의 정책 adapter·경험 데이터는 직접 공유할 수 없다. 공통으로 재사용할 것은 revision/hash 기록, 비용 계수, 관측 시각·행동 기록 형식이다. 공개 checkpoint로 현상을 탐색할 수 있으나 **RL 목적함수만의 효과**, **과거 데이터 접근 자체의 가치**는 현재 비교가 식별하지 못한다. 이 한계를 첫 탐색의 금지 조건으로 쓰지는 않는다.

확인 범위는 SimpleVLA-RL 저자 v1 §3–4.1·5.1, RL4VLA 저자 v4 §3–5·A.1–A.4, 고정 code와 작은 HF metadata다. 최종 학회 본문과 모든 release가 동일하다고 가정하지 않는다. RL4VLA paper v4는 2026-01-14, 공개 code HEAD는 2025-08-25, checkpoint 3개는 2025-06-14에 갱신된 자료이므로 v4의 추가 실험 전부를 이 weights로 재현한다고 쓰지 않는다. 파일별 URL·SHA256와 확인 경계는 [공통 source의 `integrated_n2_review`](../sources/vla_rl_new_gap_scan_2026-11-05.json)에 통합했다. Weights·PDF·assets는 받지 않았고 외부 코드는 텍스트로만 확인했다.

### 8.1 학습 계보와 데이터가 같은 비교의 범위

| 항목 | VRL의 SimpleVLA-RL A → B | FEEDBACK의 RL4VLA warmup → SFT / RL |
|---|---|---|
| 공개 계보 | A: LIBERO-10 task당 1 trajectory SFT, B: 그 설정의 후속 online RL로 저자 설명. **정확한 A SHA에서 B를 학습했다는 run 증명 없음** | Warmup: OpenVLA에서 Octo-Small·motion planner 140 trajectory. SFT와 RL card 모두 warmup repository를 parent로 표기하나 **parent SHA·run/data hash는 없음** |
| 후학습 데이터 | RL의 새 interaction이 들어가므로 A/B 자체는 data-matched 아님. 선택된 B의 정확한 rollout 목록·총량은 미확인 | SFT card: motion-planner 16k trajectories; RL card: 약 1.5M environment steps. 시연 episode 수와 interaction step 수는 같은 단위가 아님 |
| 목적함수 | 수정 discrete head의 action-token CE SFT → binary outcome GRPO, KL 제거·dynamic sampling. 이는 저자 본문 방법이며 선택 B의 exact run flag 확인과 구별 | SFT action-token CE → RL은 PPO/GAE·shared value head. Code 기본 LoRA rank 32, PPO epoch 1. 공개 SFT·RL은 같은 데이터·같은 optimizer budget의 대조군이 아님 |
| 우리가 변경할 것 | Base A/B를 동결하고 **residual**의 초기화·anchor·학습 방식을 비교 | 먼저 공개 정책을 동결하고 **관측 제공 방식**을 바꿈. 이후 matched-data 학습은 별도 단계 |
| 현재 가능한 해석 | 배포 checkpoint 교체 후 residual 적응의 조건부 비교. B가 실제 더 좋은지는 native 평가 필요 | 각 checkpoint의 정보 개입 효과와 모델 간 연관. RL 학습이 그 차이의 유일 원인이라는 해석은 불가 |

근거: [SimpleVLA-RL §3–4.1·5.1](https://arxiv.org/html/2509.09674v1), [고정 B card](https://huggingface.co/Haozhan72/openvla-oft-libero10-traj1-rl/blob/d44ac12c3431fc1d2a4579d2e768bbeba60054d4/README.md), [RL4VLA warmup card](https://huggingface.co/gen-robot/openvla-7b-rlvla-warmup/blob/735fd5d1f4472c4c9f3f998f0e89aa641af5ad03/README.md), [SFT card](https://huggingface.co/gen-robot/openvla-7b-rlvla-sft_16k/blob/cda67bb9cf33bc87cb8bf715572ae0c44e98f8ae/README.md), [RL card](https://huggingface.co/gen-robot/openvla-7b-rlvla-rl/blob/93c54b036cc90ee394731fc73788406d7e65f057/README.md), [RL4VLA method](https://arxiv.org/html/2505.19789v4).

데이터 재현의 별도 주의점도 확인했다. 고정 [warmup builder L80–85](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/openvla/rlds_dataset_builder/warmup_dataset/warmup_dataset.py#L80)는 출처마다 train 70·val 5를, [SFT builder L76–81](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/openvla/rlds_dataset_builder/sft_dataset/sft_dataset.py#L76)는 train 16,384·val 16을 설정한다. 반면 checkpoint config의 통계 count는 warmup 146·SFT 16,424다. 통계 집계 범위·release 차이인지 확인되지 않았으므로 실제 training sample 목록으로 확정하지 않는다. 두 builder는 filtering한 actions/images에 원 `info[i]`를 사용해 종료를 판단하는 경로도 보인다. **필터 후 index 정렬 확인이 필요한 코드 위험**이며, 공개 checkpoint가 잘못 학습됐다는 결과는 아니다. 같은 데이터 재학습을 선택할 때 original episode ID와 retained step index를 보존해야 한다.

### 8.2 행동·관측·실행 계약

| 계약 | VRL 기존 고정 계약 | RL4VLA 공개 경로에서 확인한 것 |
|---|---|---|
| 환경·로봇 | LIBERO / Panda / OSC_POSE | ManiSkill fork / WidowX / `arm_pd_ee_target_delta_pose_align2_gripper_pd_joint_pos` |
| 시간 | control 20 Hz, query마다 8-step chunk; 계획상 520 policy steps + reset별 warmup 10 | control 5 Hz·physics 500 Hz, query마다 7개 token으로 **1개 7-D action**, 기본 episode 80 steps |
| VLA 입력 | 단일 RGB 224 + instruction; VLA proprio 없음. Residual은 별도 2-frame feature·proprio 사용 | `3rd_view_camera` RGB + instruction만 policy에 전달. RGB+segmentation 환경의 segmentation은 policy 입력이 아님 |
| 정규화 | A/B `libero_10_no_noops` bytes 동일. α=0.1은 normalized correction scale | Warmup/RL `bridge_orig`, SFT `sft`. 첫 6축 q01/q99가 **실제로 다름**. 양쪽 gripper mask false |
| decode | 두 모델 동일 greedy discrete parallel decode를 계획 | `get_action(deterministic=True)`도 기본 eval temperature **0.6**여서 `do_sample=True`. 이름만으로 greedy라 해석 금지 |
| gripper·rotation | 원 LIBERO binarize/invert 경로 유지 | Wrapper는 gripper에 `>0.5`를 적용하고 rotation 3축을 그대로 controller에 전달. LIBERO 변환 함수로 교체 불가 |
| 보상·종료 | 기존 residual 계약은 첫 성공 1·나머지 0, 성공/기한 종료 | Wrapper의 stage score는 grasp 0.1 + consecutive grasp 0.1 + success-and-grasp 1.0, 반환은 **이전 score와의 차분**. `terminated`를 버리고 truncation을 반환함 |

VRL 수치는 [기존 계약](../sources/vla_rl_gap_review_2026-11-03.json)의 `r2_review.comparison_contract`를 따른다. SimpleVLA-RL v1의 학습 horizon 512와 현재 진단 계약 520은 다른 설정이다. 원 논문 수치의 exact reproduction이라고 쓰지 않는다. RL4VLA 근거는 [wrapper L13–124](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/SimplerEnv/simpler_env/env/simpler_wrapper.py#L13), [policy L111–163](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/SimplerEnv/simpler_env/policies/openvla/openvla_train.py#L111), [기본 args](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/SimplerEnv/simpler_env/train_ms3_ppo.py#L42)다. 모두 source 확인이며 실제 rate·성능 측정은 아니다.

RL4VLA warmup/RL의 첫 회전축 quantile은 약 [-0.08092, 0.08192], SFT는 [-0.00509, 0.00550]다. 단순 같은 normalized delta가 같은 물리 명령이 아니다. Primary 진단에는 각 checkpoint의 **native normalizer를 유지**하고 실제 controller command를 비교한다. 임의 normalizer 통일은 모델의 학습 의미를 바꾸므로 공정성 확보책이 아니다. 같은 normalizer의 인과 비교가 필요하면 그것으로 함께 학습한 별도 대조군이 필요하다. [Warmup config](https://huggingface.co/gen-robot/openvla-7b-rlvla-warmup/blob/735fd5d1f4472c4c9f3f998f0e89aa641af5ad03/config.json), [SFT config](https://huggingface.co/gen-robot/openvla-7b-rlvla-sft_16k/blob/cda67bb9cf33bc87cb8bf715572ae0c44e98f8ae/config.json).

Processor JSON은 warmup/SFT의 hash가 같고 RL은 `auto_map`만 다르다. 나머지 transform 설정의 equality는 실제 tensor equality를 입증하지 않는다. Warmup/RL config는 upstream OpenVLA remote code를 가리키며 공개 training wrapper는 자체 `OpenVLAForActionPredictionWithValueHead`를 명시적으로 import한다. **Weights SHA 하나만 pin하면 loader까지 고정되는 것이 아니다.** 새 adapter는 이 code 경로를 고정하고 native forward·token/command 일치를 확인해야 한다. JSON의 `torch_dtype` 표기만으로 실행 precision도 확정하지 않는다.

### 8.3 무엇의 효과를 추정할 것인가

아래는 **연구자 설계**이며 논문 보고 결과나 실행 결과가 아니다.

**VRL — 교체 후 추가 적응의 가치.** 같은 held-out 초기 상태에서 성공률을 `J`로 둔다. 우선 `J(A+r_A)-J(A)`로 기존 residual의 유용성을, `J(B+r_A)-J(B)`로 무학습 이식 효과를 구별한다. 추가 budget `b∈{0,500,1000}` decision에서 `J(B+r_m(b))-J(B+r_F(b))`는 fresh 초기화 F 대비 arm m의 적응 차이다. B 단독·고정 gain·warm 초기화 W와의 차이도 각각 보고한다. Proposed arm이 W를 넘는지와 모든 residual이 B를 넘는지는 다른 질문이다.

**중요한 식별 한계:** 기존 F/W/U/Z/G/P는 모두 과거 `D_A` 접근권을 가진다. 따라서 F 대비 이득은 **공통 과거 데이터 아래 초기화/anchor 선택의 가치**이며 `D_A` 자체의 인과효과가 아니다. 과거 경험 접근 유무가 독립 contribution이라면 후속에 `D_A` 없는 fresh 대조가 필요하다. 이번에는 동결 계약에 arm을 몰래 추가하지 않았다. 현재 질문은 우선 residual 재적응의 실용 가치로 한정한다.

**비용:** 교체 시점 이후의 decision·실제 env step·reset·query·encoder·gradient·GPU 시간을 보고하고, `D_A` 수집/기존 residual 학습은 매몰 비용으로 별도 병기한다. 누적 배포비용은 `기존 준비 비용 + Σ(교체별 추가 비용)`이며 여러 업데이트를 측정하지 않았으므로 amortization 이득은 주장하지 않는다. 공통 probe·critic warmup·B action 재계산·평가도 공짜로 빼지 않는다. 같은 상한은 실제 소비량 equality가 아니다.

**FEEDBACK — 정보 가용성의 효과.** `Y_m(p,v)`를 checkpoint m의 고정 deadline 성공률로 둔다. `p=0/1`은 물리 변화 없음/있음, `v=F/S`는 fresh/명시적으로 지연된 관측이다. 첫 진단은 변경 시점 뒤 **한 번의 query에만 직전 RGB를 제공**하고 이후 fresh로 돌아가는 1-query 지연으로 좁힌다. 계속 이미지를 동결하는 실험은 별도 개입이며 합치지 않는다.

`I_m = [Y_m(1,F)-Y_m(1,S)] - [Y_m(0,F)-Y_m(0,S)]`

이는 정상 조건의 지연 손실을 뺀 물리 변화 상황의 추가 관측 가치다. `I_RL-I_SFT`는 공개 정책 간 상호작용 차이이며 **RL 목적함수의 인과효과가 아니다**. Warmup도 보고하되 능력이 낮으면 floor로 인해 비교가 덜 유익할 수 있다. 큰 `I_m`은 fresh 회복이 좋거나 stale에서 더 크게 무너진 결과일 수 있으므로 **네 cell의 원 성공률과 completion time**을 항상 함께 보고한다. Clean 성공률로 나눈 비율이나 clean 성공 episode만 고르는 방법으로 혼입이 사라지지 않는다.

공통 개입 직전 상태에서 4개 branch를 만들고 instruction·robot/controller·시간·예산을 유지한다. 각 모델의 자연 rollout과 공통 상태 branch는 별도 결과로 남긴다. 공통 상태 bank도 생성 policy·task phase에 편향될 수 있다. 모델마다 방문한 state를 같은 것으로 간주하지 않는다. Background-only rendering 대조는 같은 물리 상태의 nuisance 변화이며, 물체/팔을 가리는 whole-image texture를 background-only로 이름 바꾸지 않는다. 전체 stale RGB는 robot pose 정보도 늦추므로 `I_m`을 물체 위치 정보만의 효과로 좁혀 해석하지 않는다.

**같은 상태 query와 rollout의 역할:** 같은 물리 snapshot에서 fresh/stale 입력으로 얻은 command 차이는 관측 반응성이다. Hidden pose는 기록·개입 검증용이며 policy에 주지 않는다. 반응성이 커도 유용한 회복일 수 없고, 성공률은 실제 branch rollout에서만 측정한다. 첫 IO 준비 단계에는 greedy/고정 RNG 여부를 명시해 반복 query 변동과 image 개입 효과를 구분한다. Greedy로 바꾸면 RL4VLA 기본 평가 재현이 아닌 진단 설정이다.

### 8.4 단순 대안은 어디까지 설명하는가

| 대안 | 설명할 수 있는 범위 | 남는 한계 / 수정 규칙 |
|---|---|---|
| VRL scalar gain | 오래된 보정 크기만 낮춰 이득을 회복하는가 | 충분하면 복잡한 anchor 방법 주장을 줄인다. Normalizer가 다른 두 VLA를 공정하게 만드는 수단은 아님 |
| VRL IL-S / IL-R | W와 **같은 raw data·초기 residual·actor update 수**에서 성공 선택/return-weighted command imitation으로 W 효과를 설명하는가 | 다른 online arm의 방문 데이터까지 같지 않음. Full-VLA SFT와의 비교도 아님. 성공 없음·불완전 return은 기존 contract의 NA/censor 규칙 유지 |
| FEEDBACK 성공 BC / return-weighted BC | 공통 rollout의 상태 coverage·성공 데이터 선택이 관측 활용 차이를 설명하는가 | 현재 공개 3개 weights에는 이 대조가 없음. 동일 초기 weights·data IDs·retained steps·normalizer·augmentation·trainable parameter·budget을 고정한 **VLA action-token** 대조가 후속 필요 |
| Clean competence | RL 모델이 원래 더 잘 움직이기 때문에 perturbation에도 강해 보이는가 | Clean 4-cell 원수치와 공통 상태 분기를 함께 본다. 차분 하나로 motor competence가 완전히 제거됐다고 주장하지 않음 |
| Nuisance augmentation | 배경 변화 억제만으로 robustness를 설명하는가 | 물리 변화의 유효 정보 이용과 별개. 시각 민감도/attribution만으로 회복 능력을 대신 측정하지 않음 |

같은 데이터에 임의로 PPO epoch를 반복하면 on-policy 대조가 되는 것은 아니다. **목적함수만의 비교**를 선택할 경우 공통 behavior rollout·log-prob·초기 정책을 확보한 유효한 update 범위를 먼저 고정해야 한다. 장기간 각 방법이 자기 데이터를 모으면 비교 대상은 objective와 탐색/coverage를 포함한 학습 절차 전체다. 목적함수와 데이터의 분리 주장은 그보다 좁은 추가 설계가 필요하다.

### 8.5 재사용 가능성, 구현 위험, 다음 행동

| 항목 | 판단 |
|---|---|
| VRL `native_p0.py` 그대로 사용 | **불가.** LIBERO·8×7 chunk·20 Hz·gripper·TF crop·CUDA 12.4에 묶여 있음. RL4VLA는 single action·5 Hz·ManiSkill/SAPIEN 경로 |
| 기존 Docker image 공유 | **검증 안 됨.** RL4VLA README는 Python 3.10 / torch 2.2.0+cu121 / flash-attn 2.7.4.post1을 안내. VRL torch 2.4.0+cu124 recipe와 다름. 별도 source pin/lock/build 필요 |
| VRL의 `D_A`·residual weights·critic | FEEDBACK에는 **직접 재사용 불가**. robot/task/action/reward가 다름. VRL의 실제 학습 residual과 `D_A`도 아직 생성 전 |
| 비용·provenance·관측 기록 | 형식/검증 원칙은 재사용 가능. 기존 검사 통과를 새 adapter 검사 통과로 복사하지 않음 |
| 공개 RL4VLA weights | 3개 revision·metadata pin 확보. native load·VRAM·asset·code/weight 호환성은 미확인. BF16 표시를 실행 증거로 삼지 않음 |

특히 [물체 재배치 code L2651–2672](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/ManiSkill/mani_skill/envs/tasks/digital_twins/bridge_dataset_eval/put_on_in_scene_multi.py#L2651)는 `evaluate()`가 step 5에서 **pose 변경과 `_settle(0.5)`를 수행**한다. [BaseEnv L942–952·1038–1048](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/ManiSkill/mani_skill/envs/sapien_env.py#L942)는 step → get_info/evaluate → get_obs 순서다. 따라서 observer가 get_info를 반복 호출하면 같은 step의 개입·settling을 반복할 위험이 있다. 원 `_settle` 구현의 physics 진행도 별도 계수해야 하며 인자 0.5를 실제 0.5초라고 추정하지 않는다. 공통 상태 복원에는 physical state 외에 elapsed step·controller target·RNG·task selection·event flag·wrapper reward/history가 필요하다. `get_state_dict()`가 존재한다는 것만으로 복원 완료가 아니다.

**다음 TODO: GAP-FEEDBACK-P0-PREP.** 위 위험을 반영한 단일 dev scene의 pre/post RGB·action IO adapter와 Docker 재개 packet을 준비한다. 최소 query·step·physics budget과 개입 한 번 실행을 먼저 고정하고, resource 조건이 충족되면 그 작은 IO만 검증한다. 같은 metadata 조사·새 loss·대규모 rollout·3개 모델 재학습으로 넘어가지 않는다. 본 N2는 비교 검토 완료이며 **FEEDBACK 실행 adapter/manifest는 아직 없다**. 기존 VRL P0의 36 env steps·2 queries 계약과 우선순위를 바꾸지 않는다. 호환 NVIDIA 자원이 확보되면 VRL P0도 기존 재개 경로로 진행한다.

연구 가치는 **VRL: 교체 후 적응 비용·성능 보존**, **FEEDBACK: 정보 개입으로 후학습 효과를 구분하는 진단**으로 각각 남는다. 두 질문을 합쳐야 기여가 생기는 것은 아니다. 현재는 새 방법의 top-tier 기여를 확정할 증거가 없고, 작은 pilot에서 의미 있는 차이가 관측되면 독립 task/update/seed와 matched-data 대조로 확장할 수 있다. 그렇지 않으면 단순 대안으로 설명되는 범위를 결과로 남긴다.

### 8.6 이번 작업의 검증

- Generator compile·재생성·`git diff --check` 통과. 합계 **1,110편 / CORE 47 · NEXT 332 · REFERENCE 489 · ARCHIVE 242** 유지. 생성 reading plan은 날짜만 변경됐다.
- Repository audit: 5,550 표준 노트 / active 379 / history 47 / Markdown 5,758 / links 12,010, **오류 0·경고 0**.
- Active/history tracker는 시작 시점과 **byte 동일**. 기존 staged diff·VRL 단일 계약·runtime/코드 hash 보존. 기존 31편 탐색 원장 부분도 그대로이며 N2 section만 추가했다.
- 관련 문서·source와 generated plan **10개**만 변경, 기존 파일 삭제 0·새 주제 파일 0. 27개 source metadata/code 파일의 URL·SHA256를 기록했다. Hash는 다운로드한 metadata/text의 것이며 weights 검증이 아니다.
- 새 실험·패키지 설치·weights/assets/PDF 다운로드·외부 발송·commit/push 없음. 11/05 Docker 관측을 11/06 재측정으로 표시하지 않는다. 실제 외부 연구자 피드백도 미수신이다.
