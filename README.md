# PaperReview

로봇의 관측, 상태 추정, 계획, 제어, 접촉과 복구를 연결해 논문을 정리한다. 조작·이동·로봇 학습을 중심에 두고, VLA와 3D 인식은 실제 로봇 행동에 미치는 영향으로 비교한다.

## 탐색

| 목적 | 문서 |
|---|---|
| 논문 검색 | [논문 목록](./PAPER.md) · [필터용 색인](./research/REGISTRY_INDEX.csv) |
| 정독 순서와 진행 | [읽기 계획](./research/READING_PLAN.md) · [읽기 상태 안내](./research/READING_STATUS.md) |
| 분야별 비교 | [분야별 합성](./synthesis/README.md) · [로보틱스 연구 동향](./work/update/ROBOTICS_TRENDS.md) |
| 연구 질문과 다음 검증 | [연구 설계](./research/RESEARCH_GUIDE.md) · [연구 후보](./work/research_topics/README.md) · [다음 작업](./TODO.md) |
| 실험 재현 | [Docker 재현](./work/experiments/README.md) |
| 출처와 등록 품질 | [오류율·원문 감사](./research/SOURCE_AUDIT.md) · [누락 심사](./research/GAPFILL.md) · [등록·분류 기준](./work/update/REGISTRY.md) · [운영 규칙](./AGENTS.md) |

## 현황

| 전체 | CORE | NEXT | REFERENCE | ARCHIVE |
|---:|---:|---:|---:|---:|
| 1,252 | 50 | 450 | 510 | 242 |

2026-11-24 기준 표준 노트는 6,260개다. 전체 1,252편 중 1,054편(84.19%)의 요약·기여를 원문과 대조했다. CORE 50편, NEXT 450편, REFERENCE 510편은 대조를 마쳤다. ARCHIVE는 242편 중 44편을 확인했고 198편이 남았다. 사용자 정독 진척은 읽기 기록에서 확인할 수 있다. [원문 감사](./research/SOURCE_AUDIT.md) · [읽기 기록](./research/READING_STATUS.csv) · [레지스트리 통계](./research/REGISTRY_STATS.md)

## 사용법

1. [논문 목록](./PAPER.md)에서 제목·주제·venue를 찾고 `01_overview.md`에서 출처와 확인 수준을 확인한다.
2. `02_problem.md`부터 `05_insights.md`까지 문제, 방법, 평가, 후속 연구 해석을 확인한다. 논문 제목은 공식 표기를 사용한다.
3. [분야별 비교표](./synthesis/README.md)에서 방법과 평가 조건을 비교한다. 실제 정독을 마친 뒤 [읽기 기록](./research/READING_STATUS.csv)에 분석을 남긴다.
4. 현행 후보의 질문과 근거는 각 `내용/README.md`, 실행 조건과 명령은 `재현 방법/README.md`에서 찾는다.

[작업 폴더](./work/README.md) · [조사와 변경](./work/update/README.md)
