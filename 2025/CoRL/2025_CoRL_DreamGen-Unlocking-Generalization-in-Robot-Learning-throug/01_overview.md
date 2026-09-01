# DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/labs/lpr/publication/jang2025neural/.
> PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/jang2025neural/. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, Video Generation, robot data, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Full-text retrieval: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Code/Project: https://research.nvidia.com/labs/gear/dreamgen/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we propose DREAMGEN, a new synthetic data pipeline that leverages video world models to create realistic training data at scale with minimal manual labor or engineering.를 문제로 두고, Lastly, we introduce DreamGen Bench (Section 4), a new video generation benchmark designed to evaluate how well different video world models adapt to novel robot embodiments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce DREAMGEN, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories-synthetic robot data ...
- **p. 1 / Abstract - extractive body cue:** DREAMGEN leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse ...
- **p. 1 / Abstract - extractive body cue:** Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM).
- **p. 1 / Abstract - extractive body cue:** Despite its simplicity, DREAMGEN unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while ...
- **p. 1 / Abstract - extractive body cue:** To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success.
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we propose DREAMGEN, a new synthetic data pipeline that leverages video world models to create realistic training data at scale with ...
- **p. 2 / 1 Introduction - extractive body cue:** Synthetic data generation in simulation offers an appealing alternative, but it often requires significant manual engineering and suffers from sim2real gap when deploying visuomotor policies ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Lastly, we introduce DreamGen Bench (Section 4), a new video generation benchmark designed to evaluate how well different video world models adapt to novel robot ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we propose DREAMGEN, a new synthetic data pipeline that leverages video world models to create realistic training data at scale with ...
- **p. 3 / 1 Introduction - extractive body cue:** These represent true zero-to-one improvements - GR00T N1 trained on pick-and-place alone achieves 0% success rates on most novel behavior and environment experiments, while DREAMGEN ...
- **p. 4 / 1 Introduction - extractive body cue:** We propose two scenarios of training with neural trajectories: co-training with real-world trajectories, and solely training on the neural trajectories labeled with IDM actions.
- **p. 1 / Abstract - extractive body cue:** To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success.
- **p. 4 / 1 Introduction - extractive body cue:** For latent actions, we use the LAPA latent action model [13], which has a transformer encoderdecoder architecture and is trained on diverse robot and human ...
- **p. 2 / 1 Introduction - extractive body cue:** (1) We fine-tune video world models on a target robot to capture the dynamics and kinematics of the specific embodiment; (2) we prompt the model ...
- **p. 4 / 1 Introduction - extractive body cue:** For the inverse dynamics model (IDM) architecture, we use diffusion transformers with SigLIP-2 vision encoder and train with a flow matching objective.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We condition state information with zero values, since neural trajectories do not contain state information.4 More specifically, given ot, the image observation, and it, the task instruction, we train the policies to ... | observation, uncertainty/risk estimate와 task command | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| State/latent | condition, state, information, zero, values, since, neural, trajectories, contain, More, specifically, given | safe set, recovery state 또는 constraint margin | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | 2.4 Policy Training on Neural Trajectories Lastly, we train visuomotor robot policies on neural trajectories generated by DREAMGEN by conditioning on language instruction and image observations. | shielded, recovery 또는 safe action | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (Abstract) |
| Objective/outcome | However, this paradigm relies heavily on collecting teleoperation data manually for every new task and environment, which remains costly and labor-intensive. | task return과 violation/failure probability | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Lastly, we introduce DreamGen Bench (Section 4), a new video generation benchmark designed to evaluate how well different video world models adapt to novel robot ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we propose DREAMGEN, a new synthetic data pipeline that leverages video world models to create realistic training data at scale with ...
- **p. 3 / 1 Introduction - extractive body cue:** These represent true zero-to-one improvements - GR00T N1 trained on pick-and-place alone achieves 0% success rates on most novel behavior and environment experiments, while DREAMGEN ...
- **p. 4 / 1 Introduction - extractive body cue:** We propose two scenarios of training with neural trajectories: co-training with real-world trajectories, and solely training on the neural trajectories labeled with IDM actions.
- **p. 1 / Abstract - extractive body cue:** To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success.
- **p. 5 / 3 Experiments - extractive body cue:** Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across 24 ...
- **p. 6 / 3 Experiments - extractive body cue:** As shown in Figure 5, neural trajectories consistently improve performance for different visuomotor policies (Diffusion Policy, π0, and GR00T N1) across all robot embodiments for ...
- **p. 7 / 3 Experiments - extractive body cue:** Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to generalize ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (3 Experiments), p. 6 (3 Experiments) |
| Embodiment/environment | 4 DreamGen Bench: A Video Generation Benchmark for Robotics Motivated by recent work benchmarking the capabilities of video generative models as world models [25, 26, 27, 28], we introduce DreamGen Bench, a ... | hardware/simulator version and reset protocol | p. 7 (3 Experiments), p. 5 (3 Experiments) |
| Dataset/benchmark | Using these two metrics, we benchmark 4 different video world models, Hunyuan [10], CogVideoX [8], WAN 2.1 [9], and Cosmos [7], on 2 different training and evaluation setups, one in simulation on ... | role, split, size and leakage | p. 7 (3 Experiments), p. 5 (3 Experiments), p. 8 (3 Experiments), p. 8 (3 Experiments) |
| Metric | Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across 24 tasks), further highlighting the quality of neural ... | definition, denominator, direction and uncertainty | p. 5 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Baseline/ablation | This hints towards a potential for a new paradigm in robot learning, as synthetic data generation through neural trajectories is significantly more scalable compared to the traditional method of manual teleoperation for ... | fair input/data/compute/action matching | p. 5 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitation Our approach is complementary to existing methods that learn from videos, although we do not directly benchmark against them.
- **p. 9 / 6 Conclusion - extractive body cue:** Supporting more complex, dexterous behaviors that require richer control remains an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 3. One benefit of latent actions is that it does not require actually having ground-truth actions for the target robot embodiment when training latent ...
- **p. 7 / 3 Experiments - extractive body cue:** Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to generalize ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we propose DREAMGEN, a new synthetic data pipeline that leverages video world models to create realistic training data at scale with minimal manual labor or engineering.를 문제로 두고, Lastly, we introduce DreamGen Bench (Section 4), a new video generation benchmark designed to evaluate how well different video world models adapt to novel robot embodiments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
