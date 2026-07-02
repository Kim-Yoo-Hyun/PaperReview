# Evaluation

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_Latent-Reasoning-VLA-Latent-Thinking-and-Prediction-for-Vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LIBERO

## Metrics
- accuracy
- mAP
- SR
- success rate

## Evaluation Protocol and Results
- As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T N1.5 overall.
- Experiments on simulated benchmarks and long-horizon real-robot manipulation tasks demonstrate that LaRA-VLA achieves strong performance while significantly improving inference efficiency, supporting the view that structured reasoning for embodied ...
- These results suggest that latent reasoning improves robustness to error accumulation over long-horizon manipulation.
- These results indicate that latent CoT reasoning not only improves clean performance, but also enhances robustness to corrupted visual inputs.
- Experimental results show that LaRA-VLA consistently outperforms state-of-the-art VLA methods while reducing inference latency by up to 90% compared to explicit CoT-based approaches, demonstrating latent reasoning as an ...
- As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T N1.5 overall.

## Baselines
- We compare our method against ACT (Zhao et al., 2023), ECoT (Zawalski et al., 2025) and GR00T N1.5 (Bjorck et al., 2025) as baselines.
- We further compare LaRA-VLA with Qwen-GR00T (Community, 2026), which serves as a no-CoT baseline without latent reasoning.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
