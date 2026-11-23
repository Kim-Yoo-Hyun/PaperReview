# RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.

- Year/Venue: 2026 / ICML
- Authors: Sanghwan Jang, Minjin Jeon, Minsoo Kim, Seong Jin Choi, Dongha Kim, Hwanjo Yu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, retrieval, test-time-adaptation, imitation-learning
- Official paper: https://proceedings.mlr.press/v306/jang26c.html
- Venue verification: https://proceedings.mlr.press/v306/jang26c.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: 공식 proceedings abstract; arXiv identity. abstract 기반 — 본문 수동 확인 필요. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RA-VLA는 새로운 조작 지시를 받을 때 비슷한 장면의 시연 중 행동에도 관련 있는 예시를 찾아 VLA의 실행을 유도한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=1)

## Core Idea and Contribution

- 행동 정보를 반영하는 검색기를 훈련하고 검색한 시연의 동작 단서에 조건부로 행동을 생성하는 방식을 구성했다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=4)
- LIBERO와 실제 UR5e에서 새로운 작업 적응을 평가하고 검색한 문맥을 바꿨을 때 행동이 얼마나 달라지는지 조사했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=7)

## Scope and Limitation

검색기와 행동 생성 방식에는 사전 학습이 필요하다. 저자는 표 4에서 시연 버퍼 크기와 검색 개수를 바꿔 성공률을 비교했다. [표 4](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/jang26c/jang26c.pdf#page=8)

## Why This Paper Is Here — Researcher Interpretation

RETRIEVAL 후보의 semantic retrieval·execution 결합이라는 넓은 주장이 이미 존재함을 확인하는 ICML 직접 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/jang26c.html), 공식 proceedings abstract; arXiv identity.
