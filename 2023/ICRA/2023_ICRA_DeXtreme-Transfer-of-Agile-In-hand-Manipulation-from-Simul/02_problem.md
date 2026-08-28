# Problem — DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, dexterous manipulation, sim-to-real, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality
- Code/Project: not identified
- Source audit: official NVIDIA publication page and abstract checked; training and robot trial details remain UNVERIFIED.

## Target Problem and Assumptions

고차원 dexterous hand policy를 simulation에서 학습해 실제 object reorientation에 robust하게 transfer한다.

## Closed-Loop Position

camera/proprioception과 target orientation을 multi-finger joint commands로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
