# Problem - BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv; PDF retrieval source: https://openreview.net/pdf/26f13e74e0fd6da3fdd307ba96da6dc4438d93a3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [39, 25, 13-15] that align the observation input and action output into a unified ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning.
- **p. 1 / Abstract - extractive PDF cue:** However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce a new paradigm for constructing 3D VLAs.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we first pre-train the VLM backbone to take 2D images as input and produce 2D heatmaps as output.
- **p. 1 / Abstract - extractive PDF cue:** Using this pre-trained VLM as the backbone, we then fine-tune the entire VLA model while maintaining alignment between inputs and outputs by: (1) projecting raw ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [39, 25, 13-15] that align the observation input and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To tackle the challenges mentioned above, as inllustrated in Fig.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [39, 25, 13-15] that align the ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | heatmaps, generated, tokens, corresponding, projection, images, share, same, resolution, aligning | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | strategy, fails, take, advantage, structural, priors, previous, efficient | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: heatmaps, generated, tokens, corresponding, projection, images, share, same, resolution, aligning | p. 2 (1 Introduction), p. 10 (1) The images in the pre-training dataset are), p. 2 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, threefold, introduce, BridgeVLA, novel, VLA, model | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: ablation, replaced, convex, upsampling, module, parameters, similarly, sized | p. 10 (1) The images in the pre-training dataset are) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 10 (1) The images in the pre-training dataset are), p. 10 (1) The images in the pre-training dataset are), p. 8 (Method) |
| Success / guarantee | instruction-conditioned task success | p. 23 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** To tackle the challenges mentioned above, as inllustrated in Fig.
- **p. 1 / 1 Introduction - extractive PDF cue:** On the other hand, 3D robot policies leverage 3D structural priors in model design and demonstrate exceptional sample efficiency in learning complex 3D robot manipulation ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 9 (Method), p. 10 (1) The images in the pre-training dataset are)): In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot manipulation with a vision-language model ...

- **p. 2 / 1 Introduction - extractive PDF cue:** 1, we present BridgeVLA, a novel 3D VLA model that achieves remarkable sample efficiency and strong generalization capabilities.
- **p. 2 / 1 Introduction - extractive PDF cue:** 2D Finetune 2D Pretrain Real World Simulation BridgeVLA 2D Heatmap Image Instructions 3D Projection 3D actions [ Our framework VLM BridgeVLA ... ... "Find all ...
- **p. 9 / Method - extractive PDF cue:** Although our method outperforms baseline methods in the Category setting, its absolute success rate is not high.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | A common failure mode is that the robot often ignores the target object and moves directly to the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Due to space limitations, the details of the environment setup, baselines, and analysis can be found in Appendix ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 10 (1) The images in the pre-training dataset are), p. 2 (1 Introduction), p. 8 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 10 (1) The images in the pre-training dataset are), p. 2 (1 Introduction), p. 8 (Method), objective p. 10 (1) The images in the pre-training dataset are).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
