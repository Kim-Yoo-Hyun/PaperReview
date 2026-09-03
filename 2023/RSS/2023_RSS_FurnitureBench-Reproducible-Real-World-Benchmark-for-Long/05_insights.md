# Insights — FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.12821; PDF retrieval source: https://arxiv.org/pdf/2305.12821. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **p. 1 / Abstract - extractive body cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive body cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, we provide FurnitureSim, a fast and realistic simulator of FurnitureBench.
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To further robotics research toward solving people's everyday tasks, it is crucial to tackle challenges in more complex and longer-horizon tasks.
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset highlights the need for further algorithmic improvements ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** It always achieves the phase 3 (grasping the leg) but fails at inserting 60% of the time.
- **Boundary to test:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions and different levels of challenges. Figure 18 ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on a realistic ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Failure/limitation | Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions and different levels of challenges. Figure 18 ... | p. 18 (Figure/Table caption), p. 7 (VI. BENCHMARKING RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks. (p. 2, I. INTRODUCTION).
- **Paper-specific mechanism:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color ... (p. 8, Figure/Table caption); the relevant task/metric cue is The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. (p. 7, VI. BENCHMARKING RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align a screw and a hole, ... (p. 7, VI. BENCHMARKING RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Benchmark, assembly, long-horizon manipulation, real-world evaluation, reproducibility`.
- **Reading predecessor in the generated track queue:** OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions and different levels of challenges. Figure 18 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks. (p. 2, I. INTRODUCTION); preserve the objective/update rule: (Right) A suite of 8 furniture models in our benchmark. (p. 1, Body text (section boundary not confidently recovered)).
2. Use the paper-reported task/data/environment cue: But, this benchmark environment and tasks can be also used for research in TAMP. (p. 7, VI. BENCHMARKING RESULTS).
3. Compare against the reported or matched baseline: We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. (p. 6, V. EXPERIMENTAL SETUP).
4. Report the body metric with its denominator and aggregation: The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. (p. 7, VI. BENCHMARKING RESULTS).
5. Re-run the reported ablation or stress/failure condition: 3This paper focuses on benchmarking end-to-end learning approaches since engineering furniture assembly procedures using TAMP without having access to state information is beyond the scope of this paper. (p. 7, VI. BENCHMARKING RESULTS); if none is reported, design one around: On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align a screw and a hole, ... (p. 7, VI. BENCHMARKING RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 8 (Figure/Table caption), p. 8 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), and measure the boundary at p. 7 (VI. BENCHMARKING RESULTS), p. 9 (VI. BENCHMARKING RESULTS).

## Falsifiable research question

Under the paper's stated interface (Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation ...), does the paper-specific mechanism (The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers ...) retain the reported evaluation outcome (The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" ...) when tested against the paper's strongest explicit boundary (On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align a screw and a hole, ... (p. 7, VI. BENCHMARKING RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
