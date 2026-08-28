# Problem — DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / ICML Spotlight
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, human video, generalist policy, NVIDIA
- Official paper: https://arxiv.org/abs/2602.06949
- Code/Project: https://research.nvidia.com/labs/gear/
- Source audit: arXiv abstract and official NVIDIA GEAR publication listing checked; full method/results remain UNVERIFIED.

## Target Problem and Assumptions

robot interaction data 부족을 human video의 broad physical experience로 보완하면서 robot-controllable dynamics를 학습한다.

## Closed-Loop Position

visual context와 action/task conditioning을 future robot-centric video/state prediction으로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
