# Method

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Gaussian Splatting, world model, Robotics
- Paper link: ./2025/ICCV/2025_ICCV_GWM-Towards-Scalable-Gaussian-World-Models-for-Robotic-Man/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation ...
- To achieve real-time training and inference, we design a 3D Gaussian Variational Autoencoder (VAE) to extract latent representations from 3D Gaussians, allowing the diffusion-based world model to operate ...
- For realworld evaluation, we introduce a Franka PnP task suite with 20 variations, encompassing both in-domain and out-ofdomain settings.

## 원리적 동기
- The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of the three-dimensional world, even ...
- To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation ...

## 핵심 방법론
- FVD↓ PSNR↑ SSIM↑ LPIPS↓ M ETA -W ORLD iVideoGPT GWM 75.0 73.0 20.4 20.6 82.3 82.8 9.5 9.0 F RANKA -P N P iVideoGPT GWM 63.2 61.5 27.8 ...
- Prediction Difference Ground truth t=7 (context) Action-cond.
- Prediction Ground truth (context) Difference GMW (Ours) iVideoGPT Figure 4.
- Qualitative visualization on future state prediction of GWM on F RANKA -P N P and ROBO C ASA.
- All predictions are rolled out by applying the unseen action trajectory from the valid dataset.
