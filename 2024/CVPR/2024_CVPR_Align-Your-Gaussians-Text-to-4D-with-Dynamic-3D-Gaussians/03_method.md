# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, geometry, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Align-Your-Gaussians-Text-to-4D-with-Dynamic-3D-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Scaling Align Your Gaussians To scale AYG and achieve state-of-the-art text-to-4D performance, we introduce several further novel techniques.
- Our method, called Align Your Gaussians (AYG), leverages dynamic 3D Gaussian Splatting with deformation fields as 4D representation.
- We developed a method to stabilize optimization and ensure realistic learnt motion.

## 원리적 동기
- Compared to previous work, we pursue a novel compositional generation-based approach, and combine text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D object optimization, thereby ...
- These techniques allow us to synthesize vivid dynamic scenes, outperform previous work qualitatively and quantitatively and achieve state-of-the-art text-to-4D performance.
- Scaling Align Your Gaussians To scale AYG and achieve state-of-the-art text-to-4D performance, we introduce several further novel techniques.

## 핵심 방법론
- Scaling Align Your Gaussians To scale AYG and achieve state-of-the-art text-to-4D performance, we introduce several further novel techniques.
- We developed a method to stabilize optimization and ensure realistic learnt motion.
- To overcome this limitation, we developed a method to autoregressively extend the 4D sequences.
- We use the middle 4D frame from a first sequence as the initial frame of a second sequence, optimizing a second deformation field, optionally using a different text ...
- We calculate the means ντ and diagonal covariances Γτ of the entire set of 3D Gaussians (using their means µi ) at times τ along the 4D sequence ...
