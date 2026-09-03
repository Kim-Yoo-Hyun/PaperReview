# Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Diffusion, Transformer
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, the expansive robot space within large-scale cross-embodiment datasets, encompassing diverse camera views and action spaces, presents a substantial challenge for a tiny diffusion head to effectively denoise continuous actions.를 문제로 두고, In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, 32, 54, 72], thereby ensuring scalability across extensive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While recent vision-language-action models trained on diverse robot datasets exhibit promising generalization capabilities with limited in-domain data, their reliance on compact action heads to predict ...
- **p. 1 / Abstract - extractive body cue:** We present Dita, a scalable framework that leverages Transformer architectures to directly denoise continuous action sequences through a unified multimodal diffusion process.
- **p. 1 / Abstract - extractive body cue:** Departing from prior methods that condition denoising on fused embeddings via shallow networks, Dita employs in-context conditioning-enabling fine-grained alignment between denoised actions and raw visual ...
- **p. 1 / Abstract - extractive body cue:** This design explicitly models action deltas and environmental nuances.
- **p. 1 / Abstract - extractive body cue:** This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** However, the expansive robot space within large-scale cross-embodiment datasets, encompassing diverse camera views and action spaces, presents a substantial challenge for a tiny diffusion head ...
- **p. 2 / 1. Introduction - extractive body cue:** Conventional robot learning paradigms typically depend on large-scale data collected for specific robots and tasks, yet the acquisition of data for generalized tasks remains both ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, 32, ...
- **p. 3 / 3. Method - extractive body cue:** Finally, we present the data and implementation specifics for the pretraining of our model.
- **p. 3 / 3.1. Architecture - extractive body cue:** This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced ...
- **p. 2 / 1. Introduction - extractive body cue:** This achievement implies that a universal robotic policy, pretrained on heterogeneous robotic data and finetuned with minimal supervision, could be instrumental in realizing true generalization ...
- **p. 3 / 3. Method - extractive body cue:** We then define the training objective for generating multi-modal actions.
- **p. 4 / 3.1. Architecture - extractive body cue:** The instruction tokens, image features, timestep embeddings, and noised action are concatenated to construct a token sequence, which is then fed into the network to ...
- **p. 4 / 3.1. Architecture - extractive body cue:** Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In pursuit of a unified robotic policy, recent studies have directly mapped visual observations and language instructions to actions using expansive VLA models for navigation [65, 66] or manipulation [8, 9, 32, ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| State/latent | pursuit, unified, robotic, policy, recent, studies, have, directly, mapped, visual, observations, language | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (3.1. Architecture) |
| Output/action | Remarkably, this promising performance is achieved exclusively with a single third-person camera input, while the model's inherent flexibility affords researchers the freedom to integrate additional input modalities (e.g., wrist-camera ... | continuous action, pose 또는 action chunk | p. 3 (1. Introduction), p. 3 (3.1. Architecture), p. 4 (3.2. Training Objective) |
| Objective/outcome | The optimization objective of Dita is to minimize the mean squared error (MSE) loss between xt and ˆxt. | instruction following, task success, generalization과 latency | p. 4 (3.2. Training Objective), p. 3 (3. Method), p. 3 (3.1. Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, 32, ...
- **p. 3 / 3. Method - extractive body cue:** Finally, we present the data and implementation specifics for the pretraining of our model.
- **p. 3 / 3.1. Architecture - extractive body cue:** This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced ...
- **p. 2 / 1. Introduction - extractive body cue:** This achievement implies that a universal robotic policy, pretrained on heterogeneous robotic data and finetuned with minimal supervision, could be instrumental in realizing true generalization ...
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive body cue:** Overall, Dita achieves a 63.8% success rate on two-step 7692
- **p. 5 / 4.1. Baselines - extractive body cue:** Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]).
- **p. 5 / 4.4. CALVIN - extractive body cue:** Without whistles and bells, the proposed Dita achieves comparable performance among methods relying solely on a single RGB camera for observation.
- **p. 6 / 4.6. Ablation Study - extractive body cue:** When the trajectory length is 32, Dita with 2-frame observations achieves superior performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.1. Real-Robot Task Finetuning), p. 5 (4.1. Baselines) |
| Embodiment/environment | The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from extensive, real-world pretraining datase ... | hardware/simulator version and reset protocol | p. 6 (4.4. CALVIN), p. 4 (4. Simulation Experiments) |
| Dataset/benchmark | To assess the capabilities of the pretrained model, we conduct evaluations across four simulation benchmarks in this section: 1) SimplerEnv [37] (Google Robot) demonstrates the model's zero-shot adaptation to simulation environments; 2) ... | role, split, size and leakage | p. 6 (4.4. CALVIN), p. 4 (4. Simulation Experiments), p. 4 (4. Simulation Experiments), p. 5 (4.3. LIBERO) |
| Metric | Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]). | definition, denominator, direction and uncertainty | p. 5 (4.1. Baselines), p. 5 (4.3. LIBERO), p. 6 (4.6. Ablation Study) |
| Baseline/ablation | We also implement RT-1 [8] style baseline model EDisc ω↑s with an architecture similar to ours for comparison. | fair input/data/compute/action matching | p. 6 (4.4. CALVIN), p. 6 (4.4. CALVIN), p. 7 (5.1. Real-Robot Task Finetuning) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.1. Real-Robot Task Finetuning - extractive body cue:** Failures are highlighted with red circles.
- **p. 8 / 5.1. Real-Robot Task Finetuning - extractive body cue:** For long-horizon tasks, OpenVLA effectively completes the first task but fails to handle the longhorizon task, such as completely misunderstanding the insert operation.
- **p. 5 / 4.4. CALVIN - extractive body cue:** Dita does not utilize the play data which provides external trajectory data compared to the labeled data, while GR-MG uses it for training the policy.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot adaptation ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Illustrations of different generalist robot policy architec- tures. Left head: the common robot Transformer architecture with discretization actions, e.g., Robot Transformer [8, 9] ...
- **p. 4 / 4. Simulation Experiments - extractive body cue:** We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in unseen ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens. The DinoV2 [53] model encodes image ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, the expansive robot space within large-scale cross-embodiment datasets, encompassing diverse camera views and action spaces, presents a substantial challenge for a tiny diffusion head to effectively denoise continuous actions.를 문제로 두고, In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, 32, 54, 72], thereby ensuring scalability across extensive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Architecture), p. 3 (3. Method), p. 4 (3.1. Architecture), p. 4 (3.1. Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
