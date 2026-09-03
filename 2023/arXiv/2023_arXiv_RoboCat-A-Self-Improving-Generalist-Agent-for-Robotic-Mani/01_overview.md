# RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (60 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.11706.
> PDF retrieval source: https://arxiv.org/pdf/2306.11706. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, generalist policy, cross-embodiment, self-improvement, robot manipulation
- Official paper: https://arxiv.org/abs/2306.11706
- Full-text retrieval: https://arxiv.org/pdf/2306.11706
- Code/Project: https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (60 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty of the task.를 문제로 두고, Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a large set of dexterous tasks on multiple ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot ...
- **p. 1 / Abstract - extractive body cue:** Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming actionlabelled visual experience.
- **p. 1 / Abstract - extractive body cue:** This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions.
- **p. 1 / Abstract - extractive body cue:** With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for ...
- **p. 8 / 1 Introduction - extractive body cue:** In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty of the task.
- **p. 9 / 1 Introduction - extractive body cue:** They differ in difficulty, but in all cases require dexterous and precise movements to ensure that the structure remains stable after completion.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 2 / 1 Introduction - extractive body cue:** We introduce the embodiments, tasks, and object sets that we have used in this work in Section 3.
- **p. 3 / 1 Introduction - extractive body cue:** We describe our experimental setup for both training and evaluation in Section 4, before we present our extensive experiments to support our claims in Section ...
- **p. 3 / 1 Introduction - extractive body cue:** 2 RoboCat We introduce RoboCat, a self-improving generalist agent for robotic manipulation that can perform multiple tasks and control multiple embodiments in simulation and the ...
- **p. 4 / 1 Introduction - extractive body cue:** Specifically, the encoder is trained on a dataset that consists of images from ImageNet (Deng et al., 2009), images from the control tasks in Reed ...
- **p. 4 / 1 Introduction - extractive body cue:** The VQ-GAN, similarly to a VQ-VAE (van den Oord et al., 2017), consists of an encoder that encodes an input image into a series of ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained language models and ...
- **p. 5 / 1 Introduction - extractive body cue:** Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our agent handles these variations natively without requiring common action or observation representations, by leveraging the transformer's ability to input and output variable-length sequences based on context. | multi-view observation, language/task label과 action trajectory | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | agent, handles, variations, natively, without, requiring, common, action, observation, representations, leveraging, transformer | shared representation, embodiment/task identity와 data distribution | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Output/action | Our goal-conditioned agent is represented by a policy π(at/ot, gt), where at denotes the action vector, ot = (xt, It) are the proprioceptive observation (e.g. robot joint positions and velocities) and image ... | dataset sample 또는 learned policy action | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction) |
| Objective/outcome | Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D " T X t=1 Q X q=1 ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 2 / 1 Introduction - extractive body cue:** We introduce the embodiments, tasks, and object sets that we have used in this work in Section 3.
- **p. 3 / 1 Introduction - extractive body cue:** We describe our experimental setup for both training and evaluation in Section 4, before we present our extensive experiments to support our claims in Section ...
- **p. 3 / 1 Introduction - extractive body cue:** 2 RoboCat We introduce RoboCat, a self-improving generalist agent for robotic manipulation that can perform multiple tasks and control multiple embodiments in simulation and the ...
- **p. 4 / 1 Introduction - extractive body cue:** Specifically, the encoder is trained on a dataset that consists of images from ImageNet (Deng et al., 2009), images from the control tasks in Reed ...
- **p. 17 / 5 Experiments - extractive body cue:** The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks.
- **p. 13 / 5 Experiments - extractive body cue:** We see from Figure 5(a) that the performance of this smaller model is comparable to RoboCat on the stacking tasks, but significantly lower for the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Final RoboCat performance on evaluation tasks. This table lists the tasks used for training and fine-tuning of the final RoboCat agent, and highlights ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 17 (5 Experiments), p. 13 (5 Experiments) |
| Embodiment/environment | All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is even more apparent in the real-world lifting, insertion, and removal ... | hardware/simulator version and reset protocol | p. 13 (5 Experiments), p. 15 (5 Experiments) |
| Dataset/benchmark | Overall, we show that RoboCat-lim adapts with only 100-500 episodes to a broad set of downstream tasks, including unseen variations and objects, different data sources (agent vs demonstrations; see Table 3), and ... | role, split, size and leakage | p. 13 (5 Experiments), p. 15 (5 Experiments), p. 15 (5 Experiments), p. 11 (4.3 Evaluation) |
| Metric | (Section 5.3) 5.1 Overall RoboCat performance We evaluated RoboCat over all the training tasks and we report task success rates averaged within each embodiment, task family, and object set, in Table 1 ... | definition, denominator, direction and uncertainty | p. 12 (5 Experiments), p. 13 (5 Experiments), p. 55 (Figure/Table caption) |
| Baseline/ablation | Figure 5: RoboCat compared to VFM baselines on training tasks. RoboCat performs better on the vast majority of training tasks, compared to single-task baseline agents trained on the same data for each ... | fair input/data/compute/action matching | p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 20 / 6 Related Work - extractive body cue:** While visual goal specification already allows the agent to learn from failures and sub-optimal data, incorporating RL would enable both learning with rewards and learning ...
- **p. 38 / Figure/Table caption - extractive body cue:** Table 8: Quantities of human demonstrations and self-generated data. Embodiment Task Family Object Set Variant Human teleop demos Successes Failures
- **p. 60 / Figure/Table caption - extractive body cue:** Table 20: Skill transfer analysis. Average accumulated error over all three NIST-i gear sizes. Moving from the 364M model to the full RoboCat agent eliminates ...
- **p. 56 / Figure/Table caption - extractive body cue:** Figure 27: The different types of NIST-i based environments we ablate performance against. Note, in the main paper we report performance against environments from (a) ...
- **p. 15 / 5 Experiments - extractive body cue:** In simulation, RoboCat-lim generalises 0-shot to a held-out object set on the Sawyer (third plot from the left) and the blue-on-green stacking task variant on ...
- **p. 19 / 6 Related Work - extractive body cue:** As we are primarily concerned with goal images as task specification in a behaviour cloning setting, this work does not address the question of goal ...
- **p. 20 / 6 Related Work - extractive body cue:** Future work could look into enabling flexible and multi-modal task specification.

## Why Read It

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty of the task.를 문제로 두고, Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a large set of dexterous tasks on multiple ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 8 (1 Introduction), p. 9 (1 Introduction), p. 11 (4.3 Evaluation), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
