# Evaluation

- Year/Venue: 2025 / ICML poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_GAPrompt-Geometry-Aware-Point-Cloud-Prompt-for-3D-Vision-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ModelNet40

## Metrics
- accuracy

## Evaluation Protocol and Results
- Extensive experiments demonstrate that GAPrompt significantly outperforms state-ofthe-art PEFT methods and achieves competitive results compared to full fine-tuning on various benchmarks, while utilizing only 2.19% of trainable parameters.
- Existing parameter-efficient fine-tuning (PEFT) approaches, which focus primarily on input token prompting, struggle to achieve competitive performance due to their limited ability to capture the geometric information inherent ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
