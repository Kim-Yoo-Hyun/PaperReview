# 기존 후보 밖의 VLA + RL 연구 공백 추가 탐색

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- 검토일: 2026-11-09 KST
- 이 보고서의 작업: **GAP-ROBOTICS-SCOUT — Robotics 중심 재선정**. 접촉 적응 우선·복구 가능성 보존/접촉 유지 이동 조작 예비. 후속 **[CONTACT-RL-N1/N2 완료](../research_topics/contact_adaptation/내용/README.md)**: 지정 본문·공개 구현 대조 뒤 조합 신규성 제외, charger 삽입의 좁은 비교 탐색 유지. 단일 π₀·관절 gain·동일 비용 비교와 sensor/controller P0-A 요구를 정했다. 내부 비실험 설계에 이어 P0-PREP 재개 코드도 작성했다. 현재 Mac NVIDIA allocation 실패·Docker stdlib16검사만 확인했으며 native runtime·효과는 미검증이다. 상세 결과는 주제별 두 README에 통합했다. 최초 GAP-SCOUT-NOV09의 질문과 제외 이력은 아래에 보존한다.
- 최초 scout 근거: [15편 source 원장](../sources/vla_rl_additional_gaps_2026-11-09.json). Registry 7편과 외부 8편을 대조했다. 대부분 초록·공식 project 범위이며 VIP, Grounding Sim-to-Real, RLIF, PACT는 가까운 본문 구간도 확인했다. 전체 정독·공개 코드 감사·실험 완료 수가 아니다.
- 최초 두 질문의 canonical 내용: synthesis의 [수집 예산 배분](../../synthesis/02_rl_il_offline.md#gap-allocation-2026), [물리 조건 민감도](../../synthesis/05_world_models_safety.md#gap-physics-2026). 이 보고서는 선정 이유·검색 범위·제외 이력을 보존한다.
- 후속: 같은 날 **[GAP-ALLOC-N1 초기 buildup](../research_topics/retired/README.md#task_allocation)**을 완료하고 과제 배분의 상세 내용을 주제별 두 폴더로 통합했다. 아래 9개 주제·다음 N1 표기는 최초 scout 시점의 기록이다. 후속 N2 내부 설계·P0-PREP도 완료했으며 당시 다음 행동은 호환 local NVIDIA에서 P0 native 검증이었다. 이후 사용자의 Robotics 중심 요청으로 과제 배분을 예비로 돌렸다. 현재 상태는 [TODO](../../TODO.md)가 소유한다.

<a id="robotics-reorientation"></a>
## Robotics 중심 재선정 — 2026-11-09

**이전 주제의 위치를 수정한다.** 과제 배분은 로봇 VLA를 대상으로 하지만 주요 변수는 task sampling·gradient variance·compute budget이어서 일반 다중 과제 RL에도 적용된다. 로보틱스와 무관하지는 않지만, 사용자가 원하는 물리적 행동의 문제를 중심 기여로 삼기에는 약하다. 과제 배분의 준비물은 보존하고 **예비 분석 후보**로 낮춘다. 이번 선택은 GPU 부재 때문에 우회한 것이 아니라 연구 방향의 적합성을 다시 판단한 결과다.

새 질문은 **어떤 물리 상황에서 로봇이 실패하며, 어떤 관측·행동·학습을 바꾸면 나아지는가**에서 시작한다. 2024–2026 기존 registry와 외부 1차 출처 21편을 추가 대조했다. 정확한 논문·URL·확인 범위·registry identity는 같은 [원장의 robotics_review](../sources/vla_rl_additional_gaps_2026-11-09.json)에 통합했다. 최초 15편과 별도 검토 묶음이며 unique 논문 36편을 정독했다는 뜻이 아니다. Registry 신규 등록은 하지 않았다.

### 연구 공백 후보와 검토 순서

| 순서 | 로봇의 물리 문제·남긴 질문 | 기여로 발전할 지점 | 현재 판단·주요 위험 |
|---|---|---|---|
| **1** | **접촉 전환에 대한 적응:** 삽입 중 걸림, 닦는 도중 마찰 변화에 한 VLA가 동작·순응성을 공동 조절하도록 RL로 학습하면 어떤 이득이 생기는가? | 단순히 부드럽게 움직이는 것과 경험에 따른 적응을 구별하고, 성공–힘–시간 절충을 개선하는 학습 원리 | **우선 탐색.** 로보틱스/VLA/RL 연결이 가장 직접적. TacCoRL·TORL·CompVLA와 겹칠 위험이 높고 F/T·controller·실물 평가 부담이 있음 |
| **2** | **복구 가능성 보존:** 원 목표를 수행하다 물체를 손이 닿지 않는 곳으로 밀거나 더 깊이 끼우지 않도록 정상 실행부터 학습할 수 있는가? | 실패 뒤 복구에 더해, 이후의 복구 비용을 고려하는 행동 학습과 평가 | **예비 탐색.** Recovery/safe RL와 중복 위험. Kintsugi·OGPO·RESCUE 이후의 차이를 먼저 확인해야 함 |
| **3** | **접촉 유지 이동 조작:** 문·서랍을 잡은 채 base와 arm을 움직일 때 한 정책의 RL 후학습이 접촉 유지와 실행 가능성을 높이는가? | Mobile manipulation의 실제 동역학·기구학 coupling을 학습하는 정책 | **예비 탐색.** 기존 whole-body 제어가 강하고 platform/data 부담이 가장 큼. 본문 차별성 검토도 덜 진행됨 |

이 순서는 **scout 당시 다음 문헌 검토의 투자 순서**다. 완성된 세 연구 주제, 입증된 독립 방법, 추가 세 실험 대기를 뜻하지 않는다. 탐색 카드는 각각 [접촉 적응](../../synthesis/03_manipulation_contact.md#gap-contact-rl-2026), [복구 가능성](../../synthesis/05_world_models_safety.md#gap-recoverability-rl-2026), [이동 중 접촉 유지](../../synthesis/06_locomotion_whole_body.md#gap-mobile-contact-rl-2026)에 둔다. 접촉 후보의 후속 상세 비교는 위 N1 주제 문서로 통합했다. 첫 질문은 기존 물리 일반화 질문을 구체화한 분기이며 새 이름만 붙인 완전히 독립된 gap으로 세지 않는다.

### 2024–2026 선행이 이미 답한 범위

| 근거 | 이번에 확인한 내용 | 공백으로 주장할 수 없는 것 |
|---|---|---|
| [RoboPack, RSS 2024](https://www.roboticsproceedings.org/rss20/p130.html) | 촉각 이력의 latent physics와 MPC로 실물 packing 수행 | 접촉 이력을 이용한 물성 적응 자체 |
| [ConRFT, RSS 2025](https://www.roboticsproceedings.org/rss21/p019.html) | offline/online VLA RL와 실제 조작 평가 | VLA를 RL로 직접 후학습하는 것 자체 |
| [FORGE, RA-L 2025](https://ieeexplore.ieee.org/abstract/document/10925874/) | force-conditioned RL, force threshold, dynamics randomization | 물성 불확실성 아래 힘 제한을 지키는 RL 자체 |
| [ForceVLA2, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) · [AT-VLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html) | force-position 출력·force awareness, adaptive tactile feedback | force/tactile 입력을 VLA에 추가하는 것 자체 |
| [CompVLA](https://compvla.github.io/) · [TDC](https://yifei-y.github.io/project-pages/TDC/) | 가변 순응성의 시연 학습, sim-transferable 방향과 조정 가능한 magnitude 분리 | 가변 stiffness 출력 또는 compliance head 자체 |
| [TacCoRL](https://arxiv.org/abs/2606.11743) | 촉각을 사용하는 VLA의 sim-real co-training과 simulation RL | 단일 tactile VLA에 RL을 적용하는 조합 자체 |
| [TORL-VLA](https://torl-vla.github.io/) · [ForceRFT](https://arxiv.org/abs/2609.22840) | 단계별/residual 온라인 RL, 실행 중 접촉 피드백. TORL은 마찰·유연성 변화까지 비교 | 접촉 correction·물성 OOD·residual 대비 IL 비교의 최초 주장 |
| [ContactBench 1.0](https://arxiv.org/abs/2610.24512) | 반복 가능한 접촉 과제와 물리 자산; visual-tactile의 어려움 보고 | tactile이 언제나 효과적이라는 전제, 접촉 실패 benchmark 자체 |
| [Kintsugi-VLA](https://arxiv.org/abs/2609.31048) · [OGPO](https://arxiv.org/abs/2610.12914) | simulator 분기로 recoverability와 recovery 데이터 선택, goal-conditioned offline 최적화 | recoverability 측정·recovery 데이터·goal reachability 학습 자체 |
| [ReCoVLA](https://arxiv.org/abs/2606.09630) · [RESCUE](https://arxiv.org/abs/2610.13516) · [Simple Retreat 분석](https://arxiv.org/abs/2610.06921) | residual recovery, 실제 개입 가치, 재실행/단순 후퇴 대조 | 복구 성공을 자동으로 learned correction의 고유 효과로 해석 |
| [MoTo](https://proceedings.mlr.press/v305/wu25c.html) · [Mobi-π](https://proceedings.mlr.press/v305/yang25b.html), CoRL 2025 | manipulation을 고려한 navigation/docking과 policy mobilization | navigation과 manipulation을 처음 연결한다는 주장 |
| [WholeBodyVLA, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) · [MobileVLA-R1](https://aigeeksgroup.github.io/MobileVLA-R1/) | loco-manipulation 및 language-conditioned mobile action/RL | VLA+RL로 mobile robot을 다룬다는 것 자체 |
| [FORGE-plus](https://arxiv.org/abs/2607.21227) | force budget과 복구를 결합한 계층형 시뮬레이션 사례 | 힘 제한+복구라는 조합 자체. 실물 성공 근거로 사용 불가 |

**출판 상태 경계:** CompVLA·TDC·TacCoRL은 저자 페이지에 CoRL 2026이 명시돼 있지만 이번 조사에서 공식 paper별 채택 페이지를 확인하지 못했다. 저자 표기로만 남기며 verified top-tier 편수에 합산하지 않는다. TORL·ForceRFT·ContactBench·Kintsugi·OGPO·ReCoVLA·RESCUE·Simple Retreat·FORGE-plus는 이번 확인 범위에서 arXiv다. Kintsugi의 ICRA 2027 제출 표기는 채택이 아니다. MobileVLA-R1의 ECCV 2026은 기존 registry의 11/07 공식 accepted-list 확인을 계승하고 이번에는 저자 project를 재확인했다. 논문 이름의 unified는 단일 실행 actor를 자동 보증하지 않는다.

**확인 깊이:** 공식 proceedings/출판사 초록과 저자 초록, CompVLA·TDC·TacCoRL·TORL의 지정 method/evaluation project 구간을 확인했다. ForceVLA2는 공식 CVF 검색 결과를 확인했으나 직접 페이지가 403이었다. 전체 부록·코드·실행 검토는 아직 아니다. ContactBench는 이번에 v2 초록을 재확인했으며 기존 10/23 지정 본문 검토와 구분한다. 검색 결과가 없다는 사실을 미해결 증명으로 쓰지 않는다.

### 단일 정책 선호를 연구 질문에 적용하는 방법

VLA가 시각·언어·로봇 상태·접촉 이력에서 하나의 행동 분포를 출력하고 RL이 그 정책을 후학습하는 것을 우선한다. 고정 servo·안전 제한·좌표 변환은 로봇 실행에 필요할 수 있다. 별도 학습된 high-level planner와 RL skill을 연결하는 구조는 비교 대상으로 두되 주 제안의 필수 형태로 정하지 않는다. **네트워크를 합쳤다는 사실만으로 기여를 주장하지 않고**, 같은 센서·action 권한·제어 주기·데이터와 비용에서 달라지는 물리 결과로 평가한다.

VLA를 사용해야 할 이유도 검증한다. 단일 고정 삽입 task의 성공만 높이면 specialist RL보다 큰 모델을 사용할 근거가 약하다. 우선 작은 자연 task로 현상을 확인한 뒤, 복수 지시/물체/접촉 조건의 공유와 원래 free-space 능력 유지가 논문 기여에 필요한지 판단한다. 이것은 탐색 시작 전에 대형 generalist benchmark를 완성하라는 gate가 아니다.

### 기존 후보와의 관계·다음 TODO

- ALLOC·UNIFIED·HINDSIGHT는 로봇 적용과 일반 RL 기여가 섞인 후보로 보존한다. 기존 8개 내부 순위는 역사적 비교이며 현재의 자동 실행 순서가 아니다.
- CONTACT-RL은 기존 GAP-CONTACT의 센서 필요성 증명, DEFORM/SYSID의 active identification, FEEDBACK의 stale/fresh 시각 진단을 재개하는 것이 아니다. 새 근거인 CompVLA/TacCoRL/TORL/ForceRFT를 대조하여 **contact-conditioned 행동의 학습**이 별도로 남는지 살핀다.
- 복구 가능성 후보는 C5의 physical reset 분포 문제가 아니다. 다만 safe RL와 기존 복구 문헌의 중복이 더 확인되면 따로 키우지 않는다.
- 이동 접촉 후보는 HANDOFF의 정책 교체 후 docking 재사용과 다르다. 단일 policy의 공동 action 공간·실행 부담을 먼저 확인한다.

**당시 다음 GAP-CONTACT-RL-N1 → 후속 N1/N2 완료:** [직접 선행 비교·판정](../research_topics/contact_adaptation/내용/README.md#prior-comparison)과 [공개 구현 경계](../research_topics/contact_adaptation/재현%20방법/README.md)를 주제별 두 폴더에 통합했다. Facet-0·CG-RL·CompliantVLA-adaptor를 추가 대조해 넓은 조합 주장은 제외했다. [N2 계약](../research_topics/contact_adaptation/내용/README.md#n2-contract)까지 구체화했으며 P0-PREP에서 local GPU 미지원 확인·실행 자료 작성을 마쳤고 다음은 호환 local NVIDIA의 sensor/controller P0-A다. 실제 feasibility·외부 피드백·연구 효과는 미확인이다. 초기 scout 당시 확인 범위와 수량은 아래 기록 그대로 보존한다.

실험·Docker 환경 검사·package/PDF 다운로드는 수행하지 않았다. 최신 요청은 연구 방향 조사이므로 이미 알려진 GPU 실패를 다시 재현하지 않았다. 실행 요청으로 넘어갈 때 AGENTS의 local Docker 조건 확인 규칙을 적용한다.

## 최초 scout 기록 — 과제 배분·물리 일반화

아래 순서와 다음 N1은 당시 선택이다. 현행 우선순위는 위 Robotics 중심 재선정 및 [TODO](../../TODO.md)를 따른다.

## 이번에 남긴 질문

| 이번 탐색 내 순서 | 질문 | 기대할 수 있는 기여 | 현재 판정 |
|---|---|---|---|
| 1 | 과제별 길이·난이도가 다른 단일 VLA의 RL에서, 실제 수집 비용을 맞추면 어떤 과제 배분이 배포 성능을 높이는가? | 로봇 상호작용 비용과 고정된 배포 목표를 함께 고려하는 평가·분석. 기존 allocation을 넘는 현상이 확인되면 학습 방법으로 확장 | **탐색 권고**, 신규 방법의 필요성은 미입증 |
| 2 | 시뮬레이션에서 RL 업데이트를 늘릴 때, VLA의 접촉·동역학 변화에 대한 민감도는 어떤 조건에서 개선되거나 악화되는가? | 평균 성공률로 가려지는 물리 일반화의 조건 분석. 현상이 있으면 학습/중단 기준으로 확장 | **조건부 탐색**, 직접 선행·구현 부담이 큼 |

두 질문은 각각 **학습할 경험을 어디에 쓸지**, **상호작용으로 학습한 행동이 어떤 물리 조건에 의존하는지**를 묻는다. 실행 시 하나의 VLA가 행동하며, 별도 상위 planner와 RL controller를 연결하는 계층 구조가 필수인 제안은 아니다. 다만 단일 VLA에 기존 알고리즘을 적용했다는 사실만으로 새 기여가 생기지는 않는다.

현재 9개 준비·탐색 주제를 11개 실험 대기 주제로 늘리지 않는다. 기존 UNIFIED·VRL 등의 투자 순위와 HINDSIGHT-P0 계약은 유지한다. 위 순서는 **이번에 발견한 두 질문 사이의 다음 문헌 검토 순서**이며 top-tier 채택 가능성의 수치 평가가 아니다.

## 이미 해결된 범위와 좁힌 이유

**수집 배분:** [VLA-RL](https://arxiv.org/abs/2505.18719)은 curriculum selection을, [VIP, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/dc62cd4ec77f3bbec8e6245d0bd91d08-Abstract-Conference.html)은 rollout 예산하 gradient variance 기반 배분을 이미 제시한다. [DRATS, NeurIPS 2026 공식 프로그램](https://neurips.cc/virtual/2026/poster/152819)은 목표 return과의 격차에 따른 과제 배분을 다룬다. 따라서 “어려운 과제를 더 학습한다”, “adaptive sampling을 VLA에 넣는다”는 공백으로 제시하지 않는다. 남긴 질문과 단순 비용 보정으로 충분한지의 판단은 위 canonical card에 기록했다.

**물리 일반화:** [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)는 RL/SFT의 일반화 차이를 이미 분석한다. 특히 외부 [Grounding Sim-to-Real §4.3–4.4·App. B.3](https://arxiv.org/html/2603.22876v2)은 물리 조건 왜곡과 RL의 실물 전이를 모두 비교한다. “VLA의 physics gap을 처음 측정한다”는 주장은 불가하다. 이 논문은 RL의 긍정적 전이를 보고하므로 RL이 물리 조건에 과적합한다는 방향도 전제하지 않는다. 추가 질문은 업데이트 진행에 따른 민감도 변화와 접촉 조건의 상호작용으로 한정했다.

## 사람 개입 질문을 새 후보로 올리지 않은 이유

처음에는 “사람의 개입 시점·기준이 달라지면 VLA RL의 자율 수행 능력이 달라지는가?”를 검토했다. 그러나 [RLIF, ICLR 2024의 §5.1·5.2 및 App. A.4](https://arxiv.org/html/2311.12996v2)는 이미 intervention mode, expert quality, value-gap threshold를 다룬다. [HIL-SERL](https://doi.org/10.1126/scirobotics.ads5033), [RECAP, RSS 2026](https://roboticsproceedings.org/rss22/p087.html), [PACT](https://arxiv.org/html/2606.03949v2), [WHIRL](https://arxiv.org/abs/2609.06009)은 교정 경험·선호·개입 위험의 활용까지 확장한다. 일반적인 개입 정책 민감도나 교정 credit assignment만으로는 새 질문이 충분히 구별되지 않는다.

**향후 좁힐 여지:** 동일한 task reward 아래 여러 운영자의 서로 다른 안전/스타일 선호가 섞일 때, 언어로 지정된 배포 목적과 개입 회피 목적을 구분하는 문제는 남겨 둘 수 있다. 그러나 multi-annotator preference learning, reward identifiability, RLIF·RECAP의 정확한 학습 target과 대조하지 않았으므로 이번의 신규 gap으로 세지 않는다. 실제 운영자별 기록도 미확보다.

사람이 포함된 transition이라는 이유만으로 off-policy Bellman 학습이 잘못됐다고 판단하지 않는다. 반대로 사람 도움을 받은 episode 성공을 자율 성공과 같게 취급해서도 안 된다. 개입하지 않았을 때의 반사실 결과는 overlap·모델 가정·실제 분기 관측 없이 식별됐다고 주장할 수 없다. 이는 향후 비교에서 지켜야 할 해석 경계다.

## 기존 질문과의 중복 제거

| 다시 발견한 큰 방향 | 기존 위치·이번 처리 |
|---|---|
| 단일 policy/value 표현·gradient 간섭 | UNIFIED. 수집 배분 후보는 목적함수/표현을 고정하고 경험 수집만 바꾸는 축으로 구분 |
| 실패의 hindsight 목표 선택 | HINDSIGHT. 새 배분 질문에서는 목표 relabeling을 기본 조건에서 제외 |
| 양팔 action coupling·공동 탐색 | [10/27 GAP-S2](./VLA_GAP_RESELECTION_2026-10-27.md), CROSSPLAY 및 TwinVLA/RDT 계보와 중복. 새 주제로 재명명하지 않음 |
| 추론 지연·chunk·추가 관측·semantic retention | E2/C1/SCOUT/FEEDBACK과 중복. 새 후보에서 제외 |
| reward audit·reset 비용·checkpoint 선택 | C4/C5/C6의 과거 판단 유지. 새 배분에서도 reset은 비용 항목이며 C5 재개 근거가 아님 |
| learned world-model 오류 악용·추론 후보 선택 | GAP-WM. 물리 후보는 배포 planner의 후보 점수 대신 실제 simulator transition 아래 학습된 정책을 비교 |
| 물성의 active probing·model class 식별 | GAP-DEFORM/SYSID. 물리 후보에서 online ID나 정보 획득 제어를 새 방법으로 다시 제안하지 않음 |
| 사람 교정 활용·개입 기준 | [11/05 제외 이력](./VLA_RL_NEW_GAP_SCAN_2026-11-05.md)과 RLIF 직접 선행 재확인. 추가 구체화 전 신규 후보로 채택하지 않음 |

## 조사 범위와 증거 경계

2024–2026 논문의 공식 ICLR·NeurIPS·ICML·RSS·CoRL/PMLR, Science Robotics 출판 metadata와 저자 arXiv/HTML/project를 사용했다. 이번은 두 질문의 직접 선행 중심 조사이며 모든 venue·논문을 망라한 systematic review가 아니다. 외부 목록은 발견 경로로만 사용하고 최종 사실은 1차 출처에 연결했다.

- VIP: 공식 ICLR 2026 초록 및 arXiv v3 §5.2·시간 비용 표. 정수 rollout 예산/최소·최대 배분을 이미 다룬다.
- Grounding Sim-to-Real: arXiv v2 §4.3–4.4·App. B.3/Table 7. 물리 perturbation 자체도 이미 선행이며 전체 supplement 정독은 아님.
- RLIF: 공식 ICLR PDF 검색 metadata·저자 초록 및 HTML §5.1–5.2·A.4. 공식 forum은 브라우저 확인 화면으로 직접 열람 실패했다.
- PACT: arXiv v2의 방법 구성·§6 limitation 구간. 정확한 전체 target/code 비교는 후속이다.
- DRATS: NeurIPS 2026 **공식 채택 프로그램**을 확인했다. 12월 발표 전이며 최종 proceedings 출판까지 확인한 것으로 표시하지 않는다.
- WHIRL: 저자 arXiv/project는 CoRL 2026 채택을 표기하지만 공식 paper별 발표 페이지는 이번에 확인하지 못했다. **저자 표기·공식 재확인 필요**로 보존한다.
- VLA-RL·Grounding Sim-to-Real·PACT는 이번 확인 범위에서 arXiv로 기록한다. SIMPLER는 CoRL 2024 행사와 PMLR 2025 출판 연도를 구별한다.

새 두 후보 모두 **CURATION-HYPOTHESIS**다. 가까운 본문의 일부를 확인했어도 자연 사례·효과·독립 기여를 입증한 것은 아니다. 실제 외부 연구자 피드백은 미수신이다. 본문/코드 대조가 끝나지 않은 것을 “GPU만 있으면 buildup 완료”로 표현하지 않는다.

## 다음 비실험 TODO

**GAP-ALLOC-N1:** VIP·DRATS·VLA-RL·SimpleVLA-RL/RLinf의 실제 sampler, loss normalization, episode 종료와 비용 집계 위치를 정적으로 대조한다. 하나의 공개 VLA 학습 경로에서 **task 배분과 같은-data loss weighting을 분리할 수 있는지**, 길이 차이를 만들려고 task 의미·성공 조건을 바꾸지 않는 작은 비교가 가능한지 확인한다. 단순 비용 보정·기존 allocation으로 질문이 모두 설명되면 새로운 scheduler 대신 평가 가이드/기존 주제 보조 분석으로 축소한다. 초기 계획은 synthesis card에 누적하는 것이었으며, 이후 N1을 시작하면서 상세 내용·추가 source는 위 주제 문서와 단일 원장으로 통합했다.

공개 코드와 작은 문제를 살피기 전에 새 algorithm·자원 quota·완성된 실행 packet을 요구하지 않는다. 반대로 이 탐색 완료를 실험 승인이나 과학적 GO로 확대하지 않는다. 선택되면 주제별 `내용/`·`재현 방법/` 두 폴더로 이동하고, 현재는 별도 주제 폴더를 만들지 않는다.

## 반영·검증

Synthesis의 Open Questions, 주제 index, TODO, update index와 상위 탐색 링크를 갱신했다. 신규 논문 등록·tier 변경·사용자 읽기 상태 변경은 없다. 실험·Docker 변경·PDF/weights/package 다운로드는 하지 않았다. 검증의 실제 결과는 [source 원장의 validation](../sources/vla_rl_additional_gaps_2026-11-09.json)에 기록한다.
