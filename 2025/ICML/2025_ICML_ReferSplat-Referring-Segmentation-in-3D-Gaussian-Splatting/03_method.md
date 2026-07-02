# Method

- Year/Venue: 2025 / ICML Oral
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_ReferSplat-Referring-Segmentation-in-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Training Multi-view Images We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...
- Extensive experiments demonstrate that ReferSplat achieves state-of-the-art performance on both open-vocabulary 3DGS segmentation and the newly proposed referring 3DGS segmentation tasks. ⨂ Rendered Feature Output Mask Pseudo GT ...
- To address these challenges, we propose ReferSplat, a framework that explicitly models 3D Gaussian points with natural language expressions in a spatially aware paradigm.

## 원리적 동기
- Our analysis reveals that 3D multimodal understanding and spatial relationship modeling are key challenges for R3DGS.
- To address these challenges, we propose ReferSplat, a framework that explicitly models 3D Gaussian points with natural language expressions in a spatially aware paradigm.
- Training Multi-view Images We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...

## 핵심 방법론
- Next, we introduce Gaussian-Text Contrastive Learning (GTCL, index 2) to construct discriminative multimodal representations, improving the model’s ability to distinguish semantically similar expressions.
- While τ varies with training, following the schedule: τ = 0.1 × 0.6(iteration/1000) .
- Training is conducted on an NVIDIA RTX A6000 GPU.
- 4, removing components fp,i and fp,w,i from Eq.7 results in performance dropping below the baseline, indicating that vanilla cross-attention alone is ineffective for our task.
- We optimize the Gaussian referring features for 45,000 iterations, using a learning rate of 0.0025, while other parameters, such as the MLP, are trained with a learning rate ...
