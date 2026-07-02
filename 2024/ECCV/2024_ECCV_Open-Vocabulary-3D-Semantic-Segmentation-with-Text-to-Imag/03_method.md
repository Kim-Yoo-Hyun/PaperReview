# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Open-Vocabulary-3D-Semantic-Segmentation-with-Text-to-Imag/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual ...
- We provide qualitative analysis of our approach and OpenScene for the zero-shot visual grounding task in Fig.
- 4, we provide qualitative analysis of our approach and OpenScene for the zero-shot 3D semantic segmentation task.

## 원리적 동기
- Motivated by the advance of aligning text and image embeddings with large-scale foundation models , existing methods mitigate this challenge by lifting the image features from foundation models ...
- Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data .
- We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual ...

## 핵심 방법론
- We provide qualitative analysis of our approach and OpenScene for the zero-shot visual grounding task in Fig.
- 4, we provide qualitative analysis of our approach and OpenScene for the zero-shot 3D semantic segmentation task.
- mIoU Our full model 17.5 Without 2D (salient) mask 12.8 Without 3D (geometric) mask 16.5 Without discriminative (CLIP) features 15.5 Without generative (Stable Diffusion) features 15.3 2D and ...
- We find that discriminative and diffusion features serve as strong complementary to each other.
- It predicts accurate semantic labels for both head and tail categories by leveraging both CLIP and diffusion features.
