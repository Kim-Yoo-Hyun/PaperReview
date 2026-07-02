# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Benchmarks and Datasets
- Tags: VLA, Benchmark, long-horizon
- Paper link: ./2025/ICCV/2025_ICCV_VLABench-A-Large-Scale-Benchmark-for-Language-Conditioned/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat
- RLBench
- CALVIN
- LIBERO
- ManiSkill
- VLABench

## Metrics
- accuracy
- SR
- success rate

## Evaluation Protocol and Results
- We demonstrate the superiority of our data framework through comparative experiments.
- Subsequently, the selected skills generate trajectories using RRT , with quaternion interpolation achieved through spherical linear interpolation.
- Step 3: The two operation sequences are evaluated using four metrics, which are weighted and summed to produce the final score.
- We demonstrate the superiority of our data framework through comparative experiments.
- Subsequently, the selected skills generate trajectories using RRT , with quaternion interpolation achieved through spherical linear interpolation.

## Baselines
- The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to the success rate.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
