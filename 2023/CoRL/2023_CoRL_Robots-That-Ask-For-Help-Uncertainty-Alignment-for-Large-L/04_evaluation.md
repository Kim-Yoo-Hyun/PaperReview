# Evaluation

- Year/Venue: 2023 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, LLM planning, uncertainty, conformal prediction, human intervention
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://robot-help.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- Results show that KNOWNO achieve the least deviations overall, due to the coverage guarantee from CP.
- 3 we show the difference between achieved and target rates for all methods.
- Since Section 4.1 has shown that Ensemble Set can be expensive (even more so in the multi-step setting) and Prompt Set and Binary can fail to achieve the ...
- First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the three settings — we set the failure level ϵ=0.15.
- Results show that KNOWNO achieve the least deviations overall, due to the coverage guarantee from CP.
- 3 we show the difference between achieved and target rates for all methods.

## Baselines
- A straightforward way to construct prediction sets given a desired 1−ϵ coverage is to rank options according to confidence and construct a set such that the cumulative confidence ...
- We also introduce two prompt-based baselines: Prompt Set prompts the LLM to directly output the prediction set (e.g., “Prediction set: [A, C]”); Binary prompts the LLM to directly ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
