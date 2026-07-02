# Evaluation

- Year/Venue: 2026 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, 3D manipulation, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_DiffuView-Multi-View-Diffusion-Pretraining-for-3D-Aware-Ro/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Objaverse
- LIBERO
- Open X-Embodiment

## Metrics
- success rate

## Evaluation Protocol and Results
- Quantitative results on MetaWorld Benchmark.
- Mv-bench results. provides a comprehensive suite of simulated manipulation tasks designed to assess spatial reasoning and generalization capabilities in visuomotor learning.
- In addition, we evaluate DiffuView on the MetaWorld benchmark, which is based on the MuJoCo Simulator.
- All experiments are conducted on 8 NVIDIA A100 GPUs.
- Extensive experiments in both simulation and realworld scenarios demonstrate that DiffuView achieves superior generalization, improving success rates under viewpoint shifts by nearly 20% compared with existing methods.
- Quantitative results on MetaWorld Benchmark.

## Baselines
- Additionally, we compare against OpenVLA , VQVLA , and π0.5 -ki , which constitute representative VLA models.
- To rigorously evaluate the effectiveness of our proposed method, we conduct quantitative comparisons against several state-of-the-ar methods featuring distinct model structures.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
