# Evaluation - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://jmlr.org/papers/v17/15-522.html; PDF retrieval source: https://jmlr.org/papers/volume17/15-522/15-522.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 24 (6.5 Features Learned with End-to-End Training), p. 24 (6.5 Features Learned with End-to-End Training)): When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates.

## Evaluation Body Digest

- **p. 16 / 6. Experimental Evaluation - extractive body cue:** Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks?
- **p. 19 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** In this section, we demonstrate the range of manipulation tasks that can be learned using our trajectory optimization algorithm on a real PR2 robot.
- **p. 19 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** Since performing trajectory optimization is a prerequisite for guided policy search to learn effective visuomotor policies, it is important to evaluate that our trajectory optimization ...
- **p. 16 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** In this section, we compare our method against prior policy search techniques on a range of simulated robotic control tasks.
- **p. 21 / 6.3 Spatial Softmax CNN Architecture Evaluation - extractive body cue:** This is a reasonable proxy for evaluating how well the network can overcome two major challenges in visuomotor learning: the ability to handle relatively small ...
- **p. 23 / 6.5 Features Learned with End-to-End Training - extractive body cue:** Each policy learns features on the target object and the robot manipulator, both clearly relevant 23
- **p. 24 / 6.6 Computational Performance and Sample Efficiency - extractive body cue:** Each visuomotor policy required a total of 3-4 hours of training time: 20-30 minutes for the pose prediction data collection on the robot, 40-60 minutes ...
- **p. 25 / 6.6 Computational Performance and Sample Efficiency - extractive body cue:** The policy finds features on the target object and the robot gripper and arm.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 6. Experimental Evaluation (p. 15); 6.3 Spatial Softmax CNN Architecture Evaluation (p. 21); 6.4 Deep Visuomotor Policy Evaluation (p. 22).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6.4 Deep Visuomotor Policy Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates. | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| 6.3 Spatial Softmax CNN Architecture Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially. | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |
| 6.1 Simulated Comparisons to Prior Policy Search Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | On swimming, our method achieved similar performance to the linear-Gaussian case, but since the neural network policy was stationary, the resulting gait was much ... | p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| 6.4 Deep Visuomotor Policy Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | This variant achieves poor performance. | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| 6.5 Features Learned with End-to-End Training | EMPIRICAL / REAL-ROBOT OR HARDWARE | While this is a drastic simplification, both the pose predictor and the policy still achieve good results. | p. 24 (6.5 Features Learned with End-to-End Training) |

## Dataset / Benchmark Role

