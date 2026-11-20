# 누락 논문 등록 심사

2026-11-19에 기존 원장 1,227편을 기준으로 36편을 심사했다. 지난 외부 대조 후보 17편을 모두 포함했고 능동 로봇 인식과 촉각 기반 정교 조작 검색에서 19편을 추가로 심사했다. 각 후보의 실제 서지를 먼저 확인하고, 중복 판정 뒤 등록 가치를 검토했다. [전체 심사 YAML](../work/sources/batches/gapfill_2026_11.yaml) · [등록 전 외부 대조](./EXTERNAL_COVERAGE.md)

| 최초 유입 | A 등록 | B 보류 | C 기존 등록 | D 확인 불가 |
|---|---:|---:|---:|---:|
| F | 13 | 4 | 0 | 0 |
| G | 10 | 5 | 4 | 0 |

등록한 23편은 로봇 연구의 비교에 쓸 수 있는 방법·시스템·데이터셋이며 모두 NEXT(부록 A의 2등급)다. 최근 논문의 후속 채택 횟수는 추정하지 않았다. 직접 확인한 후속 사용의 예로 T-Rex는 ViTacFormer를 실물 촉각 조작의 비교 정책으로 사용한다. [T-Rex 실기 비교표](https://arxiv.org/pdf/2606.17055#page=7)

## A. 등록한 논문

| 등록 ID | 논문 | 연구에서 쓰는 이유 |
|---|---|---|
| pr-1228 | [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html) | 계산 예산에 따라 같은 VLA의 실행 깊이를 바꾸는 비교 기준이다. |
| pr-1229 | [Improving Vision-Language-Action Model with Online Reinforcement Learning](https://arxiv.org/abs/2501.16664) | 온라인 RL을 VLA에 직접 적용하는 방식과 RL·감독학습을 교대하는 방식을 대조할 기준이다. |
| pr-1230 | [MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models](https://arxiv.org/abs/2503.08007) | 사족 로봇에서 VLA를 행동 가치 함수로 학습하는 경로를 대표한다. |
| pr-1231 | [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596) | 단기 영상 이력과 장기 의미 이력이 서로 다른 행동 오류를 해결하는지 시험할 기준이다. |
| pr-1232 | [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://proceedings.mlr.press/v305/kwok25a.html) | 추가 학습 없이 행동 후보를 더 뽑는 효과와 학습한 검증기가 주는 이득을 분리할 기준이다. |
| pr-1233 | [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055) | 접촉 중 빠른 촉각 반응을 학습할 시연 자료와 서로 다른 주기의 VLA 구조를 함께 제시한다. |
| pr-1234 | [Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding](https://roboticsproceedings.org/rss22/p005.html) | 촉각을 정책의 추가 입력으로 쓰는 경우와 미래 접촉을 실행 제어 목표로 만드는 경우를 직접 비교한다. |
| pr-1235 | [Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning](https://roboticsproceedings.org/rss20/p058.html) | 잡음 제거 세계 모델과 보행 RL을 실제 불규칙 지형에 전이한 대표 제어 사례다. |
| pr-1236 | [CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks](https://proceedings.mlr.press/v305/li25h.html) | 전신 시연을 수집할 때 제어기와 실제 위치의 차이를 폐루프로 보정하는 시스템 기준이다. |
| pr-1237 | [Vision in Action: Learning Active Perception from Human Demonstrations](https://proceedings.mlr.press/v305/xiong25a.html) | 카메라 움직임을 학습한 양팔 정책과 고정 카메라 정책을 실물에서 비교한 능동 인식의 직접 선행이다. |
| pr-1238 | [Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection](https://arxiv.org/abs/2606.09258) | 복구가 가능한 시점에서 미래 시각 목표만 바꾸는 대조군을 제공한다. |
| pr-1239 | [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](https://arxiv.org/abs/2606.21386) | 실패 감지의 정확도와 알림 시간을 함께 평가하는 지표와 VLA용 감지 기준을 제공한다. |
| pr-1240 | [HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning](https://arxiv.org/abs/2605.27724) | 전신 계획으로 이동 조작 시연을 만드는 기법과 휴머노이드용 시뮬레이션 벤치마크를 함께 제공한다. |
| pr-1241 | [Active Perception for Grasp Detection via Neural Graspness Field](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4364fef031fdf7bfd9d1c9c56b287084-Abstract-Conference.html) | 재구성 품질 대신 파지 목표에 대한 불확실성으로 카메라 시점을 고르는 기준이다. |
| pr-1242 | [KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation](https://proceedings.mlr.press/v305/zhang25l.html) | 접촉력 시연을 수집하고 힘을 제어하는 정책까지 연결하는 촉각 모방학습의 기준이다. |
| pr-1243 | [UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation](https://proceedings.mlr.press/v305/wu25d.html) | 새 물체의 손안 자세·추적·불확실성을 같은 촉각 추정기에서 평가하는 비교 기준이다. |
| pr-1244 | [ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation](https://roboticsproceedings.org/rss21/p054.html) | 손안 물체의 자세와 물체가 환경에 닿는 위치를 함께 추정하는 접촉 상태 기준이다. |
| pr-1245 | [VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e19b6f65791e350347bcff8a3955cb5b-Abstract-Conference.html) | 희소 이진 촉각의 기여를 같은 RL 과제에서 비교할 수 있는 데이터셋과 벤치마크다. |
| pr-1246 | [ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation](https://roboticsproceedings.org/rss22/p129.html) | 행동과 미래 촉각의 공동 예측을 장시간 실물 다지 조작에서 대조할 기준이다. |
| pr-1247 | [Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning](https://arxiv.org/abs/2606.11767) | 시각이 없는 다지 파지에서 촉각 접촉 보정과 RL 전문가 증류를 검토할 기준이다. |
| pr-1248 | [PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation](https://arxiv.org/abs/2603.04531) | 실물의 특권 관측을 학습 때만 사용해 촉각 상태 추정기를 증류하는 전이 기준이다. |
| pr-1249 | [HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception](https://arxiv.org/abs/2611.01659) | 카메라 탐색과 파지 가능성 판단에 전신 균형 제약을 결합한 실기 휴머노이드 기준이다. |
| pr-1250 | [ActiveMimic: Egocentric Video Pretraining with Active Perception](https://arxiv.org/abs/2606.06194) | 사람의 머리 움직임을 관측 행동으로 학습하고 실제 로봇으로 전이하는 직접 선행이다. |

## B. 보류한 논문

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

심사 후보 중 제외로 판정한 논문은 0편이다.

### ActiveZero 보류 재검토

2026-11-19에 NeurIPS 행사 프로그램과 저자 공개 목록을 다시 확인했다. 공식 프로그램에는 **포스터 채택**으로 기록돼 있다. 초록은 ActiveMem에 카메라 행동이 포함된 400만 에피소드와 49개 장면이 있으며, ActiveBench에서 시각 질의응답과 시뮬레이션 조작을 평가한다고 밝힌다. 아래 수치와 범위의 출처는 발표 초록이다. [공식 발표](https://neurips.cc/virtual/2026/poster/151254) · [공식 프로그램 데이터](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)

| 확인할 조건 | 확인한 사실 | 판정에 필요한 근거 |
|---|---|---|
| 카메라 행동 감독 | 데이터에 카메라 행동이 들어 있다. | 관측 행동의 정답을 어디서 얻는지, 어떤 손실에서 쓰는지 설명한 방법 절 |
| 학습·평가 장면 분리 | 49는 ActiveMem의 장면 수다. | ActiveBench의 학습·평가 장면 ID 또는 분할표와 두 자료의 중복 여부 |
| 같은 관측 예산의 기준선 | 초록에는 실물·시뮬레이션 비교가 있다. | 기준선별 카메라 이동 횟수·사용 프레임·실행 시간, 같은 예산에서의 결과표 |

**B 보류를 유지한다.** 행사 데이터의 `paper_pdf_url`은 비어 있고, 연결된 OpenReview 원문과 부록은 이번 접근에 403을 반환했다. 첫 저자의 공개 목록과 arXiv에서도 일치하는 원고를 찾지 못했다. 관측 행동의 감독, 장면 분할, 예산을 확인할 수 있는 원문 또는 실험 부록이 공개되면 ViA·ActiveMimic·SaPaVe와 대조한다. [OpenReview](https://openreview.net/forum?id=bkasRJF9pc) · [첫 저자 연구 목록](https://zhoues.github.io/)

## C. 기존 등록과 중복

| 기존 ID | 확인된 외부 논문 |
|---|---|
| pr-1050 | [JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments](https://roboticsproceedings.org/rss20/p007.html) |
| pr-1217 | [Real-World Reinforcement Learning of Active Perception Behaviors](https://papers.nips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) |
| pr-0894 | [GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty](https://roboticsproceedings.org/rss21/p057.html) |
| pr-0795 | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html) |

## D. 존재 불확실 또는 확인 불가

0편. 삭제 권장도 0편이다. OpenReview 페이지를 열 수 없을 때는 공식 행사 목록, 저자 원문, 정식 proceedings를 대조했다. ActiveZero는 공식 발표 페이지에서 존재가 확인돼 B에 포함했다. [NeurIPS 발표](https://neurips.cc/virtual/2026/poster/151254)

## G. 하위 주제 검색과 측정

기간은 2024–2026년 행사 기준이다. 능동 인식은 로봇이 관측을 바꾸는 경우, 촉각은 손안 조작·다지 손과 직접 이어지는 경우를 중심으로 선별했다. 수술·항법·사람 피드백처럼 경계에 있는 논문은 로봇 행동과의 관계를 개별 확인했다.

지난 외부 대조의 분모를 고정해 등록 전후를 계산했다. 같은 원자료에서 새로 등록한 ID와 원문 링크가 일치하는 행을 더했다. 이번 검색에서 확장한 동의어는 과거 분모에 소급하지 않았다.

| 동일한 제목 필터 | 등록 전 | 등록 후 |
|---|---:|---:|
| 능동 로봇 인식 | 1/40 (2.5%) | 5/40 (12.5%) |
| 촉각 조작 | 10/246 (4.1%) | 17/246 (6.9%) |
| VLA 행동정책 | 105/630 (16.7%) | 112/630 (17.8%) |

### 실제 검색식과 대상

공식 목록 제목에 NFKC 정규화를 적용하고 대소문자를 구분하지 않고 다음 정규식으로 검색했다. arXiv·저자 페이지·프로시딩은 후보 서지 및 공개물 확인에도 사용했다.

| 번호 | 제목 검색식 |
|---|---|
| G1 | <code>\bactive (?:visual &#124;3d &#124;object )?(?:perception&#124;pose estimation)&#124;next.best.view&#124;active view(?:point)? (?:selection&#124;planning)&#124;viewpoint (?:planning&#124;selection)&#124;active (?:grasp&#124;vision)&#124;active sensing</code> |
| G2 | <code>(?=.*(?:tactile&#124;haptic&#124;touch sensing&#124;touch feedback))(?=.*(?:dexterous&#124;dexterity&#124;in.hand&#124;multifinger&#124;multi.finger&#124;robotic hand))</code> |

| 검색한 공식 목록 | 고유 제목 | G1 일치 | G2 일치 |
|---|---:|---:|---:|
| [corl24](https://proceedings.mlr.press/v270/) | 264 | 0 | 0 |
| [rss24](https://roboticsproceedings.org/rss20/) | 134 | 1 | 0 |
| [iclr24](https://iclr.cc/static/virtual/data/iclr-2024-orals-posters.json) | 2,296 | 0 | 0 |
| [neurips24](https://neurips.cc/static/virtual/data/neurips-2024-orals-posters.json) | 4,537 | 2 | 0 |
| [corl25](https://proceedings.mlr.press/v305/) | 263 | 2 | 4 |
| [rss25](https://roboticsproceedings.org/rss21/) | 163 | 0 | 4 |
| [iclr25](https://iclr.cc/static/virtual/data/iclr-2025-orals-posters.json) | 3,830 | 1 | 1 |
| [neurips25](https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json) | 5,858 | 1 | 0 |
| [corl26](https://www.corl.org/program/accepted-papers) | 687 | 2 | 6 |
| [rss26](https://roboticsproceedings.org/rss22/) | 210 | 1 | 2 |
| [iclr26](https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json) | 5,468 | 4 | 1 |
| [neurips26](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) | 9,110 | 5 | 1 |

웹 검색은 arXiv·CVF·ICLR·NeurIPS·저자 연구실을 대상으로 아래 질의를 사용했다. 공개된 원고는 방법·관련 연구·기준선 표에서 직접 관계를 확인했다. 중복 판정에는 구두점·Unicode를 정규화한 표제와 별칭, arXiv·DOI·OpenReview 식별자 및 가장 비슷한 기존 제목을 사용했다.

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

### 등록 전 원장에 있던 논문

아래는 같은 G 검색식을 기존 원장 전체 제목에 적용한 결과다. 연도 제한은 외부 후보 발견에 적용했고, 기존 연구와의 중복 검사는 원장 전체 연도에 대해 수행했다. 제목에 쓰이지 않은 동의어는 집계되지 않는다.

| 검색식 | 등록 전 ID | 제목 |
|---|---|---|
| G1 | pr-0795 | ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation |
| G1 | pr-0805 | SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics |
| G1 | pr-1030 | Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation |
| G1 | pr-1050 | JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments |
| G1 | pr-1217 | Real-World Reinforcement Learning of Active Perception Behaviors |
| G1 | pr-1224 | Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes |
| G2 | pr-0849 | DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation |
| G2 | pr-0893 | PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands |
| G2 | pr-0894 | GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty |

### 검색 결과의 범위와 원인 해석

공식 목록 검색에 일치했지만 이번 심사에 포함되지 않은 제목은 아래와 같다.

| 추가 검색 결과 | 처리 |
|---|---|
| [Improving Viewpoint-Independent Object-Centric Representations through Active Viewpoint Selection](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2360da01c2ed6592bb691326424de184-Abstract-Conference.html) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands](https://roboticsproceedings.org/rss21/p056.html) | 기존 등록 pr-0893 |
| [Mind the GAP: Glimpse-based Active Perception improves generalization and sample efficiency of visual reasoning](https://openreview.net/forum?id=iXCeQ2m6vT) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [FingerEye: Learning Dexterous Manipulation with Continuous Vision-Tactile Sensing](https://openreview.net/forum?id=RAA96LpIxJ) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Demonstration with Simulated Interaction](https://openreview.net/forum?id=suRtJLXVxI) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing](https://openreview.net/forum?id=ALlLaCTHKQ) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [PEERING INTO THE UNKNOWN: ACTIVE VIEW SELECTION WITH NEURAL UNCERTAINTY MAPS FOR 3D RECONSTRUCTION](https://openreview.net/forum?id=e7gbgdw05A) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands](https://openreview.net/forum?id=dT3ZciXvNX) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [AdaViewPlanner: Adapting Video Diffusion Models for Viewpoint Planning in 4D Scenes](https://openreview.net/forum?id=c2EfS9E5CJ) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking](https://openreview.net/forum?id=r2g8TV4nJy) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [APPLE: Toward General Active Perception via Reinforcement Learning](https://openreview.net/forum?id=hU2gT2Ucua) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Towards Scalable Egocentric HOI for Humanoids: Benchmarking Whole-Body Dexterous Interaction with Tactile Prediction](https://openreview.net/forum?id=0UDyFy4rIa) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Learning Actionable Information Landscapes for Multimodal Active Sensing in Hawkmoths](https://openreview.net/forum?id=4RHseRnmZo) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Do Glimpse Policies See Like Humans? A Behavioral Audit Reveals Dissociated Viewing Priors in Classification-Trained Active Vision](https://openreview.net/forum?id=GBLeJAfMvA) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [I-Perceive: A Foundation Model for Vision-Language Active Perception](https://openreview.net/forum?id=tQvz32bRpB) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |
| [Spherical Bayesian Experimental Design for Active View Selection in 3D Gaussian Splatting](https://openreview.net/forum?id=k2OeOyeBRk) | 검색 적중. 이번 배치 밖이며 포함 여부 미판정 |

능동 인식은 (a) 수집 누락과 (c) 키워드 차이가 함께 작용한 것으로 본다. ViA처럼 실제로 빠져 있던 실기 연구가 있고, 등록돼 있던 JIGGLE은 제목에서 active sensing을 쓴다. 촉각 정교 조작에서도 KineDex·VTDexManip이 빠져 있었고, ViTaSCOPE는 dexterous 대신 in-hand pose와 extrinsic contact를 쓴다. (b) 분야 전체의 논문 수가 적다는 판단에는 이 자료만으로 근거가 부족하다.

추가 검색어는 능동 인식의 경우 gaze control, eye-in-hand exploration, information-gathering action, task-driven camera placement다. 촉각은 shear field, extrinsic contact localization, fingertip force feedback, tactile reorientation까지 넓힐 수 있다.

## 낮은 확신과 외부 목록 표기

- ActiveZero는 초록에 ActiveMem·ActiveBench가 있지만 본문 baseline 표와 분할을 확인하지 못했다. 이름이 비슷한 ActiveArena나 SaPaVe에 연결하지 않았다. [공식 발표](https://neurips.cc/virtual/2026/poster/151254)
- ViTaSCOPE의 저자 사이트는 코드 링크를 Coming Soon으로 표시한다. PTLD의 프로젝트가 가리키는 저장소는 이번 확인에서 접근되지 않아 공개 여부를 unknown으로 두었다. ActiveMimic의 공개로 확인한 코드는 데이터 처리 범위다. [ViTaSCOPE](https://jayjunlee.github.io/vitascope/) · [PTLD](https://akashsharma02.github.io/ptld-website/) · [ActiveMimic](https://github.com/leolin9248/activemimic-data)
- Real-World Reinforcement Learning of Active Perception Behaviors는 NeurIPS 2025 발표지만 proceedings 페이지의 citation publication date는 2026-04-23이다. 행사 연도와 온라인 게시일 필드를 혼용하면 연도가 달라진다. 동일 논문으로 판정했다. [공식 게재 페이지](https://papers.nips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html)
- Self-supervised perception for tactile skin covered dexterous hands의 PMLR 초록은 PercepSkin, 연결된 원고는 Sparsh-skin이라는 이름을 쓴다. 표제와 저자가 일치한다. 별도 논문으로 세지 않았다. [PMLR](https://proceedings.mlr.press/v305/sharma25a.html) · [원고 첫 장](https://raw.githubusercontent.com/mlresearch/v305/main/assets/sharma25a/sharma25a.pdf#page=1)
