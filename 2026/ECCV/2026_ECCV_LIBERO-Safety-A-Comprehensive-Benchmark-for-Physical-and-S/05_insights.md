# Insights — LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.23686; PDF retrieval source: https://arxiv.org/pdf/2606.23686. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** Our benchmark consists of four core components: a parametric environment definition framework (Sec.
- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (462 Hand-Object Pairs), p. 3 (1 INTRODUCTION), p. 5 (462 Hand-Object Pairs), p. 8 (462 Hand-Object Pairs)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these benchmarks suffer from two critical limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. - Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- **p. 39 / C.3 Additional Experimental Results - extractive body cue:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.
- **p. 10 / 4 Experiment - extractive body cue:** To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard task failures, Execution Time evaluates operational efficiency ...
- **p. 42 / C.3 Additional Experimental Results - extractive body cue:** These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic physical failure.
- **Boundary to test:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to enable the ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | p. 11 (4 Experiment), p. 10 (4 Experiment) |
| Failure/limitation | This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. | p. 39 (C.3 Additional Experimental Results), p. 10 (4 Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys. (p. 1, 462 Hand-Object Pairs).
- **Paper-specific mechanism:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to ... (p. 3, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment); the relevant task/metric cue is Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any constraint violations. (p. 10, 4 Experiment). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. (p. 39, C.3 Additional Experimental Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Benchmark, semantic`.
- **Reading predecessor in the generated track queue:** Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys. (p. 1, 462 Hand-Object Pairs); preserve the objective/update rule: Despite the impressive manipulation capabilities of VisionLanguage-Action (VLA) models, their operational safety under strict constraints remains largely unverified. (p. 1, 462 Hand-Object Pairs).
2. Use the paper-reported task/data/environment cue: To ensure unbiased representation learning across tasks, dataset and trajectory weight balancing are explicitly enabled. (p. 37, C.2 Training Configurations).
3. Compare against the reported or matched baseline: Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment).
4. Report the body metric with its denominator and aggregation: Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any constraint violations. (p. 10, 4 Experiment).
5. Re-run the reported ablation or stress/failure condition: To distinguish the safety-evaluation difficulty from the effect of training on LIBERO-Safety, we additionally evaluate two representative policies under two control settings: zero-shot inference without task-specific fine-tuning, and SF ... (p. 38, C.3 Additional Experimental Results); if none is reported, design one around: This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. (p. 39, C.3 Additional Experimental Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 13 (4 Experiment), p. 11 (Figure/Table caption), p. 10 (4 Experiment), and measure the boundary at p. 39 (C.3 Additional Experimental Results), p. 10 (4 Experiment).

## Falsifiable research question

Under the paper's stated interface (Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input ...), does the paper-specific mechanism (In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce ...) retain the reported evaluation outcome (Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any ...) when tested against the paper's strongest explicit boundary (This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to ... (p. 3, 1 INTRODUCTION).
- **Paper-supported outcome:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment).
- **Strongest explicit boundary:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. (p. 39, C.3 Additional Experimental Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
