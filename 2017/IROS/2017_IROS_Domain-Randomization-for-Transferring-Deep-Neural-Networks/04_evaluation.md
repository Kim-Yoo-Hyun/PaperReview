# Evaluation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2017 / IROS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, sim-to-real, domain randomization, perception
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- accuracy
- collision

## Evaluation Protocol and Results
- CONCLUSION We demonstrated that an object detector trained only in simulation can achieve high enough accuracy in the real world to perform grasping in clutter.
- Future directions that could improve the accuracy of object detectors trained using domain randomization include: • • Using higher resolution camera frames Optimizing model architecture choice
- type Object only Real images Distractors Occlusions Full method 1.3 ± 0.6 1.8 ± 1.7 2.4 ± 3.0 No noise added 1.4 ± 0.7 1.9 ± 2.0 2.4 ...
- For two of our most consistently accurate detectors, we evaluated the ability to pick up the detected object in 20 increasingly cluttered scenes using the positions estimated by ...
- Learning in simulation is especially promising for building on recent results using deep reinforcement learning to achieve human-level performance on tasks like Atari and robotic control , .
- CONCLUSION We demonstrated that an object detector trained only in simulation can achieve high enough accuracy in the real world to perform grasping in clutter.

## Baselines
- The detector was able to ignore the previously unseen distractors and pick up the target in 9 of 10 trials.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
