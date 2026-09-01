# Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2310.08864.
> PDF retrieval source: https://arxiv.org/pdf/2310.08864. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, Dataset, Imitation Learning
- Official paper: https://arxiv.org/abs/2310.08864
- Full-text retrieval: https://arxiv.org/pdf/2310.08864
- Code/Project: https://robotics-transformer-x.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage large datasets sourced from the web, comparably ...를 문제로 두고, Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive transfer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications.
- **p. 1 / Abstract - extractive body cue:** In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point ...
- **p. 1 / Abstract - extractive body cue:** Can such a consolidation happen in robotics?
- **p. 1 / Abstract - extractive body cue:** Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment.
- **p. 1 / Abstract - extractive body cue:** Can we instead train "generalist" X-robot policy that can be adapted efficiently to new robots, tasks, arXiv:2310.08864v9 [cs.RO] 14 May 2025
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** How can we overcome these challenges in robotics and move the field of robotic learning toward large data regime that has been so successful in ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization ...
- **p. 4 / 5 Hz - extractive body cue:** RT-1-X is an architecture designed for robotics, with a FiLM [116] conditioned EfficientNet [117] and a Transformer [118].
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Although both architectures are described in detail in their original papers [8, 9], we provide a short summary of each below: RT-1 [8] is a ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our aim is not to innovate in terms of the particular architectures and algorithms, but rather to provide the model that we trained together with ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions. | image/video, language instruction, proprioception과 history | p. 4 (5 Hz), p. 4 (IV. RT-X DESIGN) |
| State/latent | RT-1-X, RT-2-X, take, images, text, instruction, input, output, discretized, end-effector, actions, models | language-grounded task state와 action-policy context | p. 4 (5 Hz), p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |
| Output/action | Both models take in a visual input and natural language instruction describing the task, and output a tokenized action. | continuous action, pose 또는 action chunk | p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 1 (Abstract) |
| Objective/outcome | Training and inference details Both models use a standard categorical cross-entropy objective over their output space (discrete buckets for RT1 and all possible language tokens for RT-2). | instruction following, task success, generalization과 latency | p. 4 (IV. RT-X DESIGN) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization ...
- **p. 4 / 5 Hz - extractive body cue:** RT-1-X is an architecture designed for robotics, with a FiLM [116] conditioned EfficientNet [117] and a Transformer [118].
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Although both architectures are described in detail in their original papers [8, 9], we provide a short summary of each below: RT-1 [8] is a ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** However, the larger RT-2-X model outperforms both the Original Method and RT-1 suggesting that X-robot training can improve performance in the data-rich domains, but only ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** 4), where we would expect transfer from larger datasets to significantly improve performance, and evaluation on domains that have large-scale datasets (Table I), where we ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action Yes Web-pretrained 27.3% 62% (2) RT-2-X 55B none ... | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that co-training on data collected on multiple robots ... | role, split, size and leakage | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Metric | We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs row (4)), demonstrating that higher model capacity enables ... | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption) |
| Baseline/ablation | In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage large datasets sourced from the web, comparably ...를 문제로 두고, Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive transfer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
