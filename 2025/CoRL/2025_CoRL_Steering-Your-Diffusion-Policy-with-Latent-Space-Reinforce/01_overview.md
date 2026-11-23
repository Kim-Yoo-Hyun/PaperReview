# Steering Your Diffusion Policy with Latent Space Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Andrew Wagenmaker, Yunchu Zhang, Mitsuhiko Nakamoto, Seohong Park, Waleed Yagoub, Anusha Nagabandi, Abhishek Gupta, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: latent-noise, frozen-policy, real-robot-RL
- Aliases: DSRL
- Official paper: https://proceedings.mlr.press/v305/wagenmaker25a.html
- Venue verification: https://proceedings.mlr.press/v305/wagenmaker25a.html
- Code/Project: https://github.com/ajwagen/dsrl
- Code: https://github.com/ajwagen/dsrl
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

DSRL은 시연으로 배운 확산 정책의 파라미터를 고정하고 입력 노이즈를 고르는 정책을 강화학습해 행동을 조정한다. [PDF 1쪽](https://arxiv.org/pdf/2506.15799v2#page=1)

## Core Idea and Contribution

- 기존 확산 정책을 블랙박스로 호출하면서 그 잠재 노이즈를 새 강화학습 문제의 행동으로 다룬다. [PDF 4쪽](https://arxiv.org/pdf/2506.15799v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2506.15799v2#page=5)
- 시뮬레이션과 실물 단일 작업 및 사전학습한 범용 정책의 적응을 평가해 온라인 상호작용으로 얻는 개선을 측정했다. [PDF 1쪽](https://arxiv.org/pdf/2506.15799v2#page=1) · [PDF 8쪽](https://arxiv.org/pdf/2506.15799v2#page=8)

## Observation–State–Action Interface

Observation → RL latent-noise policy → frozen BC diffusion policy → robot action.

## Evaluation Scope and Claim Boundary

공식 CoRL abstract는 simulated benchmark, real-world robot task 및 pretrained generalist policy adaptation 평가를 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/wagenmaker25a.html) · [저자 project/code](https://github.com/ajwagen/dsrl). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Base policy weight를 고정하고 latent noise를 RL로 조정한다. ConRFT의 fine-tuning, RLDG의 distillation과 구분되는 adaptation baseline이며 generalist policy와 실제 robot 평가가 있다.

## Verification Boundary

Latent exploration 범위, base policy API, 성공/실패 reward와 reset 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
