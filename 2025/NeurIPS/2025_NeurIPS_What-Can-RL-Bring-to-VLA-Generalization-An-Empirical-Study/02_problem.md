# What Can RL Bring to VLA Generalization? An Empirical Study

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 RL fine-tuning이 SFT 대비 어떤 종류의 generalization을 개선하는지 분리해서 측정하는 문제다.

## Bottleneck and Changed Formulation

Visual·semantic·execution 변화 축으로 평가하고 PPO와 LLM 계열 RL 방법의 차이를 분석한다.

## System and Robotics Loop

Image/language-conditioned VLA → action; 학습 방식과 평가 시 입력 perturbation을 분리한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Generalization split 생성, pretrained overlap, RL별 budget 및 real-robot 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 NeurIPS abstract는 visual, semantic, execution generalization 및 PPO/DPO/GRPO 비교를 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) · [저자 project/code](https://rlvla.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
