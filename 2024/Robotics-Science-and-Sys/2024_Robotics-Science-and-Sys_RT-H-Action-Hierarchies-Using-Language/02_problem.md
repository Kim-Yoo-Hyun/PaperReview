# Problem — RT-H: Action Hierarchies Using Language

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Action Hierarchy, language, Google DeepMind
- Official paper: https://www.roboticsproceedings.org/rss20/p049.html
- Code/Project: not identified
- Source audit: official RSS proceedings abstract checked; full benchmark tables remain UNVERIFIED.

## Target Problem and Assumptions

flat action prediction이 correction, compositional generalization과 human intervention에 불리한 문제를 다룬다.

## Closed-Loop Position

image/language instruction → language motion concept → low-level robot action의 계층을 갖는다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
