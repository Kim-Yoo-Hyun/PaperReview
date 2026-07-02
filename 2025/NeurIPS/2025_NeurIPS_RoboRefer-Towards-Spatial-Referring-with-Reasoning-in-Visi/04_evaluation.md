# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Objaverse
- LIBERO

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- 4.1 Single-step Spatial Understanding We evaluate on public single-step spatial understanding benchmarks, including CV-Bench , the BLINK validation split, RoboSpatial configuration part, SAT , and EmbSpatial .
- To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via supervised fine-tuning (SFT).
- In addition, we present RefSpatial-Bench , a challenging benchmark filling the gap 4.1 Single-step Spatial Understanding We evaluate on public single-step spatial understanding benchmarks, including CV-Bench , the ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
