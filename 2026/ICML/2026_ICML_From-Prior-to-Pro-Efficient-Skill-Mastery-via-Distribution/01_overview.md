# From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / ICML
- Authors: Zhanyi Sun, Shuran Song
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: residual-RL, action-chunking, selective-regularization, value-selection
- Aliases: DICE-RL
- Official paper: https://proceedings.mlr.press/v306/sun26al.html
- Venue verification: https://proceedings.mlr.press/v306/sun26al.html
- Code/Project: https://zhanyisun.github.io/dice.rl.2026/
- Code: https://github.com/zhanyisun/dice-rl
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

사전학습 행동 prior를 유지하면서 online RL로 skill을 개선하는 과정의 비효율과 불안정을 줄인다.

## Core Idea and Contribution

Prior를 동결하고 chunk residual을 학습한다. 선택적 regularization과 value 기반 선택을 사용하며 공개 구현에서 Q/Monte-Carlo filtering을 확인했다.

## Observation–State–Action Interface

관측 → 동결 prior chunk·residual chunk → value 선택/실행. 학습 regularization과 inference 선택의 역할을 분리한다.

## Evaluation Scope and Limitations

시각 입력의 simulation·실제 로봇 조작을 보고한다. 공개 Robomimic/flow 구현은 OpenVLA/LIBERO adapter가 아니며 그 호환성을 검증하지 않았다.

ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다.

근거: [지정 본문](https://arxiv.org/html/2603.10263v2) — v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths. Code 검토 revision: `98d936e52523878f0172e606ea32403176497100`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다.
