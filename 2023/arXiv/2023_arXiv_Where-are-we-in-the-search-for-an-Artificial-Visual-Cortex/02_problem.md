# Problem — Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Embodied AI, Benchmark
- Official paper: https://arxiv.org/abs/2303.18240
- Code/Project: https://eai-vc.github.io/
- Source audit: arXiv abstract and official project page checked; full benchmark tables remain UNVERIFIED.

## Target Problem and Assumptions

서로 다른 pretraining objective와 dataset의 visual encoder가 embodied control에 얼마나 보편적으로 transfer되는지 평가한다.

## Closed-Loop Position

visual observation encoder를 navigation/manipulation policy의 perception front-end로 사용한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
