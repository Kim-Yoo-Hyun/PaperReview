# PaperReview

로봇의 관측·제어·접촉·복구를 연결해 문헌을 비교하고, 연구 질문을 실제 정책 행동으로 검증한다. `research1`의 현재 주제는 **위 칸에 그릇을 넣으라는 지시를 유지할 때, 다른 서랍을 여는 것만으로 로봇의 행동과 수납 위치가 바뀌는가**이다.

## 최근 실험

LIBERO 배치 2의 충돌을 피한 물체 배치에서 가운데 칸만 약 160 mm 열면 30/32회 가운데에, 아래 칸만 열면 32/32회 아래에 넣었다. 그런데 같은 장면에 모두 닫힌 조건의 성공 명령을 재생하면 각각 32/32회 위 칸에 넣었다. 원래 물체 위치에서 76 mm만 당긴 비교에서는 가운데에서 아래로 도착지가 함께 바뀐 쌍이 0/32였다. 두 비교 사이에는 개방 폭과 물체 위치가 함께 달라졌다. [결과·해석](./work/research_topics/instruction_revision/내용/README.md#drawer-location) · [그림](./work/research_topics/instruction_revision/재현%20방법/results/2026-11-25-drawer-location/drawer_location.png)

| 하려는 일 | 시작점 |
|---|---|
| 측정값을 검산하거나 같은 실험 실행 | [로컬 Docker 재현](./work/research_topics/instruction_revision/재현%20방법/README.md) |
| 후속 실험의 대조 조건 확인 | [다음 작업](./TODO.md) |
| 1,260편의 논문 검색 | [분야별 목록](./PAPER.md) · [태그·별칭 색인](./research/REGISTRY_INDEX.csv) |
| 정독 순서·기록·분야별 비교 | [논문 읽기](./research/README.md) · [7개 분야의 합성](./synthesis/README.md) |
| 원문 확인 범위와 등록 기준 확인 | [원문 감사](./research/SOURCE_AUDIT.md) · [등록 근거](./work/update/REGISTRY.md) · [전체 통계](./research/REGISTRY_STATS.md) |

각 논문의 첫 노트는 출처와 확인 범위를 안내한다. 읽기 등급은 CORE 50편, NEXT 454편, REFERENCE 514편, ARCHIVE 242편이다. 11월 원문 감사의 표본은 통합 전 1,252편이다. [읽기 계획](./research/READING_PLAN.md) · [연구 자료 안내](./work/README.md)
