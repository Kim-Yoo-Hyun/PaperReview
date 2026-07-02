# Method

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, semantic
- Paper link: ./2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use the official training split for the training and select 4 scenes for the evaluation.
- To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
- By following , we use 100 scenes for training and sample 10 scenes for testing.

## 원리적 동기
- Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an online manner.
- To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
- We use the official training split for the training and select 4 scenes for the evaluation.

## 핵심 방법론
- We use the official training split for the training and select 4 scenes for the evaluation.
- By following , we use 100 scenes for training and sample 10 scenes for testing.
- We name this baseline as 2D methods where LangSplat , LEGaussians and Online-LangSplat are chosen for this category.
- For the per-scene optimization baselines , we initialize the 3DGS with ground-truth point clouds and camera poses given by the dataset and optimize the Gaussians to each testing ...
- Using these precomputed values, the cosine of each Gaussian reduces to a sparse weighted sum over at most L−1 entries via Eq.
