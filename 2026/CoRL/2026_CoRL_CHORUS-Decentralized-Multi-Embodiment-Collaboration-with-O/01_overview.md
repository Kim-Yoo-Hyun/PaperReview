# CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / CoRL
- Authors: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, multi-robot, cross-embodiment, decentralized-control
- Official paper: https://arxiv.org/abs/2606.12352
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://chorus-model.github.io/
- Code: project_only
- Source audit: 2026-11-05: §3.1–3.3, §4.2, §5 limitations. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CHORUS는 여러 로봇이 같은 VLA의 복사본을 각자 실행하며 자신이 관측한 정보로 협동 작업을 수행하도록 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2606.12352v1#page=1)

## Core Idea and Contribution

- 로봇 식별 지시와 각 로봇의 관측을 같은 정책에 제공해 실행 중 로봇 간 통신 없이 서로의 행동에 대응하게 한다. [PDF 3쪽](https://arxiv.org/pdf/2606.12352v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2606.12352v1#page=4)
- 줄자 사용·책 전달·세탁 바구니 들어 올리기 등 실제 협업과 상대 동작 교란에서 공동 작업의 성공과 반응을 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2606.12352v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2606.12352v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2606.12352v1#page=8)

## Scope and Limitation

Scripted perturbation은 독립 학습한 partner와의 cross-play와 다르다. 엄격한 동시 release는 범위 밖이다. 저자는 CoRL 2026을 표기하지만 이번 공식 acceptance 확인은 미완료다.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY에서 여러 embodiment·local-only 협력 자체를 새 기여로 주장하지 않도록 하는 직접 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.
