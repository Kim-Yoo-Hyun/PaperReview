# Evaluation — Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1988 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence arguments remain UNVERIFIED.

## Protocol

random-walk류 prediction task와 이론 분석이 중심이며 robot control은 직접 평가하지 않는다.

## Limitations and Reproducibility

function approximation, off-policy learning과 partial observability의 안정성은 후속 이론이 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
