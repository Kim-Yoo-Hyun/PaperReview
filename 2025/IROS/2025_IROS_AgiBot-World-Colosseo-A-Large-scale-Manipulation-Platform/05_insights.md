# Insights — AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://opendrivelab.com/AgiBot-World/; PDF retrieval source: https://arxiv.org/pdf/2503.06669. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.
- **p. 7 / 2) Implementation Details - extractive body cue:** The inclusion of the latent planner yields an average improvement of 0.12 task completion score.
- **p. 7 / 2) Implementation Details - extractive body cue:** We choose the open-source RDT [10] model to study how much the AgiBot World dataset can help policy learning.
- **p. 8 / 2) Implementation Details - extractive body cue:** How does data quality impact policy learning?
- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (2) Implementation Details), p. 7 (2) Implementation Details), p. 8 (2) Implementation Details), p. 8 (2) Implementation Details)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].
- **p. 2 / I. INTRODUCTION - extractive body cue:** These findings underscore the dataset's efficacy in bridging the gap between controlled laboratory environments and real-world robotic applications.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To achieve generalpurpose robotic intelligence, it is essential to develop datasets that scale in size and diversity while capturing real-world variability, supported by general-purpose humanoid ...
- **p. 3 / Dataset - extractive body cue:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.
- **p. 3 / Dataset - extractive body cue:** Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData [12] 7.2k 4 12 ✗ ✗ Single ...
- **p. 4 / Dataset - extractive body cue:** These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset.
- **Boundary to test:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes latent action ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual review on policy learning. World alpha dataset, despite ... | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands. | p. 3 (Dataset), p. 3 (Dataset) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION).
- **Paper-specific mechanism:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 1: Introducing AgiBot World Colosseo, an open-sourced large-scale manipulation platform comprising data, models, benchmarks and ecosystem. AgiBot World stands out for its unparalleled scale and diversity compared to prior ... (p. 1, Figure/Table caption); the relevant task/metric cue is Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment. (p. 6, 1) Evaluation Tasks). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No Yes Validity Varification Model Training ... (p. 4, Dataset).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Dataset, multi-embodiment, long-horizon manipulation, robot data, humanoid, generalist policy`.
- **Reading predecessor in the generated track queue:** DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION); preserve the objective/update rule: For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps. (p. 7, 2) Implementation Details).
2. Use the paper-reported task/data/environment cue: Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than 100 homogeneous robots, providing high-quality data for challenging ... (p. 3, Dataset).
3. Compare against the reported or matched baseline: Across all tasks and comparisons, GO-1 outperforms baselines by a large margin. (p. 7, 1) Evaluation Tasks).
4. Report the body metric with its denominator and aggregation: Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment. (p. 6, 1) Evaluation Tasks).
5. Re-run the reported ablation or stress/failure condition: We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, with all policies pre-trained on AgiBot World beta. (p. 7, 1) Evaluation Tasks); if none is reported, design one around: Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No Yes Validity Varification Model Training ... (p. 4, Dataset).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENT AND ANALYSIS), and measure the boundary at p. 4 (Dataset), p. 3 (Dataset).

## Falsifiable research question

Under the paper's stated interface (Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie ...), does the paper-specific mechanism (Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie ...) retain the reported evaluation outcome (Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment.) when tested against the paper's strongest explicit boundary (Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 1: Introducing AgiBot World Colosseo, an open-sourced large-scale manipulation platform comprising data, models, benchmarks and ecosystem. AgiBot World stands out for its unparalleled scale and diversity compared to prior ... (p. 1, Figure/Table caption).
- **Strongest explicit boundary:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No Yes Validity Varification Model Training ... (p. 4, Dataset).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
