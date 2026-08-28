# Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / IJCAI
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, optimization
- Official paper: https://www.ijcai.org/Proceedings/15/Papers/274.pdf
- Code/Project: not identified
- Source audit: official proceedings paper and abstract checked; detailed constraints and experiments remain UNVERIFIED.

## Why This Paper Is Here

symbolic logic sequence와 continuous trajectory optimization을 하나의 TAMP 구조로 연결하는 대표 foundation이다.

## Problem

discrete action skeleton과 continuous geometric feasibility를 공동으로 결정해야 하는 manipulation planning을 다룬다.

## Core Idea

logic-defined mode sequence를 nonlinear trajectory optimization과 결합해 feasible task-motion solution을 탐색한다.

## Interface

symbolic goals, kinematics/contact constraints를 robot trajectory와 action sequence로 변환한다.

## Evaluation Scope

multi-step manipulation planning 사례가 보고되며 runtime·success protocol은 정독 후 확정한다.
