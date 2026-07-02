# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SimWorld-Robotics-Synthesizing-Photorealistic-and-Dynamic/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat
- R2R
- VLN-CE

## Metrics
- accuracy
- mAP
- SR
- success rate
- collision

## Evaluation Protocol and Results
- After ﬁne-tuning, QwenVL2.5-7B shows substantial improvements across all metrics and is the only model to achieve a non-zero full task success rate.
- In our experiment, the reasoning models show improved depth estimation and destination alignment, which further demonstrates the importance of visual and spatial reasoning in our benchmark.
- As shown in Table 2, among zero-shot ReAct models, Gemini 2.5 Flash achieves the highest progress score.
- However, the results for reasoning models indicate that improved reasoning abilities boost performance.
- After ﬁne-tuning, QwenVL2.5-7B shows substantial improvements across all metrics and is the only model to achieve a non-zero full task success rate.
- In our experiment, the reasoning models show improved depth estimation and destination alignment, which further demonstrates the importance of visual and spatial reasoning in our benchmark.

## Baselines
- The RL baseline, VLA-RL, fails to outperform zero-shot LLMs, indicating the difﬁculty of our benchmark, where sparse reward signals and visually complex spatial reasoning pose challenges for conventional ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
