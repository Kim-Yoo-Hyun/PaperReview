# CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p072.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p072.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, language grounding, code generation, 3D attention, diffusion policy, contact-rich manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p072.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p072.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, imposing an additional axis of multi-modality in ...를 문제로 두고, In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an intermediate representation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Natural language instructions for robotic manipula tion tasks often exhibit ambiguity and vagueness.
- **p. 1 / Abstract - extractive body cue:** For instance, the instruction "Hang a mug on the mug tree" may Involve
- **p. 1 / Abstract - extractive body cue:** ‘and low-level action genera ptimal performance due 10
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language.
- **p. 1 / Abstract - extractive body cue:** This framework employs a Vision-Language Model (VIM) to interpret abstract concepts in natural language instructions and generates task-specific code - an interpretable and executable intermediate ...
- **p. 3 / A. Problem Statement - extractive body cue:** For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, ...
- **p. 3 / A. Problem Statement - extractive body cue:** Notably, we show in Section IV-B that the current state-of the-art methods can fail to achieve a high success rate even with extensive training demonstrations

## Core Idea

- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an ...
- **p. 4 / A. Problem Statement - extractive body cue:** CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We frst evaluate our method by varying the number of demonstrations on the Pack Bat.tezy task in simulation, as shown in Figure 7 (a).
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Our method effectively, leverages the powerful visualsemantic understanding capabilities of VLMs and benefits from explicit spatial relation reasoning using 3D representations.
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** For the simulation experiments, we compare our method against the following baselines:
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In this section, we investigate whether 3D attention is a suitable representation for visuomotor policy learning and evaluate the pipeline from 3D attention maps to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | [ plalz = =)p(= = z1lor,2), Where 2 is a task-relevant latent representation of the state such that p(ajo,l,2 = =) = plalz = =). ie, 2% contains enough information about the ... | image/video, language instruction, proprioception과 history | p. 3 (A. Problem Statement), p. 4 (A. Problem Statement) |
| State/latent | plalz, z1lor, Where, task-relevant, latent, representation, state, contains, enough, information, about, observation | language-grounded task state와 action-policy context | p. 3 (A. Problem Statement), p. 4 (A. Problem Statement), p. 3 (A. Problem Statement) |
| Output/action | In Section II-C, we describe the API provided to the code generation process used to construct our state representation 44, 3D attention map that highlights task-relevant regions Finally, this 3D attention map ... | continuous action, pose 또는 action chunk | p. 4 (A. Problem Statement), p. 3 (A. Problem Statement), p. 6 (B. Analysis of Existing Imitation Learning Algorithm) |
| Objective/outcome | While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus as the number of demonstrations further increases, ... | instruction following, task success, generalization과 latency | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |

## Main Claims and Actual Contribution

- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an ...
- **p. 4 / A. Problem Statement - extractive body cue:** CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We frst evaluate our method by varying the number of demonstrations on the Pack Bat.tezy task in simulation, as shown in Figure 7 (a).
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Our method effectively, leverages the powerful visualsemantic understanding capabilities of VLMs and benefits from explicit spatial relation reasoning using 3D representations.
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** For the simulation experiments, we compare our method against the following baselines:
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus ...
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In ‘contrast to Lang-DP (RGB), our method, which incorporates 2 similar pipeline from language instructions to 2D attention, achieves a performance improvement from 12% to ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For simple tasks with no ambiguity (Lop-left entry), the high success rate confirms the validity of the baseline methods.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| Embodiment/environment | and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in handling language ambiguity. | hardware/simulator version and reset protocol | p. 2 (3) We conduct extensive evaluations of individual modules), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | In addition, we build a benchmark in the simulation to quantitatively evaluate the language-to-3D attention pipeline, which ‘can automatically generate scenes, prompts, and corresponding ground truth 3D attention maps. | role, split, size and leakage | p. 2 (3) We conduct extensive evaluations of individual modules), p. 5 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 5 (IV. EXPERIMENTS) |
| Metric | Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ... | definition, denominator, direction and uncertainty | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Baseline/ablation | We find that our policy consistently outperforms the baselines by leveraging VLMgenerated code as an interpretable and executable intermediate representation, effectively utilizing the visual-semantic reasoning capabilites of the VLM. | fair input/data/compute/action matching | p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ...
- **p. 9 / V. ConcLusion - extractive body cue:** In our experiments, we first identify the key limitations of existing imitation learning algorithms.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (b) Failure Breakdown of Two Special Scenarios
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure primarily occurs at the task stage with the highest ambiguity, demonstrating a strong cconrelation between policy failure and task ambiguity.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Additional analysis and visualizations of 3D attention failure cases are provided in the
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we analyze the common failure cases of our ‘method, as shown in Figure 9.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 9: System Failure Breakdown. We categorize the failure patterns in the real-world experiments into code generation failures, perception failures, and execution failures. Our results ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, imposing an additional axis of multi-modality in ...를 문제로 두고, In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an intermediate representation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (A. Problem Statement), p. 3 (A. Problem Statement), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
