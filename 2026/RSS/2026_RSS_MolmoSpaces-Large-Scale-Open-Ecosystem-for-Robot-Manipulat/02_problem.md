# MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실험실의 제한된 장면으로 generalist 정책의 생활환경 변이를 측정하기 어렵다.

## Bottleneck and Changed Formulation

다양한 실내 환경·상호작용 객체·grasp 자산과 통합 benchmark를 제공한다.

## System and Robotics Loop

장면·객체·로봇 설정 → simulator 기반 조작·항법 과제.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

asset license, 실제 지원 simulator별 기능, 장면 split, 정책별 co-training 여부.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

조작·항법을 포함한 8개 benchmark task와 sim-to-real 상관을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p091.html) · [저자 project/code](https://github.com/allenai/molmospaces). Exact objective, constraints, success definition은 본문 수동 확인 필요.
