# CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/ICCV/2025_ICCV_CoA-VLA-Improving-Vision-Language-Action-Models-via-Visual/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- During inference, the affordance chain is progressively generated as the action state evolves, avoiding unnecessary computational costs associated with outputting extensive language.
- porating reasoning in the format of sequential robot affordances to facilitate task completion.
- OpenAI’s recent model, O1, showcased impressive capabilities in solving complex problems by utilizing extensive reasoning chains.

## Core Idea
- We introduce two formats for chain-of-affordance reasoning: text-based and image-based chain-of-affordance prompting.
- We introduce a novel vision-language co-injection module that integrates this knowledge into the policy network.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments demonstrate that CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks.
- This prompts an important question: can robot models achieve better performance in multi-task, complex environments by reviewing prior observations and then providing task-specific reasoning to guide action prediction?
- This allows the robot to leverage essential contextual information during action inference, resulting in improved precision and ro- Robot foundation models, particularly Vision-LanguageAction (VLA) models, have garnered significant ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments demonstrate that CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks.
- This allows the robot to leverage essential contextual information during action inference, resulting in improved precision and ro- Robot foundation models, particularly Vision-LanguageAction (VLA) models, have garnered significant ...
- We introduce a novel vision-language co-injection module that integrates this knowledge into the policy network.

## Abstract Cue
- porating reasoning in the format of sequential robot affordances to facilitate task completion.
