# Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world-model, exposure-bias, visual-fidelity
- Aliases: PersistWorld
- Official paper: https://arxiv.org/abs/2603.25685
- Venue verification: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- Code/Project: https://jaibardhan.com/persistworld/
- Code: https://github.com/Jai2500/PersistWorld
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ECCV 2026 accepted/video list의 공식 검색 색인과 저자 abstract 대조; proceedings page/DOI 미확인.

## Problem and Importance

Action-conditioned video world model의 autoregressive rollout에서 exposure bias 때문에 장기 prediction 품질이 저하되는 문제다.

## Core Idea and Contribution

자신이 생성한 history에 conditioning하며 여러 미래 rollout을 비교하는 RL post-training과 multi-view visual fidelity reward를 제안한다.

## Observation–State–Action Interface

Robot action + predicted video history → future multi-view video; 최적화 대상은 robot policy가 아니라 world model이다.

## Evaluation Scope and Claim Boundary

공식 abstract/project는 DROID에서 LPIPS/SSIM/PSNR 기반 rollout fidelity와 human preference 평가를 설명한다. Downstream policy improvement는 별도 검증 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.25685) · [저자 project/code](https://jaibardhan.com/persistworld/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. RL로 개선하는 대상은 world model의 autoregressive prediction이다. DROID rollout fidelity 근거를 policy success 개선으로 간주하지 않는다. Ctrl-World/WMPO 기반 learned simulator를 직접 고도화할 때 NEXT 검토.

## Verification Boundary

Reward metric의 geometry/contact 민감도, rollout horizon, 실제 robot policy evidence 유무을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
