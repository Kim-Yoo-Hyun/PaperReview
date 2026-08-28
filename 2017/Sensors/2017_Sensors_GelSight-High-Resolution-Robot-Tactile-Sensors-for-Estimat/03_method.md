# Method — GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2017 / Sensors
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, Force, contact, manipulation
- Official paper: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/
- Code/Project: not identified
- Source audit: institutional publication page and abstract checked; calibration and result details remain UNVERIFIED.

## Pipeline

탄성 표면의 변형을 내부 camera/illumination으로 영상화하고 geometry 및 force로 해석한다.

## Interface

contact-induced tactile image를 local surface shape와 interaction-force estimate로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
