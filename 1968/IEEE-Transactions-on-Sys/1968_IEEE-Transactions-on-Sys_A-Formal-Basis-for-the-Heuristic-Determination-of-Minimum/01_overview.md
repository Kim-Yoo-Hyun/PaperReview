# A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, graph search, A*
- Official paper: https://doi.org/10.1109/TSSC.1968.300136
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof details and experimental claims remain UNVERIFIED.

## Why This Paper Is Here

A*의 admissible heuristic search를 정의한 고전으로, task/motion planning과 symbolic replanning의 탐색 기반을 이해하기 위해 등록한다.

## Problem

비용 그래프에서 목표까지의 잔여 비용을 추정하는 heuristic을 이용해 최소비용 경로를 효율적으로 찾는 문제를 다룬다.

## Core Idea

누적 비용과 추정 잔여 비용을 결합해 후보 노드를 우선 확장하며, heuristic 조건 아래 최적 경로 탐색 성질을 분석한다.

## Interface

명시적 graph state와 transition cost를 받아 discrete plan을 출력하는 task/planning 계층이다.

## Evaluation Scope

이론적 성질과 search-efficiency 분석이 중심이며 modern robot benchmark 평가는 없다.
