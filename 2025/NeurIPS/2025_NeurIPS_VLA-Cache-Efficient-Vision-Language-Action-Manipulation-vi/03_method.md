# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VLA-Cache-Efficient-Vision-Language-Action-Manipulation-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens ...
- When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency architectures and delivering additive ...
- This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.

## 원리적 동기
- To mitigate the extensive cost of VLA models, existing works often adopt generic acceleration techniques, such as model lightweighting , quantization , and early-exit .
- Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem , with traditional reinforcement learning approaches often suffering from poor ...
- To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens ...

## 핵심 방법론
- When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency architectures and delivering additive ...
