# Problem — Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Pretrained VLA를 새 robot에 fine-tune할 때 가능한 action decoder와 objective가 많지만 speed와 success를 함께 최적화하는 기준이 부족하다.

## Core Assumptions

- OpenVLA에서 얻은 adaptation recipe가 다른 backbone에도 전이된다.
- Action chunking으로 얻는 throughput 향상이 feedback 감소보다 크다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `OpenVLA → OpenVLA-OFT → efficient embodiment adaptation` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

LIBERO와 특정 ALOHA task의 결과가 contact-rich 또는 mobile embodiment까지 일반화되는지 확인해야 한다.
