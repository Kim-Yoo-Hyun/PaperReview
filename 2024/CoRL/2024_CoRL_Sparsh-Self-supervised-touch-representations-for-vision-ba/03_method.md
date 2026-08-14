# Method

- Year/Venue: 2024 / CoRL
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, self-supervised learning, foundation model, contact
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sparsh-ssl.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with ...
- In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- : In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.

## 원리적 동기
- Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and ...
- Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.
- We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with ...

## 핵심 방법론
- In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and ...
- For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition may not be suitable for tasks that ...
