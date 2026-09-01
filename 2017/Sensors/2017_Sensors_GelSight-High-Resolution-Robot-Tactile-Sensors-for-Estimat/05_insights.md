# Insights — GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/; PDF retrieval source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 2 / 1. Introduction - extractive body cue:** The first GelSight prototype was developed in 2009 by Johnson and Adelson [7].
- **p. 2 / 1. Introduction - extractive body cue:** We have developed sensors that are compact, yet have resolution far exceeding that of human skin.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The reflectance function R models both the lighting environment and the surface reflectance.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is N(x, y) = ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.
- **p. 2 / 1. Introduction - extractive body cue:** When the sensor surface is painted with small black markers, the motion of the markers provides information about both normal force and shear force.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The change of the marker displacement field with the increase of shear force. The degree of partial slip also increases as the force ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. The contact surface is flat. When the ...
- **p. 18 / 6. Application - extractive body cue:** Additionally, it can detect slip by measuring the relative movement of the objects on the sensor.
- **p. 18 / 6. Application - extractive body cue:** As indicated in Section 3.7, the GelSight sensor can estimate the slip and incipient slip state from the stretching of the surface.
- **Boundary to test:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but the unloading curve is different from the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect the contact and contact force, or force ... | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change corresponds to the surface normal of the ball. ... | p. 9 (Figure/Table caption), p. 15 (5. Evaluation) |
| Failure/limitation | Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but the unloading curve is different from the ... | p. 10 (Figure/Table caption), p. 11 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 Robots need more than force feedback, while the existing sensors do not obtain enough tactile information for the robots.를 Sensors 2017, 17, 2762 2 of 21 cup in the hand is going to slip, and thus adjust the gripping force accordingly; we can know whether a USB connector is going to ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but the unloading curve is different from the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect the contact and contact force, or force ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, Force, contact, manipulation`.
- **Reading predecessor in the generated track queue:** Planning Optimal Grasps (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Contact-Invariant Optimization for Hand Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but the unloading curve is different from the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be applied), or choose some other methods that can ....
3. Compare against the body-reported baseline or a matched simpler baseline: In the figures, we compared the measured values and the ground truth, of the pitch and yaw angles of the surface normal..
4. Report the body metric and its denominator/aggregation: We train the network with the mean squared error loss function for the regression problem..
5. Re-run the body-reported ablation/failure condition: We replace the network's last fully-connected layer with an output layer of four neurons, corresponding to the forces and torques in four axes (Fx, Fy, Fz, Tz)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 past, decades, researchers mechanism이 In the figures, we compared the measured values and the ground truth, of the pitch and ... 대비 We train the network with the mean squared error loss function for the regression problem.을 개선하고, Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
