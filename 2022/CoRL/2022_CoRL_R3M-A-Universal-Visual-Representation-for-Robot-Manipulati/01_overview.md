# R3M: A Universal Visual Representation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Video Pretraining, manipulation
- Official paper: https://proceedings.mlr.press/v205/nair23a.html
- Code/Project: https://r3m.cs.columbia.edu/
- Source audit: official proceedings abstract and project page checked; detailed result magnitudes remain UNVERIFIED.

## Why This Paper Is Here

egocentric video에서 학습한 reusable robot manipulation representation의 대표 baseline이다.

## Problem

robot task별 작은 demonstration set에서 generalizable visual representation을 확보한다.

## Core Idea

시간적·언어적 구조를 이용해 large-scale human video에서 representation을 사전학습하고 downstream policy에 사용한다.

## Interface

RGB observation을 frozen/fine-tuned embedding으로 변환해 imitation/RL action policy에 공급한다.

## Evaluation Scope

여러 simulated/real manipulation setup에서 task performance와 data efficiency를 비교한다.
