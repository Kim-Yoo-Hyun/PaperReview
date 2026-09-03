# FP3: A 3D Foundation Policy for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://2026.ieee-icra.org/awards/.
> PDF retrieval source: https://arxiv.org/pdf/2503.08950. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision
- Official paper: https://2026.ieee-icra.org/awards/
- Full-text retrieval: https://arxiv.org/pdf/2503.08950
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.를 문제로 두고, In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability and sample efficiency.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Following its success in natural language processing and computer vision, foundation models that are pre-trained on large-scale multi-task datasets have also shown great potential in ...
- **p. 1 / Abstract - extractive body cue:** However, most existing robot foundation models rely solely on 2D image observations, ignoring 3D geometric information, which is essential for robots to perceive and reason ...
- **p. 1 / Abstract - extractive body cue:** FP3 builds on a scalable diffusion transformer architecture and is pre-trained on 60k trajectories with point cloud observations.
- **p. 1 / Abstract - extractive body cue:** With the model design and diverse pre-training data, FP3 can be efficiently fine-tuned for downstream tasks while exhibiting strong generalization capabilities.
- **p. 1 / Abstract - extractive body cue:** Experiments on real robots demonstrate that with only 80 demonstrations, FP3 is able to learn a new task with over 90% success rates in novel ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these learned policies often show limited or even zero generalization capability to unseen scenarios, new objects, and distractors [66].

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability ...
- **p. 4 / III. METHOD - extractive body cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 3 / III. METHOD - extractive body cue:** We introduce the 3D Foundation Policy (FP3) model for generalist robotic manipulation, achieving high data efficiency and generalization capability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions as follows:
- **p. 3 / III. METHOD - extractive body cue:** FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.
- **p. 3 / III. METHOD - extractive body cue:** Now we describe the detailed structure of FP3 model, including the encoding of multi-modal inputs and the transformer-based encoder-decoder architecture.
- **p. 4 / III. METHOD - extractive body cue:** The Transformer encoder fuses multi-modal input embeddings to latent tokens, while the Transformer decoder takes in the noise actions and leverages adaLN [47, 5, 32] ...
- **p. 4 / III. METHOD - extractive body cue:** Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes the 3D point cloud observation, language, and robot proprioceptive state as input and predicts action chunks of future actions. | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| State/latent | takes, point, cloud, observation, language, robot, proprioceptive, state, input, predicts, action, chunks | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP MLP Transformer Encoder Diffusion Transformer with Causal ... | continuous action, pose 또는 action chunk | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | The weight decay is set to 0.1, and gradient clipping is set to 1.0. | instruction following, task success, generalization과 latency | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability ...
- **p. 4 / III. METHOD - extractive body cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 3 / III. METHOD - extractive body cue:** We introduce the 3D Foundation Policy (FP3) model for generalist robotic manipulation, achieving high data efficiency and generalization capability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions as follows:
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong baselines.
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** Results in Table I show that in in-domain experiments, with only 10 demonstrations per scene, DP and DP3 can somewhat handle easier tasks, even though ...
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** FP3 significantly outperforms other policies both in domain and in the wild.
- **p. 7 / 8 Training Scenes - extractive body cue:** FP3 achieves outstanding performance in all generalization evaluation settings.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Embodiment/environment | As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating downstream tasks. | hardware/simulator version and reset protocol | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD) |
| Dataset/benchmark | We further move the robot arm to novel environments and evaluate the policies with unseen objects. | role, split, size and leakage | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Metric | We report the success rate as our metric. | definition, denominator, direction and uncertainty | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Baseline/ablation | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong baselines. | fair input/data/compute/action matching | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, ...
- **p. 8 / V. LIMITATIONS - extractive body cue:** While FP3 shows strong performance as a policy foundation model, it still has several limitations.
- **p. 8 / V. LIMITATIONS - extractive body cue:** One limitation is that although FP3 enables efficient and generalizable downstream fine-tuning, the base model exhibits limited zero-shot performance.
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** Qualitatively, we find that the failures of all baseline algorithms are mainly due to issues in the details, such as not being precise enough when ...
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** Another interesting issue is the policy's response after an initial failure attempt.
- **p. 7 / 8 Training Scenes - extractive body cue:** FP3 generalize well to all unseen environments and new objects, while Diffusion Policy often fails to recognize the target object or misses the target position.
- **p. 4 / III. METHOD - extractive body cue:** The diffusion denoiser of FP3 is a Transformer decoder that denoises the action chunks from noise with temporal causal masking following [79].

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.를 문제로 두고, In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability and sample efficiency.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
