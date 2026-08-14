# Method

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, learning from play, latent plans
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://learning-from-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...

## 원리적 동기
- Expert demonstrations, on the other hand, can be arbitrarily complex but are expensive to collect, and still typically form narrow training distributions over visited states, leading to an ...
- This remains a challenging open problem in robotics.
- In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.

## 핵심 방법론
- labels input success % BC labeled pixels 66.5% ± 12.1 Play-GCBC (ours) unlabeled pixels 58.7% ± 11.6 Play-LMP (ours) unlabeled pixels 69.4% ± 10.8 BC labeled states 70.3% ...
