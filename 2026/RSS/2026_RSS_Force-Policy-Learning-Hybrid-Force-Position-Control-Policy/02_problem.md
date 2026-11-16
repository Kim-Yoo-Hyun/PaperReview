# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

전역 시각 행동 결정과 접촉 안정화에는 서로 다른 피드백과 시간척도가 필요하다.

## Bottleneck and Changed Formulation

시연에서 interaction frame을 복원해 전역 시각 정책과 국소 hybrid force-position 제어를 구성한다.

## System and Robotics Loop

vision으로 접근하고 접촉 시 힘 피드백·interaction frame으로 제어한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

frame label 생성과 수동 조정, 접촉 전환 조건, 정책·controller 주기.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 contact-rich 조작과 새로운 형상·물성 객체를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p128.html) · [저자 project/code](https://force-policy.github.io/) · [공식 code](https://github.com/force-policy/ForcePolicy). Exact objective, constraints, success definition은 본문 수동 확인 필요.
