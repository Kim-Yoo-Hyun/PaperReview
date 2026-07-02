# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Point-MaDi-Masked-Autoencoding-with-Diffusion-for-Point-Cl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE architecture to address ...
- Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional embeddings.
- This dual-diffusion design drives comprehensive global semantic and local geometric representations during pre-training, eliminating external geometric priors.

## 원리적 동기
- Recent studies have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can operate on partially observed data, ...
- Despite their strengths, existing diffusion-based methods mainly rely on global context aggregation or predefined conditioning mechanisms, such as class labels or auxiliary features, to guide the denoising process.
- In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE architecture to address ...

## 핵심 방법론
- These results underscore the effectiveness of Point-MaDi’s dualdiffusion pre-training in capturing complex scene semantics and fine-grained geometric details.
- Inst. mIoU mAcc mIoU 83.7 85.2 – 49.0 – – 41.1 – – 68.6 – 70.1 69.9 – 69.5 71.0 +1.1 60.0 – 61.0 60.8 – 60.2 61.2 ...
