# When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / arXiv
- Authors: Zixuan Liu, Joris Köster, Zizhan Zheng, Siavash Khajavi
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, retrieval, in-context-learning, evaluation
- Official paper: https://arxiv.org/abs/2610.05492
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: §2–3, Appendix D–E. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 RICL 기반 VLA에 제공할 시연을 고르는 검색 방식이 지표상 검색 품질과 실제 조작 성공에 미치는 영향을 비교한다. [PDF 1쪽](https://arxiv.org/pdf/2610.05492v1#page=1)

## Core Idea and Contribution

- 영상 유사도·로봇 상태를 추가한 검색·VLA 백본 특징·무작위 검색을 같은 적응 설정에서 비교했다. [PDF 2쪽](https://arxiv.org/pdf/2610.05492v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2610.05492v1#page=3)
- 항상 우세한 검색 방식은 없었고 통상적인 검색 품질 지표와 작업 성공이 일치하지 않거나 유사한 다른 과제의 시연이 도움이 되는 사례를 보고했다. [PDF 3쪽](https://arxiv.org/pdf/2610.05492v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.05492v1#page=4)

## Scope and Limitation

원 RICL과 보간 규칙이 다르다. Retrieval score가 좋다는 이유만으로 정책 성능을 추정할 수 없다. Main venue는 미확인; 본문 workshop 표기는 main acceptance 근거가 아니다.

## Why This Paper Is Here — Researcher Interpretation

RETRIEVAL의 가장 직접적인 진단 선행으로, 단순 cross-task interference 발견만으로 기여를 주장하지 않게 한다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.
