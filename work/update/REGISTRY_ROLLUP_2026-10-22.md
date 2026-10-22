# 연구 후보 요약과 registry 갱신 — 2026-10-22

사용자 요청으로 과거 연구 후보를 **주제별 한 파일 16개**로 정리하고, 후보 dossier에만 남아 있던 직접 비교·평가 문헌 **47편**을 표준 registry에 등록했다. [주제별 요약 index](../research_candidates/summaries/README.md)에서 실제 결과·GPU 후속 최소 검증·GPU 외 한계·재개 조건·상세 근거를 볼 수 있다.

## 범위와 판정

- 초기 로봇 간 RL 전이·지연 방향, retired RP-2/RP-3, C1–C6, D1–D3, E1–E2, 의미 능력 보존 탐색을 포함했다. 하위 실험 ID인 D1-E1과 연구 후보 E1을 구분했다.
- 요약 작성과 논문 등록은 기존 NO-GO/HOLD/RETIRED를 해제하지 않는다. GPU는 자원 조건이며 신규성·데이터 완전성·task/정책/평가 연결을 대신하지 않는다.
- 이번 turn은 문헌·공개 text metadata·파일 유지보수만 수행했다. Policy 실행, simulation, 학습, dependency 설치, PDF/model/trajectory 다운로드는 없다. 실험 재개 시 현재 컴퓨터 Docker-only 조건을 유지한다.
- 이번 갱신은 기존 후보에 직접 필요한 선별 문헌의 누락 보완이다. 2024–2026 모든 발표 논문이나 기존 990편의 venue를 전수 인터넷 재감사했다는 뜻은 아니다. 간접 LLM 연구·중복 버전·연구 질문에 연결되지 않는 후보는 일괄 등록하지 않았다.

## 발표 상태와 identity 확인

