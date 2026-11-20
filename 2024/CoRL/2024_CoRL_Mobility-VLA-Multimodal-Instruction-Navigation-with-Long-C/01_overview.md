# Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Zhuo Xu, Hao-Tien Lewis Chiang, Zipeng Fu, Mithun George Jacob, Tingnan Zhang, Tsang-Wei Edward Lee, Wenhao Yu, Connor Schenck, David Rendleman, Dhruv Shah, Fei Xia, Jasmine Hsu, Jonathan Hoech, Pete Florence, Sean Kirmani, Sumeet Singh, Vikas Sindhwani, Carolina Parada, Chelsea Finn, Peng Xu, Sergey Levine, Jie Tan
- Category: Embodied Navigation and Mapping
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Navigation, Vision-Language-Action, topological-map, long-context
- Aliases: Mobility VLA, MINT
- Official paper: https://proceedings.mlr.press/v270/xu25b.html
- Venue verification: https://proceedings.mlr.press/v270/xu25b.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

언어·이미지 지시를 이전 tour 영상과 연결해 실제 장소로 이동해야 한다.

## Core Idea and Contribution

장문맥 VLM의 goal-frame 선택과 topological graph 기반 하위 navigation을 결합한다.

## Observation–State–Action Interface

tour video·multimodal instruction → goal frame → graph/low-level policy → 이동 action.

## Evaluation Scope and Claim Boundary

기록된 tour를 제공한 실환경의 multimodal instruction navigation을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/xu25b.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

NaVILA·NoMaD와 비교할 계층형 VLA navigation 및 환경 사전정보 기준이다.

## Verification Boundary

tour/graph 구축 비용, goal 후보 접근, online 관측과 planner timing을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
