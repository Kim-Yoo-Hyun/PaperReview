# Method

- Year/Venue: 2025 / WACV
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, semantic, alignment
- Paper link: ./2025/WACV/2025_WACV_AIDE-Improving-3D-Open-Vocabulary-Semantic-Segmentation-by/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, to address these issues and improve generalization performance, we propose an AlIgned 3D Open-Vocabulary S Emantic Segmentation framework, called A I D E, with two ...
- Quantative Results In this part, we present the results on ScanNet, S3DIS, and nuScenes in Tabs.
- Ablation Studies In this part, we present the ablation studies on the effects of two proposed modules (Tab.

## 원리적 동기
- Due to the lack of large-scale 3D-vision-language segmentation data, instead of training models from scratch, the current solutions distill knowledge from pre-trained 2D vision-language models (VLMs) into 3D ...
- Moreover, as 2D VLMs are trained on 2D datasets, text encoders of VLMs, which serve as the bridge between 3D models and an unbounded set of categories, lack ...
- In this paper, to address these issues and improve generalization performance, we propose an AlIgned 3D Open-Vocabulary S Emantic Segmentation framework, called A I D E, with two ...

## 핵심 방법론
- Quantative Results In this part, we present the results on ScanNet, S3DIS, and nuScenes in Tabs.
- Ablation Studies In this part, we present the ablation studies on the effects of two proposed modules (Tab.
- For a fair comparison, we use ViT-GPT2 as the image captioner fcap .
- Notably, A I D E also narrows the gap with the fully supervised model, which represents the upper bound based on the backbone and training strategies.
- Four trainable tokens are used in adapting text encoders.
