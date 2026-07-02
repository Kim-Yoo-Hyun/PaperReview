# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_From-Seeing-to-Doing-Bridging-Reasoning-and-Decision-for-R/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- LIBERO
- BridgeData
- Open X-Embodiment

## Metrics
- accuracy
- IoU
- mAP
- RMSE
- success rate
- collision

## Evaluation Protocol and Results
- 1, FSD achieves a leading average rank of 1.3 across 15 tasks from spatial benchmarks, significantly outperforming other 13B open-source models and rivaling the closed-source GPT-4o.
- For object reference (RoboRefIt), FSD achieves 56.7% accuracy, surpassing both GPT-4o (15.3%) and specialist models like RoboPoint (49.8%) by significant margins.
- Specifically, FSD achieves 61.82% accuracy on VABench-P, over 3x higher than RoboPoint (19.09%) and attains significantly lower error rates with a better LLM Score on VABench-V.
- On the more challenging free space reference task (Where2Place), FSD performs competitively with RoboPoint while substantially outperforming other models.
- 1, FSD achieves a leading average rank of 1.3 across 15 tasks from spatial benchmarks, significantly outperforming other 13B open-source models and rivaling the closed-source GPT-4o.
- For object reference (RoboRefIt), FSD achieves 56.7% accuracy, surpassing both GPT-4o (15.3%) and specialist models like RoboPoint (49.8%) by significant margins.

## Baselines
- Since end-to-end VLA methods require fine-tuning, for fair comparison, we ensured that all end-to-end baseline methods were trained using the BridgeData Walke et al. (2023) dataset and evaluated ...
- We conducted this comparison to demonstrate the advantages of our reasoning-based FSD approach.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
