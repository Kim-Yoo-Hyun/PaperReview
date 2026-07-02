# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Point-MaDi-Masked-Autoencoding-with-Diffusion-for-Point-Cl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Recent studies have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can operate on partially observed data, ...
- Despite their strengths, existing diffusion-based methods mainly rely on global context aggregation or predefined conditioning mechanisms, such as class labels or auxiliary features, to guide the denoising process.
- 1 illustrates how Point-MaDi contrasts with existing pretext tasks: while MAEs reconstruct masked patches using provided positional embeddings, PointDif advances this paradigm by formulating pre-training as a conditional ...

## 해결하려는 문제
- In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE architecture to address ...
- Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional embeddings.
- In the decoder, we design a conditional patch diffusion process, guided by the encoder’s latent features and predicted centers to reconstruct masked patches directly from noise.

## 선행 연구 / 배경 단서
- However, unlike 2D images arranged in regular grids, point clouds lack a consistent topology, making the annotation process both expensive and labor-intensive.
- Recent studies have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can operate on partially observed data, ...
- 1 illustrates how Point-MaDi contrasts with existing pretext tasks: while MAEs reconstruct masked patches using provided positional embeddings, PointDif advances this paradigm by formulating pre-training as a conditional ...
