# MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2511.09516v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2511.09516v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In other words, the robot lacks episodic memory; it cannot directly recall "how an expert accomplished a similar stage" when it is performing one.를 문제로 두고, The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with demonstrationderived memory prompts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs.
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to ...
- **p. 1 / Abstract - extractive body cue:** To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task.
- **p. 1 / Abstract - extractive body cue:** These memory units are implemented as learnable soft prompts optimized through prompt tuning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In other words, the robot lacks episodic memory; it cannot directly recall "how an expert accomplished a similar stage" when it is performing one.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite the advantages mentioned above, current VLA models have a key limitation: they fail to leverage historical memory at task execution.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also develop MemoryAugmented Action Generation (MAAG), which enables memory retrieval and dynamic memory-aware prompt ensembling to augment action generation during realtime task execution. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present the Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), bridging the gap in current VLA models by enabling dynamic access to demonstration-derived ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose Memory-Augmented Action Generation, which retrieves the most relevant stage-specific memory prompt along with the corresponding demonstration actions by comparing the trajectory similarity.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To overcome this, we introduce a memory-augmented framework that enhances VLA models for better long-horizon task performance.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To identify meaningful task stage boundaries, we first select a well-performed demonstration as reference and extract its key poses that mark salient transitions such as ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Instead, we use it as an action prior to guide the dynamic weighting between Abase t and Amem t .

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an overview image I1 t, a wrist image ... | image/video, language instruction, proprioception과 history | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| State/latent | demonstration, consists, sequence, observation-action, pairs, where, observation, includes, overview, image, wrist, language | language-grounded task state와 action-policy context | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Output/action | VLA models acquire broad knowledge about the world from vision-language pre-training and learn to map raw visual observations and natural language instructions directly to robot actions through end-to-end training on diverse robotic ... | continuous action, pose 또는 action chunk | p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Objective/outcome | To encode the stage-specific memory, we optimize Vk by aligning the model's predicted action tokens with expert actions using the flow matching loss: V∗ k = arg min Vk Ep(At/ot), q(Aτ t ... | instruction following, task success, generalization과 latency | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also develop MemoryAugmented Action Generation (MAAG), which enables memory retrieval and dynamic memory-aware prompt ensembling to augment action generation during realtime task execution. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present the Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), bridging the gap in current VLA models by enabling dynamic access to demonstration-derived ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose Memory-Augmented Action Generation, which retrieves the most relevant stage-specific memory prompt along with the corresponding demonstration actions by comparing the trajectory similarity.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To overcome this, we introduce a memory-augmented framework that enhances VLA models for better long-horizon task performance.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** On average, MAP-VLA achieves an 83.4% success rate, whereas the baseline OpenVLA and π0 achieve 54.0% and 76.4%, respectively.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Averaged over the three tasks, MAP-VLA's partial success and complete success rates are 68.3% and 48.3%, versus 53.3% and 23.3% for the baseline, showing a ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** MAP-VLA achieves average success rates of 55.8% and 75.9% for the 10-shot and 20-shot settings, which are consistently higher than those of the baseline π0 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest baseline, π0, across three long-horizon tasks. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | We also note that MAP-VLA's trial outcomes are more consistent, with a lower standard deviation in success rate (0.7%) across runs than π0 (2.3%). | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | As summarized in Table II, MAPVLA again outperforms the baseline policy. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, the memoryless baseline policy π0 exhibits inconsistent and ambiguous object alignment behavior, especially during critical pick-and-place phases (as circled in the figure), often leading ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** By dynamically balancing the task-level generalization of the base prompt with the stage-specificity of the retrieved prompt, the model maintains robustness to retrieval inaccuracies, improves ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This reduced variability suggests improved robustness and reliability, as a result of encoding additional contextual memory into the prompt and dynamic prompt ensembling as we ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In contrast, our MAP-VLA framework demonstrates memory-augmented robustness in such settings.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In other words, the robot lacks episodic memory; it cannot directly recall "how an expert accomplished a similar stage" when it is performing one.를 문제로 두고, The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with demonstrationderived memory prompts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
