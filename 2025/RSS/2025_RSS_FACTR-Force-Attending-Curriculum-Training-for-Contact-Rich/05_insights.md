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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image at time 1), and (ii) an external ...를 attends to vision vs. force tokens at layer [, and will be the Finally, we project the decoder output H/? to action space,로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance FACTR's applicabil ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: For the decoder, we introduce & action tokens, A ¢ R**¢.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile/force, force feedback, contact-rich manipulation, Imitation Learning, curriculum learning`.
- **Reading predecessor in the generated track queue:** Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance FACTR's applicabil ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with unseen visual appearances and geometries,.
3. Compare against the body-reported baseline or a matched simpler baseline: ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR?.
4. Report the body metric and its denominator/aggregation: We present the average success rate for truining and testing objects, respectively..
5. Re-run the body-reported ablation/failure condition: We discuss more detailed ablations ‘on the curriculum in See..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model); the primary result is directionally consistent at p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 7 (C. Policy Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 decoder, introduce, action mechanism이 ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ... 대비 We present the average success rate for truining and testing objects, respectively.을 개선하고, Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
