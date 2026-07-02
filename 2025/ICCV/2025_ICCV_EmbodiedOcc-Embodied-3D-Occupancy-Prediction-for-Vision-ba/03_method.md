# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_EmbodiedOcc-Embodied-3D-Occupancy-Prediction-for-Vision-ba/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Following existing works , we use a pre-trained EfficientNet-B7 to initialize the image encoder in our local module.
- We use mIoU and IoU as the evaluation metrics.
- For each update, we extract semantic and structural features from the observed image and efficiently incorporate them via deformable crossattention to refine the regional Gaussians.

## 원리적 동기
- Most existing methods focus on offline perception from one or a few views and cannot be applied to embodied agents that demand to gradually perceive the scene through ...
- Most existing methods still focus on local 3D occupancy prediction by integrati
- Following existing works , we use a pre-trained EfficientNet-B7 to initialize the image encoder in our local module.

## 핵심 방법론
- Following existing works , we use a pre-trained EfficientNet-B7 to initialize the image encoder in our local module.
- We use mIoU and IoU as the evaluation metrics.
- Each scene consists of 30 posed frames with their corresponding local occupancies.
- The depth prediction network used in the depth-aware branch is a fine-tuned DepthAnything-V2 model that remains frozen during the training, and the depth-aware layer is a 3-layer MLP.
- The resolutions of the monocular input are set to 480\times 640 and the number of Gaussians used to conduct the local prediction is 16200.
