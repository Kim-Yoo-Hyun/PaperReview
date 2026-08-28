# Method — FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / The International Journal of Robotics Research
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; probabilistic-completeness details remain UNVERIFIED.

## Pipeline

factored representation, conditional samplers와 symbolic planning heuristic을 결합해 solution search를 안내한다.

## Interface

task facts, sampled poses/grasps와 motion planner를 executable manipulation plan으로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
