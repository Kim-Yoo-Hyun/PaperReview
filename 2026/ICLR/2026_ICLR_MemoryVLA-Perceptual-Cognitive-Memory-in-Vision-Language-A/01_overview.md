# MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=54U3XHf7qq.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248101. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=54U3XHf7qq
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/248101
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking temporal dependencies and performing poorly on long-horizon ...를 문제로 두고, Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense priors, a perceptualcognitive memory mechan ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally ...
- **p. 1 / ABSTRACT - extractive body cue:** Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and ...
- **p. 1 / ABSTRACT - extractive body cue:** Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and highlevel ...
- **p. 1 / ABSTRACT - extractive body cue:** Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, it faces two critical limitations: (1) The quadratic complexity of self-attention severely limits the usable temporal context length; (2) Sequential frame inputs are misaligned ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.
- **p. 4 / 3 METHOD - extractive body cue:** To complement this short-term store, we introduce the Perceptual-Cognitive Memory Bank (PCMB), inspired by the hippocampus, which maintains long-term high-level semantics and fine-grained perceptual details.
- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 6 / 3 METHOD - extractive body cue:** The combined representation is then refined through a feed-forward network to obtain the denoised action at that step.
- **p. 6 / 3 METHOD - extractive body cue:** Since real-world robotic actions lie in a continuous multimodal control space, we adopt a diffusion-based Transformer (DiT) (Peebles & Xie, 2023) implemented with Denoising Diffusion ...
- **p. 4 / 3 METHOD - extractive body cue:** The resulting representations are then fed into a memory-conditioned diffusion action expert to generate a sequence of N future 7-DoF actions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = (a1, . . . , aT ) ... | image/video, language instruction, proprioception과 history | p. 4 (3 METHOD), p. 4 (3 METHOD) |
| State/latent | Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence, future, actions | language-grounded task state와 action-policy context | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Output/action | 3.1 OVERVIEW OF MEMORYVLA Problem Formulation We formulate robotic manipulation in VLA models as a sequential decision-making process, where visual observations and language instructions are mapped to control actions for real world ... | continuous action, pose 또는 action chunk | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The model is trained with mean squared error (MSE) loss between the predicted and target actions, and the final denoised vectors are passed through an MLP to generate continuous 7-DoF robotic actions. | instruction following, task success, generalization과 latency | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.
- **p. 4 / 3 METHOD - extractive body cue:** To complement this short-term store, we introduce the Perceptual-Cognitive Memory Bank (PCMB), inspired by the hippocampus, which maintains long-term high-level semantics and fine-grained perceptual details.
- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) 23 27 27 ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** MemoryVLA achieves an overall success rate of 72.7%, improving CogACT by +4.6 points and surpassing π0.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 1, MemoryVLA achieves an average success rate of 71.9%, a +14.6 point gain over the CogACT-Large baseline, and surpasses recent state-of-the-art VLAs including π0 (Black ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | In total, we evaluate 3 robots across 6 benchmarks, spanning over 150 tasks and 500 variations. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near tasks evaluated under unseen backgrounds, distractors, lighting, textures, ... | definition, denominator, direction and uncertainty | p. 19 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for temporal modeling. (b) Humans handle manipulation tasks via a dual-memory system: working memory (neural activity) supports ... | fair input/data/compute/action matching | p. 2 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 27 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near tasks ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 7: Robustness and generalization under out-of-distribution (OOD) variants in simu- lation: Hinge-like object manipulation. (a) OOD variants of Open/Close Drawer and (b) Place Apple ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 11: Ablation on the Number of Cognitive Tokens. Increasing the number of cognitive tokens from 1 to 4 does not improve performance. A single ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.6) (6) How robust and generalizable is it under diverse environmental conditions?
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Bottom: real-world evaluation (General and Longhorizon Temporal), real-world robustness and generalization evaluation.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** VM mirrors the real setup to reduce sim-to-real gap, while VA stress-tests robustness by altering background, lighting, distractors, and table textures.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking temporal dependencies and performing poorly on long-horizon ...를 문제로 두고, Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense priors, a perceptualcognitive memory mechan ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
