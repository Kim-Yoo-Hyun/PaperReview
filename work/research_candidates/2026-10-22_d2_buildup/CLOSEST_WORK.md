# D2 직접 문헌·공개 자산 대조

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 확인: 2026-10-22 KST. [판정](./README.md), [claim 계약](./CLAIM_CONTRACT.md), [source identity](./sources_2026-10-22.json).
- `본문 확인`은 아래 지정 절을 읽었다는 뜻이며 전편 정독·독립 재현을 뜻하지 않는다. 저자 보고와 연구자 해석을 분리한다.
- 기존 registry 4편과 외부 비교 문헌 6편이다. 외부 6편은 이 검토의 evidence record이며 paper registry에 신규 등록한 상태는 아니다. 사용자 reading status는 유지한다.

## 1. 식별자와 출판 근거

| ID | 정확한 title / year·status | 공식/원문 근거 | Project/code와 확인 경계 |
|---|---|---|---|
| S01 / pr-0748 | **PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning** / ICAPS 2020, 기존 registry | [등록 노트](../../../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | [공식 repo](https://github.com/caelan/pddlstream). 이번에는 README의 framework 역할만 확인; 특정 D2 task 구현을 확인한 것은 아님 |
| S02 / pr-0054 | **ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation** / CoRL 2024, proceedings 발행 2025 | [PMLR 270](https://proceedings.mlr.press/v270/huang25g.html), [arXiv v2](https://arxiv.org/html/2409.01652v2) | [Project](https://rekep-robot.github.io/), [repo](https://github.com/huangwl18/ReKep). Source 6개 확인 |
| S03 / pr-0975 | **MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation** / CVPR 2025 | [CVF 출판본](https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.pdf), [arXiv v1](https://arxiv.org/html/2503.13446v1) | [Project](https://gary3410.github.io/momanipVLA/)의 Code Coming Soon 표기. 실행 code 미확보 |
| S04 / pr-0060 | **MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation** / CoRL 2025 | [PMLR 305](https://proceedings.mlr.press/v305/wu25c.html), [arXiv v1](https://arxiv.org/html/2509.01658v1) | [Project](https://gary3410.github.io/MoTo/). 검토한 공식 page에서 code를 식별하지 못함; 미공개 확정과 구분 |
| S05 / 외부 | **Cooperative Grasping for Collective Object Transport in Constrained Environments** / RA-L 2026, 11(3):2967–2974 | [DOI](https://doi.org/10.1109/LRA.2026.3653338), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1109/LRA.2026.3653338), [저자 accepted manuscript](https://repository.kaust.edu.sa/bitstreams/fadd5961-e26e-40d8-8cc5-448446a87d3b/download), [읽은 preprint v1](https://arxiv.org/html/2509.03638v1) | [저자 publication page](https://sites.google.com/site/shinkyupark1/publications)에서 연결한 [repo](https://github.com/davidfalgo/cooperative_grasping). IEEE 본문 UI는 bot challenge. 출판 metadata와 읽은 2025 preprint 버전을 구분 |
| S06 / 외부 | **Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments** / RA-L 2025, 10(6):5553–5560 | [출판본](https://research.tudelft.nl/files/243256288/Globally-Guided_Geometric_Fabrics_for_Reactive_Mobile_Manipulation_in_Dynamic_Environments.pdf), DOI `10.1109/LRA.2025.3562005` | [저자 project](https://autonomousrobots.nl/paper_websites/g3f). Abstract/introduction 확인; code 내부는 미감사 |
| S07 / 외부 | **WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation** / arXiv 2026, 공식 venue 미확인 | [2610.01083v1](https://arxiv.org/html/2610.01083v1) | 검토 원문·exact-title 검색에서 저자 code를 식별하지 못함 |
| S08 / 외부 | **CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance** / arXiv 2026, 공식 venue 미확인 | [2610.21453v1](https://arxiv.org/html/2610.21453v1) | [공식 repo](https://github.com/JIA-Lab-research/CarryOn): 확인 revision은 README 1개만 존재. 예정 공지는 release 증거가 아님 |
| S09 / 외부 | **Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation** / NeurIPS 2026 공식 program의 Poster 항목 확인; 개최 전 | [공식 2026 목록](https://neurips.cc/Downloads/2026)의 poster `155467`, [읽은 2606.03385v1](https://arxiv.org/html/2606.03385v1) | [저자 project](https://sites.google.com/view/gtp-fa/)는 접근했으나 실질 code 링크를 추출하지 못함. 개별 NeurIPS poster URL 접근 실패; 목록의 exact title/class를 근거로 기록. 최종 proceedings 원문은 미대조 |
| S10 / 외부 | **Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models** / arXiv 2026; **IROS 2026 accepted는 저자 표기**, 공식 program 미확인 | [2607.16506v1](https://arxiv.org/html/2607.16506v1), [arXiv comments](https://arxiv.org/abs/2607.16506), [저자 목록](https://litaoliu01.github.io/) | 원문이 연결한 [project](https://jaysparrow.github.io/foresight-residual-rl)는 이번 접근에서 HTTP 404. Code not identified이며 code 미공개를 확정하지 않음 |

S05/S06의 publisher 형식 원문은 웹에서 확인했으며 local PDF cache를 만들지 않았다. S09와 S10의 status 근거 강도는 다르다. 제3자 curated list의 venue 표기는 최종 근거로 사용하지 않았다.

## 2. 직접 비교 — 논문이 지지하는 범위

| ID·읽은 위치 | 입력·결정·학습 | 평가/가정 및 경계 | D2에 대한 연구자 해석 |
|---|---|---|---|
| S01 / README | Symbolic planning과 blackbox sampling 결합 | 특정 D2 executor와 runtime은 미선정 | 알려진 geometry에서 grasp·route·place 탐색을 새 개념으로 주장하지 않기 위한 foundation |
| S02 / method, App. A.8–A.9, task 설명 | RGB-D/keypoint constraints, subgoal/path 최적화; gripper와 grasped-object point cloud의 ESDF 비용 | 좁은 shelf/용기 배치 포함. 물체 강체 가정, 표본 collision 비용; 연속 경로 전체의 안전 보장은 아님 | Attached object를 고려하지 않는 baseline으로 묘사하면 잘못된 비교 |
| S03 / §3.3–3.4, §4 | VLA trajectory와 base/arm waypoint 최적화; robot-surface ESDF 비용 | Simulation의 ESDF에 3D object models 사용. OVMM·실물 평가 | VLA를 mobile system으로 연결하는 자체가 contribution은 아님; 같은 정보로 강한 baseline을 구성해야 함 |
| S04 / §3, §4.1·4.3 | RGB-D·scene graph·VLM interaction keypoints; docking 최적화. Eq.8은 robot surface 비용 | Navigate 후 fixed-base manipulation 분해 가정. Tool의 접촉 keypoint도 고려함 | ‘물체를 전혀 고려하지 않는다’고 단정하지 않음. 확인한 objective에서 grasped-object의 전체 swept volume은 명시되지 않았음 |
| S05 / §II–IV, App. B | Map·polygon footprint·grasp configurations → CE affinity; planner label과 negative sampling의 supervised learning | 두 mobile manipulator, 고정 높이·yaw, 알려진 2D geometry. 새로운 물체/장면과 physical demonstration. Top-k metric은 feasible pair 포함 여부 | ‘이후 운반 가능한 grasp를 학습한다’는 좁힌 주장도 이미 존재. Physical demo와 top-k 수치를 같은 end-to-end 성공률로 읽지 않음 |
| S06 / abstract·introduction | Global optimization과 reactive geometric fabrics의 결합 | Dynamic mobile manipulation; 세부 sensing/label·attached-object 구현은 본문 추가 확인 필요 | Local filter의 한계만으로 RL 필요성을 주장할 수 없다는 대안. 직접 재현 baseline으로 자격 부여하지 않음 |
| S07 / §II-C–V | Frozen π0.5의 6D action을 geometry CBF-QP로 수정; grasp 후 물체 추가, RGB-D 기반 scene/target geometry | SafeLIBERO 1,600 episodes. Task-role identity는 simulator 제공; 안전 평가는 eligible object displacement proxy. 고정 mode 안전 논의가 grasp transition까지 보장하지 않음 | VLA + grasp-conditioned attached geometry 자체의 최신 직접 충돌. 이 논문의 tabletop 결과가 mobile transport를 해결했다는 주장은 하지 않음 |
| S08 / §3.3, Table 3, README | Carried-object 포함 geometric shield가 action chunk의 safe prefix를 실행; reactive loop 병행 | RGB-D·contact role 사용. Table 3의 violation 감소와 task success는 별도 측정. 실행 code는 미공개 상태의 README snapshot | Chunk-level 보호도 직접 선행. 보고된 수치를 WBAG와 직접 비교하지 않음 |
| S09 / §4.1–4.4, §5.1–5.4, App. A.7 | Task/observation/grasp/execution summary → 실패 attribution; repeated-trial 약한 label; grasp prior/risk와 downstream data/학습 갱신 | ManiSkill3 8 tasks 및 Franka 실험, π0.5 LoRA 포함. Code/recipe 실행 미검증 | ‘grasp와 execution 실패를 분리해 최적화’도 충돌. 한 정책의 반복 실패를 물리적 불가능의 독립 증거로 재사용하지 말아야 함 |
| S10 / §IV–VI, limitations | 고정 VLA + residual PPO; downstream rollout으로 terminal-state foresight predictor를 학습하고 역순 phase 최적화 | 알려진 phase 분해, 단일 wrench assembly, simulation-only | ‘다음 단계 성공을 고려한 VLA RL’의 직접 선행. 새 task 적용만으로 신규성이나 RL 필요성이 생기지 않음 |

여기서 문헌의 비교 범위는 읽은 버전에 한정된다. 특정 가정이 제한적이라는 사실은 우리 방법이 그 가정을 제거했다는 증거가 아니다. 원문 수치는 D2 자체 결과가 아니므로 현재 의사결정에 불필요한 SOTA 숫자를 나열하지 않았다.

## 3. 공개 source의 정적 확인

| Repo / 고정 commit | 읽은 파일 | 확인한 연결 | 아직 확인하지 않은 것 |
|---|---|---|---|
| ReKep / `63c43fdba60354980258beaeb8a7d48e088e1e3e` | README, environment.py, main.py, subgoal_solver.py, path_solver.py, configs/config.yaml | `environment.py:221–259`의 gripper/wrist 및 in-hand object **collision meshes** → `main.py`의 solver 전달. Assisted grasp config. README는 real perception pipeline 대신 sim 정보를 사용한다고 명시 | RGB-D-only 재현·mobile task competence. 논문과 config의 sampling/margin 세부값은 다르므로 동일 실행 recipe라고 주장하지 않음 |
| Cooperative Grasping / `4eea7ae76cf8c7be623de241e5b22faed01a2579` | README, data/dataloader.py, models/center_embedding_resnet.py, training/trainer.py | Map/footprint/grasping approach 입력, positive combinations와 negative samples, sigmoid BCE 계열 loss. 공개 CE 코드 존재 | Dataset/checkpoint/planner payload·원문 결과 재현. 전체 repo를 읽거나 실행한 것 아님 |
| CarryOn / `7bc6849d2b89dfea015f1e2726d9758dad3c1311` | README | Recursive tree에 README 1개. Release 예고와 실제 자산을 구분 | Shield 구현·weights·native task 실행 |
| PDDLStream / `2c7d6f514b07ed018e18710192aa0f91c2e70ee2` | README | Framework와 예제 탐색 경로 | D2용 attachment/scene/action adapter·runtime |

파일 bytes/SHA-256은 [JSON](./sources_2026-10-22.json)에 있다. 다운로드한 text는 source identity와 정적 읽기에만 사용했고 repo clone·패키지 설치·연구 코드 실행·model/data/PDF payload 저장은 하지 않았다. Source가 존재하는 것과 논문 실험의 모든 자산이 공개된 것은 다르다.

## 4. 탐색 범위와 남은 한계

검색은 `attached geometry VLA`, `grasp object transport narrow passage`, `task-oriented grasp downstream planning`, `foresight residual RL`, 각 exact title의 venue/code 확인으로 확장했다. D2 최초 formulation의 기하학, 운반 전 파지 선택, VLA 후속 실행, RL credit라는 주요 대안 설명을 대조했다. 새 검색에서 직접 선행이 추가되어 좁힌 주장도 함께 하향했다. 문헌이 완전히 포화되었다거나 관련 연구가 이 10편뿐이라는 뜻은 아니다.

외부 6편의 역할은 다음과 같다: S05/S06은 planning/control의 직접 baseline, S07/S08은 VLA safety 최신 충돌, S09는 manipulation의 grasp/execution interface, S10은 RL/IL의 phase coupling이다. 현 시점에 새로운 tier·읽기 순서를 부여하지 않는다. Registry에 등록할 때는 별도의 dedup/admission과 표준 5개 note 절차를 따른다.
