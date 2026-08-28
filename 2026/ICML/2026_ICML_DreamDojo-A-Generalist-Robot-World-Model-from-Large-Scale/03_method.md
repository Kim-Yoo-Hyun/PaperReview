# Method — DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / ICML Spotlight
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, human video, generalist policy, NVIDIA
- Official paper: https://arxiv.org/abs/2602.06949
- Code/Project: https://research.nvidia.com/labs/gear/
- Source audit: arXiv abstract and official NVIDIA GEAR publication listing checked; full method/results remain UNVERIFIED.

## Pipeline

large-scale human video pretraining과 robot data adaptation/conditioning을 결합한 generative robot world model을 제시한다.

## Interface

visual context와 action/task conditioning을 future robot-centric video/state prediction으로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
