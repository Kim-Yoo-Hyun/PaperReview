# Evaluation — R3M: A Universal Visual Representation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Video Pretraining, manipulation
- Official paper: https://proceedings.mlr.press/v205/nair23a.html
- Code/Project: https://r3m.cs.columbia.edu/
- Source audit: official proceedings abstract and project page checked; detailed result magnitudes remain UNVERIFIED.

## Protocol

여러 simulated/real manipulation setup에서 task performance와 data efficiency를 비교한다.

## Limitations and Reproducibility

pretraining data bias와 representation score가 closed-loop robustness로 이어지는지 별도 검증이 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
