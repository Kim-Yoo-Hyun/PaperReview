# When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Zixuan Liu, Joris Köster, Zizhan Zheng, Siavash Khajavi
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, retrieval, in-context-learning, evaluation
- Official paper: https://arxiv.org/abs/2610.05492
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: §2–3, Appendix D–E. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

검색 representation의 품질이 downstream robot success에 어떻게 연결되는지 조사한다.

같은 RICL 계열 정책에서 image, image+state, VLA feature, random retrieval을 비교한다.

## Scope and Limitation

원 RICL과 보간 규칙이 다르다. Retrieval score가 좋다는 이유만으로 정책 성능을 추정할 수 없다. Main venue는 미확인; 본문 workshop 표기는 main acceptance 근거가 아니다.

## Why This Paper Is Here — Researcher Interpretation

RETRIEVAL의 가장 직접적인 진단 선행으로, 단순 cross-task interference 발견만으로 기여를 주장하지 않게 한다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.
