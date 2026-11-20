# Diffusion Policy Policy Optimization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Allen Z. Ren, Justin Lidard, Lars L. Ankile, Anthony Simeonov, Pulkit Agrawal, Anirudha Majumdar, Benjamin Burchfiel, Hongkai Dai, Max Simchowitz
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Diffusion, policy-gradient, sim-to-real
- Aliases: DPPO
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html
- Code/Project: https://diffusion-ppo.github.io/
- Code: https://github.com/irom-lab/dppo
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

BC로 학습한 diffusion action policy를 sparse reward 환경에서 안정적으로 RL fine-tuning하는 문제다.

## Core Idea and Contribution

Denoising 과정을 policy-gradient 최적화에 포함하고 diffusion policy에 맞춘 학습 설계를 제안한다.

## Observation–State–Action Interface

Observation-conditioned diffusion policy → 연속 action sequence; denoising step과 환경 실행 step은 구분해야 한다.

## Evaluation Scope and Claim Boundary

Continuous-control/robotic simulation, pixel/state 입력 및 Furniture-Bench sim-to-real assembly 평가를 project에서 확인했다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) · [저자 project/code](https://diffusion-ppo.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.

## Verification Boundary

정확한 likelihood 구성, denoising horizon, 실행 chunk와 sim-to-real reset 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