- **p. 16 / 6. Experimental Evaluation - extractive body cue:** Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks?
- **p. 19 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** In this section, we demonstrate the range of manipulation tasks that can be learned using our trajectory optimization algorithm on a real PR2 robot.
- **p. 19 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** Since performing trajectory optimization is a prerequisite for guided policy search to learn effective visuomotor policies, it is important to evaluate that our trajectory optimization ...
- **p. 16 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** In this section, we compare our method against prior policy search techniques on a range of simulated robotic control tasks.
- **p. 21 / 6.3 Spatial Softmax CNN Architecture Evaluation - extractive body cue:** This is a reasonable proxy for evaluating how well the network can overcome two major challenges in visuomotor learning: the ability to handle relatively small ...
- **p. 23 / 6.5 Features Learned with End-to-End Training - extractive body cue:** Each policy learns features on the target object and the robot manipulator, both clearly relevant 23
- **p. 24 / 6.6 Computational Performance and Sample Efficiency - extractive body cue:** Each visuomotor policy required a total of 3-4 hours of training time: 20-30 minutes for the pose prediction data collection on the robot, 40-60 minutes ...
- **p. 25 / 6.6 Computational Performance and Sample Efficiency - extractive body cue:** The policy finds features on the target object and the robot gripper and arm.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Our method learns visuomotor policies that directly use camera image observa- tions (left) to set motor torques on a PR2 robot (right). perception ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Summary of the notation frequently used in this article. avoid this issue, the training data must come from the policy's own state distribution ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2: Visuomotor policy architecture. The network contains three convolutional lay- ers, followed by a spatial softmax and an expected position layer that converts pixel-wise ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Diagram of our ap- proach, including the main guided policy search phase and initializa- tion phases. To reduce the amount of experience needed ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 4: Results for learning linear-Gaussian controllers for 2D and 3D insertion, octopus arm, and swimming. Our approach uses fewer samples and finds better solutions ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Comparison on neural network policies. For insertion, the policy was trained to search for an unknown slot position on four slot positions (shown ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6: Tasks for linear-Gaussian controller evaluation: (a) stacking lego blocks on a fixed base, (b) onto a free-standing block, (c) held in both gripper; ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 7: Distance to target point during training of linear-Gaussian controllers. The actual target may differ due to perturbations. Error bars indicate one standard deviation. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks? | embodiment, simulator version and control stack | p. 16 (6. Experimental Evaluation), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Task/environment | In this section, we demonstrate the range of manipulation tasks that can be learned using our trajectory optimization algorithm on a real PR2 robot. | reset, timeout, object/scene variation | p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 12 (4.3 Supervised Policy Optimization), p. 5 (3.1 Definitions and Problem Formulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We also did not extensively optimize the parameters of this network, such as filter size and number of channels, and investigating these design decisions ... | definition/direction/unit from same section | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |
| 0 cm 5/5 5/5 3/5 2/5 5/5 5/5 0/5 0/5 1 cm 5/5 5/5 3/5 2/5 5/5 5/5 3/5 0/5 2 cm 5/5 5/5 ... | definition/direction/unit from same section | p. 21 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| The success rates for each test are shown in Figure 9. | definition/direction/unit from same section | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates. | definition/direction/unit from same section | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle training visual test coat hanger training (18) spatial test (24) visual test (18) end-to-end 100% ... | definition/direction/unit from same section | p. 24 (6.5 Features Learned with End-to-End Training) |
| Error bars indicate one standard deviation. with the initialization of the controllers p(ut/xt) described in Appendix B.2. | definition/direction/unit from same section | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| We compare to a variant of REPS that also fits linear dynamics to generate 500 pseudo-samples (Lioutikov et al., 2014), which we label "REPS ... | definition/direction/unit from same section | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block and ring tasks where the target ... | definition/direction/unit from same section | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On 3D insertion, it outperformed the iLQG baseline, which used a known model. | comparison identity and matched condition | p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| Our controllers outperformed the baseline by a wide margin. | comparison identity and matched condition | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| We compared to two baselines, both of which train the vision layers in advance for pose prediction, instead of training the entire policy end-to-end. | comparison identity and matched condition | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| We also use iLQG (Li and Todorov, 2004) with a known model as a baseline, shown as a black horizontal line in all plots. | comparison identity and matched condition | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| This baseline was only able to place the lego block in the absence of perturbations. | comparison identity and matched condition | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Our network is able to outperform the more standard architectures because it is forced by the softmax and expectation operators to learn feature points, ... | comparison identity and matched condition | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without. | component/input/data sensitivity | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| We compare to a variant of REPS that also fits linear dynamics to generate 500 pseudo-samples (Lioutikov et al., 2014), which we label "REPS ... | component/input/data sensitivity | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| In practice, we found the performance of these methods to be very similar, though the BADMM variant was substantially faster and easier to implement. | component/input/data sensitivity | p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| On peg insertion, the neural network was trained to insert the peg without precise knowledge of the position of the hole, resulting in a ... | component/input/data sensitivity | p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| Robustness increased slightly when more noise was injected during training, but even controllers trained without noise exhibited considerable robustness, since the linear-Gaussian controllers themselves ... | component/input/data sensitivity | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| This is a reasonable proxy for evaluating how well the network can overcome two major challenges in visuomotor learning: the ability to handle relatively ... | component/input/data sensitivity | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our methods consists of two main components, which are illustrated in Figure 3. | When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates. | PDF body cue; verify exact table/figure and matched conditions | p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 24 (6.5 Features Learned with End-to-End Training), p. 24 (6.5 Features Learned with End-to-End Training) |
| Primary metric/result | The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially. | numeric claim only at cited anchor | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |

