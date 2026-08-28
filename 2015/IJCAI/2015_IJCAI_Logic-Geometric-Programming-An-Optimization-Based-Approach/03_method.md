# Method — Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / IJCAI
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, optimization
- Official paper: https://www.ijcai.org/Proceedings/15/Papers/274.pdf
- Code/Project: not identified
- Source audit: official proceedings paper and abstract checked; detailed constraints and experiments remain UNVERIFIED.

## Pipeline

logic-defined mode sequence를 nonlinear trajectory optimization과 결합해 feasible task-motion solution을 탐색한다.

## Interface

symbolic goals, kinematics/contact constraints를 robot trajectory와 action sequence로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
