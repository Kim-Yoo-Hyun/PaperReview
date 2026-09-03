# TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=b1CVu9l5GO.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114852. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=b1CVu9l5GO
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114852
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these models are not equipped to handle the challenges unique to robot manipulation, such as understanding kinematics, adapting to different embodiment configurations, and executing reliable physical actions.를 문제로 두고, To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and finetuned on our dataset, rivals the 7B ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction by encoding state-action ...
- **p. 1 / ABSTRACT - extractive body cue:** We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting.
- **p. 1 / ABSTRACT - extractive body cue:** Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv ...
- **p. 1 / ABSTRACT - extractive body cue:** To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, these models are not equipped to handle the challenges unique to robot manipulation, such as understanding kinematics, adapting to different embodiment configurations, and executing ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We posit that this limitation arises because simply mapping image inputs as current states to control actions is insufficient.

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce visual trace prompting, a novel technique that significantly enhances VLA models' spatial-temporal reasoning in manipulation tasks. • Dataset & models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce TraceVLA, a 7B-parameter VLA model fine-tuned from OpenVLA using our novel visual trace prompting dataset, which includes 150K robot manipulation trajectories as shown ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address this, we propose explicitly computing multi-point temporal trajectories and overlaying them directly onto the image inputs for VLA models.
- **p. 3 / 2 PRELIMINARIES - extractive body cue:** First, we introduce visual trace prompting in Section 3.1.
- **p. 3 / 2 PRELIMINARIES - extractive body cue:** The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction by encoding state-action ...
- **p. 4 / 2 PRELIMINARIES - extractive body cue:** These visual traces are then visually overlaid on the robot's original observations, serving as visual prompts that provide the model with a spatial memory of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 VISUAL TRACE PROMPTING Multi-Point Tracking Initial State Final State Visual Trace Prompting Visual Trace Generation Original Image 🧑💻 User: [Prompting for visual inputs] - [Language instruction] 🤖 TraceVLA: [∆𝑥, ∆𝜃, ∆𝐺rip] ... | image/video, language instruction, proprioception과 history | p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES) |
| State/latent | VISUAL, TRACE, PROMPTING, Multi-Point, Tracking, Initial, State, Final, Generation, Original, Image, User | language-grounded task state와 action-policy context | p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION) |
| Output/action | The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ˆa ∼πθ(·/z, s). | continuous action, pose 또는 action chunk | p. 3 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective/outcome | During VLM training, the model is trained end-to-end with a next text token prediction objective on paired or interleaved vision and language data curated from various Internet sources. | instruction following, task success, generalization과 latency | p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES), p. 4 (1. We then identify) |

## Main Claims and Actual Contribution

- **p. 1 / ABSTRACT - extractive body cue:** To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce visual trace prompting, a novel technique that significantly enhances VLA models' spatial-temporal reasoning in manipulation tasks. • Dataset & models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce TraceVLA, a 7B-parameter VLA model fine-tuned from OpenVLA using our novel visual trace prompting dataset, which includes 150K robot manipulation trajectories as shown ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address this, we propose explicitly computing multi-point temporal trajectories and overlaying them directly onto the image inputs for VLA models.
- **p. 3 / 2 PRELIMINARIES - extractive body cue:** First, we introduce visual trace prompting in Section 3.1.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and environmental ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** 0 2 4 6 8 10 Number of Successful Trials Pickplace Corn Pickplace Knife Swipe Corn Sink Fold Cloth 1 4 0 2 8 8 ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** As shown in Figure 9, using a smaller number of steps (N = 3) results in a 3.2% performance improvement.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Embodiment/environment | We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Dataset/benchmark | We benchmark our approach against the following generalist policies, including state-ofthe-art open-sourced models: OpenVLA (Kim et al., 2024): A 7B parameter VLA trained on the Open-X-Embodiment (Collaboration et al., 2023a) Dataset, r ... | role, split, size and leakage | p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 6 (4 EXPERIMENT) |
| Metric | Camera orientations Lighting darker Background change Distractor Table texture Success Rate (%) OpenVLA TraceVLA Camera Lighting Background Distractor TraceVLA OpenVLA TraceVLA OpenVLA TraceVLA Table Texture OpenVLA OpenVLA TraceVLA 32. ... | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 17 (Figure/Table caption) |
| Baseline/ablation | When compared to other baselines like Octo-Base and RT1-X, both TraceVLA and TraceVLA-Phi3 generally perform better, with a few exceptions where RT1-X, shows competitive performance in specific tasks. | fair input/data/compute/action matching | p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 EXPERIMENT - extractive body cue:** In the pick-place banana task, TraceVLA's only failures occurred due to grasping issues, while OpenVLA, even when successfully grasping the banana, failed to follow the ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** Moreover, relying solely on text fails to fully leverage the multimodal grounding capabilities of current vision-language models.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** However, as shown in 7 (Right), finetuning OpenVLA with historical information not only fails to improve overall performance but also reduces it by 6%.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 5 LIMITATION ANALYSIS: TRAINING MEMORY COST AND INFERENCE SPEED Since TraceVLA introduces an additional image input into the model and uses CoTracker to obtain the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. In additional, we finetuned a more compact VLA model, TraceVLA-Phi3, using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, which ...
- **p. 5 / 4 EXPERIMENT - extractive body cue:** This comprehensive set of variations allows us to assess the robustness and adaptability of our approach in handling diverse manipulation scenarios, particularly evaluating the spatial ...
- **p. 10 / 6 RELATED WORK - extractive body cue:** Additionally, leveraging 3D point cloud data for training could further enrich spatial representations, capturing fine-grained details in complex scenes and objects, thus improving manipulation accuracy ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these models are not equipped to handle the challenges unique to robot manipulation, such as understanding kinematics, adapting to different embodiment configurations, and executing reliable physical actions.를 문제로 두고, To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and finetuned on our dataset, rivals the 7B ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
