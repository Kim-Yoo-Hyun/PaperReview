# Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=4asFznbzJg.
> PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/8cf3760422b9d4505589a97c8f9569e7-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=4asFznbzJg
- Full-text retrieval: https://papers.nips.cc/paper_files/paper/2025/file/8cf3760422b9d4505589a97c8f9569e7-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.를 문제로 두고, In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained VLM while preserving its inherent System 2 ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** While recent foundation policies benefit from the commonsense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency.
- **p. 1 / Abstract - extractive body cue:** To mitigate this dilemma, dual-system approaches have been proposed to leverage a VLM-based System 2 module for handling high-level decision-making, and a separate System 1 ...
- **p. 1 / Abstract - extractive body cue:** However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / 1 Introduction - extractive body cue:** Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- **p. 2 / 1 Introduction - extractive body cue:** While these methods improve execution efficiency, their System 1, as a lightweight separate model, lacks internetscale pretrained knowledge and depends solely on feature representations extracted ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / Abstract - extractive body cue:** This innovative paradigm not only enables high-frequency execution in System 1, but also facilitates coordination between multimodal reasoning and execution components within a single foundation ...
- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 1 / Abstract - extractive body cue:** To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's ...
- **p. 3 / 1 Introduction - extractive body cue:** Our model demonstrates SOTA performance in both single-arm simulation and dual-arm real-world experiments, while maintaining a high execution frequency.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action (a) Previous Dual-system VLA (b) Fast-in-Slow Dual-system ... | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous, Dual-system, VLA | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/action | Most recent end-to-end approaches [22, 23, 24] leverage VLM as System 2 for high-level feature extraction, while appending an additional policy head as System 1 to transform VLM outputs into executable action ... | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Objective/outcome | For the multimodal comprehension component (System 2), we exploit an autoregressive next-token prediction objective to maintain its discrete action generation or high-level language planning capabilities and preserve the overall coheren ... | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / Abstract - extractive body cue:** This innovative paradigm not only enables high-frequency execution in System 1, but also facilitates coordination between multimodal reasoning and execution components within a single foundation ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the ...
- **p. 8 / 4 Experiments - extractive body cue:** FiS-VLA achieves a 73% average success rate with plan-based co-training, outperforming the 69% obtained using discrete actions.
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and inference ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (4 Experiments) |
| Embodiment/environment | Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water Fold towel Mean and place and place at rack blackboard ... | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | In order to fully evaluate our method, we tested on 10 various manipulation tasks in the RLBench [33] benchmark based on the CoppeliaSim simulator, including Close box, Close Laptop, Toilet seat down, ... | role, split, size and leakage | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Metric | Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and reporting the average success rate along with the ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 7 (4 Experiments) |
| Baseline/ablation | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the baseline π0 across eight real-world tasks. On ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** Additional visualizations and failure cases are provided in Appendix C and D, respectively.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality input design in FiS-VLA's dual systems, which ...
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 11: AlphaBot task execution visualization. We visualize key frames of the agent's execution process from a static exterior view. D Failure Case Analysis. Through ...
- **p. 35 / Figure/Table caption - extractive body cue:** Figure 12: Failure case visualization. We visualize the failure cases observed in four real-world experiments, with key error frames during execution highlighted using red bounding ...
- **p. 10 / A B - extractive body cue:** We hypothesize that enabling dynamic adaptation of these factors based on task demands and environmental complexity could lead to a more robust and generalizable model, ...
- **p. 7 / 4 Experiments - extractive body cue:** In particular, FiS-VLA achieves superior performance on 8 out of 10 tasks, highlighting the robustness of its action generation capabilities.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.를 문제로 두고, In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained VLM while preserving its inherent System 2 ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
