# Insights — Scene-LLM: Extending Language Model for 3D Visual Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this, we propose integrating both types of 3D visual information to an unified visual feature in Scene-LLM.
- **p. 1 / Abstract - extractive body cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We showcase some applications, including describing scene details (scene captioning), identifying and describing objects (object captioning), breaking down complex tasks into simpler steps (task decomposition), ...
- **p. 3 / 3. 3D-Visual-Language Data Generation - extractive body cue:** Our dataset comprises about 9, 000 indoor scenes from three sources: real indoor scans [14], single rooms from the Habitat-Matterport 3D dataset (hm3d) [53], and ...
- **p. 4 / 4. Scene-LLM - extractive body cue:** This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process.
- **p. 5 / 4.1. 3D Visual Feature - extractive body cue:** The scene semantic feature is then updated using: \l abe l {eq u a ti o n: u p da te} \t extbf {F}^{vox}_{t+1} = ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 1 (Body text (section not recovered)), p. 3 (3. 3D-Visual-Language Data Generation), p. 4 (4. Scene-LLM)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive ...
- **p. 2 / 1. Introduction - extractive body cue:** While existing visuallanguage models (VLMs) [5, 15, 34] have made strides in 2D visual-language understanding, their limited grasp of persistent 3D spatial information often renders ...
- **p. 8 / 6. Conclusion - extractive body cue:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive body cue:** A: To enhance safety, consider laying down anti-slip mats by the sink and in any zones where spills are likely to happen.
- **p. 8 / 5.2. Ablation Studies and Discussions - extractive body cue:** While Q-Former is a robust downsampling technique, it exhibits slightly lower performance compared to direct spatial down-sampling in our benchmarks, aligning with findings from [38].
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive body cue:** It measures the ability to create precise and robust plans from a high-level goal in 3D interactive environments from iTHOR [1].
- **Boundary to test:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • We show ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. 3D egocentric representation outperforms ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations. | p. 8 (6. Conclusion), p. 6 (5.1. Results and Benchmark Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 At the egocentric step, 3D frame data and a egocentric instruction are first input to Scene-LLM to describe the current state.를 The updated scene feature, along with the state description and user instructions, are fed into Scene-LLM to yield the corresponding response.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • We show ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `LLM, 3D visual reasoning, Vision-Language`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14]..
3. Compare against the body-reported baseline or a matched simpler baseline: Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for SQA3D, comparing it against other baseline methods..
4. Report the body metric and its denominator/aggregation: Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), and high-level planning accu- racy(HLP). The notation "(s)" ....
5. Re-run the body-reported ablation/failure condition: We conducted ablation studies by replacing visual representation and extractor with those from other methods to demonstrate the effectiveness of our 3D visual representation, the effectiveness of frame data, and the impact ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1. Introduction), p. 4 (4. Scene-LLM), p. 5 (4.1. 3D Visual Feature); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (5. Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, primary, contributions mechanism이 Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 ... 대비 Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include ...을 개선하고, Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
