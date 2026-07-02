# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark
- Paper link: ./2026/ICLR/2026_ICLR_RobotArena-infty-Scalable-Robot-Benchmarking-via-Real-to-S/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench
- CALVIN
- LIBERO
- Open X-Embodiment

## Metrics
- mAP

## Evaluation Protocol and Results
- The advantage of Figure 3: Automated robot-camera calibraour modular design is long-term upgradability; tion through differentiable rendering of poseeach module can be replaced with stronger modconditioned 3D robot ...
- We estimate the camera-to-robot transformation using differentiable rendering, shown in Figure 3.
- Specifically, we first construct a joint angle–conditioned 3D Gaussian model of the robot via differentiable rendering in simulation based on its URDF file, following DR-Robot (Liu et al., ...
- Given a robot demonstration video annotated with per-frame joint angles, we then render the Gaussian robot model and optimize the camera’s 3D translation and orientation to minimize a ...
- The advantage of Figure 3: Automated robot-camera calibraour modular design is long-term upgradability; tion through differentiable rendering of poseeach module can be replaced with stronger modconditioned 3D robot ...
- We estimate the camera-to-robot transformation using differentiable rendering, shown in Figure 3.

## Baselines
- To recover each object’s correct 3D pose, we render 2D image views of the reconstructed 3D mesh and compare them against the 2D object crop using correspondence estimation ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
