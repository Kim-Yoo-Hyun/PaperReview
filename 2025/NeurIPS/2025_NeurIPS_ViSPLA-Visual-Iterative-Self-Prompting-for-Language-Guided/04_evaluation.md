# Evaluation - ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=EyNzLH7BZK; PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 1 (Abstract), p. 9 (Figure/Table caption), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (Figure/Table caption)): Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across the PIAD benchmark, as shown in ...

## Evaluation Body Digest

- **p. 1 / Abstract - extractive body cue:** Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.
- **p. 1 / 1 Introduction - extractive body cue:** The evolution of robotic systems toward increasingly unstructured environments necessitates a fundamental paradigm shift in how we conceptualize affordance detection.
- **p. 2 / 1 Introduction - extractive body cue:** Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts.
- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, 3D affordance detection methods typically remain limited to static, single-affordance settings, with little capacity to handle instructions requiring compositional or context-aware reasoning across multiple ...
- **p. 3 / 1 Introduction - extractive body cue:** Unlike existing single-pass methods, our approach establishes a self-improving cycle that enhances precision across multiple object geometries. • We propose a novel Differential Geometric Self-Prompting ...
- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...
- **p. 3 / 1 Introduction - extractive body cue:** accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction across ...
- **p. 3 / 1 Introduction - extractive body cue:** In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across ... | p. 8 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | p. 1 (Abstract) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. (3) The most substantial gains come from incorporating Iterative Differential Geometry-Based Self-Prompting (IDGSP), which provides a significant boost on LASO seen (+2.5 ... | p. 9 (Figure/Table caption) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction ... | p. 3 (1 Introduction) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes ... | p. 3 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive body cue:** Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.
- **p. 1 / 1 Introduction - extractive body cue:** The evolution of robotic systems toward increasingly unstructured environments necessitates a fundamental paradigm shift in how we conceptualize affordance detection.
- **p. 2 / 1 Introduction - extractive body cue:** Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts.
- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, 3D affordance detection methods typically remain limited to static, single-affordance settings, with little capacity to handle instructions requiring compositional or context-aware reasoning across multiple ...
- **p. 3 / 1 Introduction - extractive body cue:** Unlike existing single-pass methods, our approach establishes a self-improving cycle that enhances precision across multiple object geometries. • We propose a novel Differential Geometric Self-Prompting ...
- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Traditional vision-based methods [3, 4] rely on trainable network fθ to predict a fixed set of affordances fθ : P 7→A; A ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the ViSPLA framework: given a point cloud P and a language instruction L, first we extract geometric features X = fP ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Performance analysis (aIoU on "seen" setting) with varying T and K values. Following 3D-AffordanceLLM [6], we utilize Phi-3.5-mini-instruct [27] as our base LLM ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Qualitative comparison of our proposed method on the PIAD (left) and LASO (right) datasets. The best and second-best results are highlighted in red ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative visualization of ablation
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. (3) The most substantial gains come from incorporating Iterative Differential Geometry-Based Self-Prompting (IDGSP), which provides a significant boost on LASO seen (+2.5 aIoU) ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Ablation study of different components. The best results are in bold. Type PIAD LASO IDGSP INAFS SCSP aIoU

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | embodiment, simulator version and control stack | p. 1 (Abstract), p. 1 (1 Introduction) |
| Task/environment | The evolution of robotic systems toward increasingly unstructured environments necessitates a fundamental paradigm shift in how we conceptualize affordance detection. | reset, timeout, object/scene variation | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction ... | definition/direction/unit from same section | p. 3 (1 Introduction) |
| In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes ... | definition/direction/unit from same section | p. 3 (1 Introduction) |
| Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | definition/direction/unit from same section | p. 1 (Abstract) |
| To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision. | definition/direction/unit from same section | p. 1 (Abstract) |
| This disconnect motivates a more integrated, multimodal approach that unifies linguistic understanding with spatial perception. | definition/direction/unit from same section | p. 2 (1 Introduction) |
| The final refined mask MT integrates both semantic guidance and geometric consistency, enabling robust and generalizable affordance segmentation across varying levels of granularity and ... | definition/direction/unit from same section | p. 2 (1 Introduction) |
| Figure 3: Performance analysis (aIoU on "seen" setting) with varying T and K values. Following 3D-AffordanceLLM [6], we utilize Phi-3.5-mini-instruct [27] as our base ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | comparison identity and matched condition | p. 1 (Abstract) |
| To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision. | comparison identity and matched condition | p. 1 (Abstract) |
| By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural ... | comparison identity and matched condition | p. 3 (1 Introduction) |
| accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction ... | comparison identity and matched condition | p. 3 (1 Introduction) |
| Table 1: Qualitative comparison of our proposed method on the PIAD (left) and LASO (right) datasets. The best and second-best results are highlighted in ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. (3) The most substantial gains come from incorporating Iterative Differential Geometry-Based Self-Prompting (IDGSP), which provides a significant boost on LASO seen (+2.5 ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 2: Ablation study of different components. The best results are in bold. Type PIAD LASO IDGSP INAFS SCSP aIoU | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision. | component/input/data sensitivity | p. 1 (Abstract) |
| By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural ... | component/input/data sensitivity | p. 3 (1 Introduction) |
| accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction ... | component/input/data sensitivity | p. 3 (1 Introduction) |
| Figure 5: Qualitative visualization of ablation | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as ... | Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 1 (Abstract), p. 9 (Figure/Table caption), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (Figure/Table caption) |
| Primary metric/result | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | numeric claim only at cited anchor | p. 1 (Abstract) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts. | p. 2 (1 Introduction) |
| body limitation/failure cue | The final refined mask MT integrates both semantic guidance and geometric consistency, enabling robust and generalizable affordance segmentation across varying levels of granularity and ... | p. 2 (1 Introduction) |
| body limitation/failure cue | In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes ... | p. 3 (1 Introduction) |
| body limitation/failure cue | 3.5 Overall Learning Strategy To effectively address data scarcity and ensure robust affordance understanding, we adopt a multistage training strategy inspired by 3D-AffordanceLLM [6]. | p. 6 (2 Related Work) |
| body limitation/failure cue | This design enables evaluation of our model's robustness in both instruction-conditioned and shape-driven generalization scenarios. | p. 7 (2 Related Work) |
| body limitation/failure cue | Earlier fusion-based approaches like [33-38] exhibit significantly inferior performance due to their generic multimodal architectures that fail to model the specialized nature of affordance ... | p. 8 (2 Related Work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex spatial structures. | p. 1 (Abstract) |
| Mathematically, we formulate this as: Mt = fθ  P, G(Mt-1), L  ; t ∈{1, 2, .., T}, where M0 = fθ(P, L) is ... | p. 2 (1 Introduction) |
| This approach enables more accurate affordance localization by incorporating intrinsic geometric cues rather than relying solely on language. • We develop a Multi-Stage Refinement ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / 1 Introduction - extractive body cue:** Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts.
- **p. 2 / 1 Introduction - extractive body cue:** The final refined mask MT integrates both semantic guidance and geometric consistency, enabling robust and generalizable affordance segmentation across varying levels of granularity and complexity.
- **p. 3 / 1 Introduction - extractive body cue:** In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes and ...
- **p. 6 / 2 Related Work - extractive body cue:** 3.5 Overall Learning Strategy To effectively address data scarcity and ensure robust affordance understanding, we adopt a multistage training strategy inspired by 3D-AffordanceLLM [6].
- **p. 7 / 2 Related Work - extractive body cue:** This design enables evaluation of our model's robustness in both instruction-conditioned and shape-driven generalization scenarios.
- **p. 8 / 2 Related Work - extractive body cue:** Earlier fusion-based approaches like [33-38] exhibit significantly inferior performance due to their generic multimodal architectures that fail to model the specialized nature of affordance relationships.

- **Evidence anchors reviewed:** datasets p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), metrics p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), baselines p. 1 (Abstract), p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 1 (Abstract), p. 9 (Figure/Table caption), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
