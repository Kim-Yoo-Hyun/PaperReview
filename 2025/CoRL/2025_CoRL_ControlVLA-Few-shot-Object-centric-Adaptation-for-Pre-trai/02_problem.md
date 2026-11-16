# ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

소수 시연으로 generalist VLA를 특정 물체·과제에 적응시키기 어렵다.

## Bottleneck and Changed Formulation

Zero-initialized projection을 가진 ControlNet 형태로 object-centric 조건을 주입한다.

## System and Robotics Loop

장면·객체 중심 표현 → 사전학습 VLA → 조작 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

객체 mask 감독 비용, base model 학습 데이터, 표준·장기 task 구분.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 조작과 새 객체·배경 및 long-horizon 확장을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/li25c.html) · [저자 project/code](https://controlvla.github.io/) · [공식 code](https://github.com/ControlVLA/ControlVLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
