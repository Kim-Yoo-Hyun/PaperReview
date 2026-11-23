# Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz, Yu-Chiang Frank Wang, Fu-En Yang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: latent-reasoning, VLA, distillation, inference-efficiency
- Aliases: Fast-ThinkAct
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html
- Code/Project: https://jasper0314-huang.github.io/fast-thinkact/
- Code: project_only
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

명시적 긴 chain-of-thought는 행동 결정을 지연시킨다.

## Core Idea and Contribution

Teacher의 언어·시각 계획을 preference-guided distillation으로 압축하여 verbalizable latent reasoning을 학습한다.

## Observation–State–Action Interface

관측·지시 → compact latent plan → action model. 압축된 추론과 action model의 연결을 구분한다.

## Evaluation Scope and Claim Boundary

Embodied manipulation·reasoning benchmark의 latency와 장기 계획·적응·복구를 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) · [저자 project/code](https://jasper0314-huang.github.io/fast-thinkact/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL reasoning의 이득을 긴 텍스트 출력 없이 행동에 전달하는 대안으로 비교한다.

## Verification Boundary

teacher 감독 비용, action model 별도 학습 여부, end-to-end latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
