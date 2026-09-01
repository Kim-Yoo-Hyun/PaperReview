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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".를 Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, object poses, memory, or symbolic states.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Evaluations are scored either 0 for failures or 100 for complete successes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF actions. • ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Imitation Learning, 3D manipulation`.
- **Reading predecessor in the generated track queue:** BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VIMA: General Robot Manipulation with Multimodal Prompts (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Evaluations are scored either 0 for failures or 100 for complete successes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks)..
3. Compare against the body-reported baseline or a matched simpler baseline: PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos..
4. Report the body metric and its denominator/aggregation: Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. Each evaluation ....
5. Re-run the body-reported ablation/failure condition: Figure 3. Ablation Experiments. Success rate of PER- ACT after ablating key components. Ablations. Table 1 reports PERACT w/o Lang, an agent without any language conditioning. Without a language goal, the agent ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 8 (4 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 ... 대비 Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 ...을 개선하고, Evaluations are scored either 0 for failures or 100 for complete successes. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
