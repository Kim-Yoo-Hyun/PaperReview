# RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, world-model, model-based-RL, termination
- Aliases: RehearseVLA
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- Code/Project: https://github.com/iSEE-Laboratory/RehearseVLA
- Code: https://github.com/iSEE-Laboratory/RehearseVLA
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

현실 reset 비용과 부족한 시연이 VLA online 후학습을 제한한다.

## Core Idea and Contribution

물리 일관성을 지향한 world simulator와 보상·종료를 판단하는 VLM reflector를 구성한다.

## Observation–State–Action Interface

행동 → 미래 영상 예측 → 보상·종료 판단 → VLA 후학습.

## Evaluation Scope and Claim Boundary

소수 시연 조건의 복잡한 로봇 조작 개선을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) · [저자 project/code](https://github.com/iSEE-Laboratory/RehearseVLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLAW 등과 함께 imagined rollout으로 실제 interaction을 대체하는 직접 비교 기준이다.

## Verification Boundary

실제/가상 rollout 분모, 물리 일관성 검증, reflector의 감독 비용, 종료 오탐을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
