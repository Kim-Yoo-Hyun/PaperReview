# Evaluation — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 RSS abstract는 다양한 robot manipulation task에서 learned/post-hoc signal과 failure-detection baseline을 비교한다고 보고한다.
- Accuracy뿐 아니라 detection delay와 false alarm을 함께 기록해야 한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

성공 trajectory만으로 detector를 calibration한 뒤 occlusion, object displacement, wrong grasp를 삽입해 lead time과 false alarm을 측정한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
