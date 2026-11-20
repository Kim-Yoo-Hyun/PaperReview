# DEAS: DEtached value learning with Action Sequence for Scalable Offline RL

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee, Yuke Zhu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, action-chunk, value-learning, VLA
- Aliases: DEAS
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html
- Code/Project: https://changyeon.site/deas/
- Code: https://github.com/csmile-1006/DEAS-Isaac-GR00T
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Action sequence를 critic에 쓰면 장기 문제의 horizon을 줄이면서도 가치 과대추정이 커질 수 있다.

## Core Idea and Contribution

행동 sequence 기반 가치 학습에 detached value learning을 적용하여 데이터 안의 고수익 행동으로 추정을 유도한다.

## Observation–State–Action Interface

Offline observation/action sequence → value estimation → sequence policy; VLA action chunk와 연결한다.

## Evaluation Scope and Claim Boundary

OGBench, RoboCasa Kitchen과 실세계 조작의 VLA 확장을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) · [저자 project/code](https://changyeon.site/deas/) · [공식 code](https://github.com/csmile-1006/DEAS-Isaac-GR00T). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Chunk-aware actor-critic과 공유 표현 연구에서 반드시 넘어야 하는 직접 offline RL 선행이다.

## Verification Boundary

value target gradient 경계, OOD action 처리, 실로봇 데이터·환경 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
