# Method

- Year/Venue: 2025 / RA-L
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, diffusion policy, model-based planning, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://computationalrobotics.seas.harvard.edu/GPC/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- During evaluation, we use 100 action candidates for all baselines.
- Rather than retraining or fine-tuning, GPC augments a frozen diffusion policy at deployment by coupling it with a predictive world model.

## 원리적 동기
- Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance .
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.

## 핵심 방법론
- During evaluation, we use 100 action candidates for all baselines.
- Besides, we compare the world model against two baselines: deep visual foresight , which uses CNNs and LSTMs for prediction,1 and AVDC , a video diffusion model originally ...
- For fairness, all baselines are trained on the same data and share the same pretrained diffusion policy.
