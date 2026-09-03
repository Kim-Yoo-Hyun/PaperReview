# Insights — Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3.3. Hierarchical Relation Extension - extractive body cue:** To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM.
- **p. 4 / 3.2. Generative Relation Recognition - extractive body cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive body cue:** Our method achieves comparable performance to prior models, without requiring access to various instruction prompts or additional pretraining.
- **p. 6 / Method - extractive body cue:** Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking [5, 43], to assess the effectiveness ...
- **p. 2 / 1. Introduction - extractive body cue:** The contributions can be summarized as follows, • We consider a new perspective for OV-SGG, i.e., optimizing the structure of the VLM.
- **p. 4 / 3.2. Generative Relation Recognition - extractive body cue:** As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder.
- **p. 5 / 3.4. Training Objectives - extractive body cue:** Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } ...
- **Contribution anchor:** p. 4 (3.3. Hierarchical Relation Extension), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method), p. 6 (Method), p. 2 (1. Introduction), p. 4 (3.2. Generative Relation Recognition)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Since existing pre-trained VLMs lack relation-aware knowledge [5], directly building a VLM for OV-SGG is challenging.
- **p. 2 / 1. Introduction - extractive body cue:** Unlike existing methods, this approach does not rely on a large amount of additional pre-training data or carefully set instruction prompts. • We develop a ...
- **p. 1 / 1. Introduction - extractive body cue:** (b) In this work, we consider the lack of quadratic relation-aware knowledge in VLMs, and construct an Interactive Relation Mining model for OV-SGG. tiple objects.
- **p. 1 / 1. Introduction - extractive body cue:** Though existing methods have been verified to be effective, they usually follow a closed-set assumption, i.e., the training and testing data share the same predicate ...
- **p. 8 / 5. Conclusion - extractive body cue:** This work proposes a novel vision-language interactive relation mining model for OV-SGG.
- **p. 8 / 5. Conclusion - extractive body cue:** Specifically, by introducing a generative relation recognition model, our model achieves generating open-vocabulary relation names.
- **p. 8 / 5. Conclusion - extractive body cue:** In addition, a hierarchical extension module is adopted to further extend the relations.
- **Boundary to test:** This work proposes a novel vision-language interactive relation mining model for OV-SGG.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM. | p. 4 (3.3. Hierarchical Relation Extension), p. 4 (3.2. Generative Relation Recognition) |
| Reported outcome | Figure 9. Comparison of qualitative results on VG test set. namic fitting module could alleviate the model's semantic bias towards the common predicates. By dynamically ad- justing the learning strategy for various ... | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | This work proposes a novel vision-language interactive relation mining model for OV-SGG. | p. 8 (5. Conclusion), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Moreover, recent advancements propose using an instruction prompt sequence, thus the model could more efficiently utilize the image-text pair knowledge of pre-trained VLMs or Large Language Models (LLMs) [18, 21].를 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL (e.g., BERT [12]) for text feature extraction, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This work proposes a novel vision-language interactive relation mining model for OV-SGG.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This work proposes a novel vision-language interactive relation mining model for OV-SGG.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: As for VG dataset, We considered two different settings in the PGSG [21] and OVSGTR [5]..
3. Compare against the body-reported baseline or a matched simpler baseline: Specifically, without the full supervision of novel categories, our model can provide novel relationship predictions (e.g., "from" and ‘part of')..
4. Report the body metric and its denominator/aggregation: These results demonstrate that our model has a more general relation recognition ability..
5. Re-run the body-reported ablation/failure condition: Table 7. Ablation study of pseudo labeling on VG150 test set. Relation Generation. We conduct ablation experiments to evaluate the effectiveness of the relation language gen- erator in our method. Fig. 5 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Generative Relation Recognition), p. 5 (3.4. Training Objectives), p. 3 (3.1. OV-SGG Architecture); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 mitigate, overfitting, VLM mechanism이 Specifically, without the full supervision of novel categories, our model can provide novel relationship predictions (e.g., ... 대비 These results demonstrate that our model has a more general relation recognition ability.을 개선하고, the paper's strongest untested assumption 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
