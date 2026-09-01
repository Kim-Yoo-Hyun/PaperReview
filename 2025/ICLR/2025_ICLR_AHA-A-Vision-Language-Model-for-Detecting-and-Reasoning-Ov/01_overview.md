# AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=JVkdSi7Ekg.
> PDF retrieval source: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=JVkdSi7Ekg
- Full-text retrieval: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex environments.를 문제로 두고, We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation in open-world settings requires not only task execution but also the ability to detect and learn from failures.
- **p. 1 / Abstract - extractive body cue:** While recent advances in vision-language models (VLMs) and large language models (LLMs) have improved robots' spatial reasoning and problem-solving abilities, they still struggle with failure ...
- **p. 1 / Abstract - extractive body cue:** We introduce AHA, an open-source VLM designed to detect and reason about failures in robotic manipulation using natural language.
- **p. 1 / Abstract - extractive body cue:** By framing failure detection as a free-form reasoning task, AHA identifies failures and provides detailed, adaptable explanations across different robots, tasks, and environments.
- **p. 1 / Abstract - extractive body cue:** We fine-tuned AHA using FailGen, a scalable framework that generates the first large-scale dataset of robotic failure trajectories, the AHA dataset.
- **p. 2 / 1 Introduction - extractive body cue:** While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior work that treats failure reasoning as a binary detection problem, we frame it as a free-form reasoning task, offering deeper insights into failure ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce FailGen, a data generation pipeline for the procedural generation of failure demonstration data for robotic manipulation tasks across simulators.
- **p. 7 / 4 Method - extractive body cue:** This structured input enables consistent handling of data across different tasks and viewpoints.
- **p. 10 / 4 Method - extractive body cue:** AHA enables efficient reward synthesis for reinforcement learning.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.
- **p. 7 / 4 Method - extractive body cue:** 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model.
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **p. 7 / 4 Method - extractive body cue:** These multimodal tokens are then concatenated and passed through the language transformer.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To capture the temporal relationships within the action sequence, the input image was constructed by selecting a single frame that represents the robot's trajectory up to the current sub-task and concatenating it ... | image/video, language instruction, proprioception과 history | p. 7 (4 Method), p. 6 (4 Method) |
| State/latent | capture, temporal, relationships, within, action, sequence, input, image, constructed, selecting, single, frame | language-grounded task state와 action-policy context | p. 7 (4 Method), p. 6 (4 Method), p. 10 (4 Method) |
| Output/action | For the input formulation in VLMs for instruction fine-tuning and evaluation, we required a query prompt 6 | continuous action, pose 또는 action chunk | p. 6 (4 Method), p. 10 (4 Method), p. 6 (4 Method) |
| Objective/outcome | To systematically assess the reasoning capabilities of different VLMs under budget constraints, we sampled one reward function initially and allowed for iterations over two sessions of GPT API calls. | instruction following, task success, generalization과 latency | p. 10 (4 Method), p. 9 (4 Method), p. 9 (4 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce FailGen, a data generation pipeline for the procedural generation of failure demonstration data for robotic manipulation tasks across simulators.
- **p. 7 / 4 Method - extractive body cue:** This structured input enables consistent handling of data across different tasks and viewpoints.
- **p. 10 / 4 Method - extractive body cue:** AHA enables efficient reward synthesis for reinforcement learning.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic Application ...
- **p. 10 / 4 Method - extractive body cue:** This resulted in success across all five tasks within the budget constraints, and our approach outperformed GPT4o by a significant margin of 22.34% in task ...
- **p. 10 / 4 Method - extractive body cue:** We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping to accelerate and improve task success ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Embodiment/environment | Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks. | hardware/simulator version and reset protocol | p. 8 (4 Method), p. 8 (4 Method) |
| Dataset/benchmark | The evaluation spans three diverse datasets, covering out-of-domain tasks, various simulation environments, and cross-embodiment scenarios. | role, split, size and leakage | p. 8 (4 Method), p. 8 (4 Method), p. 7 (4 Method), p. 9 (4 Method) |
| Metric | Comparing the evaluated policy success rates using different failure feedback VLMs, we observed that AHA-13B provided intuitive, human-level failure reasoning that aided in modifying and improving generated dense reward functions. | definition, denominator, direction and uncertainty | p. 10 (4 Method), p. 10 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Baseline/ablation | Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. AHA-13B outperf ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (4 Method), p. 8 (4 Method) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4 Method - extractive body cue:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By incorporating ...
- **p. 6 / 4 Method - extractive body cue:** This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA.
- **p. 6 / 4 Method - extractive body cue:** If the answer is "No", the VLM is expected to generate a concise, free-form natural language explanation detailing why the task is perceived as a ...
- **p. 7 / 4 Method - extractive body cue:** 4.2 Synthetic Data for Instruction-tuning To facilitate the instruction-tuning of AHA, we needed to systematically generate failure demonstration data.
- **p. 7 / 4 Method - extractive body cue:** Using FailGen, we curated the AHA dataset (Train) dataset by alternating across 79 different tasks in the RLBench simulator, resulting in 49k failure image-text pairs.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex environments.를 문제로 두고, We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 7 (4 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
