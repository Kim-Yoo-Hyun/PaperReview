# CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, multi-robot, cross-embodiment, decentralized-control
- Official paper: https://arxiv.org/abs/2606.12352
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://chorus-model.github.io/
- Code: project_only
- Source audit: 2026-11-05: §3.1–3.3, §4.2, §5 limitations. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

서로 다른 로봇이 공유 관측·통신 없이 함께 조작하는 문제.

하나의 π0.5를 다중 로봇 시연으로 학습하고 로봇 식별 prompt와 padded action으로 embodiment를 구분한다.

## Scope and Limitation

Scripted perturbation은 독립 학습한 partner와의 cross-play와 다르다. 엄격한 동시 release는 범위 밖이다. 저자는 CoRL 2026을 표기하지만 이번 공식 acceptance 확인은 미완료다.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY에서 여러 embodiment·local-only 협력 자체를 새 기여로 주장하지 않도록 하는 직접 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.
