# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Vision-Language Model, Robotics, Benchmark
- Paper link: ./2026/ICLR/2026_ICLR_RoboInter-A-Holistic-Intermediate-Representation-Suite-Tow/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- BLEU
- accuracy
- IoU
- success rate

## Evaluation Protocol and Results
- Generate Trace Remove Outliers SAM Calibrate Camera Param Cross Validation & Formatting Spatial VQA Episodes Env Temporal VQA Trace Generation Q: The robot task is ‘drag the plate… ...
- A: [, ] Q: The robot task is ‘drag the plate… Return the future 10 point of gripper.
- A: (, , … Trace Choose Object Grounding Box Q: The robot task is ‘pick the orange… Determine manipulated object’s bbox.
- Q: Which image describe the task ‘move the salt cellar to the table? (A/B/C/D) A: B Grasp Pose Choose Q: Which images contains the most suitable Grasp Pose ...
- Generate Trace Remove Outliers SAM Calibrate Camera Param Cross Validation & Formatting Spatial VQA Episodes Env Temporal VQA Trace Generation Q: The robot task is ‘drag the plate… ...
- A: [, ] Q: The robot task is ‘drag the plate… Return the future 10 point of gripper.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
