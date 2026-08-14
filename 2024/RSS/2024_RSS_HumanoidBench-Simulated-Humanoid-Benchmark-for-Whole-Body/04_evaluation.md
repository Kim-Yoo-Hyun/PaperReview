# Evaluation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / RSS
- Category: Benchmarks and Datasets
- Tags: Robotics, humanoid, Benchmark, whole-body control, loco-manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://humanoid-bench.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- collision

## Evaluation Protocol and Results
- The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most challenging tasks, illustrating ...
- In this regard, such simulations have accelerated research on control algorithms , ultimately leading to achieve robust humanoid locomotion in the real world .
- Our humanoid robot benchmark tests a variety of complex, longhorizon task with a large action space. we mainly opt for a Unitree H1 humanoid robot1 , which is ...
- On the other hand, the IKEA high-dimensional action spaces and DoFs resulting from furniture assembly environment , BEHAVIOR , and humanoid robots and dexterous hands, and a variety ...
- Our findings reveal that state-of-the-art reinforcement learning algorithms struggle with most tasks, whereas a hierarchical learning baseline achieves superior performance when supported by robust low-level policies, such as ...
- The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most challenging tasks, illustrating ...

## Baselines
- 1 PnP: Pick-and-place / P: Push / I: Insert / R: Reach / Po: Pose / IR: In-hand re-orientation / H: Hold / L: Lift / Ro: Rotate ...
- In addition, most of the previous as Atari and continuous control benchmarks.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
