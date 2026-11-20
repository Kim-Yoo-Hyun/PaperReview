# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Senyu Fei, Siyin Wang, Li Ji, Ao Li, Shiduo Zhang, Liming Liu, Jinlong Hou, Jingjing Gong, Xianzhong Zhao, Xipeng Qiu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, online-RL, dense-reward, self-reference
- Aliases: SRPO
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

이진 성공 보상만으로는 실패 rollout의 진행 정보를 활용하기 어렵다.

## Core Idea and Contribution

같은 batch의 성공 궤적을 기준으로 world-model latent에서 실패의 진행 보상을 만든다.

## Observation–State–Action Interface

성공·실패 rollout → latent 진행 비교 → VLA 정책 갱신.

## Evaluation Scope and Claim Boundary

LIBERO와 LIBERO-Plus에서 학습 효율·견고성을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

HINDSIGHT의 실패 재사용이 이미 존재하는 self-reference reward shaping과 다른지 검토할 직접 선행이다.

## Verification Boundary

성공 없는 batch 처리, world-model 사전학습 비용, 진행 측정 오류, reward scale을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
