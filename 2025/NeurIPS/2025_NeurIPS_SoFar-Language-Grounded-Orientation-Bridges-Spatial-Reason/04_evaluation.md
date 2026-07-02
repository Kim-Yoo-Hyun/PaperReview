# Evaluation

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SoFar-Language-Grounded-Orientation-Bridges-Spatial-Reason/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Objaverse
- LIBERO
- BridgeData
- Open X-Embodiment

## Metrics
- accuracy
- mAP
- success rate
- collision

## Evaluation Protocol and Results
- 7, S O FAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead.
- We train different model variants on OrienText300K, and the results in Table 2 report performance across different angular thresholds ranging from 45° to 5°.
- We also demonstrate S O FAR’s embodiment generality with different end-effectors, including dexterous hands and suction cups, as illustrated in Fig.
- Additional robot setups and generalization results are provided in Appendix A.
- Extensive experiments demonstrated the effectiveness and generalization of our S O FAR, e.g., zero-shot 48.7% successful rate on Open6DOR and zero-shot 74.9% successful rate on SIMPLER-Env.
- 7, S O FAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead.

## Baselines
- 7, S O FAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
