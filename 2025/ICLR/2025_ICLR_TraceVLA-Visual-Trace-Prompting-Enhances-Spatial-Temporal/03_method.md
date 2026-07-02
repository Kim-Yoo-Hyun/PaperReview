# Method

- Year/Venue: 2025 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_TraceVLA-Visual-Trace-Prompting-Enhances-Spatial-Temporal/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- TraceVLA finetuned OpenVLA finetuned LIBERO-Spatial 84.6% ± 0.2% 82.6% ± 0.4% LIBERO-Object 85.2% ± 0.4% 83.8% ± 0.6% LIBERO-Goal 75.1% ± 0.3% 70.4% ± 0.5% LIBERO-Long 54.1% ± ...
- In addition to SimplerEnv and WIDOWX-250 real robot experiments, in this section, we conduct an additional experiment on LIBERO simulation benchmarks.
- In particular, we take the four suites from LIBERO: LIBERO-long, LIBERO-Spatial, LIBERO-Object, LIBERO-Goal in LIBERO, each with 10 tasks and 50 human teleoperated demonstrations per task.

## 원리적 동기
- TraceVLA finetuned OpenVLA finetuned LIBERO-Spatial 84.6% ± 0.2% 82.6% ± 0.4% LIBERO-Object 85.2% ± 0.4% 83.8% ± 0.6% LIBERO-Goal 75.1% ± 0.3% 70.4% ± 0.5% LIBERO-Long 54.1% ± ...

## 핵심 방법론
- TraceVLA finetuned OpenVLA finetuned LIBERO-Spatial 84.6% ± 0.2% 82.6% ± 0.4% LIBERO-Object 85.2% ± 0.4% 83.8% ± 0.6% LIBERO-Goal 75.1% ± 0.3% 70.4% ± 0.5% LIBERO-Long 54.1% ± ...
- In addition to SimplerEnv and WIDOWX-250 real robot experiments, in this section, we conduct an additional experiment on LIBERO simulation benchmarks.
- In particular, we take the four suites from LIBERO: LIBERO-long, LIBERO-Spatial, LIBERO-Object, LIBERO-Goal in LIBERO, each with 10 tasks and 50 human teleoperated demonstrations per task.
- We evaluate the multitask performance of the pretrained VLA policy on these four suites.
- Specifically: • LIBERO-Spatial: Contains the same set of objects but in varying layouts, testing the model’s ability to understand spatial relationships.
