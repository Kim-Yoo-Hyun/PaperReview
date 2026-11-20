# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue
- Authors: Xiu Yuan, Tongzhou Mu, Stone Tao, Yunhao Fang, Zhang Zhang, Hao Su
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: residual-RL, imitation-learning, controlled-exploration, manipulation
- Aliases: Policy Decorator
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html
- Code/Project: https://policydecorator.github.io/
- Code: https://github.com/tongzhoumu/policy_decorator
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 final paper §4.1–4.3, selected Appendix B.5; project/code README를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

Offline imitation 정책의 조작 오차를 online RL로 보완하면서 초반 탐색으로 기존 행동을 훼손하는 문제를 줄인다.

## Core Idea and Contribution

동결 base 위에 SAC residual을 학습하고 residual 범위와 탐색 진행을 제어한다.

## Observation–State–Action Interface

Base 행동 + 제한된 residual → 환경. Base 모델 계열별 적용 가능성과 학습된 residual weights의 전이는 서로 다른 주장이다.

## Evaluation Scope and Limitations

ManiSkill·Adroit의 8개 task, Behavior Transformer·Diffusion Policy에 적용한다. 보고된 성능 향상은 해당 설정이며 같은 residual의 base 교체 전이를 뜻하지 않는다.

Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.

## Why This Paper Is Here — Researcher Interpretation

Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다.
