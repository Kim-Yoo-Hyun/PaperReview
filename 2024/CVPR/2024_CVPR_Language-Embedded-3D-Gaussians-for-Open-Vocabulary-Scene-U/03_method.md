# Method

- Year/Venue: 2024 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, semantic
- Paper link: ./2024/CVPR/2024_CVPR_Language-Embedded-3D-Gaussians-for-Open-Vocabulary-Scene-U/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that ...
- In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks.
- We conduct a comparative evaluation of our method with DFF , LeRF , and 3DOVS , focusing on visual quality, languageembedded accuracy, rendering speed and model efficiency.

## 원리적 동기
- Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation.
- Language-embedded scene representations have made progress by incorporating language features into 3D spaces.
- Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that ...

## 핵심 방법론
- We conduct a comparative evaluation of our method with DFF , LeRF , and 3DOVS , focusing on visual quality, languageembedded accuracy, rendering speed and model efficiency.
- Quantitative comparison of our method with DFF , LeRF , 3DOVS . mPA↑ mP↑ mIoU↑ mAP↑ Quantization w/o DINO w/o Llb 0.927 0.939 0.604 0.666 0.481 0.544 0.676 ...
- Comparisons We compare our method both qualitatively and quantitatively with DFF , LeRF , and 3DOVS on our annotated Mip-NeRF360 dataset using a single RTX3090 GPU, following their ...
- Our approach notably delivers the highest visual rendering quality and query accuracy across all the tested scenes.
- The training involves 30,000 iterations, utilizing the Adam optimizer , with a learning rate set to 0.001 and betas equal to (0.9, 0.999).
