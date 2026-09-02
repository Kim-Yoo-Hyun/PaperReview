# Insights — Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/file/430894999584d0bd358611e2ecf00b15-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Habitat 3.0 - a simulator that supports both humanoid avatars and robots for the study of collaborative human-robot tasks in ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework is open-sourced, for more details see Appendix A.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent layers, resulting nearly ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A simulation platform can overcome these challenges; however, the development of a collaborative human-robot simulation platform also comes with its own complexities.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Today's embodied AI agents are largely hermits - existing within and navigating through virtual worlds as solitary occupants (Batra et al., 2020; Anderson et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We conduct an in-depth study of learned and heuristic baselines on both tasks, with a focus on generalization to new scenes, layouts and collaboration partners.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Hence the high-level policy is not robust to low-level execution failures.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks.
- **Boundary to test:** Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the center and the front of the robot ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of removing sensors. Scenes and Robot. We incorporate the ... | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Failure/limitation | Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the center and the front of the robot ... | p. 17 (A.1 SOCIAL NAVIGATION), p. 19 (A.2 SOCIAL REARRANGEMENT) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 The policy uses a ResNet-18 (He et al., 2016) visual encoder to embed the 256 × 256 depth input image into a 512 dimension embedding.를 (2019)) to generate realistic body shapes and poses, (4) a library of avatars made from 12 base models with multiple gender representations, body shapes, and appearances, (5) a motion and behavior generation ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the center and the front of the robot ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, simulation, human-robot interaction, social navigation, humanoid, mobile manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the center and the front of the robot ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m away from the humanoid..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. We use 3 seeds for each model. path ....
4. Report the body metric and its denominator/aggregation: Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. We measure the trained agents' performance when evaluated ....
5. Re-run the body-reported ablation/failure condition: Among the ablations, removing the sensors used in original training make learning slower, with primitive actions having the most effect..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 19 (A.2 SOCIAL REARRANGEMENT); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Social, tasks, Aiming mechanism이 Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and ... 대비 Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to ...을 개선하고, Since the Spot robot has a long body shape and cannot be represented by a single ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
