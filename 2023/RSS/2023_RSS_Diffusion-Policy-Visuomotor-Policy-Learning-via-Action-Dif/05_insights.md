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
- **p. 1 / 1 Introduction - extractive body cue:** (2011), which includes multimodal action distributions, a well-known challenge for policy learning. arXiv:2303.04137v5 [cs.RO] 14 Mar 2024
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

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Diffusion Policy 3 b) CNN-based c) Transformer-based Conv1D Conv1D Conv1D Conv1D Conv1D Input: Image Observation Sequence Output: Action Sequence … Cross Attention Cross Attention ×K Obs Emb Action Emb Action Emb A ...를 At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) In the CNN-based Diffusion Policy, FiLM (Feature-wise ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: • Closed-loop ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Diffusion, Imitation Learning, Robotics`.
- **Reading predecessor in the generated track queue:** Flow Matching for Generative Modeling (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 of the tasks (9 variants in total)..
3. Compare against the body-reported baseline or a matched simpler baseline: We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%..
4. Report the body metric and its denominator/aggregation: We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset..
5. Re-run the body-reported ablation/failure condition: There are two variants: one with RGB image observations and another with 9 2D keypoints obtained from the groundtruth pose of the T block, both with proprioception for endeffector location..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 16 (A.4 Hyperparameters), p. 16 (A.4 Hyperparameters); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (5 Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 successfully, employ, diffusion mechanism이 We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, ... 대비 We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset.을 개선하고, We observed that poor performance during the transition between stages is the most common failure case ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
