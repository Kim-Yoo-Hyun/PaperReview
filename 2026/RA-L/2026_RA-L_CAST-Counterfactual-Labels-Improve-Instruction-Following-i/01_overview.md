# CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Catherine Glossop, William Chen, Arjun Bhorkar, Dhruv Shah, Sergey Levine
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, counterfactual-data, instruction-following, Navigation, manipulation
- Aliases: CAST, Counterfactual Augmentation with Synthetic Trajectories
- Official paper: https://arxiv.org/abs/2508.13446
- Venue verification: https://api.crossref.org/works/10.1109/lra.2026.3726383
- Code/Project: https://cast-vla.github.io/
- Code: https://github.com/catglossop/CAST
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. 최초 preprint2025, 최신 v2는2026-06-08. 공식 project/저자 code 확인; 이번 확인으로 main-conference 채택을 확정하지 않는다. 사용자 reading status UNREAD 유지.

## Problem and Importance

비슷한 관측에서 행동과 지시가 다양하지 않으면 VLA가 언어를 무시하고 데이터 편향에 의존할 수 있다.

## Core Idea and Contribution

VLM 기반 counterfactual 라벨과 대응 행동 자료로 기존 robot dataset의 지시·행동 다양성을 늘려 언어 추종을 학습한다.

## Observation–State–Action Interface

기존 trajectory와 counterfactual instruction/action 자료 → VLA 학습 → navigation 또는 manipulation 행동. 실제 수행된 실패의 hindsight 라벨과 합성 counterfactual을 구분한다.

## Evaluation Scope and Claim Boundary

v2 abstract는 실내외 3개 navigation 환경과 distractor가 있는 manipulation의 instruction following을 평가한다고 보고한다. 정확한 trial·split·수치는 본문 확인 필요다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2508.13446) · [저자 project/code](https://cast-vla.github.io/) · [공식 code](https://github.com/catglossop/CAST). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

목표 의미를 바꾸는 학습 자료의 직접 대조. 사실인 실패 라벨 선택과 실행되지 않은 counterfactual augmentation의 차이를 명확히 하는 데 필요하다.

## Verification Boundary

합성 행동의 물리적 유효성, 원 데이터/평가 중복, language와 action 증강 기여 분리, 공개 모델/자료의 논문 version 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
