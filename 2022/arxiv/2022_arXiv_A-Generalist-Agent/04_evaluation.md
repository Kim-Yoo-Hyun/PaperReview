# Evaluation - A Generalist Agent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.06175; PDF retrieval source: https://arxiv.org/abs/2205.06175. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (1 Introduction), p. 14 (1 Introduction), p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 41 (Figure/Table caption)): The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games.

## Evaluation Body Digest

- **p. 14 / 1 Introduction - extractive body cue:** However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the test set in Skill Generalization ...
- **p. 14 / 1 Introduction - extractive body cue:** To the best of our knowledge this agent is the first one to accomplish nearly 100% average success rate simultaneously (multi-task) for this benchmark.
- **p. 15 / 1 Introduction - extractive body cue:** For each task, we randomly sample 100 episodes and tokenize each of them.
- **p. 15 / 1 Introduction - extractive body cue:** These visualizations clearly show that attention tracks the task-relevant objects and regions.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained on ...
- **p. 14 / 1 Introduction - extractive body cue:** See Table 7 in the supplementary material (Section K) for the full list of tasks and corresponding success rates of our agent.
- **p. 14 / 1 Introduction - extractive body cue:** This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks.
- **p. 41 / Figure/Table caption - extractive body cue:** Table 7: Success rates of specialist Meta-World agent. Averaged over 500 evaluations. Task name Success rate assembly-v2 0.980 basketball-v2 0.964 bin-picking-v2

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games. | p. 14 (1 Introduction) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks. | p. 14 (1 Introduction) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Gato's performance on simulated control tasks. Number of tasks where the performance of the pretrained model is above a percentage of expert ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Model size scaling laws results. In-distribution performance as a function of tokens processed for 3 model scales. Performance is first mean-aggregated within ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 14 / 1 Introduction - extractive body cue:** However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the test set in Skill Generalization ...
- **p. 14 / 1 Introduction - extractive body cue:** To the best of our knowledge this agent is the first one to accomplish nearly 100% average success rate simultaneously (multi-task) for this benchmark.
- **p. 15 / 1 Introduction - extractive body cue:** For each task, we randomly sample 100 episodes and tokenize each of them.
- **p. 15 / 1 Introduction - extractive body cue:** These visualizations clearly show that attention tracks the task-relevant objects and regions.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: A generalist agent. Gato can sense and act with different embodiments across a wide range of environments using a single neural network with ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Training phase of Gato. Data from different tasks and modalities is serialized into a flat sequence of tokens, batched, and processed by a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Running Gato as a control policy. Gato consumes a sequence of interleaved tokenized observations, separator tokens, and previously sampled actions to produce the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Datasets. Left: Control datasets used to train Gato. Right: Vision & language datasets. Sample weight means the proportion of each dataset, on average, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: RGB Stacking environment with the Sawyer robot arm. Blocks vary along several shape axes, with 5 held out test triplets. The goal is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Gato's performance on simulated control tasks. Number of tasks where the performance of the pretrained model is above a percentage of expert score, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Image captions generated by Gato. Gato prompted to be an image captioner, describing the first several held-out images from MS-COCO. We report the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the test set in Skill ... | embodiment, simulator version and control stack | p. 14 (1 Introduction), p. 14 (1 Introduction) |
| Task/environment | To the best of our knowledge this agent is the first one to accomplish nearly 100% average success rate simultaneously (multi-task) for this benchmark. | reset, timeout, object/scene variation | p. 14 (1 Introduction), p. 15 (1 Introduction) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (Abstract), p. 5 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| See Table 7 in the supplementary material (Section K) for the full list of tasks and corresponding success rates of our agent. | definition/direction/unit from same section | p. 14 (1 Introduction) |
| This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks. | definition/direction/unit from same section | p. 14 (1 Introduction) |
| Table 7: Success rates of specialist Meta-World agent. Averaged over 500 evaluations. Task name Success rate assembly-v2 0.980 basketball-v2 0.964 bin-picking-v2 | definition/direction/unit from same section | p. 41 (Figure/Table caption) |
| Figure 5: Gato's performance on simulated control tasks. Number of tasks where the performance of the pretrained model is above a percentage of expert ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 8: Normalized Gato per-domain scores. Averaged over 50 evaluations. Control environment Normalized Score (in %) DM Lab 91.4 ALE Atari 30.9 ALE Atari ... | definition/direction/unit from same section | p. 42 (Figure/Table caption) |
| Figure 8: Model size scaling laws results. In-distribution performance as a function of tokens processed for 3 model scales. Performance is first mean-aggregated within ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 19: Few-shot performance of Gato for Skill Generalization in simulation. Each test set object is plotted separately. We ablate over different pretraining datasets. ... | definition/direction/unit from same section | p. 39 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Figure 19: Few-shot performance of Gato for Skill Generalization in simulation. Each test set object is plotted separately. We ablate over different pretraining datasets. ... | comparison identity and matched condition | p. 39 (Figure/Table caption) |
| Table 2: Gato real robot Skill Generalization results. In addition to performing hundreds of other tasks, Gato also stacks competitively with the comparable published ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Gato is competitive with the filtered BC baseline. | comparison identity and matched condition | p. 14 (1 Introduction) |
| The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games. | comparison identity and matched condition | p. 14 (1 Introduction) |
| Figure 6: Image captions generated by Gato. Gato prompted to be an image captioner, describing the first several held-out images from MS-COCO. We report ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 19: Few-shot performance of Gato for Skill Generalization in simulation. Each test set object is plotted separately. We ablate over different pretraining datasets. ... | component/input/data sensitivity | p. 39 (Figure/Table caption) |
| Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Figure 11: Comparing training/test task goal variations. Top: the standard "stack red on blue" task tested in the Skill Generalization benchmark. Bottom: the novel ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Figure 9: Few-shot performance, ablating over various pretraining settings. Orange corresponds to the base Gato pretrained on all data. Red is trained from scratch ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| Both of them were trained on data from a single domain only and rolled out 500 times for each training task without any per-task ... | component/input/data sensitivity | p. 14 (1 Introduction) |
| Figure 6: Image captions generated by Gato. Gato prompted to be an image captioner, describing the first several held-out images from MS-COCO. We report ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results ... | The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games. | PDF body cue; verify exact table/figure and matched conditions | p. 14 (1 Introduction), p. 14 (1 Introduction), p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 41 (Figure/Table caption) |
| Primary metric/result | This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks. | numeric claim only at cited anchor | p. 14 (1 Introduction) |

