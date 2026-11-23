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
- Source audit: 2026-11-05: §3, §5.5, §6 limitations. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

World model의 pixel 예측 품질과 그 안에서 학습한 정책의 return이 일치하지 않는 문제.

Imagined rollout의 GRPO update 이후 return을 목표로 world model을 학습하는 bilevel 구성. VWI 가중 surrogate와 IMG meta-gradient 두 형태를 제안한다.

## Scope and Limitation

VWI와 IMG의 관계는 가정에 의존한다. Pixel 품질과 control utility 차이 자체는 이 논문이 이미 직접 다룬다. 실제 로봇 검증으로 확대하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

World-model utility라는 broad gap의 직접 충돌을 registry에 남겨 같은 제안을 반복하지 않도록 한다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.
