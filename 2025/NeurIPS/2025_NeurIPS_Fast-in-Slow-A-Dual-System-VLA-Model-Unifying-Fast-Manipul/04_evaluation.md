# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fast-in-Slow-A-Dual-System-VLA-Model-Unifying-Fast-Manipul/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench
- Open X-Embodiment

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- As shown in Table 1, FiS-VLA achieves an average success rate of 69% across 10 diverse tasks, surpassing the previous SOTA methods CogACT and π0 by margins of ...
- We compare FiS-VLA against four state-of-the-art (SOTA) VLA models, including ManipLLM , OpenVLA , π0 , and CogACT, where the latter two are dual-system methods but operate with ...
- In particular, FiS-VLA achieves superior performance on 8 out of 10 tasks, highlighting the robustness of its action generation capabilities.
- Section 4.3 presents both quantitative and qualitative results for FiS-VLA on realworld manipulation tasks, including dual-arm control under different robot configurations.
- For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in realworld tasks in terms of average success rate, while achieving a 117.7 Hz control ...
- As shown in Table 1, FiS-VLA achieves an average success rate of 69% across 10 diverse tasks, surpassing the previous SOTA methods CogACT and π0 by margins of ...

## Baselines
- We compare FiS-VLA against four state-of-the-art (SOTA) VLA models, including ManipLLM , OpenVLA , π0 , and CogACT, where the latter two are dual-system methods but operate with ...
- For baselines, we load the official pretrained parameters provided by each method and adhere to their respective fine-tuning settings.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
