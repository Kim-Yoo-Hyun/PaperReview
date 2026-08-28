# Problem — FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / The International Journal of Robotics Research
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; probabilistic-completeness details remain UNVERIFIED.

## Target Problem and Assumptions

large hybrid task-motion search space에서 geometric sample과 symbolic action을 효율적으로 조합한다.

## Closed-Loop Position

task facts, sampled poses/grasps와 motion planner를 executable manipulation plan으로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
