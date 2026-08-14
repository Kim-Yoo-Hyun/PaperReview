# Problem

- Year/Venue: 2023 / ICRA
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, program synthesis, situated planning, long-horizon tasks
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://progprompt.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- — Task planning can require defining myriad domain knowledge about the world in which a robot needs to act.
- To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, given an instruction ...
- However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a given robot in its ...

## 해결하려는 문제
- We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and deploy our method ...
- We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- In scoring mode, the LLM evaluates an enumeration of actions and their arguments from the space of what’s possible.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
