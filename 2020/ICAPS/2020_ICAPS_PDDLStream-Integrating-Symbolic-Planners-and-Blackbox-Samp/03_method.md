# Method — PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / ICAPS
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, task and motion planning, symbolic planning, sampling, manipulation planning
- Official paper: https://ojs.aaai.org/index.php/ICAPS/article/view/6739
- Official PDF: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593
- Code/Project: https://github.com/caelan/pddlstream
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- PDDL에 declarative black-box sampling procedure인 stream을 추가한다.
- PDDLStream 문제를 finite PDDL 문제의 sequence로 환원한다.
- Optimistic adaptive planning으로 candidate plan 탐색과 parameter binding exploitation을 조절한다.

## Interface

Symbolic facts·actions와 continuous sampler를 입력으로 받아 task-level action skeleton과 motion-feasible parameter binding을 출력한다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `PRM/RRT + symbolic planning → PDDLStream → SayCan / SayPlan / MomaGraph`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
