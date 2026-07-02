# Method

- Year/Venue: 2026 / ECCV
- Category: Benchmarks and Datasets
- Tags: VLA, Vision-Language Model, Benchmark, semantic
- Paper link: ./2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/paper.pdf
- Code/Project: https://libero-safety.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.
- To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline.
- Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.

## 원리적 동기
- This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. – Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and scalability bottlenecks of ...
- First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.

## 핵심 방법론
- Perceptual Parametric Perturbation Task Definition Scene Dynamics Physical Semantic Proximal Safety Safety HRI Data Acquisition RLBench CALVIN LIBERO RoboCasa RoboTwin 2.0 LIBERO-PRO LIBERO-Plus SafeLIBERO VLA-Arena LIBERO-X ✗ ✗ ...
- Ours ✓ ✓ Static / Dynamic ✓ ✓ ✓ Gen. / Teleop.
- 2.2 Safety-Aware Policy Learning The limitations of current robotic policies have motivated increasing research into safety-aware policy learning.
- SafeVLA introduces explicit safety objectives into policy optimization, providing a foundation for improving robustness to long-tail failures and distributional shifts.
- Extending the focus on robustness during execution, Latent Safety Filters estimates safe sets directly from high-dimensional observations and constrains policies to avoid entering unsafe regions.
