# Method

- Year/Venue: 2026 / RA-L
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/RA-L/2026_RA-L_CLARE-Continual-Learning-for-Vision-Language-Action-Models/paper.pdf
- Code/Project: https://tum-lsy.github.io/CLARE/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- Pre-training on internet-scale data and robot demonstrations , provides VLAs with broad priors that enable some degree of generalization .
- During deployment, an autoencoder-based routing mechanism dynamically activates the most relevant adapters without requiring task labels.

## 원리적 동기
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- This long-term adaptability, known as continual or lifelong learning , remains an open challenge in robotics despite decades of research –.
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.

## 핵심 방법론
- AUC ↑ FWT ↑ NBT ↓ AUC ↑ FWT ↑ NBT ↓ AUC ↑ FWT ↑ NBT ↓ SeqFFT SeqLoRA PackNet ER LOTUS DMPEL MLR CLARE (ours) 22.4±0.3 ...
- CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. “NA” indicates not available.
- FWT 60 ER CLARE (ours) 20 0 40 20 0 0 2.5 5 7.5 10 12.5 15 17.5 20 Threshold # Adapters NBT [%] 10 60 ER CLARE ...
