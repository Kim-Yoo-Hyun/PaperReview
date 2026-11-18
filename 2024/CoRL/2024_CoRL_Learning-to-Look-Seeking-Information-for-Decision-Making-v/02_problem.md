# Learning to Look: Seeking Information for Decision Making via Policy Factorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

조작에 필요한 숨은 정보를 얻는 행동과 그 정보를 이용하는 행동을 함께 학습해야 한다.

## Bottleneck and Changed Formulation

정보 탐색과 조작 정책을 분리하고 조작 정책에서 탐색 reward를 구성하는 DISaM을 제안한다.

## System and Robotics Loop

관측·context에서 정보 수집 또는 조작으로 전환한다. 두 정책 분해를 단일 VLA 공동 학습으로 부르지 않는다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Context privilege·KL 대상 분포·학습 reward·전환 threshold.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 초록은 simulation·실세계의 정보 탐색이 필요한 조작 과제 5개를 평가한다고 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/dass25a.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/learning2look/) · [공식 code](https://github.com/UT-Austin-RobIn/l2l). Exact objective, constraints, success definition은 본문 수동 확인 필요.
