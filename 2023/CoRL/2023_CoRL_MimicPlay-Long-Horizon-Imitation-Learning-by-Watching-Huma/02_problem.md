# Problem

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, human video, cross-embodiment, hierarchical policy, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://mimic-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Such latent plans provide rich 3D guidance (what to do and where to interact) at each time step, tackling the challenging long-horizon manipulation problem by converting it into ...
- Efficiently teaching robots to perform general-purpose manipulation tasks is a long-standing challenge.
- In this work, we argue that the data required for learning high-level plan and low-level control can come in different forms, and doing so could substantially reduce the ...

## 해결하려는 문제
- With systematic evaluations of 14 longhorizon manipulation tasks in the real world, we show that MIMICPLAY outperforms state-of-the-art imitation learning methods in task success rate, generalization ability, and ...
- Motivated by this, we introduce a hierarchical learning framework named MIMICPLAY that learns latent plans from human play data to guide low-level visuomotor control trained on a small ...

## 선행 연구 / 배경 단서
- Such latent plans provide rich 3D guidance (what to do and where to interact) at each time step, tackling the challenging long-horizon manipulation problem by converting it into ...
- Efficiently teaching robots to perform general-purpose manipulation tasks is a long-standing challenge.
- Prior works show that data collected this way covers more diverse behaviors and situations compared to typical task-oriented demonstrations .
