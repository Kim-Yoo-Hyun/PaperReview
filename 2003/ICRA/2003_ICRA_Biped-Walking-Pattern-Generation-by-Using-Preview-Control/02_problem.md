# Problem — Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2003 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, ZMP, Control
- Official paper: https://doi.org/10.1109/ROBOT.2003.1241826
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller gains and experiments remain UNVERIFIED.

## Target Problem and Assumptions

미리 주어진 ZMP reference를 안정적으로 추종하면서 biped center-of-mass trajectory를 생성한다.

## Closed-Loop Position

desired footsteps/ZMP trajectory를 CoM 및 walking pattern으로 변환하는 locomotion planning-control 계층이다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
