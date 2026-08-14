# SAFE: Multitask Failure Detection for Vision-Language-Action Models

- Year/Venue: 2025 / NeurIPS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, failure detection, conformal prediction, uncertainty
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://vla-safe.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this paper, we focus on the multitask failure detection problem.
- To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.
- Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.

## Core Idea
- In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- We use uppert as the failure flag threshold δt , and more details about functional CP can be found in Appendix.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and a favorable trade-off between accuracy and detection time using conformal prediction.
- While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of ...
- Therefore, we use LIBERO-10 in our experiments and test OpenVLA , π0 and π0 -FAST on it.

## Limitation
- In this paper, we introduce the multitask failure detection problem for generalist VLA policies, where failure detectors are trained only on seen tasks and evaluated on unseen tasks.
- Based on this observation, we propose SAFE, a simple and efficient failure detection method by operating on the VLA’s internal features.
- Experiments show that SAFE achieves SOTA results in failure detection, and aligns with human intuition.

## Contribution
- We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and a favorable trade-off between accuracy and detection time using conformal prediction.
- In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of ...

## Abstract Cue
- While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of the box.
