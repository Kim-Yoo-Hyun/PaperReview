# DRILL: Training World Models to Improve Policies, Not Predict Pixels

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / NeurIPS
- Authors: Zhaolu Kang, Tailong Luo, Lei Wei, Guangyuan Dong, Sihan Liu, Yingjie He, Siheng Wang, Shuaibo Li, Rongchao Zhang, Zhen Tian, Richeng Xuan, Zhichao Hu
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: VLA, world-model, RL, policy-utility
- Official paper: https://arxiv.org/abs/2610.30814
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: §3, §5.5, §6 limitations. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DRILL은 세계 모델에서 얻은 가상 경험이 VLA를 얼마나 개선하는지에 맞춰 세계 모델 자체의 학습 목표를 조정한다. [PDF 1쪽](https://arxiv.org/pdf/2610.30814v1#page=1)

## Core Idea and Contribution

- 정책의 방문 빈도·상대 어드밴티지·모델의 확신도로 예측 오차에 가중치를 주는 방식과 가상 GRPO 갱신을 통해 정책 수익률을 미분하는 방식을 비교한다. [PDF 4쪽](https://arxiv.org/pdf/2610.30814v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.30814v1#page=5)
- 다섯 조작 시뮬레이터와 두 VLA에서 예측 정확도 중심의 세계 모델 및 모델 기반 기준선과 비교해 이후 정책 학습의 효과를 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2610.30814v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2610.30814v1#page=7)

## Scope and Limitation

VWI와 IMG의 관계는 가정에 의존한다. Pixel 품질과 control utility 차이 자체는 이 논문이 이미 직접 다룬다. 실제 로봇 검증으로 확대하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

World-model utility라는 broad gap의 직접 충돌을 registry에 남겨 같은 제안을 반복하지 않도록 한다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.
