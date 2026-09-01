# Insights — ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To mitigate this issue, we introduce a termination curriculum that progressively refines the motion error tolerance throughout training, guiding the policy toward improved tracking performance, ...
- **p. 5 / C. Fine-tuning Motion Tracking Policy under New Dynamics - extractive body cue:** In this section, we present extensive experimental results oon three policy transfers: IsaaeGym [58] to IsaacSim [63], IsaaeGym to Genesis [6], and IsiaeGym to real-world ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **Contribution anchor:** p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (C. Fine-tuning Motion Tracking Policy under New Dynamics), p. 4 (B. Phase-based Motion Tracking Policy Training)

### Strongest assumption and failure boundary

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Crucially, because the actor does not depend on position-based motion targets, ‘our approach eliminates the need for odometry during real world deployment-overcoming a well-documented challenge ...
- **p. 2 / Abstract - extractive body cue:** the sim-to-teal gap, especially when real-world dynamics fall outside the modeled distribution.
- **p. 2 / Abstract - extractive body cue:** However, most prior work [46, 74, 47, 73, 107, 19, 95, 50] has primarily focused ‘on locomotion, treating the legs as a means of mobility.
- **p. 3 / Abstract - extractive body cue:** This model effectively serves as a residual correction term for the dynamics gap.
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.
- **Boundary to test:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP | p. 1 (Abstract), p. 2 (Abstract) |
| Reported outcome | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution (grea) and ... | p. 10 (Figure/Table caption) |
| Failure/limitation | Such structured discrepancies cannot be effectively captured by merely adding uniform action noise. | p. 11 (C. Does ASAP Fine-Tuning Outperform Random Action Noise), p. 12 (B. Offine and Online System Identification for Roboties) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective actions based on the current state sy ...를 Wwe tin the dea action model by minimizing the discrepancy between simulation sales; and real-world sates () Policy Fine-taning: We freeze the ‘eli action model incorporate ito the siilator o align the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, sim-to-real, residual dynamics`.
- **Reading predecessor in the generated track queue:** HumanPlus: Humanoid Shadowing and Imitation from Humans (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 ()..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution (grea) and ....
4. Report the body metric and its denominator/aggregation: settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors..
5. Re-run the body-reported ablation/failure condition: Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution (grea) and ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model), p. 5 (B. Training Delta Action Model); the primary result is directionally consistent at p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 mnparal-, result, overly mechanism이 Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. ... 대비 settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion ...을 개선하고, Such structured discrepancies cannot be effectively captured by merely adding uniform action noise. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
