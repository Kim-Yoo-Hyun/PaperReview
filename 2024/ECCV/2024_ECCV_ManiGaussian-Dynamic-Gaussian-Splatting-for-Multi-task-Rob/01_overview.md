# ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Designing autonomous agents for language-conditioned manipulation tasks has been highly desired in the pursuit of artificial intelligence for a long time.
- In realistic deployment, intelligent robots are usually required to deal with unseen scenarios in novel tasks.
- Therefore, comprehending complex 3D structures in the deployment scenes is necessary for the robots to achieve high task success rates across diverse manipulation tasks. ⋆

## Core Idea
- In this paper, we propose a dynamic Gaussian Splatting method named ManiGaussian for multi-task robotic manipulation, which mines scene dynamics via future scene reconstruction.
- On the contrary, we present a dynamic Gaussian Splatting framework to mine the scene dynamics for robotic manipulation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our ManiGaussian on 10 RLBench tasks with 166 variations, and the results demonstrate our framework can outperform the state-of-the-art methods by 13.1% in average success rate1 ...
- Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to verify the effectiveness of ...
- The diversity of these tasks requires the agent to acquire generalizable knowledge about the intrinsical scene-level spatial-temporal dynamics for manipulation, rather than solely relying on mimicking the provided ...

## Limitation
- The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework.

## Contribution
- We evaluate our ManiGaussian on 10 RLBench tasks with 166 variations, and the results demonstrate our framework can outperform the state-of-the-art methods by 13.1% in average success rate1 ...
- In this paper, we propose a dynamic Gaussian Splatting method named ManiGaussian for multi-task robotic manipulation, which mines scene dynamics via future scene reconstruction.
- Specifically, we first formulate the dynamic Gaussian Splatting framework that infers the semantics propagation in the Gaussian embedding space, where the semantic representation is leveraged to predict the ...

## Abstract Cue
- Performing language-conditioned robotic manipulation tasks in unstructured environments is highly demanded for general intelligent robots.
