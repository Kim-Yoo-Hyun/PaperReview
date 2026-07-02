# Evaluation

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICRA/2026_ICRA_Scalable-Vision-Language-Action-Model-Pretraining-for-Robo/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Open X-Embodiment

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- Our dataset achieves higher values on both metrics compared to the other datasets.
- As illustrated, our dataset demonstrates a significantly higher degree of diversity than existing human and robot VLA datasets.
- 5.1 Pretraining Data Analysis An overview of our pretraining data is shown in Fig.
- We visualize the most frequent words in the language instructions using word clouds, and showcase randomly-sampled task environments.
- Additionally, fine-tuning it on a small amount of real robot action data significantly improves task success rates and generalization to novel objects in real robotic experiments.
- Our dataset achieves higher values on both metrics compared to the other datasets.

## Baselines
- We compare our dataset with existing VLA datasets, including EgoDex , a human-hand VLA dataset of over 300K episodes collected in lab environments, and widely-used robotic VLA datasets: ...
- To fairly compare datasets with varying instruction formats, we employ GPT-4.1 to extract nouns, verbs, and adjectives from each instruction and analyze their distributions separately.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
