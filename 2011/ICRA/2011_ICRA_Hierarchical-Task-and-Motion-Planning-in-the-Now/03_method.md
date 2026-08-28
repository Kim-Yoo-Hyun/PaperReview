# Method — Hierarchical Task and Motion Planning in the Now

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://doi.org/10.1109/ICRA.2011.5980391
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; algorithmic details remain UNVERIFIED.

## Pipeline

현재 필요한 action을 중심으로 task planning과 motion planning을 interleave하는 hierarchical approach를 제안한다.

## Interface

symbolic state/goals와 robot geometry를 executable motion/action sequence로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
