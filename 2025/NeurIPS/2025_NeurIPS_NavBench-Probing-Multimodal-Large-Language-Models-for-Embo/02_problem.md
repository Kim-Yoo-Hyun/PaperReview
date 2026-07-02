# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_NavBench-Probing-Multimodal-Large-Language-Models-for-Embo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- For example, navigating across multiple rooms with ambiguous instructions poses greater challenges than following simple step-by-step commands in a single hallway.
- The step-by-step navigation is assessed from different difficulty levels, which is defined by cognitive, spatial, and execution complexity. and ObjectNav , were developed prior to the emergence of ...
- Furthermore, navigation tasks in real-world environments can vary significantly in difficulty due to differences in spatial layout, instruction complexity, and required decision-making steps.

## 해결하려는 문제
- We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.
- Results also show that models with higher comprehension scores tend to achieve better execution performance.
- To support real-world deployment, we introduce a pipeline that converts MLLMs’ outputs into robotic actions.

## 선행 연구 / 배경 단서
- However, most existing benchmarks treat all navigation episodes equally difficult, failing to capture this essential variation.
- For example, navigating across multiple rooms with ambiguous instructions poses greater challenges than following simple step-by-step commands in a single hallway.
- Difficulty Level Easy Medium Hard Cognitive Complexity Spatial Complexity Execution Complexity Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability ...
