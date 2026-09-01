# Insights — Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.05189v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / Abstract - extractive body cue:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 1 / Abstract - extractive body cue:** (Bottom) A POGS unified representation enables language querying, grasp sampling, and continuous tracking of irregular objects as they move.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The drill handle is fully occluded by the motor body, yet our POGS unified representation enables handle grasping based on previously observed geometry.
- **p. 2 / Abstract - extractive body cue:** Our approach aims to achieve robust online object tracking and scene updating with
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature supervision ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These features are then supervised into the gaussians, enabling the model to render them at deployment time for optimizing object tracking objectives, similar to the ...
- **Contribution anchor:** p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** Recently introduced Gaussian Splats [1] efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.
- **p. 1 / Abstract - extractive body cue:** The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and the ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** This feature loss measures how well the current pose estimates visually align the rendered model with the actual objects.
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning ...
- **Boundary to test:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects due to degraded tracking feature alignment between ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system for creating ... | p. 2 (Abstract), p. 1 (Abstract) |
| Reported outcome | Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 13.06 Follow Target 24/25 - 21/25 - TABLE II: Tool ... | p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking) |
| Failure/limitation | Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects due to degraded tracking feature alignment between ... | p. 6 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with dynamic objects, eliminating the need to re-scan ...를 To distill 2D object masks into 3D gaussian partitions, we borrow principles from [49, 50] and train a feature embedding encoder Femb that passes an input gaussian mean position⃗ x ∈R3 through ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects due to degraded tracking feature alignment between ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system for creating ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Gaussian Splatting, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Gaussian Splatting Visual MPC for Granular Media Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects due to degraded tracking feature alignment between ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with dynamic objects, eliminating the need to re-scan ....
3. Compare against the body-reported baseline or a matched simpler baseline: Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized with RGB substituting for DINO features..
4. Report the body metric and its denominator/aggregation: The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the mean and standard deviation of the translation error ....
5. Re-run the body-reported ablation/failure condition: Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth No DINO ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract); the primary result is directionally consistent at p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 makes, following, contributions mechanism이 Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either ... 대비 The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the ...을 개선하고, Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
