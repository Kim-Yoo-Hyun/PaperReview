# Method — Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- Parallel decoding, action chunking, continuous action representation과 L1 objective를 결합한 OFT recipe를 제안한다.
- OpenVLA에 적용한 OpenVLA-OFT로 simulation과 real bimanual manipulation을 평가한다.

## Interface

Image·language·proprioception 입력에서 continuous action chunk를 병렬 생성한다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `OpenVLA → OpenVLA-OFT → efficient embodiment adaptation`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
