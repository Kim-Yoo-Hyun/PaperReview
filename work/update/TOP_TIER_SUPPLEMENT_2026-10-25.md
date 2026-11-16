# 2024–2026 top-tier Robotics/AI 보완 — REG-R3

- Checked: 2026-10-25 KST
- 전체 **1,055 → 1,072편**, 표준 노트 **5,275 → 5,360개**. 신규 **17편 / 노트 85개**.
- CORE **47**, NEXT **285 → 297**, REFERENCE **481 → 486**, ARCHIVE **242**. 기존 논문의 tier는 유지한다.
- 신규 17편은 peer-reviewed publication이 확인된 문헌이다. 모두 `ABSTRACT_CHECKED`; NEXT 12편의 사용자 읽기 상태는 `UNREAD`다.
- 범위: 현재 registry의 누락과 기존 gap의 비교 필요성을 기준으로 CoRL·ICRA·ICCV·ICLR·ICML 및 IJRR·RA-L·Nature Machine Intelligence·Science Robotics를 교차 확인했다. 해당 기간 모든 venue/논문의 전수 조사나 모든 본문 정독은 아니다.

## 무엇을 보완했는가

1. **VLA 평가·실행:** RoboArena, STAR-Gen, Gen2Act, Mobility VLA. 실환경 정책 순위·일반화 축·video-to-action·tour-to-navigation을 구분한다.
2. **데이터·적응·구조적 일반화:** ReMix, DexMimicGen, TRANSIC, Equivariant Diffusion Policy의 IJRR 확장. Domain mixture, 생성 trajectory, 인간 correction, 기하학적 대칭성을 서로 다른 대안으로 연결한다.
3. **접촉·이동·3D:** FMB, visuotactile estimation/control, TidyBot++, PhysTwin. 실제 제어·접촉·planning을 지원하는 자산을 우선했다. Process-centric tactile taxonomy는 전문가 명세와 skill/controller 비교용 REFERENCE다.
4. **AI 방법론:** General agents need world models, WorldTest, Delphic, DML-IL. 환경 이해·정보 비대칭·식별 가정의 참조이며, 이들의 이론·grid-world·의료 결과를 VLA 정책 효과로 확대하지 않는다.

이 분류와 중요도는 연구자 해석이다. 개별 paper의 source claim·최소 비교·확인 필요 사항은 각 5개 노트에 분리했다. 최신 읽기 순서는 [READING_PLAN](../../research/READING_PLAN.md) 하나에서 관리한다.

## 신규 등록

