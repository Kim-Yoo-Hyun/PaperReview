# Research — 읽기와 아이디어 검증

- Updated: 2026-11-16 KST

이 디렉토리는 논문 읽기와 연구 판단의 운영 기준을 관리한다. 현재 새 탐색은 **VLA + RL 중심의 manipulation·navigation**이며 기존 VLA 단독 후보와 행동을 지원하는 3D 범위도 보존한다. 연구 후보의 실행 자산·원시 근거는 `work/`에 둔다.

| 필요한 작업 | 문서 | 수정 주체 |
|---|---|---|
| 현재 11개 주제의 가능성·재현 방법 | [주제별 통합 index](../work/research_topics/README.md) | 기존 8개 순위·HINDSIGHT/과제 배분/접촉 적응 후보 판정은 index, 개별 근거는 주제 README, 다음 행동은 TODO; paper tier와 별개 |
| 논문 찾기·전체 범위 확인 | [전체 registry](../PAPER.md), [필터 index](./REGISTRY_INDEX.csv), [통계](./REGISTRY_STATS.md) | Manifest에서 생성 |
| 무엇을 어떤 순서로 읽을지 | [READING_PLAN](./READING_PLAN.md), [전체 tier](./READING_TIERS.csv) | `build_reading_tiers.py`의 group/rationale 수정 후 생성 |
| 실제 읽은 내용 기록 | [상태 규칙](./READING_STATUS.md), [active tracker](./READING_STATUS.csv), [inactive history](./READING_STATUS_HISTORY.csv) | 사용자 상태·분석 보존; 자동 필드만 생성 |
| 논문 사이의 차이·미해결 질문 | [7개 synthesis와 교차 질문 분류](../synthesis/README.md) | Source에 연결한 수동 합성; queue만 자동 생성 |
| 공백 탐색·아이디어 가치 검토 | [단계 0 + 8단계 buildup guide](./IDEA_BUILDUP_GUIDE.md), [현재 질문과 비교 근거](../synthesis/README.md) | 분야의 열린 문제와 새 논문의 기여를 분리; 알려진 답 → 조건부 질문·대안·최소 검증 |
| 후보별 결과·GPU 후속·한계 | [16개 주제 요약](../work/research_candidates/summaries/README.md) | 상세 dossier/측정 결과를 요약 |
| 지금 할 일·실험 재개 | [TODO](../TODO.md), [실험/재개 index](../work/experiments/README.md) | 연구 gate·자원 gate·실제 artifact를 별도 확인 |

## 현재 근거의 해석

현재 규모·tier·읽기 진행 집계는 생성된 [REGISTRY_STATS](./REGISTRY_STATS.md), 최신 등록·교정은 [11/16 Ψ₀ 보완](../work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)을 따른다. Ψ₀와 인간/휴머노이드 데이터 전제를 기존 기반→VLA RL 비교에 연결했다. 논문 노트의 source evidence와 사용자 reading status는 별개다.

현재 11개 주제의 기여 판단과 준비·실행 수준은 [주제 index](../work/research_topics/README.md)에 통합한다. 비실험 설계, Docker 제어 검사, 실제 정책 실행과 연구 효과는 서로 다른 증거다. 날짜별 과거 준비 묶음을 현재 실행 가능한 주제 수로 세지 않는다.

[비실험 절차](./IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)는 탐색 진입 기준을 낮추고 결과 주장의 증거 기준을 유지한다. [11/04 기존 6개 감사](../work/research_topics/README.md#nonexperimental-process-audit)는 당시 범위로 보존하며 FEEDBACK의 단계별 상태는 자체 내용 문서를 따른다. 실제 독립 연구자 피드백은 아직 수신하지 않았다.

과거 NO-GO/HOLD와 재개 조건은 [16개 주제 요약](../work/research_candidates/summaries/README.md), 후보 투자 순위는 주제 index, 선택한 다음 행동은 [TODO](../TODO.md)가 관리한다. `projects/`의 RETIRED 문서나 GPU 확보를 자동 재개 승인으로 해석하지 않는다.
