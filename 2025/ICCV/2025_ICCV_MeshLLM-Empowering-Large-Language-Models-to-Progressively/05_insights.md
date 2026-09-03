# Insights — MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of the ...
- **p. 3 / 3. Method - extractive body cue:** Next, we introduce the concept of Primitive-Mesh.
- **p. 3 / 3. Method - extractive body cue:** The set of faces F = {fj}Nf j=1 consists of Nf triangular face elements defined by three vertex indices.
- **p. 2 / 1. Introduction - extractive body cue:** This simple approach enables us to quickly construct a largescale dataset comprising 1500k+ training samples.
- **p. 4 / 3.3. Training Task Design - extractive body cue:** This task enables the LLM to predict face connectivity given vertices, thereby learning the topological relationships between vertices.
- **p. 4 / 3.2. Primitive-Mesh - extractive body cue:** Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and point clusters, thereby ...
- **p. 4 / 3.3. Training Task Design - extractive body cue:** Given a set of vertex coordinates V and its corresponding faces F, the LLM is optimized according to the following objective: max θ P(F / ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction), p. 4 (3.3. Training Task Design), p. 4 (3.2. Primitive-Mesh)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Despite pioneering the exploration of understanding and generating text-serialized mesh, LLaMA-Mesh poses new challenges to the research community: 1) Data scale limitations: As suggested by ...
- **p. 2 / 1. Introduction - extractive body cue:** However, due to the limitation of LLMs' token length, LLaMA-Mesh discards a large number of long mesh sequences, and only 31k samples are used for ...
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid development of virtual reality and robotic interaction, equipping LLMs with 3D perception and spatial reasoning capabilities has become a pressing challenge.
- **p. 1 / 1. Introduction - extractive body cue:** Against this backdrop, existing research has attempted to integrate LLMs with 3D data [11, 21, 26, 33, 69, 71].
- **p. 8 / 5. Limitation and Future Work - extractive body cue:** While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available ...
- **p. 8 / 6. Conclusions - extractive body cue:** In this paper, we propose MeshLLM, a novel approach that rethinks the paradigm of generating text-serialized meshes using Large Language Models, which addresses two key ...
- **Boundary to test:** While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available mesh data is still vastly smaller than ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of the trainable dataset by nearly 50 times, which ... | p. 2 (1. Introduction), p. 3 (3. Method) |
| Reported outcome | 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the effectiveness of our Primitive-Mesh construction strategy and training task design. | p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation) |
| Failure/limitation | While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available mesh data is still vastly smaller than ... | p. 8 (5. Limitation and Future Work), p. 8 (6. Conclusions) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Large Language Model output input mesh understanding mesh generation (1) pretrain on clustered primitive-mesh (2) pretrain on semantic primitive-mesh a muscular humanoid character with armored and horn-like structures. mesh mesh caption ...를 It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available mesh data is still vastly smaller than ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of the trainable dataset by nearly 50 times, which ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available mesh data is still vastly smaller than ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We follow dataset split configurations from previous works [8, 49], extracting 10% of the 4 subsets (chair, table, bench, lamp) from ShapeNet and 1K samples from Objaverse-XL as the test set to ....
3. Compare against the body-reported baseline or a matched simpler baseline: We further compare it with state-of-the-art methods in Fig..
4. Report the body metric and its denominator/aggregation: For the mesh understanding task, we use the BLEU-1 [51], CIDEr [63], METEOR [16], and ROUGE [40] metrics to evaluate the accuracy of the generated captions..
5. Re-run the body-reported ablation/failure condition: In particular, the constructed data sets and training pipeline are fully compatible with any existing LLM without necessitating additional complex encoder-decoder designs..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Primitive-Mesh), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation); the primary result is directionally consistent at p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 8 (4.4. Ablation Studies); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 We further compare it with state-of-the-art methods in Fig. 대비 For the mesh understanding task, we use the BLEU-1 [51], CIDEr [63], METEOR [16], and ROUGE [40] metrics ...을 개선하고, While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
