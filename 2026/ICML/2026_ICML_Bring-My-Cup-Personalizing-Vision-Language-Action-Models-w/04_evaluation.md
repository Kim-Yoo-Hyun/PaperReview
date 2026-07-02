# Evaluation

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_Bring-My-Cup-Personalizing-Vision-Language-Action-Models-w/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Open X-Embodiment
- VLABench

## Metrics
- accuracy
- SR
- success rate

## Evaluation Protocol and Results
- Personalized-SIMPLER (Fractal) Personalized-SIMPLER (Bridge) Personalized-VLABench Real-world Robot Task types #Tasks #Episodes #Personal categories #Cameras Google Robot WidowX Franka SO-101 Pick / Move-near Pick / Place Selection Selection / ...
- The frozen VLA then acts on (x̃t , ℓ̃), so personalization is handled entirely by g and p operating on its inputs.
- At the start of an episode, we parse the personalized instruction (e.g., “bring my cup”) and extract the generic category name c (“cup”).
- We use c as the text query for an open-vocabulary detector and run it on each camera (v) view It , obtaining category-level bounding box propos(v) v als ...
- Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level ...
- We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipu- 1.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
