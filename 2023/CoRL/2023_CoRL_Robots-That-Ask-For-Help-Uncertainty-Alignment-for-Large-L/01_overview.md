# Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

- Year/Venue: 2023 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, LLM planning, uncertainty, conformal prediction, human intervention
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://robot-help.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this work, we study this challenge in the context of language-instructed robots.
- Accurately modeling and accounting for uncertainty is a longstanding challenge towards robots that operate reliably in unstructured and novel environments.
- However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and untethered from reality.

## Core Idea
- In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they don’t know and ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Results show that KNOWNO achieve the least deviations overall, due to the coverage guarantee from CP.
- 3 we show the difference between achieved and target rates for all methods.
- Since Section 4.1 has shown that Ensemble Set can be expensive (even more so in the multi-step setting) and Prompt Set and Binary can fail to achieve the ...

## Limitation
- Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text input to the ...
- Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it.
- Future work could also incorporate human modeling/error in the conformal prediction framework.

## Contribution
- In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they don’t know and ...
- Experiments across a variety of simulated and real robot setups that involve tasks with different modes of ambiguity (e.g., from spatial to numeric uncertainties, from human preferences to ...

## Abstract Cue
- : Large language models (LLMs) exhibit a wide range of promising capabilities — from step-by-step planning to commonsense reasoning — that may provide utility for robots, but remain prone to confidently hallucinated predictions.
