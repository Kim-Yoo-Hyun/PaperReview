# Insights — VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** We introduce VLR-Driver, a visual-language-reasoning model developed for embodied AD.
- **p. 4 / 3. Method - extractive body cue:** We present the motivation and design details of our VLRDriver framework.
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** To address this limitation, we introduce consecutive frames I = {If, Ifr, Ifl, Ib, Ibl, Ibr}Tnow t=Tnow-T into the model, allowing it to track temporal ...
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** In this scenario, where some vehicles are illegally parked ahead and blocking the lane, our method can conduct hierarchical patiotemporal reasoning analysis and make a ...
- **p. 6 / 3.3. Training Paradigm - extractive body cue:** Specifically, we first generate multiple candidate decision answers for the current driving scenario using prompts within the VLR model; Then, following our ST-CoT strategy, the ...
- **p. 6 / 3.3. Training Paradigm - extractive body cue:** We use LoRA for all linear modules, which not only saves computation but also ensures the performance of the model.
- **Contribution anchor:** p. 4 (3.2.1. Perception Level CoT), p. 2 (Body text (section not recovered)), p. 4 (3. Method), p. 5 (3.2.1. Perception Level CoT), p. 5 (3.2.1. Perception Level CoT), p. 6 (3.3. Training Paradigm)

### Strongest assumption and failure boundary

- **p. 2 / Body text (section not recovered) - extractive body cue:** However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.
- **p. 2 / Body text (section not recovered) - extractive body cue:** Moreover, most VLMs are trained on internet data, lacking spatial understanding and specialized training in the field of AD, making it difficult for them to ...
- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** A critical aspect of safe driving is identifying potential risk points within the current lane.
- **p. 4 / 3.1. Overview - extractive body cue:** At the same time, there are also the current position (x, y) of ego vehicle, the speed v, the target point position (p, q).
- **p. 7 / 4.1. Data Collection - extractive body cue:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical reasoning, ...
- **Boundary to test:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, Stop Sign infractions, Off-Road infractions, Agent Blocked, ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning for driving decisions. | p. 4 (3.2.1. Perception Level CoT), p. 2 (Body text (section not recovered)) |
| Reported outcome | We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR). | p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods) |
| Failure/limitation | CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, Stop Sign infractions, Off-Road infractions, Agent Blocked, ... | p. 7 (4.1. Data Collection), p. 3 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The forward pass is computed as: y = W ′x =  W0 + α r B · A  x, (2) where y is the output and x is input.를 Subsequently, the compressed and cropped image data and the information from the ego's sensors are input into the model.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, Stop Sign infractions, Off-Road infractions, Agent Blocked, ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning for driving decisions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, Stop Sign infractions, Off-Road infractions, Agent Blocked, ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset includes 20,000 sets of multi-frame, multi-angle image data collected from various road conditions such as urban, rural, and highways in the CARLA simulator, covering over 30 specific complex traffic scenarios ....
3. Compare against the body-reported baseline or a matched simpler baseline: It can be seen that our method outperforms other methods in key metrics such as DS, RC, and SR, achieving first place and effectively improving DS by 17.5%, mean advanced driving ability ....
4. Report the body metric and its denominator/aggregation: We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR)..
5. Re-run the body-reported ablation/failure condition: The experimental configurations include four variants: (1) Without utilizing our proposed spatiotemporal CoT strategy, using only a question-based approach without reasoning guidance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3.3. Training Paradigm), p. 6 (3.3. Training Paradigm), p. 4 (3. Method); the primary result is directionally consistent at p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 enables, VLR, model mechanism이 It can be seen that our method outperforms other methods in key metrics such as DS, ... 대비 We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), ...을 개선하고, CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
