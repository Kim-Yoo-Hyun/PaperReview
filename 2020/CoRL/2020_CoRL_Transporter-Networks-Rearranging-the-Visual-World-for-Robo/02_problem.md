# Problem

- Year/Venue: 2020 / CoRL
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Robotics, Vision-Language Action, equivariance, Imitation Learning
- Paper link: ./2020/CoRL/2020_CoRL_Transporter-Networks-Rearranging-the-Visual-World-for-Robo/paper.pdf
- Code/Project: https://github.com/google-research/ravens
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- It is sample efficient in learning complex vision-based manipulation tasks: inserting blocks into fixtures (a), sequential pick-and-place in Towers of Hanoi (c), assembling kits with unseen objects (d), ...
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.

## 해결하려는 문제
- In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input – which can parameterize robot ...
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.
- Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses.

## 선행 연구 / 배경 단서
- This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any of the limitations ...
- In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation involves rearranging things, ...
- We propose a simple model architecture that learns to attend to a local region and predict its spatial displacement, while retaining the spatial structure of the visual input.
