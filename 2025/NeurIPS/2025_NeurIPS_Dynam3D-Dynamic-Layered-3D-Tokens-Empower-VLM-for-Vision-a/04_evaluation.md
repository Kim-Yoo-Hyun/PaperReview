# Evaluation

- Year/Venue: 2025 / NeurIPS Oral
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Dynam3D-Dynamic-Layered-3D-Tokens-Empower-VLM-for-Vision-a/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Matterport3D
- 3RScan
- HM3D
- R2R

## Metrics
- accuracy
- mAP
- SPL
- SR
- success rate

## Evaluation Protocol and Results
- Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR).
- Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE.
- Methods LLM CM2 WS-MGMap InstructNav∗ AO-Planner∗ NaVid VLN-3DFF g3D-LF Uni-NaVid Dynam3D (Ours) × × ✓ ✓ ✓ × × ✓ ✓ 4.2 R2R-CE Val R2R-CE Test NE↓ OSR↑ ...
- 4.1 Comparison with SOTA Methods As shown in Tables 1 and 2, we evaluate the navigation performance of our Dynam3D across three distinct continuous-environment VLN benchmarks.
- Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR).
- Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE.

## Baselines
- Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR).
- 4.1 Comparison with SOTA Methods As shown in Tables 1 and 2, we evaluate the navigation performance of our Dynam3D across three distinct continuous-environment VLN benchmarks.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
