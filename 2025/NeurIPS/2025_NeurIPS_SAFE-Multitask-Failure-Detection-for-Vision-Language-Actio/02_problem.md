# Problem

- Year/Venue: 2025 / NeurIPS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, failure detection, conformal prediction, uncertainty
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://vla-safe.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- In this paper, we focus on the multitask failure detection problem.
- To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.
- Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.

## 해결하려는 문제
- We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and a favorable trade-off between accuracy and detection time using conformal prediction.
- In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of ...

## 선행 연구 / 배경 단서
- In this paper, we focus on the multitask failure detection problem.
- To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.
- Most existing failure detection methods train a separate failure detector for each task, and evaluate the detector only on that task [8–17].
