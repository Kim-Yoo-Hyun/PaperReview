# Evaluation

- Year/Venue: 2026 / ICLR Oral
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Vision-Language Model, Robotics, 3D Vision, Graph Reasoning
- Paper link: ./2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- AI2-THOR

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- Our MomaGraph-R1 achieves state-of-the-art performance among open-source VLMs, leading by 3.8% on BLINK and 4.8% on our correspondence benchmark compared to the best competing open-source models.
- However, the consistent gap reduction achieved by MomaGraph-R1 shows that reinforcement learning with graphstructured intermediate representations can substantially narrow the divide, offering a practical path toward competitive open-source ...
- Our MomaGraph-R1 achieves performance on par with closed-source giants like Claude-4.5-Sonnet and GPT-5, while clearly surpassing all leading opensource VLMs.
- Notably, MomaGraph-R1 delivers a +11.4% relative improvement over its base model (Qwen2.5-VL-7B) under w/ Graph, highlighting the effectiveness of reinforcement learning with graph-based rewards. (3) Scalability with Task ...
- Our MomaGraph-R1 achieves state-of-the-art performance among open-source VLMs, leading by 3.8% on BLINK and 4.8% on our correspondence benchmark compared to the best competing open-source models.
- However, the consistent gap reduction achieved by MomaGraph-R1 shows that reinforcement learning with graphstructured intermediate representations can substantially narrow the divide, offering a practical path toward competitive open-source ...

## Baselines
- Our MomaGraph-R1 achieves state-of-the-art performance among open-source VLMs, leading by 3.8% on BLINK and 4.8% on our correspondence benchmark compared to the best competing open-source models.
- As shown in Table 3, we compare model performance on visual correspondence tasks from public benchmark BLINK Fu et al. (2024) and our MomaGraph-Bench.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
