# Evaluation - BlenderAlchemy: Editing 3D Graphics with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12578.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments)): Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has no visual compo- nents (-Vision) still ...

## Evaluation Body Digest

- **p. 12 / 4 Experiments - extractive body cue:** We show qualitative examples of our system controlling geometry by programmatically 1) interpolating between preset blend shapes, 2) editing of geometry node graphs, and 3) ...
- **p. 13 / 4 Experiments - extractive body cue:** In Figure 8(a), BlenderAlchemy is presented with a scene layout editing task, where assets are initially dropped out of camera view and must be iteratively ...
- **p. 13 / 4 Experiments - extractive body cue:** 4.3 Lighting Setup Editing We show that BlenderAlchemy can be used to adjust the lighting of scenes according to language instructions as well.
- **p. 14 / 4 Experiments - extractive body cue:** As mentioned in Section 3.1, we can consider iteratively optimizing two separate programs, one controlling the lighting of the whole scene and another controlling the ...
- **p. 9 / 4 Experiments - extractive body cue:** We compare against BlenderGPT, the most recent open-sourced Blender AI agent that use GPT-4 to execute actions within the Blender environment through the Python API.
- **p. 9 / 4 Experiments - extractive body cue:** In reality, this is a very challenging task, since this may require a wide range in the size of edits even if the language describing ...
- **p. 11 / 4 Experiments - extractive body cue:** BlenderGPT for the text-based material editing task.
- **p. 11 / 4 Experiments - extractive body cue:** Image-based material-editing Given an image of a desired material, the task is to convert the code of the starter material into a material that contains ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has ... | p. 11 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1: Overview of BlenderAlchemy. Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the ... | p. 2 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | To match the number of edit generator queries we make, we run their method a maximum of 32 times, using the first successful example ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that BlenderAlchemy is preferred to Paint3D 73% of the time. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We additionally conducted a user preference study to compare BlenderAlchemy's performance with two material generation baselines that use diffusion: TEXTure [33] and Paint3D [60]. | p. 10 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 12 / 4 Experiments - extractive body cue:** We show qualitative examples of our system controlling geometry by programmatically 1) interpolating between preset blend shapes, 2) editing of geometry node graphs, and 3) ...
- **p. 13 / 4 Experiments - extractive body cue:** In Figure 8(a), BlenderAlchemy is presented with a scene layout editing task, where assets are initially dropped out of camera view and must be iteratively ...
- **p. 13 / 4 Experiments - extractive body cue:** 4.3 Lighting Setup Editing We show that BlenderAlchemy can be used to adjust the lighting of scenes according to language instructions as well.
- **p. 14 / 4 Experiments - extractive body cue:** As mentioned in Section 3.1, we can consider iteratively optimizing two separate programs, one controlling the lighting of the whole scene and another controlling the ...
- **p. 9 / 4 Experiments - extractive body cue:** We compare against BlenderGPT, the most recent open-sourced Blender AI agent that use GPT-4 to execute actions within the Blender environment through the Python API.
- **p. 9 / 4 Experiments - extractive body cue:** In reality, this is a very challenging task, since this may require a wide range in the size of edits even if the language describing ...
- **p. 11 / 4 Experiments - extractive body cue:** BlenderGPT for the text-based material editing task.
- **p. 11 / 4 Experiments - extractive body cue:** Image-based material-editing Given an image of a desired material, the task is to convert the code of the starter material into a material that contains ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of BlenderAlchemy. Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 3: Text-based Material Editing Results. The step-by-step edits of a 4x8 version of BlenderAlchemy to the same wooden material, given the text description on ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4: The edit discovery process of turning a wooden material into "mar- bled granite". Each column shows the hypotheses generated by G, with the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has no ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 5: Comparisons between our method and BlenderGPT for the text- based material editing task setting. Note how our materials align better with the original ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6: Material editing based on image inputs. Our edit intention is described by the target image shown on the right. 5 different Infinigen [32] ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7: BlenderAlchemy editing geometry using blend shapes. Edits are made to match a description or a script line. Input shapes from BlenderKit.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We show qualitative examples of our system controlling geometry by programmatically 1) interpolating between preset blend shapes, 2) editing of geometry node graphs, and ... | embodiment, simulator version and control stack | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Task/environment | In Figure 8(a), BlenderAlchemy is presented with a scene layout editing task, where assets are initially dropped out of camera view and must be ... | reset, timeout, object/scene variation | p. 13 (4 Experiments), p. 13 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 7 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.1 Procedural Material Editing Procedural material editing has characteristics that make it difficult for the same reason as a lot of other visual program ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Fig. 3: Text-based Material Editing Results. The step-by-step edits of a 4x8 version of BlenderAlchemy to the same wooden material, given the text description ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| We demonstrate BlenderAlchemy on editing procedural materials, geometry and lighting setups within Blender, three of the most tedious parts of 3D design. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| To match the number of edit generator queries we make, we run their method a maximum of 32 times, using the first successful example ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Our system is composed of an edit generator that generates 8 hypotheses per iteration, for 4 iterations (d = 4, b = 8), cycling ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We additionally conducted a user preference study to compare BlenderAlchemy's performance with two material generation baselines that use diffusion: TEXTure [33] and Paint3D [60]. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Each column shows the hypotheses generated by G, with the most promising candidates chosen by V indicated by the highlights. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We collect 592 Mechanical Turk comparisons between BlenderAlchemy and the baselines from 24 Turkers on materials created using 32 different text prompts. | comparison identity and matched condition | p. 10 (4 Experiments) |
| We additionally conducted a user preference study to compare BlenderAlchemy's performance with two material generation baselines that use diffusion: TEXTure [33] and Paint3D [60]. | comparison identity and matched condition | p. 10 (4 Experiments) |
| We find that a version of our system that has no visual components (-Vision) still outperforms BlenderGPT. | comparison identity and matched condition | p. 11 (4 Experiments) |
| BlenderGPT reasons only about how to edit the program using the input text description, doing so in a single pass without state evaluation or ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Our system is the same as for text-based material editing, but without the need for visual imagination. | comparison identity and matched condition | p. 11 (4 Experiments) |
| 5: Comparisons between our method and BlenderGPT for the textbased material editing task setting. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| BlenderGPT reasons only about how to edit the program using the input text description, doing so in a single pass without state evaluation or ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Our system is the same as for text-based material editing, but without the need for visual imagination. | component/input/data sensitivity | p. 11 (4 Experiments) |
| Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| We find that a version of our system that has no visual components (-Vision) still outperforms BlenderGPT. | component/input/data sensitivity | p. 11 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1]. | Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Primary metric/result | Fig. 1: Overview of BlenderAlchemy. Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | For instance, observe that for the "digital camouflage" example, BlenderAlchemy is able to produce the "sharper angles" that the original description requests (See Figure ... | p. 9 (4 Experiments) |
| body limitation/failure cue | We've demonstrated BlenderAlchemy on editing materials, geometry and lighting, and hope that future works will extend this to other workflows as well. | p. 14 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.1 Procedural Material Editing Procedural material editing has characteristics that make it difficult for the same reason as a lot of other visual program ... | p. 8 (4 Experiments) |
| 2 We provide the same target material text prompt to BlenderGPT, as well as the starter code for the initial wood material for reference. | p. 9 (4 Experiments) |
| To match the number of edit generator queries we make, we run their method a maximum of 32 times, using the first successful example ... | p. 9 (4 Experiments) |
| Image-based material-editing Given an image of a desired material, the task is to convert the code of the starter material into a material that ... | p. 11 (4 Experiments) |
| At each step, the edit generator is first asked to textually enumerate a list of obvious visual differences between the current material and the ... | p. 11 (4 Experiments) |
| 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender state Sbase ... | p. 5 (3 Method) |
| 6 Huang et al. "node transpiler" from Infinigen [32], which converts entities within the Blender instance into lines of Python code that can recreate ... | p. 6 (3 Method) |
| Though it's possible for all edits to be encompassed in a single program instead of k programs, this is limiting in practice - either ... | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential ...
- **p. 9 / 4 Experiments - extractive body cue:** For instance, observe that for the "digital camouflage" example, BlenderAlchemy is able to produce the "sharper angles" that the original description requests (See Figure 3) ...
- **p. 14 / 4 Experiments - extractive body cue:** We've demonstrated BlenderAlchemy on editing materials, geometry and lighting, and hope that future works will extend this to other workflows as well.

- **Evidence anchors reviewed:** datasets p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), metrics p. 8 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 11 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
