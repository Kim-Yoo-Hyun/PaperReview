# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Open-Vocabulary-3D-Semantic-Segmentation-with-Text-to-Imag/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Motivated by the advance of aligning text and image embeddings with large-scale foundation models , existing methods mitigate this challenge by lifting the image features from foundation models ...
- Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data .
- Traditional studies in this field usually target solving this problem in a closed-set fashion , resulting in models that can only be used to make predictions within the ...

## 해결하려는 문제
- We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods.
- In particular, Diff2Scene improves the state-of-the-art method on ScanNet200 by 12%.
- We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual ...

## 선행 연구 / 배경 단서
- Motivated by the advance of aligning text and image embeddings with large-scale foundation models , existing methods mitigate this challenge by lifting the image features from foundation models ...
- Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data .
- Traditional studies in this field usually target solving this problem in a closed-set fashion , resulting in models that can only be used to make predictions within the ...
