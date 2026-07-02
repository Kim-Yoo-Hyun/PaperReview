# Method

- Year/Venue: 2014 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, geometry
- Paper link: ./2014/NeurIPS/2014_NeurIPS_Depth-Map-Prediction-from-a-Single-Image-using-a-Multi-Sca/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction based on the ...

## 원리적 동기
- Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.
- While there is much prior work on estimating depth based on stereo images or motion , there has been relatively little on estimating depth from a single image.
- In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction based on the ...

## 핵심 방법론
- Our network is made of two component stacks, shown in Fig.
- A coarse-scale network first predicts the depth of the scene at a global level.
- This is then refined within local regions by a fine-scale network.
- Both stacks are applied to the original input, but in addition, the coarse network’s output is passed to the fine network as additional first-layer image features.
- In this way, the local network can edit the global prediction to incorporate finer-scale details.
