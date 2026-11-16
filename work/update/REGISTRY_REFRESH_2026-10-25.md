# REG-R2 — Registry 갱신: 2026-10-25

- 상태: **DONE**. 등록·문서 동기화·최종 audit 완료; 오류 0·경고 0. [source/validation ledger](../sources/registry_refresh_review_2026-10-25.json).
- 범위: 최근 gap 조사에서 인용한 미등록 직접 선행과 VLA 평가 자산을 우선한 incremental update. 2024–2026 공식 proceedings/저자 source를 확인했다. 모든 1,055편의 출판 상태나 해당 기간의 모든 학회를 전수 재조사한 작업은 아니다.
- 전체 **1,037 → 1,055편**, 표준 노트 **5,185 → 5,275개**. CORE **47**, NEXT **275 → 285**, REFERENCE **473 → 481**, ARCHIVE **242**.
- 신규 18편은 **ABSTRACT_CHECKED**; 새 집중 읽기 10편은 **UNREAD**. 기존 1,037편의 tier와 사용자 읽기 이력은 보존한다. 논문 추가는 후보 GO나 native 검증 완료를 뜻하지 않는다.

## 선정 기준과 변경

VLA의 memory·강건성·sensor interface, policy-aware 데이터 선택, world-model 평가를 보강했다. Manipulation의 물성/부착 조건, navigation uncertainty, affordance의 행동 연결은 기존 gap 판단에 직접 필요한 비교 문헌으로 추가했다. Venue quota나 논문 수를 맞추지 않았다. 기존 AIR-VLA는 이미 등록되어 있어 신규로 세지 않는다.

- **기준 평가·직접 비교:** DataMIL, What Matters, RoboMME, LIBERO-Plus, THE COLOSSEUM, FuSe, activation steering, sensor failure training, dWorldEval, conformal crowd navigation은 NEXT.
- **필요시 참조:** DARP, STAFF, proxy 학습 설정 연구, JIGGLE, AdaptiGraph, Robo-ABC, LIBERO-PRO, Colosseum V2는 REFERENCE. STAFF/proxy 학습 논문은 LLM 근거이며 VLA task 성공까지 검증한 것으로 해석하지 않는다.
- Canonical priority는 [READING_PLAN](../../research/READING_PLAN.md)과 generator에만 둔다. 이 문서는 해당 날짜의 변경 기록이다.

## 신규 등록

