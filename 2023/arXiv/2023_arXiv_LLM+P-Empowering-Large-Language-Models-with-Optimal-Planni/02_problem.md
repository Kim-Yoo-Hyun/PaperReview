# Problem

- Year/Venue: 2023 / arXiv
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, classical planning, PDDL, plan verification
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/Cranial-XIX/llm-p
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.
- However, so far, LLMs cannot reliably solve long-horizon robot planning problems.
- By contrast, classical planners, once a problem is given in a formatted way, can use efficient search algorithms to quickly identify correct, or even optimal, plans.

## 해결하려는 문제
- Via a comprehensive set of experiments on these benchmark problems, we find that LLM+P is able to provide optimal solutions for most problems, while LLMs fail to provide ...
- Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their training corpus or ...
- Along with LLM+P, we define a diverse set of different benchmark problems taken from robot planning scenarios.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
