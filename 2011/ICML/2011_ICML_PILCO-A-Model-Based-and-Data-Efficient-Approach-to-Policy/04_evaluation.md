# Evaluation - PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.deisenroth.cc/publication/deisenroth-2011-c/; PDF retrieval source: https://www.deisenroth.cc/publication/deisenroth-2011-c/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption), p. 3 (2.2. Policy Evaluation), p. 5 (3. Experimental Results), p. 5 (3.2. Cart-Double-Pendulum Swing-up), p. 6 (3.3. Unicycle Riding)): The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints.

## Evaluation Body Digest

- **p. 5 / 3. Experimental Results - extractive body cue:** In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** Robotic unicycle system and simulation results.
- **p. 5 / 3.1. Cart-Pole Swing-up - extractive body cue:** Pilco successfully learned a sufficiently good dynamics model and a good controller for this standard benchmark problem fully automatically in only a handful of trials ...
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The dynamics of the robotic unicycle can be described by 12 coupled firstorder ODEs, see (Forster, 2009).
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The covariance Σ0 of the initial state was 0.252I allowing each angle to be offby about 30◦(twice the standard deviation).
- **p. 3 / 2.2. Policy Evaluation - extractive body cue:** The computation of the cross-covariance cov[xt-1, ∆t] in Eq.
- **p. 3 / 2.2. Policy Evaluation - extractive body cue:** Subsequently, the cross-covariance cov[xt-1, ut-1] is computed.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 2.2. Policy Evaluation (p. 3); 3. Experimental Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.3. Unicycle Riding | EMPIRICAL / SIMULATION | The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | p. 6 (3.3. Unicycle Riding) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 1. Small data set of observed transitions (left), multiple plausible deterministic function approximators (center), probabilistic function approximator (right). The probabilistic approximator models uncertainty ... | p. 2 (Figure/Table caption) |
| 2.2. Policy Evaluation | EMPIRICAL / SIMULATION | In the following, we assume that these test inputs are Gaussian distributed and extend the results from Qui˜nonero-Candela et al. | p. 3 (2.2. Policy Evaluation) |
| 3. Experimental Results | EMPIRICAL / SIMULATION | The results discussed in the following are typical, i.e., they do neither represent best nor worst cases. | p. 5 (3. Experimental Results) |
| 3.2. Cart-Double-Pendulum Swing-up | EMPIRICAL / SIMULATION | In the following, we show the results for pilco learning a dynamics model and a controller for the cart-doublependulum swing-up. | p. 5 (3.2. Cart-Double-Pendulum Swing-up) |

## Dataset / Benchmark Role

