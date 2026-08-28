# Method — Planning Optimal Grasps

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / ICRA
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Grasp Planning, manipulation, contact
- Official paper: https://doi.org/10.1109/ROBOT.1992.219918
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; optimization formulation details remain UNVERIFIED.

## Pipeline

grasp wrench/quality criterion을 이용해 candidate grasp를 평가하고 최적 contact 구성을 탐색한다.

## Interface

object geometry와 friction/contact model을 grasp/contact plan으로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
