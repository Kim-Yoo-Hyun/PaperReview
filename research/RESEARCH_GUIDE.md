# 연구 설계

로보틱스 석사 주제를 고를 때는 **답을 알면 달라질 로봇 행동이나 연구자의 결정**부터 쓴다. 조작·이동·제어에서 중요한 실패를 출발점으로 삼고 VLA, RL, 3D 인식은 질문에 따라 선택한다. 아래 절차는 연구자의 공개 회고와 심사 지침을 이 저장소에 적용한 것이다. 후보별 현재 판단과 실행 순서는 따로 관리한다. [연구 후보](../work/research_topics/README.md) · [다음 작업](../TODO.md)

<a id="nonexperimental-workflow"></a>
<a id="5-문헌에서-아이디어로-넘어가는-8단계"></a>

## 문헌에서 연구 질문으로

공백을 조사한 뒤 여덟 단계를 따른다. 선행이 같은 질문에 답했거나 강한 단순 대안이 드러나면 앞 단계로 돌아간다. 기존 후보의 **비실험 검토 일곱 항목**은 문제와 독자, 가까운 선행, 질문과 대안, 짧은 논문 이야기, 최소 비교 설계, 실행 부담, 외부 비판이다. 아래 표를 해당 후보의 `내용/README.md`에 적용한다.

| 단계 | 할 일 | 판단을 남길 근거 |
|---|---|---|
| 0. 공백 탐색 | 관심 행동·비용·검색 종료일을 기록한다. registry와 외부 학회·저널, 최근 프리프린트를 동의어로 검색한다. | 가장 가까운 논문에서 이미 답한 조건, 아직 확인할 수 없는 조건, 후속 연구의 반례 |
| 1. 문제 선택 | 누가 어떤 상황에서 무엇을 결정하는지 한 문장으로 쓴다. | 답에 따라 바뀌는 센서·제어·학습·평가 결정 |
| 2. 핵심 문헌 | 넓게 선별한 뒤 직접 경쟁 연구의 원문·부록과 공개 구현을 읽는다. 실제 평가한 태스크와 정책 입력을 확인한다. | 원문 절·그림·표와 코드 위치. 워크숍·프리프린트·게재본의 판본 |
| 3. 조건 비교 | 각 논문을 관측, 상태, 행동 단위, 제어 주기, 피드백, 자료 분할, 자원 예산, 결과 지표로 정리한다. | 결과가 엇갈린 두 논문의 조건을 맞추면 차이가 남는지 |
| 4. 가설과 대안 | 현상을 설명하는 원인과 더 단순한 설명을 각각 적는다. 둘이 다른 행동을 예측하는 조건을 찾는다. | 조작할 변수, 직접 관측할 결과, 가설을 약화시킬 반례 |
| 5. 선행과 차이 | 가장 가까운 방법·평가·데이터와 바뀌는 부분을 비교한다. 후속 인용과 최근 유사 논문도 확인한다. | 선행의 실제 기준선, 남는 차이, 논문 기여의 유형 |
| 6. 주장과 증거 | 문제·공백·예상 기여를 한 문단으로 쓰고, 주장별 기준선·관측 단위·비용·기각 기준을 정한다. | 결과 칸은 미측정으로 두고 필요한 산출물과 구현 부담을 적는다. |
| 7. 최소 검사 | 핵심 가정을 가장 싸게 판별할 공개 기록·반례·정적 인터페이스부터 검사한다. 실험은 실행 환경과 독립 결과를 확보한 뒤 진행한다. | 가능한 판정, 실패 시 범위 축소, 추정 시간과 실제 비용 |
| 8. 독립 비판과 결정 | 연구실 동료에게 한 페이지를 보여 주고 가장 약한 주장과 강한 대안을 묻는다. | 수신한 반론, 수정한 비교, 진행·수정·보류의 이유와 재개 조건 |

