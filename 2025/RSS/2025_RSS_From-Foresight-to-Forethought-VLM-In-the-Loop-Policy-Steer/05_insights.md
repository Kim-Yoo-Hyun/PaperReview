# Insights — From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p076.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p076.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks ...
- **p. 4 / 1. InTRopucTION - extractive body cue:** The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** Ultimately, this alignment step enables ‘our "VLM-in-the-loop" policy steering approach to interpret, action plans as behavior narrations and select high-quality plans by reasoning over those ...
- **p. 1 / Front matter - extractive body cue:** 1: We present FOREWARN, an VLM-in-the-loop policy steering algorithm for multi-modal generative robot policies.
- **p. 1 / Abstract - extractive body cue:** We validate our framework across diverse robotic manipulation tasks, demonstrating its ability to bridge representational gaps and provide robust, generalizable policy steering.
- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the VLM.
- **Contribution anchor:** p. 8 (B. Policy Steering for Open-World Alignment), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 1 (Front matter), p. 1 (Abstract), p. 9 (B. Policy Steering for Open-World Alignment)

### Strongest assumption and failure boundary

- **p. 3 / 1. InTRopucTION - extractive body cue:** Initially, it may be tempting use the VLM directly as a black-box solver of Eq.1 (ie. t0 solve the overarching behavior generation problem) by simply ...
- **p. 1 / 1. InTRopucTION - extractive body cue:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown ...
- **p. 3 / 1. InTRopucTION - extractive body cue:** However, this strategy is sampleinefficient, requiring extensive embodied rollouts and human annotations to generate labels, Instead, we propose tackling the problem in Eq.1 in a ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** complexity of dynamics modeling and the difficulty of hand
- **p. 2 / 1. InTRopucTION - extractive body cue:** Here, existing approaches [22, 24, 25] often rely on out-of-distribution (OOD) detection in a latent space or dense human labels to train a binary classifier ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced failures (e.g., crushing the chips inside the ...
- **Boundary to test:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks are included in Appendix B2. | p. 8 (B. Policy Steering for Open-World Alignment), p. 4 (1. InTRopucTION) |
| Reported outcome | V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Failure/limitation | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 The robot's observations 0 < O :=ZxQ combine RGB image data I € T and proprioceptive states q © Q(eg., end-effector pose, gripper state), and ay := ay.¢.7 denotes a robot's T ...를 The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world model to accurately predict the outcomes of ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks are included in Appendix B2.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, VLM verifier, policy steering, failure prevention, latent alignment`.
- **Reading predecessor in the generated track queue:** Unified Video Action Model (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying VLMs. Only FOREWARN and FOREWARN-Oracle consistently produce accurate ....
4. Report the body metric and its denominator/aggregation: V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec..
5. Re-run the body-reported ablation/failure condition: VLM Fine-tuning, We construct our VQA dataset for fine-tuning from the same offline dataset, Dyyy, used to train the world model..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 9 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 8 (B. Policy Steering for Open-World Alignment); the primary result is directionally consistent at p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Figure, present, examples mechanism이 Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth ... 대비 V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task ...을 개선하고, We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
