# Insights — Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.04137; PDF retrieval source: https://arxiv.org/pdf/2303.04137. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its ...
- **p. 4 / 1 Introduction - extractive body cue:** (2020), we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a visionconditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution.
- **p. 4 / 1 Introduction - extractive body cue:** Third, we removed inpainting-based goal state conditioning due to incompatibility with our framework utilizing a receding prediction horizon.
- **p. 1 / 1 Introduction - extractive body cue:** This formulation allows robot policies to inherit several key properties from diffusion models - significantly improving performance. • Expressing multimodal action distributions.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** For CNN-based Diffusion Policy, We found using FiLM conditioning to pass-in observations is better than impainting on all tasks 1 2 3 4 5 6 ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), p. 16 (A.4 Hyperparameters)

### Strongest assumption and failure boundary

- **p. 5 / 1 Introduction - extractive body cue:** (2022) fails to commit to a single mode due to its lack of temporal action consistency.
- **p. 1 / 1 Introduction - extractive body cue:** Prior work attempts to address this challenge by exploring different action representations (Fig 1 a) - using mixtures of Gaussians Mandlekar et al.
- **p. 4 / 1 Introduction - extractive body cue:** The difficulty of transformer training Liu et al.
- **p. 5 / 1 Introduction - extractive body cue:** Similarly, BCRNN and BET would have difficulty specifying the number of modes that exist in the action distribution (needed for GMM or k-means steps).
- **p. 1 / 1 Introduction - extractive body cue:** (2011), which includes multimodal action distributions, a well-known challenge for policy learning.
- **p. 9 / 5 Evaluation - extractive body cue:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. Realworld Push-T Comparisons. Columns 1-4 show action trajectories based on key events. The last column shows averaged images of the end state. A: ...
- **Boundary to test:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: • Closed-loop ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Reported outcome | Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 checkpoints), with each averaged across ... | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Failure/limitation | We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary. | p. 9 (5 Evaluation), p. 10 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) In the CNN-based Diffusion Policy, ... (p. 3, 1 Introduction).
- **Paper-specific mechanism:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 checkpoints), with each ... (p. 7, Figure/Table caption); the relevant task/metric cue is 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. (p. 9, 5 Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting the shirt at the end. (p. 12, A C).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Diffusion, Imitation Learning, Robotics`.
- **Reading predecessor in the generated track queue:** Flow Matching for Generative Modeling (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) In the CNN-based Diffusion Policy, ... (p. 3, 1 Introduction); preserve the objective/update rule: Scaling the min and max of each action dimension independently to [-1,1] works well for most tasks. (p. 16, A.1 Normalization).
2. Use the paper-reported task/data/environment cue: This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects. (p. 6, 5 Evaluation).
3. Compare against the reported or matched baseline: We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. (p. 6, 5 Evaluation).
4. Report the body metric with its denominator and aggregation: 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. (p. 9, 5 Evaluation).
5. Re-run the reported ablation or stress/failure condition: For each variant, we report results for both stateand image-based observations. (p. 6, 5 Evaluation); if none is reported, design one around: The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting the shirt at the end. (p. 12, A C).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 4 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 6 (5 Evaluation), p. 8 (5 Evaluation), and measure the boundary at p. 12 (A C), p. 12 (A C).

## Falsifiable research question

Under the paper's stated interface (At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of ...), does the paper-specific mechanism (To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy ...) retain the reported evaluation outcome (0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants.) when tested against the paper's strongest explicit boundary (The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 checkpoints), with each ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting the shirt at the end. (p. 12, A C).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
