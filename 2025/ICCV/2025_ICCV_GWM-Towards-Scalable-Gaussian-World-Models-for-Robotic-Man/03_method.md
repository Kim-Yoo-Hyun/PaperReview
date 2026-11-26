# Method - GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. World State Encoding), p. 5 (3.3. GWM for Policy Learning), p. 3 (3.1. World State Encoding), p. 4 (3.1. World State Encoding), p. 5 (3.3. GWM for Policy Learning), p. 3 (3. Gaussian World Model)): The 3D variational encoder embeds the Gaussian Splats estimated by a foundational reconstruction model to a compact latent space, and the diffusion transformer operates on the latent patches to interactively ...

## Method Body Digest

- **p. 4 / 3.1. World State Encoding - extractive body cue:** The 3D variational encoder embeds the Gaussian Splats estimated by a foundational reconstruction model to a compact latent space, and the diffusion transformer operates on ...
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** Specifically, we use the feature vector after the first denoising step in the diffusion process as the input for downstream policy models like BCtransformer [59] ...
- **p. 3 / 3.1. World State Encoding - extractive body cue:** Next, we use these sampled Gaussians GN as queries to attend and aggregate information from all Gaussians G to latent embedding x using a L ...
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer.
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** GWM for Imitation Learning In imitation learning, we use GWM as a more effective encoder to provide better features for policy learning.
- **p. 3 / 3. Gaussian World Model - extractive body cue:** 3.1) and leverage a diffusion-based conditional generative model to learn the dynamics over representations given robot states and actions (Sec.
- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** The superior performance stems from GWM's 3D Gaussian representation, which allows more accurate prediction of contact dynamics and object movement under manipulation, compared to purely ...
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** The goal of model-based RL [31] is to learn a policy π that maximizes the expected sum of discounted rewards π∗ = arg maxπ Eπ ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose Gaussian World Model (GWM), a novel 3D world model that integrates 3D-GS with high-capacity generative models for robotic manipulation.
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer.

## Source Evidence Cues

- **p. 4 / 3.1. World State Encoding - extractive body cue:** The 3D variational encoder embeds the Gaussian Splats estimated by a foundational reconstruction model to a compact latent space, and the diffusion transformer operates on ...
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** Specifically, we use the feature vector after the first denoising step in the diffusion process as the input for downstream policy models like BCtransformer [59] ...
- **p. 3 / 3.1. World State Encoding - extractive body cue:** Next, we use these sampled Gaussians GN as queries to attend and aggregate information from all Gaussians G to latent embedding x using a L ...
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer.
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** GWM for Imitation Learning In imitation learning, we use GWM as a more effective encoder to provide better features for policy learning.
- **p. 3 / 3. Gaussian World Model - extractive body cue:** 3.1) and leverage a diffusion-based conditional generative model to learn the dynamics over representations given robot states and actions (Sec.
- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** The superior performance stems from GWM's 3D Gaussian representation, which allows more accurate prediction of contact dynamics and object movement under manipulation, compared to purely ...
- **Detected method headings:** 3. Gaussian World Model (p. 3); 3.2. Diffusion-based Dynamics Modeling (p. 4); 3.3. GWM for Policy Learning (p. 5); 2. Does Gaussian world model benefits downstream imita (p. 5)

## Pipeline

한두 시점 RGB에서 얻은 장면 표현과 로봇 행동 이력 → 3D 가우시안 집합을 압축한 잠재 상태 → 예측한 다음 장면 상태와 렌더링 영상. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** The goal of model-based RL [31] is to learn a policy π that maximizes the expected sum of discounted rewards π∗ = arg maxπ Eπ ...
- **p. 4 / 3.2. Diffusion-based Dynamics Modeling - extractive body cue:** (6) using the reverse-time SDE [2] for sampling: \ label { e q:rever se_ process} d\rvx = [\mathbf {f} (\rvx , \tau ) - g(\tau ...
- **p. 5 / 3.2. Diffusion-based Dynamics Modeling - extractive body cue:** Algorithm 1: Monotonic Model-Based Policy Optimization (MBPO) with Gaussian World Model Initialize policy π(at/st), Gaussian world model pθ(st+1, rt/st, at), empty replay buffer B; for ...
- **p. 4 / 3.2. Diffusion-based Dynamics Modeling - extractive body cue:** With this conversion, we can rewrite the objective in Eq.
- **p. 3 / 3.1. World State Encoding - extractive body cue:** Since vanilla 3D-GS relies on time-consuming per-scene offline optimization, we employ generalizable 3D-GS to learn feed-forward mappings from images to 3D Gaussians to accelerate the ...
- **p. 8 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** FRANKA-PNP Diffusion Policy GWM (Ours) Cup distractor 6/10 7/10 Plate distractor 1/5 3/5 Table distractor 0/5 3/5 Total 7/20 13/20 explicit 3D representation offers substantial ...
- **Formal bridge:** 한두 시점 RGB에서 얻은 장면 표현과 로봇 행동 이력 → 3D 가우시안 집합을 압축한 잠재 상태 → 예측한 다음 장면 상태와 렌더링 영상.
- **Equation/algorithm anchors:** p. 4 (3.2. Diffusion-based Dynamics Modeling), p. 4 (3.1. World State Encoding), p. 5 (3.2. Diffusion-based Dynamics Modeling).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Feed-forward, Gaussian, Splatting, Given, single, two-view, image, inputs, world, state, goal, first, encode, scene | 한두 시점 RGB에서 얻은 장면 표현과 로봇 행동 이력 | body cue; exact tensor/frame verify |
| State/latent | Feed-forward, Gaussian, Splatting, Given, single, two-view, image, inputs, world, state | 3D 가우시안 집합을 압축한 잠재 상태 | body cue; notation verify |
| Action/output | summary, main, contributions, threefold, introduce, GWM, novel, world, model, instantiated | 예측한 다음 장면 상태와 렌더링 영상 | body cue; unit/decoder verify |
| Objective/constraint | goal, model-based, learn, policy, maximizes, expected, discounted, rewards, while, constructing | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. World State Encoding - extractive body cue:** Feed-forward 3D Gaussian Splatting Given single or two-view image inputs I = {I}i={1,2} of a world state, our goal is to first encode the scene ...
- **p. 3 / 3.1. World State Encoding - extractive body cue:** Specifically, we obtain the 3D Gaussian world state G using Splatt3R [70], which first employs the stereo reconstruction model Mast3R [37] to generate 3D point ...
- **p. 6 / 4.2. GWM-based Imitation Learning - extractive body cue:** The task suite in ROBOCASA comprises 24 atomic tasks with related language instructions for kitchen environments, including actions such as pick-and-place, open, and close.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, our approach combines recent advancements in feed-forward 3D-GS reconstruction with Diffusion Transformers (DiTs), enabling fine-grained future scene reconstruction through Gaussian rendering conditioned on current ...
- **p. 4 / 3.2. Diffusion-based Dynamics Modeling - extractive body cue:** With the encoded world state embeddings xt at time t and its future state xt+1, we aim to learn the world dynamics p(xt+1/x≤t, a≤t), where ...
- **p. 4 / 3.2. Diffusion-based Dynamics Modeling - extractive body cue:** Specifically, we leverage a diffusion-based dynamics model where we convert dynamics learning into a conditional generation problem, generating future state xt+1 from noise with history ...
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** S and A are the state and action spaces, γ is the discount factor, and r(s, a) is the reward function.
- **Normalized interface:** observation=한두 시점 RGB에서 얻은 장면 표현과 로봇 행동 이력; state=3D 가우시안 집합을 압축한 잠재 상태; output/action=예측한 다음 장면 상태와 렌더링 영상.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | The 3D variational encoder embeds the Gaussian Splats estimated by a foundational reconstruction model to a compact latent space, and the diffusion ... | episode/sequence/action-chunk boundary |
| Rate / latency | While PSNR shows a slight decrease, both SSIM and LPIPS metrics improve, suggesting that Gaussian Splatting provides better 3D consistency across different ... | Hz/fps, inference time and control rate |
| Memory | not recovered | window and reset |
| Compute | For fair comparisons, all compared methods use the same context length, horizon, and are trained to a maximum of 1 × 105 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** For fair comparisons, all compared methods use the same context length, horizon, and are trained to a maximum of 1 × 105 steps.

## Method-Specific Formal Details

- **Body-defined terms:** variational, encoder, embeds, Gaussian, Splats, estimated, foundational, reconstruction, model, compact, latent, space, diffusion, transformer, operates, patches, interactively, imagine, future, conditioned.
- **Relevant PDF headings:** 3. Gaussian World Model (p. 3); 3.2. Diffusion-based Dynamics Modeling (p. 4); 3.3. GWM for Policy Learning (p. 5); 2. Does Gaussian world model benefits downstream imita (p. 5).

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches. | p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis) |
| 원문 대조 | Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| 원문 대조 | Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with ... | p. 8 (4.5. Ablation Analysis), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation Study on PnP CabToCounter in ROBO- CASA task suite. We report the reconstruction metrics and the suc- cess rates (SR) of imitation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Real-World Experiment Setup. Left: using a Franka Emika Panda robotic arm equipped with an RGB camera, we eval- uate the performance of the ...
- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we introduce a novel Gaussian World Model (GWM) for robotic manipulation that addresses limitations of image-based world models by incorporating robust geometric ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Gaussian World Model (GWM) is a novel branch of world model that predicts dynamic future states and enables robotic manipulation based on the ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. World State Encoding), p. 5 (3.3. GWM for Policy Learning), p. 3 (3.1. World State Encoding), p. 4 (3.1. World State Encoding), p. 5 (3.3. GWM for Policy Learning), p. 3 (3. Gaussian World Model), objective p. 5 (3.3. GWM for Policy Learning), p. 4 (3.2. Diffusion-based Dynamics Modeling), p. 5 (3.2. Diffusion-based Dynamics Modeling), p. 4 (3.2. Diffusion-based Dynamics Modeling), p. 3 (3.1. World State Encoding), p. 8 (4.3. GWM-based Reinforcement Learning), temporal p. 4 (3.1. World State Encoding), p. 8 (4.5. Ablation Analysis), p. 5 (3.2. Diffusion-based Dynamics Modeling), p. 7 (4.3. GWM-based Reinforcement Learning), p. 2 (1. Introduction), p. 2 (1. Introduction).
