# Insights — MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are:
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to render robots in a camera pose that is within the distribution of the training image poses.
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to transfer between robots with different numbers of joints and compensate for alternate gripper shapes across embodiments.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 3 (1) We assume knowledge of the two robots' coordinate), p. 3 (1) We assume knowledge of the two robots' coordinate), p. 4 (4) We assume that the background and lighting conditions)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** This allows us to separate any challenges that arise due to changes in the background environment and focus on the impact of visual differences between ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Mirage leverages the following assumptions and design choices to reduce the gap between robots and enable zero-shot transfer:
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Prior work [108] has found aligning the action and observation spaces can facilitate policy transfer.
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source policy ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...
- **Boundary to test:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our key contributions are: | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Reported outcome | Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption) |
| Failure/limitation | Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (2) Can Mirage successfully zero-shot transfer trained vision) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Mirage applies to both first-person and third-person camera views and policies that take in both states and images as inputs or only images as inputs. (p. 1, Abstract).
- **Paper-specific mechanism:** To summarize, our key contributions are: (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS); the relevant task/metric cue is that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. (p. 2, 3) Physical experiments with Franka and UR5 demonstrating). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, cross-embodiment, zero-shot transfer, policy transfer, manipulation, domain adaptation`.
- **Reading predecessor in the generated track queue:** VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Mirage applies to both first-person and third-person camera views and policies that take in both states and images as inputs or only images as inputs. (p. 1, Abstract); preserve the objective/update rule: Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: To motivate the study, imagine there is a source robot ("oracle") teaching a target robot to perform a task side by side in a duplicate environment. (p. 4, IV. STATE-BASED TRANSFER EXPERIMENTS).
3. Compare against the reported or matched baseline: that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. (p. 2, 3) Physical experiments with Franka and UR5 demonstrating).
4. Report the body metric with its denominator and aggregation: that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. (p. 2, 3) Physical experiments with Franka and UR5 demonstrating).
5. Re-run the reported ablation or stress/failure condition: Bridging the Visual Gap To replace the robots, we leverage the knowledge of the robot URDFs and camera poses to perform cross-painting at test time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS); if none is reported, design one around: Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), and measure the boundary at p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (Mirage applies to both first-person and third-person camera views and policies that take in both states and images as inputs or only ...), does the paper-specific mechanism (To summarize, our key contributions are:) retain the reported evaluation outcome (that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from ...) when tested against the paper's strongest explicit boundary (Less robust source policies leave little room for error, while more robust ones tend to retry even if ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To summarize, our key contributions are: (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
- **Strongest explicit boundary:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
