# Evaluation - Unifying 2D and 3D Vision-Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FcTeo26AfZ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167696. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (1. Lifting 2D datasets to 3D improves 3D performance), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 2 (Figure/Table caption), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 8 (4.4. Evaluation on 2D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding)): We observe that incorporating 2D data improves performance in both scenarios, but our approach of lifting 2D images to 3D achieves the best results.

## Evaluation Body Digest

- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald et ...
- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** GT, where our model and baselines use groundtruth 3D object proposals provided in the benchmarks.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** We show results in Table 3 on the validation sets of these benchmarks.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** Alongside question-answer pairs, the dataset includes annotations for the objects referenced in the question, and we supervise our model to predict these in addition to ...
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** We also evaluate UniVLG on the 2D Referential Grounding benchmarks (Kazemzadeh et al., 2014) (Table 4).
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** We train two versions of our model: UniVLG (2D only), which is trained exclusively on 2D datasets, and UniVLG (2D-3D), which is trained on both ...
- **p. 7 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** It dramatically outperforms alternative single stage models, such as BUTDDETR, on the stricter IoU threshold of 0.75, thanks to predicting masks instead of bounding boxes-as ...
- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** Evaluation Metrics: We use the standard top-1 accuracy metric.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Evaluation on 3D Referential Grounding (p. 6); 4.2. Evaluation on Out-of-Domain 3D Referential (p. 7); 4.3. Evaluation on 3D Question Answering (p. 7); 4.4. Evaluation on 2D Referential Grounding (p. 8); 1. Lifting 2D datasets to 3D improves 3D performance (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 1. Lifting 2D datasets to 3D improves 3D performance | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that incorporating 2D data improves performance in both scenarios, but our approach of lifting 2D images to 3D achieves the best results. | p. 8 (1. Lifting 2D datasets to 3D improves 3D performance) |
| 4.1. Evaluation on 3D Referential Grounding | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the GT setup as well, UniVLG significantly outperforms 3D-VisTA and closely matches the performance of the recent work of PQ3D in the setup ... | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. (A) UniVLG achieves state-of-the-art performance performance across a range of referential grounding, question answering, and instance segmentation benchmarks. (B) UniVLG is a ... | p. 2 (Figure/Table caption) |
| 4.1. Evaluation on 3D Referential Grounding | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even without our joint 2D training strategy-and with less 3D data than prior methods-UniVLG-3D-only significantly outperforms all prior methods. | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| 4.4. Evaluation on 2D Referential Grounding | EMPIRICAL / SOURCE-REPORTED EVALUATION | As we show in our experiments, this approach leads to significant improvements in 3D performance without negatively affecting 2D performance. | p. 8 (4.4. Evaluation on 2D Referential Grounding) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald et ...
- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** GT, where our model and baselines use groundtruth 3D object proposals provided in the benchmarks.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** We show results in Table 3 on the validation sets of these benchmarks.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** Alongside question-answer pairs, the dataset includes annotations for the objects referenced in the question, and we supervise our model to predict these in addition to ...
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** We also evaluate UniVLG on the 2D Referential Grounding benchmarks (Kazemzadeh et al., 2014) (Table 4).
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** We train two versions of our model: UniVLG (2D only), which is trained exclusively on 2D datasets, and UniVLG (2D-3D), which is trained on both ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (A) UniVLG achieves state-of-the-art performance performance across a range of referential grounding, question answering, and instance segmentation benchmarks. (B) UniVLG is a unified ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. UniVLG Architecture: A vision language transformer that accepts a language utterance and either (1) a sequence of posed RGB-D images or (2) a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Results on 3D language grounding in 3D mesh and sensor point clouds (PC). We evaluate top-1 accuracy on the official validation set with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Out-of-Domain 3D Referential Grounding Acc@25 in Det. From left-to-right, ScanNet++, HM3D, ARKitScenes, ScanNet (GT), ScanNet (SAMPro3D). See ?? for details.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Results on 3D Visual Question Answering on official validation sets. We evaluate top-1 exact match accuracy (EM@1).
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Results on val sets of 2D Ref. grounding datasets RefCOCO RefCOCO+ RefCOCOg LAVT (Yang et al., 2022) (B) 72.7 62.4 61.2
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. Analysis of Box Head vs Mask Head on ScanRefer Dataset with Acc@25 if not otherwise stated. (a) Parametric vs Non-parametric Query Query Type ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 6. Analysis of 2D training strategies Acc@25 in DetSetup

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald ... | embodiment, simulator version and control stack | p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Task/environment | GT, where our model and baselines use groundtruth 3D object proposals provided in the benchmarks. | reset, timeout, object/scene variation | p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 7 (4.3. Evaluation on 3D Question Answering) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| It dramatically outperforms alternative single stage models, such as BUTDDETR, on the stricter IoU threshold of 0.75, thanks to predicting masks instead of bounding ... | definition/direction/unit from same section | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| Evaluation Metrics: We use the standard top-1 accuracy metric. | definition/direction/unit from same section | p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| We evaluate top-1 accuracy on the official validation set with assuming ground-truth (GT) or without assuming ground-truth proposals (Det). | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Shifting from ground-truth box proposals to a more realistic setup of using predicted box proposals from a SOTA detector results in a drop of ... | definition/direction/unit from same section | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| Figure 6. We analyze the performance of UniVLG and BUTD-DETR on SR3D as the pose and depth error increases. We add gaussian noise to ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| This demonstrates that it is indeed possible to train a single model for both 2D and 3D tasks. | definition/direction/unit from same section | p. 8 (4.4. Evaluation on 2D Referential Grounding) |
| Our results show that co-training with 3D data does not degrade the performance of the version trained solely on 2D data. | definition/direction/unit from same section | p. 8 (4.4. Evaluation on 2D Referential Grounding) |
| Figure 1. (A) UniVLG achieves state-of-the-art performance performance across a range of referential grounding, question answering, and instance segmentation benchmarks. (B) UniVLG is a ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| UniVLG outperforms all prior baselines on both benchmarks. | comparison identity and matched condition | p. 7 (4.3. Evaluation on 3D Question Answering) |
| Nonetheless, even when UniVLG uses sensor pointclouds (which as we showed above result in a 5-15% accuracy drop on these benchmarks), it still outperforms ... | comparison identity and matched condition | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| All two-stage baselines assume access to ground-truth proposals at test-time in the SR3D and NR3D benchmarks; hence we re-evaluate them with predicted boxes coming ... | comparison identity and matched condition | p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Baselines: We compare our model against the state-of-theart two-stage methods of 3D-VisTA (Zhu et al., 2023b), PQ3D (Zhu et al., 2024b) and concurrent work ... | comparison identity and matched condition | p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Figure 1. (A) UniVLG achieves state-of-the-art performance performance across a range of referential grounding, question answering, and instance segmentation benchmarks. (B) UniVLG is a ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| In this work, due to our focus on improving 3D vision-language grounding and resource constraints, we did not train our model on additional 2D ... | comparison identity and matched condition | p. 8 (4.4. Evaluation on 2D Referential Grounding) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In Table 6, we compare three variants of our model: one trained only on 3D data, one trained with 3D data and 2D images ... | component/input/data sensitivity | p. 8 (1. Lifting 2D datasets to 3D improves 3D performance) |
| Table 11. Ablation of visual backbones on 3D language grounding. We evaluate top-1 accuracy on the official validation set without assuming ground-truth proposals (Det). | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Table 10. Effect of Fine-tuning 2D backbones of UniVLG for Acc@25 in DetSetup. SR3D and NR3D are in-domain and Scan- Refer is out-of-domain | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| We show the results of our model, both a 3D-only variant and our full model w/2D data + lifting in Table 2. | component/input/data sensitivity | p. 7 (4.2. Evaluation on Out-of-Domain 3D Referential) |
| Even without our joint 2D training strategy-and with less 3D data than prior methods-UniVLG-3D-only significantly outperforms all prior methods. | component/input/data sensitivity | p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| As we show in our experiments, this approach leads to significant improvements in 3D performance without negatively affecting 2D performance. | component/input/data sensitivity | p. 8 (4.4. Evaluation on 2D Referential Grounding) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D ... | We observe that incorporating 2D data improves performance in both scenarios, but our approach of lifting 2D images to 3D achieves the best results. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (1. Lifting 2D datasets to 3D improves 3D performance), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 2 (Figure/Table caption), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 8 (4.4. Evaluation on 2D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Primary metric/result | In the GT setup as well, UniVLG significantly outperforms 3D-VisTA and closely matches the performance of the recent work of PQ3D in the setup ... | numeric claim only at cited anchor | p. 7 (4.1. Evaluation on 3D Referential Grounding) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald et ...
- **p. 8 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** Results on val sets of 2D Ref. grounding datasets RefCOCO RefCOCO+ RefCOCOg LAVT (Yang et al., 2022) (B) 72.7 62.4 61.2 ReSTR (Kim et al., ...
- **p. 5 / 3.1. Supervision Objective - extractive body cue:** For 3D scenes, we compute CLIP embeddings for all images and captions and use this to select 5 relevant frames, with an additional 10 frames ...
- **p. 5 / 3.1. Supervision Objective - extractive body cue:** Our method provides for fast inference, with a 90-frame scene taking ∼1050ms and ∼15GB of VRAM on an A100 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We identify three systematic failure modes in our model, illustrated in Figure-5 (see Appendix). | p. 9 (4.7. Common failure modes of UniVLG) |
| body limitation/failure cue | Classes UniVLG 72.6 53.8 UniVLG w/o 2D-to-3D lifting 71.4 0.0 UniVLG (Upper-Bound) 69.7 84.2 Grounding failures as seen in the third image of Figure-5. | p. 9 (4.7. Common failure modes of UniVLG) |
| body limitation/failure cue | Figure 5. Systematic failure modes of UniVLG: Green boxes and masks are ground-truth, red masks and boxes are UniVLG's predictions. COCO/+/g datasets (Kazemzadeh et ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Our results show that co-training with 3D data does not degrade the performance of the version trained solely on 2D data. | p. 8 (4.4. Evaluation on 2D Referential Grounding) |
| body limitation/failure cue | We found that using sensor point clouds vs mesh point clouds does not result in a significant difference in performance in these benchmarks, likely ... | p. 7 (4.3. Evaluation on 3D Question Answering) |
| body limitation/failure cue | L3DD allows us to assess the robustness of our model on new scenes, camera capture systems, and language instructions. | p. 7 (4.2. Evaluation on Out-of-Domain 3D Referential) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Similarly, PQ3D adds the Multi3DRefer (Zhang et al., 2023) and Scan2Cap datasets (Chen et al., 2020b), but also utilizes a point encoder that was ... | p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| We also compare with 3D-VisTA (Zhu et al., 2023b) and PQ3D (Zhu et al., 2024b) which use small decoder heads like T5-small (Raffel et ... | p. 7 (4.3. Evaluation on 3D Question Answering) |
| Results on val sets of 2D Ref. grounding datasets RefCOCO RefCOCO+ RefCOCOg LAVT (Yang et al., 2022) (B) 72.7 62.4 61.2 ReSTR (Kim et ... | p. 8 (4.3. Evaluation on 3D Question Answering) |
| Implementation details: UniVLG consists of 108M trainable parameters along with a frozen 220M parameter textencoder (Koukounas et al., 2024) and a 304M parameter image-encoder ... | p. 5 (3.1. Supervision Objective) |
| We train in data-parallel across 32 A100 80G GPUs with an effective batch size of 64. | p. 5 (3.1. Supervision Objective) |
| This attention mechanism uses feature maps from the ViT encoder, with 3D pointmaps serving as the positional embeddings. | p. 3 (3. Method) |
| Language Encoder: We embed the natural language query using JinaCLIP (Koukounas et al., 2024), generating tokens of shape M × F where M is ... | p. 3 (3. Method) |
| Masks are decoded through a dot-product between 3D feature tokens and learnable queries. | p. 4 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.7. Common failure modes of UniVLG - extractive body cue:** We identify three systematic failure modes in our model, illustrated in Figure-5 (see Appendix).
- **p. 9 / 4.7. Common failure modes of UniVLG - extractive body cue:** Classes UniVLG 72.6 53.8 UniVLG w/o 2D-to-3D lifting 71.4 0.0 UniVLG (Upper-Bound) 69.7 84.2 Grounding failures as seen in the third image of Figure-5.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 5. Systematic failure modes of UniVLG: Green boxes and masks are ground-truth, red masks and boxes are UniVLG's predictions. COCO/+/g datasets (Kazemzadeh et al., ...
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** Our results show that co-training with 3D data does not degrade the performance of the version trained solely on 2D data.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** We found that using sensor point clouds vs mesh point clouds does not result in a significant difference in performance in these benchmarks, likely because ...
- **p. 7 / 4.2. Evaluation on Out-of-Domain 3D Referential - extractive body cue:** L3DD allows us to assess the robustness of our model on new scenes, camera capture systems, and language instructions.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 7 (4.3. Evaluation on 3D Question Answering), p. 7 (4.3. Evaluation on 3D Question Answering), p. 8 (4.4. Evaluation on 2D Referential Grounding), p. 8 (4.4. Evaluation on 2D Referential Grounding), metrics p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4. Experiments), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 21 (Figure/Table caption), p. 8 (4.4. Evaluation on 2D Referential Grounding), baselines p. 7 (4.3. Evaluation on 3D Question Answering), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 2 (Figure/Table caption), p. 8 (4.4. Evaluation on 2D Referential Grounding), results p. 8 (1. Lifting 2D datasets to 3D improves 3D performance), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 2 (Figure/Table caption), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 8 (4.4. Evaluation on 2D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
