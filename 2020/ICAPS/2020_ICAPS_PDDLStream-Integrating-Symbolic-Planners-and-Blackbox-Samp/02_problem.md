# Problem — PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / ICAPS
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, task and motion planning, symbolic planning, sampling, manipulation planning
- Official paper: https://ojs.aaai.org/index.php/ICAPS/article/view/6739
- Official PDF: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593
- Code/Project: https://github.com/caelan/pddlstream
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Symbolic action sequence와 continuous kinematic, collision, visibility, pose constraint를 한 planning problem에서 결합해야 한다.

## Core Assumptions

- Continuous constraint를 만족하는 값을 생성하는 black-box sampler를 제공할 수 있다.
- Symbolic abstraction과 stream predicate가 실제 robot state를 충분히 표현한다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `PRM/RRT + symbolic planning → PDDLStream → SayCan / SayPlan / MomaGraph` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

Predicate와 sampler를 사람이 설계해야 하며 perception error와 stale world state에 취약하다.
