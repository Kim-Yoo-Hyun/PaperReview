# Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Diffusion, VLA, Planning
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not progressive step-wise prompts, but implicitly contain sever ...를 문제로 두고, The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into coherent subgoal images in a chain-ofthought manner ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotics agents often struggle to understand and follow the multi-modal prompts in complex manipulation scenes which are challenging to be sufficiently and accurately described by ...
- **p. 1 / Abstract - extractive body cue:** Moreover, for long-horizon manipulation tasks, the deviation from general instruction tends to accumulate if lack of intermediate guidance from high-level subgoals.
- **p. 1 / Abstract - extractive body cue:** For this, we consider can we generate subgoal images before act to enhance the instruction following in long-horizon manipulation with multi-modal prompts?
- **p. 1 / Abstract - extractive body cue:** Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model ...
- **p. 1 / Abstract - extractive body cue:** We design a semantic alignment module that can anchor the progress of generated keyframes along a coherent generation chain, unlocking the chain-of-thought reasoning ability of ...
- **p. 1 / 1. Introduction - extractive body cue:** However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not progressive step-wise prompts, ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the compounding small errors over long horizons will lead to catastrophic deviations from the original task instructions due to the lack of intermediate guidance ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into ...
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Thus, we propose a two-stage coarse-to-fine approach decoupling semantic alignment pretraining from diffusion model finetuning, illustrated in Fig.
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned to the prompts.
- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive body cue:** Here we propose bi-directional aligned generation, where the aligned token zi align not only guides forward prediction but also reconstructs the current frame through backward ...
- **p. 4 / 3.1. Pipeline Overview - extractive body cue:** Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and foundation model F ...
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The final component in our framework is the low-level policy model for action planning, generating an action trajectory ⌧i a when given observation trajectory ⌧i ...
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the generated subgoal image ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the generated subgoal image gi: ⌧i a = {ai,t}T t=1 ⇠QT ... | image/video, language instruction, proprioception과 history | p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview) |
| State/latent | policy, model, parameterized, image-conditioned, planner, infers, action, given, current, observation, generated, subgoal | language-grounded task state와 action-policy context | p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview) |
| Output/action | Given the initial observation x0 and a multi-modal prompt P as task instruction potentially needs to be reached by N subgoal steps, robots are required to learn a policy conditioned on the ... | continuous action, pose 또는 action chunk | p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview), p. 3 (3.1. Pipeline Overview) |
| Objective/outcome | The training objective can be formulated as: L = Exi2D[k ˆxi -E ⇣ xi-1, zi align , P) / {z } Forward Generation k+kˆxi-1 -E ⇣ xi, zi align, P) / {z ... | instruction following, task success, generalization과 latency | p. 5 (3.3. Fine-grained Diffusion Training), p. 5 (3.3. Fine-grained Diffusion Training), p. 6 (3.4. Goal-conditioned Policy Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into ...
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Thus, we propose a two-stage coarse-to-fine approach decoupling semantic alignment pretraining from diffusion model finetuning, illustrated in Fig.
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned to the prompts.
- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive body cue:** Here we propose bi-directional aligned generation, where the aligned token zi align not only guides forward prediction but also reconstructs the current frame through backward ...
- **p. 6 / 4.3. Quantitative Results of Success Rate - extractive body cue:** 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate.
- **p. 7 / 4.4. Further Analysis - extractive body cue:** 3 shows, CoTDiffusion still achieves much better fidelity than SuSIE even though SuSIE has got improved after fine-tuning on the same datasets in VIMABENCH.
- **p. 8 / 4.4. Further Analysis - extractive body cue:** CoTDiffusion achieves outstanding gain in the zero-shot performance of combinatorial tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.4. Further Analysis) |
| Embodiment/environment | Benchmark & Tasks We conduct evaluation on VIMABENCH, a benchmark suite for multimodal robot learning, which is built on the Ravens robot simulator [50]. | hardware/simulator version and reset protocol | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Dataset/benchmark | Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks. | role, split, size and leakage | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis) |
| Metric | Gato and Flamingo gets low success rates on longhorizon tasks without explicit subgoal generation to correct the accumulative deviation errors from the instructions. | definition, denominator, direction and uncertainty | p. 7 (4.3. Quantitative Results of Success Rate), p. 6 (4.1. Experiment Setup), p. 6 (4.3. Quantitative Results of Success Rate) |
| Baseline/ablation | 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | fair input/data/compute/action matching | p. 6 (4.3. Quantitative Results of Success Rate), p. 6 (4.2. Baselines), p. 7 (4.4. Further Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Incorporating commonsense knowledge from pre-trained MLLM like GPT-4V provides an avenue for more generalizable and promising reasoning in CoTDiffusion, which leaves as our future work.
- **p. 7 / 4.4. Further Analysis - extractive body cue:** Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits.
- **p. 7 / 4.4. Further Analysis - extractive body cue:** Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not progressive step-wise prompts, but implicitly contain sever ...를 문제로 두고, The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into coherent subgoal images in a chain-ofthought manner ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
