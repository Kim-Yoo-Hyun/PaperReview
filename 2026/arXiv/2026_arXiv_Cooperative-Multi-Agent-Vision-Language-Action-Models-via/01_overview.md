# Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / arXiv
- Authors: Ruixiao Xu, WONG Lik Hang Kenny, Zhiqian Liu, Jianing Guo, Hanxiao Li, Kejian Shi, Shuning Zhang, Pu Feng, Yongjia Ma, Yuqing Ma, Kai Chen, Qi Dou, Yaodong Yang, Xianglong Liu, Simin Li
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, multi-agent-RL, cooperative-manipulation, latent-action
- Official paper: https://arxiv.org/abs/2609.36588
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: https://anonymous.4open.science/r/mavla_rft-2BC0/
- Code: https://anonymous.4open.science/r/mavla_rft-2BC0/
- Source audit: 2026-11-05: §4.2–4.3, §5, Appendix C.1. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 협동 VLA가 반복해서 실패하는 초기 조건에서 시연을 수집하고 각 로봇의 행동을 구분해 강화학습으로 정책을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2609.36588v1#page=1)

## Core Idea and Contribution

- 오프라인 자료에서 각 에이전트의 양의 어드밴티지를 이용하고 이후 고정 VLA의 잠재 잡음 선택을 강화학습으로 갱신한다. [PDF 4쪽](https://arxiv.org/pdf/2609.36588v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.36588v1#page=5)
- 협동 시뮬레이션 과제와 두 대의 실제 Franka를 이용해 시연만으로 학습한 정책 및 다른 강화학습 방식과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2609.36588v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.36588v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2609.36588v1#page=8)

## Scope and Limitation

CHORUS의 local-only 입력과 같지 않다. 읽은 평가에서 독립 학습 partner 교체의 순수 효과는 분리되지 않는다. Anonymous code 링크는 논문에 있으나 실행·내용 확인은 미완료.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY에서 VLA+MARL 결합 자체의 신규성을 배제하는 가장 가까운 RL 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.

## 공개 자료

- 코드 — 시뮬레이션의 다중 로봇 잠재 잡음 강화학습 · dsrl_pi0/examples/train_sim_ma.py [배포 파일](https://anonymous.4open.science/api/repo/mavla_rft-2BC0/file/dsrl_pi0/examples/train_sim_ma.py)

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://arxiv.org/pdf/2609.36588v1#page=1)
