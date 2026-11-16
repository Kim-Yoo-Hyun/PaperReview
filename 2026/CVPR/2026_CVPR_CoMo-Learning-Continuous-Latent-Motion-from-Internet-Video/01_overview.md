# CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: latent-motion, human-video, representation-learning, robot-data
- Aliases: CoMo
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html
- Code/Project: https://github.com/MCG-NJU/CoMo
- Code: https://github.com/MCG-NJU/CoMo
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Discrete latent motion은 세밀한 연속 동작과 로봇 행동의 대응을 잃을 수 있다.

## Core Idea and Contribution

시간 차분과 temporal contrastive 학습으로 연속 motion latent를 얻는다.

## Observation–State–Action Interface

인터넷 영상 → motion pseudo-label → robot policy 공동 학습.

## Evaluation Scope and Claim Boundary

Diffusion·autoregressive 정책의 simulation·실제 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html) · [저자 project/code](https://github.com/MCG-NJU/CoMo). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

행동 공간의 통합이 discrete/continuous 선택 자체의 효과인지 분리할 비교다.

## Verification Boundary

정적 배경 shortcut, reverse-video negative의 유효성, action-label 없이 가능한 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
