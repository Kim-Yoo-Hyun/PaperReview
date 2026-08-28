# Evaluation — FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / The International Journal of Robotics Research
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; probabilistic-completeness details remain UNVERIFIED.

## Protocol

다양한 manipulation planning problem의 runtime/coverage 비교가 보고되며 상세 protocol은 정독이 필요하다.

## Limitations and Reproducibility

modelled actions와 samplers 품질에 의존하며 noisy closed-loop execution은 핵심 범위가 아니다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
