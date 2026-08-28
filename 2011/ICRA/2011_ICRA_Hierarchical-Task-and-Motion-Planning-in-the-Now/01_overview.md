# Hierarchical Task and Motion Planning in the Now

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://doi.org/10.1109/ICRA.2011.5980391
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; algorithmic details remain UNVERIFIED.

## Why This Paper Is Here

symbolic task choice와 geometric motion feasibility를 계층적으로 연결한 초기 TAMP 대표작이다.

## Problem

긴 symbolic plan 전체를 미리 확정하면 geometric infeasibility와 실행 중 변화에 취약한 문제를 다룬다.

## Core Idea

현재 필요한 action을 중심으로 task planning과 motion planning을 interleave하는 hierarchical approach를 제안한다.

## Interface

symbolic state/goals와 robot geometry를 executable motion/action sequence로 연결한다.

## Evaluation Scope

robot manipulation planning 사례가 보고되며 benchmark·runtime 세부는 정독 후 기록한다.
