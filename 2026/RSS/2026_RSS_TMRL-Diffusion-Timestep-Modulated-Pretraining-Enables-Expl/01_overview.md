# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: exploration, Diffusion, policy-finetuning, VLA
- Aliases: TMRL
- Official paper: https://roboticsproceedings.org/rss22/p208.html
- Venue verification: https://roboticsproceedings.org/rss22/p208.html
- Code/Project: https://weirdlabuw.github.io/tmrl/
- Code: https://github.com/matthewh6/tmrl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

BC prior의 좁은 행동 범위가 후속 RL 탐색을 제한한다.

## Core Idea and Contribution

입력에 diffusion noise를 넣어 사전학습하고 RL이 조건화 noise 수준을 선택한다.

## Observation–State–Action Interface

관측·noise 수준 → 사전학습 정책의 행동; RL이 timestep을 조절.

## Evaluation Scope and Claim Boundary

항법·조작 평가를 보고하며 project는 실제 VLA 후학습도 설명한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p208.html) · [저자 project/code](https://weirdlabuw.github.io/tmrl/) · [공식 code](https://github.com/matthewh6/tmrl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA 내부 학습을 제안할 때 비교해야 할 사전학습 coverage·탐색 조절 대안이다.

## Verification Boundary

pretraining 추가 비용, high-level action 주기, baseline 탐색 분산, 로봇별 학습 시간을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
