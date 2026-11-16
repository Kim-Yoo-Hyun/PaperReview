# ClevrSkills: Compositional Language And Visual Reasoning in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

익힌 기본 조작 기술을 새로운 복합 지시로 조합할 수 있는지 평가한다.

## Bottleneck and Changed Formulation

ManiSkill2 기반 환경과 demonstration dataset, 단계별 조합 과제로 언어·시각 지시 이행을 비교한다.

## System and Robotics Loop

언어·시각 task prompt와 로봇 관측 → 조작 정책 → simulator predicate 평가. Dataset annotation과 정책에 허용되는 입력을 구분해야 한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

task 생성의 정답 정보와 자동 입력, 부분집합 허용 범위, release/contact predicate, 조합 split의 학습 support.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

기초 조작에서 복합 과제로 이어지는 세 수준의 curriculum에서 VLM 기반 baseline을 평가한다. 이 등록에서는 정확한 trial 수·성공률을 새로 확정하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [저자 project/code](https://github.com/Qualcomm-AI-research/ClevrSkills). Exact objective, constraints, success definition은 본문 수동 확인 필요.
