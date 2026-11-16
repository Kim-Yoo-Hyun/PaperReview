# 공식 논문 보완·문서 정리 — 2026-11-02

- Task: **REG-R7**
- 범위: 2024–2026을 검색 창으로 두고 최근 공식 proceedings/publisher에서 VLA·robot data·manipulation/mobile manipulation의 빠진 비교 기준을 보완했다. 최종 등록은 2025년 1편·2026년 9편이다. 모든 학회나 기존 1,080편의 최신 status를 전수 조사한 작업은 아니다.
- [등록 입력](../sources/registry_admissions_2026-11-02.json) · [정리·보존·검증 ledger](../sources/registry_maintenance_2026-11-02.json)
- 기존 연구 후보의 과학적 판단·실행 순서는 유지했다. 신규 문헌 등록이나 노트 작성은 정독·재현·연구 효과의 증거가 아니다.

## 추가한 논문과 선정 이유

| 논문 | 공식 게재 | Tier | 추가 목적 |
|---|---|---|---|
| [RICL](../../2025/CoRL/2025_CoRL_RICL-Adding-In-Context-Adaptability-to-Pre-Trained-Vision/01_overview.md) / pr-1081 | CoRL 2025 · [공식 근거](https://proceedings.mlr.press/v305/sridhar25a.html) | NEXT | 시연 검색으로 적응 능력을 부여하는 직접 선행 |
| [MemER](../../2026/ICLR/2026_ICLR_Scaling-up-Memory-for-Robotic-Control-via-Experience-Retri/01_overview.md) / pr-1082 | ICLR 2026 · [공식 근거](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) | NEXT | Episode 기억과 외부 시연 bank를 구분하는 비교 기준 |
| [LIBERO-X](../../2026/RSS/2026_RSS_LIBERO-X-Robustness-Litmus-for-Vision-Language-Action-Mode/01_overview.md) / pr-1083 | RSS 2026 · [공식 근거](https://roboticsproceedings.org/rss22/p097.html) | NEXT | 복합 시각·공간·지시 shift benchmark |
| [A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation](../../2026/RSS/2026_RSS_A-Systematic-Study-of-Data-Modalities-and-Strategies-for-C/01_overview.md) / pr-1084 | RSS 2026 · [공식 근거](https://roboticsproceedings.org/rss22/p007.html) | NEXT | 데이터 modality와 학습 단계의 단순 대안 |
| [Emergence of Human to Robot Transfer in Vision-Language-Action Models](../../2026/RSS/2026_RSS_Emergence-of-Human-to-Robot-Transfer-in-Vision-Language-Ac/01_overview.md) / pr-1085 | RSS 2026 · [공식 근거](https://roboticsproceedings.org/rss22/p072.html) | NEXT | 사람→로봇 전이의 사전학습 다양성 조건 |
| [Legato](../../2026/RSS/2026_RSS_Learning-Native-Continuation-for-Action-Chunking-Flow-Poli/01_overview.md) / pr-1086 | RSS 2026 · [공식 근거](https://roboticsproceedings.org/rss22/p058.html) | NEXT | Chunk 경계·제어 지연의 직접 선행 |
| [Dejavu](../../2026/CVPR/2026_CVPR_Dejavu-Towards-Experience-Feedback-Learning-for-Embodied-I/01_overview.md) / pr-1087 | CVPR 2026 · [공식 근거](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) | NEXT | 경험 bank + RL residual이라는 기존 조합 |
| [SAGA](../../2026/RA-L/2026_RA-L_SAGA-Open-World-Mobile-Manipulation-via-Structured-Afforda/01_overview.md) / pr-1088 | RA-L 2026 · [공식 근거](https://ieeexplore.ieee.org/document/11568510/) | NEXT | 3D affordance와 whole-body 제어 연결 |
| [Residual Semantic Steering](../../2026/ACL/2026_ACL_Stable-Language-Guidance-for-VisionLanguageAction-Models/01_overview.md) / pr-1089 | ACL 2026 · [공식 근거](https://aclanthology.org/2026.acl-long.190/) | NEXT | 지시 표현 민감성과 의미 steering의 대안 |
| [LILAC](../../2026/RA-L/2026_RA-L_LILAC-Language-Conditioned-Object-Centric-Optical-Flow-for/01_overview.md) / pr-1090 | RA-L 2026 · [공식 근거](https://ieeexplore.ieee.org/abstract/document/11478289) | REFERENCE | Flow→6-DoF 개방루프 표현의 참고 자료 |

CoRL은 PMLR, ICLR/RSS는 공식 proceedings, CVPR은 CVF Open Access, ACL은 Anthology, RA-L은 IEEE publisher의 서지/abstract를 근거로 확인했다. 일부 CVF/IEEE 직접 요청은 접근 제한이 있어 같은 공식 페이지의 검색 색인 내용과 저자 project를 대조했다. 기관/저자 자료보다 공식 게재 상태를 우선했고 oral/award는 추정하지 않았다.

제목·별칭·고유 구절·arXiv/DOI/OpenReview 식별자를 로컬 registry와 대조했다. 등록 dry-run 결과는 **10편 승인, 제목/identifier 충돌 0**이었다. 공식 source와 저자 repo만을 최종 근거로 사용했고 별도 awesome-list/블로그의 해석은 논문 사실로 옮기지 않았다.

## 근거 경계와 발견한 불일치

- **MemER:** 공식 proceedings와 project의 상위 Qwen 크기가 각각 7B/3B로 다르다. 어느 버전을 실행할지 확정하지 않고 method 검토 질문으로 남겼다. 공식 title과 project title의 Robot/Robotic·MemER 접두사 차이는 alias로 연결했다.
- **SAGA:** 저자 lab page의 under-review 문구보다 IEEE RA-L 2026 게재 정보를 우선했다.
- **LILAC:** publisher abstract와 project의 loss/adapter 이름 차이는 원문 version 확인 항목이다. Code/data의 coming-soon을 released로 표시하지 않았다.
- **LIBERO-X:** 공개 project와 실제 코드 repo를 구분했다. Training-data 공개 안내를 전체 checkpoint·init-state 검증으로 확대하지 않았다.
- **Dejavu:** 고정 backbone에 RL로 학습한 residual과 경험 bank를 결합한다. “Frozen VLA + 경험 bank” 자체가 새 기여라는 주장을 지지하지 않는다. 현재 시연 검색 후보는 target support 고정의 제한된 진단으로 유지하며 과거 NO-GO/HOLD를 자동 재개하지 않았다.
- **보류/중복:** 기존 OTTER(ICML 2025)는 재등록하지 않았다. Retrieval-VLA의 정확한 CVPR 공식 title/entry는 이번 검색에서 충분히 확정하지 못해 추가하지 않았다. AR-VLA·offline liveness 평가 등은 발견했으나 이번 직접 missing-link 보완 범위에서는 등록 심사를 완료하지 않았다. 미등록이 연구 공백이나 논문 가치 부재를 뜻하지 않는다.

모든 신규 노트는 **ABSTRACT_CHECKED**다. 전체 본문 수치·평가 split·실패를 임의로 채우지 않았다. 기존 5개 파일 구조와 canonical overview를 유지하면서 반복 problem/method 문단과 일반 checklist를 줄였다. 생성된 초안 89,473자에서 수동 정리한 본문 58,591자로 축약했고, 실제 Tier header 동기화는 이후 수행했다. 사용자 읽기 상태는 기존 그대로이며 NEXT 신규 9행만 UNREAD로 추가했다.

## 삭제·병합·보존

| 대상 | 처리 |
|---|---|
| 시연 검색 통합 보고서의 과거 설계·반복 완료 설명 | 387 → 175행. R1/R2의 핵심 변경을 요약하고 현행 N1·revision 3 계약에 연결. R1/R2/A1/N1 anchor와 source/실제 실행 근거 보존 |
| TODO·root/research/work 안내의 중복 완료 이력 | 활성 상태와 날짜별 결과 링크로 축약. 과거 수량은 기존 audit log에 보존 |
| Python bytecode cache 2개 | 개별 hash 확인 후 삭제. Source script와 사용 중인 dependency 선언은 보존 |
| 동일한 과거 Docker version JSON 2개 | 서로 다른 실험의 실행 당시 증거이므로 각각 보존 |
| 논문·PDF·원시 결과·P0 packet·source ledger | 삭제하지 않음. 불필요하다는 근거가 없는 package/환경 자산도 변경하지 않음 |

이번에 삭제한 문서 파일은 없다. 중복은 문서 내부에서 병합했으며 독립적인 source 기록을 통째로 지우지 않았다. Docker/정책/embedding 실행, host package 설치, weights/PDF 다운로드, commit/push는 하지 않았다.

## 갱신된 규모와 연결

- 전체 **1,080 → 1,090편**, 표준 노트 **5,400 → 5,450개**.
- CORE **47**, NEXT **305 → 314**, REFERENCE **486 → 487**, ARCHIVE **242**.
- 집중 읽기 **352 → 361편**, inactive history **47편**.
- LIBERO-X benchmark 탐색 항목 추가: benchmark **56**, metric **29**, 통합 resource **570**. 자동 연결은 `cue_only`.
- PAPER·tier/plan/tracker·registry index/stats/resources·README/AGENTS·3개 synthesis의 비교 질문과 전체 generated queue를 동기화했다. 별도 priority/gap 목록은 만들지 않았다.

## 검증

- `build_reading_tiers.py`·`build_registry_catalogs.py` 구문 검사와 tier/plan/tracker/queue, priority header, catalog/view 생성 완료.
- `audit_repository.py`: **오류 0, 경고 0**. 논문 1,090편·노트 5,450개·집중 읽기 361편·Markdown link 11,555개 확인.
- `test_reading_history.py` **6/6**, `test_document_maintenance.py` **6/6** 통과. Working tree와 staged diff의 whitespace 검사 통과.
- 시작 시 SHA-256 snapshot과 대조: 기존 노트 **5,400/5,400**, manifest entry **1,080/1,080**, 사용자 읽기 입력 **399/399**, 연구/실험 파일 **303/303**, staged index 모두 보존.
- 전체 표준 노트 **5,450개**의 C0/C1 제어문자 이상 **0**. 신규 50개 노트의 title/evidence 표기 확인. NEXT 신규 9행은 `UNREAD + ABSTRACT_CHECKED`이며 기존 status 승격 없음.
- 신규 insights의 반복 실험 문구를 논문별 비교·반증 질문으로 구체화했다. 기존 논문 본문 노트는 변경하지 않았다.

작업 완료는 registry 유지보수의 완료다. 신규 논문의 본문 정독, MemER/LILAC source version 불일치 해소, 연구 가설의 정책 실험 검증은 완료 범위에 포함하지 않는다.
