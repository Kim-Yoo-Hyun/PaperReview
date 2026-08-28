# Method — R3M: A Universal Visual Representation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Video Pretraining, manipulation
- Official paper: https://proceedings.mlr.press/v205/nair23a.html
- Code/Project: https://r3m.cs.columbia.edu/
- Source audit: official proceedings abstract and project page checked; detailed result magnitudes remain UNVERIFIED.

## Pipeline

시간적·언어적 구조를 이용해 large-scale human video에서 representation을 사전학습하고 downstream policy에 사용한다.

## Interface

RGB observation을 frozen/fine-tuned embedding으로 변환해 imitation/RL action policy에 공급한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
