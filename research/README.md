# Research — 읽기와 아이디어 검증

- Updated: 2026-11-18 KST

이 디렉토리는 논문 읽기와 연구 판단의 운영 기준을 관리한다. 최신 [REG-R18](../work/update/REGISTRY_MAINTENANCE_2026-11-18.md#reg-r18)에서 geometry 추정과 VLA의 직접 선행3편을 추가했다. 연구 후보의 현재 상태는 [통합 index](../work/research_topics/README.md), 실제 다음 행동은 [TODO](../TODO.md), 내용·실행 준비·근거는 주제별 두 폴더가 소유한다. 이 안내에는 완료 이력을 반복하지 않는다.

| 필요한 작업 | 문서 | 수정 주체 |
|---|---|---|
| 유지·예비 및 추가 탐색 주제의 가능성·재현 방법 | [주제별 통합 index](../work/research_topics/README.md) | 현행 투자 판단·폐기 사유는 index, 개별 근거는 주제 README, 다음 행동은 TODO; paper tier와 별개 |
| 논문 찾기·전체 범위 확인 | [전체 registry](../PAPER.md), [필터 index](./REGISTRY_INDEX.csv), [통계](./REGISTRY_STATS.md) | Manifest에서 생성 |
| 무엇을 어떤 순서로 읽을지 | [READING_PLAN](./READING_PLAN.md), [전체 tier](./READING_TIERS.csv) | `build_reading_tiers.py`의 group/rationale 수정 후 생성 |
| 실제 읽은 내용 기록 | [상태 규칙](./READING_STATUS.md), [active tracker](./READING_STATUS.csv), [inactive history](./READING_STATUS_HISTORY.csv) | 사용자 상태·분석 보존; 자동 필드만 생성 |
| 논문 사이의 차이·미해결 질문 | [7개 synthesis와 교차 질문 분류](../synthesis/README.md) | Source에 연결한 수동 합성; queue만 자동 생성 |
| 공백 탐색·아이디어 가치 검토 | [단계 0 + 8단계 buildup guide](./IDEA_BUILDUP_GUIDE.md), [현재 질문과 비교 근거](../synthesis/README.md) | 분야의 열린 문제와 새 논문의 기여를 분리; 알려진 답 → 조건부 질문·대안·최소 검증 |
| 후보별 결과·GPU 후속·한계 | [16개 주제 요약](../work/research_candidates/summaries/README.md) | 상세 dossier/측정 결과를 요약 |
| 지금 할 일·실험 재개 | [TODO](../TODO.md), [실험/재개 index](../work/experiments/README.md) | 연구 gate·자원 gate·실제 artifact를 별도 확인 |

## 현재 근거의 해석

현재 규모·tier·읽기 진행 집계는 생성된 [REGISTRY_STATS](./REGISTRY_STATS.md), 최신 등록·교정·정리는 [11/18 유지보수](../work/update/REGISTRY_MAINTENANCE_2026-11-18.md#reg-r18)를 따른다. 논문 노트의 source evidence와 사용자 reading status는 별개다.

유지 3개·예비 1개 주제의 기여 판단과 준비·실행 수준은 [주제 index](../work/research_topics/README.md)에 통합한다. 비실험 설계, Docker 제어 검사, 실제 정책 실행과 연구 효과는 서로 다른 증거다. 날짜별 과거 준비 묶음을 현재 실행 가능한 주제 수로 세지 않는다.

[비실험 절차](./IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)는 탐색 진입 기준을 낮추고 결과 주장의 증거 기준을 유지한다. [11/04 기존 6개 감사](../work/research_topics/README.md#nonexperimental-process-audit)는 당시 범위로 보존하며 FEEDBACK의 단계별 상태는 자체 내용 문서를 따른다. 실제 독립 연구자 피드백은 아직 수신하지 않았다.

과거 NO-GO/HOLD와 재개 조건은 [16개 주제 요약](../work/research_candidates/summaries/README.md), 후보 투자 순위는 주제 index, 선택한 다음 행동은 [TODO](../TODO.md)가 관리한다. `projects/`의 RETIRED 문서나 GPU 확보를 자동 재개 승인으로 해석하지 않는다.
