# KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

지각·언어 오류와 기하·동역학 추론 실패가 통합 과제에서 섞인다.

## Bottleneck and Changed Formulation

물리 추론 난점을 분리한 절차적 환경과 skill·시연·평가 baseline을 제공한다.

## System and Robotics Loop

기하·동역학 제약 → 계획 또는 학습된 행동 → 물리적 결과.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

skill 호출 권한, 관측 특권, baseline별 compute, 절차적 split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

다양한 planning·IL·RL baseline 및 mobile manipulator 대응 실험을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p184.html) · [저자 project/code](https://prpl-group.com/kinder-site/) · [공식 code](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden). Exact objective, constraints, success definition은 본문 수동 확인 필요.
