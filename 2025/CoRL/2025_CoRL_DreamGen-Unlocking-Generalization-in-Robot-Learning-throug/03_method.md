# Method — DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Video Generation, robot data, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Code/Project: https://research.nvidia.com/labs/gear/dreamgen/
- Source audit: official NVIDIA publication/project pages checked; generation and policy result details remain UNVERIFIED.

## Pipeline

video generative world model을 robot-domain data에 adaptation하고 generated trajectories/observations를 policy learning에 사용한다.

## Interface

task/context와 visual trajectory generation을 robot policy training data 및 actions로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