- Numeric sentences retained from the body:
- **p. 14 / 1 Introduction - extractive body cue:** The training procedure was to train single-task MPO (Abdolmaleki et al., 2018) experts on each of the MT-50 tasks individually, recording the trajectories produced while ...
- **p. 14 / 1 Introduction - extractive body cue:** This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks.
- **p. 15 / 1 Introduction - extractive body cue:** For each task, we randomly sample 100 episodes and tokenize each of them.
- **p. 15 / 1 Introduction - extractive body cue:** Then, from each episode we take a subsequence of 128 tokens, compute their embeddings (at layer 12, which is half the total depth of the ...
- **p. 4 / 1 Introduction - extractive body cue:** Gato uses a 1.2B parameter decoder-only transformer with 24 layers, an embedding size of 2048, and a post-attention feedforward hidden size of 8196 (more details ...
- **p. 5 / 1 Introduction - extractive body cue:** By default, we take the first 1024 tokens of the demonstration.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: Embedding visualization. T-SNE visualization of embeddings from different tasks. A large part of the vision-language embeddings (M3W) overlaps with the language cluster ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | 8 Limitations and Future work 8.1 RL data collection Gato is a data-driven approach, as it is derived from imitation learning. | p. 18 (6 Related Work) |
| body limitation/failure cue | This limitation underscores the need for a careful design and a deployment process that incorporates multiple disciplines and viewpoints. | p. 18 (6 Related Work) |
| body limitation/failure cue | Context-length is therefore a current limitation of our architecture, mainly due to the quadratic scaling of self-attention. | p. 19 (6 Related Work) |
| body limitation/failure cue | Figure 9: Few-shot performance, ablating over various pretraining settings. Orange corresponds to the base Gato pretrained on all data. Red is trained from scratch ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | Figure 11: Comparing training/test task goal variations. Top: the standard "stack red on blue" task tested in the Skill Generalization benchmark. Bottom: the novel ... | p. 13 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training of the model is performed on a 16x16 TPU v3 slice for 1M steps with batch size 512 and token sequence length L ... | p. 4 (1 Introduction) |
| Below we report the tokenization scheme we found to produce the best results for Gato at the current scale using contemporary hardware and model ... | p. 3 (1 Introduction) |
| Furthermore, its performance continues to improve even at the frontier of data, compute and model scale (Kaplan et al., 2020; Hoffmann et al., 2022). | p. 2 (1 Introduction) |
| As hardware and model architectures improve, this operating point will naturally increase the feasible model size, pushing generalist models higher up the scaling law ... | p. 2 (1 Introduction) |
| The values are mu-law encoded to the range [-1, 1] if not already there (see Figure 14 for details), then discretized to 1024 uniform ... | p. 3 (1 Introduction) |
| Gato uses a 1.2B parameter decoder-only transformer with 24 layers, an embedding size of 2048, and a post-attention feedforward hidden size of 8196 (more ... | p. 4 (1 Introduction) |
| This action is sent to the environment which steps and yields a new observation. | p. 5 (1 Introduction) |
| The approximate number of tokens per control dataset is computed assuming the tokenization mechanism described in Section 2.1. | p. 5 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Embedding visualization. T-SNE visualization of embeddings from different tasks. A large part of the vision-language embeddings (M3W) overlaps with the language cluster (MassiveText). ...
- **p. 18 / 6 Related Work - extractive body cue:** 8 Limitations and Future work 8.1 RL data collection Gato is a data-driven approach, as it is derived from imitation learning.
- **p. 18 / 6 Related Work - extractive body cue:** This limitation underscores the need for a careful design and a deployment process that incorporates multiple disciplines and viewpoints.
- **p. 19 / 6 Related Work - extractive body cue:** Context-length is therefore a current limitation of our architecture, mainly due to the quadratic scaling of self-attention.
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 9: Few-shot performance, ablating over various pretraining settings. Orange corresponds to the base Gato pretrained on all data. Red is trained from scratch only ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 11: Comparing training/test task goal variations. Top: the standard "stack red on blue" task tested in the Skill Generalization benchmark. Bottom: the novel "stack ...

- **PDF anchors reviewed:** datasets p. 14 (1 Introduction), p. 14 (1 Introduction), p. 15 (1 Introduction), p. 15 (1 Introduction), metrics p. 12 (Figure/Table caption), p. 14 (1 Introduction), p. 14 (1 Introduction), p. 41 (Figure/Table caption), p. 8 (Figure/Table caption), p. 42 (Figure/Table caption), baselines p. 12 (Figure/Table caption), p. 39 (Figure/Table caption), p. 10 (Figure/Table caption), p. 14 (1 Introduction), p. 14 (1 Introduction), p. 9 (Figure/Table caption), results p. 14 (1 Introduction), p. 14 (1 Introduction), p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 41 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