| ID | 논문 / 노트 | Publication / source | Tier |
|---|---|---|---|
| pr-1038 | [What Matters in Learning from Large-Scale Datasets for Robot Manipulation](../../2025/ICLR/2025_ICLR_What-Matters-in-Learning-from-Large-Scale-Datasets-for-Rob/01_overview.md) | 2025 ICLR · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html) | NEXT |
| pr-1039 | [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](../../2026/ICLR/2026_ICLR_DataMIL-Selecting-Data-for-Robot-Imitation-Learning-with-D/01_overview.md) | 2026 ICLR · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) | NEXT |
| pr-1040 | [Difference-Aware Retrieval Policies for Imitation Learning](../../2026/ICLR/2026_ICLR_Difference-Aware-Retrieval-Policies-for-Imitation-Learning/01_overview.md) | 2026 ICLR · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) | REFERENCE |
| pr-1041 | [STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](../../2025/ICLR/2025_ICLR_STAFF-Speculative-Coreset-Selection-for-Task-Specific-Fine/01_overview.md) | 2025 ICLR · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html) | REFERENCE |
| pr-1042 | [Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice](../../2026/ICLR/2026_ICLR_Can-Small-Training-Runs-Reliably-Guide-Data-Curation-Rethi/01_overview.md) | 2026 ICLR · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html) | REFERENCE |
| pr-1043 | [Mechanistic Interpretability for Steering Vision-Language-Action Models](../../2025/CoRL/2025_CoRL_Mechanistic-Interpretability-for-Steering-Vision-Language/01_overview.md) | 2025 CoRL · [공식 근거](https://proceedings.mlr.press/v305/haon25a.html) | NEXT |
| pr-1044 | [Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure](../../2025/CoRL/2025_CoRL_Simple-Masked-Training-Strategies-Yield-Control-Policies-T/01_overview.md) | 2025 CoRL · [공식 근거](https://proceedings.mlr.press/v270/skand25a.html) | NEXT |
| pr-1045 | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](../../2026/CVPR/2026_CVPR_LIBERO-Plus-A-Progressive-Robustness-Benchmark-for-Visual/01_overview.md) | 2026 CVPR · [공식 근거](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) | NEXT |
| pr-1046 | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](../../2024/RSS/2024_RSS_THE-COLOSSEUM-A-Benchmark-for-Evaluating-Generalization-fo/01_overview.md) | 2024 RSS · [공식 근거](https://roboticsproceedings.org/rss20/p133.html) | NEXT |
| pr-1047 | [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../../2026/ICML/2026_ICML_RoboMME-Benchmarking-and-Understanding-Memory-for-Robotic/01_overview.md) | 2026 ICML · [공식 근거](https://proceedings.mlr.press/v306/dai26c.html) | NEXT |
| pr-1048 | [Scaling Robot Policy Evaluation via Discrete Diffusion World Model](../../2026/ICML/2026_ICML_Scaling-Robot-Policy-Evaluation-via-Discrete-Diffusion-Wor/01_overview.md) | 2026 ICML · [공식 근거](https://proceedings.mlr.press/v306/li26hi.html) | NEXT |
| pr-1049 | [Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling](../../2025/CoRL/2025_CoRL_Towards-Generalizable-Safety-in-Crowd-Navigation-via-Confo/01_overview.md) | 2025 CoRL · [공식 근거](https://proceedings.mlr.press/v305/yao25a.html) | NEXT |
| pr-1050 | [JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments](../../2024/RSS/2024_RSS_JIGGLE-An-Active-Sensing-Framework-for-Boundary-Parameters/01_overview.md) | 2024 RSS · [공식 근거](https://www.roboticsproceedings.org/rss20/p007.html) | REFERENCE |
| pr-1051 | [AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation](../../2024/RSS/2024_RSS_AdaptiGraph-Material-Adaptive-Graph-Based-Neural-Dynamics/01_overview.md) | 2024 RSS · [공식 근거](https://roboticsproceedings.org/rss20/p010.html) | REFERENCE |
| pr-1052 | [Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation](../../2024/ECCV/2024_ECCV_Robo-ABC-Affordance-Generalization-Beyond-Categories-via-S/01_overview.md) | 2024 ECCV · [공식 근거](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) | REFERENCE |
| pr-1053 | [Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](../../2025/ICRA/2025_ICRA_Beyond-Sight-Finetuning-Generalist-Robot-Policies-with-Het/01_overview.md) | 2025 ICRA · [공식 근거](https://arxiv.org/abs/2501.04693) | NEXT |
| pr-1054 | [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](../../2025/arXiv/2025_arXiv_LIBERO-PRO-Towards-Robust-and-Fair-Evaluation-of-Vision-La/01_overview.md) | 2025 arXiv · [공식 근거](https://arxiv.org/abs/2510.03827) | REFERENCE |
| pr-1055 | [Colosseum V2: Benchmarking Generalization for Vision Language Action Models](../../2026/arXiv/2026_arXiv_Colosseum-V2-Benchmarking-Generalization-for-Vision-Langua/01_overview.md) | 2026 arXiv · [공식 근거](https://arxiv.org/abs/2605.27759) | REFERENCE |

## Publication·identity와 source 경계

- **16편은 공식 peer-reviewed publication, 2편은 preprint.** LIBERO-PRO와 Colosseum V2는 정식 acceptance를 확인하지 못해 arXiv로 등록했다. 저자/third-party 언급만으로 승격하지 않는다.
- LIBERO-Plus의 기존 arXiv 제목을 alias로 보존하고 CVPR 2026의 final title로 한 번만 등록했다. [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html)
- dWorldEval의 final title과 project/preprint title을 같은 arXiv identity 안에 연결했다. Official final authors/title을 기준으로 삼으며, final/preprint 본문이 동일하다고 판단한 것은 아니다. [PMLR](https://proceedings.mlr.press/v306/li26hi.html), [저자 project](https://dworldeval.github.io/)
- Masked training 논문은 **CoRL 개최 2024 / PMLR 출판 2025**다. Folder/registry year는 publication 2025다. REG-R3에서 normalizer가 덮어쓴 값을 발견해 `publication.venue_year=2024`로 실제 정합했다. [PMLR volume 270](https://proceedings.mlr.press/v270/), [paper](https://proceedings.mlr.press/v270/skand25a.html), [후속 정합](./TOP_TIER_SUPPLEMENT_2026-10-25.md)
- FuSe의 IEEE 직접 페이지는 challenge로 본문이 제공되지 않았다. IEEE가 기탁한 Crossref의 title·DOI·conference·event date가 ICRA 2025와 일치한다. 내용 요약은 저자 abstract/project 수준이다. [Crossref record](https://api.crossref.org/works/10.1109/ICRA55743.2025.11127987), [저자 project](https://fuse-model.github.io/)
- Exact/normalized title·alias·공개 ID 충돌은 0건. Distinctive phrase 검색에서 LIBERO-Plus/PRO가 기존 논문의 evaluation/lineage에 등장했지만 독립 paper entry는 아니었다.
- PDF를 내려받거나 이전 노트를 일괄 재생성하지 않았다. 본문·code를 더 깊게 확인한 과거 dossier는 당시 범위로 보존하고, 신규 등록 노트에 그 깊이를 자동 전이하지 않았다.

## 기존 metadata 정합

| ID | 변경 | 유지한 경계 |
|---|---|---|
| pr-0150 AIR-VLA | Primary source를 OpenReview에서 공식 PMLR ICML 2026 paper page로 갱신하고 venue verification 추가 | 기존 ID·year·venue·tier, PDF source와 과거 본문 검토, 모든 분석 본문 보존. Final 본문 재검토 아님 |
| pr-1022 RoboReward | arXiv v2 metadata와 저자가 연결한 HELM project URL 반영 | arXiv 유지. 목적지 HTML은 client-rendered shell이며 code/data/checkpoint 공개 범위·실행 가능성을 검증한 것은 아님 |

AIR-VLA의 근거는 [공식 proceedings](https://proceedings.mlr.press/v306/sun26an.html), RoboReward의 project 연결 근거는 [저자 arXiv abstract](https://arxiv.org/abs/2601.00675)다. OpenReview challenge를 acceptance 확인으로 세지 않았다. SmolVLA와 Leave No Observation Behind는 조회한 arXiv record에서 신규 publication을 확인하지 못해 유지했다. Rethinking VLA Scaling도 공식 acceptance를 새로 확인하지 못해 그대로다.

## 검증과 다음 행동

등록 dry-run/apply, tier generator compile·재생성, priority-only reconcile dry-run/apply, catalog/view 재생성, repository audit와 diff 검사를 수행했다. 첫 audit에서 신규 18편의 note별 evidence map 누락을 발견해 실제 header와 정합화하고 등록기를 보완했다. 임시 registry에서 dry-run 무변경·5개 note 근거 기록·기존 record 보존을 확인했다. 기존 tracker의 자동 sequence만 새 문헌 삽입에 따라 바뀌며 사용자 상태·분석은 유지한다. 최종 audit 및 dirty 파일·실행 packet 보존은 ledger의 실제 비교 결과를 따른다.

Registry 갱신 후의 연구 실행 단계는 [TODO](../../TODO.md)를 따른다. **GAP-N3-B WAITING_RESOURCE / 전체 N3 PARTIAL**, 기존 NO-GO/HOLD는 유지한다. 환경 구성은 [N3-B 설정 문서](../experiments/proxy_observation_contract/ENVIRONMENT.md)에 있으며 이번에는 실험·설치·Docker 변경·Git commit/push를 수행하지 않았다.
