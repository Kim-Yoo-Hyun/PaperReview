# Method

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Benchmark, Embodied AI, long-horizon tasks, simulation, household robotics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://behavior.stanford.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- : We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.
- Further details about our training and evaluation setup can be found in Appendix F.
- Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick or the desired location ...

## 원리적 동기
- The most needed activities indicated by the survey range from ‘wash floor’ to ‘clean bathtub.’ Clearly, the diversity of these activities is far beyond what real-world robotics challenges ...
- While significant progress in realism has been made in specific domains [43–45], achieving realism for a diverse set of activities remains a tremendous challenge, due to the effort ...
- : We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.

## 핵심 방법론
- Further details about our training and evaluation setup can be found in Appendix F.
- Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick or the desired location ...
