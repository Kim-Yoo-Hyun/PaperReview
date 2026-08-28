# Method — A Method for Registration of 3-D Shapes

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- Category: 3D Geometry, Registration, and Equivariance
- Tags: Robotics, 3D Registration, ICP, state estimation
- Official paper: https://doi.org/10.1109/34.121791
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence and experiment details remain UNVERIFIED.

## Pipeline

closest-point correspondence와 rigid transform fitting을 번갈아 수행해 registration error를 줄인다.

## Interface

3D point/shape observations를 rigid pose transform으로 변환하는 perception/state-estimation 모듈이다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
