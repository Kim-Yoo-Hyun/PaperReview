# OGBench: Benchmarking Offline Goal-Conditioned RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Offline goal-conditioned RL 알고리즘의 stitching·long-horizon·pixel input 성능을 체계적으로 비교할 benchmark가 부족하다.

## Bottleneck and Changed Formulation

다양한 goal-conditioned environment/dataset와 reference algorithm 구현을 제공하여 능력별 차이를 드러낸다.

## System and Robotics Loop

Offline transition data + goal → policy/action; unlabeled data에서의 goal-conditioned 학습을 평가한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Goal sampling, reward relabeling, split/dataset 품질과 성공률 aggregation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ICLR abstract는 8종 환경, 85 datasets 및 6 reference algorithm을 보고한다. Task/split별 정확한 성공 정의는 본문 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/ogbench). Exact objective, constraints, success definition은 본문 수동 확인 필요.
