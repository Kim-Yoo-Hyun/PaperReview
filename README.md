# PaperReview

로봇의 관측·제어·접촉·복구를 연결해 문헌을 비교하고, 연구 질문을 실제 정책 행동으로 검증한다. `research1`에서는 **위 칸에 그릇을 넣으라는 지시에서, 다른 서랍의 개방 폭을 언제 얼마나 오래 보여주면 로봇의 첫 접촉과 수납 위치가 바뀌는가**를 조사한다.

## 최근 실험

아래 서랍을 약 160 mm 연 채 정책 시작 후 0.5–1초에 76 mm로 보여주면, 첫 접촉이 바뀐 경우는 배치 2에서 32/32쌍, 배치 3에서 0/32쌍이었다. 두 배치에서 그릇 중심 위치만 9.4 mm 서로 바꾸고 다시 측정해도 각각 30/32쌍과 0/32쌍이었다. 달라진 두 쌍은 같은 자세·시드를 두 번 실행한 결과다. [접촉·수납과 검증 범위](./work/research_topics/instruction_revision/내용/README.md#drawer-bowl-position) · [그릇 위치 비교 그림](./work/research_topics/instruction_revision/재현%20방법/results/2026-11-26-drawer-bowl-position/drawer_bowl_position.png)

| 하려는 일 | 시작점 |
|---|---|
| 측정값을 검산하거나 같은 실험 실행 | [로컬 Docker 재현](./work/research_topics/instruction_revision/재현%20방법/README.md#drawer-bowl-position) |
| 후속 실험의 대조 조건 확인 | [다음 작업](./TODO.md) |
| 1,260편의 논문 검색 | [분야별 목록](./PAPER.md) · [태그·별칭 색인](./research/REGISTRY_INDEX.csv) |
| 정독 순서·기록·분야별 비교 | [논문 읽기](./research/README.md) · [7개 분야의 합성](./synthesis/README.md) |
| 원문 확인 범위와 등록 기준 확인 | [원문 감사](./research/SOURCE_AUDIT.md) · [등록 근거](./work/update/REGISTRY.md) · [전체 통계](./research/REGISTRY_STATS.md) |

각 논문의 첫 노트는 출처와 확인 범위를 안내한다. 읽기 등급은 CORE 50편, NEXT 454편, REFERENCE 514편, ARCHIVE 242편이다. 11월 원문 감사의 표본은 통합 전 1,252편이다. [읽기 계획](./research/READING_PLAN.md) · [연구 자료 안내](./work/README.md)
