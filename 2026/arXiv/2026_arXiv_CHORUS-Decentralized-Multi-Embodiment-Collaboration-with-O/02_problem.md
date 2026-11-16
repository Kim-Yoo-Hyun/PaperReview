# Problem — CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

서로 다른 로봇이 공유 관측·통신 없이 함께 조작하는 문제.

## Robotics Loop

로봇별 local 관측·identity prompt → 공유 가중치의 독립 copy → 해당 로봇 action; 공유 camera나 명시적 통신 없음.

## Assumptions to Check — Researcher Interpretation

연구자 점검: task의 관련 정보가 각 로봇 관측에 실제로 보이는지 확인한다.

개념 연결: π0.5·LatentToM → shared decentralized VLA → independent partner 평가.

## Boundary

Scripted perturbation은 독립 학습한 partner와의 cross-play와 다르다. 엄격한 동시 release는 범위 밖이다. 저자는 CoRL 2026을 표기하지만 이번 공식 acceptance 확인은 미완료다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.
