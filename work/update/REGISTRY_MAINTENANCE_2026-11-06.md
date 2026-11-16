# Registry 정합성·공식 metadata 갱신·중복 정리

- Work ID: **REG-R10** / 2026-11-06 KST
- 범위: 전체 1,110편의 로컬 identity·분류·노트·링크·생성 view 감사, 주요 preprint **10편**의 공식 publication/source 재확인. 전체 논문의 최신 게재·본문을 인터넷으로 전수 재조사한 것은 아니다.
- [변경·보존·검증 원장](../sources/registry_maintenance_2026-11-06.json) · [현재 TODO](../../TODO.md)

## 실제 metadata 변경

| 항목 | 변경·근거 |
|---|---|
| FlowDreamer, pr-0703 | **2025 arXiv → 2026 RA-L**, DOI·journal title·공식 code 반영. IEEE-deposited [Crossref metadata](https://api.crossref.org/works/10.1109/LRA.2026.3653273)와 [저자 project](https://sharinka0715.github.io/FlowDreamer/)로 확인했다. Xplore의 JS challenge는 우회하지 않았다. [현행 노트](../../2026/RA-L/2026_RA-L_FlowDreamer-A-RGB-D-World-Model-With-Flow-Based-Motion-Rep/01_overview.md) |
| Isaac Lab, pr-0863 | [arXiv 2511.04831](https://arxiv.org/abs/2511.04831) 식별자·primary source와 [공식 code](https://github.com/isaac-sim/IsaacLab) 보완. [공식 문서](https://isaac-sim.github.io/IsaacLab/main/)의 technical-report 인용에 따라 arXiv 유지. 최신 소프트웨어 기능을 2025 논문 결과로 소급하지 않음 |
| AutoRT / GR00T N1 | 누락된 [2401.12963](https://arxiv.org/abs/2401.12963) / [2503.14734](https://arxiv.org/abs/2503.14734) 식별자 추가. GR00T의 공식 paper title을 기존 NVIDIA publication title의 alias로 연결; 중복 항목 생성 없음 |
| 나머지 재확인 | Robotic World Model·DreamZero·Gemini Robotics·SmolVLA·Gemini Robotics 1.5·RoboReward의 arXiv 유지. Workshop listing·under-review 문서·새 제품 landing을 main-conference 채택 근거로 사용하지 않음. 논문별 URL과 한계는 원장 참조 |

FlowDreamer의 stable ID·NEXT membership을 유지하고 journal hierarchy로 폴더를 이동했다. Tracker의 자동 경로/연도/venue/title과 생성 링크를 갱신했으며 사용자 입력은 보존했다. 두 과거 full-text review record에는 현재 identity를 연결하고 원 title/folder는 `identity_at_review`에 남겼다. 당시 PDF hash·검토 날짜·결과는 그대로다. 기존 preprint page anchor를 journal 최종본 확인으로 승격하지 않는다.

## 중복·불필요한 내용 처리

- Root/research/synthesis/work 안내, TODO와 buildup guide의 반복 완료 이력을 현행 주제 index·기존 update log로 통합했다. 현재 **7개**, 11/04 당시 6개, 이전 비교 5개, 과거 정책 준비 묶음 3개를 구별한다. 읽기 계획 생성기의 고정 후보 수·낡은 최신 등록 문구도 제거했다.
- FlowDreamer 5개 노트에서 world model을 QP shield·risk margin·recovery policy로 설명하던 generic safety 해석을 motion/frame prediction·visual planning으로 고쳤다. 중복 읽기 동기·generic 연구 질문을 합치고 기존 preprint 근거·수치·page anchor는 보존했다. 전체 노트의 의미 정확성을 보증하는 작업은 아니다.
- 재생성 가능한 Python bytecode cache **3개**를 삭제했다. 같은 bytes의 navigation `docker_version.json` 2개는 서로 다른 실행 당시 증거여서 각각 보존했다. 사용 중인 dependency 선언·실행 코드·원시 결과·source 원장은 삭제하지 않았다.
- 논문 추가/삭제·PDF 다운로드·실험·host package 설치·git commit/push 없음. 기존 연구 판단·실행 계약 유지.

## Registry 생성기 보호

기존 `build_lit_survey.py --write-registry`가 과거 발견 목록 **811편**으로 PAPER를 쓰는 문제를 실제 확인했다. Canonical manifest·논문 파일은 손상되지 않았으며 현재 1,110편으로 즉시 재생성했다. CLI가 manifest 전체를 읽도록 수정하고, `write_registry()`는 기존 stable ID가 빠지면 **쓰기 전에 중단**하도록 보강했다. 두 회귀 사례를 기존 문서 유지보수 test에 추가했다. 이후 등록된 논문이 rebuild에서 누락되는 문제를 막는다.

Flag 없는 실행은 read-only이며 PDF·노트·manifest 갱신은 각각 별도 opt-in을 유지한다. 과거 discovery 입력은 삭제하지 않고 일반 유지보수 경로에서 분리했다.

## 검증과 현행 규모

- 1,110편·5,550개 표준 노트 유지; CORE 47 / NEXT 332 / REFERENCE 489 / ARCHIVE 242. 읽기 상태·분석 입력을 승격하거나 초기화하지 않았다.
- Generator compile/rebuild·priority-only reconcile·cue catalog/resource/index/stats 동기화를 수행했다. 문서/registry 회귀 검사 **8개**, 읽기 history 검사 **6개** 통과. 전체 노트 extraction-artifact dry-run 검출은 0이다.
- Repository audit는 Markdown 5,761개·내부 링크 11,992개를 포함해 **오류 0 / 경고 0**이다. 사용자 읽기 기록 426건의 상태·분석 11개 필드, 연구 자료 345개, 기존 staged 변경과 동결 VRL source를 보존했다. 기본 CLI의 read-only 동작과 `git diff --check`도 통과했다. 전체 측정값은 원장의 `validation`에 기록했다. Keyword 기반 형식 검사는 semantic correctness나 재현성을 인증하지 않는다.
- 다음 연구 행동과 native 자원/구현 대기는 TODO를 따른다. 이번 정리는 FEEDBACK·VRL의 연구 효과 검증이나 새 학습 실행이 아니다.

<a id="candidate-priority-update"></a>

## 2026-11-07 후속 — 후보 우선순위와 registry 안내 동기화

**CANDIDATES-PRIORITY-R1.** 앞의 REG-R10 수치는 11/06 당시 결과다. N1의 2편 등록 이후 현재 **1,112편 / CORE 47·NEXT 334·REFERENCE 489·ARCHIVE 242 / 읽기 active 381·history 47**을 기준으로 점검했다.

- [현행 8개 후보](../research_topics/README.md#candidate-priority)를 기여·VLA+RL/단일 정책 적합성·식별 가능성·석사 검증 부담으로 비교했다. 정성적인 투자 판단이며 채택 확률·새 정책 결과가 아니다. 8개 개별 내용 문서에 현행 역할과 canonical 비교 링크를 넣었다.
- 기존 5개 상세 비교의 중복을 현행 표와 각 주제의 근거로 통합했다. 과거 순위는 한 문단으로 보존하고 11/05 비교·16개 과거 후보에는 현행 안내만 추가했다. NO-GO/HOLD/RETIRED 및 연구 재개 gate는 바꾸지 않았다.
- TODO의 대기 행을 현행 투자 순서로 정렬하되 **선택된 다음 행동은 UNIFIED-P0 하나**다. 각 실행 상한·contract 행은 보존했다. Root/research/synthesis/work 안내와 AGENTS의 비교 소유권 링크를 동기화했다.
- PAPER 생성기의 낡은 “RL optional” scope를 현재 VLA+RL 탐색과 기존 폭넓은 범위의 구분으로 수정하고 후보 index/TODO 링크를 넣었다. Canonical manifest 전체에서 PAPER와 resource/index/stats를 재생성했다. 후보 순위만으로 논문 tier나 사용자 읽기 상태를 바꾸지 않았다.
- 웹 검토는 11/06–07에 직접 선행의 공식 페이지·저자 abstract를 재확인한 범위다. 접근 실패·추가 후보·공식 채택 미확인 경계는 위 비교표에 기록했다. 신규 paper 등록·PDF/weight 다운로드·패키지 설치·실험·commit/push는 없다. 기존 source JSON·실행 코드·raw 결과를 보존한다.

- 생성기 compile, 읽기 계획·PAPER·registry view 재생성과 `git diff --check`를 통과했다. Repository audit는 **1,112편·표준 노트 5,560개·Markdown 5,773개·내부 링크 12,081개, 오류 0 / 경고 0**이다.
- 시작 시점과 비교해 읽기 기록 **428건**, 주제별 재현 자료·JSON **83개**, canonical paper manifest·동결 VRL 원장·기존 staged 변경을 보존했다. 이번 작업의 파일 추가·삭제는 없으며 중복 비교 내용은 기존 문서 안에서 통합했다. 문서·registry 검증이며 native 정책 실행이나 연구 효과 검증은 아니다.
