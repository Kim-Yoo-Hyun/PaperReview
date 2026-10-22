# NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Language instruction을 따라 unseen environment를 이동할 때 scene generalization과 sim-to-real gap을 줄이는 문제다.

## Bottleneck and Changed Formulation

Monocular RGB video history를 VLM context로 처리하여 다음 navigation action을 출력한다.

## System and Robotics Loop

Language instruction + 누적 RGB video → next-step navigation action; map·odometry·depth 입력 없이 동작하는 formulation을 제안한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Camera-only 가정, action discretization, history truncation, 실제 low-level controller.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RSS abstract는 continuous navigation simulation과 실제 환경의 cross-dataset/sim-to-real 평가를 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p079.html) · [저자 project/code](https://pku-epic.github.io/NaVid/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
