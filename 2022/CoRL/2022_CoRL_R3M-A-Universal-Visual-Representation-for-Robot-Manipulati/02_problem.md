# Problem — R3M: A Universal Visual Representation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Video Pretraining, manipulation
- Official paper: https://proceedings.mlr.press/v205/nair23a.html
- Code/Project: https://r3m.cs.columbia.edu/
- Source audit: official proceedings abstract and project page checked; detailed result magnitudes remain UNVERIFIED.

## Target Problem and Assumptions

robot task별 작은 demonstration set에서 generalizable visual representation을 확보한다.

## Closed-Loop Position

RGB observation을 frozen/fine-tuned embedding으로 변환해 imitation/RL action policy에 공급한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
