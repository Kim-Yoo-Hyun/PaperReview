# Method

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Diffusion, Transformer
- Paper link: ./2025/ICCV/2025_ICCV_Dita-Scaling-Diffusion-Transformer-for-Generalist-Vision-L/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present Dita, a scalable framework that leverages Transformer architectures to directly denoise continuous action sequences through a unified multimodal diffusion process.
- While recent vision-language-action models trained on diverse robot datasets exhibit promising generalization capabilities with limited in-domain data, their reliance on compact action heads to predict discretized or continuous ...
- Octo & OpenVLA We also reproduce these two opensource VLA models using their released checkpoints, as they employ the same multimodal inputs (language instruction and third-person camera image) ...

## 원리적 동기
- Departing from prior methods that condition denoising on fused embeddings via shallow networks, Dita employs in-context conditioning—enabling fine-grained alignment between denoised actions and raw visual tokens from historical ...
- We present Dita, a scalable framework that leverages Transformer architectures to directly denoise continuous action sequences through a unified multimodal diffusion process.

## 핵심 방법론
- Octo & OpenVLA We also reproduce these two opensource VLA models using their released checkpoints, as they employ the same multimodal inputs (language instruction and third-person camera image) ...
- Method SPATIAL OBJECT GOAL LONG Averge DP* 78.3% 92.5% 68.3% 50.5% 72.4% Octo 78.9% 85.7% 84.6% 51.1% 75.1% OpenVLA 84.9% 88.4% 79.2% 53.7% 76.5% Dita (Ours) 84.2% 96.3% ...
- In this section, we compare our approach with leading generalist policies, including RT-1-X , Octo , and OpenVLA , under both match and variant scenarios.
- It consists of four sub-datasets: LIBERO-SPATIAL, LIBEROOBJECT, LIBERO-GOAL, and LIBERO-100.
- It consists of four distinct scenes (A, B, C, and D) and introduces the ABC↔D evaluation protocol, where models are trained on environments A, B, and C and ...
