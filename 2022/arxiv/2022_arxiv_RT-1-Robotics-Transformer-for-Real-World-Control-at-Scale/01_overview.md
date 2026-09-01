# RT-1: Robotics Transformer for Real-World Control at Scale

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2212.06817.
> PDF retrieval source: https://arxiv.org/pdf/2212.06817. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: VLA, Robotics, Imitation Learning
- Official paper: https://arxiv.org/abs/2212.06817
- Full-text retrieval: https://arxiv.org/pdf/2212.06817
- Code/Project: https://robotics-transformer1.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?를 문제로 두고, We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to ...
- **p. 1 / ABSTRACT - extractive body cue:** While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in ...
- **p. 1 / ABSTRACT - extractive body cue:** We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 1 / ABSTRACT - extractive body cue:** We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although recent years have seen several large multitask robot policies proposed in the literature (Reed et al., 2022; Jang et al., 2021), such models often ...

## Core Idea

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 2 (a), consists of partial counters and is constructed for large scale data collection.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Our primary dataset consists of ∼130k robot demonstrations, collected with a fleet of 13 robots over the course of 17 months.
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 5 RT-1: ROBOTICS TRANSFORMER In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 model architecture.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To this end, the architecture (shown in Figure 1a) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at each time step. | image/video, language instruction, proprioception과 history | p. 4 (3 PRELIMINARIES), p. 2 (3 Hz) |
| State/latent | RT-1, takes, short, sequence, images, natural, language, instruction, input, outputs, action, robot | language-grounded task state와 action-policy context | p. 4 (3 PRELIMINARIES), p. 2 (3 Hz), p. 3 (3 PRELIMINARIES) |
| Output/action | We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ... | continuous action, pose 또는 action chunk | p. 2 (3 Hz), p. 3 (3 PRELIMINARIES), p. 2 (3 Hz) |
| Objective/outcome | The goal is to learn a policy π that maximizes the average reward, in expectation over a distribution of instructions, starting states x0, and transition dynamics. | instruction following, task success, generalization과 latency | p. 3 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES) |

## Main Claims and Actual Contribution

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 2 (a), consists of partial counters and is constructed for large scale data collection.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Our primary dataset consists of ∼130k robot demonstrations, collected with a fleet of 13 robots over the course of 17 months.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally ...
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to achieve ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Experimental results for incorporating simulation data in RT-1. Adding simulation data does not impact the performance on real objects, while significantly improving real ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS) |
| Embodiment/environment | It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to Y" where X only appeared in simulated "pick X" task. ... | hardware/simulator version and reset protocol | p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Dataset/benchmark | RT-1 trained across large datasets of different tasks, originally collected by different robots. | role, split, size and leakage | p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS) |
| Metric | We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance in long-horizon scenarios, as detailed below. | definition, denominator, direction and uncertainty | p. 8 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS) |
| Baseline/ablation | (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art architectures, Gato (Reed et al., 2022) and BC-Z (Jang et al., 2021). | fair input/data/compute/action matching | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 30 / Figure/Table caption - extractive body cue:** Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Second, it does not use a pre-trained text embedding to encode the language string.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** It also does not include inference time considerations that are necessary for real robots as discussed in Sec.
- **p. 12 / 6 EXPERIMENTS - extractive body cue:** Adding simulation data does not impact the performance on real objects, while significantly improving real performance on objects that were only introduced in simulation (+64%).
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Surprisingly, the manipulation performance does not 13
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting avenue ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Example configurations of the robustness evaluation scenarios are depicted in Fig.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?를 문제로 두고, We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 2 (3 Hz) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
