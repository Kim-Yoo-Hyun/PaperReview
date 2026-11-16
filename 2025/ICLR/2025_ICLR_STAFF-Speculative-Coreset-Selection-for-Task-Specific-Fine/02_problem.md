# STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

큰 target model에서 coreset 점수를 직접 계산하는 비용이 크다.

## Bottleneck and Changed Formulation

동일 family의 작은 model로 점수를 추정하고 target에서 확인해 선택 예산과 coverage를 조정한다.

## System and Robotics Loop

LLM 학습 예제 → proxy score·target verification → coreset; robot action interface는 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

LLM에서 VLA로의 적용 한계, target verification 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LLM fine-tuning 평가이며 VLA의 closed-loop 성공을 검증한 논문은 아니다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
