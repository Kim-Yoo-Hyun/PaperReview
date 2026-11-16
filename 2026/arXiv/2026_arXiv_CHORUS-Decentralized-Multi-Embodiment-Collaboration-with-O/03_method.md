# Method — CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

하나의 π0.5를 다중 로봇 시연으로 학습하고 로봇 식별 prompt와 padded action으로 embodiment를 구분한다.

## Observation, State and Action

로봇별 local 관측·identity prompt → 공유 가중치의 독립 copy → 해당 로봇 action; 공유 camera나 명시적 통신 없음.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.
