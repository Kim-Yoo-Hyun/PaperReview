# Method

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, Imitation Learning, robot manipulation, data scaling, generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://rail-berkeley.github.io/bridgedata/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Project page: https://rail-berkeley.github.io/bridgedata/ Many Skills 24 Environments move the green cloth from the left burner to the right burner remove the carrot from the drawer and put it ...
- In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset .
- : We introduce BridgeData V2, a large and diverse dataset of robotic manipulation behaviors designed to facilitate research on scalable robot learning.

## 원리적 동기
- However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.
- Many existing robot datasets contain only one or a few environments and tasks , meaning a researcher would need to exactly replicate a scene from the data to ...
- Project page: https://rail-berkeley.github.io/bridgedata/ Many Skills 24 Environments move the green cloth from the left burner to the right burner remove the carrot from the drawer and put it ...

## 핵심 방법론
- In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset .
- These methods cover a range of key design decisions involving the policy architecture, the use of observation histories, action discretization, and action prediction horizon.
- Importantly, the dataset should contain data for many feasible tasks in a given environment so that a multi-task policy must learn to pay attention to the task specification ...
