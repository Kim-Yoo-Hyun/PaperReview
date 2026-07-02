# Code as Policies: Language Model Programs for Embodied Control

- Year/Venue: 2023 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, Planning, Robotics
- Paper link: ./2023/ICRA/2023_ICRA_Code-as-Policies-Language-Model-Programs-for-Embodied-Cont/paper.pdf
- Code/Project: https://code-as-policies.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- More recent methods learn the grounding end-to-end (language to action) –, but they require copious amounts of training data, which can be expensive to obtain on real robots.
- By chaining classic logic structures and referencing third-party libraries (e.g., NumPy, Shapely) to perform arithmetic, LLMs used in this way can write robot policies that (i) exhibit spatial-geometric ...
- Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-theart to solve 39.8% of problems on ...

## Core Idea
- RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions on spatial reasoning ...
- Our method also inherits LLM capabilities unrelated to code writing e.g., supporting instructions with non-English languages or emojis (Appendix L.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-theart to solve 39.8% of problems on ...
- This paper presents Code as Policies: a robot-centric formulation of language model generated programs (LMPs) that can represent reactive policies (e.g., impedance controllers), as well as waypoint-based policies ...
- — Large language models (LLMs) trained on codecompletion have been shown to be capable of synthesizing simple Python programs from docstrings .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-theart to solve 39.8% of problems on ...
- More recent methods learn the grounding end-to-end (language to action) –, but they require copious amounts of training data, which can be expensive to obtain on real robots.
- This paper presents Code as Policies: a robot-centric formulation of language model generated programs (LMPs) that can represent reactive policies (e.g., impedance controllers), as well as waypoint-based policies ...

## Abstract Cue
- — Large language models (LLMs) trained on codecompletion have been shown to be capable of synthesizing simple Python programs from docstrings .
