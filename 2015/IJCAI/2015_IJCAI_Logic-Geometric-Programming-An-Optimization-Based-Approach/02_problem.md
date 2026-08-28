# Problem — Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / IJCAI
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, optimization
- Official paper: https://www.ijcai.org/Proceedings/15/Papers/274.pdf
- Code/Project: not identified
- Source audit: official proceedings paper and abstract checked; detailed constraints and experiments remain UNVERIFIED.

## Target Problem and Assumptions

discrete action skeleton과 continuous geometric feasibility를 공동으로 결정해야 하는 manipulation planning을 다룬다.

## Closed-Loop Position

symbolic goals, kinematics/contact constraints를 robot trajectory와 action sequence로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
