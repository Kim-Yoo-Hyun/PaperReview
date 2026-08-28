# Method — Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Embodied AI, Benchmark
- Official paper: https://arxiv.org/abs/2303.18240
- Code/Project: https://eai-vc.github.io/
- Source audit: arXiv abstract and official project page checked; full benchmark tables remain UNVERIFIED.

## Pipeline

대규모 embodied evaluation suite와 통일된 adaptation protocol로 여러 representation을 비교하고 VC-1을 학습한다.

## Interface

visual observation encoder를 navigation/manipulation policy의 perception front-end로 사용한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
