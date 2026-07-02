# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: semantic
- Paper link: ./2024/ECCV/2024_ECCV_Global-Local-Collaborative-Inference-with-LLM-for-Lidar-Ba/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global ...
- We use LLaMA as the LLM backbone, which is initialized by the checkpoint vicuna-7b-v1.5-16k .
- We choose the model architecture of 3DETR as our 3D backbone and bounding box prediction heads.

## 원리적 동기
- In this way, the detection model fails to detect objects not belonging to the training object classes.
- In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global ...

## 핵심 방법론
- We use LLaMA as the LLM backbone, which is initialized by the checkpoint vicuna-7b-v1.5-16k .
- We choose the model architecture of 3DETR as our 3D backbone and bounding box prediction heads.
- The training of phase 2 lasts for 50 epochs with a total batch size of 16.
- The training of phase 1 lasts for 400 epochs with a total batch size of 32 (i.e., a single batch size 4 × 8 GPUs).
- 4.2 Implementation Details The training process contains two phases: 1) training the 3D backbone and the bounding box prediction heads; 2) training the object confidence prediction head, as ...
