# META-W1 — Splat-Nav 게재처·발표 기록 정합

- Updated: 2026-10-23 KST
- Scope: 기존 `pr-0284` 한 편의 metadata·경로·source link 정합. 신규 등록·tier 변경·본문 재검토·실험은 이 작업 범위에 포함하지 않는다.
- 상태: DONE — metadata 정합과 보존·무결성 검증 완료.

## 확인 결과

Canonical publication은 **IEEE Transactions on Robotics (T-RO), 2025, volume 41, pages 2765–2784**, DOI `10.1109/TRO.2025.3552348`이다. [Publisher-deposited Crossref record](https://api.crossref.org/works/10.1109/TRO.2025.3552348)는 `journal-article`과 IEEE publisher를 명시한다. [DOI](https://doi.org/10.1109/TRO.2025.3552348)는 IEEE document 10930696으로 연결되지만 직접 페이지에는 browser verification challenge가 있어 본문을 재검토한 것으로 기록하지 않았다.

[저자 연구실 목록](https://sites.temple.edu/trail/publications/)은 T-RO 게재와 IROS 2025 presentation을 별도로 연결한다. 이 목록의 [IROS program 링크](https://ras.papercept.net/conferences/conferences/IROS25/program/IROS25_ContentListWeb_3.html)는 이번 web fetch에서 접근되지 않았다. 따라서 발표 사실의 근거는 저자 연구실 표기로 남기며 oral/poster 형식·IROS proceedings 게재를 추정하지 않는다. 연구실의 축약 저자 목록 대신 DOI metadata와 arXiv가 일치하는 9명 저자를 overview에 기록했다.

[arXiv 2403.02751](https://arxiv.org/abs/2403.02751)은 2024-03-05 최초 제출, 확인 시점 최신 v3는 2025-01-11이다. Preprint year 2024와 journal year 2025를 같은 identity 안에 보존한다. [공식 프로젝트](https://chengine.github.io/splatnav/)의 BibTeX는 arXiv 2024 표기이므로 journal publication 판정에 사용하지 않았다. 프로젝트와 연구실에서 연결한 [공개 코드](https://github.com/chengine/splatnav)는 `released`로 정정하되 실행·data payload·runtime 검증으로 승격하지 않았다.

## 변경과 보존

| 항목 | 처리 |
|---|---|
| Paper identity | `pr-0284`, title, arXiv ID 유지; DOI 추가 |
| Canonical publication | IROS / conference → T-RO / journal, 2025 |
| Paper folder | `2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla` → `2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla` |
| 5개 note | 같은 파일을 이관하고 metadata header만 수정; 첫 `##` 이후 분석 본문 보존 |
| Canonical/derived navigation | manifest·PAPER·tracker key·reading plan/tier·synthesis·catalog·resource/index/statistics 동기화 |
| 과거 full-text review manifest 2개 | `folder` 포인터만 이관; review date·PDF hash·추출 근거 유지 |
| GAP-W1/W2 source ledger | 현재 overview 포인터 이관, 별도 resolution 추가; 당시 불일치 관찰은 보존 |
| Historical text | 과거 report 및 `legacy_maintenance_reports.json`의 당시 경로는 역사 기록으로 보존; 현재 실행 경로로 사용하지 않음 |
| Reading | NEXT · UNREAD · FULL_TEXT_CHECKED 유지; 다른 1,036편 metadata 및 active/history 사용자 입력 보존 |

현재 overview는 [Splat-Nav](../../2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md), 기계가 읽을 수 있는 출처·이관 내역은 [source ledger](../sources/splat_nav_metadata_2026-10-23.json)에 있다. 기존 source evidence는 과거 arXiv PDF 검토의 범위를 뜻하며 이번 metadata 수정이 journal 본문의 동등성·연구 효과를 새로 검증했다는 뜻은 아니다. GEOMETRY 후보의 기존 HOLD 판정도 유지한다.

## 검증

- 작업 전 repository audit: 1,037편·표준 note 5,185개, 오류·경고 0.
- `build_reading_tiers.py` compile·재생성, `reconcile_registry.py --priorities-only` dry-run/apply, catalog와 registry view dry-run/apply, repository audit·`git diff --check` 통과. Priority/header 동기화의 추가 변경은 0건이었다.
- 작업 후 audit: 1,037편·표준 note 5,185개·active 322행·history 47행·7개 queue, 오류·경고 0. CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242 유지. 공식 코드 링크 추가로 통합 resource는 521 → 522개다.
- Snapshot 대조: manifest 변경 ID는 `pr-0284` 하나. 다른 1,036개 record는 동일하며 active tracker는 해당 행의 `venue`·`overview_path`만 변경, history는 동일하다. 5개 note의 첫 `##` 이후 분석 본문과 과거 full-text review 2개 record의 경로 외 내용도 동일하다.
- 기존 dirty 파일 165개 중 이 작업에 연결된 7개 문서/ledger만 추가 수정했으며, 나머지 158개는 SHA256이 동일하다. 활성 탐색 경로에 이전 IROS 폴더 참조가 남지 않았음을 확인했다. 신규 등록·읽기 상태 승격·실험·설치·PDF cache·Git 게시는 수행하지 않았다.

## 후속 작업

META-W1 이후 남은 문서 작업은 DOC-QA2의 84편·156개 note 원문 대조다. 먼저 대상과 해당 원문 구간을 확보하고, 수식·문맥을 확인한 뒤 수정해야 한다. PORT-R1은 새 물리 컴퓨터가 필요하며 현재 컴퓨터의 기존 clone/replay 검사를 반복한 것으로 완료 처리하지 않는다. 활성 상태는 [TODO](../../TODO.md)를 따른다.
