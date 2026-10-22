# Research — 읽기와 아이디어 검증

- Updated: 2026-10-23 KST

이 디렉토리는 논문 읽기와 연구 판단의 운영 기준을 관리한다. 현재 축은 **VLA 기반 manipulation·navigation, 이를 지원하는 3D**이며 RL은 선택 사항이다. 연구 후보의 실행 자산·원시 근거는 `work/`에 둔다.

| 필요한 작업 | 문서 | 수정 주체 |
|---|---|---|
| 논문 찾기·전체 범위 확인 | [전체 registry](../PAPER.md), [필터 index](./REGISTRY_INDEX.csv), [통계](./REGISTRY_STATS.md) | Manifest에서 생성 |
| 무엇을 어떤 순서로 읽을지 | [READING_PLAN](./READING_PLAN.md), [전체 tier](./READING_TIERS.csv) | `build_reading_tiers.py`의 group/rationale 수정 후 생성 |
| 실제 읽은 내용 기록 | [상태 규칙](./READING_STATUS.md), [active tracker](./READING_STATUS.csv), [inactive history](./READING_STATUS_HISTORY.csv) | 사용자 상태·분석 보존; 자동 필드만 생성 |
| 논문 사이의 차이·미해결 질문 | [7개 synthesis와 교차 질문 분류](../synthesis/README.md) | Source에 연결한 수동 합성; queue만 자동 생성 |
| 아이디어 가치 검토 | [8단계 buildup guide](./IDEA_BUILDUP_GUIDE.md) | Claim·대안·최소 검증·기각 조건 작성 |
| 후보별 결과·GPU 후속·한계 | [16개 주제 요약](../work/research_candidates/summaries/README.md) | 상세 dossier/측정 결과를 요약 |
| 지금 할 일·실험 재개 | [TODO](../TODO.md), [Docker 재개 안내](../work/experiments/portable/README.md) | 연구 gate·자원 gate·실제 artifact를 별도 확인 |

## 현재 근거의 해석

Registry 1,037편 중 CORE 47·NEXT 275편이 7개 queue에 배정돼 있다. 읽기 상태는 active 322행·history 47행으로 보존한다. 자동 노트·source 감사·metadata 통계·Docker 코드 실행을 논문 정독이나 정책 효과 입증으로 바꾸지 않는다.

후보는 다음 세 축으로 읽는다. **연구 판단**은 GO/REVISE/NO-GO/HOLD/RETIRED, **실행 준비**는 source·data·runtime·resource 자격, **증거**는 문헌/정적 감사/저장 측정/closed-loop 실험이다. GPU 확보가 연구 판단의 변경을 뜻하지 않는다. 현재 새 native 정책 실험은 모두 연구 조건을 더 갖춰야 하며, C3 저장 logits의 Docker 재분석만 독립 실행 경로를 검증했다.

`projects/`의 RP-2·RP-3는 RETIRED 역사 문서다. 활성 목록으로 옮기거나 이전 가설을 현재 결과처럼 갱신하지 않는다. 읽기 priority는 READING_PLAN 하나, 활성 작업은 TODO 하나, 후보 핵심은 주제별 요약 하나를 따른다.
