# Evaluation - SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.01990; PDF retrieval source: https://arxiv.org/pdf/2312.01990. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption)): It turns out that the resulting ViT-linear-attention hybrid RT-2 variant (third row in Table I) provides 12%+ mean accuracy improvement, excelling in certain tasks (e.g.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** It consists of expert demonstrations collected with a mobile manipulation robot.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The actual sequence length for the on-robot deployment varies from scene to scene, but can easily exceed 1K.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Robotic Point Cloud Transformers In our first set of experiments, we trained robotic grasping Transformer policies operating on the point cloud (PC) data.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The latter two techniques provide farther accuracy boost, but are more demanding computationally, and thus challenging for direct on-robot deployment.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 7: The scheme of some of the key elements of the PaLI-X backbone of RT-2 from the computational viewpoint, accompanied with the real robot performing ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These points are hierarchically clustered into objects.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations iterations ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It turns out that the resulting ViT-linear-attention hybrid RT-2 variant (third row in Table I) provides 12%+ mean accuracy improvement, excelling in certain tasks ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations ... | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure). | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As described in [1], the action space consists of 6-DoF positional and rotational displacement of the robot end-effector, as well as the level of ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We noticed that the vector representation of actions results in higher quality models. | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** It consists of expert demonstrations collected with a mobile manipulation robot.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The actual sequence length for the on-robot deployment varies from scene to scene, but can easily exceed 1K.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Robotic Point Cloud Transformers In our first set of experiments, we trained robotic grasping Transformer policies operating on the point cloud (PC) data.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The latter two techniques provide farther accuracy boost, but are more demanding computationally, and thus challenging for direct on-robot deployment.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 7: The scheme of some of the key elements of the PaLI-X backbone of RT-2 from the computational viewpoint, accompanied with the real robot performing ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These points are hierarchically clustered into objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different modalities: vision, language and point clouds and varying sequence ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The agent's ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Training regular PCT policy as well as three variants of SARA with f ∈{ReLU, exp, sqrt} (up-training from the regular PCT checkpoint). The ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Upper row: The AB-test setup. Different configurations can vary by the number of objects of the table and their shapes. Lower rows: One ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Speed tests for SARA-PCT and regular PCT. Reported are mean inference times (averaged over l = 10 random seeds) for PCT encoders (as ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: The scheme of some of the key elements of the PaLI-X backbone of RT-2 from the computational viewpoint, accompanied with the real robot ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: Speed tests (on a CPU). Reported numbers are as in Fig. 7, but for PaLI-ViT encoders as functions of the resolution of the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It consists of expert demonstrations collected with a mobile manipulation robot. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | The actual sequence length for the on-robot deployment varies from scene to scene, but can easily exceed 1K. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 1 (Body text (section not recovered)) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 1 (Body text (section not recovered)), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure). | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The reported reward is computed as their average over 100 trials. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| The average reward obtained by the regular PCT agent is: rreg ave = 0.64 and by the SARA-PCT agent: rSARA ave = 0.75. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Both variants have very similar mean accuracy, though SARA variant generalizes better. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| The latter two techniques provide farther accuracy boost, but are more demanding computationally, and thus challenging for direct on-robot deployment. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Thus we chose (here and for the RT-2 experiments) the simplest ReLU (that can be thought of as the tamed version of the exp ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| The comparison is conducted on the six regular manipulation task and an additional task measuring generalization level (diverse pick). | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For SARA variants (with f = ReLU and all-one vector v), up-training is conducted after the fine-tuning phase. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| A pass-through filter removes all points except for those of table top objects. | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| The adaptation process of the linear attention for the ReLU variant is highlighted. | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| We see almost immediate adaptation of the linear attention for all SARA variants. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Frames are encoded via SARA variants of the ViTs (sViT). | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| This self-attention block is yet another good candidate for injecting SARA variants. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for ... | It turns out that the resulting ViT-linear-attention hybrid RT-2 variant (third row in Table I) provides 12%+ mean accuracy improvement, excelling in certain tasks ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption) |
| Primary metric/result | 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations ... | numeric claim only at cited anchor | p. 4 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The reported reward is computed as their average over 100 trials.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The observation space has 3 components: (1) cloud: N × 3 point cloud with the workspace origin at the mean of the object's cloud; (2) ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The test consisted of N = 200 random object configurations (see: Fig.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 6, SARAPCT provides significant speedups, guaranteeing practically constant inference ≈100ms (regardless of the point cloud size), with the attention module not being a computational bottleneck ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Besides, regular RT-2 controller needs 53.2 ms (TPU) for the forward pass, while SARA's: 45.7 ms (TPU) (14% speedup).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Finally, we combine SARA with the new tokenizer from IV-B.2 and the history of H = 3 frames.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure). | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | In this work, we chose the former, leaving testing the latter to future work. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | SARA remains a feasible approach even for high resolution images, while the regular variant does not. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | We plan to exercise this feature of SARA by using much higher resolution images (a challenge for regular RT-2 models) in future work. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different modalities: vision, language and point clouds and varying ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Reported are mean inference times (averaged over l = 10 random seeds) for PCT encoders (as well as the corresponding standard deviations; see: shaded ... | p. 5 (IV. EXPERIMENTS) |
| The reported reward is computed as their average over 100 trials. | p. 4 (IV. EXPERIMENTS) |
| We then run speed tests for the regular PCT encoder and SARA-PCT encoder for input sequences of different lengths. | p. 5 (IV. EXPERIMENTS) |
| 4: Training regular PCT policy as well as three variants of SARA with f ∈{ReLU, exp, sqrt} (up-training from the regular PCT checkpoint). | p. 4 (IV. EXPERIMENTS) |
| Frames are encoded via SARA variants of the ViTs (sViT). | p. 6 (IV. EXPERIMENTS) |
| The ViT encoder of PaLI is computationally bottlenecked by its attention module. | p. 6 (IV. EXPERIMENTS) |
| On the other side of the spectrum are linear attention models with ϕ = ϕf given as: ϕf(z) = (f(z1), ..., f(zdQK))⊤for some f ... | p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |
| In that case, each ai can be approximated as:      ˜ai = Ψϕ(qi) Γϕ(qi) , Ψ = PN j=1 ¯ajϕ⊤(kj), ... | p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure).
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The agent's ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this work, we chose the former, leaving testing the latter to future work.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** SARA remains a feasible approach even for high resolution images, while the regular variant does not.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We plan to exercise this feature of SARA by using much higher resolution images (a challenge for regular RT-2 models) in future work.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different modalities: vision, language and point clouds and varying sequence ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), metrics p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
