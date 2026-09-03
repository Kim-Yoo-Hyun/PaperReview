# Evaluation - VIMA: General Robot Manipulation with Multimodal Prompts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.03094; PDF retrieval source: https://arxiv.org/pdf/2210.03094. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (Figure/Table caption)): Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes.

## Evaluation Body Digest

- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Our proposed object tokens outperform all methods that learn directly from raw pixels, and Object Perceiver that downsamples the object sequence to a fixed number ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT L1 ...
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** Next we investigate how different methods scale with varying dataset sizes.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We compare model performance at 0.1%, 1%, 10% and full imitation learning dataset provided in VIMA-BENCH (Fig.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** We compare the performance of VIMA-200M model across different visual tokenizers.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: VIMA Architecture. We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention layers. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.2. Evaluation Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Evaluation Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes. | p. 6 (5.2. Evaluation Results) |
| 5.2. Evaluation Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the ... | p. 6 (5.2. Evaluation Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all ... | p. 5 (Figure/Table caption) |
| 5.2. Evaluation Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT ... | p. 7 (5.2. Evaluation Results) |
| 5.2. Evaluation Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Finally, across all levels with just 10% of the data, VIMA can outperform other architectures trained with the full dataset by a significant margin. | p. 7 (5.2. Evaluation Results) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Our proposed object tokens outperform all methods that learn directly from raw pixels, and Object Perceiver that downsamples the object sequence to a fixed number ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT L1 ...
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** Next we investigate how different methods scale with varying dataset sizes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Multimodal prompts for task specification. We observe that many robot manipulation tasks can be expressed as multimodal prompts that interleave language and image/video ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Evaluation Protocol in VIMA-BENCH. We design 4 levels of evaluation settings to systematically measure the zero-shot generalization capability of an agent. Each level ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: VIMA Architecture. We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention layers. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: VIMA incurs much less performance drop than baselines as we evaluate on progressively harder settings.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Ablation on visual tokenizers. We compare the performance of VIMA-200M model across different visual tokenizers. Our proposed object tokens outperform all methods that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Ablation on prompt conditioning. We compare our method (xattn: cross-attention prompt conditioning) with a vanilla transformer decoder (gpt-decoder) across different model sizes. Cross-attention ...
- **p. 33 / Figure/Table caption - extractive body cue:** Table 1: Comparison of different methods. Visual Tokenizer Prompt Conditioning Number of Observation Tokens per Step Ours Object tokens consisting of cropped images and bounding ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes. | embodiment, simulator version and control stack | p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results) |
| Task/environment | Our proposed object tokens outperform all methods that learn directly from raw pixels, and Object Perceiver that downsamples the object sequence to a fixed ... | reset, timeout, object/scene variation | p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4. Novel task generalization. New tasks with novel), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (5.1. Baselines), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT ... | definition/direction/unit from same section | p. 7 (5.2. Evaluation Results) |
| We compare model performance at 0.1%, 1%, 10% and full imitation learning dataset provided in VIMA-BENCH (Fig. | definition/direction/unit from same section | p. 6 (5.2. Evaluation Results) |
| Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes. | definition/direction/unit from same section | p. 6 (5.2. Evaluation Results) |
| We compare the performance of VIMA-200M model across different visual tokenizers. | definition/direction/unit from same section | p. 7 (5.2. Evaluation Results) |
| Figure 3: VIMA Architecture. We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 7: Hyperparameters used during training. Hyperparameter Value Learning Rate 0.0001 Warmup Steps 7K LR Cosine Annealing Steps | definition/direction/unit from same section | p. 38 (Figure/Table caption) |
| Table 13: Performances of our method with differently sized pre-trained T5 prompt encoder. We fix the parameter count of the decision-making part to be ... | definition/direction/unit from same section | p. 41 (Figure/Table caption) |
| Table 12: Data scaling when baseline variants' ViT is trained from scratch, indicated inside parentheses. ↑and ↓denote performance increase and decrease. Numbers in the ... | definition/direction/unit from same section | p. 41 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT ... | comparison identity and matched condition | p. 7 (5.2. Evaluation Results) |
| Across all levels of zero-shot generalization, we find that VIMA strongly outperforms other alternatives. | comparison identity and matched condition | p. 6 (5.2. Evaluation Results) |
| We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes. | comparison identity and matched condition | p. 6 (5.2. Evaluation Results) |
| In contrast, the baselines can degrade as much as 20%, particularly in more difficult generalization scenarios. | comparison identity and matched condition | p. 7 (5.2. Evaluation Results) |
| Figure 3: VIMA Architecture. We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 6: Ablation on visual tokenizers. We compare the performance of VIMA-200M model across different visual tokenizers. Our proposed object tokens outperform all methods ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the ... | component/input/data sensitivity | p. 6 (5.2. Evaluation Results) |
| Finally, we compare the relative performance degradation as we test the models on progressively challenging zero-shot evaluation levels without further fine-tuning (Fig. | component/input/data sensitivity | p. 7 (5.2. Evaluation Results) |
| We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes. | component/input/data sensitivity | p. 6 (5.2. Evaluation Results) |
| Figure 7: Ablation on prompt conditioning. We compare our method (xattn: cross-attention prompt conditioning) with a vanilla transformer decoder (gpt-decoder) across different model sizes. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that ... | Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (Figure/Table caption) |
| Primary metric/result | We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the ... | numeric claim only at cited anchor | p. 6 (5.2. Evaluation Results) |

- Numeric sentences retained from the body:
- **p. 3 / 2. Multimodal Prompts for Task Specification - extractive body cue:** VIMA: General Robot Manipulation with Multimodal Prompts Training Level 1 Object Placement Level 2 Novel Combination Level 3 Novel Object Level 4 Novel Task Put ...
- **p. 3 / 6. Visual reasoning - extractive body cue:** Specifically, we provide 17 tasks with multimodal prompt templates, which can be instantiated into thousands of task instances.
- **p. 3 / 6. Visual reasoning - extractive body cue:** Each task belongs to one or more of the 6 task categories mentioned above.
- **p. 4 / 6. Visual reasoning - extractive body cue:** We hold out a subset of objects and textures for evaluation and designate 4 out of 17 tasks as a testbed for zero-shot generalization.
- **p. 5 / 4. Novel task generalization. New tasks with novel - extractive body cue:** VIMA: General Robot Manipulation with Multimodal Prompts 2 4 8 16 32 64 128 256 Model Size (M) 0 20 40 60 80 L1 2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Multimodal prompts for task specification. We observe that many robot manipulation tasks can be expressed as multimodal prompts that interleave language and ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Therefore, we recommend our agent design as a solid starting point for future work. | p. 9 (7. Conclusion) |
| body limitation/failure cue | We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the ... | p. 6 (5.2. Evaluation Results) |
| body limitation/failure cue | In contrast, the baselines can degrade as much as 20%, particularly in more difficult generalization scenarios. | p. 7 (5.2. Evaluation Results) |
| body limitation/failure cue | These results suggest that VIMA has developed a more generalizable policy and robust representations than the alternative approaches. | p. 7 (5.2. Evaluation Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We open-source the simulation environment, training dataset, algorithm code, and pre-trained model checkpoints to ensure reproducibility and facilitate future work from the community. | p. 2 (1. Introduction) |
| The encoder size is kept constant (T5-Base, 111M) for all methods and excluded from the parameter count. | p. 6 (5.2. Evaluation Results) |
| We then compute object tokens by encoding them with a bounding box encoder and a ViT (Dosovitskiy et al., 2020), respectively. | p. 5 (4. Novel task generalization. New tasks with novel) |
| We compute key KP and value VP sequences from the prompt and query QH from the trajectory history, following the encoder-decoder convention in Raffel ... | p. 5 (4. Novel task generalization. New tasks with novel) |
| Code and video demos are available at vimalabs.github.io. | p. 1 (Abstract) |
| The transformer decoder is conditioned on the prompt via cross-attention layers that alternate with the usual causal self-attention. | p. 2 (1. Introduction) |
| During test time, we execute agent policies in the simulator for multiple episodes to compute a percentage success rate. | p. 4 (6. Visual reasoning) |
| We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention layers. | p. 4 (6. Visual reasoning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Multimodal prompts for task specification. We observe that many robot manipulation tasks can be expressed as multimodal prompts that interleave language and image/video ...
- **p. 9 / 7. Conclusion - extractive body cue:** Therefore, we recommend our agent design as a solid starting point for future work.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the performance, ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** In contrast, the baselines can degrade as much as 20%, particularly in more difficult generalization scenarios.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** These results suggest that VIMA has developed a more generalizable policy and robust representations than the alternative approaches.

- **Evidence anchors reviewed:** datasets p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), metrics p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (Figure/Table caption), p. 38 (Figure/Table caption), baselines p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (Figure/Table caption), results p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model sizes and generalization levels, VIMA ... (p. 5, Figure/Table caption).
- **Metric evidence:** We compare model performance at 0.1%, 1%, 10% and full imitation learning dataset provided in VIMA-BENCH (Fig. (p. 6, 5.2. Evaluation Results).
- **Baseline/ablation evidence:** VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT L1 L2 L3 L4 0 10 ... (p. 7, 5.2. Evaluation Results).
- **Failure/negative evidence:** To make VIMA robust to detection inaccuracies and failures, we apply object augmentation by randomly injecting false-positive detection outputs. (p. 5, 4. Novel task generalization. New tasks with novel).
