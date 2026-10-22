# RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Embodied instruction 실행 중 여러 수준의 계획 실패를 수정한다.

## Bottleneck and Changed Formulation

고수준 계획 감사와 탐색·저수준 보정을 연결한다.

## System and Robotics Loop

지시·환경 관측 → subgoal/map 판단 → 행동 보정.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

ALFRED predicate, oracle map 접근, action executor, VLA와의 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ALFRED instruction following 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
