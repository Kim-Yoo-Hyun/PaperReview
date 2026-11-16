# LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

기본 LIBERO 성공률만으로 VLA의 환경 변화 강건성을 판단하기 어렵다.

## Bottleneck and Changed Formulation

배치·camera·robot 초기 상태·언어·조명·배경·sensor noise를 통제한 점진 평가를 구성한다.

## System and Robotics Loop

Perturbed 환경/지시 → 기존 VLA → task success와 조건별 분석.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

난도 선정에 쓰인 model, perturbation validity, test contamination.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

다수 VLA의 simulation robustness를 비교한다. 수치·정확한 난도 split은 본문 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [저자 project/code](https://github.com/sylvestf/LIBERO-plus). Exact objective, constraints, success definition은 본문 수동 확인 필요.
