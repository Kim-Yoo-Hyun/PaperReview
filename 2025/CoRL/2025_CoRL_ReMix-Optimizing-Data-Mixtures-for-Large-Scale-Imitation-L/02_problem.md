# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

서로 다른 로봇 데이터 domain을 어떤 비율로 섞어야 할지 불명확하다.

## Bottleneck and Changed Formulation

DRO 기반 domain 가중치 학습에 action 정규화·이산화와 early stopping을 적용한다.

## System and Robotics Loop

이질적 demonstration domain → mixture weights → downstream imitation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

domain 정의, proxy/target 접근, normalization, selection 계산 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Bridge·Open X-Embodiment 기반 데이터 혼합과 후속 정책 성능을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/hejna25a.html) · [저자 project/code](https://github.com/jhejna/remix). Exact objective, constraints, success definition은 본문 수동 확인 필요.
