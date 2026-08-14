# Method

- Year/Venue: 2025 / RSS
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, loco-manipulation, human demonstrations
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss21/p122.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.
- In this work, we introduce a cross-embodiment imitation learning system for quadrupedal manipulation, leveraging data collected from both humans and LocoMan, a quadruped equipped with multiple manipulation modes.
- Specifically, we develop a teleoperation and data collection pipeline, which unifies and modularizes the observation and action spaces of the human and the robot.

## 원리적 동기
- Prior works have explored various strategies for collecting in-domain robot data, primarily focusing on robot arms , humanoid robots , and quadrupeds equipped with top-mounted arms .
- —Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant challenge.
- To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.

## 핵심 방법론
- Scooping Pouring Unimanual ID OOD SR TS SR TS Bimanual ID OOD SR TS SR TS Unimanual ID OOD SR TS SR TS Shoe Rack Organization Bimanual ID ...
