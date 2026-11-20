# Insights — RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.01977; PDF retrieval source: https://arxiv.org/pdf/2311.01977. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose to use a coarse trajectory as a middle-ground solution between expressiveness and ease of use.
- **p. 3 / 3 METHOD - extractive body cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 4 / 3 METHOD - extractive body cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive body cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.
- **p. 3 / 3 METHOD - extractive body cue:** We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments show that RT-Trajectory outperforms existing policy conditioning techniques, particularly in terms of generalization to novel motions, an open challenge in robotics.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The pursuit of generalist robot policies has been a perennial challenge in robotics.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests an intriguing opportunity: if a trajectory-conditioned robot ...
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a few remaining limitations.
- **Boundary to test:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in the first two rows, suboptimal trajectory prompts ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are described in App. B.3. The resulting trajectory sketches ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in the first two rows, suboptimal trajectory prompts ... | p. 22 (Figure/Table caption), p. 8 (3. What emergent capabilities are enabled by RT-Trajectory?) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 Human Demonstration Videos with Hand-object Interaction First-person human demonstration videos are an alternative input.를 Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and trajectory sketch.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in the first two rows, suboptimal trajectory prompts ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, VLA, trajectory representation, spatial reasoning, task generalization`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in the first two rows, suboptimal trajectory prompts ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Can RT-Trajectory generalize to tasks beyond those contained in the training dataset?.
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper interactions of query trajectories to the first gripper interactions of the most similar training trajectories, as ....
4. Report the body metric and its denominator/aggregation: Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen motions in novel ways or generalizing to new ....
5. Re-run the body-reported ablation/failure condition: Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in the first two rows, suboptimal trajectory prompts ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 METHOD), p. 3 (3 METHOD), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contribution, novel mechanism이 Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper ... 대비 Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of ...을 개선하고, Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
