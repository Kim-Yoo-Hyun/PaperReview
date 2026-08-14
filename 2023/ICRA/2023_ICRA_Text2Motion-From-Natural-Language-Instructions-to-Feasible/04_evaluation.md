# Evaluation

- Year/Venue: 2023 / ICRA
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, task and motion planning, feasibility, skill chaining
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/text-to-motion/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate
- collision

## Evaluation Protocol and Results
- We conduct experiments to test four hypotheses: H1 Geometric feasibility planning is a necessary ingredient when using LLMs and robot skills to solve manipulation tasks with geometric dependencies ...
- The following subsections describe the baseline methods we compare against, details on LLMs and prompts, the tasks over which planners are evaluated, and performance metrics we report.
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We conduct experiments to test four hypotheses: H1 Geometric feasibility planning is a necessary ingredient when using LLMs and robot skills to solve manipulation tasks with geometric dependencies ...

## Baselines
- The following subsections describe the baseline methods we compare against, details on LLMs and prompts, the tasks over which planners are evaluated, and performance metrics we report.
- We provide an example of the prompt structure used to query greedy-search for K = 5 skills at the first planning iteration (prompt template is in black and ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
