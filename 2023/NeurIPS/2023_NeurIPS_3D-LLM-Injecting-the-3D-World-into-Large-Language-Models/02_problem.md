# Problem

- Year/Venue: 2023 / NeurIPS
- Category: 3D Large Multimodal Models
- Tags: LLM, 3D Vision, Vision-Language
- Paper link: ./2023/NeurIPS/2023_NeurIPS_3D-LLM-Injecting-the-3D-World-into-Large-Language-Models/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3dllm/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- One major challenge of training the proposed 3D-LLMs lies in data acquisition.
- Qualitative examples also show that our model could perform more tasks beyond the scope of existing LLMs and VLMs.

## 해결하려는 문제
- Experiments on ScanQA show that our model outperforms state-of-the-art baselines by a large margin (e.g., the BLEU-1 score surpasses state-of-the-art score by 9%).
- Furthermore, experiments on our held-in datasets for 3D captioning, task composition, and 3D-assisted dialogue show that our model outperforms 2D VLMs.
- In this work, we propose to inject the 3D world into large language models and introduce a whole new family of 3D-LLMs.

## 선행 연구 / 배경 단서
- One major challenge of training the proposed 3D-LLMs lies in data acquisition.
- To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs that could take 3D representations (i.e., ...
- To address this, we propose a set of unique data generation pipelines that could generate large-scale 3D data paired with language.
