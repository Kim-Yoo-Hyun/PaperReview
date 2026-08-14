# Insights — Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Paper-Supported Direction

OpenVLA를 새 embodiment에 적용할 때 decoding, representation과 objective 선택을 비교하는 실용 기준점.

## Researcher Interpretation

- Foundation/frontier connection: `OpenVLA → OpenVLA-OFT → efficient embodiment adaptation`
- 가장 먼저 반박할 가정: OpenVLA에서 얻은 adaptation recipe가 다른 backbone에도 전이된다.
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

- LIBERO와 특정 ALOHA task의 결과가 contact-rich 또는 mobile embodiment까지 일반화되는지 확인해야 한다.
- Throughput 외에 sensor-to-action latency와 disturbance reaction을 따로 측정해야 한다.

## Minimum Experiment

LIBERO 한 suite에서 decoder, chunk length, continuous/discrete action과 L1 objective를 단계적으로 ablation한다.

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
