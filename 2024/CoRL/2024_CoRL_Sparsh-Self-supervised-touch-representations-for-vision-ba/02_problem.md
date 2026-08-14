# Problem

- Year/Venue: 2024 / CoRL
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, self-supervised learning, foundation model, contact
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sparsh-ssl.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and ...
- Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.
- For instance, properties like forces and slip require careful and expensive instrumentation in lab settings, while other properties like tracking deformations or extrinsic contact can be infeasible.

## 해결하려는 문제
- We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with ...
- In evaluations, we find that SSL pre-training for touch representation outperforms task and sensor-specific end-to-end training by 95.1% on average over TacBench, and Sparsh (DINO) and Sparsh (IJEPA) ...
- : In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.

## 선행 연구 / 배경 단서
- Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation and slip detection, ...
- Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and ...
- Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.
