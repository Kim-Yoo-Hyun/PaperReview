# Insights — On Bringing Robots Home

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.16098; PDF retrieval source: https://arxiv.org/pdf/2311.16098. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 1 Introduction - extractive body cue:** In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.
- **p. 1 / Abstract - extractive body cue:** Success 81% Pick up hat Open microwave door Pick up paper towel roll Place rag in laundry Open cabinet door Close cabinet door Open shower ...
- **p. 7 / C D - extractive body cue:** Our method can be divided into four broad stages: (a) designing a hardware setup that helps us in the collection of demonstrations and their seamless ...
- **p. 1 / Abstract - extractive body cue:** Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb·E can reliably ...
- **p. 4 / 1 Introduction - extractive body cue:** For user comfort, we have developed an ergonomic demonstration collection tool, enabling us to gather task-specific demonstrations in unfamiliar homes without direct robot operation.
- **p. 4 / 1 Introduction - extractive body cue:** This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home ...
- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **Contribution anchor:** p. 4 (1 Introduction), p. 1 (Abstract), p. 7 (C D), p. 1 (Abstract), p. 4 (1 Introduction), p. 4 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 4 / 1 Introduction - extractive body cue:** Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments or in academic ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and with depth (third row). The depth values (bottom row) ...
- **p. 17 / 3 Experiments - extractive body cue:** We discuss the failure cases further in Section 3.3.
- **p. 17 / 3 Experiments - extractive body cue:** Once we turned on an overhead light for even lighting, there were no more failures.
- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 23 / 3 Experiments - extractive body cue:** This failure mode points to the need of better designed, less bare-boned robot grippers for household tasks.
- **Boundary to test:** Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed onto a red book on a different ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort. | p. 4 (1 Introduction), p. 1 (Abstract) |
| Reported outcome | Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. In under 30 mins of training per task, Dobb·E achieves ... | p. 1 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Failure/limitation | Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed onto a red book on a different ... | p. 20 (Figure/Table caption), p. 19 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired actions.를 On average, only using 91 seconds of data on each task collected over five minutes, Dobb·E can achieve a 81% success rate in homes (see Section 3). • Impact of effective SSL ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed onto a red book on a different ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, home robotics, whole-body autonomy`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed onto a red book on a different ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . . . . . . . . . ....
3. Compare against the body-reported baseline or a matched simpler baseline: Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use to run our baselines and ablations..
4. Report the body metric and its denominator/aggregation: 0 20 40 60 80 100 Success rate (%) Air-fryer closing Cushion flipping Door closing Drawer closing Chair pulling Pulling from shelf Bag pickup Drawer opening Towel pickup Unplugging Tissue pickup Door ....
5. Re-run the body-reported ablation/failure condition: The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some featureless task object, for example a door ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (1 Introduction), p. 6 (C D), p. 6 (C D); the primary result is directionally consistent at p. 1 (Figure/Table caption), p. 22 (Figure/Table caption), p. 21 (3 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, Dobb, framework mechanism이 Alongside these household experiments, we also set up a "home" area in our lab, with a ... 대비 0 20 40 60 80 100 Success rate (%) Air-fryer closing Cushion flipping Door closing Drawer closing Chair ...을 개선하고, Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
