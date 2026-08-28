# Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2003 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, ZMP, Control
- Official paper: https://doi.org/10.1109/ROBOT.2003.1241826
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller gains and experiments remain UNVERIFIED.

## Why This Paper Is Here

ZMP preview control 기반 humanoid walking의 대표 foundation으로, 학습 기반 locomotion과 model-based gait control을 비교하는 기준점이다.

## Problem

미리 주어진 ZMP reference를 안정적으로 추종하면서 biped center-of-mass trajectory를 생성한다.

## Core Idea

future reference를 preview하는 linear control law로 cart-table model의 CoM motion을 계산한다.

## Interface

desired footsteps/ZMP trajectory를 CoM 및 walking pattern으로 변환하는 locomotion planning-control 계층이다.

## Evaluation Scope

biped walking simulation/robot demonstration의 범위와 수치는 원문에서 확인해야 한다.
