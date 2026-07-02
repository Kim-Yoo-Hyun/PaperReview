# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OWMM-Agent-Open-World-Mobile-Manipulation-With-Multi-modal/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since PIVOT and RoboPoint are ...
- Our model excels in decision-making, achieving state-of-the-art results in image retrieval and affordance grounding.
- Moreover, our model demonstrates a marked improvement over GPT-4o in decision-making tasks.
- We present the experimental results of single-step evaluation for OWMM-VLM in our simulated benchmark in section 5.1 and episodic evaluation for the OWMM-Agent in our simulated benchmark in ...
- Through experiments, we demonstrate that our model achieves SOTA performance compared to other foundation models including GPT-4o and strong zero-shot generalization in real world.
- The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since PIVOT and RoboPoint are ...

## Baselines
- Regarding the baseline methods, we have evaluated both 1) multitasking foundation VLM models, including GPT-4o and InternVL-2.5-8B that share the same unified input and output configuration as ours ...
- We further provide the qualitative comparisons of different models in Appendix J.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
