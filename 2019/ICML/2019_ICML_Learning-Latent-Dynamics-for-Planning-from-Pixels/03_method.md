# Method

- Year/Venue: 2019 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Planning, latent dynamics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://planetrl.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space.
- Moreover, we propose a multi-step variational inference objective that we name latent overshooting.
- Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.

## 원리적 동기
- Introduction Planning is a natural and powerful approach to decision making problems with known dynamics, such as game playing and simulated robot control (Tassa et al., 2012; Silver ...
- Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space.

## 핵심 방법론
- The training curves for these are shown as orange lines in Figure 4 and as solid green lines in Figure 6 in their paper.
