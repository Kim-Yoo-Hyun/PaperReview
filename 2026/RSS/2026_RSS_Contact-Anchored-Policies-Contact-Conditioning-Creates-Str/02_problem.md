# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

추상 언어만으로 구체적 접촉 목표를 전달하기 어려운 문제를 다룬다.

## Bottleneck and Changed Formulation

Contact point로 조건화한 modular utility policies와 EgoGym 반복 평가를 제안한다.

## System and Robotics Loop

접촉 anchor·관측 → skill action; language-conditioned VLA 자체는 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

anchor 획득 비용, embodiment split, 실제 checkpoint release.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Pick/Open/Close와 새 환경·embodiment 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p141.html) · [저자 project/code](https://cap-policy.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
