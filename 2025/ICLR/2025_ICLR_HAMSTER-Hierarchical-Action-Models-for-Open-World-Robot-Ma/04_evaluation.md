# Evaluation - HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=h7aQxzKbq6; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114802. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption)): Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report averaged success score (success) described in ...

## Evaluation Body Digest

- **p. 20 / B IMPLEMENTATION AND ARCHITECTURE DETAILS - extractive body cue:** Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal.
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We run this algorithm on paths produced by simulation and real robot data to generate the labels po for Doff.
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** In real-world experiments, we simplify the language instruction in the same way as for RVT2 when conditioning on HAMSTER 2D paths to encourage following the ...
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** The current position of the robot gripper is: {current position}.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of 3D-DA with just 50% of the data.
- **p. 28 / Figure/Table caption - extractive body cue:** Table 6: Real world average success rates grouped by task type. G DIFFERENT WAYS OF REPRESENTING 2D PATHS To investigate the effect of the number ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report averaged ...
- **p. 20 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** In order to also ensure the policies are robust to possible error introduced by HAMSTER VLM predictions during evaluation, we add a small 20

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A VLM FINETUNING DATASET DETAILS (p. 19); B IMPLEMENTATION AND ARCHITECTURE DETAILS (p. 20); B.1 VLM IMPLEMENTATION DETAILS (p. 20); C REAL WORLD EXPERIMENT DETAILS (p. 21); C.3 EVALUATION TASKS (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Ranking-based human evaluation of different VLMs, averaged across various real-world evaluation tasks. Results indicate that HAMSTER including simulation data is most effective ... | p. 25 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Example real-world HAMSTER rollouts demonstrate its strong performance in novel scenes achieved by leveraging VLMs' generalization capabilities and the robust execution of ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 20 / B IMPLEMENTATION AND ARCHITECTURE DETAILS - extractive body cue:** Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal.
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We run this algorithm on paths produced by simulation and real robot data to generate the labels po for Doff.
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** In real-world experiments, we simplify the language instruction in the same way as for RVT2 when conditioning on HAMSTER 2D paths to encourage following the ...
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** The current position of the robot gripper is: {current position}.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of in-domain ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Depiction of HAMSTER's execution. The high-level VLM is called once to generate the 2D path. The low-level policy is conditioned on the 2D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Off Domain Training Data: Doff contains (a) Pixel Point Prediction: 770k object location tasks from RoboPoint. (b) Simulated Robot Data: 320k 2D end-effector ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and non-prehensile ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Example real-world HAMSTER rollouts demonstrate its strong performance in novel scenes achieved by leveraging VLMs' generalization capabilities and the robust execution of low-level ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of 3D-DA with just 50% of the data.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report averaged ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Simulation evaluation of HAMSTER across different visual variations. We test vanilla 3D Diffuser Actor and HAMSTER across variations in Colosseum (Pumacay et al., ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal. | embodiment, simulator version and control stack | p. 20 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 20 (B.1 VLM IMPLEMENTATION DETAILS) |
| Task/environment | We run this algorithm on paths produced by simulation and real robot data to generate the labels po for Doff. | reset, timeout, object/scene variation | p. 20 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 7 (3 BACKGROUND), p. 5 (3 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of 3D-DA with just 50% of the ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 6: Real world average success rates grouped by task type. G DIFFERENT WAYS OF REPRESENTING 2D PATHS To investigate the effect of the ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| In order to also ensure the policies are robust to possible error introduced by HAMSTER VLM predictions during evaluation, we add a small 20 | definition/direction/unit from same section | p. 20 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 6: Camera pos. for view in- variance: old (right) and new (left). VLM Generalization. We further demonstrate the benefit of HAMSTER's hi- erarchy ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| In fact, we saw a performance drop for HAMSTER+3D-DA when removing language for Colosseum tasks and a small drop in performance when using simplified ... | definition/direction/unit from same section | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Figure 2: Depiction of HAMSTER's execution. The high-level VLM is called once to generate the 2D path. The low-level policy is conditioned on the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 7: HAMSTER's VLM demonstrates strong generalization to unseen scenarios. From left to right: (a) leveraging world knowledge for user-specified tasks, (b) handling out-of-domain ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Figure 12: The full text prompt we use for RT-Trajectory with Code-as-Policies on top of GPT4-o. The scene description at the bottom comes from ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Table 5: Ranking-based human evaluation of different VLMs, averaged across various real-world evaluation tasks. Results indicate that HAMSTER including simulation data is most effective ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| Figure 13: Human VLM evaluation example images and instructions along with corresponding trajectories from HAMSTER without any finetuning on (RLBench) simulation data, HAMSTER finetuned ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Real world average success rates grouped by task type. G DIFFERENT WAYS OF REPRESENTING 2D PATHS To investigate the effect of the ... | component/input/data sensitivity | p. 28 (Figure/Table caption) |
| Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We remove the language instruction for RVT-2 when conditioning on HAMSTER 2D paths. | component/input/data sensitivity | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| In addition, we reduced the embedding dimension of the transformer to 60 from 120, removed proprioception information from past timesteps, and reduced the number ... | component/input/data sensitivity | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Figure 13: Human VLM evaluation example images and instructions along with corresponding trajectories from HAMSTER without any finetuning on (RLBench) simulation data, HAMSTER finetuned ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 6: Camera pos. for view in- variance: old (right) and new (left). VLM Generalization. We further demonstrate the benefit of HAMSTER's hi- erarchy ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et ... | Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Primary metric/result | Table 5: Ranking-based human evaluation of different VLMs, averaged across various real-world evaluation tasks. Results indicate that HAMSTER including simulation data is most effective ... | numeric claim only at cited anchor | p. 25 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We use tolerance ϵ = 0.05, resulting in paths that are around 2-5 points for each short horizon task.
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** The training process takes about 30 hours to complete.
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We use tolerance ϵ = 0.05, resulting in paths that are around 2-5 points for each short horizon task.
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** The training process takes about 30 hours to complete.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes. | p. 9 (3 BACKGROUND) |
| body limitation/failure cue | 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve robust generalization in robotic manipulation. | p. 10 (3 BACKGROUND) |
| body limitation/failure cue | Figure 15: Performance Distribution of RVT2+Sketch and 3DDA+Sketch This section outlines the failure modes observed during our experiments and provides a detailed breakdown of ... | p. 27 (Figure/Table caption) |
| body limitation/failure cue | Moreover, the interface of just using 2D paths is a bandwidth limited one, which cannot communicate nuances such as force or rotation. | p. 10 (3 BACKGROUND) |
| body limitation/failure cue | Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Depiction of HAMSTER's execution. The high-level VLM is called once to generate the 2D path. The low-level policy is conditioned on the ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use an effective batch size of 256 and a learning rate of 1 × 10-5. | p. 20 (B.1 VLM IMPLEMENTATION DETAILS) |
| During fine-tuning, the entire model-including the vision encoder-is updated. | p. 20 (B.1 VLM IMPLEMENTATION DETAILS) |
| In addition, we reduced the embedding dimension of the transformer to 60 from 120, removed proprioception information from past timesteps, and reduced the number ... | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 3 BACKGROUND - extractive body cue:** See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.
- **p. 10 / 3 BACKGROUND - extractive body cue:** 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve robust generalization in robotic manipulation.
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 15: Performance Distribution of RVT2+Sketch and 3DDA+Sketch This section outlines the failure modes observed during our experiments and provides a detailed breakdown of the ...
- **p. 10 / 3 BACKGROUND - extractive body cue:** Moreover, the interface of just using 2D paths is a bandwidth limited one, which cannot communicate nuances such as force or rotation.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of in-domain ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Depiction of HAMSTER's execution. The high-level VLM is called once to generate the 2D path. The low-level policy is conditioned on the 2D ...

- **Evidence anchors reviewed:** datasets p. 20 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 20 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), metrics p. 9 (Figure/Table caption), p. 28 (Figure/Table caption), p. 9 (Figure/Table caption), p. 20 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 25 (Figure/Table caption), p. 24 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
