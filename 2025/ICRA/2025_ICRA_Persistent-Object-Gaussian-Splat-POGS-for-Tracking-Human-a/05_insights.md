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

- **Paper-specific interface:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose estimation. (p. 1, Abstract).
- **Paper-specific mechanism:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system ... (p. 2, Abstract).
- **Evidence boundary:** the reported outcome is Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth ... (p. 6, 3) Persistent Object Tracking phase for online tracking); the relevant task/metric cue is The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the mean and standard deviation of the ... (p. 5, 3) Persistent Object Tracking phase for online tracking). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning failures occur due to irrecoverable ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Gaussian Splatting, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Gaussian Splatting Visual MPC for Granular Media Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects due to degraded tracking feature alignment between ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose estimation. (p. 1, Abstract); preserve the objective/update rule: However, NeRF-based representations are limited by NeRF's training speed and implicit spatial representation, making it impossible to update when objects move without further scene-scale optimization. (p. 2, Abstract).
2. Use the paper-reported task/data/environment cue: As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with dynamic objects, eliminating the need ... (p. 2, Abstract).
3. Compare against the reported or matched baseline: Each Gaussian cluster pose parameter is optimized independently, allowing POGS to track multiple moving objects, without imposing constraints on their relative movements. unlike prior work in real-time tracking of gaussian ... (p. 4, 3) Persistent Object Tracking phase for online tracking).
4. Report the body metric with its denominator and aggregation: The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the mean and standard deviation of the ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
5. Re-run the reported ablation or stress/failure condition: Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth ... (p. 6, 3) Persistent Object Tracking phase for online tracking); if none is reported, design one around: Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning failures occur due to irrecoverable ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (Abstract), p. 1 (Abstract), match the reported outcome at p. 6 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 6 (3) Persistent Object Tracking phase for online tracking), and measure the boundary at p. 5 (3) Persistent Object Tracking phase for online tracking), p. 6 (3) Persistent Object Tracking phase for online tracking).

## Falsifiable research question

Under the paper's stated interface (After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised ...), does the paper-specific mechanism (This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously ...) retain the reported evaluation outcome (The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the ...) when tested against the paper's strongest explicit boundary (Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system ... (p. 2, Abstract).
- **Paper-supported outcome:** Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth ... (p. 6, 3) Persistent Object Tracking phase for online tracking).
- **Strongest explicit boundary:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning failures occur due to irrecoverable ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
