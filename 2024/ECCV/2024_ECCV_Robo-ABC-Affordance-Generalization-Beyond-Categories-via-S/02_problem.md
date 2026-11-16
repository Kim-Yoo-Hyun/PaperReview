# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 물체 category에서 조작 contact point를 얻기 어렵다.

## Bottleneck and Changed Formulation

Human video의 affordance memory에서 유사 물체를 찾고 semantic correspondence로 contact point를 옮긴다.

## System and Robotics Loop

새 물체 영상·contact memory → affordance/contact point → robot manipulation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

2D/3D lifting, grasp 실행기, source별 수치 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

시각 affordance 추정과 실세계 cross-category grasping을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC). Exact objective, constraints, success definition은 본문 수동 확인 필요.
