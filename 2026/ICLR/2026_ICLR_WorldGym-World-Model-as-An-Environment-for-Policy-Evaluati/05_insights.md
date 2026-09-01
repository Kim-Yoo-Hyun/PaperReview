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

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk of actions apred.를 This makes it possible to learn a single world model that, in principle, can be used as an interactive environment to evaluate any policies on any tasks. o0 o1 Policy o2 o3 ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a comprehensive set of studies to understand its ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, VLA, world model, policy evaluation, video prediction`.
- **Reading predecessor in the generated track queue:** SAFE: Multitask Failure Detection for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim et al.)..
3. Compare against the body-reported baseline or a matched simpler baseline: We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim et al.)..
4. Report the body metric and its denominator/aggregation: Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves high true ....
5. Re-run the body-reported ablation/failure condition: RT-1-X Octo OpenVLA 0 10 20 30 40 50 60 70 Success Rate (%) 15.6% 23.8% 67.4% 7.6% 4.1% 39.4% Effect of OOD Distractors on Success Rates World Model World Model (with ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 23 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Key, contributions, include mechanism이 We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its ... 대비 Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 ...을 개선하고, Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
