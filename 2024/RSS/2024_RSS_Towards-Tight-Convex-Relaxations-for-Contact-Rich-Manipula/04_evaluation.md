# Evaluation

- Year/Venue: 2024 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, contact-rich manipulation, convex relaxation, trajectory optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss20/p132.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate
- collision

## Evaluation Protocol and Results
- Exhaustive experiments show that our convexoptimization method generates plans that are consistently within a small percentage of the global optimum, without relying on an initial guess, and that ...
- For each contact mode, we use semidefinite programming to relax the nonconvex dynamics that results from the simultaneous optimization of the object’s pose, contact locations, and contact forces.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
