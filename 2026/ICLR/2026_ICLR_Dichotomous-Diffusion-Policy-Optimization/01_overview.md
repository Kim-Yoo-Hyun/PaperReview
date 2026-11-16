# Dichotomous Diffusion Policy Optimization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: diffusion-policy, offline-RL, offline-to-online-RL
- Aliases: DIPOLE
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html
- Code/Project: https://lrmbbj.github.io/DIPOLE/
- Code: https://github.com/LRMbbj/DIPOLE
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 저자 repository의 rl-bench 하위 코드 범위는 추가 확인 필요. 전체 DIPOLE training release로 판정하지 않는다. NAVSIM의 VLA 결과는 자율주행이다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Diffusion 정책의 직접 value 최대화는 불안정하고 likelihood 근사는 비용이 크다.

## Core Idea and Contribution

보상 최대화·최소화 diffusion policy를 따로 학습하고 score의 선형 결합으로 추론 greediness를 조절한다.

## Observation–State–Action Interface

Offline transition → 두 diffusion score → 결합된 action generation.

## Evaluation Scope and Claim Boundary

ExORL·OGBench의 offline 및 offline-to-online RL과 NAVSIM 자율주행 VLA를 평가한다. 주행 VLA 결과를 조작 VLA의 근거로 확대하지 않는다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html) · [저자 project/code](https://lrmbbj.github.io/DIPOLE/) · [공식 code](https://github.com/LRMbbj/DIPOLE). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Diffusion RL 안정화의 알고리즘 대안으로 참고하며 로봇 조작 효과는 별도 검증한다.

## Verification Boundary

두 모델의 추가 계산량, 추론 결합 계수 선택, manipulation 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
