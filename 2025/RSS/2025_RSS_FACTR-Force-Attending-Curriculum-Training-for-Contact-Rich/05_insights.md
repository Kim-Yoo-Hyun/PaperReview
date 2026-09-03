# Insights — FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p079.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p079.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** For the decoder, we introduce & action tokens, A ¢ R**¢.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** then tokenized by a vision encoder and a force encoder before fed into an action transformer to regress joint position targets gee.
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image ...
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Each trajectory in D comprises tuples (I;,7:, 1).
- **Contribution anchor:** p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model)

### Strongest assumption and failure boundary

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes.
- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** This limitation can particularly affect tasks that involve subtle force adjustments during finegrained manipulation since the torque readings can be too noisy to be used ...
- **p. 7 / C. Policy Evaluation - extractive body cue:** 6, All the policies perform similarly on the train objects for most tasks, except for the rolling dough task, where the vision-only policy smashes the ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** FACTR leads to better recovery behavior.
- **Boundary to test:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance FACTR's applicabil ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | For the decoder, we introduce & action tokens, A ¢ R**¢. | p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Reported outcome | For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating force. | p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation) |
| Failure/limitation | Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance FACTR's applicabil ... | p. 9 (VI. CONCLUSION AND LIMITATIONS), p. 8 (C. Policy Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image at time 1), and (ii) ... (p. 4, A. Problem Statement and Base Model).
- **Paper-specific mechanism:** For the decoder, we introduce & action tokens, A ¢ R**¢. (p. 5, A. Problem Statement and Base Model).
- **Evidence boundary:** the reported outcome is Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation); the relevant task/metric cue is Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile/force, force feedback, contact-rich manipulation, Imitation Learning, curriculum learning`.
- **Reading predecessor in the generated track queue:** Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance FACTR's applicabil ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image at time 1), and (ii) ... (p. 4, A. Problem Statement and Base Model); preserve the objective/update rule: Each trajectory in D comprises tuples (I;,7:, 1). (p. 4, A. Problem Statement and Base Model).
2. Use the paper-reported task/data/environment cue: We observe that for tasks that require continuous contact between the arm and an object, such as non-prehensile pivoting and bimanual box lifting, the un-actuated teleoperation system often causes the ... (p. 7, B. Teleoperation Evaluation).
3. Compare against the reported or matched baseline: ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR? (p. 7, C. Policy Evaluation).
4. Report the body metric with its denominator and aggregation: Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation).
5. Re-run the reported ablation or stress/failure condition: We discuss more detailed ablations ‘on the curriculum in See. (p. 7, C. Policy Evaluation); if none is reported, design one around: While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 5 (A. Problem Statement and Base Model), p. 1 (Abstract), match the reported outcome at p. 7 (B. Teleoperation Evaluation), p. 9 (C. Policy Evaluation), p. 7 (C. Policy Evaluation), and measure the boundary at p. 8 (C. Policy Evaluation), p. 7 (C. Policy Evaluation).

## Falsifiable research question

Under the paper's stated interface (We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual ...), does the paper-specific mechanism (For the decoder, we introduce & action tokens, A ¢ R**¢.) retain the reported evaluation outcome (Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% ...) when tested against the paper's strongest explicit boundary (While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** For the decoder, we introduce & action tokens, A ¢ R**¢. (p. 5, A. Problem Statement and Base Model).
- **Paper-supported outcome:** Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation).
- **Strongest explicit boundary:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
