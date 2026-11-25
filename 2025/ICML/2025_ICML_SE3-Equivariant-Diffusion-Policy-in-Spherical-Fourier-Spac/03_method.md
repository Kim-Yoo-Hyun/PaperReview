# Method - SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v267/zhu25u.html; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167962. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal), p. 5 (4.4. Spherical FiLM Conditioning Layer), p. 5 (4.2. Representing State and Action by Spherical Signal), p. 6 (4.4. Spherical FiLM Conditioning Layer)): We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature enc(S) = C, and then ii) ...

## Method Body Digest

- **p. 4 / 4.1. Method Overview - extractive body cue:** We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature enc(S) ...
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 5 / 4.4. Spherical FiLM Conditioning Layer - extractive body cue:** We propose equivariant spherical FiLM (SFiLM) layers to extend the Feature-wise Linear Modulation (FiLM) layer (Perez et al., 2018) used by Diffuser (Janner et al., ...
- **p. 5 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** The robot state e is concatenated to the output of the encoder yielding C.
- **원문 대조:** Spherical FiLM은 입력 feature와 conditioning feature를 Wigner D(g)로 회전시켰을 때 출력도 같은 변환을 따르는 SO(3) equivariance를 만족한다. 식 (6)은 이 교환 관계이며 증명은 Appendix A.2를 참조한다. ([PDF p. 6](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25u/zhu25u.pdf#page=6), §4.4, Eq. (6)).
- **p. 5 / 4.3. Spherical Denoising Temporal U-net - extractive body cue:** The mixing channel temporal convolution in Equation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** There are several advantages of using spherical Fourier features as latent features.
- **p. 4 / 4.1. Method Overview - extractive body cue:** The Spherical Diffusion Policy model maps observations to actions π(S) = A.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method is light and SE(3) equivariant across multiple objects, allowing it to perform more complicated tasks with less engineering.

## Source Evidence Cues

- **p. 4 / 4.1. Method Overview - extractive body cue:** We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature enc(S) ...
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 5 / 4.4. Spherical FiLM Conditioning Layer - extractive body cue:** We propose equivariant spherical FiLM (SFiLM) layers to extend the Feature-wise Linear Modulation (FiLM) layer (Perez et al., 2018) used by Diffuser (Janner et al., ...
- **p. 5 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** The robot state e is concatenated to the output of the encoder yielding C.
- **원문 대조:** Spherical FiLM은 입력 feature와 conditioning feature를 Wigner D(g)로 회전시켰을 때 출력도 같은 변환을 따르는 SO(3) equivariance를 만족한다. 식 (6)은 이 교환 관계이며 증명은 Appendix A.2를 참조한다. ([PDF p. 6](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25u/zhu25u.pdf#page=6), §4.4, Eq. (6)).
- **Detected method headings:** 4. Method (p. 4); 4.1. Method Overview (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical ... | p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In this section, we propose a spherical representation of the state and action for the policy. | p. 4 (4.2. Representing State and Action by Spherical Signal), p. 5 (4.4. Spherical FiLM Conditioning Layer) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We propose equivariant spherical FiLM (SFiLM) layers to extend the Feature-wise Linear Modulation (FiLM) layer (Perez et al., 2018) used by Diffuser ... | p. 5 (4.4. Spherical FiLM Conditioning Layer), p. 5 (4.2. Representing State and Action by Spherical Signal) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Spherical Denoising Temporal U-net - extractive body cue:** The mixing channel temporal convolution in Equation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** There are several advantages of using spherical Fourier features as latent features.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4.3. Spherical Denoising Temporal U-net).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | section, spherical, representation, state, action, policy, Diffusion, model, maps, observations, actions, states, consist, camera | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | section, spherical, representation, state, action, policy, Diffusion, model, maps, observations | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, novel, Spherical, Diffusion, Policy, equivariant, rotations, invariant, translations, enabling | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | mixing, channel, temporal, convolution, Equation, There, several, advantages, spherical, Fourier | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 4 / 4.1. Method Overview - extractive body cue:** The Spherical Diffusion Policy model maps observations to actions π(S) = A.
- **p. 2 / 2. Background - extractive body cue:** The states s consist of camera observation o, e.g. images or voxels or point clouds, and the end-effector's 6DoF pose (3D translation and 3D rotation) ...
- **p. 2 / 2. Background - extractive body cue:** The policy takes an input a history of h states St = [st, st-1, . . . , st-h+1].
- **p. 5 / 4.3. Spherical Denoising Temporal U-net - extractive body cue:** This equivariance is enforced by mixing channel temporal convolution on each degree l of the spherical Fourier coefficient: ho l,m,t = r X j=0 X ...
- **p. 5 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** The robot state e is concatenated to the output of the encoder yielding C.
- **p. 1 / 1. Introduction - extractive body cue:** SDP achieves translational invariance by formulating states and actions in the gripper frame (Chi et al., 2024).
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Specifically, we use an equivariant conditional denoising function ϵθ(S, A + ϵk, k) to estimate the noise for a noisy action A ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

## Method-Specific Formal Details

- **Body-defined terms:** model, three, components, Figure, spherical, encoder, embeds, state, multichannel, scene, feature, then, denoising, temporal, Unet, SDTU, estimates, noise, noisy, action.
- **Relevant PDF headings:** 4. Method (p. 4); 4.1. Method Overview (p. 4).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly ... | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments) |
| Action / skill decoding | Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 tasks, except for Coffee and Coffee ... | p. 6 (5.1. Simulation Experiments), p. 6 (5.1. Simulation Experiments) |
| Receding execution / feedback | Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines. | p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** 3) EquiBot (Yang et al., 2024a) - an SO(3)-equivariant diffusion policy with up to degree l = 1 representations.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We compare several baselines in our experiments: 1) EquiDiff (Wang et al., 2024b) - an SO(2)-equivariant diffusion policy using either voxel or RGB image observations.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SDP enforces that the policy is SO(3) equivariant. Specifically, in the second row, an SO(3) rotation that is applied to the scene leads ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising step ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study. The relative action space and the spherical representation are critical for the SE(3) generalization, while the latter one is more important. ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, such as these in the Push Eraser ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal), p. 5 (4.4. Spherical FiLM Conditioning Layer), p. 5 (4.2. Representing State and Action by Spherical Signal), p. 6 (4.4. Spherical FiLM Conditioning Layer), objective p. 5 (4.3. Spherical Denoising Temporal U-net), p. 4 (4.2. Representing State and Action by Spherical Signal), temporal p. 4 (4.1. Method Overview), p. 4 (4.1. Method Overview), p. 5 (4.3. Spherical Denoising Temporal U-net), p. 5 (4.3. Spherical Denoising Temporal U-net), p. 6 (5.2. Physical Experiments), p. 6 (5.1. Simulation Experiments).
