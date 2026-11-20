# πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kang Chen, Zhihao Liu, Tonghe Zhang, Zhen Guo, Si Xu, Hao Lin, Hongzhi Zang, Xiang Li, Quanlu Zhang, Zhaofei Yu, Guoliang Fan, Tiejun Huang, Yu Wang, Chao Yu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, flow-matching, online-RL
- Aliases: πRL, piRL, pi_RL
- Official paper: https://arxiv.org/abs/2510.25889
- Venue verification: https://arxiv.org/abs/2510.25889
- Code/Project: https://github.com/RLinf/RLinf
- Code: https://github.com/RLinf/RLinf
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v3(2026-01-29) abstract 확인; 최초 공개 연도 2025 유지. πRL은 공식 수식 제목의 plain-text 표기. 기존 N2의 RLinf pin 검토와 새 registry 초록 노트의 근거 범위를 구분한다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

Flow VLA의 action log-likelihood를 직접 계산하기 어려워 RL 후학습이 까다롭다.

## Core Idea and Contribution

Flow-Noise의 학습 가능한 noise 과정과 Flow-SDE의 ODE–SDE 변환을 대안으로 제시한다.

## Observation–State–Action Interface

Flow denoising과 environment interaction의 확률적 정책 인터페이스.

## Evaluation Scope and Claim Boundary

여러 benchmark에서 ID/OOD 개선을 보고한다. 접촉 강성 학습 효과를 직접 입증한 것은 아니다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.25889) · [저자 project/code](https://github.com/RLinf/RLinf). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 π₀ Flow-SDE/PPO backend의 likelihood·탐색 정의를 이해할 직접 prerequisite다.

## Verification Boundary

Flow-Noise/Flow-SDE 구분, likelihood 집계, normalizer와 update budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
