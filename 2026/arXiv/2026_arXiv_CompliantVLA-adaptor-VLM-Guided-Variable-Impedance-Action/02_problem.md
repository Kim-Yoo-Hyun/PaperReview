# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

위치 명령 중심 VLA가 접촉 force와 순응성을 충분히 조절하지 못한다.

## Bottleneck and Changed Formulation

VLM이 task context에 따른 impedance를 정하고 실시간 force/torque feedback으로 조절한다.

## System and Robotics Loop

VLA가 목표 동작을 내고, VLM이 영상·지시·힘을 바탕으로 강성을 제안한다. 제어기는 측정 힘으로 강성을 조절하고 적용 감쇠를 계산한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Prompt와 controller 설정 비용, force threshold, release 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 접촉 과제에서 성공률·force violation을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2601.15541) · [저자 project/code](https://sites.google.com/view/compliantvla). Exact objective, constraints, success definition은 본문 수동 확인 필요.
