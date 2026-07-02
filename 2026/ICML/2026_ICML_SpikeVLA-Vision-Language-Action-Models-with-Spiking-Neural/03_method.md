# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ICML/2026_ICML_SpikeVLA-Vision-Language-Action-Models-with-Spiking-Neural/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components. (i) A spiking vision encoder, Spike-V, that replaces dense continuous ...
- However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time scenarios.

## 원리적 동기
- However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time scenarios.
- We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components. (i) A spiking vision encoder, Spike-V, that replaces dense continuous ...
- We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components. (i) A spiking vision encoder, Spike-V, that replaces dense continuous ...

## 핵심 방법론
- CM2 (Georgakis et al., 2022) WS-MGMap (Chen et al., 2022) CMA (Hong et al., 2022a) Sim2Sim (Krantz & Lee, 2022) GridMM (Wang et al., 2023c) Ego2 -Map (Hong ...
- RGB. ✗ ✗ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ 7.02 6.28 6.20 6.07 5.11 5.54 5.53 4.80 4.71 4.42 5.55 5.47 ...
- NaVILA result is reproduced under the same conditions.
- All experiments evaluated on 1,077 episodes in the VLN-CE-Isaac.
- 16126.18 6251.53 141.25 44.23 NE ↓ for low-level policy execution, focusing on control accuracy, safety, and energy efficiency.
