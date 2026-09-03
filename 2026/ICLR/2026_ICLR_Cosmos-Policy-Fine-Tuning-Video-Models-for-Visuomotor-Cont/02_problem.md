# Problem - Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006732; PDF retrieval source: https://arxiv.org/pdf/2601.16163. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 6 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES)): In this work, we address these limitations with Cosmos Policy: an effective robot policy that is adapted from a pretrained video model (Cosmos-Predict2-2B (NVIDIA et al., 2025)) through a single ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution over time.
- **p. 1 / ABSTRACT - extractive body cue:** To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce complexity by requiring multiple stages of post-training and new ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we introduce Cosmos Policy, a simple approach for adapting a large pretrained video model (CosmosPredict2) into an effective robot policy through a ...
- **p. 1 / ABSTRACT - extractive body cue:** Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and ...
- **p. 1 / ABSTRACT - extractive body cue:** Additionally, Cosmos Policy generates future state images and values (expected cumulative rewards), which are similarly encoded as latent frames, enabling test-time planning of action trajectories ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we address these limitations with Cosmos Policy: an effective robot policy that is adapted from a pretrained video model (Cosmos-Predict2-2B (NVIDIA et ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We aggregate these via "majority mean": we determine whether the majority predict success or failure (via a fixed threshold) and then average values within the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this work, we address these limitations with Cosmos Policy: an effective robot policy that is adapted from a pretrained video model ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | It does not support robot proprioception as input, robot actions or state values as output, nor multiple camera views-all of which are ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | does, support, robot, proprioception, input, actions, state, values, output, multiple | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Note, single-step, training, losses, given, varying, noise, levels | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: does, support, robot, proprioception, input, actions, state, values, output, multiple | p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 17 (A.2.2 LIBERO TRAINING DETAILS) |
| Decision / output variable | filtered/recovery action u_safe; body terms: evaluate, modes, first, direct, policy, without, planning, then | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: After, gradient, steps, policy, action, training, loss, future | p. 17 (A.2.4 ALOHA TRAINING DETAILS), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 15 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), p. 9 (5 EXPERIMENTS), p. 19 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We aggregate these via "majority mean": we determine whether the majority predict success or failure (via a fixed threshold) and then average values within the ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** However, training on demonstrations alone is insufficient for effective planning since the data only covers successful outcomes,‡ which means that the world model and value ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These spatiotemporal priors hold significant value for robotics applications.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** A world model ˆT : S × A →Π(S) learns to predict the future state given current state and action, approximating the true environment dynamics.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES)): We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and value predictions.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This search process produces trajectories that are more likely to succeed at the task Our main contribution is the Cosmos Policy approach for fine-tuning pretrained ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Rather than designing new model components or making architectural modifications as done in prior works, we propose to encode additional modalities as new latent frames ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** To encode the new modalities as latent frames, we fill each H′ ×W ′ ×C′ latent volume with normalized and duplicated copies of the robot ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Once we have the fine-tuned checkpoint for refined world modeling and policy learning, we propose dual deployment: the original Cosmos Policy checkpoint serves as the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | The additional episodes are important for this task since training an accurate world model for it is particularly ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | For OOD trials, we replace the pink ziploc bag with an unseen blue ziploc bag that is filled ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 5: Common failure modes of π0.5 and OpenVLA-OFT+ on two challenging ALOHA robot tasks. Left: π0.5 struggles ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 6: World model predictions: base Cosmos Policy vs. fine-tuned checkpoint. Top: The base Cosmos Policy's world model ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 5 (3 PRELIMINARIES). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 6 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), interface p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 5 (3 PRELIMINARIES), objective p. 17 (A.2.4 ALOHA TRAINING DETAILS), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
