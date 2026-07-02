# Method

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_On-Device-Diffusion-Transformer-Policy-for-Efficient-Robot/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model’s postpruning recoverability explicitly.
- In this paper, we propose LightDP, a novel framework specifically designed to accelerate Diffusion Policies for real-time deployment on mobile devices.
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.

## 원리적 동기
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures involve billions of parameters, leading ...
- To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model’s postpruning recoverability explicitly.

## 핵심 방법론
- Depth Param (M) NFE GFLOPs Inference Speed (ms) Success Rate DP-T DP-T⋆ 8 8.97 100 4.39 90.6 0.772±0.039 0.754±0.023 DP-T-D6/6-8 DP-T-D6/4-4 6 6.87 4 0.134 4.79 0.752±0.019 0.732±0.034 ...
- Performance comparison of LightDP compressed models with varying depth and inference steps.
- All models are trained on the same Push-T dataset for 3K epochs.
- DP-T⋆ refers to the baseline model evaluated by us.
- DP-T-DL/N -M indicates that L blocks are retained during the pruning process, with a local block scheme of N :M .
