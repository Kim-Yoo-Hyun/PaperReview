# Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Point-MaDi-Masked-Autoencoding-with-Diffusion-for-Point-Cl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Recent studies have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can operate on partially observed data, ...
- Despite their strengths, existing diffusion-based methods mainly rely on global context aggregation or predefined conditioning mechanisms, such as class labels or auxiliary features, to guide the denoising process.
- 1 illustrates how Point-MaDi contrasts with existing pretext tasks: while MAEs reconstruct masked patches using provided positional embeddings, PointDif advances this paradigm by formulating pre-training as a conditional ...

## Core Idea
- In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE architecture to address ...
- Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional embeddings.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on ScanObjectNN, ModelNet40, ShapeNetPart, S3DIS, and ScanNet demonstrate that Point-MaDi achieves superior performance across downstream tasks, surpassing Point-MAE by 5.50% on OBJ-BG, 5.17% on OBJ-ONLY, and ...
- Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively.
- While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, demonstrating strong generalization without ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE architecture to address ...
- Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional embeddings.
- In the decoder, we design a conditional patch diffusion process, guided by the encoder’s latent features and predicted centers to reconstruct masked patches directly from noise.

## Abstract Cue
- Self-supervised pre-training is essential for 3D point cloud representation learning, as annotating their irregular, topology-free structures is costly and labor-intensive.
