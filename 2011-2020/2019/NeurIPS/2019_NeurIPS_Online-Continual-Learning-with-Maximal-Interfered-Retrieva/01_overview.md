# Online Continual Learning with Maximal Interfered Retrieval

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2019 / NeurIPS
- Authors: Rahaf Aljundi, Lucas Caccia, Eugene Belilovsky, Massimo Caccia, Min Lin, Laurent Charlin, Tinne Tuytelaars
- NeurIPS 게재 PDF 표제면의 일곱 저자를 인쇄 순서대로 반영했다. 학회 웹 서지는 Lucas Page-Caccia를 일곱 번째로, 게재 PDF는 Lucas Caccia를 두 번째로 표기한다. [게재 PDF](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=1) · [학회 서지](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html)
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: continual-learning, replay, retrieval
- Aliases: MIR, Online Continual Learning with Maximally Interfered Retrieval
- 게재 PDF에는 “Online Continual Learning with Maximally Interfered Retrieval”라는 제목이 실렸다. [표제면](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=1) · [학회 서지](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html)
- Official paper: https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html
- Full-text retrieval: https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf
- Venue verification: https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html
- Code/Project: https://github.com/optimass/Maximally_Interfered_Retrieval
- Code: https://github.com/optimass/Maximally_Interfered_Retrieval
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

MIR은 새 자료로 다음 학습 갱신을 수행했을 때 손실이 크게 늘 것으로 예상되는 과거 예를 골라 온라인 연속학습에서 다시 사용한다. [PDF 1쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=1)

## Core Idea and Contribution

- 가상 매개변수 갱신 전후의 예측 손실 변화를 이용해 저장 메모리와 생성 재생에서 간섭이 큰 표본을 찾는다. [PDF 3쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=5)
- 단일 통과 분류 설정에서 무작위 재생 등과 정확도 및 망각을 비교하고 표본 선택 구성의 효과를 측정했다. [PDF 7쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=9)

## Observation–State–Action Interface

현재 minibatch·stored memory → virtual update → 간섭 score.

## Evaluation Scope and Claim Boundary

Continual learning benchmark에서 경험/생성 replay 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) · [저자 project/code](https://github.com/optimass/Maximally_Interfered_Retrieval). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

현재 미니배치로 가상 파라미터 갱신을 한 뒤 손실이 가장 증가할 과거 예시를 골라 재생한다. 검증 대상은 연속 분류 및 생성 재생 과제의 데이터다. [원문 3쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=3) · [원문 6쪽](https://proceedings.neurips.cc/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

E1에서 loss/gradient interference를 신규 원리로 재주장하지 않게 하는 foundation이다.

## Verification Boundary

virtual step, candidate memory budget, classification과 robot rollout의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
