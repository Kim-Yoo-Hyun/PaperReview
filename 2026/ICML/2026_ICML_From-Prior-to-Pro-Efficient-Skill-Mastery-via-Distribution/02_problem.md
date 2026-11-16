# From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

사전학습 행동 prior를 유지하면서 online RL로 skill을 개선하는 과정의 비효율과 불안정을 줄인다.

## Changed Formulation

Prior를 동결하고 chunk residual을 학습한다. 선택적 regularization과 value 기반 선택을 사용하며 공개 구현에서 Q/Monte-Carlo filtering을 확인했다.

## Assumptions and Robotics Loop

Prior가 유용한 행동 support를 제공하고 critic/return 신호가 선택적 제약을 안내해야 한다.

관측 → 동결 prior chunk·residual chunk → value 선택/실행. 학습 regularization과 inference 선택의 역할을 분리한다.

근거: [지정 본문](https://arxiv.org/html/2603.10263v2) — v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths. Code 검토 revision: `98d936e52523878f0172e606ea32403176497100`; 실행하지 않았다.
