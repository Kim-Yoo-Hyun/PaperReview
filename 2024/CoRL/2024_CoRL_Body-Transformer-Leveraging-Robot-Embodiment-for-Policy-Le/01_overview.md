# Body Transformer: Leveraging Robot Embodiment for Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Oce2215aJE.
> PDF retrieval source: https://arxiv.org/pdf/2408.06316. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, embodiment, graph neural network, policy learning
- Official paper: https://openreview.net/forum?id=Oce2215aJE
- Full-text retrieval: https://arxiv.org/pdf/2408.06316
- Code/Project: https://sferrazza.cc/bot_site/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. • We incorporate this ...를 문제로 두고, Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. • We incorporate this ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In recent years, the transformer architecture has become the de facto standard for machine learning algorithms applied to natural language processing and computer vision.
- **p. 1 / Abstract - extractive body cue:** Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.
- **p. 1 / Abstract - extractive body cue:** We represent the robot body as a graph of sensors and actuators, and rely on masked attention to pool information throughout the architecture.
- **p. 1 / Abstract - extractive body cue:** The resulting architecture outperforms the vanilla transformer, as well as the classical multilayer perceptron, in terms of task completion, scaling properties, and computational efficiency when ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of ...
- **p. 4 / 3 Background - extractive body cue:** This is similar to the concurrent work in Buterez et al.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of ...
- **p. 2 / 1 Introduction - extractive body cue:** In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.
- **p. 4 / 3 Background - extractive body cue:** We propose Body Transformer (BoT), which is based on masked attention, where at each layer in the resulting architecture, a node can only attend to ...
- **p. 4 / 3 Background - extractive body cue:** We present below the various components of the BoT architecture (see also Figure 1): (1) a tokenizer that projects the sensory inputs into the corresponding ...
- **p. 1 / Abstract - extractive body cue:** Keywords: Robot Learning, Graph Neural Networks, Imitation Learning, Reinforcement Learning Tokenizer observations per node Torso Front Right Hip Front Right Thigh Rear Left Calf … ...
- **p. 3 / 3 Background - extractive body cue:** While the standard self-attention mechanism amounts to modeling a fully connected graph, a popular transformer-based GNN, Graphormer [18], injects node-edges information through graph-based positional encodings ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We present below the various components of the BoT architecture (see also Figure 1): (1) a tokenizer that projects the sensory inputs into the corresponding node embedding, (2) a transformer encoder that ... | multi-view observation, language/task label과 action trajectory | p. 4 (3 Background), p. 1 (Abstract) |
| State/latent | present, below, various, components, BoT, architecture, Figure, tokenizer, projects, sensory, inputs, corresponding | shared representation, embodiment/task identity와 data distribution | p. 4 (3 Background), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | Keywords: Robot Learning, Graph Neural Networks, Imitation Learning, Reinforcement Learning Tokenizer observations per node Torso Front Right Hip Front Right Thigh Rear Left Calf … Front Right Calf Front Left Hip graph ... | dataset sample 또는 learned policy action | p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (3 Background) |
| Objective/outcome | Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. • We incorporate this ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of ...
- **p. 2 / 1 Introduction - extractive body cue:** In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.
- **p. 4 / 3 Background - extractive body cue:** We propose Body Transformer (BoT), which is based on masked attention, where at each layer in the resulting architecture, a node can only attend to ...
- **p. 4 / 3 Background - extractive body cue:** We present below the various components of the BoT architecture (see also Figure 1): (1) a tokenizer that projects the sensory inputs into the corresponding ...
- **p. 5 / 5 Experiments - extractive body cue:** We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.
- **p. 6 / 5 Experiments - extractive body cue:** The result shows that BoT-Mix consistently outperforms both the MLP and vanilla transformer baselines in terms of sample efficiency and asymptotic performance, highlighting the efficacy ...
- **p. 5 / 5 Experiments - extractive body cue:** While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Embodiment/environment | With the following experiments, we aim to answer the following questions: • Does masked attention benefit imitation learning in terms of performance and generalization? • Does BoT exhibit a positive scaling trend ... | hardware/simulator version and reset protocol | p. 5 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | Finally, we adapt the A1-Walk environment, which is part of the Legged Gym repository [32], where the task is for a Unitree A1 quadruped robot to follow a fixed velocity command. | role, split, size and leakage | p. 5 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 5 (5 Experiments) |
| Metric | Statistics of the various architecturecriterion combinations are shown with two values, the leftside being the maximum value recorded during training, and the rightside being the mean evaluation scores with standard deviation. | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Baseline/ablation | We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines. | fair input/data/compute/action matching | p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6 Conclusion - extractive body cue:** We leave the extension of BoT to the temporal dimension as future work, as it promises to further improve real world deployment of robot policies, ...

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. • We incorporate this ...를 문제로 두고, Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. • We incorporate this ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 4 (3 Background), p. 4 (3 Background), p. 1 (Abstract), p. 4 (3 Background), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
