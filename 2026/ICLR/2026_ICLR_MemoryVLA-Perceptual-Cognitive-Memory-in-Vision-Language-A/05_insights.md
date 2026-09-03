# Insights — MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=54U3XHf7qq; PDF retrieval source: https://openreview.net/pdf/df1ca9dfbbf5ff164113332379a9cfa71dbf1958.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.
- **p. 4 / 3 METHOD - extractive body cue:** To complement this short-term store, we introduce the Perceptual-Cognitive Memory Bank (PCMB), inspired by the hippocampus, which maintains long-term high-level semantics and fine-grained perceptual details.
- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 6 / 3 METHOD - extractive body cue:** The combined representation is then refined through a feed-forward network to obtain the denoised action at that step.
- **p. 6 / 3 METHOD - extractive body cue:** Since real-world robotic actions lie in a continuous multimodal control space, we adopt a diffusion-based Transformer (DiT) (Peebles & Xie, 2023) implemented with Denoising Diffusion ...
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, it faces two critical limitations: (1) The quadratic complexity of self-attention severely limits the usable temporal context length; (2) Sequential frame inputs are misaligned ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Robotic manipulation is inherently non-Markovian, and neglecting history leads to failures on long-horizon temporal tasks.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, π0 (Black et al., 2024), CogACT (Li et al., 2024a), DexVLA (Wen et al., 2025) and HybridVLA (Liu et al., 2025c) adopt diffusion-based ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, a vision encoder extracts perceptual tokens from observation, while a large language model (LLM) processes them together with the language instruction, leveraging commonsense priors ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near tasks ...
- **Boundary to test:** Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and Clean Restaurant Table), including unseen backgrounds, ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense priors, a perceptualcognitive memory mechan ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) 23 27 27 17 11 21.0 OpenVLA-OFT (Kim et al., ... | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Failure/limitation | Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and Clean Restaurant Table), including unseen backgrounds, ... | p. 18 (Figure/Table caption), p. 19 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = (a1, . . . , aT ) ...를 3.1 OVERVIEW OF MEMORYVLA Problem Formulation We formulate robotic manipulation in VLA models as a sequential decision-making process, where visual observations and language instructions are mapped to control actions for real world ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and Clean Restaurant Table), including unseen backgrounds, ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense priors, a perceptualcognitive memory mechan ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and Clean Restaurant Table), including unseen backgrounds, ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for temporal modeling. (b) Humans handle manipulation tasks via a dual-memory system: working memory (neural activity) supports ....
4. Report the body metric and its denominator/aggregation: Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near tasks evaluated under unseen backgrounds, distractors, lighting, textures, ....
5. Re-run the body-reported ablation/failure condition: Table 6: Ablation on memory type and length. We report average success rates (%) on SimplerEnv-Bridge tasks. Variant Avg. Success Memory Type.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD); the primary result is directionally consistent at p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for ... 대비 Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick ...을 개선하고, Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
