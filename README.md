# PaperReview

로봇의 관측, 상태 추정, 계획, 제어, 접촉과 복구를 연결해 논문을 정리한다. 조작·이동·로봇 학습을 중심에 두고, VLA와 3D 인식은 실제 로봇 행동에 미치는 영향으로 비교한다.

## 탐색

| 목적 | 문서 |
|---|---|
| 논문 검색 | [분야별 논문 목록](./PAPER.md) · [제목·태그·별칭 색인](./research/REGISTRY_INDEX.csv) |
| 정독 순서와 진행 | [읽기 계획](./research/READING_PLAN.md) · [읽기 기록](./research/READING_STATUS.csv) · [노트 검토 기준](./research/READING_STATUS.md#note-checks) |
| 분야별 비교 | [분야별 합성](./synthesis/README.md) · [로보틱스 연구 동향](./work/update/ROBOTICS_TRENDS.md) |
| 연구 질문과 다음 검증 | [연구 설계](./research/RESEARCH_GUIDE.md) · [연구 후보](./work/research_topics/README.md) · [다음 작업](./TODO.md) |
| 실험 재현 | [Docker 재현](./work/experiments/README.md) |
| 출처와 등록 품질 | [오류율·원문 감사](./research/SOURCE_AUDIT.md) · [누락 심사](./research/GAPFILL.md) · [등록·분류 기준](./work/update/REGISTRY.md) · [운영 규칙](./AGENTS.md) |

## 현황

| 전체 | CORE | NEXT | REFERENCE | ARCHIVE |
|---:|---:|---:|---:|---:|
| 1,252 | 50 | 450 | 510 | 242 |

2026-11-25 기준 전체 1,252편의 요약·핵심 기여를 원문과 대조했다. 감사 10개 항목을 모두 통과한 논문은 92편이다. 집중 읽기 500편 중 423편(84.6%)에 방법·기체·모달리티·데이터 출처·공개 범위가 기록돼 있다. [감사 결과와 미확인 범위](./research/SOURCE_AUDIT.md) · [분류 배치](./work/update/REGISTRY.md#taxonomy-batches) · [전체 통계](./research/REGISTRY_STATS.md)

각 논문의 `01_overview.md`에서 출처와 확인 수준을 먼저 확인한다. 나머지 네 노트에 문제, 방법, 평가, 후속 연구에 관한 해석이 있다. 연구 후보의 문헌 근거는 `내용/README.md`, 재현 명령과 실제 실행 범위는 `재현 방법/README.md`에 모았다.
