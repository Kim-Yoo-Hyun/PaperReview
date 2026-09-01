# Evaluation - Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.1. Latent Motion Token as an Interpretable Mo), p. 8 (5.3. Moto-GPT as an Effective Robot Policy)): 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion Token Moto (OXE) Moto (OXE+SSV2) 50 55 60 ...

## Evaluation Body Digest

- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig.
- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** Fine-tuning is performed using 73k action-labeled expert trajectories from the RT-1 Robot-Action dataset [4].
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It also maintains competitiveness against OpenVLA (finetuned), which is further fine-tuned specially on the RT-1 Robot-Action trajectories, despite its pre-training data already containing action labels ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various pre-training strategies (see supplementary material ...
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned from ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** We additionally test Moto-GPT on three real-world tasks.
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** This enables not only pretraining with human videos but also in-context robot learning guided by online human demonstrations.
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** This demonstrates Moto-GPT's efficiency in action adaptation and its potential to improve robot manipulation tasks through large-scale video pre-training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Benchmarks and Datasets (p. 4); 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Moto-GPT as an Effective Robot Policy | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion Token Moto ... | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| 5.3. Moto-GPT as an Effective Robot Policy | EMPIRICAL / REAL-ROBOT OR HARDWARE | For instance, Moto-GPT achieves a 52.5% success rate with just 1% of labeled data, compared to 0% for the variant. | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| 5.3. Moto-GPT as an Effective Robot Policy | EMPIRICAL / REAL-ROBOT OR HARDWARE | It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned ... | p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| 5.3. Moto-GPT as an Effective Robot Policy | EMPIRICAL / REAL-ROBOT OR HARDWARE | With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task in ... | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| 5.1. Latent Motion Token as an Interpretable Mo | EMPIRICAL / REAL-ROBOT OR HARDWARE | A video classifier using initial frame ViT patch features and concatenated latent motion tokens for seven subsequent frames achieves 79.7% accuracy in predicting semantic ... | p. 6 (5.1. Latent Motion Token as an Interpretable Mo) |

## Dataset / Benchmark Role

- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig.
- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** Fine-tuning is performed using 73k action-labeled expert trajectories from the RT-1 Robot-Action dataset [4].
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It also maintains competitiveness against OpenVLA (finetuned), which is further fine-tuned specially on the RT-1 Robot-Action trajectories, despite its pre-training data already containing action labels ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various pre-training strategies (see supplementary material ...
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned from ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** We additionally test Moto-GPT on three real-world tasks.
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** This enables not only pretraining with human videos but also in-context robot learning guided by online human demonstrations.
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** This demonstrates Moto-GPT's efficiency in action adaptation and its potential to improve robot manipulation tasks through large-scale video pre-training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The overview of Moto, which utilizes Latent Motion Tokens as a bridging "language" for autoregressive pretraining on video data. The Moto-GPT pre-trained through ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of Moto's three training stages: (1) The Latent Motion Tokenizer encodes key visual motions between video frames into compact latent tokens in ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Illustration of real-world evaluation tasks. bles the policy inference of real robots if we take the code- book of latent motion tokens as ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Interpretability of latent motion tokens. Each row displays reconstructed frames from the same initial frame using different latent motion tokens, while each column ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Video imitation generation via latent motion tokens, where a sequence of motion tokens extracted from a demonstration video are decoded into a new ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Visualization of video trajectories generated from a se- quence of latent motion tokens, which are predicted by the pre- trained Moto-GPT given different ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Video classification accuracy with varied representations. Video Representation Semantic Acc. Initial frame 0.292 Initial frame repeated by 8 times 0.283 Initial frame + ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Moto-GPT distinguishes successful, failed, and random robot trajectories using log-likelihoods, enabling effective assess- ment of trajectory rationality and potential reward signals. for more ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig. | embodiment, simulator version and control stack | p. 5 (4. Benchmarks and Datasets), p. 5 (4. Benchmarks and Datasets) |
| Task/environment | Fine-tuning is performed using 73k action-labeled expert trajectories from the RT-1 Robot-Action dataset [4]. | reset, timeout, object/scene variation | p. 5 (4. Benchmarks and Datasets), p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.3. Motion Token Autoregressive Pre-training), p. 3 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The "Overall" column reports the success rate averaged across the sub-tasks of all task types. | definition/direction/unit from same section | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| Visual Distractor Novel Object 0 10 20 30 40 50 60 70 Success Rate (%) Moto Moto w/o Motion Token Figure 8. | definition/direction/unit from same section | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| For instance, Moto-GPT achieves a 52.5% success rate with just 1% of labeled data, compared to 0% for the variant. | definition/direction/unit from same section | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| 1% 5% 10% 50% 100% Proportion of Fine-tuning Data 0.0 0.2 0.4 0.6 0.8 Success Rate Moto Moto w/o Motion Token Figure 11. | definition/direction/unit from same section | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step 5.0 4.5 4.0 3.5 Log Likelihood ... | definition/direction/unit from same section | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |
| 7 illustrates the potential of using Moto's log-likelihoods as a reward signal for trajectory videos, indicating how well a trajectory aligns with MotoGPT's distribution ... | definition/direction/unit from same section | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |
| For example, the Google Everyday Robot uses a continuous value for gripper extension, necessitating Smooth-L1 loss for ∆grip. | definition/direction/unit from same section | p. 4 (4. Benchmarks and Datasets) |
| Pre-training utilizes OXE data, and we collect 90 teleoperated demonstrations (30 per task) for finetuning. | definition/direction/unit from same section | p. 5 (4. Benchmarks and Datasets) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 8. Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various pre-training strategies ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned ... | comparison identity and matched condition | p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| 11 shows that Moto-GPT fine-tuned with varying amounts of labeled data consistently outperforms its variant trained from scratch without latent motion tokens, especially with ... | comparison identity and matched condition | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| To assess this, we collected 98 video triplets in CALVIN using the baseline policies and a random policy. | comparison identity and matched condition | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |
| With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task in ... | comparison identity and matched condition | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| For instance, Moto-GPT achieves a 52.5% success rate with just 1% of labeled data, compared to 0% for the variant. | comparison identity and matched condition | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 11 shows that Moto-GPT fine-tuned with varying amounts of labeled data consistently outperforms its variant trained from scratch without latent motion tokens, especially with ... | component/input/data sensitivity | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned ... | component/input/data sensitivity | p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| Ablations on Policy Fine-tuning Methods. | component/input/data sensitivity | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| To comprehensively evaluate the effectiveness of Moto, we study three key experimental questions: • Q1 (Interpretability): Does the Latent Motion Tokenizer learn interpretable latent ... | component/input/data sensitivity | p. 5 (5. Experiments) |
| After fine-tuning, Moto-GPT3 was evaluated on the SIMPLER and CALVIN benchmarks, demonstrating promising results as shown in Tables 2 and 3. | component/input/data sensitivity | p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| Method Pick Coke Can Move Near Open / Close Drawer Overall Horizontal Vertical Standing Average Average Open Close Average Average RT-1-X [4] 0.820 0.330 ... | component/input/data sensitivity | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, ... | 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion Token Moto ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.1. Latent Motion Token as an Interpretable Mo), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| Primary metric/result | For instance, Moto-GPT achieves a 52.5% success rate with just 1% of labeled data, compared to 0% for the variant. | numeric claim only at cited anchor | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** Fine-tuning is performed using 73k action-labeled expert trajectories from the RT-1 Robot-Action dataset [4].
- **p. 5 / 4. Benchmarks and Datasets - extractive PDF cue:** We assess long-horizon task completion with the Franka Emika Panda robot, requiring consecutive completion of 5 out of 34 tasks in each trial in a ...
- **p. 6 / 5.1. Latent Motion Token as an Interpretable Mo - extractive PDF cue:** This performance is comparable to using ViT features for all eight frames, despite reducing input features from 196 to 8 tokens per frame, confirming that ...
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It also maintains competitiveness against OpenVLA (finetuned), which is further fine-tuned specially on the RT-1 Robot-Action trajectories, despite its pre-training data already containing action labels ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Len. is a comprehensive metric indicating the average number of tasks accomplished in a row across 1,000 trial sequences. "Static RGB" and "Gripper RGB" denote ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Moto-IML and 1 2 3 4 5 Tasks Completed in a Row 0.0 0.2 0.4 0.6 0.8 Success Rate Moto Moto-IML Moto-DM Moto w/o Motion ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 7, clearly differentiate successful trajectories from failures and random attempts. | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |
| body limitation/failure cue | The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step 5.0 4.5 4.0 3.5 Log Likelihood ... | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |
| body limitation/failure cue | Future work will improve model architectures and incorporate more diverse human videos to tackle complex manipulation tasks. | p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| body limitation/failure cue | This further demonstrates the robustness of MotoGPT in real-world deployment. | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| body limitation/failure cue | Figure 9. With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This demonstrates its ability to represent fine-grained motion details, with its decoder acting as a reliable simulator for visualizing environmental changes. | p. 6 (5.1. Latent Motion Token as an Interpretable Mo) |
| Len. is a comprehensive metric indicating the average number of tasks accomplished in a row across 1,000 trial sequences. "Static RGB" and "Gripper RGB" ... | p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| Implementation details can be found in the Supplementary Material. | p. 3 (3.1. Overview) |
| The architecture follows a standard auto-encoder design for motion tokenization and detokenization. | p. 3 (3.2. Latent Motion Tokenizer) |
| We specifically use the MSE loss between the output pixel values from the ViT Decoder and the ground-truth pixel values of o_ t as ... | p. 4 (3.2. Latent Motion Tokenizer) |
| Illustration of real-world evaluation tasks. bles the policy inference of real robots if we take the codebook of latent motion tokens as an abstract ... | p. 4 (3.4. Co-fine-tuning for Robot Manipulation) |
| Video imitation generation via latent motion tokens, where a sequence of motion tokens extracted from a demonstration video are decoded into a new video. | p. 5 (4. Benchmarks and Datasets) |
| We assess long-horizon task completion with the Franka Emika Panda robot, requiring consecutive completion of 5 out of 34 tasks in each trial in ... | p. 5 (4. Benchmarks and Datasets) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive PDF cue:** 7, clearly differentiate successful trajectories from failures and random attempts.
- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive PDF cue:** The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step 5.0 4.5 4.0 3.5 Log Likelihood ( ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Future work will improve model architectures and incorporate more diverse human videos to tackle complex manipulation tasks.
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** This further demonstrates the robustness of MotoGPT in real-world deployment.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 9. With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task ...

- **PDF anchors reviewed:** datasets p. 5 (4. Benchmarks and Datasets), p. 5 (4. Benchmarks and Datasets), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), metrics p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner), baselines p. 7 (Figure/Table caption), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), results p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.1. Latent Motion Token as an Interpretable Mo), p. 8 (5.3. Moto-GPT as an Effective Robot Policy).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
