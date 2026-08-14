# Problem

- Year/Venue: 2025 / RA-L
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, diffusion policy, model-based planning, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://computationalrobotics.seas.harvard.edu/GPC/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance .

## 해결하려는 문제
- Rather than retraining or fine-tuning, GPC augments a frozen diffusion policy at deployment by coupling it with a predictive world model.
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance .

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
