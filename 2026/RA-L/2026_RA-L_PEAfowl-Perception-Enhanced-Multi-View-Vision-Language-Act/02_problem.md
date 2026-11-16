# PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

양팔 조작에서 다중 시점 간 기하 정합과 언어 의미의 결합이 필요하다.

## Bottleneck and Changed Formulation

깊이 분포 기반 3D lifting·cross-view 이웃 집계·text-aware readout을 사용하고 학습 시 depth distillation을 적용한다.

## System and Robotics Loop

다중 시점 영상·지시 → 3D-aware VLA 표현 → 양팔 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

학습 depth 정답 비용, 추론 depth 필요 여부, unseen camera/object 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboTwin2.0과 실제 양팔 조작을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11661761/) · [저자 project/code](https://peafowlvla.github.io/) · [공식 code](https://github.com/Qingyu-Fan/PEAfowl). Exact objective, constraints, success definition은 본문 수동 확인 필요.
