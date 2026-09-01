# Insights — RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p028.html; PDF retrieval source: https://arxiv.org/pdf/2412.09858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To fine-tune the model on our RL-generated dataset, we use the public model weights pre-trained on 970 thousand Open X-Embodiment dataset (Collaboration et al., 2024) ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 4 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting ...
- **p. 1 / 1. Introduction - extractive body cue:** This challenge affects all robotic tasks but becomes particularly pronounced in scenarios requiring precise control and dexterity, such as contact-rich manipulation.
- **p. 9 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.
- **p. 9 / 5.1. Is RL data better because of better action - extractive body cue:** However, an interesting RL-specific failure mode was observed: objects were sometimes dropped too early, bouncing out of the bowl.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference speed limitations.
- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** (B) Pick and Place involves an unseen scenario that tests the policy's visual robustness to different backgrounds and objects.
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** 4, the RL policy success rate quickly degraded from 20/20 for the training scenario to 1/20 for the unseen scenario of the Pick and Place ...
- **Boundary to test:** The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data for robotic foundation models. | p. 1 (1. Introduction), p. 4 (3.3. Generalist Policy Finetuning) |
| Reported outcome | When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect success rate in both scenarios while the performance ... | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption) |
| Failure/limitation | The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task. | p. 9 (4.3. Generalization of RLDG vs. Original RL), p. 9 (5.1. Is RL data better because of better action) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 It takes a single image as observation input along with a language instruction.를 Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data for robotic foundation models.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, generalist policy, policy distillation, robot data, real-world manipulation`.
- **Reading predecessor in the generated track queue:** Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3 (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic manipulation methods..
3. Compare against the body-reported baseline or a matched simpler baseline: On the precise FMB Insertion and Connector Insertion tasks, where we anticipated the generalist to benefit the most from higher quality training data, OpenVLA with RLDG saw 33% and 23% higher success ....
4. Report the body metric and its denominator/aggregation: When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect success rate in both scenarios while the performance ....
5. Re-run the body-reported ablation/failure condition: To further investigate the effectiveness of RLDG, we conduct a scaling experiment studying the success rate of OpenVLA policies on a seen VGA connector and an unseen Type-C connector when fine-tuned on ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning); the primary result is directionally consistent at p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption), p. 6 (4.2. RLDG vs. Conventional Fine-tuning); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 tackle, challenge, Reinforcement mechanism이 On the precise FMB Insertion and Connector Insertion tasks, where we anticipated the generalist to benefit ... 대비 When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring ...을 개선하고, The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
