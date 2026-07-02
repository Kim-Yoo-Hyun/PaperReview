# Evaluation

- Year/Venue: 2025 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark
- Paper link: ./2025/ICLR/2025_ICLR_PARTNR-A-Benchmark-for-Planning-and-Reasoning-in-Embodied/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat
- RLBench

## Metrics
- accuracy
- SR
- success rate
- collision

## Evaluation Protocol and Results
- In contrast, human pairs outperform single humans, in our human-in-the-loop experiments, highlighting potential for improving LLM collaboration strategies.
- As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et al., 2022), we ...
- When comparing model sizes, we observe that a smaller fine-tuned Llama3.18B achieves a similar performance to a Llama3.1-70B without finetuning, while being 8.6X faster.
- We analyze LLM-based planning agents and also provide a human-in-the-loop tool to evaluate how agents collaborate with real humans.
- In contrast, human pairs outperform single humans, in our human-in-the-loop experiments, highlighting potential for improving LLM collaboration strategies.
- As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et al., 2022), we ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
