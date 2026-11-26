# PaperReview

로봇이 관측을 바탕으로 행동을 선택하고 실패에서 회복하는 과정을 다루는 논문 레지스트리다. 조작·이동·로봇 학습을 중심으로, VLA의 행동 표현과 3D 인식이 실제 제어에 주는 효과를 비교한다.

| 하고 싶은 일 | 시작할 곳 |
|---|---|
| 논문 찾기 | [분야별 목록](./PAPER.md)에서 둘러보거나 [검색 색인](./research/REGISTRY_INDEX.csv)에서 제목·별칭·태그로 찾는다. 각 행의 `overview_path`에 원문과 개요가 있다. |
| 읽을 순서 정하기 | [읽기 계획](./research/READING_PLAN.md)에서 선행 연구와 선정 이유를 확인하고 [읽기 기록](./research/READING_STATUS.csv)에 분석을 남긴다. [상태와 노트 작성법](./research/READING_STATUS.md#note-checks) |
| 논문끼리 비교하기 | [일곱 분야별 비교](./synthesis/README.md) · [VLA의 행동 공간과 접촉 제어](./research/VLA_ACTION_SPACE.md) · [OpenVLA 인용 계보](./research/OPENVLA_LINEAGE.md) |
| 연구 주제와 실험 찾기 | [로보틱스 동향](./work/update/ROBOTICS_TRENDS.md) · [연구 설계](./research/RESEARCH_GUIDE.md) · [현재 연구 후보](./work/research_topics/README.md) · [다음 작업](./TODO.md) · [Docker 재현](./work/experiments/README.md) |
| 수록 범위와 신뢰도 확인하기 | [외부 목록 대조와 누락 심사](./research/GAPFILL.md#external-coverage) · [원문 감사](./research/SOURCE_AUDIT.md) · [전체 통계](./research/REGISTRY_STATS.md) |

## 수록 현황

연도별로 찾으려면 [1960–2010년](./1960-2010/) 또는 [2011–2020년](./2011-2020/)을 연다. 2021년부터는 루트의 연도 폴더에서 발표처별로 찾을 수 있다.

2026-11-26 기준 **1,266편**이다. CORE 50편과 NEXT 450편은 모두 방법·태스크·기체·입력·데이터 출처·공개 범위를 분류했다. 원문에서 판별하기 어려운 값은 `unknown`으로 표시한다. REFERENCE 524편과 ARCHIVE 242편도 색인에서 검색할 수 있다. [분류 기준과 원문 근거](./work/update/REGISTRY.md#taxonomy-batches)

11월 전수 감사 대상 1,252편 모두 요약·기여를 원문과 대조했고 검색 태그를 검토했다. 서지·링크와 공개 자료를 포함한 10개 감사 항목을 모두 통과한 논문은 118편이다. 이후 등록한 14편의 근거는 각 논문 노트에 있다. [항목별 통과·미확인 수](./research/SOURCE_AUDIT.md) · [최근 등록](./work/update/REGISTRY.md#reg-r18)

논문을 추가할 때는 [선정·출처 기준](./research/README.md#paper-admission)과 [원장 갱신 명령](./work/README.md#registry-maintenance)을 따른다. 자동화 에이전트의 작업 지침은 [AGENTS.md](./AGENTS.md)에 있다.
