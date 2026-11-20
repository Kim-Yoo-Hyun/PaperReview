# GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: differentiable-RL, drone-navigation, Gaussian Splatting, VLA
- Aliases: GRaD-Nav++, GRAD-NAV++, GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics
- Official paper: https://arxiv.org/abs/2506.14009
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3643290
- Code/Project: https://qianzhong-chen.github.io/gradnavpp.github.io/
- Code: https://github.com/Qianzhong-Chen/grad_nav
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RA-L 11(2), 1418–1425, February 2026; first online 2025-12-11. Canonical year follows journal issue, not online year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

언어 목표를 드론의 시각 기반 저수준 제어로 연결하면서 효율적으로 학습해야 한다.

## Core Idea and Contribution

Gaussian radiance field와 differentiable dynamics를 이용한 학습에 VLM·mixture-of-experts를 결합한다.

## Observation–State–Action Interface

시각·언어 → VLA navigation/control; rendering과 dynamics gradient를 학습에 활용한다.

## Evaluation Scope and Claim Boundary

Simulation과 실제 드론의 언어 조건부 navigation을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11297793/) · [저자 project/code](https://qianzhong-chen.github.io/gradnavpp.github.io/) · [공식 code](https://github.com/Qianzhong-Chen/grad_nav). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

언어·시각·행동과 differentiable RL을 결합한 직접 항법 선행이다. 기존 GRaD-Nav의 언어 조건부 확장이라 별도 등록한다.

## Verification Boundary

언어 encoder·MoE 갱신 범위, dynamics model 오차, 이전 GRaD-Nav 대비 새 평가 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
