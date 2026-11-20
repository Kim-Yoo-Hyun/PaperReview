# 외부 목록 대비 등록 현황

아래는 등록 전의 기준 측정이다. 이후 36편을 심사해 23편을 추가한 결과와 동일한 분모로 다시 계산한 비율은 [누락 논문 등록 심사](./GAPFILL.md)에 있다.

2026-11-19에 레지스트리의 ID와 제목 1,227쌍을 외부 목록 25개와 대조했다. 아래에서 일치는 등록된 논문 수, 분모는 목록 내 중복을 정리한 항목 수다. 전체 44,911건 중 586건, 로보틱스 세부 주제 제목 필터에 걸린 1,401건 중 159건이 일치했다. [후보 YAML](../work/sources/batches/missing_candidates_2026.yaml) · [제목별 판정 원자료](../work/sources/coverage_titles.jsonl.gz)

## 기준 목록별 커버리지

| 목록 · 원문 | 전체 일치/분모 | 주제 필터 일치/분모 | 필터 내 동일성 미결 |
|---|---:|---:|---:|
| [VLA · Concepts, Progress, Applications and Challenges](https://arxiv.org/html/2505.04769) · `surveyV` | 66/297 (22.2%) | 38/95 (40.0%) | 0 |
| [Humanoid Locomotion and Manipulation](https://arxiv.org/html/2501.02116) · `surveyH` | 53/423 (12.5%) | 12/90 (13.3%) | 0 |
| [VLA · A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/html/2405.14093) · `surveyM` | 168/766 (21.9%) | 55/217 (25.3%) | 0 |
| [RSS 2024](https://roboticsproceedings.org/rss20/) · `rss24` | 29/134 (21.6%) | 7/11 (63.6%) | 0 |
| [CoRL 2024](https://proceedings.mlr.press/v270/) · `corl24` | 27/264 (10.2%) | 7/16 (43.8%) | 0 |
| [ICLR 2024](https://iclr.cc/static/virtual/data/iclr-2024-orals-posters.json) · `iclr24` | 9/2296 (0.4%) | 0/1 (0.0%) | 0 |
| [NeurIPS 2024](https://neurips.cc/static/virtual/data/neurips-2024-orals-posters.json) · `neurips24` | 6/4537 (0.1%) | 1/10 (10.0%) | 0 |
| [ICRA 2024](https://api.crossref.org/works?filter=container-title%3A2024+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra24` | 12/1766 (0.7%) | 1/52 (1.9%) | 0 |
| [IROS 2024](https://api.crossref.org/works?filter=container-title%3A2024+IEEE%2FRSJ+International+Conference+on+Intelligent+Robots+and+Systems+%28IROS%29%2Ctype%3Aproceedings-article) · `iros24` | 0/1587 (0.0%) | 0/70 (0.0%) | 0 |
| [RSS 2025](https://roboticsproceedings.org/rss21/) · `rss25` | 65/163 (39.9%) | 20/26 (76.9%) | 0 |
| [CoRL 2025](https://proceedings.mlr.press/v305/) · `corl25` | 22/263 (8.4%) | 7/29 (24.1%) | 0 |
| [ICLR 2025](https://iclr.cc/static/virtual/data/iclr-2025-orals-posters.json) · `iclr25` | 49/3830 (1.3%) | 1/11 (9.1%) | 0 |
| [NeurIPS 2025](https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json) · `neurips25` | 52/5858 (0.9%) | 16/36 (44.4%) | 0 |
| [ICRA 2025](https://api.crossref.org/works?filter=container-title%3A2025+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra25` | 13/1609 (0.8%) | 4/61 (6.6%) | 0 |
| [IROS 2025](https://api.crossref.org/works?filter=container-title%3A2025+IEEE%2FRSJ+International+Conference+on+Intelligent+Robots+and+Systems+%28IROS%29%2Ctype%3Aproceedings-article) · `iros25` | 12/1985 (0.6%) | 2/83 (2.4%) | 0 |
| [RSS 2026](https://roboticsproceedings.org/rss22/) · `rss26` | 36/210 (17.1%) | 9/34 (26.5%) | 0 |
| [CoRL 2026](https://www.corl.org/program/accepted-papers) · `corl26` | 13/687 (1.9%) | 9/177 (5.1%) | 0 |
| [ICLR 2026](https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json) · `iclr26` | 65/5468 (1.2%) | 19/49 (38.8%) | 0 |
| [NeurIPS 2026](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) · `neurips26` | 4/9110 (0.0%) | 2/113 (1.8%) | 0 |
| [ICRA 2026](https://api.crossref.org/works?filter=container-title%3A2026+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · `icra26` | 23/1881 (1.2%) | 15/152 (9.9%) | 1 |
| [IROS 2026](https://2026.ieee-iros.org/program/paper-index/) · `iros26` | 7/1929 (0.4%) | 2/170 (1.2%) | 0 |
| [Awesome Embodied VLA/VA/VLN](https://raw.githubusercontent.com/jonyzhang2023/awesome-embodied-vla-va-vln/main/README.md) · `awesome` | 71/253 (28.1%) | 43/141 (30.5%) | 1 |
| [Stanford ILIAD](https://iliad.stanford.edu/publications/) · `stanford` | 10/124 (8.1%) | 2/2 (100.0%) | 0 |
| [NVIDIA GEAR](https://research.nvidia.com/labs/gear/publications/) · `gear` | 18/47 (38.3%) | 6/10 (60.0%) | 0 |
| [Physical Intelligence](https://www.pi.website/research) · `pi` | 5/7 (71.4%) | 4/6 (66.7%) | 0 |

## 가장 적게 수록한 하위 주제

| 순위 | 주제 | 일치/분모 | 동일성 미결 |
|---:|---|---:|---:|
| 1 | 능동 로봇 인식 | 1/40 (2.5%) | 0 |
| 2 | 촉각 조작 | 10/246 (4.1%) | 0 |
| 3 | 실패 감지·복구 | 1/19 (5.3%) | 0 |
| 4 | 시연 수집·전이 | 11/129 (8.5%) | 0 |
| 5 | 휴머노이드 전신·보행 | 17/196 (8.7%) | 0 |
| 6 | 지시 기반 내비게이션 | 12/123 (9.8%) | 0 |
| 7 | 접촉 조립·삽입 | 9/88 (10.2%) | 0 |
| 8 | VLA 행동정책 | 105/630 (16.7%) | 1 |

처음 다섯 행이 조사한 여덟 주제 중 커버리지가 낮은 순서다. 한 논문은 여러 주제에 들어갈 수 있다. 이 비율은 문헌 수집의 빈틈을 뜻한다. 연구 질문의 독창성은 가장 가까운 선행의 방법과 실험까지 대조해야 판단할 수 있다.

## 대조 범위와 재검산

- 서베이 3편 모두 HTML 본문의 참고문헌을 직접 열었다. 원문 항목은 VLA Concepts 299개, VLA for Embodied AI 786개, 휴머노이드 424개다. VLA for Embodied AI의 제목 미식별 1개를 제외하고 중복을 제거했다. 인용된 웹 자료와 책도 제목을 식별하면 전체 분모에 포함했다. 서베이·연구실 목록은 게시된 전 기간, 학회는 2024–2026년 행사 연도, 큐레이션은 VLA/WAM의 해당 연도 구간이다.
- CoRL은 PMLR 및 2026 공식 채택 목록, RSS는 proceedings, ICLR·NeurIPS는 공식 oral/poster 자료를 썼다. ICRA·IROS는 IEEE가 Crossref에 기탁한 해당 연도 proceedings-article 전체를 커서로 조회했다. IROS 2026은 저널 발표도 포함하는 공식 발표 색인을 사용했다. 프로그램 등재와 출판 상태를 구분한다.
- 전체 분모에는 AI 학회의 비로보틱스 논문도 포함한다. 주제 분모에는 촉각·조립·휴머노이드·능동/상호작용 인식·실패·지시 내비게이션·VLA·시연 관련 제목 패턴에 걸린 항목만 포함한다. 제목에 로봇 맥락이 생략되면 누락될 수 있고, 타 분야의 동음어가 포함될 수 있다. 모든 로보틱스 논문에 대한 회수율은 미측정이다.
- HTML 엔티티·유니코드·그리스 문자·대소문자·구두점을 정규화했다. 완전 일치와 판정한 제목 변형만 분자에 넣었다. 검토 후보는 공통 희소 단어를 포함하고 문자열 또는 단어 겹침이 높은 제목이다. 의심 사례는 분모에 남기고 미결로 기록했다. 학회 간 교집합은 같은 등록 ID 또는 정규화된 외부 제목으로 한 번 센다.
- 압축 JSON Lines 첫 행은 목록 주소·검색 범위·정규식·원장 ID/제목 해시다. 이후 행마다 원제, 정규화 제목, 출처별 링크, 주제, 등록 ID와 판정이 있다. 동일 목록의 같은 등록 ID를 한 번 세면 표를 재현할 수 있다. 서로 다른 제목이 같은 미등록 연구인지 본문으로 전수 판별하지 않았다.

## 먼저 검토할 후보

등록된 표제와 대조하고 저자 초록·공식 발표 또는 게재 목록까지 확인한 17편이다. 등록 전에는 공개물, 정확한 과업 범위, 버전 식별자를 다시 확인한다. 근거가 많은 순서와 연구 기여의 중요도는 별개다.

| 논문 | 분야 또는 등록 검토 이유 | 발견 목록 |
|---|---|---|
| [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html) | 로봇 정책이 관측마다 다른 깊이에서 추론을 종료하도록 학습한다. | surveyV, surveyM, neurips24, awesome |
| [Improving Vision-Language-Action Model with Online Reinforcement Learning](https://doi.org/10.1109/icra55743.2025.11127299) | 로봇 상호작용에서 얻은 RL 개선을 감독학습과 교대로 VLA에 반영한다. | surveyV, surveyM, icra25, awesome |
| [MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models](https://doi.org/10.1109/icra55743.2025.11128601) | 사족 로봇 VLA에서 품질이 다른 경험으로 행동 가치를 학습한다. | surveyV, surveyM, icra25, awesome |
| [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://openreview.net/forum?id=5TiiTY1fK3) | 짧은 시각 이력과 긴 의미 이력을 다른 형식으로 보존하는 로봇 정책이다. | corl26, awesome, pi |
| [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://proceedings.mlr.press/v305/kwok25a.html) | VLA가 생성한 후보 행동을 검증해 실행할 행동을 선택한다. | surveyM, corl25, awesome |
| [T-Rex: Tactile-Reactive Dexterous Manipulation](https://openreview.net/forum?id=KdaClHHEUt) | 촉각 시계열에 빠르게 반응하는 다지 조작 정책을 학습한다. | corl26, gear |
| [Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding](https://roboticsproceedings.org/rss22/p005.html) | 접촉의 미래 상태를 예측해 다지 손의 순응 제어 목표를 만든다. | rss26 |
| [Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning](https://roboticsproceedings.org/rss20/p058.html) | 잡음 제거 세계 모델을 이용해 험지 보행을 위한 휴머노이드 제어기를 학습한다. | surveyH, rss24 |
| [CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks](https://proceedings.mlr.press/v305/li25h.html) | 전신 원격조작에서 상·하체를 함께 제어하고 누적 위치 오차를 수정한다. | corl25 |
| [ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion](https://proceedings.mlr.press/v305/hu25c.html) | 복합 지시를 구성하는 이동 조건별로 확산 모델을 학습한다. | corl25 |
| [Vision in Action: Learning Active Perception from Human Demonstrations](https://proceedings.mlr.press/v305/xiong25a.html) | 사람의 시선 이동 시연으로 양팔 조작 중 카메라를 움직이는 정책을 학습한다. | corl25 |
| [Motion-Uncertainty-Aware Next-Best-View Planning for Moving Object Reconstruction](https://roboticsproceedings.org/rss22/p176.html) | 움직이는 물체의 표면을 재구성할 때 이동 지연과 운동 불확실성을 시점 선택에 반영한다. | rss26 |
| [Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection](https://openreview.net/forum?id=JQvRoFU5aS) | 실행 전 상상한 시각적 이정표에서 복구 목표를 선택해 VLA를 재조건화한다. | corl26 |
| [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](https://openreview.net/forum?id=mg7X6SFE75) | 미세조정한 VLA의 실행 실패를 가벼운 감지기로 추적한다. | corl26 |
| [ARCH: Hierarchical Hybrid Learning for Long-Horizon Contact-Rich Robotic Assembly](https://proceedings.mlr.press/v305/sun25b.html) | 긴 조립 과업에서 상위 모방 정책이 하위 정밀 조립 기술과 매개변수를 선택한다. | corl25 |
| [Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions](https://roboticsproceedings.org/rss20/p008.html) | 저차원 사용자 명령을 로봇 행동으로 변환할 때 예측 불확실성을 추정한다. | rss24 |
| [HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning](https://openreview.net/forum?id=9kXz22fI7a) | 소수 시연과 전신 계획으로 휴머노이드 이동 조작 학습 데이터를 생성한다. | corl26, gear |

버전별 원제 대조로 SafeVLA, 평가 taxonomy, Moto를 기존 항목과 연결했다. RoboCasa는 RSS와 arXiv의 표제가 달랐지만 저자 목록과 발표 시점이 일치했다. [SafeVLA 초판](https://arxiv.org/abs/2503.03480v1) · [개정판](https://arxiv.org/abs/2503.03480) · [RoboCasa RSS](https://roboticsproceedings.org/rss20/p050.html) · [RoboCasa arXiv](https://arxiv.org/abs/2406.02523)

## 동일 연구 여부 미결

| 외부 제목 | 원장 대조 후보 | 확인할 차이 |
|---|---|---|
| [BEHAVIOR-1K: A human-centered, embodied AI benchmark with 1, 000 everyday activities and realistic simulation](https://arxiv.org/html/2405.14093#bib.bib171) | pr-0730 | CoRL 발표와 후속 확장 원고가 같은 등록 단위인지 확인한다. |
| [Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos](https://doi.org/10.1109/icra57385.2026.11697552) | pr-0186 | 공식 프로그램과 DOI 표제에서 Dexterous 표기가 달라 저자·판본을 확인한다. |
| [Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning](https://arxiv.org/pdf/2506.01953) | pr-0116 | Foundation Model과 VLA Model 두 표제가 어느 발표 판본을 가리키는지 확인한다. |
