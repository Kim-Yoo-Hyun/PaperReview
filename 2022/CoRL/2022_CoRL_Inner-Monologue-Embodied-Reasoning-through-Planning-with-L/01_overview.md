# Inner Monologue: Embodied Reasoning through Planning with Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v205/huang23c.html.
> PDF retrieval source: https://arxiv.org/pdf/2207.05608. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, LLM planning, feedback, replanning, long-horizon manipulation
- Official paper: https://proceedings.mlr.press/v205/huang23c.html
- Full-text retrieval: https://arxiv.org/pdf/2207.05608
- Code/Project: https://innermonologue.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about complex tasks also requires semantic knowledge a ...를 문제로 두고, Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent works have shown how the reasoning capabilities of Large Language Models (LLMs) can be applied to domains beyond natural language processing, such as planning ...
- **p. 1 / Abstract - extractive body cue:** These embodied problems require an agent to understand many semantic aspects of the world: the repertoire of skills available, how these skills influence the world, ...
- **p. 1 / Abstract - extractive body cue:** LLMs planning in embodied environments need to consider not just what skills to do, but also how and when to do them - answers that ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate to what extent LLMs used in such embodied contexts can reason over sources of feedback provided through natural language, without ...
- **p. 1 / Abstract - extractive body cue:** We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in ...
- **p. 1 / 1 Introduction - extractive body cue:** While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- **p. 2 / 1 Introduction - extractive body cue:** Robot Success Detector Scene Descriptor (b) (c) (a) Human Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that similarly to recent work [19], natural language provides a universal and interpretable interface for such grounding of model communication and allows them ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and place actions as ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Given the first and last observation, the model outputs a probability distribution over all the possible skills.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** At the start of the action plan, the language model first generates a list of desired sub-goals given the high-level instruction.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As a demonstration of the versatility of LLMs and grounded closed-loop feedback, we additionally show several surprising capabilities emerging from the inner monologue formulation, including continued adaptation to new instructions, sel ... | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |
| State/latent | demonstration, versatility, LLMs, grounded, closed-loop, feedback, additionally, several, surprising, capabilities, emerging, inner | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Output/action | The policy is trained on 20000 pre-collected demonstrations, where each demonstration contains 1) language instruction of the format "pick up [x] and place it on [y]", 2) top-down view of RGB-D observation ... | continuous action, pose 또는 action chunk | p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Objective/outcome | The model is trained with the binary cross entropy loss with respect to the ground truth binary label. | instruction following, task success, generalization과 latency | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- **p. 2 / 1 Introduction - extractive body cue:** Robot Success Detector Scene Descriptor (b) (c) (a) Human Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that similarly to recent work [19], natural language provides a universal and interpretable interface for such grounding of model communication and allows them ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the robot has successfully moved into a plate. | hardware/simulator version and reset protocol | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Dataset/benchmark | Environment Feedback: Object Recognition We use human-provided object recognition to provide feedback about the presence of objects visible to the robot camera. | role, split, size and leakage | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |
| Metric | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success rates over ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success rates over ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and adversarial ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue can ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** This is done to prevent undesired stacking behavior when placing objects into the plate, which may cause the object to roll off and fall off ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about complex tasks also requires semantic knowledge a ...를 문제로 두고, Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
