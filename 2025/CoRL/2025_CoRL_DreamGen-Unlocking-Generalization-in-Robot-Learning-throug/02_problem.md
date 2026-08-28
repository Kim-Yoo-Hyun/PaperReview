# Problem — DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Video Generation, robot data, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Code/Project: https://research.nvidia.com/labs/gear/dreamgen/
- Source audit: official NVIDIA publication/project pages checked; generation and policy result details remain UNVERIFIED.

## Target Problem and Assumptions

real robot demonstration의 task·scene coverage 부족 때문에 policy가 새로운 조건에 일반화하지 못하는 문제를 다룬다.

## Closed-Loop Position

task/context와 visual trajectory generation을 robot policy training data 및 actions로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
