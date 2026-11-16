# ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 기술의 다양성과 실험실 간 재현 가능한 평가가 부족하다.

## Bottleneck and Changed Formulation

접촉 skill taxonomy와 제작 가능한 물체·대응 simulation asset을 제공한다.

## System and Robotics Loop

물체·task variation → 실제/시뮬레이션 접촉 과제.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

task별 success 판정, asset version, 정책용 reset/step와 scripted helper 분리.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

36개 reference task 중 6개에서 vision-only와 visual-tactile 정책을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.24512) · [저자 project/code](https://jingyi-xiang.github.io/contactbench/) · [공식 code](https://github.com/Michaelwyx/contactbench-sim). Exact objective, constraints, success definition은 본문 수동 확인 필요.
