# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ForceVLA-Enhancing-VLA-Models-with-a-Force-aware-MoE-for-C/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- Incorporating external force feedback improves performance for π0 -base model, while our method achieves the highest average success rate, demonstrating robust performance under complex interaction dynamics. “Wipe Board-1” ...
- As demonstrated in FigTable 1: Performance of cucumber peeling. ure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outAvg.
- 5.1 Experimental Setups To evaluate the effectiveness of ForceVLA, we conducted experiments on five diverse contact-rich manipulation tasks: Bottle Pumping, Plug Insertion, USB Drive Insertion, Whiteboard Wiping, and ...
- To contextualize the performance of our proposed ForceVLA model, we compare it against several carefully selected baselines derived from the state-of-the-art π0 architecture, which serves as our foundational ...
- Incorporating external force feedback improves performance for π0 -base model, while our method achieves the highest average success rate, demonstrating robust performance under complex interaction dynamics. “Wipe Board-1” ...
- As demonstrated in FigTable 1: Performance of cucumber peeling. ure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outAvg.

## Baselines
- To contextualize the performance of our proposed ForceVLA model, we compare it against several carefully selected baselines derived from the state-of-the-art π0 architecture, which serves as our foundational ...
- The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion mechanism; (2) the ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
