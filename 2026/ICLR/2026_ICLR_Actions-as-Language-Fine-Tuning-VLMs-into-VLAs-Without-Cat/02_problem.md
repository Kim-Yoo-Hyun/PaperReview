# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Robot action 학습 중 VLM의 일반 의미 능력 손실을 줄인다.

## Bottleneck and Changed Formulation

자연어로 low-level action을 표현하고 parameter-efficient adaptation을 사용한다.

## System and Robotics Loop

영상·언어 → 언어형 action 표현 → robot 명령.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

action decoding, LoRA 범위, VQA/robot split과 robot controller.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Robot manipulation과 VQA 능력 보존을 함께 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
