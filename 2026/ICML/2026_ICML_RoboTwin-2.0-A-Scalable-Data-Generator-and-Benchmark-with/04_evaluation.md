# Evaluation

- Year/Venue: 2026 / ICML
- Category: Benchmarks and Datasets
- Tags: VLA, Robotics, Benchmark
- Paper link: ./2026/ICML/2026_ICML_RoboTwin-2.0-A-Scalable-Data-Generator-and-Benchmark-with/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- CALVIN
- LIBERO
- RoboTwin

## Metrics
- success rate
- collision

## Evaluation Protocol and Results
- VLA models pre-trained on RoboTwin 2.0 data achieve a 3.6× improvement in few-shot real-world transfer and a 2.2× gain in zero-shot generalization compared to baselines trained on real-world ...
- The framework comprises: (1) an automated expert pipeline that integrates MLLMs with simulation feedback to validate and iteratively refine task execution code; (2) comprehensive domain randomization over language, ...
- Extensive evaluations demonstrate that the proposed paradigm yields consistent and substantial real-world performance gains.
- We further introduce a standardized benchmark for evaluating policy generalization under domain shift, covering variations in scene clutter, visual appearance, embodiment, and open-ended language goals.
- our synthetic data achieve a 3.6× improvement in few-shot real-world transfer (over a 10-demo baseline) and a 2.2× gain in zero-shot generalization.
- VLA models pre-trained on RoboTwin 2.0 data achieve a 3.6× improvement in few-shot real-world transfer and a 2.2× gain in zero-shot generalization compared to baselines trained on real-world ...

## Baselines
- VLA models pre-trained on RoboTwin 2.0 data achieve a 3.6× improvement in few-shot real-world transfer and a 2.2× gain in zero-shot generalization compared to baselines trained on real-world ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