- 새 47편 중 main conference/journal 확인 29편, CVPR workshop 1편, arXiv 17편이다. 2024–2026 논문 39편과 직접 비교에 필요한 이전 foundation 8편이다. Venue quota 없이 현재 질문의 기준으로 선정했다.
- Memory Anchors, CounterAlign, RoboFollow, VoLo는 공식 OpenReview 검색 API의 `CoRL 2026 Poster`와 Conference venueid를 확인했다. [Memory Anchors](https://openreview.net/forum?id=dSbtHPqFj9), [CounterAlign](https://openreview.net/forum?id=AY4totylcx), [RoboFollow](https://openreview.net/forum?id=A9AQjk3dAt), [VoLo](https://openreview.net/forum?id=sF3YZbbTNX).
- GTP-FA는 [NeurIPS 공식 2026 목록](https://neurips.cc/Downloads/2026)의 exact title와 poster 155467 연결 기준이다. 개최 전 program 확인이며 최종 proceedings를 읽었다고 표시하지 않았다.
- HiMoE와 A2C2의 ICLR 2026 `Rejected_Submission`은 채택 증거가 아니므로 arXiv로 유지했다. Foresight Residual RL·SafeLoop의 IROS 저자 표기도 공식 채택으로 승격하지 않았다.
- EARL과 MPG는 공식 [ICLR 2022](https://iclr.cc/Downloads/2022)·[2019](https://iclr.cc/Downloads/2019) 목록을 대조했다. 일부 OpenReview live 요청의 challenge·HTTP 200 응답을 성공적인 metadata 확인으로 세지 않았다.
- ExecVLA/KineVLA는 같은 arXiv identity의 title revision으로 한 편만 등록했다. MIR의 proceedings title `Maximal`과 다른 문서의 `Maximally`는 alias로 처리했다. Real-world continual v3·PaceVLA v2도 별도 논문으로 나누지 않았다.
- Exact/normalized title, alias와 공개 identifier 충돌을 검사했다. 등록 dry-run: 신규 47, 기존/identifier collision 0. [입력](../sources/candidate_rollup_admissions_2026-10-22.json), [출처와 응답 경계](../sources/candidate_rollup_sources_2026-10-22.json).

## 등록된 문헌

각 row의 tier는 이번 등록 결과다. 현재 우선순위의 canonical source는 [READING_PLAN](../../research/READING_PLAN.md)과 generator이며 별도 queue를 만들지 않는다. 새 5개 note는 모두 **ABSTRACT_CHECKED**다. Dossier에서 본문/코드를 더 깊게 검토한 경우 그 범위는 해당 dossier에 보존하며 자동 정독 승격하지 않는다.

| ID | 논문·표준 note | 연도 / status | Tier | 이번 등록의 직접 이유 |
|---|---|---|---|---|
| pr-0991 | [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) | 2026 / ICML | NEXT | E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다. |
| pr-0992 | [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](../../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) | 2026 / ICLR | NEXT | 의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다. |
| pr-0993 | [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](../../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) | 2026 / RSS | NEXT | Cross-embodiment VLA interface를 비교할 최신 직접 선행이다. |
| pr-0994 | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](../../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) | 2026 / CVPR | NEXT | E2의 adaptive horizon 주장에 대한 직접 baseline이다. |
| pr-0995 | [Memory Anchors for Continual Robot Learning](../../2026/CoRL/2026_CoRL_Memory-Anchors-for-Continual-Robot-Learning/01_overview.md) | 2026 / CoRL | NEXT | E1의 action-conflict replay와 가장 가까운 직접 비교군이다. |
| pr-0996 | [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](../../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) | 2026 / arXiv | NEXT | E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다. |
| pr-0997 | [Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?](../../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) | 2026 / arXiv | NEXT | E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다. |
| pr-0998 | [HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies](../../2025/arXiv/2025_arXiv_HiMoE-VLA-Hierarchical-Mixture-of-Experts-for-Generalist-V/01_overview.md) | 2025 / arXiv | REFERENCE | E1에서 물리 action 충돌을 단순 expert 분리와 구별할 직접 REFERENCE다. |
| pr-0999 | [Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization](../../2026/arXiv/2026_arXiv_Vela-Scaling-Vision-Language-Action-Models-with-Adaptive-A/01_overview.md) | 2026 / arXiv | REFERENCE | E2에서 연속 행동 곡선 자체를 신규 기여로 재주장하지 않기 위한 REFERENCE다. |
| pr-1000 | [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) | 2026 / arXiv | NEXT | E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다. |
| pr-1001 | [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](../../2026/arXiv/2026_arXiv_PaceVLA-Adaptive-Temporal-Action-Quantization-in-Vision-La/01_overview.md) | 2026 / arXiv | REFERENCE | E2의 adaptive time compression과 직접 겹치는 REFERENCE다. |
| pr-1002 | [Real-Time Execution of Action Chunking Flow Policies](../../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) | 2025 / NeurIPS | NEXT | 초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다. |
| pr-1003 | [SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies](../../2025/CoRL/2025_CoRL_SAIL-Faster-than-Demonstration-Execution-of-Imitation-Lear/01_overview.md) | 2025 / CoRL | NEXT | E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다. |
| pr-1004 | [Learning High-Frequency Continuous Action Chunks in Latent Space](../../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) | 2026 / ICML | NEXT | E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다. |
| pr-1005 | [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](../../2025/arXiv/2025_arXiv_Leave-No-Observation-Behind-Real-time-Correction-for-VLA-A/01_overview.md) | 2025 / arXiv | REFERENCE | E2의 fresh feedback correction·delay/horizon 분리가 이미 존재함을 보여준다. |
| pr-1006 | [Measuring the Stability Assumption Behind Action Chunking](../../2026/arXiv/2026_arXiv_Measuring-the-Stability-Assumption-Behind-Action-Chunking/01_overview.md) | 2026 / arXiv | REFERENCE | E2 진단에서도 state-dependent 안정성을 새 발견으로 주장하지 않도록 하는 REFERENCE다. |
| pr-1007 | [Cooperative Grasping for Collective Object Transport in Constrained Environments](../../2026/RA-L/2026_RA-L_Cooperative-Grasping-for-Collective-Object-Transport-in-Co/01_overview.md) | 2026 / RA-L | REFERENCE | D2의 운반 결과를 고려한 파지 주장이 이미 다뤄졌음을 보여준다. |
| pr-1008 | [Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments](../../2025/RA-L/2025_RA-L_Globally-Guided-Geometric-Fabrics-for-Reactive-Mobile-Mani/01_overview.md) | 2025 / RA-L | REFERENCE | D2에서 grasp/place 변경과 전체 경로 reasoning의 기하학 baseline이다. |
| pr-1009 | [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](../../2026/arXiv/2026_arXiv_WBAG-A-Whole-Body-and-Attached-Geometry-Safety-Framework-f/01_overview.md) | 2026 / arXiv | REFERENCE | D2의 파지 후 geometry 고려라는 넓은 기여와 직접 충돌한다. |
| pr-1010 | [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](../../2026/arXiv/2026_arXiv_CarryOn-A-Dual-Loop-Harness-for-Personalized-and-Reliable/01_overview.md) | 2026 / arXiv | REFERENCE | D2/D3에서 persistent planning·shield 결합의 신규성 경계를 정한다. |
| pr-1011 | [Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation](../../2026/NeurIPS/2026_NeurIPS_Grasp-Then-Plan-with-Failure-Attribution-A-Closed-Two-Stag/01_overview.md) | 2026 / NeurIPS | REFERENCE | D2에서 downstream outcome·failure attribution을 새 방법으로 주장하지 않게 한다. |
| pr-1012 | [Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models](../../2026/arXiv/2026_arXiv_Foresight-Residual-RL-for-Long-Horizon-Robot-Manipulation/01_overview.md) | 2026 / arXiv | REFERENCE | D2에서 후속 실행 가능성을 reward에 넣는 좁은 RL 주장도 제한한다. |
| pr-1013 | [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](../../2026/arXiv/2026_arXiv_SafeLoop-Risk-Aware-Rollback-for-Vision-Language-Action-Ma/01_overview.md) | 2026 / arXiv | REFERENCE | D3에서 rollback이 세계 상태를 되돌린다는 잘못된 가정을 피할 직접 비교군이다. |
| pr-1014 | [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](../../2026/CoRL/2026_CoRL_VoLo-A-Physical-Orchestrator-for-Open-Vocabulary-Long-Hori/01_overview.md) | 2026 / CoRL | REFERENCE | D3에서 단순 switching 방법과 추가 도구 정보의 효과를 구분할 기준이다. |
| pr-1015 | [Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments](../../2025/NeurIPS/2025_NeurIPS_Robust-and-Scalable-Autonomous-Reinforcement-Learning-in-I/01_overview.md) | 2025 / NeurIPS | REFERENCE | C5/D3의 비가역성·reset 질문에 필요한 RL 선행이다. |
| pr-1016 | [RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following](../../2026/CVPR-Workshop/2026_CVPR-Workshop_RePlan-Bot-Multi-Level-Replanning-for-Embodied-Instruction/01_overview.md) | 2026 / CVPR-Workshop | REFERENCE | D3의 multi-level replanning이 이미 존재하는 workshop 비교군이다. |
| pr-1017 | [Online Continual Learning with Maximal Interfered Retrieval](../../2019/NeurIPS/2019_NeurIPS_Online-Continual-Learning-with-Maximal-Interfered-Retrieva/01_overview.md) | 2019 / NeurIPS | REFERENCE | E1에서 loss/gradient interference를 신규 원리로 재주장하지 않게 하는 foundation이다. |
| pr-1018 | [Learning Human Objectives by Evaluating Hypothetical Behavior](../../2020/ICML/2020_ICML_Learning-Human-Objectives-by-Evaluating-Hypothetical-Behav/01_overview.md) | 2020 / ICML | REFERENCE | C4에서 query 선택·reward refinement의 오래된 직접 선행이다. |
| pr-1019 | [Information Directed Reward Learning for Reinforcement Learning](../../2021/NeurIPS/2021_NeurIPS_Information-Directed-Reward-Learning-for-Reinforcement-Lea/01_overview.md) | 2021 / NeurIPS | REFERENCE | C4의 decision-relevant reward audit 주장의 직접 foundation이다. |
| pr-1020 | [PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement](../../2025/ICCV/2025_ICCV_PROGRESSOR-A-Perceptually-Guided-Reward-Estimator-with-Sel/01_overview.md) | 2025 / ICCV | REFERENCE | C4에서 progress reward 품질과 정책 효과를 분리할 비교군이다. |
| pr-1021 | [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](../../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) | 2026 / RSS | NEXT | C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다. |
| pr-1022 | [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](../../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) | 2026 / arXiv | NEXT | C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다. |
| pr-1023 | [Autonomous Reinforcement Learning: Formalism and Benchmarking](../../2022/ICLR/2022_ICLR_Autonomous-Reinforcement-Learning-Formalism-and-Benchmarki/01_overview.md) | 2022 / ICLR | REFERENCE | C5의 continuing/deployed 평가와 human intervention 기준을 제공한다. |
| pr-1024 | [A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning](../../2022/ICML/2022_ICML_A-State-Distribution-Matching-Approach-to-Non-Episodic-Rei/01_overview.md) | 2022 / ICML | REFERENCE | C5의 reset-induced state distribution 자체가 신규 문제가 아님을 보여준다. |
| pr-1025 | [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) | 2025 / CoRL | NEXT | C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다. |
| pr-1026 | [Active Offline Policy Selection](../../2021/NeurIPS/2021_NeurIPS_Active-Offline-Policy-Selection/01_overview.md) | 2021 / NeurIPS | REFERENCE | C6에서 OPE+능동 online 평가라는 넓은 방법의 직접 선행이다. |
| pr-1027 | [Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping](../../2025/RSS/2025_RSS_Is-Your-Imitation-Learning-Policy-Better-than-Mine-Policy/01_overview.md) | 2025 / RSS | NEXT | C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다. |
| pr-1028 | [Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison](../../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) | 2026 / RSS | NEXT | C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다. |
| pr-1029 | [Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection](../../2025/CoRL/2025_CoRL_Efficient-Evaluation-of-Multi-Task-Robot-Policies-With-Act/01_overview.md) | 2025 / CoRL | REFERENCE | C6의 task-aware cost-aware 평가 배분에 대한 직접 REFERENCE다. |
| pr-1030 | [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](../../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) | 2026 / arXiv | REFERENCE | C1/D1의 능동 관측·관측 정렬 주장과 직접 충돌한다. |
| pr-1031 | [EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras](../../2026/arXiv/2026_arXiv_EyeRobot-2.0-Active-Gaze-for-Precise-Manipulation-without/01_overview.md) | 2026 / arXiv | REFERENCE | C1의 시선 조절과 action-relevant 관측에 대한 직접 REFERENCE다. |
| pr-1032 | [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](../../2026/arXiv/2026_arXiv_RESCUE-Is-This-Alarm-Worth-Acting-On-Counterfactual-Evalua/01_overview.md) | 2026 / arXiv | REFERENCE | C1/RP-2의 관측/개입 가치 진단에 대한 직접 evaluation 기준이다. |
| pr-1033 | [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](../../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) | 2026 / CoRL | NEXT | C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다. |
| pr-1034 | [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](../../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) | 2026 / CoRL | NEXT | C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다. |
| pr-1035 | [ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation](../../2026/arXiv/2026_arXiv_ExecVLA-Following-Fine-Grained-Execution-Constraints-in-Vi/01_overview.md) | 2026 / arXiv | REFERENCE | C2의 수행 방식 지시 주장이 겹치는 직접 선행이며 KineVLA와 동일 identity다. |
| pr-1036 | [Clipped Action Policy Gradient](../../2018/ICML/2018_ICML_Clipped-Action-Policy-Gradient/01_overview.md) | 2018 / ICML | REFERENCE | C3에서 실행 동치 action의 확률 질량을 합치는 원리의 foundation이다. |
| pr-1037 | [Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications](../../2019/ICLR/2019_ICLR_Marginal-Policy-Gradients-A-Unified-Family-of-Estimators-f/01_overview.md) | 2019 / ICLR | REFERENCE | C3의 action equivalence 주장을 제한하는 가장 직접적인 이론 계보다. |

## Registry와 문서 동기화

- 전체 990 → **1,037편**, CORE **47**, NEXT **257 → 275**, REFERENCE **444 → 473**, ARCHIVE **242**. 기존 membership은 바꾸지 않았다.
- 표준 note **4,950 → 5,185개**. 신규 47개 folder에 각각 5개 note를 만들었다. 새 NEXT 18개는 `UNREAD + ABSTRACT_CHECKED`; active 322개·history 47개다.
- `PAPER.md`, manifest/meta, tier/plan/tracker, synthesis queue, catalog/resource/index/stats, root/work README·AGENTS·TODO·reading-status 문서를 동기화했다.
- 등록 renderer에서 미식별 project를 깨진 Markdown link로 만들지 않도록 수정했다. Priority sync는 이번 incremental review 날짜를 과거 cohort에 덮어쓰지 않고, 같은 이유의 기존 검토 날짜·basis를 보존하도록 보완했다.
- 기존 note 내용·manifest·사용자 입력 보존, 링크·수량·schema·중복·생성기 일관성의 실제 검증은 [VALIDATION](./REGISTRY_ROLLUP_VALIDATION_2026-10-22.md)에 기록한다.

## 다음 행동

추가 실험을 자동 시작하지 않는다. E2-R1/E1-R2는 일관된 native 비교 자료와 기존 대안 이후 차별적 예측이 생겼을 때 재심사한다. 다른 후보 역시 각 요약의 재개 조건을 먼저 따른다. 새로운 연구 주제 선택·실험 실행은 이 유지보수 작업의 결과와 구분한다.
