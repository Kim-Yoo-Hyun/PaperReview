# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Simulation에서 학습한 navigation diffusion policy를 실제 환경과 다른 robot embodiment로 옮기는 문제다.

## Bottleneck and Changed Formulation

Privileged information guidance를 이용한 simulation training과 end-to-end local navigation diffusion policy를 제안한다.

## System and Robotics Loop

Local visual observation + point/image goal 또는 no-goal setting → trajectory/action proposal; privileged 정보의 train/test 경계 확인 필요.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Training oracle, depth/pose 입력, trajectory selector, robot footprint와 controller 한계.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 project는 no-goal exploration, point-goal/image-goal navigation과 cross-embodiment real-world transfer를 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2505.08712) · [저자 project/code](https://github.com/InternRobotics/NavDP). Exact objective, constraints, success definition은 본문 수동 확인 필요.
