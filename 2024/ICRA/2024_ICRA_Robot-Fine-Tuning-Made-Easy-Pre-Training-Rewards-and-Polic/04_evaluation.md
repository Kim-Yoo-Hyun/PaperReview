# Evaluation - Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10610421/; PDF retrieval source: https://arxiv.org/pdf/2310.15145. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS)): After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by 58% on an average.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Similarly, we find that one-hot task encodings perform substantially worse than language-conditioned policies, as the prior dataset used in real-robot training is larger and more ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Tasks that use the kitchen-sink environment (pot lid and pot pnp) frequently experience episode interruptions when the robot arm applies more than the maximum allowed ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Simulation Experiments and Ablations We use a suite of simulated robotic manipulation environments to ablate contributions of different components of our algorithm.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We evaluate ROBOFUME on five different realrobot manipulation tasks.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Task FP FN Accuracy Precision Cloth Covering 6.3% 80.9% 89.4% 15.3% Cloth Folding 1.2% 59.8% 84.1% 92.0% Pot PNP 6.1% 81.3% 86.9% 24.3% TABLE II: ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We use a WidowX 250 robotic arm with a single third-person camera (Logitech C920, resizing images to 100x100 pixels).
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 0k 20k 40k 60k 80k 100k 120k 140k Training Steps 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate Reward Model Choices on Vase Task Ours ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by 58% on ... | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps ... | p. 5 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: Performance of our method on three simulated environments. We report the success rate over the course of training, averaged over three seeds. ... | p. 6 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method uses a fine-tuned VLM reward function and outperforms VICE rewards, whereas CNN and VIP rewards fail to improve online. goal image can ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We design our experiments to answer the following questions: Is our method able to improve its performance through near autonomous online interactions? | p. 4 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Similarly, we find that one-hot task encodings perform substantially worse than language-conditioned policies, as the prior dataset used in real-robot training is larger and more ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Tasks that use the kitchen-sink environment (pot lid and pot pnp) frequently experience episode interruptions when the robot arm applies more than the maximum allowed ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Simulation Experiments and Ablations We use a suite of simulated robotic manipulation environments to ablate contributions of different components of our algorithm.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We evaluate ROBOFUME on five different realrobot manipulation tasks.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Task FP FN Accuracy Precision Cloth Covering 6.3% 80.9% 89.4% 15.3% Cloth Folding 1.2% 59.8% 84.1% 92.0% Pot PNP 6.1% 81.3% 86.9% 24.3% TABLE II: ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We use a WidowX 250 robotic arm with a single third-person camera (Logitech C920, resizing images to 100x100 pixels).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose a system that enables autonomous and efficient real-world robot learning. First, we pre-train a multi-task policy and fine-tune a pre-trained Vision-Language ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Illustrations of the five real-world evaluation tasks. (a) Sweep candies to the top of the tray. (b) fold the yellow cloth. (c) cover ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Performance of our method on three simulated environments. We report the success rate over the course of training, averaged over three seeds. Our ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Performance of our method on the Vase simulated task with different actor-critic update objectives. Fine-tuning with CalQL is critical to obtain stable improvements ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Performance of our method on the simulated Vase task using different reward functions. Our method uses a fine-tuned VLM reward function and outperforms ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Similarly, we find that one-hot task encodings perform substantially worse than language-conditioned policies, as the prior dataset used in real-robot training is larger and ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | Tasks that use the kitchen-sink environment (pot lid and pot pnp) frequently experience episode interruptions when the robot arm applies more than the maximum ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 3 (III. PRELIMINARIES), p. 4 (IV. ROBOFUME) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| 0k 20k 40k 60k 80k 100k 120k 140k Training Steps 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate Reward Model Choices on Vase Task ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| In Table II, we report the false positive rate, false negative rate, accuracy, and precision metrics for the VLM reward. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 1: We propose a system that enables autonomous and efficient real-world robot learning. First, we pre-train a multi-task policy and fine-tune a pre-trained ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| How does our proposed VLM reward function mechanism compare to existing alternatives? | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| And, how does each component of ROBOFUME or data affect the performance of our method? | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| ROBOFUME policies retained 68% of its original performance, compared to BC which retained only 10% of its original performance. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Our method ROBOFUME outperforms BC, ARIEL+VLM [7], and MEDAL++ [13] consistently on all three domains. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Our method uses a fine-tuned VLM reward function and outperforms VICE rewards, whereas CNN and VIP rewards fail to improve online. goal image can ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Simulation Experiments and Ablations We use a suite of simulated robotic manipulation environments to ablate contributions of different components of our algorithm. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Ablations on RL Algorithm Design Choices. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| When pre-training without using prior data, that is, exclusively using target data, our method is able to sweep less than half the amount of ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| And, how does each component of ROBOFUME or data affect the performance of our method? | component/input/data sensitivity | p. 4 (V. EXPERIMENTS) |
| The metrics are computed on the data collected during fine-tuning against a hand-engineered ground truth reward. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Fig. 1: We propose a system that enables autonomous and efficient real-world robot learning. First, we pre-train a multi-task policy and fine-tune a pre-trained ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method assumes access to a prior dataset Dprior = ∪N j=1Dj = ∪N j=1{(sj i, aj i, s′j i )}K i=1, which consists ... | After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by 58% on ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Primary metric/result | In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps ... | numeric claim only at cited anchor | p. 5 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For tasks involving deformable objects (the two cloth tasks) we manually reset the object to the initial forward pose every 15-25 episodes, and for the ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use demos from the BridgeDataV2 [19], [54] for pre-training our languageconditioned policy, selecting approximately 1,000 trajectories with relevant behaviors per task.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Our method significantly improves over both offline-only and BC performance after 30k steps of online interaction (2-4 hours).
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For all methods that require online experience, we reset the environment every 1,000 environment steps, i.e. every 25 episodes of interactions.
- **p. 1 / Abstract - extractive body cue:** In a diverse set of five real robot manipulation tasks, we show that our method can incorporate data from an existing robot dataset collected at ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures. | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | We provide 10 forward and reset demonstrations for each task, 30 failure demos, and 10 demos each for 20 prior tasks that show picking ... | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | We find that in the Vase simulated task, VIP fails to obtain good behaviors. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Integrating this work with new VLM models that can exhibit robust zero-shot performance on unseen manipulation tasks and improving the reset efficiency of this ... | p. 6 (VI. CONCLUSION AND FUTURE WORK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward. | p. 5 (V. EXPERIMENTS) |
| Our method significantly improves over both offline-only and BC performance after 30k steps of online interaction (2-4 hours). | p. 5 (V. EXPERIMENTS) |
| We report the success rate over the course of training, averaged over three seeds. | p. 6 (V. EXPERIMENTS) |
| The metrics are computed on the data collected during fine-tuning against a hand-engineered ground truth reward. | p. 6 (V. EXPERIMENTS) |
| Indeed, most existing works only show the benefit of the pre-train and fine-tune paradigm where the robot uses the same hardware instance in both ... | p. 1 (I. INTRODUCTION) |
| The encoder ϕ is a 4-layer CNN, and is optimized exclusively against the critic loss. | p. 3 (IV. ROBOFUME) |
| To best utilize the multi-task data, we encode task descriptions l using pre-trained CLIP embeddings, resulting in an embedding z = CLIP(l) which is ... | p. 3 (IV. ROBOFUME) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. EXPERIMENTS - extractive body cue:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We provide 10 forward and reset demonstrations for each task, 30 failure demos, and 10 demos each for 20 prior tasks that show picking and ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We find that in the Vase simulated task, VIP fails to obtain good behaviors.
- **p. 6 / VI. CONCLUSION AND FUTURE WORK - extractive body cue:** Integrating this work with new VLM models that can exhibit robust zero-shot performance on unseen manipulation tasks and improving the reset efficiency of this framework ...

- **Evidence anchors reviewed:** datasets p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 4 (V. EXPERIMENTS), baselines p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), results p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by 58% on an average. (p. 5, V. EXPERIMENTS).
- **Metric evidence:** For all other tasks, we report success rate over 20 trials. language instruction, given only a sparse binary reward. (p. 5, V. EXPERIMENTS).
- **Baseline/ablation evidence:** In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within 200k steps of online fine-tuning. (p. 5, V. EXPERIMENTS).
- **Failure/negative evidence:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures. (p. 5, V. EXPERIMENTS).
