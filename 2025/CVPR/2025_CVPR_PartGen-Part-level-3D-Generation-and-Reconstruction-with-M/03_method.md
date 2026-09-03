# Method - PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 5 (3.5. Training data), p. 5 (3.5. Training data), p. 4 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation)): 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of image conditioning, we use all 140k models, and the conditioning yn comes in the form of single renders from a randomly ...
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** In the experiments, we follow AssetGen [73] and obtain Φ by fine-tuning a pretrained text-to-image diffusion model with an architecture similar to Emu [13], an ...
- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** The network Φseg has the same architecture as the network Φ with some changes to allow conditioning on the multi-view image I: we encode it ...
- **p. 3 / 3.1. Background on 3D generation - extractive body cue:** First, we provide essential background on multi-view diffusion models for 3D generation [36, 71, 73].
- **p. 6 / 3.5. Training data - extractive body cue:** Our algorithm produces various plausible completions across different runs.
- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** Addressing 3D object segmentation through the lens of multi-view diffusion offers several advantages.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these requirements, we introduce PartGen, a method to upgrade existing 3D generation pipelines from producing unstructured 3D objects to generating compositions of meaningful ...
- **p. 3 / 3. Method - extractive body cue:** This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of image conditioning, we use all 140k models, and the conditioning yn comes in the form of single renders from a randomly ...
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** In the experiments, we follow AssetGen [73] and obtain Φ by fine-tuning a pretrained text-to-image diffusion model with an architecture similar to Emu [13], an ...
- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** The network Φseg has the same architecture as the network Φ with some changes to allow conditioning on the multi-view image I: we encode it ...
- **p. 3 / 3.1. Background on 3D generation - extractive body cue:** First, we provide essential background on multi-view diffusion models for 3D generation [36, 71, 73].
- **p. 6 / 3.5. Training data - extractive body cue:** Our algorithm produces various plausible completions across different runs.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D ... | p. 3 (3. Method), p. 5 (3.5. Training data) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text ... | p. 5 (3.5. Training data), p. 5 (3.5. Training data) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | In the case of image conditioning, we use all 140k models, and the conditioning yn comes in the form of single renders ... | p. 5 (3.5. Training data), p. 4 (3.1. Background on 3D generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** Addressing 3D object segmentation through the lens of multi-view diffusion offers several advantages.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** The generator Φ is obtained by fine-tuning an image generation model pre-trained on Internet-scale 2D data, which is a significant advantage compared to learning a ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.5. Training data).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, model, multi-view, image, output, part, masks, corresponding, parts, addition, text, images, existing, first | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | input, model, multi-view, image, output, part, masks, corresponding, parts, addition | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | assess, empirically, large, collection, assets, produced, artists, scanned, quantitatively, qualitatively | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Addressing, object, segmentation, through, lens, multi-view, diffusion, offers, several, advantages | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** The input to the model is a multi-view image I, and the output is a set of multi-view part masks M 1, M 2, . ...
- **p. 3 / 3.1. Background on 3D generation - extractive body cue:** In addition to text and images, the input y can also be an existing 3D model.
- **p. 3 / 3.1. Background on 3D generation - extractive body cue:** In the first stage, given a prompt y, an image generator Φ outputs several 2D views of the object from different vantage points.
- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** The network Φseg has the same architecture as the network Φ with some changes to allow conditioning on the multi-view image I: we encode it ...
- **p. 5 / 3.3. Contextual part completion - extractive body cue:** We apply the pre-trained VAE separately to the masked image I ⊙M and the context image I, yielding 2 × 8 channels, and stack them ...
- **p. 6 / 3.5. Training data - extractive body cue:** The images with blue borders are the inputs.
- **p. 2 / 1. Introduction - extractive body cue:** We show that PartGen can be applied to different input modalities: starting from text, an image, or a real-world 3D scan, PartGen can generate 3D ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Second, it integrates easily with established multi-view frameworks. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.5. Training data - extractive body cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** In the experiments, we follow AssetGen [73] and obtain Φ by fine-tuning a pretrained text-to-image diffusion model with an architecture similar to Emu [13], an ...
- **p. 6 / 4.1. Part Segmentation - extractive body cue:** First, we fine-tune SAM2's mask decoder on our dataset, given the ground-truth masks and randomly selected seed points for different views.
- **p. 4 / 3.2. Multi-view part segmentation - extractive body cue:** Then, we obtain Φseg by fine-tuning Φ to: (1) take as conditioning the multi-view image I, and (2) generate the color-coded multi-view segmentation map C, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, necessary, background, multiview, diffusion, briefly, describe, PartGen, applied, text, image, model, inputs, case, conditioning, training, data, consists, pairs, multi-view.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | For all experiments, we use 100 held-out objects from the dataset described in Sec. | p. 6 (4. Experiments), p. 8 (4.4. Applications) |
| Denoiser / vector field | We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation. | p. 6 (4.1. Part Segmentation), p. 7 (4.2. Part completion and reconstruction) |
| Sampling / downstream interface | Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view ... | p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation) |

## Failure and Ablation Link

- **p. 8 / 4.4. Applications - extractive body cue:** 7, a variant of our method enables effective editing of the shape and texture of parts based on textual prompts.
- **p. 8 / 4.3. Reassembling parts - extractive body cue:** We then compare ˆL = S k Ψ( ˆJk) to the whole-object reconstruction ˆL = Ψ(I), i.e. without decomposing the object into parts, using the ...
- **p. 6 / 4.1. Part Segmentation - extractive body cue:** We fine-tune SAM2 in two different ways.
- **p. 6 / 4.1. Part Segmentation - extractive body cue:** We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation.
- **p. 7 / 4.1. Part Segmentation - extractive body cue:** As shown in the table, mAP results for our method are much higher than others, including SAM2 fine-tuned on our data.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of PartGen. Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object. ...
- **p. 6 / 4.1. Part Segmentation - extractive body cue:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 5 (3.5. Training data), p. 5 (3.5. Training data), p. 4 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation), objective p. 4 (3.2. Multi-view part segmentation), p. 4 (3.1. Background on 3D generation), temporal p. 3 (3. Method), p. 4 (3.2. Multi-view part segmentation), p. 4 (3.2. Multi-view part segmentation), p. 5 (3.4. Part reconstruction), p. 8 (5. Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