문제 선택은 Karpathy의 회고, 선택적 정독은 Keshav의 세 번 읽기, 작은 반례로 원인을 분리하는 방법은 Torralba·Isola·Freeman의 교재에서 가져왔다. Peyton Jones는 글을 먼저 써서 주장의 빈칸을 드러내는 방법을, Steinhardt는 연구자의 실제 선택을 복기하는 연습을 제안한다. 아래 원자료에는 확인한 위치와 용도를 기록했다. [원자료](#원자료)

<a id="stage-appropriate-gates"></a>

## 단계별 증거와 투자 판단

| 시점 | 필요한 근거 | 다음 결정 |
|---|---|---|
| 탐색 | 중요한 로봇 상황, 답을 알 때의 가치, 가까운 선행과 아직 모르는 조건 | 유망하면 작은 진단으로 진행한다. 실패 빈도나 긍정 효과를 이때 요구할 필요는 없다. |
| 진단 | 기초 수행 능력, 같은 초기 상태·관측·실행 예산, 독립 결과의 식별 가능성, 단순 대안 | 대안이 같은 결과를 내면 질문을 원인 분석이나 평가 문제로 좁힌다. 입력·측정이 일치하지 않으면 비교를 다시 설계한다. |
| 확증·본격 구현 | 주 주장, 독립 표본, 분모, 기준선, 시행·시드·일반화 범위, 실패/중단 기준, 구현·장비·데이터 비용 | 관측 범위 안에서 기여를 판단한다. 성능·효율, 분석, 데이터·벤치마크, 시스템 기여는 각각 뒷받침할 증거가 다르다. |

문헌·논리 검토, 외부 피드백, 실행 준비, 실측 결과는 각각 기록한다. 독립 연구자의 피드백을 아직 받지 못했으면 그 사실을 적는다. 같은 자료로 결론이 바뀌지 않는다면 보류를 풀 수 있는 새 관측을 명시하고 종료한다. 공개 코드·가중치의 실제 조합과 로컬 Docker에서 확인할 최초 검사는 후보의 `재현 방법/README.md`에 둔다. [실험 재현](../work/experiments/README.md) · [보류 결과와 재개 조건](../work/research_topics/RESULTS.md)

## 적용 예시

다음은 비교 설계를 설명하는 가상 사례다.

| 질문 | 경쟁 설명을 가르는 최소 비교 |
|---|---|
| 조작 중 물체가 움직인 뒤 언제 action chunk를 갱신해야 하는가? | 같은 체크포인트·평균 호출 예산에서 주기적 갱신과 변화 직후 갱신을 비교한다. 관측 품질을 고정하고, 정확한 상태를 주어도 복구 행동이 가능한지 따로 본다. critic과 actor의 시간 구간을 분리한 연구를 먼저 확인한다. [Q-chunking](../2025/NeurIPS/2025_NeurIPS_Reinforcement-Learning-with-Action-Chunking/01_overview.md) · [Decoupled Q-Chunking](../2026/ICLR/2026_ICLR_Decoupled-Q-Chunking/01_overview.md) |
| 동적 장애물 앞에서 재계획이 충돌을 줄이는가? | 같은 시작 상태·이동거리·정지 비용에서 고정 재계획 및 대기와 비교한다. 진행률을 함께 보면 단순 감속의 효과를 분리할 수 있다. [주행 비교 결과](../work/experiments/reactive_nav_pilot/RESULTS.md) |
| 3D 추정이 나아지면 로봇도 더 잘 집는가? | 같은 장면·제어기에서 추정치만 교체하고 자세 오차와 과제 성공을 별도로 측정한다. 가림 해소용 새 시점을 사용하면 이동·관측 비용을 포함한다. [조작용 3D 추정](../work/research_topics/task_geometry_estimation/내용/README.md) |

## 후보 기록 양식

| 기입란 | 한 페이지에 남길 내용 |
|---|---|
| 문제·독자 | 로봇, 현상, 실패 비용, 답이 바꿀 결정 |
| 공백·가장 가까운 선행 | ID·원문 위치·코드, 확인된 답, 남은 조건, 가장 강한 반례 |
| 기여 후보 | 질문 한 줄, 예상 원인, 경쟁 설명, 서로 다른 행동 예측 |
| 최소 비교 | 개입, 관측, 공정한 기준선, 분할·독립 단위·지표·예산, 실행 가능 조건 |
| 판정 | 실제로 확인한 것, 미확인, 반론, 진행·수정·보류 기준과 다음 행동 |

<a id="search-map-2026-11-17"></a>

## 분야별 검색 지도

현상·가정·경쟁 설명을 동의어로 검색한다. 서베이·큐레이션·arXiv·연구실 발표로 후보를 찾고, 가장 가까운 3–5편의 본문·참고문헌·후속 인용을 따라간다. 최근 흐름은 현재 연도를 포함한 3개 연도로, 기반 연구는 연도 제한 없이 본다. 공개·게재 여부와 실험 조건은 원 출처에서 확인한다. [조사 원칙](../AGENTS.md) · [로보틱스 동향](../work/update/ROBOTICS_TRENDS.md)

| 분야 | 함께 돌려 검색할 표현 |
|---|---|
| VLA × RL 알고리즘 | RL fine-tuning, reinforced fine-tuning/RFT, post-training, off-policy/on-policy, offline-to-online, residual/action editing, advantage-conditioned, critic, Q-chunking, PPO/GRPO for diffusion/flow matching, noise-space steering, consistency policy, LoRA, test-time adaptation, self-improving |
| 보상·성공·진행도 | reward model, VLM-as-reward/judge, success detector/classifier, progress estimator, process reward, dense reward from video, reward hacking/calibration, failure analysis, goal-conditioned value, temporal distance |
| 실제 로봇 RL | real-world/sample-efficient RL, human intervention, DAgger, reset-free/autonomous reset, forward-backward policy, continual/lifelong/deployment-time learning |
| World model·상상 학습 | embodied world model, action-conditioned video, WAM, latent dynamics, imagination/model-based RL, Dreamer/MBPO, policy verification, real2sim/sim2real, digital twin, hallucination control, model-policy co-evolution |
| 3D·4D·동적 장면 | spatial/geometry-aware VLA, point-cloud policy, spatiotemporal/4D, scene flow, CoTracker/TAP, optical flow, dynamic manipulation, interception/catching/conveyor, 3D/4D Gaussian, VGGT/depth, multi-view consistency, viewpoint robustness |
| 물체 상태·추적 | 6D pose estimation/tracking, FoundationPose, novel-object/category-level/model-free pose, symmetry/occlusion/multi-hypothesis/SE(3) distribution, re-initialization/re-detection, object-centric policy/permanence, SAM2, grounding/keypoint/affordance, active perception/next-best-view |
| **신뢰성·불확실성·실패 — 우선** | failure detection/prediction, runtime monitoring/verification, anomaly/OOD detection, covariate/policy/monitor drift, conformal prediction, ECE/calibration, selective prediction/abstention, epistemic/aleatoric UQ, hidden-state/latent probe, ensemble, failure attribution/root cause/taxonomy, perception vs policy failure, recovery/rollback/retry, confidence gate/fallback, graceful degradation |
| 기억·장기 작업 | memory-augmented/retrieval-augmented policy, episodic/working/spatial/object/failure memory, non-Markovian/POMDP, history compression/keyframe/recurrent/Mamba, negative experience, retrieve-then-steer, progress tracking |
| 안전 | safe/constrained RL/CMDP, safety filter/CBF, chunk-level safety, shielding/reachability/runtime assurance, semantic safety, fragile-object/HRI/whole-body safety, adversarial attack/backdoor |
| 일반화·평가 | LIBERO/Plus/PRO/Safety, VLABench, RoboTwin, SimplerEnv, ManiSkill, RoboMME, MIKASA-Robo, DOMINO, CALVIN, camera/light/layout/instruction shift, cross-embodiment, sim-real correlation, reproducibility/evaluation harness |
| 효율·배포 | small/efficient VLA, SmolVLA, quantization/distillation/token caching/early exit, action/real-time chunking, asynchronous/latency-aware control, on-device, inference-time compute/speculative decoding/dual system |
| 데이터 | augmentation/domain randomization, synthetic/video-to-action/latent action, egocentric video, UMI/teleoperation quality, curation/filtering, failure/counterfactual/recovery data, perturbation injection |
| 기반 모델의 역할 | hierarchical VLA, VLM planner, embodied reasoning/chain-of-thought, code-as-policy/skill library, agentic policy, closed-loop monitoring, 단일 정책·공유 학습과 배포 시 모듈 연결 구분 |
| 비전 + 촉각·힘 | visuo-tactile, force-aware VLA, contact-rich manipulation/insertion, proprioception fusion, adaptive/variable impedance |

### 검색식 예시

```text
("VLA" OR "vision-language-action") ("failure detection" OR "runtime monitoring")
"robot manipulation" "perception failure" "policy failure"
"VLA" "failure attribution" recovery
"VLA" "policy update" (calibration OR "monitor drift")
"object pose uncertainty" (manipulation OR "fallback policy")
"pose tracking" "failure recovery" manipulation
"VLA" "residual RL" perception
"VLM reward" "failure detector" "real-world RL"
"negative memory" "failure retrieval" "robot policy"
"conformal prediction" "VLA" recalibration
"perception uncertainty" ("safety filter" OR "control barrier function")
"dynamic manipulation" "motion uncertainty" policy
("diffusion policy" OR "flow matching") "reinforcement learning" contact
"vision-language-action" "language grounding" "reinforcement learning"
```

## 원자료

2026년 10월 19일 조사했고, 10월 23일 MIT 교재·DARPA·ICLR·NeurIPS E&D를 재대조하고 ECCV와 NeurIPS 체크리스트를 추가했다. 학회 기준은 표시된 연도와 트랙에 해당한다.

| 자료 | 저자·기관 / 확인 범위 | 이 문서에서 사용한 부분 |
|---|---|---|
| [A Survival Guide to a PhD](https://karpathy.github.io/2016/09/07/phd/) | Andrej Karpathy, 2016, 본인 블로그의 Research topics 및 회고 | 문제 선택과 실제 관심 분야 전환 사례 |
| [How to Read a Paper](https://cs.uwaterloo.ca/~brecht/courses/854-http-video-2012/readings/keshav-paper-reading.pdf) | S. Keshav, ACM SIGCOMM CCR 37(3), 2007, Waterloo의 2쪽 공개 원문 | 단계별 읽기와 가정·논리 재구성 |
| [How to Do Research](https://visionbook.mit.edu/how_to_do_research.html) | Antonio Torralba·Phillip Isola·William T. Freeman, 공개 교재 52장 | 가정 검사, toy model, 연구 디버깅 |
| [How to Write a Great Research Paper](https://simon.peytonjones.org/great-research-paper/) | Simon Peyton Jones, 저자 페이지와 연결된 공개 슬라이드 | 초기 쓰기, 중심 주장, 주장에 대응하는 증거 |
| [Film Study for Research](https://jsteinhardt.stat.berkeley.edu/blog/film-study) | Jacob Steinhardt, 2021, 본인 글 | 사고 과정 학습과 판단 복기 |
| [The Heilmeier Catechism](https://www.darpa.mil/about/heilmeier-catechism) | DARPA 공식 페이지 | 중요성·기존 접근·위험·비용·검증을 연결하는 질문 |
| [ICLR 2026 Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide) | ICLR 공식 지침, Review Content | 지식·가치·문헌적 동기·주장 검증 |
| [NeurIPS 2026 E&D Reviewing Guidelines](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines) | NeurIPS 공식 E&D track 지침 | 기여 유형별 평가와 체계적인 부정 결과 |
| [RSS 2026 Call for Papers](https://roboticsconference.org/2026/information/cfp/) | RSS 공식 연도별 페이지 | scientific / systems contribution 범위 |
| [T-RO Information for Authors](https://www.ieee-ras.org/publications/t-ro/t-ro-information-for-authors/) | IEEE RAS 공식 저널 안내 | 중요성과 기존 연구 확장 시 요구되는 실질적 기여 |
| [ECCV 2026 Contribution Types](https://eccv.ecva.net/Conferences/2026/ReviewerContributionTypes) | 2026-10-23 추가, 공식 reviewer 지침 | 알고리즘·이론·시스템·dataset 등 기여에 맞는 판단, 획일적 checklist 회피 |
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) | 2026-10-23 추가, 공식 checklist | 주장 범위·한계·통계적 변동·계산 자원과 재현 정보 |
