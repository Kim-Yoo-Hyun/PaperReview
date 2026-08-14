# PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / ICAPS
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, task and motion planning, symbolic planning, sampling, manipulation planning
- Official paper: https://ojs.aaai.org/index.php/ICAPS/article/view/6739
- Official PDF: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593
- Code/Project: https://github.com/caelan/pddlstream
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

PRM/RRT/trajectory optimization과 language-level task planning 사이의 canonical TAMP bridge.

## Problem

Symbolic action sequence와 continuous kinematic, collision, visibility, pose constraint를 한 planning problem에서 결합해야 한다.

## Core Idea

- PDDL에 declarative black-box sampling procedure인 stream을 추가한다.
- PDDLStream 문제를 finite PDDL 문제의 sequence로 환원한다.
- Optimistic adaptive planning으로 candidate plan 탐색과 parameter binding exploitation을 조절한다.

## Observation / State / Action Interface

Symbolic facts·actions와 continuous sampler를 입력으로 받아 task-level action skeleton과 motion-feasible parameter binding을 출력한다.

## Evaluation Scope

- 공식 ICAPS 페이지는 3개 simulated robotics domain과 여러 real-world robot task 평가를 보고한다.
- Planning success, cost, sample/solver calls와 wall-clock time을 함께 확인해야 한다.

## Limitations to Verify

- Predicate와 sampler를 사람이 설계해야 하며 perception error와 stale world state에 취약하다.
- LLM/VLA와 결합할 때 language plan의 uncertainty를 symbolic feasibility로 전달하는 interface가 필요하다.

## Reading Lineage

`PRM/RRT + symbolic planning → PDDLStream → SayCan / SayPlan / MomaGraph`
