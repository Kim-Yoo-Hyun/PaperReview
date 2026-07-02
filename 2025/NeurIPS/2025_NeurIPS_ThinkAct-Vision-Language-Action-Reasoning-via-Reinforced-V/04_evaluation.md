# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ThinkAct-Vision-Language-Action-Reasoning-via-Reinforced-V/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LIBERO
- Open X-Embodiment

## Metrics
- BLEU
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- 4.1 Experimental Setup Implementation Details We initialize Fθ with Qwen2.5-VL 7B .
- The cold-start stage runs for 20K iterations with batch size 32 and learning rate 1e−5 using DeepSpeed ZeRO-3.
- Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
