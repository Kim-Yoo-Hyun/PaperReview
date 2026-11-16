# Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Robot 데이터에 없는 물체 종류와 동작으로 언어 조건 조작을 확장해야 한다.

## Bottleneck and Changed Formulation

고정된 생성 모델의 인간 영상을 조건으로 공통 robot policy를 실행한다.

## System and Robotics Loop

장면·언어 → 생성 인간 영상 → 영상 조건 closed-loop robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

robot-data holdout, video 사전학습 중복, motion conditioning과 실행 latency.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

새 물체 종류·동작을 포함한 실환경 manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/bharadhwaj25a.html) · [저자 project/code](https://homangab.github.io/gen2act/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
