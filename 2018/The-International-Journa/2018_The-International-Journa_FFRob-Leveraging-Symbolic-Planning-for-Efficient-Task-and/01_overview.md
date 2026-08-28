# FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / The International Journal of Robotics Research
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; probabilistic-completeness details remain UNVERIFIED.

## Why This Paper Is Here

symbolic planning heuristic을 이용해 continuous samples와 motion feasibility 탐색을 효율화한 TAMP 대표 baseline이다.

## Problem

large hybrid task-motion search space에서 geometric sample과 symbolic action을 효율적으로 조합한다.

## Core Idea

factored representation, conditional samplers와 symbolic planning heuristic을 결합해 solution search를 안내한다.

## Interface

task facts, sampled poses/grasps와 motion planner를 executable manipulation plan으로 연결한다.

## Evaluation Scope

다양한 manipulation planning problem의 runtime/coverage 비교가 보고되며 상세 protocol은 정독이 필요하다.
