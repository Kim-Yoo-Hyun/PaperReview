# Method — DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, dexterous manipulation, sim-to-real, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality
- Code/Project: not identified
- Source audit: official NVIDIA publication page and abstract checked; training and robot trial details remain UNVERIFIED.

## Pipeline

massively parallel RL, domain randomization, vision-based object pose tracking과 deployable control stack을 결합한다.

## Interface

camera/proprioception과 target orientation을 multi-finger joint commands로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
