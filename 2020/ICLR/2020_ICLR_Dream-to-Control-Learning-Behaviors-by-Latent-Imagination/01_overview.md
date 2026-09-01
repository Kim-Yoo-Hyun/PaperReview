# Dream to Control: Learning Behaviors by Latent Imagination

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1912.01603.
> PDF retrieval source: https://arxiv.org/pdf/1912.01603. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, latent imagination, model-based reinforcement learning
- Official paper: https://arxiv.org/abs/1912.01603
- Full-text retrieval: https://arxiv.org/pdf/1912.01603
- Code/Project: https://dreamrl.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We approach this limitation by predicting both actions and state values.를 문제로 두고, We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learned world models summarize an agent's experience to facilitate learning complex behaviors.
- **p. 1 / Abstract - extractive body cue:** While learning world models from high-dimensional sensory inputs is becoming feasible through deep learning, there are many potential ways for deriving behaviors from them.
- **p. 1 / Abstract - extractive body cue:** We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination.
- **p. 1 / Abstract - extractive body cue:** We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world ...
- **p. 1 / Abstract - extractive body cue:** On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We approach this limitation by predicting both actions and state values.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, and 3D environments.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key contributions of this paper are summarized as follows: • Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This section describes the main contribution of our paper.
- **p. 5 / B Sequence length - extractive body cue:** We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved or in parallel: ...
- **p. 5 / B Sequence length - extractive body cue:** Learning objective To update the action and value models, we first compute the value estimates Vλ(sτ) for all states sτ along the imagined trajectories.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh et al., 2017; Gregor et al., 2019). | observation, uncertainty/risk estimate와 task command | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | When, sensory, inputs, high-dimensional, images, latent, dynamics, models, abstract, observations, predict, forward | safe set, recovery state 또는 constraint margin | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Output/action | The representation model encodes observations and actions to create continuous vector-valued model states st with Markovian transitions (Watter et al., 2015; Zhang et al., 2019; Hafner et al., 2018). | shielded, recovery 또는 safe action | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (B Sequence length) |
| Objective/outcome | The values optimize Bellman consistency for imagined rewards and the policy maximizes the values by propagating their analytic gradients back through the dynamics. | task return과 violation/failure probability | p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key contributions of this paper are summarized as follows: • Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This section describes the main contribution of our paper.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap et ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent that ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** This suggests that future improvements in representation learning are likely to translate to higher task performance with Dreamer.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Embodiment/environment | These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes. | hardware/simulator version and reset protocol | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Dataset/benchmark | With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent that achieves an average of 786 within 108 ... | role, split, size and leakage | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Metric | Figure 11: Comparison of representation learning methods for Dreamer. The lines show mean scores and the shaded areas show the standard deviation across 5 seeds. We compare generating both images and rewards, ... | definition, denominator, direction and uncertainty | p. 18 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (6 EXPERIMENTS) |
| Baseline/ablation | The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for online planning using PlaNet, and the 24 hours ... | fair input/data/compute/action matching | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Performance of Dreamer in environments with discrete actions and early termination. Dreamer learns successful behaviors on this subset of Atari games and the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning a ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 12: Robustness of Dreamer to different control frequencies. Reinforcement learning methods can be sensitive to this hyper parameter, which could be amplified when learning ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We approach this limitation by predicting both actions and state values.를 문제로 두고, We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (B Sequence length) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
