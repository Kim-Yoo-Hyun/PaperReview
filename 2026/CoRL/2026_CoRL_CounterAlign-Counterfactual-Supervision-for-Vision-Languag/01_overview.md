# CounterAlign: Counterfactual Supervision for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Haru Kondoh, Kei Ota, Asako Kanezaki, Yueh-Hua Wu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, offline-RL, counterfactual, manipulation
- Aliases:
- Official paper: https://arxiv.org/abs/2608.21740
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://counteralign.airoa.io/
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다.

## Problem and Importance

CounterAlign은 성공 시연에 맞지 않는 지시를 조합해 반사실적 음성 표본을 만들고 오프라인 RL로 조작 정책을 개선한다. [PDF 3쪽](https://arxiv.org/pdf/2608.21740v1#page=3)

## Core Idea and Contribution

- 바른 지시와 잘못된 지시, 시연 행동과 정책 행동을 구별하는 신호로 이득을 추정한다. [PDF 4쪽](https://arxiv.org/pdf/2608.21740v1#page=4)
- LIBERO-PRO와 실물 TX-G2 조작에서 지시·배치 변화에 대한 일반화를 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2608.21740v1#page=7)

## Observation–State–Action Interface

관측·지시·mismatch negative → 학습 신호 → action.

## Evaluation Scope and Claim Boundary

LIBERO 계열 instruction 평가와 실제 robot 결과를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=AY4totylcx). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다.

## Verification Boundary

negative validity, reward leakage, scene overlap, constraint label 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 저자 프로젝트가 코드 공개 예정이라고 명시한다. [저자 공개 안내](https://counteralign.airoa.io/)
