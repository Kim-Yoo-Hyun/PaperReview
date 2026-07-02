# Method

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Paper link: ./2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/paper.pdf
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) for multi-scale feature extraction and a cross-attention module for segmentation region ...
- We use a cross-attention module taking inputs as FsP E and a randomly initialized queries q0 ∈ RN ×D to generate mask queries q ∈ RN ×D .
- We propose a model, called OpenSeg, that can organize pixels into meaningful regions indicated by texts.

## 원리적 동기
- Image segmentation is an important step to organize an image into a small number of regions in order to understand “what” and “where” are in an image.
- Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff (e.g., floor).
- 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) for multi-scale feature extraction and a cross-attention module for segmentation region ...

## 핵심 방법론
- 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) for multi-scale feature extraction and a cross-attention module for segmentation region ...
- We use a cross-attention module taking inputs as FsP E and a randomly initialized queries q0 ∈ RN ×D to generate mask queries q ∈ RN ×D .
- In the following sections, We use a bold symbol to indicate an array of elements x = {x1 , x2 , ..., xn }, where the first dimension ...
- 3.2 Visual-Semantic Alignment with Masks We use a pair of image Ib and caption Cb to learn visual-semantic alignments.
- This architecture is conceptually similar to Max-deeplab and MaskFormer .
