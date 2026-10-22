# Steering Your Diffusion Policy with Latent Space Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: latent-noise, frozen-policy, real-robot-RL
- Aliases: DSRL
- Official paper: https://proceedings.mlr.press/v305/wagenmaker25a.html
- Venue verification: https://proceedings.mlr.press/v305/wagenmaker25a.html
- Code/Project: https://github.com/ajwagen/dsrl
- Code: https://github.com/ajwagen/dsrl
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

좋은 demonstration policy가 새로운 환경에서 충분한 성능을 내지 못할 때 추가 demonstration 없이 적응시키는 문제다.

## Core Idea and Contribution

Base diffusion policy의 weight를 고정하고 latent-noise space에서 RL을 수행하는 DSRL을 제안한다.

## Observation–State–Action Interface

Observation → RL latent-noise policy → frozen BC diffusion policy → robot action.

## Evaluation Scope and Claim Boundary

공식 CoRL abstract는 simulated benchmark, real-world robot task 및 pretrained generalist policy adaptation 평가를 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/wagenmaker25a.html) · [저자 project/code](https://github.com/ajwagen/dsrl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Base policy weight를 고정하고 latent noise를 RL로 조정한다. ConRFT의 fine-tuning, RLDG의 distillation과 구분되는 adaptation baseline이며 generalist policy와 실제 robot 평가가 있다.

## Verification Boundary

Latent exploration 범위, base policy API, 성공/실패 reward와 reset 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
