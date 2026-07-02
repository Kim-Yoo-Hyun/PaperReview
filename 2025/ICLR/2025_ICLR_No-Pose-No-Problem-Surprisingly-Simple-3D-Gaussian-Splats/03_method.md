# Method

- Year/Venue: 2025 / ICLR Oral
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_No-Pose-No-Problem-Surprisingly-Simple-3D-Gaussian-Splats/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use PyTorch, and the encoder is a vanilla ViT-large model with a patch size of 16, and the decoder is ViT-base.
- Our method is trained either on RE10K (denoted as Ours) or a combination of RE10K and DL3DV (denoted as Ours*).
- Additional details on model weight initialization and training resolution can be found in the appendix.

## 원리적 동기
- We use PyTorch, and the encoder is a vanilla ViT-large model with a patch size of 16, and the decoder is ViT-base.

## 핵심 방법론
- We use PyTorch, and the encoder is a vanilla ViT-large model with a patch size of 16, and the decoder is ViT-base.
- Our method is trained either on RE10K (denoted as Ours) or a combination of RE10K and DL3DV (denoted as Ours*).
- Additional details on model weight initialization and training resolution can be found in the appendix.
- We initialize the encoder/decoder and Gaussian center head with the weights from MASt3R, while the remaining layers are initialized randomly.
