# Insights — Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.05451; PDF retrieval source: https://arxiv.org/pdf/2209.05451. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 1 / 1 Introduction - extractive body cue:** To this end, we present PERACT (short for PERCEIVER-ACTOR), a language-conditioned BC agent that can learn to imitate a wide variety of 6-DoF manipulation tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach with a Franka Panda on 7 real-world tasks (k-o; only 5 shown) with a multi-task agent trained with just 53 ...
- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 2 / 1 Introduction - extractive body cue:** But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only a small set ...
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, recent works in reinforcement-learning like C2FARM [14] construct a voxelized observation and action space to efficiently learn visual representations of 3D actions with ...
- **p. 2 / 1 Introduction - extractive body cue:** Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?
- **p. 1 / 1 Introduction - extractive body cue:** Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 2 / 1 Introduction - extractive body cue:** This voxel-based formulation provides a strong structural prior with several benefits: a natural method for fusing multi-view observations, learning robust action-centric3 representations [18, 19], and ...
- **p. 6 / 4 Results - extractive body cue:** Evaluations are scored either 0 for failures or 100 for complete successes.
- **p. 7 / 4 Results - extractive body cue:** Each evaluation episode is scored either a 0 for failure or 100 for succces.
- **p. 7 / 4 Results - extractive body cue:** These are very high-precision tasks where being off by a few centimeters or degrees could lead to unrecoverable failures.
- **Boundary to test:** Evaluations are scored either 0 for failures or 100 for complete successes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF actions. • ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. Each evaluation ... | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Failure/limitation | Evaluations are scored either 0 for failures or 100 for complete successes. | p. 6 (4 Results), p. 7 (4 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action". (p. 1, Abstract).
- **Paper-specific mechanism:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption); the relevant task/metric cue is Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Imitation Learning, 3D manipulation`.
- **Reading predecessor in the generated track queue:** BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VIMA: General Robot Manipulation with Multimodal Prompts (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Evaluations are scored either 0 for failures or 100 for complete successes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action". (p. 1, Abstract); preserve the objective/update rule: PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action". (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks). (p. 6, 4 Results).
3. Compare against the reported or matched baseline: PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos. (p. 7, 4 Results).
4. Report the body metric with its denominator and aggregation: Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Figure 3. Ablation Experiments. Success rate of PER- ACT after ablating key components. Ablations. Table 1 reports PERACT w/o Lang, an agent without any language conditioning. Without a language goal, ... (p. 7, Figure/Table caption); if none is reported, design one around: The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), and measure the boundary at p. 8 (4 Results), p. 6 (4 Results).

## Falsifiable research question

Under the paper's stated interface (PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best ...), does the paper-specific mechanism (In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An ...) retain the reported evaluation outcome (Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 ...) when tested against the paper's strongest explicit boundary (The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
