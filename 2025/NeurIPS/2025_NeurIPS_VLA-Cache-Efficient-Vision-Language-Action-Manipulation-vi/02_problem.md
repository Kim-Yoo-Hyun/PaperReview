# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VLA-Cache-Efficient-Vision-Language-Action-Manipulation-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To mitigate the extensive cost of VLA models, existing works often adopt generic acceleration techniques, such as model lightweighting , quantization , and early-exit .
- Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem , with traditional reinforcement learning approaches often suffering from poor ...
- While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics of VLA tasks.

## 해결하려는 문제
- To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens ...
- Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15% ...
- This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.

## 선행 연구 / 배경 단서
- To mitigate the extensive cost of VLA models, existing works often adopt generic acceleration techniques, such as model lightweighting , quantization , and early-exit .
- Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem , with traditional reinforcement learning approaches often suffering from poor ...
- While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics of VLA tasks.
