# DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, dexterous manipulation, sim-to-real, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality
- Code/Project: not identified
- Source audit: official NVIDIA publication page and abstract checked; training and robot trial details remain UNVERIFIED.

## Why This Paper Is Here

GPU simulation, domain randomization과 real-time perception을 결합한 agile in-hand sim-to-real의 대표 NVIDIA paper다.

## Problem

고차원 dexterous hand policy를 simulation에서 학습해 실제 object reorientation에 robust하게 transfer한다.

## Core Idea

massively parallel RL, domain randomization, vision-based object pose tracking과 deployable control stack을 결합한다.

## Interface

camera/proprioception과 target orientation을 multi-finger joint commands로 매핑한다.

## Evaluation Scope

real Shadow Hand의 cube reorientation/robustness가 중심이며 exact trials와 perturbations는 정독 후 기록한다.
