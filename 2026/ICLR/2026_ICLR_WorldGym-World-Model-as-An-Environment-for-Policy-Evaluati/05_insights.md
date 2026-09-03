# Insights — WorldGym: World Model as An Environment for Policy Evaluation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10008029; PDF retrieval source: https://arxiv.org/pdf/2506.00613. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this observation, we propose a world-model-based policy evaluation environment (WorldGym), as shown in Figure 1.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To ensure the world model is fully controllable by robot actions, we propose to randomly drop out actions for entire video clips, and use classifier-free ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose setting the horizon equal to the policy's action chunk size, /apred/.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** Specifically, the OpenVLA Bridge evaluation consists of 17 challenging tasks which are not present in the Bridge V2 (Walke et al., 2023) dataset.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy rollouts.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** As a result, the sim-to-real gap has hindered progress in robotics (Zhao et al., 2020; Salvato et al., 2021; Dulac-Arnold et al., 2019).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, most of the existing work in model-based RL considers single-task settings, which puts itself at a disadvantage compared to model-free RL, since learning a ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, existing work in OPE mostly focuses on simulated settings that are less practical (e.g., assumptions about full observability, access to ground truth states).
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Motivated by characteristics of a real-robot system such as image based observations, high control frequencies, diverse offline data from different tasks/environments, and the lack of ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10: OOD: Failure modes. Left: We add a laptop to the scene, which displays an image of a carrot. In 15% of trials, OpenVLA ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset ...
- **Boundary to test:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a comprehensive set of studies to understand its ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves high true ... | p. 17 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes. | p. 8 (1 INTRODUCTION), p. 8 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 4.3 OUT-OF-DISTRIBUTION INPUTS In this section, use WorldGym to explore policies' performance on both OOD input images and OOD language instructions. (p. 7, 1 INTRODUCTION).
- **Paper-specific mechanism:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a comprehensive set of studies to ... (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset does not contain trajectories which ... (p. 9, Figure/Table caption); the relevant task/metric cue is Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves ... (p. 17, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Notably, GPT-4o achieves very low false positives (i.e., the rollout is a failure but the VLM thinks it is a success), which is highly useful in policy evaluation. (p. 18, B.2 VALIDATING VLM SUCCESS PREDICTIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, VLA, world model, policy evaluation, video prediction`.
- **Reading predecessor in the generated track queue:** SAFE: Multitask Failure Detection for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 4.3 OUT-OF-DISTRIBUTION INPUTS In this section, use WorldGym to explore policies' performance on both OOD input images and OOD language instructions. (p. 7, 1 INTRODUCTION); preserve the objective/update rule: Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards. (p. 1, ABSTRACT).
2. Use the paper-reported task/data/environment cue: We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim et al.). (p. 8, 1 INTRODUCTION).
3. Compare against the reported or matched baseline: Additionally, even without access to an image editing model, we demonstrate that WorldGym can be used to evaluate policies' performance on OOD language instructions. (p. 8, 1 INTRODUCTION).
4. Report the body metric with its denominator and aggregation: Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves ... (p. 17, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Additionally, even without access to an image editing model, we demonstrate that WorldGym can be used to evaluate policies' performance on OOD language instructions. (p. 8, 1 INTRODUCTION); if none is reported, design one around: Notably, GPT-4o achieves very low false positives (i.e., the rollout is a failure but the VLM thinks it is a success), which is highly useful in policy evaluation. (p. 18, B.2 VALIDATING VLM SUCCESS PREDICTIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 9 (Figure/Table caption), p. 23 (Figure/Table caption), p. 9 (Figure/Table caption), and measure the boundary at p. 18 (B.2 VALIDATING VLM SUCCESS PREDICTIONS), p. 1 (ABSTRACT).

## Falsifiable research question

Under the paper's stated interface (4.3 OUT-OF-DISTRIBUTION INPUTS In this section, use WorldGym to explore policies' performance on both OOD input images and OOD language instructions.), does the paper-specific mechanism (Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, ...) retain the reported evaluation outcome (Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 ...) when tested against the paper's strongest explicit boundary (Notably, GPT-4o achieves very low false positives (i.e., the rollout is a failure but the VLM thinks it ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a comprehensive set of studies to ... (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset does not contain trajectories which ... (p. 9, Figure/Table caption).
- **Strongest explicit boundary:** Notably, GPT-4o achieves very low false positives (i.e., the rollout is a failure but the VLM thinks it is a success), which is highly useful in policy evaluation. (p. 18, B.2 VALIDATING VLM SUCCESS PREDICTIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
