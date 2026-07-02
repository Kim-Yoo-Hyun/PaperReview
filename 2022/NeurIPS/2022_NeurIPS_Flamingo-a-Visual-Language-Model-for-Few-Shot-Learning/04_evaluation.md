# Evaluation

- Year/Venue: 2022 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, few-shot, alignment
- Paper link: ./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- This is achieved with as few as four examples per task, demonstrating practical and efficient adaptation of vision models to new tasks.
- Flamingo outperforms by a large margin all previous zero-shot or few-shot methods on the 16 benchmarks considered.
- On six tasks, Flamingo even outperforms the fine-tuned SotA despite using a single set of model weights and only 32 task-specific examples.
- We report the results of the Flamingo models on few-shot learning in Section 3.1.
- Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no fine-tuning.
- This is achieved with as few as four examples per task, demonstrating practical and efficient adaptation of vision models to new tasks.

## Baselines
- Flamingo outperforms by a large margin all previous zero-shot or few-shot methods on the 16 benchmarks considered.
- More importantly, Flamingo is often competitive with state-of-the-art methods additionally fine-tuned on up to hundreds of thousands of annotated examples.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