- **p. 5 / 3. Experimental Results - extractive body cue:** In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** Robotic unicycle system and simulation results.
- **p. 5 / 3.1. Cart-Pole Swing-up - extractive body cue:** Pilco successfully learned a sufficiently good dynamics model and a good controller for this standard benchmark problem fully automatically in only a handful of trials ...
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The dynamics of the robotic unicycle can be described by 12 coupled firstorder ODEs, see (Forster, 2009).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Small data set of observed transitions (left), multiple plausible deterministic function approximators (center), probabilistic function approximator (right). The probabilistic approximator models uncertainty about ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. GP prediction at an uncertain input. The input distribution p(xt-1, ut-1) is assumed Gaussian (lower right panel). When propagating it through the GP ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Real cart-pole system. Snapshots of a controlled trajectory of 20 s length after having learned the task. To solve the swing-up plus balancing, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Robotic unicycle system and simulation results. The state space is R12, the control space R2. unicycle is 0.76 m high and consists of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Pilco's data efficiency scales to high dimensions. cart-pole cart-double-pole unicycle state space R4 R6 R12
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Data efficiency for learning the cart-pole task in the absence of expert knowledge. The horizontal axis chronologically orders the references according to their ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems. | embodiment, simulator version and control stack | p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding) |
| Task/environment | Robotic unicycle system and simulation results. | reset, timeout, object/scene variation | p. 6 (3.3. Unicycle Riding), p. 5 (3.1. Cart-Pole Swing-up) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 3 (2.1. Dynamics Model Learning) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 1 (Abstract), p. 2 (2. Model-based Indirect Policy Search) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | definition/direction/unit from same section | p. 6 (3.3. Unicycle Riding) |
| The covariance Σ0 of the initial state was 0.252I allowing each angle to be offby about 30◦(twice the standard deviation). | definition/direction/unit from same section | p. 6 (3.3. Unicycle Riding) |
| The computation of the cross-covariance cov[xt-1, ∆t] in Eq. | definition/direction/unit from same section | p. 3 (2.2. Policy Evaluation) |
| Subsequently, the cross-covariance cov[xt-1, ut-1] is computed. | definition/direction/unit from same section | p. 3 (2.2. Policy Evaluation) |
| In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems. | definition/direction/unit from same section | p. 5 (3. Experimental Results) |
| Pilco successfully learned a sufficiently good dynamics model and a good controller for this standard benchmark problem fully automatically in only a handful of ... | definition/direction/unit from same section | p. 5 (3.1. Cart-Pole Swing-up) |
| Figure 1. Small data set of observed transitions (left), multiple plausible deterministic function approximators (center), probabilistic function approximator (right). The probabilistic approximator models uncertainty ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without ... | comparison identity and matched condition | p. 6 (3.4. Data Efficiency) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without ... | component/input/data sensitivity | p. 6 (3.4. Data Efficiency) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce pilco, a practical, data-efficient model-based policy search method. | The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption), p. 3 (2.2. Policy Evaluation), p. 5 (3. Experimental Results), p. 5 (3.2. Cart-Double-Pendulum Swing-up), p. 6 (3.3. Unicycle Riding) |
| Primary metric/result | Figure 1. Small data set of observed transitions (left), multiple plausible deterministic function approximators (center), probabilistic function approximator (right). The probabilistic approximator models uncertainty ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3.1. Cart-Pole Swing-up - extractive body cue:** The learned statefeedback controller was a nonlinear RBF network, i.e., π(x, θ) = Xn i=1 wiφi(x) , (31) φi(x) = exp(-1 2(x -µi)⊤Λ-1(x -µi)) (32) ...
- **p. 5 / 3.1. Cart-Pole Swing-up - extractive body cue:** Pilco successfully learned a sufficiently good dynamics model and a good controller for this standard benchmark problem fully automatically in only a handful of trials ...
- **p. 5 / 3.1. Cart-Pole Swing-up - extractive body cue:** Snapshots of a 20 s test trajectory are shown in Fig.
- **p. 5 / 3.2. Cart-Double-Pendulum Swing-up - extractive body cue:** (31), with n = 200 and θ ∈R1816 to jointly solve the swing-up and balancing.
- **p. 5 / 3.2. Cart-Double-Pendulum Swing-up - extractive body cue:** For this, Pilco required about 20-30 trials corresponding to an interaction time of about 60 s-90 s.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** Snapshots of a controlled trajectory of 20 s length after having learned the task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping. | p. 7 (4. Discussion and Conclusion) |
| body limitation/failure cue | Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the ... | p. 7 (4. Discussion and Conclusion) |
| body limitation/failure cue | The goal was to ride the unicycle, i.e., to prevent it from falling. | p. 6 (3.3. Unicycle Riding) |
| body limitation/failure cue | After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very closely to the desired upright position. | p. 6 (3.3. Unicycle Riding) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Subsequently, the cross-covariance cov[xt-1, ut-1] is computed. | p. 3 (2.2. Policy Evaluation) |
| (12) depends on the policy parametrization, but can often be computed analytically. | p. 3 (2.2. Policy Evaluation) |
| In all cases, pilco learns completely from scratch by following the steps detailed in Alg. | p. 5 (3. Experimental Results) |
| For this, Pilco required about 20-30 trials corresponding to an interaction time of about 60 s-90 s. | p. 5 (3.2. Cart-Double-Pendulum Swing-up) |
| Pilco required about 20 trials (experience of about 30 s) to learn a dynamics model and a controller that keeps the unicycle upright. | p. 6 (3.3. Unicycle Riding) |
| Pilco's data efficiency scales to high dimensions. cart-pole cart-double-pole unicycle state space R4 R6 R12 # trials ≤10 20-30 ≈20 experience ≈20 s ≈60 ... | p. 6 (3.3. Unicycle Riding) |
| (27) is known from time step t -1 and ∂µt/∂p(xt-1) is computed by applying the chain-rule to Eqs. | p. 4 (2.3. Analytic Gradients for Policy Improvement) |
| Hence, we can analytically compute the gradients of the expected return Jπ with respect to the policy parameters θ, which we sketch in the ... | p. 4 (2.3. Analytic Gradients for Policy Improvement) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping.
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The goal was to ride the unicycle, i.e., to prevent it from falling.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very closely to the desired upright position.

- **Evidence anchors reviewed:** datasets p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding), p. 5 (3.1. Cart-Pole Swing-up), p. 6 (3.3. Unicycle Riding), metrics p. 6 (3.3. Unicycle Riding), p. 6 (3.3. Unicycle Riding), p. 3 (2.2. Policy Evaluation), p. 3 (2.2. Policy Evaluation), p. 5 (3. Experimental Results), p. 5 (3.1. Cart-Pole Swing-up), baselines p. 6 (3.4. Data Efficiency), results p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption), p. 3 (2.2. Policy Evaluation), p. 5 (3. Experimental Results), p. 5 (3.2. Cart-Double-Pendulum Swing-up), p. 6 (3.3. Unicycle Riding).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Robotic unicycle system and simulation results. (p. 6, 3.3. Unicycle Riding).
- **Metric evidence:** The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. (p. 6, 3.3. Unicycle Riding).
- **Baseline/ablation evidence:** In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without informative prior knowledge. (p. 6, 3.4. Data Efficiency).
- **Failure/negative evidence:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task. (p. 7, 4. Discussion and Conclusion).
