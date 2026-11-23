# Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / arXiv
- Authors: Ruixiao Xu, Wong Lik Hang Kenny, Zhiqian Liu, Jianing Guo, Hanxiao Li, Kejian Shi, Shuning Zhang, Pu Feng, Yongjia Ma, Yuqing Ma, Kai Chen, Qi Dou, Yaodong Yang, Xianglong Liu, Simin Li
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, multi-agent-RL, cooperative-manipulation, latent-action
- Official paper: https://arxiv.org/abs/2609.36588
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: https://anonymous.4open.science/r/mavla_rft-2BC0/
- Code: https://anonymous.4open.science/r/mavla_rft-2BC0/
- Source audit: 2026-11-05: §4.2–4.3, §5, Appendix C.1. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

단일 로봇 사전학습 VLA에 협력 기술을 부여하고 시연 이상의 성능으로 개선한다.

실패 초기조건 중심 데이터 수집, agent별 positive-advantage filtering, 동결 VLA의 latent-noise RL을 순차 적용한다.

## Scope and Limitation

CHORUS의 local-only 입력과 같지 않다. 읽은 평가에서 독립 학습 partner 교체의 순수 효과는 분리되지 않는다. Anonymous code 링크는 논문에 있으나 실행·내용 확인은 미완료.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY에서 VLA+MARL 결합 자체의 신규성을 배제하는 가장 가까운 RL 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.
