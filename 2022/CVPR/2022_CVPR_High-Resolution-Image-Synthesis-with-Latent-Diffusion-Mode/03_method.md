# Method

- Year/Venue: 2022 / CVPR
- Category: Foundations: Diffusion and Generative Models
- Tags: Diffusion, latent representation, generation
- Paper link: ./2022/CVPR/2022_CVPR_High-Resolution-Image-Synthesis-with-Latent-Diffusion-Mode/paper.pdf
- Code/Project: https://github.com/CompVis/latent-diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and ...
- To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders.
- In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, ...

## 원리적 동기
- In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, ...
- However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations.
- By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and ...

## 핵심 방법론
- Analyzing the training of class-conditional LDMs with different downsampling factors f over 2M train steps on the ImageNet dataset.
