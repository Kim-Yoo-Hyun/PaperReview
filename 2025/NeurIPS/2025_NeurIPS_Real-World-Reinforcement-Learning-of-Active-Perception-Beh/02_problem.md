# Real-World Reinforcement Learning of Active Perception Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

부분 관측 때문에 범용 robot policy가 필요한 정보 수집 행동을 하지 못한다.

## Bottleneck and Changed Formulation

훈련 때만 사용하는 추가 센서로 privileged value를 학습하고 advantage-weighted regression으로 정책을 개선한다.

## System and Robotics Loop

훈련 critic의 privileged 정보와 배포 actor의 제한된 관측을 구분하는 AAWR이다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

추가 센서 접근·초기 demonstrations·advantage 추정·배포 observation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 초록은 3개 로봇·8개 조작 과제 및 generalist 초기 정책의 능동 관측 개선을 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) · [저자 project/code](https://penn-pal-lab.github.io/aawr/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
