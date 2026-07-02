# Problem

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Paper link: ./2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/paper.pdf
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Image segmentation is an important step to organize an image into a small number of regions in order to understand “what” and “where” are in an image.
- Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff (e.g., floor).
- Language is a natural interface to describe what is in an image.

## 해결하려는 문제
- We propose OpenSeg to address the above issue while still making use of scalable image-level supervision of captions.
- We propose a model, called OpenSeg, that can organize pixels into meaningful regions indicated by texts.
- OpenSeg significantly outperforms the recent openvocabulary method of LSeg by +19.9 mIoU on PASCAL dataset, thanks to its scalability. bride groom hills field sky cow calf grass trees ...

## 선행 연구 / 배경 단서
- Recently, CLIP and ALIGN learn with billion-scale image-text training examples to understand “what” are in an image with arbitrary text queries.
- Recently, Li et al. introduce an open-vocabulary segmentation method using pre-trained CLIP text-encoders.
- It trains an image encoder to predict pixel embedding aligned with the text embedding of its pixel label.