| ID | 논문 / 노트 | 출판 | Tier | Publication 근거 |
|---|---|---|---|---|
| pr-1056 | [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../../2025/CoRL/2025_CoRL_RoboArena-Distributed-Real-World-Evaluation-of-Generalist/01_overview.md) | 2025 CoRL | NEXT | [근거](https://proceedings.mlr.press/v305/atreya25a.html) |
| pr-1057 | [A Taxonomy for Evaluating Generalist Robot Manipulation Policies](../../2026/RA-L/2026_RA-L_A-Taxonomy-for-Evaluating-Generalist-Robot-Manipulation-Po/01_overview.md) | 2026 RA-L | NEXT | [근거](https://api.crossref.org/works/10.1109/LRA.2026.3656785) |
| pr-1058 | [FMB: A functional manipulation benchmark for generalizable robotic learning](../../2025/IJRR/2025_IJRR_FMB-A-functional-manipulation-benchmark-for-generalizable/01_overview.md) | 2025 IJRR | NEXT | [근거](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) |
| pr-1059 | [ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning](../../2025/CoRL/2025_CoRL_ReMix-Optimizing-Data-Mixtures-for-Large-Scale-Imitation-L/01_overview.md) | 2025 CoRL (개최 2024) | NEXT | [근거](https://proceedings.mlr.press/v270/hejna25a.html) |
| pr-1060 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../../2025/ICRA/2025_ICRA_DexMimicGen-Automated-Data-Generation-for-Bimanual-Dextero/01_overview.md) | 2025 ICRA | NEXT | [근거](https://api.crossref.org/works/10.1109/ICRA55743.2025.11127809) |
| pr-1061 | [TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction](../../2025/CoRL/2025_CoRL_TRANSIC-Sim-to-Real-Policy-Transfer-by-Learning-from-Onlin/01_overview.md) | 2025 CoRL (개최 2024) | NEXT | [근거](https://proceedings.mlr.press/v270/jiang25a.html) |
| pr-1062 | [Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation](../../2025/CoRL/2025_CoRL_Gen2Act-Human-Video-Generation-in-Novel-Scenarios-enables/01_overview.md) | 2025 CoRL | NEXT | [근거](https://proceedings.mlr.press/v305/bharadhwaj25a.html) |
| pr-1063 | [Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs](../../2025/CoRL/2025_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md) | 2025 CoRL (개최 2024) | NEXT | [근거](https://proceedings.mlr.press/v270/xu25b.html) |
| pr-1064 | [TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning](../../2025/CoRL/2025_CoRL_TidyBot%2B%2B-An-Open-Source-Holonomic-Mobile-Manipulator-for/01_overview.md) | 2025 CoRL (개최 2024) | NEXT | [근거](https://proceedings.mlr.press/v270/wu25a.html) |
| pr-1065 | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../../2025/ICCV/2025_ICCV_PhysTwin-Physics-Informed-Reconstruction-and-Simulation-of/01_overview.md) | 2025 ICCV | NEXT | [근거](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) |
| pr-1066 | [Equivariant diffusion policy for sample-efficient robotic manipulation](../../2026/IJRR/2026_IJRR_Equivariant-diffusion-policy-for-sample-efficient-robotic/01_overview.md) | 2026 IJRR | NEXT | [근거](https://journals.sagepub.com/doi/10.1177/02783649261424445) |
| pr-1067 | [A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills](../../2025/Nature-Machine-Intellige/2025_Nature-Machine-Intellige_A-process-centric-manipulation-taxonomy-for-the-organizati/01_overview.md) | 2025 Nature Machine Intelligence | REFERENCE | [근거](https://www.nature.com/articles/s42256-025-01045-3) |
| pr-1068 | [Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions](../../2025/CoRL/2025_CoRL_Learning-Visuotactile-Estimation-and-Control-for-Non-prehe/01_overview.md) | 2025 CoRL (개최 2024) | NEXT | [근거](https://proceedings.mlr.press/v270/ferrandis25a.html) |
| pr-1069 | [General agents need world models](../../2025/ICML/2025_ICML_General-agents-need-world-models/01_overview.md) | 2025 ICML | REFERENCE | [근거](https://proceedings.mlr.press/v267/richens25a.html) |
| pr-1070 | [Benchmarking World-Model Learning with Environment-Level Queries](../../2026/ICML/2026_ICML_Benchmarking-World-Model-Learning-with-Environment-Level-Q/01_overview.md) | 2026 ICML | REFERENCE | [근거](https://proceedings.mlr.press/v306/warrier26a.html) |
| pr-1071 | [Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding](../../2024/ICLR/2024_ICLR_Delphic-Offline-Reinforcement-Learning-under-Nonidentifiab/01_overview.md) | 2024 ICLR | REFERENCE | [근거](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html) |
| pr-1072 | [Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding](../../2026/ICLR/2026_ICLR_Causal-Imitation-Learning-under-Expert-Observable-and-Expe/01_overview.md) | 2026 ICLR | REFERENCE | [근거](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html) |

## Publication·version·접근 경계

- **HIL-SERL(pr-0914):** 기존 arXiv 2024 entry를 Science Robotics 2025로 정정했다. DOI `10.1126/scirobotics.ads5033`, volume 10 issue 105, 출판 2025-08-20은 [publisher-deposited Crossref](https://api.crossref.org/works/10.1126/scirobotics.ads5033)에서 확인했다. [Publisher](https://www.science.org/doi/10.1126/scirobotics.ads5033) 직접 HTML은 403이어서 본문 재정독으로 표시하지 않았다. 기존 ID·CORE·읽기 입력·preprint PDF 분석 본문을 보존하고 현행 경로/링크만 이관했다.
- **STAR-Gen·DexMimicGen:** IEEE 직접 페이지는 접근 제한이었다. IEEE-deposited DOI metadata와 저자 [STAR-Gen](https://stargen-taxonomy.github.io/)·[DexMimicGen](https://dexmimicgen.github.io/)의 venue 표기를 교차 확인했다. Abstract 내용은 연결된 arXiv/project에서 읽었다.
- **CoRL 2024 / PMLR 2025:** ReMix·TRANSIC·Mobility VLA·TidyBot++·visuotactile 논문은 개최 2024, 출판 2025다. Folder/year는 출판 연도, `publication.venue_year`는 개최 연도다. [PMLR 270](https://proceedings.mlr.press/v270/)
- **FMB:** 온라인 선출판 2024-09-22와 2025 권호를 구분한다. Registry는 권호의 2025로 등록했다. [IJRR](https://journals.sagepub.com/doi/full/10.1177/02783649241276017)
- **Equivariant Diffusion Policy:** CoRL 원판도 미등록이므로 [IJRR 2026 확장판](https://journals.sagepub.com/doi/10.1177/02783649261424445) 하나를 canonical entry로 추가했다. 원판 제목은 alias, 확장 관계는 계보에 남겼다. Journal 설명은 point-cloud/translation symmetry 확장을 명시한다. 연결 repository는 원판 기반이며 journal 전체 구현 coverage는 확인하지 않았다. 별도 원판 중복 등록은 하지 않았다.
- **Nature Machine Intelligence tactile taxonomy:** 공식 검색 인덱스의 abstract/서지정보를 사용했다. 직접 HTML은 인증 redirect로 제한되어 전체 본문 확인으로 기록하지 않았다. [Publisher](https://www.nature.com/articles/s42256-025-01045-3)
- **WorldTest software:** 공식 proceedings가 연결한 Zenodo 링크만 확보했다. Landing 접근 실패로 payload·실행 가능성·code release를 확인한 것으로 표시하지 않았다.
- Code 링크는 공개 repository/저자 연결 확인 수준이며 dependency 설치·코드 실행·checkpoint 검증과 다르다.

## 중복 및 보류한 후보

| 후보 | 결정과 이유 |
|---|---|
| Dobb-E / On Bringing Robots Home | pr-0669에 이미 존재. 이번 확인에서 top-tier 출판의 확정 근거를 확보하지 못해 기존 arXiv entry 유지 |
| HIL-SERL | pr-0914의 journal metadata 갱신; 신규 논문 수에 포함하지 않음 |
| OpenVLA·RoboMIND·NaVILA·NoMaD·DROID·RoboCasa | 기존 identity 확인, 신규 등록 제외 |
| Equivariant Diffusion Policy 원판 | IJRR 확장판의 alias/계보로 연결해 한 entry 유지 |
| EquiBot | 관련 CoRL 연구로 발견. 이번에는 EquiDiff journal·기존 ET-SEED/SDP와의 우선 차별 역할을 좁히지 못해 추가 보류; 낮은 연구 가치 판정은 아님 |
| 2026 IJRR neurosymbolic manipulation / standard skill-agent library | 공식 abstract 후보로 확인. 현재 skill/controller·language 선행 대비 꼭 필요한 비교 역할을 확정하지 않아 미등록 |
| Nature Machine Intelligence spherical hand mechanism | 하드웨어 중심 contribution. 현재 VLA/control 연구에 필요한 새 비교 조건을 특정하지 않아 미등록 |

## 정합 및 생성기 보완

- `register_papers.py` dry-run에서 title/identifier collision 0건 확인 후 17편 등록했다. 별도 normalized title/alias 검사와 `rg` phrase/identifier 검색으로 역사 문헌 언급을 실제 등록과 구분했다.
- Metadata normalizer가 명시적 개최 연도를 출판 연도로 덮어쓰던 부분을 수정했다. REG-R2의 pr-1044도 기존 source 설명과 맞도록 `venue_year=2024`로 정합했다.
- `TidyBot++`의 encoded Markdown 경로(`%2B%2B`)를 파일로 열 때 decode하도록 reading generator와 CORE note audit를 수정했다. CSV/Markdown의 URL 표기와 실제 파일명을 구분한다.
- HIL-SERL 공식 title의 대소문자 변화에 맞춰 CORE exact query를 갱신했다. 본문 페이지 근거는 기존 preprint를 계속 가리킨다.
- 기존 REG-R2 보고서의 누락된 표 header를 보완하고 event-year 실제 수정 시점을 명시했다.

## 검증과 인계

실제 명령 결과·tracker 보존·파일 변경 범위는 [source/validation ledger](../sources/top_tier_supplement_review_2026-10-25.json)에 기록한다. 기존 사용자 상태·분석은 active/history 합집합에서 비교하고 HIL-SERL의 경로/서지 자동 필드와 sequence 변경만 구분한다.

`py_compile`, reading generator, priority-only reconcile의 dry-run/apply, catalog/view의 dry-run/apply, repository audit, `git diff --check`를 완료했다. **최종 audit 오류·경고 0**, 기존 1,055편 tier와 active 332행·history 47행의 사용자 입력을 보존했다. Metadata normalizer 4조건·TidyBot++ 경로/identity·generator 재실행 안정성을 확인했다. 전체 표준 노트 5,360개에서 C0/C1 잔여 0, 신규 85개 title/source/evidence header와 HIL-SERL 기존 분석 본문 보존도 확인했다. 새 문헌은 6개 synthesis의 읽기 전 비교 연결로 추가했으며 완료된 reading matrix를 덮어쓰지 않았다.

연구 후보의 기존 HOLD/NO-GO, 전체 N3 PARTIAL·N3-B WAITING_RESOURCE를 유지한다. 신규 논문 등록은 연구 재개나 가설 입증이 아니다. PDF 다운로드/삭제·설치·Docker 변경·실험·Git commit/push는 하지 않았다. 다음 활성 행동은 [TODO](../../TODO.md)를 따른다.
