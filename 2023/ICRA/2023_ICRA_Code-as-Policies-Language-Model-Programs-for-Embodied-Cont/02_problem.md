# Problem

- Year/Venue: 2023 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, Planning, Robotics
- Paper link: ./2023/ICRA/2023_ICRA_Code-as-Policies-Language-Model-Programs-for-Embodied-Cont/paper.pdf
- Code/Project: https://code-as-policies.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- More recent methods learn the grounding end-to-end (language to action) –, but they require copious amounts of training data, which can be expensive to obtain on real robots.
- By chaining classic logic structures and referencing third-party libraries (e.g., NumPy, Shapely) to perform arithmetic, LLMs used in this way can write robot policies that (i) exhibit spatial-geometric ...
- Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-theart to solve 39.8% of problems on ...

## 해결하려는 문제
- Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-theart to solve 39.8% of problems on ...
- More recent methods learn the grounding end-to-end (language to action) –, but they require copious amounts of training data, which can be expensive to obtain on real robots.
- This paper presents Code as Policies: a robot-centric formulation of language model generated programs (LMPs) that can represent reactive policies (e.g., impedance controllers), as well as waypoint-based policies ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
