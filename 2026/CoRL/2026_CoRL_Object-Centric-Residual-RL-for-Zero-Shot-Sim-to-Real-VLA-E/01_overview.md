# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / CoRL
- Authors: Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo, Yasuyuki Matsushita
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, residual-RL, object-centric, sim-to-real
- Aliases: Object-Centric Residual RL
- Official paper: https://arxiv.org/abs/2606.18953
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://www.microsoft.com/en-us/research/articles/object-centric-residual-rl/
- Code: not identified
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §3.1–3.4/5.1–5.4/7, Appendix A를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. CoRL 공식 accepted list에서 exact title/forum을 확인했다. 읽은 것은 arXiv v1이며 final paper 동등성과 공식 학습 code 공개는 미확인이다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

시뮬레이션에서 학습한 residual로 실제 VLA 조작을 개선할 때 시각·행동 도메인 차이를 줄이는 문제다.

## Core Idea and Contribution

Object pose·proprioception·base action을 residual 입력으로 사용하며, paired teleoperation을 통한 정렬과 simulation 학습을 결합한다.

## Observation–State–Action Interface

VLA의 base action과 물체 중심 상태 → 보정 행동 → 실제 조작. 학습에 사용하는 상태와 실제 배포에서 추정하는 상태를 구분해야 한다.

## Evaluation Scope and Limitations

Simulation-to-real residual 전이와 base SFT를 다룬다. 여기서 동일 residual의 sim-to-real 사용은 확인했지만 서로 다른 backbone/갱신된 base 간 동일 weights 재사용은 확정하지 않았다.

CoRL 공식 accepted list에서 exact title/forum을 확인했다. 읽은 것은 arXiv v1이며 final paper 동등성과 공식 학습 code 공개는 미확인이다.

근거: [지정 본문](https://arxiv.org/html/2606.18953v1) — §3.1–3.4/5.1–5.4/7, Appendix A.

## Why This Paper Is Here — Researcher Interpretation

Object-centric residual의 전이를 이미 다룬 직접 충돌 선행이다. 다양한 로봇·base 갱신 전이와 sim-to-real 전이를 구분할 NEXT다.
