# Method

- Year/Venue: 2023 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, Planning, Robotics
- Paper link: ./2023/ICRA/2023_ICRA_Code-as-Policies-Language-Model-Programs-for-Embodied-Cont/paper.pdf
- Code/Project: https://code-as-policies.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions on spatial reasoning ...
- Our method also inherits LLM capabilities unrelated to code writing e.g., supporting instructions with non-English languages or emojis (Appendix L.
- Our approach also assumes all given instructions are feasible, and we cannot tell if a response will be correct a priori.

## 원리적 동기
- More recent methods learn the grounding end-to-end (language to action) –, but they require copious amounts of training data, which can be expensive to obtain on real robots.
- By chaining classic logic structures and referencing third-party libraries (e.g., NumPy, Shapely) to perform arithmetic, LLMs used in this way can write robot policies that (i) exhibit spatial-geometric ...
- RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions on spatial reasoning ...

## 핵심 방법론
- RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions on spatial reasoning ...
- Our method also inherits LLM capabilities unrelated to code writing e.g., supporting instructions with non-English languages or emojis (Appendix L.
- Our approach also assumes all given instructions are feasible, and we cannot tell if a response will be correct a priori.
- Hierarchical LMPs on Code-Generation Benchmarks We evaluate our code-generation approach on two codegeneration benchmarks: (i) a robotics-themed RoboCodeGen and (ii) HumanEval , which consists of standard code-gen problems.
