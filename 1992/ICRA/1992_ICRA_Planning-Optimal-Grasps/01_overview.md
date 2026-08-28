# Planning Optimal Grasps

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / ICRA
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Grasp Planning, manipulation, contact
- Official paper: https://doi.org/10.1109/ROBOT.1992.219918
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; optimization formulation details remain UNVERIFIED.

## Why This Paper Is Here

grasp quality와 contact placement를 최적화 문제로 보는 고전으로, analytic grasping에서 learned grasp proposal로 이어지는 배경이다.

## Problem

물체를 안정적으로 제어할 수 있는 contact configuration과 finger placement를 선택하는 문제를 다룬다.

## Core Idea

grasp wrench/quality criterion을 이용해 candidate grasp를 평가하고 최적 contact 구성을 탐색한다.

## Interface

object geometry와 friction/contact model을 grasp/contact plan으로 변환한다.

## Evaluation Scope

analytic examples 중심이며 센서 노이즈와 large-scale real-robot generalization은 범위 밖이다.
