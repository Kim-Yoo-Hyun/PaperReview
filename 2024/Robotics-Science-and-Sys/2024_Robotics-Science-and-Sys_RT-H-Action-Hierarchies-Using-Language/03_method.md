# Method — RT-H: Action Hierarchies Using Language

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Action Hierarchy, language, Google DeepMind
- Official paper: https://www.roboticsproceedings.org/rss20/p049.html
- Code/Project: not identified
- Source audit: official RSS proceedings abstract checked; full benchmark tables remain UNVERIFIED.

## Pipeline

policy가 먼저 language motion command를 예측하고 이를 robot action으로 변환하는 hierarchical action representation을 학습한다.

## Interface

image/language instruction → language motion concept → low-level robot action의 계층을 갖는다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
