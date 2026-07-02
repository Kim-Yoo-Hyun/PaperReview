# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VLA-Cache-Efficient-Vision-Language-Action-Manipulation-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LIBERO

## Metrics
- accuracy
- SR
- success rate

## Evaluation Protocol and Results
- Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM and FastV on OpenVLA as compared methods in the LIBERO benchmark.
- In simulation, we evaluate VLA-Cache on three open-source VLA models: OpenVLA , OpenVLA-OFT and CogAct , using the LIBERO benchmark and SIMPLER environment , respectively.
- All experiments are conducted on an NVIDIA RTX 4090 GPU.
- To validate the effectiveness of VLA-Cache, we evaluate our method in both simulation and real-world settings.
- Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15% ...
- Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM and FastV on OpenVLA as compared methods in the LIBERO benchmark.

## Baselines
- Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM and FastV on OpenVLA as compared methods in the LIBERO benchmark.
- CogAct, which integrates a Diffusion Policy for continuous control, serves as our baseline.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
