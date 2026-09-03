# Insights — Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W5e8c9nwNo; PDF retrieval source: https://arxiv.org/pdf/2605.10118.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead of relying on difficult exploration in the real world, we propose operating the VLM within a physics-grounded sandbox to synthesize diverse tasks and proactively ...
- **p. 3 / 2.3. Navigation Task - extractive body cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 1 / 1. Introduction - extractive body cue:** Motivated by these strides, the research community has increasingly focused on developing general-purpose embodied navigation agents.
- **p. 3 / 2.3. Navigation Task - extractive body cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...
- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive body cue:** P(s′/s, a) denotes the state transition dynamics.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Navigation Task), p. 1 (1. Introduction), p. 3 (2.3. Navigation Task), p. 3 (2.1. Physics-Grounded Interaction Sandbox)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, fully unleashing the potential of VLMs within embodied environments remains fraught with challenges.
- **p. 2 / 1. Introduction - extractive body cue:** Simulator Env Frontier Node Memory Node Sandbox Open-world Experience Question Observation w/ exp Optimized Policy 1 2 1 2 3 Frontier 2 3 2 Memory ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, the huge modality gap between the semantic reasoning space of VLMs and the continuous actuation space of robots often renders learned policies brittle.
- **p. 3 / 2. Problem Formulation - extractive body cue:** Our objective is to bridge the gap between the unsupervised sandbox S and the high-level navigation task N by maximizing a surrogate objective over O.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the required ...
- **Boundary to test:** (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation) |
| Failure/limitation | (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0. | p. 6 (4.1. Experimental Settings), p. 17 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 A represents the agent's action space, which we decompose into the selection of discrete intermediate observations and their corresponding navigable waypoints.를 For any specific task n ∼N, the agent aims to reach the target state via a policy πθ(a/s, n), which maximizes the expected cumulative reward over the target distribution: JN (θ) = ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Navigation, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin..
4. Report the body metric and its denominator/aggregation: Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length (SPL†), utilizing Qwen3-235B-A22B (Yang et al., 2025a) as ....
5. Re-run the body-reported ablation/failure condition: We benchmark SAGE against a diverse set of state-of-the-art (SOTA) methods categorized into two paradigms: (1) RL Paradigm, including SenseAct-NN variants (Khanna et al., 2024); and (2) VLM Paradigm, covering both closed-source ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (2.3. Navigation Task), p. 3 (2.1. Physics-Grounded Interaction Sandbox); the primary result is directionally consistent at p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), p. 6 (4.1. Experimental Settings); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, introduce mechanism이 SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. 대비 Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and ...을 개선하고, (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
