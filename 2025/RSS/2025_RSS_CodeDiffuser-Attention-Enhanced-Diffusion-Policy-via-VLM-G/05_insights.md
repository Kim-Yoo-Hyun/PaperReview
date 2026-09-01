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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 [ plalz = =)p(= = z1lor,2), Where 2 is a task-relevant latent representation of the state such that p(ajo,l,2 = =) = plalz = =). ie, 2% contains enough information about the ...를 In Section II-C, we describe the API provided to the code generation process used to construct our state representation 44, 3D attention map that highlights task-relevant regions Finally, this 3D attention map ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an intermediate representation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, language grounding, code generation, 3D attention, diffusion policy, contact-rich manipulation`.
- **Reading predecessor in the generated track queue:** ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in handling language ambiguity..
3. Compare against the body-reported baseline or a matched simpler baseline: We find that our policy consistently outperforms the baselines by leveraging VLMgenerated code as an interpretable and executable intermediate representation, effectively utilizing the visual-semantic reasoning capabilites of the VLM..
4. Report the body metric and its denominator/aggregation: Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task success rates ....
5. Re-run the body-reported ablation/failure condition: For DP, we consider two variants - DP with RGB inputs, denoted as "DP (RGB)", and DP with point cloud inputs, denoted as "DP (PCD)"..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm); the primary result is directionally consistent at p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contrast, framework, capable mechanism이 We find that our policy consistently outperforms the baselines by leveraging VLMgenerated code as an interpretable ... 대비 Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ...을 개선하고, Similarly, as the number of placement options increases, most failures occur during the placement stage of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
