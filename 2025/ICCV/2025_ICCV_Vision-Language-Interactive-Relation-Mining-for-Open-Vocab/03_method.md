# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Vision-Language Model, Graph Reasoning, semantic
- Paper link: ./2025/ICCV/2025_ICCV_Vision-Language-Interactive-Relation-Mining-for-Open-Vocab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multimodal interaction.
- Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking , to assess the effectiveness of the open-end generative ...
- Specifically, first, to enhance the generalization of the relation text to visual content, we present a generative relation model to make the text modality explore possible open-ended relations ...

## 원리적 동기
- Though existing methods have been verified to be effective, they usually follow a closed-set assumption, i.e., the training and testing data share the same predicate categories.
- Illustration of the interactive visual-language model for OV-SGG. (a) Previous methods directly use category-level correspondence to adapt the vision-language models to openvocabulary relations. (b) In this work, we ...
- To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multimodal interaction.

## 핵심 방법론
- Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking , to assess the effectiveness of the open-end generative ...
- We use pre-trained GLIP models to initialize our model and keep the visual backbone and text encoder frozen.
- Method Backbone Training Dataset SVRP CaCao PGSG Ours Faster-RCNN CLIP BLIP GLIP VG VG,CC3M,COCO caption VG VG Novel+base R@50/100 mR@50/100 33.5 / 35.9 8.3 / 10.8 -/10.3 / ...
- Following previous works , the Open-Vocabulary SGG (OV-SGG) setting requires the model not to see novel relation categories during training.
- During training, only base relation annotation is available.
