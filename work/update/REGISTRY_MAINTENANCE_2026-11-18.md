# REG-R17 — 직접 선행 보강과 연구 workspace 게시 준비

- Reviewed: 2026-11-18 KST
- 범위: 최근 후보 탐색의 미등록 직접 선행·비교 baseline 보강, 읽기 우선순위 정합, 누적 후보 정리/재개 자료의 GitHub 반영
- [검증 원장](../sources/registry_maintenance_2026-11-18.json) · [전체 registry](../../PAPER.md) · [현재 TODO](../../TODO.md)

## 등록과 publication 경계

**19개 등록 입력을 대조해 신규18편·기등록1편을 확인했다.** ActiveAlign은 `pr-1030`으로 이미 있어 재등록하지 않았다. 신규18편은 공식 top-tier conference/IJRR12편, 직접 비교가 필요한 Autonomous Robots·Industrial Robot2편, venue 미확인 preprint4편이다. 전체2024–2026 문헌을 다시 전수 조사했다는 뜻은 아니며 최근 탐색에 인용된 missing link 중심의 보강이다.

| 논문 | 확인한 publication | tier·역할 |
|---|---|---|
| [FoundationPose](../../2024/CVPR/2024_CVPR_FoundationPose-Unified-6D-Pose-Estimation-and-Tracking-of/01_overview.md) | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) | NEXT — 현재 능동 관측 후보의 pose baseline이며 CAD/reference·score·좌표 가정을 판단하는 직접 NEXT다. |
| [DISaM](../../2024/CoRL/2024_CoRL_Learning-to-Look-Seeking-Information-for-Decision-Making-v/01_overview.md) | [CoRL 2024](https://proceedings.mlr.press/v270/dass25a.html) | NEXT — 행동 불확실성 기반 관측 전환이 이미 존재함을 확인할 필수 직접 선행이다. |
| [ActiveODPE](../../2026/IJRR/2026_IJRR_Active-6D-pose-estimation-for-textureless-objects-using-mu/01_overview.md) | [IJRR 2026](https://journals.sagepub.com/doi/10.1177/02783649251411922) | NEXT — Pose 정확도 중심 NBV와 task 성공 중심 관측 중단을 비교할 journal 기준이다. |
| [UA-Pose](../../2025/CVPR/2025_CVPR_UA-Pose-Uncertainty-Aware-6D-Object-Pose-Estimation-and-On/01_overview.md) | [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) | REFERENCE — CAD 완전성 전제를 완화하는 geometry 대안으로 보존하되 첫 active-pose 비교의 필수 정독에서는 REFERENCE로 둔다. |
| [RFMPose](../../2025/NeurIPS/2025_NeurIPS_RFMPose-Generative-Category-level-Object-Pose-Estimation-v/01_overview.md) | [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) | NEXT — 유한 pose 가설 생성과 score 해석을 비교하는 직접 NEXT다. |
| [Pose-VLA](../../2026/RSS/2026_RSS_Universal-Pose-Pretraining-for-Generalizable-Vision-Langua/01_overview.md) | [RSS 2026](https://roboticsproceedings.org/rss22/p145.html) | NEXT — Pose 표현을 VLA에 넣는 것만으로 새 기여를 주장하지 않도록 하는 직접 선행이다. |
| [Robo3R](../../2026/RSS/2026_RSS_Robo3R-Enhancing-Robotic-Manipulation-with-Accurate-Feed-F/01_overview.md) | [RSS 2026](https://roboticsproceedings.org/rss22/p056.html) | NEXT — TASK-GEOMETRY가 일반 재구성 정확도 개선의 반복인지 판단할 직접 비교다. |
| [GeoPredict](../../2026/CVPR/2026_CVPR_GeoPredict-Leveraging-Predictive-Kinematics-and-3D-Gaussia/01_overview.md) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) | NEXT — 3D reconstruction auxiliary loss 자체가 새 기여가 아님을 보여 주는 직접 VLA 비교다. |
| [ReconVLA](../../2026/AAAI/2026_AAAI_ReconVLA-Reconstructive-Vision-Language-Action-Model-as-Ef/01_overview.md) | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/38921) | NEXT — TASK-GEOMETRY의 이득이 단순 target attention/영역 supervision 때문인지 비교할 선행이다. |
| [GAP](../../2026/CVPR/2026_CVPR_Action-Geometry-Prediction-with-3D-Geometric-Prior-for-Bim/01_overview.md) | [CVPR 2026](https://openaccess.thecvf.com/CVPR2026?day=2026-06-07) | NEXT — 관계 기반 탐색 후보에서 geometry representation 이득과 exploration 변경의 이득을 구별하는 직접 비교다. |
| [AAWR](../../2025/NeurIPS/2025_NeurIPS_Real-World-Reinforcement-Learning-of-Active-Perception-Beh/01_overview.md) | [NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) | NEXT — VLA+RL로 관측 행동을 만든다는 넓은 주장을 제한하는 핵심 실세계 기준이다. |
| [Colored Noise PPO](../../2024/AAAI/2024_AAAI_Colored-Noise-in-PPO-Improved-Exploration-and-Performance/01_overview.md) | [AAAI 2024](https://ojs.aaai.org/index.php/AAAI/article/view/29139) | NEXT — 복잡한 관계 noise 학습 전에 비교해야 할 단순 시간 상관 탐색 baseline이다. |
| [RL-SCT](../../2024/Autonomous-Robots/2024_Autonomous-Robots_Guiding-real-world-reinforcement-learning-for-in-contact-m/01_overview.md) | [Autonomous Robots 2024](https://link.springer.com/article/10.1007/s10514-024-10164-6) | NEXT — 관계/geometry로 탐색을 제한한다는 원리를 이미 제시한 직접 선행이다. |
| [Robotic task success evaluation under multi-modal non-parametric object pose uncertainty](../../2025/Industrial-Robot/2025_Industrial-Robot_Robotic-task-success-evaluation-under-multi-modal-non-para/01_overview.md) | [Industrial Robot 2025](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF) | NEXT — 불확실성이 남아도 성공하면 행동한다는 원리를 신규성에서 제외하게 하는 직접 비교다. |
| [StructRL](../../2026/arXiv/2026_arXiv_StructRL-Structured-Action-Space-Exploration-for-Flow-Base/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2608.15139) | NEXT — 관계 기반 RL 탐색의 noise 위치·시간 구조·재채점 설계와 직접 충돌하는 최신 선행이다. |
| [SOE](../../2025/arXiv/2025_arXiv_SOE-Sample-Efficient-Robot-Policy-Self-Improvement-via-On/01_overview.md) | [arXiv 2025](https://arxiv.org/abs/2509.19292) | NEXT — 관계 조건 탐색이 일반 latent/on-manifold 탐색보다 필요한지 확인할 직접 baseline이다. |
| [ActivePose](../../2025/arXiv/2025_arXiv_ActivePose-Active-6D-Object-Pose-Estimation-and-Tracking-f/01_overview.md) | [arXiv 2025](https://arxiv.org/abs/2509.11364) | NEXT — Pose estimation+active perception 조합이 이미 구현됐음을 보여 주는 직접 선행이다. |
| [ATAP](../../2026/arXiv/2026_arXiv_Imagine-then-Verify-Affordance-Targeted-Active-Perception/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.23504) | NEXT — Task-aware NBV와 verification 기반 중단이 이미 있는 점을 반영할 직접 비교다. |

- Learning to Look은 **CoRL2024 행사 / PMLR2025 출판**을 구별해 행사 연도로 등록했다.
- SOE의 저자 ICRA2026 표기만으로 venue를 승격하지 않았다. 공식 proceedings identity는 미확인이며 preprint2025로 유지한다. ActivePose는 최초2025·현재 확인한 abstract v2(2026)를 구별한다.
- UA-Pose의 공식 repo에는 README/images만 확인돼 `project_only`다. Code URL이 있다는 사실을 구현 release·실행 재현으로 표시하지 않는다. 다른 code의 root source 목록 확인도 환경 설치·checkpoint 호환 증거가 아니다.
- CVF 일부 HTML403·AAAI bot 차단은 공식 도메인의 검색 색인 abstract/BibTeX와 저자 abstract/project로 보완했다. 원문 전체 확인으로 기록하지 않는다. PDF·weight·asset 다운로드와 dependency 설치는 없다.

신규 각5개 노트는 paper-specific 문제·interface·평가 범위·비교 질문을 포함하며 `ABSTRACT_CHECKED`다. 동일 내용을 실제 정독으로 간주하지 않고 신규 tracker는 UNREAD로 둔다. 이전 후보 검토의 지정 본문 절 확인과 이번 paper-note의 evidence를 혼합하지 않는다.

## 우선순위와 중복 정리

신규17편 NEXT·UA-Pose1편 REFERENCE. 기존 **SaPaVe(pr-0805)·ActiveAlign(pr-1030)**은 현재 pose-active 질문의 공동 camera/manipulation 및 observation-state adaptation 비교에 직접 필요해 REFERENCE→NEXT로 승격했다. CORE는50편 유지한다. Source 확인과 생성기 membership/rationale에서 변경했으며 reading CSV를 직접 바꾸지 않았다.

누적 사용자 요청에 따른 기존 후보7개의 폐기·중복 문서/실행 recipe 정리는 [11/17 원장](../sources/candidate_triage_2026-11-17.json)과 [핵심 증거](../research_topics/retired/README.md)대로 게시한다. 이번 턴에서 다른 연구 자료나 실험 자산을 추가로 삭제하지 않는다. Pose-active·관계 기반 탐색의 준비 코드와 `내용/`·`재현 방법/`를 포함하고, 미실행 상태와 Docker-only 제약을 유지한다. 임시 등록 입력은 작업 외부 temp에 두고 분석은 canonical manifest에 통합해 중복 입력 파일을 추가로 보존하지 않는다.

데이터 artifact의 자동 cue 검사에 `full_text note audited`가 붙던 기본 문구를 `note_cue_scan`으로 수정했다. 신규17개 미확인 항목에 반영했으며 과거 수동 검토 profile은 보존한다. RFMPose의 태그는 기존 `Flow Matching`과 통일했고 새 노트의 중복 마침표도 제거했다.

## 현재 상태

Registry **1,224편·표준 노트6,120개**, CORE50/NEXT424/REFERENCE508/ARCHIVE242, 집중 읽기474편. Source evidence FULL_TEXT_CHECKED968/ABSTRACT_CHECKED256. 연구 후보의 효과·신규성·native 검증 상태는 바꾸지 않는다. 11/17의 daemon 실패를 오늘의 재측정으로 기록하지 않으며 이번 작업은 registry 유지보수로 실험을 요청하거나 실행하지 않았다.

[3D 비교](../../synthesis/07_robotics_3d_perception.md#pose-reconstruction-2026)·[VLA](../../synthesis/04_vla_generalist.md)·[RL](../../synthesis/02_rl_il_offline.md)에 정독 전 비교 질문을 연결했다. 사실 전수 검증 범위는 전체1,224편의 **구조·identity·tier·link**이며, 과학적 내용의 새 인터넷 확인은 위 추가/승격 문헌과 관련 공개 자료에 한정한다.

## 검증과 게시

<!-- VALIDATION:START -->
- `audit_repository.py`: **PASS — 오류0·경고0**, paper1,224·note6,120·markdown6,343·local link13,592.
- 읽기 이력 단위검사6개·문서 유지보수 단위검사8개 PASS. Active/history 합집합의 기존502개 행의 상태·evidence·사용자 분석 필드가 보존됐다.
- Tier/등록/profile script 컴파일, tier·catalog·resource/index 재생성, priority reconciliation dry-run(변경0), `git diff --check` PASS.
- 기존1,206편 manifest는 승격2편의 curation 외 동일. 기존6,030노트 중6,028개 byte-identical; 승격2편 overview는 읽기 우선순위 header만 변경. Pose/관계 탐색의 기존 재현 파일17개도 byte-identical.
- 초기 검사의 태그 대소문자 충돌·manifest hash 불일치를 수정한 뒤 전체 감사 PASS. 미확인 native 효과·읽기 상태의 임의 승격은 없다.
- Staged 변경246파일·binary0·`git diff --cached --check` PASS. 기존 폐기7개 이력/재현 자료와 새 registry 보강만 포함한다. GitHub 게시·remote clone 확인을 이어서 수행하며 게시 commit은 아래에 기록한다.
<!-- VALIDATION:END -->
