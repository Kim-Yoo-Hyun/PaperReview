# AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, active perception, visual attention, POMDP, recurrent state, long-horizon
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.를 문제로 두고, Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep.
- **p. 1 / Abstract - extractive body cue:** This history-agnostic design treats robot manipulation as a Markov Decision Process, even though realworld robotic control is inherently partially observable and requires reasoning over past ...
- **p. 1 / Abstract - extractive body cue:** To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action ...
- **p. 1 / Abstract - extractive body cue:** Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dualarm manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 1 / 1. Introduction - extractive body cue:** (b) Qualitative comparison of visual focus from two viewpoints while executing the task "turn on the stove and put the moka pot on it." The ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** To our knowledge, it is the first VLA framework to explicitly address this limitation via a POMDP-inspired approach. • We introduce an Active Visual Attention ...
- **p. 3 / 3. Methods - extractive body cue:** In this section, we present our proposed VLA method.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** For simplicity, our framework is built upon the OpenVLA-OFT foundation model.
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which modulate the visual ...
- **p. 3 / 3.2. AVA-VLA Framework - extractive body cue:** To utilize the recurrent state, we introduce the active visual attention module by quantifying the importance of visual tokens and dynamically modulating the processing of ...
- **p. 5 / 3.3. Active Visual Attention - extractive body cue:** Therefore, the proposed AVA module uses the recurrent state and current visual observation to calculate soft weights to guide the VLA model to filter and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In a POMDP framework, the optimal policy at timestep t should be conditioned not only on the current observation xt but also on a belief state bt-1, which captures all relevant historical ... | image/video, language instruction, proprioception과 history | p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries) |
| State/latent | POMDP, framework, optimal, policy, timestep, should, conditioned, only, current, observation, belief, state | language-grounded task state와 action-policy context | p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework) |
| Output/action | (1) Recent representative VLA models, such as OpenVLAOFT [20] and its variant [23], map the output hidden states into an executable action chunk At = [at 0, at 1, ..., at Lc-1] ... | continuous action, pose 또는 action chunk | p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework), p. 4 (3.2. AVA-VLA Framework) |
| Objective/outcome | However, given the substantial memory constraint and computational cost of modern VLA backbones, performing the full backpropagation through time is computationally prohibitive [34]. | instruction following, task success, generalization과 latency | p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** To our knowledge, it is the first VLA framework to explicitly address this limitation via a POMDP-inspired approach. • We introduce an Active Visual Attention ...
- **p. 3 / 3. Methods - extractive body cue:** In this section, we present our proposed VLA method.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** For simplicity, our framework is built upon the OpenVLA-OFT foundation model.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance.
- **p. 7 / 4.2. Evaluation Results - extractive body cue:** Results demonstrate that the proposed AVA-VLA framework achieves state-of-the-art overall performance in both singletask and multi-task settings.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The results are reported in terms of success rates (%) and average length.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results) |
| Embodiment/environment | We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world tablemounted Mobile ALOHA robot with four test tasks, to validate ... | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Dataset/benchmark | We use a stationary cobot magic dual-arm robot to assess our model's adaptability to novel real-world environments with a small number of robot demonstrations. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Metric | We use widely adopted performance evaluation metrics "Success Rate (SR)" (the same 13458 | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation Studies) |
| Baseline/ablation | The results show that the proposed AVA-VLA framework comprehensively outperforms baseline methods across all tasks. | fair input/data/compute/action matching | p. 7 (4.2. Evaluation Results), p. 7 (4.2. Evaluation Results), p. 8 (4.4. Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Analysis - extractive body cue:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while executing ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Due to space limitations, implementation details are provided in Appendix A.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** LIBERO+ [11] is a challenging LIBERO-based benchmark, which offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions.
- **p. 7 / 4.2. Evaluation Results - extractive body cue:** The results demonstrate that the proposed model possesses robust semantic understanding and dexterous action capabilities after training.
- **p. 8 / 4.4. Analysis - extractive body cue:** The results reported in Table 5, demonstrate the robustness of our method: the model suffers only a negligible drop in performance after pruning.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.를 문제로 두고, Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models. (p. 2, 1. Introduction).
- **Actual contribution:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models. (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 3. Comparison on the Mobile ALOHA real-world experiments. Evaluation across four manipulation tasks, including (a) Pick and Place, (b) Sequenced Instruction Understanding, (c) Flexible Object Folding, (d) Dexterous Action. ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a robust and spatially consistent focus ... (p. 8, 4.4. Analysis).
