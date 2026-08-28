# A Method for Registration of 3-D Shapes

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- Category: 3D Geometry, Registration, and Equivariance
- Tags: Robotics, 3D Registration, ICP, state estimation
- Official paper: https://doi.org/10.1109/34.121791
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence and experiment details remain UNVERIFIED.

## Why This Paper Is Here

ICP 계열 registration의 출발점으로, robot localization·mapping·object pose estimation의 고전적 geometry baseline이다.

## Problem

초기 정렬이 주어진 두 3D shape representation 사이의 rigid transform을 반복적으로 추정한다.

## Core Idea

closest-point correspondence와 rigid transform fitting을 번갈아 수행해 registration error를 줄인다.

## Interface

3D point/shape observations를 rigid pose transform으로 변환하는 perception/state-estimation 모듈이다.

## Evaluation Scope

다양한 3D shape representation의 registration 예제가 보고되며 modern learned baseline은 없다.
