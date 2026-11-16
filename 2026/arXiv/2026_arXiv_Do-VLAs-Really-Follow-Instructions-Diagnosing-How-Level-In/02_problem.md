# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

어떤 작업을 할지뿐 아니라 어떻게 수행할지를 지정하는 언어 조건의 준수는 일반 task success만으로 평가하기 어렵다.

## Bottleneck and Changed Formulation

How-level 지시의 효과를 진단하고 segment-level 지시 보강을 비교하며, 지시에만 주어진 조건을 성공 정의에 포함하는 SIMPLER-IN을 제안한다.

## System and Robotics Loop

영상·행동 맥락과 수행 방식 지시 → VLA 행동 → 목표 달성 및 지시 조건 준수 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

SIMPLER-IN 조건별 성공 정의와 중립 문장 대조, 지시 보강 학습의 정보·데이터 통제, OOD 범위, 평가 코드와 checkpoint 일치.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.21251) · [저자 project/code](https://github.com/sangwu99/how-level-vla-Arxiv). Exact objective, constraints, success definition은 본문 수동 확인 필요.
