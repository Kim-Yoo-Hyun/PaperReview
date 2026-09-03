# Insights — Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html; PDF retrieval source: https://arxiv.org/pdf/1903.09537. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / IV. METHODS - extractive body cue:** In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarize, this paper makes the following contributions: • We present a simple-yet-effective technique to reconstruct policies from only a small number of samples, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** In this section, we present results for using DASS to compress and distill multiple policies.
- **p. 3 / IV. METHODS - extractive body cue:** For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = {} 2: Reset ...
- **p. 3 / IV. METHODS - extractive body cue:** 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to ...
- **p. 4 / IV. METHODS - extractive body cue:** At each iteration, we will estimate ∇θtJrl using the usual policy gradient algorithm, and update θ according to θt+1 = θt + α(∇θtJrl -w∇θtJsp).
- **Contribution anchor:** p. 3 (IV. METHODS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 3 (IV. METHODS), p. 3 (IV. METHODS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This offers a strong alternative to "fine-tuning" approaches, where an existing policy may be adapted via small changes and additions to an existing reward function, ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** The goal of reinforcement learning is to find a policy π, parameterized by θ, where πθ : S × A →[0, ∞) is the probability ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** More formally, we aim to solve the following optimization problem:
- **p. 3 / III. PRELIMINARIES - extractive body cue:** This causes the well-known covariate shift problem, where the student policy will accumulate errors overtime and eventually drift to states that were not seen by ...
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the final policies to adapt to other noise.
- **Boundary to test:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to combine imitation learning and reinforcement learning. | p. 3 (IV. METHODS), p. 1 (I. INTRODUCTION) |
| Reported outcome | Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient samples, we allow for the iterative design of ... | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty. | p. 8 (VIII. CONCLUSION AND DISCUSSION), p. 8 (VIII. CONCLUSION AND DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 2, where the blue curves represent the limit cycle produced by a deterministic policy, and the green arrows represent the deterministic feedback actions associated with the additional states resulting from the execution ...를 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to the limit cycle. an expert with no ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to combine imitation learning and reinforcement learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, Cassie`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests can be moved from simulation to hardware by copying files ....
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable policies. Compared to the (256, 256) network, ....
4. Report the body metric and its denominator/aggregation: Training Framework We adopt the framework used in [41] for training several initial policies πe, where we reward the agent for producing motion that approximately reproduces a set of specified reference motions..
5. Re-run the body-reported ablation/failure condition: At each level, all policies are trained from scratch instead of fine-tuning the previous policies..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 4 (IV. METHODS); the primary result is directionally consistent at p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, present, collecting mechanism이 Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger ... 대비 Training Framework We adopt the framework used in [41] for training several initial policies πe, where we reward ...을 개선하고, The final policies obtained are robust to unmodeled noise and enable us to transfer them from ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
