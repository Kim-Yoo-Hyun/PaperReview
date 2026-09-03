# Insights — CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p072.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p072.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an ...
- **p. 4 / A. Problem Statement - extractive body cue:** CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We frst evaluate our method by varying the number of demonstrations on the Pack Bat.tezy task in simulation, as shown in Figure 7 (a).
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Our method effectively, leverages the powerful visualsemantic understanding capabilities of VLMs and benefits from explicit spatial relation reasoning using 3D representations.
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** For the simulation experiments, we compare our method against the following baselines:
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations.
- **Contribution anchor:** p. 3 (B. Foundational Vision Model for Roboties), p. 4 (A. Problem Statement), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm)

### Strongest assumption and failure boundary

- **p. 3 / A. Problem Statement - extractive body cue:** For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, ...
- **p. 3 / A. Problem Statement - extractive body cue:** Notably, we show in Section IV-B that the current state-of the-art methods can fail to achieve a high success rate even with extensive training demonstrations
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ...
- **p. 9 / V. ConcLusion - extractive body cue:** In our experiments, we first identify the key limitations of existing imitation learning algorithms.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (b) Failure Breakdown of Two Special Scenarios
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure primarily occurs at the task stage with the highest ambiguity, demonstrating a strong cconrelation between policy failure and task ambiguity.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Additional analysis and visualizations of 3D attention failure cases are provided in the
- **Boundary to test:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an intermediate representation. | p. 3 (B. Foundational Vision Model for Roboties), p. 4 (A. Problem Statement) |
| Reported outcome | While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus as the number of demonstrations further increases, ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| Failure/limitation | Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (V. ConcLusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We first generate intermediate code from the instruction {and multiView RGBD observations 0, € RA*!W 4, where AC is the number of camera views, and H and W represent the ... (p. 4, A. Problem Statement).
- **Paper-specific mechanism:** To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language. (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets semantic meanings from abstract instructions. Given ... (p. 10, Figure/Table caption); the relevant task/metric cue is We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even with extensive demonstrations, indicating that additional training data alone may oot resolve ... (p. 6, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task ... (p. 7, B. Analysis of Existing Imitation Learning Algorithm).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, language grounding, code generation, 3D attention, diffusion policy, contact-rich manipulation`.
- **Reading predecessor in the generated track queue:** ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We first generate intermediate code from the instruction {and multiView RGBD observations 0, € RA*!W 4, where AC is the number of camera views, and H and W represent the ... (p. 4, A. Problem Statement); preserve the objective/update rule: Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations. (p. 6, B. Analysis of Existing Imitation Learning Algorithm).
2. Use the paper-reported task/data/environment cue: and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in handling language ambiguity. (p. 2, 3) We conduct extensive evaluations of individual modules).
3. Compare against the reported or matched baseline: For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such as successfully following the language instruction or picking ... (p. 6, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even with extensive demonstrations, indicating that additional training data alone may oot resolve ... (p. 6, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: For DP, we consider two variants - DP with RGB inputs, denoted as "DP (RGB)", and DP with point cloud inputs, denoted as "DP (PCD)". (p. 6, B. Analysis of Existing Imitation Learning Algorithm); if none is reported, design one around: Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task ... (p. 7, B. Analysis of Existing Imitation Learning Algorithm).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 3 (B. Foundational Vision Model for Roboties), match the reported outcome at p. 10 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), and measure the boundary at p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (IV. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (We first generate intermediate code from the instruction {and multiView RGBD observations 0, € RA*!W 4, where AC is the number of ...), does the paper-specific mechanism (To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language.) retain the reported evaluation outcome (We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even ...) when tested against the paper's strongest explicit boundary (Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language. (p. 1, Abstract).
- **Paper-supported outcome:** Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets semantic meanings from abstract instructions. Given ... (p. 10, Figure/Table caption).
- **Strongest explicit boundary:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task ... (p. 7, B. Analysis of Existing Imitation Learning Algorithm).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
