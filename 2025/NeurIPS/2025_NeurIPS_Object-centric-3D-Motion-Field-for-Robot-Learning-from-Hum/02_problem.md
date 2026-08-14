# Problem

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Robot Learning and Data
- Tags: Robotics, learning from human videos, 3D motion field, cross-embodiment
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.
- Unlike existing 3D tracking works that assume depth as a groundtruth reference, we recover accurate 3D object motion from noisy depth. amount of footage available from internet or ...
- Due to this data collection challenge, many works look into the feasibility of using real-world actionfree videos for robot learning.

## 해결하려는 문제
- Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior ...
- In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this ...
- We introduce two novel components in its implementation.

## 선행 연구 / 배경 단서
- Data is the primary bottleneck in robot learning – collecting large-scale high quality robotic data in real world at scale for training control policies is not only expensive ...
- Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.
- Unlike existing 3D tracking works that assume depth as a groundtruth reference, we recover accurate 3D object motion from noisy depth. amount of footage available from internet or ...
