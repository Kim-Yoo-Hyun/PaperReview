# Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

OpenVLA를 새 embodiment에 적용할 때 decoding, representation과 objective 선택을 비교하는 실용 기준점.

## Problem

Pretrained VLA를 새 robot에 fine-tune할 때 가능한 action decoder와 objective가 많지만 speed와 success를 함께 최적화하는 기준이 부족하다.

## Core Idea

- Parallel decoding, action chunking, continuous action representation과 L1 objective를 결합한 OFT recipe를 제안한다.
- OpenVLA에 적용한 OpenVLA-OFT로 simulation과 real bimanual manipulation을 평가한다.

## Observation / State / Action Interface

Image·language·proprioception 입력에서 continuous action chunk를 병렬 생성한다.

## Evaluation Scope

- 공식 RSS abstract는 LIBERO 4개 suite에서 OpenVLA 평균 성공률 76.5%에서 97.1%, action throughput 26배 향상을 보고한다.
- Real bimanual ALOHA에서는 π0, RDT-1B, Diffusion Policy와 ACT를 비교한다.

## Limitations to Verify

- LIBERO와 특정 ALOHA task의 결과가 contact-rich 또는 mobile embodiment까지 일반화되는지 확인해야 한다.
- Throughput 외에 sensor-to-action latency와 disturbance reaction을 따로 측정해야 한다.

## Reading Lineage

`OpenVLA → OpenVLA-OFT → efficient embodiment adaptation`
