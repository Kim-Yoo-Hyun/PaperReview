# Method — Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2003 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, ZMP, Control
- Official paper: https://doi.org/10.1109/ROBOT.2003.1241826
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller gains and experiments remain UNVERIFIED.

## Pipeline

future reference를 preview하는 linear control law로 cart-table model의 CoM motion을 계산한다.

## Interface

desired footsteps/ZMP trajectory를 CoM 및 walking pattern으로 변환하는 locomotion planning-control 계층이다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
