# Method - FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~thrun/papers/montemerlo.fastslam-tr.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract)): First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st / ut, s[m] t-1), (6) obtained ...

## Method Body Digest

- **p. 3 / Abstract - extractive PDF cue:** First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st / ...
- **p. 1 / Abstract - extractive PDF cue:** Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.
- **p. 1 / Abstract - extractive PDF cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.
- **p. 2 / Abstract - extractive PDF cue:** Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present day ...
- **p. 3 / Abstract - extractive PDF cue:** We note that, with a linear Gaussian observation model, the resulting distribution p(θk / st, zt, ut, nt) is exactly a Gaussian, even if the ...
- **p. 4 / Abstract - extractive PDF cue:** In the last line, "EKF" makes explicit the use of a linearized model as an approximation to the observation model p(zt / θ[m] nt , ...
- **p. 2 / Abstract - extractive PDF cue:** This conditional independence is the basis of the FastSLAM algorithm described in the next section.
- **p. 3 / Abstract - extractive PDF cue:** For nt = k, we obtain p(θk / st, zt, ut, nt) (9) Bayes ∝ p(zt / θk, st, zt-1, ut, nt) p(θk / st, ...

## Design Rationale

- **p. 2 / Abstract - extractive PDF cue:** We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to ...
- **p. 4 / Abstract - extractive PDF cue:** Our approach makes it possible to execute a FastSLAM iteration in O(M log K) time.
- **p. 1 / Abstract - extractive PDF cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.

## Source Evidence Cues

- **p. 3 / Abstract - extractive PDF cue:** First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st / ...
- **p. 1 / Abstract - extractive PDF cue:** Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.
- **p. 1 / Abstract - extractive PDF cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.
- **p. 2 / Abstract - extractive PDF cue:** Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present day ...
- **p. 3 / Abstract - extractive PDF cue:** We note that, with a linear Gaussian observation model, the resulting distribution p(θk / st, zt, ut, nt) is exactly a Gaussian, even if the ...
- **p. 4 / Abstract - extractive PDF cue:** In the last line, "EKF" makes explicit the use of a linearized model as an approximation to the observation model p(zt / θ[m] nt , ...
- **p. 2 / Abstract - extractive PDF cue:** This conditional independence is the basis of the FastSLAM algorithm described in the next section.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ... | p. 3 (Abstract), p. 1 (Abstract) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM. | p. 1 (Abstract), p. 1 (Abstract) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps. | p. 1 (Abstract), p. 2 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Abstract - extractive PDF cue:** For nt = k, we obtain p(θk / st, zt, ut, nt) (9) Bayes ∝ p(zt / θk, st, zt-1, ut, nt) p(θk / st, ...
- **p. 2 / Abstract - extractive PDF cue:** Without loss of generality, we will think of landmarks as points in the plane, so that locations are specified by two numerical values.
- **p. 1 / Abstract - extractive PDF cue:** Sensor updates require time quadratic in the number of landmarks K to compute.
- **p. 1 / Abstract - extractive PDF cue:** Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and realworld data.
- **p. 2 / Abstract - extractive PDF cue:** Practical implementations use maximum likelihood estimators for estimating the correspondence on-the-fly, which work well if landmarks are spaced sufficiently far apart.
- **p. 3 / Abstract - extractive PDF cue:** Calculating the Importance Weights Let us now return to the problem of calculating the importance weights w[m] t needed for particle filter resampling, as defined ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Kalman, filter-based, algorithms, example, require, time, quadratic, number, landmarks, incorporate, sensor, observation, describes, efficient | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Kalman, filter-based, algorithms, example, require, time, quadratic, number, landmarks, incorporate | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | extend, FastSLAM, algorithm, situations, unknown, data, association, number, landmarks, showing | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | obtain, Bayes, zt-1, Markov, st-1, ut-1, nt-1, simply, leave, Gaussian | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation.
- **p. 1 / Abstract - extractive PDF cue:** Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.
- **p. 3 / Abstract - extractive PDF cue:** We note that, with a linear Gaussian observation model, the resulting distribution p(θk / st, zt, ut, nt) is exactly a Gaussian, even if the ...
- **p. 4 / Abstract - extractive PDF cue:** In the last line, "EKF" makes explicit the use of a linearized model as an approximation to the observation model p(zt / θ[m] nt , ...
- **p. 2 / Abstract - extractive PDF cue:** The robot's pose at time t will be denoted st.
- **p. 2 / Abstract - extractive PDF cue:** To map its environment, the robot can sense landmarks.
- **p. 3 / Abstract - extractive PDF cue:** The posterior over the k-th landmark pose θk is easily obtained.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | It poses no restriction, as multiple landmark sightings at a single time step can be processed sequentially. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | SLAM addresses the problem of building a map of an environment from a sequence of landmark measurements obtained from a moving robot. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, particle, St-1, generate, probabilistic, guess, robot, pose, time, obtained, sampling, motion, model, observation, describes, efficient, SLAM, algorithm, called, FastSLAM.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To map its environment, the robot can sense landmarks. | p. 2 (Abstract), p. 2 (Abstract) |
| Global / local decision | FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map. | p. 5 (Abstract), p. 2 (Abstract) |
| Motion execution / recovery | Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of ... | p. 6 (Figure/Table caption), p. 2 (Abstract) |

## Failure and Ablation Link

- **p. 2 / Abstract - extractive PDF cue:** In mobile robotics, the motion model is usually a time-invariant probabilistic generalization of robot kinematics [1].
- **p. 2 / Abstract - extractive PDF cue:** Without loss of generality, we will think of landmarks as points in the plane, so that locations are specified by two numerical values.
- **p. 3 / Abstract - extractive PDF cue:** Each particle st,[m] is drawn (with replacement) with a probability proportional to a so-called importance factor w[m] t , which is calculated as follows [10]: ...
- **p. 4 / Abstract - extractive PDF cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 5 / Abstract - extractive PDF cue:** Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach.
- **p. 2 / Abstract - extractive PDF cue:** Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded by measurement noise.
- **p. 5 / Abstract - extractive PDF cue:** It has been observed frequently that false data association will make the conventional EKF approach fail catastrophically [2].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), objective p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), temporal p. 2 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
