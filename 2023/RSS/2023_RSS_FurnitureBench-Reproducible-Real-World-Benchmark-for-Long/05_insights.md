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

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks.를 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or exceeds 3000 steps in total.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions and different levels of challenges. Figure 18 ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on a realistic ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Benchmark, assembly, long-horizon manipulation, real-world evaluation, reproducibility`.
- **Reading predecessor in the generated track queue:** OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions and different levels of challenges. Figure 18 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: But, this benchmark environment and tasks can be also used for research in TAMP..
3. Compare against the body-reported baseline or a matched simpler baseline: We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods..
4. Report the body metric and its denominator/aggregation: Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color indicates each ....
5. Re-run the body-reported ablation/failure condition: 3This paper focuses on benchmarking end-to-end learning approaches since engineering furniture assembly procedures using TAMP without having access to state information is beyond the scope of this paper..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract); the primary result is directionally consistent at p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. 대비 Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the ...을 개선하고, Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
