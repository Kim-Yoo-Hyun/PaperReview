# What Matters in Learning from Large-Scale Datasets for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

다양한 robot demonstration을 늘릴 때 어떤 다양성을 수집하고 어떤 데이터를 조회해야 하는지 불명확하다.

## Bottleneck and Changed Formulation

통제 가능한 데이터 생성으로 카메라·물체·배치 다양성과 retrieval 정렬을 비교한다.

## System and Robotics Loop

시연 집합과 target 조건 → 데이터 구성/선택 → manipulation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

camera와 task 분할, retrieval의 target 접근, 동일 학습 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

시뮬레이션 구성 실험과 DROID를 이용한 실로봇 학습을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
