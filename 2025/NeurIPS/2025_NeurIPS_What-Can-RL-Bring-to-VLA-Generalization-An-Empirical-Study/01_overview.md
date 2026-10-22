# What Can RL Bring to VLA Generalization? An Empirical Study

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: RL-finetuning, generalization, evaluation
- Aliases: RL4VLA
- Official paper: https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html
- Venue verification: https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html
- Code/Project: https://rlvla.github.io/
- Code: https://github.com/gen-robot/RL4VLA
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

VLA의 RL fine-tuning이 SFT 대비 어떤 종류의 generalization을 개선하는지 분리해서 측정하는 문제다.

## Core Idea and Contribution

Visual·semantic·execution 변화 축으로 평가하고 PPO와 LLM 계열 RL 방법의 차이를 분석한다.

## Observation–State–Action Interface

Image/language-conditioned VLA → action; 학습 방식과 평가 시 입력 perturbation을 분리한다.

## Evaluation Scope and Claim Boundary

공식 NeurIPS abstract는 visual, semantic, execution generalization 및 PPO/DPO/GRPO 비교를 설명한다.

근거: [공식 paper/abstract](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) · [저자 project/code](https://rlvla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.

## Verification Boundary

Generalization split 생성, pretrained overlap, RL별 budget 및 real-robot 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
