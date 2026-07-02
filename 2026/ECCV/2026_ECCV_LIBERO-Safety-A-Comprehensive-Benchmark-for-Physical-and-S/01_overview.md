# LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

- Year/Venue: 2026 / ECCV
- Category: Benchmarks and Datasets
- Tags: VLA, Vision-Language Model, Benchmark, semantic
- Paper link: ./2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/paper.pdf
- Code/Project: https://libero-safety.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. – Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and scalability bottlenecks of ...
- First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- By coupling sparse human intent with an optimization-based motion planner , we ensure the rapid synthesis of large-scale, kinematically feasible, and collision-free expert demonstrations. – Large-Scale Safety Dataset: ...

## Core Idea
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.
- To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 4.1 Experimental Setup To systematically benchmark safety performance across both physical execution and cognitive reasoning, we evaluate a comprehensive suite of 10 representative architectures.
- The selected models are initialized with their official configurations, and all experiments are conducted on 8 NVIDIA A800 GPUs to guarantee a fair and standardized comparison.
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.

## Limitation
- We therefore view LIBERO-Safety as a structured evaluation and data-generation foundation for future work on real-world validation, dense unsafe-event annotation, and intrinsically safety-aligned VLA models.
- Meanwhile, LIBEROSafety remains a simulation-based benchmark; it cannot fully capture realworld contact dynamics, hardware latency, or unpredictable human behavior.
- Through a cross-paradigm evaluation of representative VLA and embodied foundation models, we identify a clear gap between task-level robustness and strict safety compliance: increasing data diversity improves safety-aware ...

## Contribution
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.
- To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline.
- Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.

## Abstract Cue
- Despite the impressive manipulation capabilities of VisionLanguage-Action (VLA) models, their operational safety under strict constraints remains largely unverified.
