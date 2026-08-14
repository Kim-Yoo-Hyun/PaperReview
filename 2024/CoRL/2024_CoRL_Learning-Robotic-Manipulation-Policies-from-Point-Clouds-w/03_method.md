# Method

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, point cloud, conditional flow matching, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- This result demonstrates that the combination of our choices of observation type, encoder architecture, and training objective leads to a highly effective imitation learning algorithm.
- Training objective unplug charger close door open box open fridge frame hanger open oven books shelf shoes box Mean SR Delta SR Img.
- However, imitation learning algorithms require a number of design choices ranging from the input modality, training objective, and 6-DoF end-effector pose representation.

## 원리적 동기
- Imitation learning (IL) is the widely studied problem of training policies from a given set of expert demonstrations .
- To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models .
- This result demonstrates that the combination of our choices of observation type, encoder architecture, and training objective leads to a highly effective imitation learning algorithm.

## 핵심 방법론
- This result demonstrates that the combination of our choices of observation type, encoder architecture, and training objective leads to a highly effective imitation learning algorithm.
- Training objective unplug charger close door open box open fridge frame hanger open oven books shelf shoes box Mean SR Delta SR Img.
- Given the similar performance of the three point cloud-based baselines, we report the average across 3 training seeds, each tested on the same 3 evaluation seeds, for a ...
- For this reason, we consider the Open loop trajectory diffusion baseline presented in ChainedDiffuser , which is the underlying diffusion model without the higher level waypoint policy forming ...
- For image-based methods, we compare against the original Diffusion Policy as well as AdaFlow which also uses the CFM learning objective.