- Numeric sentences retained from the body:
- **p. 16 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** The challenge in this task stems from its high dimensionality: the arm has 25 degrees of freedom, corresponding to 50 state dimensions.
- **p. 17 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without.
- **p. 17 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Due to its computational cost, PILCO was provided with 5 rollouts per iteration, while other prior methods used 20 and 100.
- **p. 19 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Previous methods could only solve this task with 100 samples per iteration, with RWR eventually obtaining a distance of 0.5m after 4000 samples, and CEM ...
- **p. 19 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Indeed, it is generally known that model-free policy search methods struggle with policies that have over 100 parameters (Deisenroth et al., 2013).
- **p. 21 / 6.3 Spatial Softmax CNN Architecture Evaluation - extractive body cue:** We also did not extensively optimize the parameters of this network, such as filter size and number of channels, and investigating these design decisions further ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent ... | p. 27 (7. Discussion and Future Work) |
| body limitation/failure cue | A promising direction for addressing this limitation is to combine our method with unsupervised state-space learning, as proposed in several recent works, including our ... | p. 27 (7. Discussion and Future Work) |
| body limitation/failure cue | This suggests that the failure of this baseline is not atypical, and that our visuomotor policies are learning visual features and control strategies that ... | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| body limitation/failure cue | Although we demonstrate moderate generalization over variations in the scene, our current method does not generalize to dramatically different settings, especially when visual distractors ... | p. 26 (7. Discussion and Future Work) |
| body limitation/failure cue | More practical alternatives that could be explored in future work include simultaneously training the policy on multiple robots, each of which is located in ... | p. 26 (7. Discussion and Future Work) |
| body limitation/failure cue | Since the peg is 0.5 units long, distances above this amount correspond to controllers that cannot perform an insertion. | p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Only about 15 minutes of the training time consisted of executing trials on the robot. | p. 26 (6.6 Computational Performance and Sample Efficiency) |
| Each visuomotor policy required a total of 3-4 hours of training time: 20-30 minutes for the pose prediction data collection on the robot, 40-60 ... | p. 24 (6.6 Computational Performance and Sample Efficiency) |
| To initialize the vision layers, the robot moves the target object through a range of random positions, recording camera images and the object's pose, ... | p. 15 (5.2 Visuomotor Policy Training) |
| We used the open-source implementation of PILCO provided by the authors. | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| For all prior methods with free hyperparameters (such as the fraction of elites for CEM), we performed hyperparameter sweeps and chose the most successful ... | p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| The high dimensionality of the octopus arm made it difficult to run PILCO, though in principle, such methods should perform well on this task ... | p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block and ring tasks where the target ... | p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| This issue could also be mitigated by artificially augmenting the image samples with synthetic transformations, as discussed in prior work in computer vision (Simard ... | p. 23 (6.4 Deep Visuomotor Policy Evaluation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 27 / 7. Discussion and Future Work - extractive body cue:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.
- **p. 27 / 7. Discussion and Future Work - extractive body cue:** A promising direction for addressing this limitation is to combine our method with unsupervised state-space learning, as proposed in several recent works, including our own ...
- **p. 23 / 6.4 Deep Visuomotor Policy Evaluation - extractive body cue:** This suggests that the failure of this baseline is not atypical, and that our visuomotor policies are learning visual features and control strategies that improve ...
- **p. 26 / 7. Discussion and Future Work - extractive body cue:** Although we demonstrate moderate generalization over variations in the scene, our current method does not generalize to dramatically different settings, especially when visual distractors occlude ...
- **p. 26 / 7. Discussion and Future Work - extractive body cue:** More practical alternatives that could be explored in future work include simultaneously training the policy on multiple robots, each of which is located in a ...
- **p. 18 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Since the peg is 0.5 units long, distances above this amount correspond to controllers that cannot perform an insertion.

- **PDF anchors reviewed:** datasets p. 16 (6. Experimental Evaluation), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 16 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 23 (6.5 Features Learned with End-to-End Training), metrics p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 21 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 24 (6.5 Features Learned with End-to-End Training), p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), baselines p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), results p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 24 (6.5 Features Learned with End-to-End Training), p. 24 (6.5 Features Learned with End-to-End Training).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
