# 외부 대조와 누락 심사

2026-11-19 당시 원장 1,227편의 ID·제목을 서베이·학회·연구실·큐레이션 25개 목록과 대조했다. 외부 대조 후보 17편과 추가 검색에서 고른 19편을 심사해 **23편을 NEXT에 등록하고 9편을 보류했다. 4편은 기존 논문과 일치했다.** 날짜와 분모는 이 조사 시점에 고정한다. [등록 전 후보와 발견 목록](../work/sources/batches/missing_candidates_2026.yaml) · [36편의 판정과 원문 근거](../work/sources/batches/gapfill_2026_11.yaml)

<a id="external-coverage"></a>

## 기준 목록별 커버리지

목록별 중복을 정리한 44,911개 항목 중 586개, 로보틱스 관련 여덟 주제의 제목 필터에 든 1,401개 항목 중 159개가 일치했다. 같은 논문이 여러 목록에 나타날 수 있다. 마지막 열은 추가 검색식 G1·G2에 각각 걸린 제목 수이며, 대시는 해당 목록에 추가 검색을 적용하지 않았다는 뜻이다. [대조 원자료와 제목 정규식](../work/sources/coverage_titles.jsonl.gz) · [추가 검색식](#search-queries)

| 목록 · 원문 | 전체 일치/분모 | 주제 필터 일치/분모 | 필터 내 동일성 미결 | 능동 / 촉각 추가 검색 |
|---|---:|---:|---:|---:|
| [VLA · Concepts, Progress, Applications and Challenges](https://arxiv.org/html/2505.04769) · `surveyV` | 66/297 (22.2%) | 38/95 (40.0%) | 0 | — |
| [Humanoid Locomotion and Manipulation](https://arxiv.org/html/2501.02116) · `surveyH` | 53/423 (12.5%) | 12/90 (13.3%) | 0 | — |
| [VLA · A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/html/2405.14093) · `surveyM` | 168/766 (21.9%) | 55/217 (25.3%) | 0 | — |
| [RSS 2024](https://roboticsproceedings.org/rss20/) · `rss24` | 29/134 (21.6%) | 7/11 (63.6%) | 0 | 1 / 0 |
| [CoRL 2024](https://proceedings.mlr.press/v270/) · `corl24` | 27/264 (10.2%) | 7/16 (43.8%) | 0 | 0 / 0 |
| [ICLR 2024](https://iclr.cc/static/virtual/data/iclr-2024-orals-posters.json) · `iclr24` | 9/2296 (0.4%) | 0/1 (0.0%) | 0 | 0 / 0 |
| [NeurIPS 2024](https://neurips.cc/static/virtual/data/neurips-2024-orals-posters.json) · `neurips24` | 6/4537 (0.1%) | 1/10 (10.0%) | 0 | 2 / 0 |
| [ICRA 2024](https://api.crossref.org/works?filter=container-title%3A2024+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra24` | 12/1766 (0.7%) | 1/52 (1.9%) | 0 | — |
| [IROS 2024](https://api.crossref.org/works?filter=container-title%3A2024+IEEE%2FRSJ+International+Conference+on+Intelligent+Robots+and+Systems+%28IROS%29%2Ctype%3Aproceedings-article) · `iros24` | 0/1587 (0.0%) | 0/70 (0.0%) | 0 | — |
| [RSS 2025](https://roboticsproceedings.org/rss21/) · `rss25` | 65/163 (39.9%) | 20/26 (76.9%) | 0 | 0 / 4 |
| [CoRL 2025](https://proceedings.mlr.press/v305/) · `corl25` | 22/263 (8.4%) | 7/29 (24.1%) | 0 | 2 / 4 |
| [ICLR 2025](https://iclr.cc/static/virtual/data/iclr-2025-orals-posters.json) · `iclr25` | 49/3830 (1.3%) | 1/11 (9.1%) | 0 | 1 / 1 |
| [NeurIPS 2025](https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json) · `neurips25` | 52/5858 (0.9%) | 16/36 (44.4%) | 0 | 1 / 0 |
| [ICRA 2025](https://api.crossref.org/works?filter=container-title%3A2025+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra25` | 13/1609 (0.8%) | 4/61 (6.6%) | 0 | — |
| [IROS 2025](https://api.crossref.org/works?filter=container-title%3A2025+IEEE%2FRSJ+International+Conference+on+Intelligent+Robots+and+Systems+%28IROS%29%2Ctype%3Aproceedings-article) · `iros25` | 12/1985 (0.6%) | 2/83 (2.4%) | 0 | — |
| [RSS 2026](https://roboticsproceedings.org/rss22/) · `rss26` | 36/210 (17.1%) | 9/34 (26.5%) | 0 | 1 / 2 |
| [CoRL 2026](https://www.corl.org/program/accepted-papers) · `corl26` | 13/687 (1.9%) | 9/177 (5.1%) | 0 | 2 / 6 |
| [ICLR 2026](https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json) · `iclr26` | 65/5468 (1.2%) | 19/49 (38.8%) | 0 | 4 / 1 |
| [NeurIPS 2026](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) · `neurips26` | 4/9110 (0.0%) | 2/113 (1.8%) | 0 | 5 / 1 |
| [ICRA 2026](https://api.crossref.org/works?filter=container-title%3A2026+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra26` | 23/1881 (1.2%) | 15/152 (9.9%) | 1 | — |
| [IROS 2026](https://2026.ieee-iros.org/program/paper-index/) · `iros26` | 7/1929 (0.4%) | 2/170 (1.2%) | 0 | — |
| [Awesome Embodied VLA/VA/VLN](https://raw.githubusercontent.com/jonyzhang2023/awesome-embodied-vla-va-vln/main/README.md) · `awesome` | 71/253 (28.1%) | 43/141 (30.5%) | 1 | — |
| [Stanford ILIAD](https://iliad.stanford.edu/publications/) · `stanford` | 10/124 (8.1%) | 2/2 (100.0%) | 0 | — |
| [NVIDIA GEAR](https://research.nvidia.com/labs/gear/publications/) · `gear` | 18/47 (38.3%) | 6/10 (60.0%) | 0 | — |
| [Physical Intelligence](https://www.pi.website/research) · `pi` | 5/7 (71.4%) | 4/6 (66.7%) | 0 | — |

서베이 3편의 참고문헌을 직접 확인했고, 연구실은 공개 목록 전체, 학회는 2024–2026년 행사를 조사했다. ICRA·IROS는 IEEE가 Crossref에 기탁한 자료를 사용했으며 IROS 2026은 저널 발표를 포함하는 행사 색인을 썼다. 원자료 첫 행에는 출처·기간·제목 규칙·기준 원장 해시가 있고, 뒤의 각 행에 원제·정규화 제목·일치 ID·미결 판정이 있다. 동일 목록에서는 같은 등록 ID를 한 번 센다.

## 하위 주제별 수록 범위

등록 전 일치율이 낮은 순서다. 오른쪽 세 수치는 같은 분모로 재측정했다. 한 논문이 여러 주제에 해당할 수 있으며, 제목에 드러나지 않은 로봇 과업은 이 검색에서 빠질 수 있다.

| 순위 | 하위 주제 | 등록 전 일치/분모 | 미결 | 23편 등록 후 재측정 |
|---:|---|---:|---:|---:|
| 1 | 능동 로봇 인식 | 1/40 (2.5%) | 0 | 5/40 (12.5%) |
| 2 | 촉각 조작 | 10/246 (4.1%) | 0 | 17/246 (6.9%) |
| 3 | 실패 감지·복구 | 1/19 (5.3%) | 0 | — |
| 4 | 시연 수집·전이 | 11/129 (8.5%) | 0 | — |
| 5 | 휴머노이드 전신·보행 | 17/196 (8.7%) | 0 | — |
| 6 | 지시 기반 내비게이션 | 12/123 (9.8%) | 0 | — |
| 7 | 접촉 조립·삽입 | 9/88 (10.2%) | 0 | — |
| 8 | VLA 행동정책 | 105/630 (16.7%) | 1 | 112/630 (17.8%) |

능동 인식에서는 ViA처럼 실제로 빠진 연구가 있었고 기존 논문 JIGGLE은 *active sensing*이라는 표현을 썼다. 촉각에서도 KineDex·VTDexManip이 누락됐고 ViTaSCOPE는 *in-hand pose*로 검색된다. 낮은 수록률에는 수집 누락과 용어 차이가 함께 작용한다. 연구 공백으로 판단할 때는 가까운 선행의 본문과 평가를 대조한다.

## 등록 판정

| 유입 경로 | 등록 | 보류 | 기존과 중복 | 존재 확인 불가 |
|---|---:|---:|---:|---:|
| 외부 목록과 대조한 17편 | 13 | 4 | 0 | 0 |
| 능동 인식·촉각 추가 검색 19편 | 10 | 5 | 4 | 0 |

등록 ID는 `pr-1228`–`pr-1250`이다. 각 논문의 선정 이유, 공개물, 선행 관계는 심사 원장 A에 있다. 예를 들어 T-Rex가 ViTacFormer를 실물 조작의 기준선으로 사용한 표까지 확인했다. 중복 4편은 JIGGLE(`pr-1050`), 실물 능동 인식 RL(`pr-1217`), GeoDEx(`pr-0894`), ActiveVLA(`pr-0795`)다. [등록 23편](../work/sources/batches/gapfill_2026_11.yaml#L5) · [중복 판정](../work/sources/batches/gapfill_2026_11.yaml#L2741) · [T-Rex 실물 비교표](https://arxiv.org/pdf/2606.17055#page=7)

### 보류한 후보

| 논문 | 보류 이유 |
|---|---|
| [ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion](https://proceedings.mlr.press/v305/hu25c.html) | 동적 환경에서 복합 이동 지시를 조합하는 선행이다. 이번에 찾는 관측 행동·촉각 제어의 직접 비교군으로 쓰인 근거는 확인하지 못했다. |
| [Motion-Uncertainty-Aware Next-Best-View Planning for Moving Object Reconstruction](https://roboticsproceedings.org/rss22/p176.html) | 움직이는 물체의 다음 시점 계획은 직접 관련된다. 평면 병진하는 강체의 표면 재구성이 평가 목표로, 시점 선택이 로봇 조작을 개선하는지는 후속 검토 대상이다. |
| [ARCH: Hierarchical Hybrid Learning for Long-Horizon Contact-Rich Robotic Assembly](https://proceedings.mlr.press/v305/sun25b.html) | 정밀 조립의 계층형 IL·RL 구성은 유용하다. 촉각이나 관측 행동을 바꾸는 실험의 기준으로 채택할 직접 근거는 약하다. |
| [Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions](https://roboticsproceedings.org/rss20/p008.html) | 사용자 명령의 불확실성을 보정하는 원격조작 연구다. 물체 상태에 대한 로봇의 능동 관측과는 평가 변수가 다르다. |
| [ActLoc: Learning to Localize on the Move via Active Viewpoint Selection](https://proceedings.mlr.press/v305/li25b.html) | 카메라의 방위를 선택해 이동 중 위치 추정을 개선한다. 탐색 대상인 물체 상태 관측·손 조작과 평가 목적이 달라 내비게이션 후속 배치로 보류한다. |
| [Self-supervised perception for tactile skin covered dexterous hands](https://proceedings.mlr.press/v305/sharma25a.html) | 자기지도 촉각 피부 인코더는 관련성이 높다. 기존 Sparsh 계열과 센서·로봇 손을 맞춘 비교 가능 범위를 추가 확인한 후 읽기 우선순위를 판단한다. |
| [Text2Touch: Tactile In-Hand Manipulation with LLM-Designed Reward Functions](https://proceedings.mlr.press/v305/field25a.html) | LLM으로 설계한 보상을 사용해 촉각 손안 회전을 실물에 전이한다. 같은 과제의 사람 설계 보상 대비 결과가 다른 정교 조작 과제로 이어지는 범위는 미확인이다. |
| [DOGlove: Dexterous Manipulation with a Low-Cost Open-Source Haptic Force Feedback Glove](https://roboticsproceedings.org/rss21/p104.html) | DOGlove는 원격조작자에게 힘·진동을 돌려주는 공개 장치다. 로봇 정책 입력으로 쓰는 촉각의 기여와 조작자가 느낀 피드백의 기여를 분리할 때 다시 검토한다. |
| [Learning Active Perception and Manipulation via Spatio-temporal Visual Memory](https://neurips.cc/virtual/2026/poster/151254) | 공식 발표 페이지에서 ActiveMem·ActiveBench와 저자를 확인했다. 관련 연구 절과 기준선 표를 확보해 SaPaVe 등과 직접 관계를 판정한 뒤 등록한다. |

### ActiveZero 보류 재검토

2026-11-19에 NeurIPS 행사 프로그램과 저자 공개 목록을 다시 확인했다. 공식 프로그램에는 **포스터 채택**으로 기록돼 있다. 초록은 ActiveMem에 카메라 행동이 포함된 400만 에피소드와 49개 장면이 있으며, ActiveBench에서 시각 질의응답과 시뮬레이션 조작을 평가한다고 밝힌다. 아래 수치와 범위의 출처는 발표 초록이다. [공식 발표](https://neurips.cc/virtual/2026/poster/151254) · [공식 프로그램 데이터](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)

| 확인할 조건 | 확인한 사실 | 판정에 필요한 근거 |
|---|---|---|
| 카메라 행동 감독 | 데이터에 카메라 행동이 들어 있다. | 관측 행동의 정답을 어디서 얻는지, 어떤 손실에서 쓰는지 설명한 방법 절 |
| 학습·평가 장면 분리 | 49는 ActiveMem의 장면 수다. | ActiveBench의 학습·평가 장면 ID 또는 분할표와 두 자료의 중복 여부 |
| 같은 관측 예산의 기준선 | 초록에는 실물·시뮬레이션 비교가 있다. | 기준선별 카메라 이동 횟수·사용 프레임·실행 시간, 같은 예산에서의 결과표 |

**B 보류를 유지한다.** 행사 데이터의 `paper_pdf_url`은 비어 있고, 연결된 OpenReview 원문과 부록은 이번 접근에 403을 반환했다. 첫 저자의 공개 목록과 arXiv에서도 일치하는 원고를 찾지 못했다. 관측 행동의 감독, 장면 분할, 예산을 확인할 수 있는 원문 또는 실험 부록이 공개되면 ViA·ActiveMimic·SaPaVe와 대조한다. [OpenReview](https://openreview.net/forum?id=bkasRJF9pc) · [첫 저자 연구 목록](https://zhoues.github.io/)

### 등록 전 대조에서 남은 판본 문제

| 외부 제목 | 원장 대조 후보 | 확인할 차이 |
|---|---|---|
| [BEHAVIOR-1K: A human-centered, embodied AI benchmark with 1, 000 everyday activities and realistic simulation](https://arxiv.org/html/2405.14093#bib.bib171) | pr-0730 | CoRL 발표와 후속 확장 원고가 같은 등록 단위인지 확인한다. |
| [Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos](https://doi.org/10.1109/icra57385.2026.11697552) | pr-0186 | 공식 프로그램과 DOI 표제에서 Dexterous 표기가 달라 저자·판본을 확인한다. |
| [Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning](https://arxiv.org/pdf/2506.01953) | pr-0116 | Foundation Model과 VLA Model 두 표제가 어느 발표 판본을 가리키는지 확인한다. |

<a id="search-queries"></a>

## 추가 검색식과 판정 범위

공식 학회 목록에서 유니코드를 NFKC로 정규화하고 대소문자를 구분하지 않고 검색했다. 같은 식을 등록 전 원장의 전 연도에 적용하면 G1은 6편(`pr-0795`, `pr-0805`, `pr-1030`, `pr-1050`, `pr-1217`, `pr-1224`), G2는 3편(`pr-0849`, `pr-0893`, `pr-0894`)이다. 학회별 적중 수는 위의 기준 목록 표에 있다.

| 번호 | 제목 검색식 |
|---|---|
| G1 | <code>\bactive (?:visual &#124;3d &#124;object )?(?:perception&#124;pose estimation)&#124;next.best.view&#124;active view(?:point)? (?:selection&#124;planning)&#124;viewpoint (?:planning&#124;selection)&#124;active (?:grasp&#124;vision)&#124;active sensing</code> |
| G2 | <code>(?=.*(?:tactile&#124;haptic&#124;touch sensing&#124;touch feedback))(?=.*(?:dexterous&#124;dexterity&#124;in.hand&#124;multifinger&#124;multi.finger&#124;robotic hand))</code> |

<details>
<summary>arXiv·CVF·학회·저자 페이지에서 사용한 검색어</summary>

~~~text
2024 2025 2026 active perception robot grasp active viewpoint planning GenNBV active vision manipulation CVPR CoRL next best view
2024 2025 2026 tactile dexterous in-hand rotation manipulation VTDexManip KineDex ViTacFormer dataset RSS CoRL
"VTDexManip" "Blind Dexterous Grasping" tactile CoRL openreview arXiv
"PTLD" privileged tactile latent distillation "HuG" humanoid affordance grasping CoRL
"Learning Active Perception and Manipulation via Spatio-temporal Visual Memory" "ActiveMimic" robotics 2026
"Real-World Reinforcement Learning of Active Perception Behaviors" pdf
"Learning Active Perception and Manipulation via Spatio-temporal Visual Memory" NeurIPS Yibo Li site:neurips.cc
VTDexManip ICLR 2025 visual tactile benchmark Qi PDF proceedings.iclr.cc paper
"Enshen Zhou" "Spatio-temporal Visual Memory" active manipulation AVM arxiv NeurIPS spatio-temporal Enshen 2026
ViTaSCOPE visuo-tactile implicit representation in-hand pose extrinsic contact estimation arXiv authors
ActiveZero Enshen Zhou ActiveMem ActiveBench arXiv manipulation visual memory paper
"VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning" robotics paper arXiv
"Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning" robotics paper arXiv
"PTLD: Sim-to-Real Privileged Tactile Latent Distillation for dexterous manipulation" robotics paper arXiv
"Learning Active Perception and Manipulation via Spatio-temporal Visual Memory" robotics paper arXiv
"HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception" robotics paper arXiv
"ActiveMimic: Egocentric Video Pretraining with Active Perception" robotics paper arXiv
"Real-World Reinforcement Learning of Active Perception Behaviors" robotics paper arXiv
"PTLD: Sim-to-Real Privileged Tactile Latent Distillation for dexterous manipulation"
"HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception"
"ActiveMimic: Egocentric Video Pretraining with Active Perception"
~~~

</details>

추가로 탐색할 표현은 능동 인식의 *gaze control*, *eye-in-hand exploration*, *information-gathering action*과 촉각의 *shear field*, *extrinsic contact localization*, *tactile reorientation*이다. 검색 적중과 실제 심사 대상을 구분했다. [당시 검색 결과와 미판정 제목](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/research/GAPFILL.md#검색-결과의-범위와-원인-해석)

## 판본과 공개 범위

- ViTaSCOPE의 저자 사이트는 코드 링크를 Coming Soon으로 표시한다. PTLD의 프로젝트가 가리키는 저장소는 이번 확인에서 접근되지 않아 공개 여부를 unknown으로 두었다. ActiveMimic의 공개로 확인한 코드는 데이터 처리 범위다. [ViTaSCOPE](https://jayjunlee.github.io/vitascope/) · [PTLD](https://akashsharma02.github.io/ptld-website/) · [ActiveMimic](https://github.com/leolin9248/activemimic-data)
- Real-World Reinforcement Learning of Active Perception Behaviors는 NeurIPS 2025 발표지만 proceedings 페이지의 citation publication date는 2026-04-23이다. 행사 연도와 온라인 게시일 필드를 혼용하면 연도가 달라진다. 동일 논문으로 판정했다. [공식 게재 페이지](https://papers.nips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html)
- Self-supervised perception for tactile skin covered dexterous hands의 PMLR 초록은 PercepSkin, 연결된 원고는 Sparsh-skin이라는 이름을 쓴다. 표제와 저자가 일치한다. 별도 논문으로 세지 않았다. [PMLR](https://proceedings.mlr.press/v305/sharma25a.html) · [원고 첫 장](https://raw.githubusercontent.com/mlresearch/v305/main/assets/sharma25a/sharma25a.pdf#page=1)
