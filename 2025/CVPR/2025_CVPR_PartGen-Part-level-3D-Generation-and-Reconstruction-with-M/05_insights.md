# Insights — PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these requirements, we introduce PartGen, a method to upgrade existing 3D generation pipelines from producing unstructured 3D objects to generating compositions of meaningful ...
- **p. 3 / 3. Method - extractive body cue:** This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts.
- **p. 3 / 3. Method - extractive body cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of image conditioning, we use all 140k models, and the conditioning yn comes in the form of single renders from a randomly ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Background on 3D generation), p. 5 (3.5. Training data)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, current 3D reconstruction and generation methods only model an object's visible outer surface, omitting internal details.
- **p. 3 / 3.1. Background on 3D generation - extractive body cue:** In addition to text and images, the input y can also be an existing 3D model.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.
- **p. 6 / 4.1. Part Segmentation - extractive body cue:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the ...
- **p. 7 / 4.2. Part completion and reconstruction - extractive body cue:** We then compare ˆJ to the ground-truth render J using Peak Signalto-Noise Ratio (PSNR) of the foreground pixels, Learned Perceptual Image Patch Similarity (LPIPS) [97], ...
- **p. 8 / 4.4. Applications - extractive body cue:** 6, PartGen can effectively generate 3D objects with distinct and completed parts, even in challenging cases with heavy occlusions, such as the gummy bear.
- **Boundary to test:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the seed point randomly falls in one of ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object. This view is then processed by a ... | p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation) |
| Failure/limitation | Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the seed point randomly falls in one of ... | p. 6 (4.1. Part Segmentation), p. 7 (4.2. Part completion and reconstruction) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `conditioning observation와 noisy/intermediate sample → latent/noise variable와 conditional distribution → generated sample, action chunk 또는 trajectory`.
- 이 논문의 재사용 가능한 지점은 The input to the model is a multi-view image I, and the output is a set of multi-view part masks M 1, M 2, . . . , M S corresponding to ...를 In addition to text and images, the input y can also be an existing 3D model.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 latent/noise variable와 conditional distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the seed point randomly falls in one of ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, Diffusion, Generation, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the seed point randomly falls in one of ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For all experiments, we use 100 held-out objects from the dataset described in Sec..
3. Compare against the body-reported baseline or a matched simpler baseline: We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation..
4. Report the body metric and its denominator/aggregation: We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J..
5. Re-run the body-reported ablation/failure condition: 7, a variant of our method enables effective editing of the shape and texture of parts based on textual prompts..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3. Method), p. 5 (3.5. Training data), p. 5 (3.5. Training data); the primary result is directionally consistent at p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation), p. 7 (4.1. Part Segmentation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 assess, empirically, large mechanism이 We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation. 대비 We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J.을 개선하고, Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
