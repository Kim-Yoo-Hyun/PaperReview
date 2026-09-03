# Insights — BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p068.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p068.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** In this work, we introduce BEAMDOJO, a novel reinforcement learning-based framework for controlling humanoid robots traversing risky terrains with sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** + We propose BEAMDOIO, a two-stage RL framework that combines a newly designed foothold reward for the polygonal foot model and a double critic, enabling ...
- **p. 3 / A. Foothold Reward - extractive body cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 1 / Body text (section not recovered) - extractive body cue:** 1: Our proposed framework, BEAMDOJO, enables agile and robust humanoid locomotion across challenging sparse foothold.
- **p. 2 / A. Locomotion on Sparse Footholds - extractive body cue:** Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based controllers [15, 61, ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** We begin by defining a samplingbased foothold reward, designed to evaluate the foot placement ‘of a polygonal foot model. ‘To address the challenge of sparse ...
- **Contribution anchor:** p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (A. Foothold Reward), p. 1 (Body text (section not recovered)), p. 2 (A. Locomotion on Sparse Footholds)

### Strongest assumption and failure boundary

- **p. 1 / 1. INrRopucTION - extractive body cue:** However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference
- **p. 1 / Abstract - extractive body cue:** Traversing risky terrains with sparse footholds poses f significant challenge for humanoid robot iri foot placements and stable locomotion.
- **p. 2 / 1. INrRopucTION - extractive body cue:** Enabling agile movement on risky terrains for humanoid robots presents several challenges.
- **p. 2 / 1. INrRopucTION - extractive body cue:** Additionally, obtaining reliable percep tual information is challenging due to sensory limitations and environmental noise [66]
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive body cue:** In contrast, this work introduces a novel two-stage training approach specitically aimed at improving sample efficiency, particularly addressing. the challenge of early termination when walking ...
- **p. 10 / 7 Single Leg Support ) Stand Still - extractive body cue:** 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.
- **p. 8 / B. Simulation Experiments - extractive body cue:** Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected by the noise of unstable locomotion signals, ...
- **Boundary to test:** 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. | p. 1 (Abstract), p. 2 (1. INrRopucTION) |
| Reported outcome | 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels (terrain level 6 and level 8, respectively) in ‘Table II. | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup) |
| Failure/limitation | 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig. | p. 10 (7 Single Leg Support ) Stand Still), p. 8 (B. Simulation Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 1) Observation Space and Action Space: ‘The policy observations, denoted a8 o,, consist of four components: 0 = [61 0f°"*, of", a ® ‘The commands ¢; € R° specify the desired velocity, ...를 We let the humanoid robot traverse the terrain F, receiving proprioceptive observations, while providing perceptual feedback in the form of the elevation map of terrain T at the corresponding humanoids base position, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, perceptive locomotion, sparse footholds, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work..
3. Compare against the body-reported baseline or a matched simpler baseline: This requires a distinct gait compared to regular Jocomotion tasks..
4. Report the body metric and its denominator/aggregation: single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains..
5. Re-run the body-reported ablation/failure condition: Gait Regularization: The combination of small-scale gait regularization rewards with sparse foothold reward can hinder gait performance, as shown in Table Ill, where the naive design and the ablation without the double ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (A. Locomotion on Sparse Footholds), p. 2 (1. INrRopucTION), p. 1 (Abstract); the primary result is directionally consistent at p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 8 (B. Simulation Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, challenges, introduce mechanism이 This requires a distinct gait compared to regular Jocomotion tasks. 대비 single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains.을 개선하고, 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
