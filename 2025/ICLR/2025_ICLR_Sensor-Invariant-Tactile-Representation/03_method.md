# Method

- Year/Venue: 2025 / ICLR Poster
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, sensor transfer, representation learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- For baseline models, we use similar pipelines as detailed in Section A.1.
- Random guess classification accuracy corresponds to 6.67%. performs better than that trained from scratch, which indicates the effectiveness of pre-training on the image domain.
- We separately feed 2 tactile images of the same object into the frozen SITR encoder, concatenate their features, and train a decoder to learn the pose change with ...

## 원리적 동기
- For baseline models, we use similar pipelines as detailed in Section A.1.

## 핵심 방법론
- For baseline models, we use similar pipelines as detailed in Section A.1.
- Random guess classification accuracy corresponds to 6.67%. performs better than that trained from scratch, which indicates the effectiveness of pre-training on the image domain.
- We separately feed 2 tactile images of the same object into the frozen SITR encoder, concatenate their features, and train a decoder to learn the pose change with ...
