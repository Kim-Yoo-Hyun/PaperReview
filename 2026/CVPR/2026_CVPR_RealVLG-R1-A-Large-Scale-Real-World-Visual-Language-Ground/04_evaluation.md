# Evaluation

- Year/Venue: 2026 / CVPR
- Category: Benchmarks and Datasets
- Tags: Visual-Language Grounding, Benchmark, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_RealVLG-R1-A-Large-Scale-Real-World-Visual-Language-Ground/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mIoU
- IoU

## Evaluation Protocol and Results
- The predicted contact points P1p , P2p are first converted into a rectangular grasp pose Gp with fixed width, and then the rectangle alignment and point accuracy are ...
- Based on the annotation pipeline described above, RealVLG-11B achieves a unified integration of multiple real-world grasping datasets, producing high-quality, multigranularity visual-language annotations.
- Task-Specific Pipelines and Verifiable Rewards (3) To achieve a unified model pipeline for visual-language grounding and grasping tasks, supporting coarse-to-fine perception capabilities, RealVLG-R1 constructs taskspecific pipelines and designs ...
- Formally, the verifiable reward function R(q, o) is defined as, To evaluate open-world generalization, as shown in Table 2, we split ∼800 RealVLG-11B objects into three subsets: Seen ...
- Experimental results demonstrate that RealVLG supports zeroshot perception and manipulation in real-world unseen environments, establishing a unified semantic-visual multimodal benchmark that provides a comprehensive data and evaluation platform ...
- The predicted contact points P1p , P2p are first converted into a rectangular grasp pose Gp with fixed width, and then the rectangle alignment and point accuracy are ...

## Baselines
- As summarized in Table 1, compared to existing datasets, RealVLG-11B provides consistent bounding boxes, segmentation masks, rectangular grasp poses, and language descriptions that are rigorously verified through both ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
