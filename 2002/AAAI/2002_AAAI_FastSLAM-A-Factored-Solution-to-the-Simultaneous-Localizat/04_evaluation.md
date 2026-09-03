# Evaluation - FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~thrun/papers/montemerlo.fastslam-tr.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 2 (Abstract), p. 5 (Abstract), p. 5 (Abstract)): Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. Large number of landmarks reduce the ...

## Evaluation Body Digest

- **p. 2 / Abstract - extractive body cue:** To map its environment, the robot can sense landmarks.
- **p. 2 / Abstract - extractive body cue:** Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present day ...
- **p. 5 / Abstract - extractive body cue:** Real-world experiments were complimented by systematic simulation experiments, to investigate the scaling abilities of the approach.
- **p. 3 / Abstract - extractive body cue:** MCL is an application of particle filter to the problem of robot pose estimation (localization).
- **p. 3 / Abstract - extractive body cue:** This is a consequence of the use of sampling to approximate the distribution over the robot's pose.
- **p. 4 / Abstract - extractive body cue:** In such situations, the robot has to solve a data association problem between momentary landmarks sightings zt and the set of landmarks in the map ...
- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 5 / Abstract - extractive body cue:** The robot's estimates are indicated by x's, illustrating the high accuracy of the resulting maps.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. ... | p. 6 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present ... | p. 2 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results are graphically depicted in Figure 6. | p. 5 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experimental Results The FastSLAM algorithm was tested extensively under various conditions. | p. 5 (Abstract) |

## Dataset / Benchmark Role

- **p. 2 / Abstract - extractive body cue:** To map its environment, the robot can sense landmarks.
- **p. 2 / Abstract - extractive body cue:** Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present day ...
- **p. 5 / Abstract - extractive body cue:** Real-world experiments were complimented by systematic simulation experiments, to investigate the scaling abilities of the approach.
- **p. 3 / Abstract - extractive body cue:** MCL is an application of particle filter to the problem of robot pose estimation (localization).
- **p. 3 / Abstract - extractive body cue:** This is a consequence of the use of sampling to approximate the distribution over the robot's pose.
- **p. 4 / Abstract - extractive body cue:** In such situations, the robot has to solve a data association problem between momentary landmarks sightings zt and the set of landmarks in the map ...
- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 5 / Abstract - extractive body cue:** The robot's estimates are indicated by x's, illustrating the high accuracy of the resulting maps.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The SLAM problem: The robot moves from pose s1 through a sequence of controls, u1, u2, . . . , ut. As it ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: A tree representing K = 8 landmark estimates within a single particle. p(st,[m] / zt-1, ut, nt) p(st,[m] / zt-1, ut, nt) = ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Generating a new particle from an old one, while modi- fying only a single Gaussian. The new particle receives only a par- tial ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: (a) Physical robot mapping rocks, in a testbed developed for Mars Rover research. (b) Raw range and path data. (c) Map generated using ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Maps and estimated robot path, generated using sensors with (a) large and (b) small perceptual fields. The correct landmark locations are shown as ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. Large ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To map its environment, the robot can sense landmarks. | embodiment, simulator version and control stack | p. 2 (Abstract), p. 2 (Abstract) |
| Task/environment | Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present ... | reset, timeout, object/scene variation | p. 2 (Abstract), p. 5 (Abstract) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (Abstract) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (Abstract), p. 4 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map. | definition/direction/unit from same section | p. 5 (Abstract) |
| Increasing the number of particles M also bears a positive effect on the map and pose errors, as illustrated in Figure 6b. | definition/direction/unit from same section | p. 5 (Abstract) |
| To map its environment, the robot can sense landmarks. | definition/direction/unit from same section | p. 2 (Abstract) |
| The gray shading illustrates a conditional independence relation. | definition/direction/unit from same section | p. 2 (Abstract) |
| The landmark pose estimators p(θk / st, zt, ut, nt) are realized by Kalman filters, using separate filters for different landmarks. | definition/direction/unit from same section | p. 3 (Abstract) |
| First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st ... | definition/direction/unit from same section | p. 3 (Abstract) |
| Suppose FastSLAM incorporates a new control ut and a new measurement zt. | definition/direction/unit from same section | p. 4 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map. | comparison identity and matched condition | p. 5 (Abstract) |
| Without loss of generality, we will think of landmarks as points in the plane, so that locations are specified by two numerical values. | comparison identity and matched condition | p. 2 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In mobile robotics, the motion model is usually a time-invariant probabilistic generalization of robot kinematics [1]. | component/input/data sensitivity | p. 2 (Abstract) |
| Without loss of generality, we will think of landmarks as points in the plane, so that locations are specified by two numerical values. | component/input/data sensitivity | p. 2 (Abstract) |
| Each particle st,[m] is drawn (with replacement) with a probability proportional to a so-called importance factor w[m] t , which is calculated as follows ... | component/input/data sensitivity | p. 3 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended ... | Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 2 (Abstract), p. 5 (Abstract), p. 5 (Abstract) |
| Primary metric/result | Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present ... | numeric claim only at cited anchor | p. 2 (Abstract) |

- Numeric sentences retained from the body:
- **p. 3 / Abstract - extractive body cue:** One significant difference between the FastSLAM algorithm's use of Kalman filters and that of the traditional SLAM algorithm is that the updates in the FastSLAM ...
- **p. 5 / Abstract - extractive body cue:** The resulting map generated with M = 10 samples is depicted in Figure 4c, with manually determined landmark locations marked by circles.
- **p. 5 / Abstract - extractive body cue:** FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map.
- **p. 3 / Abstract - extractive body cue:** One significant difference between the FastSLAM algorithm's use of Kalman filters and that of the traditional SLAM algorithm is that the updates in the FastSLAM ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case ... | p. 4 (Abstract) |
| body limitation/failure cue | Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach. | p. 5 (Abstract) |
| body limitation/failure cue | Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded by measurement noise. | p. 2 (Abstract) |
| body limitation/failure cue | It has been observed frequently that false data association will make the conventional EKF approach fail catastrophically [2]. | p. 5 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Sensor updates require time quadratic in the number of landmarks K to compute. | p. 1 (Abstract) |
| A naive implementation of this idea leads to an algorithm that requires AAAI-02 593 From: AAAI-02 Proceedings. | p. 1 (Abstract) |
| Practical implementations use maximum likelihood estimators for estimating the correspondence on-the-fly, which work well if landmarks are spaced sufficiently far apart. | p. 2 (Abstract) |
| Efficient Implementation The FastSLAM algorithm, as described thus far, may require time linear in the number of landmarks K for each update iteration if ... | p. 4 (Abstract) |
| Moreover, accessing a Gaussian also takes time logarithmic in K, since the number of steps required to navigate to a leaf of the tree ... | p. 4 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 5 / Abstract - extractive body cue:** Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach.
- **p. 2 / Abstract - extractive body cue:** Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded by measurement noise.
- **p. 5 / Abstract - extractive body cue:** It has been observed frequently that false data association will make the conventional EKF approach fail catastrophically [2].

- **Evidence anchors reviewed:** datasets p. 2 (Abstract), p. 2 (Abstract), p. 5 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), metrics p. 6 (Figure/Table caption), p. 5 (Abstract), p. 5 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), baselines p. 5 (Abstract), p. 2 (Abstract), results p. 6 (Figure/Table caption), p. 2 (Abstract), p. 5 (Abstract), p. 5 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
