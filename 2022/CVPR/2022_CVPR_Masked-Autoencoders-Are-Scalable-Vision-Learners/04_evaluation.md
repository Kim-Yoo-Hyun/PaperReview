# Evaluation - Masked Autoencoders Are Scalable Vision Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.06377; PDF retrieval source: https://arxiv.org/pdf/2111.06377. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5. Transfer Learning Experiments), p. 5 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 7 (4.2. Comparisons with Previous Results)): More significantly, with the larger ViT-L, our MAE pre-training outperforms supervised pre-training by 4.0 points (53.3 vs.

## Evaluation Body Digest

- **p. 4 / 4.1. Main Properties - extractive PDF cue:** It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** Wall-clock time of our MAE training (800 epochs), benchmarked in 128 TPU-v3 cores with TensorFlow.
- **p. 8 / 5. Transfer Learning Experiments - extractive PDF cue:** Transfer learning accuracy on classification datasets, using MAE pre-trained on IN1K and then fine-tuned.
- **p. 8 / 5. Transfer Learning Experiments - extractive PDF cue:** Self-supervised entries use IN1K data without labels. dataset ViT-B ViT-L ViT-H ViT-H448 prev best iNat 2017 70.5 75.7 79.3 83.4 75.4 [55] iNat 2018 75.4 ...
- **p. 4 / 4. ImageNet Experiments - extractive PDF cue:** We do self-supervised pre-training on the ImageNet-1K (IN1K) [13] training set.
- **p. 7 / 4.2. Comparisons with Previous Results - extractive PDF cue:** Even so, our total pre-training time is less than the other methods when trained on the same hardware.
- **p. 7 / 4.2. Comparisons with Previous Results - extractive PDF cue:** We improve over the state-of-the-art by a nontrivial margin in the highly competitive benchmark of IN1K (no external data).
- **p. 12 / A. Implementation Details - extractive PDF cue:** We adjust the lr and finetuning epochs for each individual dataset. method model params acc iGPT [6] iGPT-L 1362 M 69.0 iGPT [6] iGPT-XL 6801 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4. ImageNet Experiments (p. 4); 4.2. Comparisons with Previous Results (p. 7); 5. Transfer Learning Experiments (p. 8); A. Implementation Details (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5. Transfer Learning Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | More significantly, with the larger ViT-L, our MAE pre-training outperforms supervised pre-training by 4.0 points (53.3 vs. | p. 8 (5. Transfer Learning Experiments) |
| 4.1. Main Properties | EMPIRICAL / REAL-ROBOT OR HARDWARE | By removing the mask token from the encoder, we constrain the encoder to always see real patches and thus improve accuracy. | p. 5 (4.1. Main Properties) |
| 4.1. Main Properties | EMPIRICAL / REAL-ROBOT OR HARDWARE | A deep decoder can improve linear probing accuracy. dim ft lin 128 84.9 69.1 256 84.8 71.3 512 84.9 73.5 768 84.4 73.1 1024 ... | p. 5 (4.1. Main Properties) |
| 4.1. Main Properties | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using pixels with normalization improves accuracy. | p. 6 (4.1. Main Properties) |
| 4.1. Main Properties | EMPIRICAL / REAL-ROBOT OR HARDWARE | The accuracy improves steadily with longer training. | p. 6 (4.1. Main Properties) |

## Dataset / Benchmark Role

- **p. 4 / 4.1. Main Properties - extractive PDF cue:** It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** Wall-clock time of our MAE training (800 epochs), benchmarked in 128 TPU-v3 cores with TensorFlow.
- **p. 8 / 5. Transfer Learning Experiments - extractive PDF cue:** Transfer learning accuracy on classification datasets, using MAE pre-trained on IN1K and then fine-tuned.
- **p. 8 / 5. Transfer Learning Experiments - extractive PDF cue:** Self-supervised entries use IN1K data without labels. dataset ViT-B ViT-L ViT-H ViT-H448 prev best iNat 2017 70.5 75.7 79.3 83.4 75.4 [55] iNat 2018 75.4 ...
- **p. 4 / 4. ImageNet Experiments - extractive PDF cue:** We do self-supervised pre-training on the ImageNet-1K (IN1K) [13] training set.
- **p. 7 / 4.2. Comparisons with Previous Results - extractive PDF cue:** Even so, our total pre-training time is less than the other methods when trained on the same hardware.
- **p. 7 / 4.2. Comparisons with Previous Results - extractive PDF cue:** We improve over the state-of-the-art by a nontrivial margin in the highly competitive benchmark of IN1K (no external data).
- **p. 12 / A. Implementation Details - extractive PDF cue:** We adjust the lr and finetuning epochs for each individual dataset. method model params acc iGPT [6] iGPT-L 1362 M 69.0 iGPT [6] iGPT-XL 6801 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Our MAE architecture. During pre-training, a large random subset of image patches (e.g., 75%) is masked out. The encoder is applied to the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Example results on ImageNet validation images. For each triplet, we show the masked image (left), our MAE reconstruction† (middle), and the ground-truth (right). ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 3. Example results on COCO validation images, using an MAE trained on ImageNet (the same model weights as in Figure 2). Observe the reconstructions ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 4. Reconstructions of ImageNet validation images using an MAE pre-trained with a masking ratio of 75% but applied on inputs with higher masking ratios. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. Masking ratio. A high masking ratio (75%) works well for both fine-tuning (top) and linear probing (bottom). The y-axes are ImageNet-1K validation accuracy ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. MAE ablation experiments with ViT-L/16 on ImageNet-1K. We report fine-tuning (ft) and linear probing (lin) accuracy (%). If not specified, the default is: ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Wall-clock time of our MAE training (800 epochs), benchmarked in 128 TPU-v3 cores with TensorFlow. The speedup is relative to the entry whose ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Mask sampling strategies determine the pretext task difficulty, influencing reconstruction quality and representations (Table 1f). Here each output is from an MAE trained ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures. | embodiment, simulator version and control stack | p. 4 (4.1. Main Properties), p. 5 (4.1. Main Properties) |
| Task/environment | Wall-clock time of our MAE training (800 epochs), benchmarked in 128 TPU-v3 cores with TensorFlow. | reset, timeout, object/scene variation | p. 5 (4.1. Main Properties), p. 8 (5. Transfer Learning Experiments) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 4 (3. Approach), p. 2 (1. Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 13. Robustness evaluation on ImageNet variants (top-1 accuracy, except for IN-C [27] which evaluates mean corruption error). We test the same MAE models ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Our implementation of supervised training (see A.2) works better, but accuracy saturates. | definition/direction/unit from same section | p. 7 (4.2. Comparisons with Previous Results) |
| We report top-1 validation accuracy of a single 224×224 crop. | definition/direction/unit from same section | p. 4 (4. ImageNet Experiments) |
| 200 from scratch), implying that the fine-tuning accuracy heavily depends on pre-training. | definition/direction/unit from same section | p. 4 (4. ImageNet Experiments) |
| This gap may degrade accuracy in deployment. | definition/direction/unit from same section | p. 5 (4.1. Main Properties) |
| We report fine-tuning (ft) and linear probing (lin) accuracy (%). | definition/direction/unit from same section | p. 5 (4.1. Main Properties) |
| It also reduces linear probing accuracy. | definition/direction/unit from same section | p. 6 (4.1. Main Properties) |
| Using pixels with normalization improves accuracy. | definition/direction/unit from same section | p. 6 (4.1. Main Properties) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The following is a comparison between ViT-L trained from scratch vs. fine-tuned from our baseline MAE: scratch, original [16] scratch, our impl. baseline MAE ... | comparison identity and matched condition | p. 4 (4. ImageNet Experiments) |
| While there have been strong baselines with publicly available implementations [53] for smaller models, the recipes for the larger ViT-L/H are unexplored. | comparison identity and matched condition | p. 11 (A. Implementation Details) |
| We improve over the state-of-the-art by a nontrivial margin in the highly competitive benchmark of IN1K (no external data). | comparison identity and matched condition | p. 7 (4.2. Comparisons with Previous Results) |
| 0 1 2 4 6 12 18 24 70 75 80 85 73.5 81.0 83.1 84.2 84.4 84.6 84.7 84.9 77.6 79.9 80.8 81.6 ... | comparison identity and matched condition | p. 7 (4.2. Comparisons with Previous Results) |
| Our pixel-based MAE also outperforms the token-based BEiT. | comparison identity and matched condition | p. 8 (5. Transfer Learning Experiments) |
| Compared to supervised pre-training, our MAE performs better under all configurations (Table 4). | comparison identity and matched condition | p. 8 (5. Transfer Learning Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We note that the layer does not break the linear property, and it can be absorbed into the linear classifier after training: it is ... | component/input/data sensitivity | p. 11 (A. Implementation Details) |
| Table 13. Robustness evaluation on ImageNet variants (top-1 accuracy, except for IN-C [27] which evaluates mean corruption error). We test the same MAE models ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| We use ViT-Large (ViT-L/16) [16] as the backbone in our ablation study. | component/input/data sensitivity | p. 4 (4. ImageNet Experiments) |
| MAE ablation experiments with ViT-L/16 on ImageNet-1K. | component/input/data sensitivity | p. 5 (4.1. Main Properties) |
| An encoder without mask tokens is more accurate and faster (Table 2). case ft lin pixel (w/o norm) 84.9 73.5 pixel (w/ norm) 85.4 ... | component/input/data sensitivity | p. 5 (4.1. Main Properties) |
| Our ablations thus far are based on 800-epoch pre-training. | component/input/data sensitivity | p. 6 (4.1. Main Properties) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning. | More significantly, with the larger ViT-L, our MAE pre-training outperforms supervised pre-training by 4.0 points (53.3 vs. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5. Transfer Learning Experiments), p. 5 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 7 (4.2. Comparisons with Previous Results) |
| Primary metric/result | By removing the mask token from the encoder, we constrain the encoder to always see real patches and thus improve accuracy. | numeric claim only at cited anchor | p. 5 (4.1. Main Properties) |

- Numeric sentences retained from the body:
- **p. 4 / 4. ImageNet Experiments - extractive PDF cue:** We report top-1 validation accuracy of a single 224×224 crop.
- **p. 4 / 4. ImageNet Experiments - extractive PDF cue:** Here fine-tuning is only for 50 epochs (vs.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** If not specified, the default is: the decoder has depth 8 and width 512, the reconstruction target is unnormalized pixels, the data augmentation is random ...
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** Wall-clock time of our MAE training (800 epochs), benchmarked in 128 TPU-v3 cores with TensorFlow.
- **p. 6 / 4.1. Main Properties - extractive PDF cue:** Indeed, we have not observed saturation of linear probing accuracy even at 1600 epochs.
- **p. 6 / 4.1. Main Properties - extractive PDF cue:** This behavior is unlike contrastive learning methods, e.g., MoCo v3 [9] saturates at 300 epochs for ViT-L.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hope this perspective will inspire future work. | p. 8 (6. Discussion and Conclusion) |
| body limitation/failure cue | It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures. | p. 4 (4.1. Main Properties) |
| body limitation/failure cue | In this case, there is a gap between pre-training and deploying: this encoder has a large portion of mask tokens in its input in ... | p. 5 (4.1. Main Properties) |
| body limitation/failure cue | Using pixels does not suffer from these problems. | p. 6 (4.1. Main Properties) |
| body limitation/failure cue | Directly applying the previous recipes to these larger models does not work. | p. 11 (A. Implementation Details) |
| body limitation/failure cue | Our MAE does not use relative position or layer scaling (which are used in the code of [2]). | p. 11 (A. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3Alternatively, we can pre-compute the mean and std of the features and use the normalized features to train linear classifiers. config value optimizer AdamW ... | p. 11 (A. Implementation Details) |
| Pre-training setting. config value optimizer AdamW base learning rate 1e-3 weight decay 0.05 optimizer momentum β1, β2=0.9, 0.999 layer-wise lr decay [10, 2] 0.75 ... | p. 11 (A. Implementation Details) |
| We fine-tune end-to-end for 100 epochs with a batch size of 16. | p. 12 (A. Implementation Details) |
| The hyper-parameters we search for are the learning rate, weight decay, drop path rate, and fine-tuning epochs. | p. 12 (A. Implementation Details) |
| The decoder width is 512, and the mask ratio is 75%. †: This entry is estimated by training ten epochs. | p. 5 (4.1. Main Properties) |
| If not specified, the default is: the decoder has depth 8 and width 512, the reconstruction target is unnormalized pixels, the data augmentation is ... | p. 5 (4.1. Main Properties) |
| With this asymmetrical design, the full set of tokens are only processed by the lightweight decoder, which significantly reduces pre-training time. | p. 4 (3. Approach) |
| Even so, our total pre-training time is less than the other methods when trained on the same hardware. | p. 7 (4.2. Comparisons with Previous Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Discussion and Conclusion - extractive PDF cue:** We hope this perspective will inspire future work.
- **p. 4 / 4.1. Main Properties - extractive PDF cue:** It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** In this case, there is a gap between pre-training and deploying: this encoder has a large portion of mask tokens in its input in pretraining, ...
- **p. 6 / 4.1. Main Properties - extractive PDF cue:** Using pixels does not suffer from these problems.
- **p. 11 / A. Implementation Details - extractive PDF cue:** Directly applying the previous recipes to these larger models does not work.
- **p. 11 / A. Implementation Details - extractive PDF cue:** Our MAE does not use relative position or layer scaling (which are used in the code of [2]).

- **PDF anchors reviewed:** datasets p. 4 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 8 (5. Transfer Learning Experiments), p. 8 (5. Transfer Learning Experiments), p. 4 (4. ImageNet Experiments), p. 7 (4.2. Comparisons with Previous Results), metrics p. 12 (Figure/Table caption), p. 7 (4.2. Comparisons with Previous Results), p. 4 (4. ImageNet Experiments), p. 4 (4. ImageNet Experiments), p. 5 (4.1. Main Properties), p. 5 (4.1. Main Properties), baselines p. 4 (4. ImageNet Experiments), p. 11 (A. Implementation Details), p. 7 (4.2. Comparisons with Previous Results), p. 7 (4.2. Comparisons with Previous Results), p. 8 (5. Transfer Learning Experiments), p. 8 (5. Transfer Learning Experiments), results p. 8 (5. Transfer Learning Experiments), p. 5 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 7 (4.2. Comparisons with Previous Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
