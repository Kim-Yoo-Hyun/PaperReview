# Problem — Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Target Problem

각 로봇이 자기 관측·계산만으로 공동 조작을 수행하는 문제.

## Robotics Loop

로봇별 sensor stream → ego/consensus latent → diffusion action; 선택적으로 consensus를 교환한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: 중앙 학습으로 합의된 latent와 독립 팀 간 latent 호환성을 구별한다.

개념 연결: Diffusion Policy → LatentToM → CHORUS 및 multi-agent VLA RFT.

## Boundary

정확한 formulation·loss·필요 가정은 본문 확인 전 확정하지 않는다.

근거: [확인한 원문](https://proceedings.mlr.press/v305/he25a.html), 공식 proceedings abstract.
