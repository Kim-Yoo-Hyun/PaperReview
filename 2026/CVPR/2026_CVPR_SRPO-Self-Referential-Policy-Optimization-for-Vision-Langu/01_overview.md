# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

SRPO는 같은 배치에서 VLA가 스스로 성공한 궤적을 기준으로 삼아 실패한 실행에도 진행도에 따른 강화학습 보상을 부여한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 사전학습 세계 모델의 잠재 표현으로 성공 궤적과 실패 궤적의 진행을 비교해 이진 성공 신호보다 세밀한 보상을 계산한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=4)
- LIBERO와 LIBERO-Plus에서 정책 성능을 측정하고 잠재 표현 기반 진행 보상 및 실패 궤적 활용의 기여를 분석했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

성공·실패 rollout → latent 진행 비교 → VLA 정책 갱신.

## Evaluation Scope and Claim Boundary

LIBERO와 LIBERO-Plus에서 학습 효율·견고성을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

HINDSIGHT의 실패 재사용이 이미 존재하는 self-reference reward shaping과 다른지 검토할 직접 선행이다.

## Verification Boundary

성공 없는 batch 처리, world-model 사전학습 비용, 진행 측정 오류, reward scale을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
