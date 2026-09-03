# Method - Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.5. Bi-equivariant Score Model), p. 4 (3.5. Bi-equivariant Score Model), p. 5 (4.3. Score Model), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)): (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) esω;t(g, x/Os, Oe) :::::::::::::::::::::::::::: Spin term + Z ...

## Method Body Digest

- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) esω;t(g, x/Os, Oe) ...
- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (28)) of the score field, we propose using the following model with two EDFs: es□;t(g, x/Os, Oe) = ψ□;t(x/Oe) ⊗(→1) □;t D(R-1) φ□;t(g x/Os) (29) ...
- **p. 5 / 4.3. Score Model - extractive body cue:** We use the weighted query points model similar to Ryu et al.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** In our multiscale EDF architecture, we use smaller message passing radius for small-scale points and larger radius for large-scale points.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** [61], we model P0 to be bi-equivariant (see Supp.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Our goal is to train a model that denoises gt, which is sampled from the diffused marginal distribution Pt(gt/Os, Oe), into a denoised sample g, ...
- **p. 4 / 3.4. Score Matching Objectives - extractive body cue:** The minimizer of Jt is neither ∇log Kt nor ∇log Pt/0 but the score function of the diffused marginal ∇log Pt, that is arg min ...
- **p. 4 / 3.4. Score Matching Objectives - extractive body cue:** (22) is a straightforward adaptation of the MSE minimizer formula [71], we still provide the derivation in Supp.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** This enables our method to be trained end-to-end from only 5∼10 human demonstrations without requiring any pre-training and object segmentation, yet are highly generalizable to ...
- **p. 1 / 1. Introduction - extractive body cue:** A) and locality of robotic manipulation tasks in our method design.
- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) esω;t(g, x/Os, Oe) ...

## Source Evidence Cues

- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) esω;t(g, x/Os, Oe) ...
- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (28)) of the score field, we propose using the following model with two EDFs: es□;t(g, x/Os, Oe) = ψ□;t(x/Oe) ⊗(→1) □;t D(R-1) φ□;t(g x/Os) (29) ...
- **p. 5 / 4.3. Score Model - extractive body cue:** We use the weighted query points model similar to Ryu et al.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** In our multiscale EDF architecture, we use smaller message passing radius for small-scale points and larger radius for large-scale points.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** [61], we model P0 to be bi-equivariant (see Supp.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Our goal is to train a model that denoises gt, which is sampled from the diffused marginal distribution Pt(gt/Os, Oe), into a denoised sample g, ...
- **Detected method headings:** 3.5. Bi-equivariant Score Model (p. 4); 4.2. Architecture of Equivariant Descriptor Fields (p. 5); 4.3. Score Model (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) ... | p. 4 (3.5. Bi-equivariant Score Model), p. 4 (3.5. Bi-equivariant Score Model) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | (28)) of the score field, we propose using the following model with two EDFs: es□;t(g, x/Os, Oe) = ψ□;t(x/Oe) ⊗(→1) □;t D(R-1) ... | p. 4 (3.5. Bi-equivariant Score Model), p. 5 (4.3. Score Model) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | We use the weighted query points model similar to Ryu et al. | p. 5 (4.3. Score Model), p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.4. Score Matching Objectives - extractive body cue:** The minimizer of Jt is neither ∇log Kt nor ∇log Pt/0 but the score function of the diffused marginal ∇log Pt, that is arg min ...
- **p. 4 / 3.4. Score Matching Objectives - extractive body cue:** (22) is a straightforward adaptation of the MSE minimizer formula [71], we still provide the derivation in Supp.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** However, the original EDFs [61] have small receptive fields due to memory constraints.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (3.4. Score Matching Objectives), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), p. 4 (3.4. Score Matching Objectives).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Due, bi-equivariance, trained, policy, effectively, generalized, previously, unseen, configurations, observation, scene, grasp, representations, equivalent | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Due, bi-equivariance, trained, policy, effectively, generalized, previously, unseen, configurations, observation | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | enables, trained, end-to-end, only, human, demonstrations, without, requiring, pre-training, object | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | minimizer, neither, Pt/0, score, function, diffused, marginal, g/Os, Although, straightforward | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2.1. SO(3) Group Representation Theory - extractive body cue:** Due to the bi-equivariance, the trained policy can be effectively generalized to previously unseen configurations in the observation of the scene and the grasp. representations ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Let the target policy distribution1 be P0(g0/Os, Oe), where g0 ∈SE(3) is the target end-effector pose, and Os and Oe are the observed point clouds ...
- **p. 2 / 2.1. SO(3) Group Representation Theory - extractive body cue:** (b) The end-effector pose is sampled from the policy by denoising with learned bi-equivariant score function.
- **p. 5 / 4. Implementation - extractive body cue:** (a) The feature extractor encodes the input point cloud into multiscale featured point clouds.
- **p. 5 / 4. Implementation - extractive body cue:** The field model outputs the time-conditioned EDF field value at the query point.
- **p. 6 / 4.3. Score Model - extractive body cue:** For the implementation of the query weight field w(x/O), we use an EDF with a single scalar (type-0) output.
- **p. 1 / 2.1. SO(3) Group Representation Theory - extractive body cue:** A representation D(g) is a map from a group G to a linear map on a vector space W that satisfies D(g)D(h) = D(gh) ∀g, ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | In this section, we first provide the specific implementation of the bi-equivariant diffusion frame selection mechanism, which was postponed in Sec. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | However, the original EDFs [61] have small receptive fields due to memory constraints. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | However, the original EDFs [61] have small receptive fields due to memory constraints. | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | It took 20∼45 minutes to train Diffusion-EDFs for single pick or place task with RTX 3090 GPU and i9-12900k CPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Our goal is to train a model that denoises gt, which is sampled from the diffused marginal distribution Pt(gt/Os, Oe), into a denoised sample g, ...
- **p. 6 / 5. Experiments and Results - extractive body cue:** It took 20∼45 minutes to train Diffusion-EDFs for single pick or place task with RTX 3090 GPU and i9-12900k CPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** following, models, g/Os, R3d3x, x/Oe, x/Os, Spin, term, Orbital, where, denotes, cross, product, wedge, score, field, model, EDFs, R-1, different.
- **Relevant PDF headings:** 3.5. Bi-equivariant Score Model (p. 4); 4.2. Architecture of Equivariant Descriptor Fields (p. 5); 4.3. Score Model (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | The mug-on-a-hanger task is similar to the one in the simulation benchmark. | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |
| Grasp / trajectory generation | 1, Diffusion-EDFs consistently outperform both the SE(3)-equivariant baseline (R-NDFs [68]) and diffusion model baseline (SE(3)-DiffusionFields [75]) in almost all scenarios, despite not ... | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |
| Contact execution / correction | Without object segmentation, R-NDFs achieve zero success rates due to the lack of locality in their method design [15, 37, 61]. | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |

## Failure and Ablation Link

- **p. 7 / 5. Experiments and Results - extractive body cue:** Scenario Method Without Pretraining Without Obj.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of Diffusion-EDFs. (a) The target end-effector pose g0 is bi-equivariantly diffused for the training of Diffusion-EDFs. (b) The end-effector pose is sampled ...
- **p. 6 / 5. Experiments and Results - extractive body cue:** We train Diffusion-EDFs in a fully end-to-end manner without using any pre-training or object segmentation.
- **p. 6 / 5. Experiments and Results - extractive body cue:** In contrast, we evaluate R-NDFs and SE(3)- Diffusion Fields for both with and without object segmentation pipelines.
- **p. 4 / 4. Implementation - extractive body cue:** In this section, we first provide the specific implementation of the bi-equivariant diffusion frame selection mechanism, which was postponed in Sec.
- **p. 5 / 4.1. Diffusion Origin Selection Mechanism - extractive body cue:** Several works have addressed the importance of incorporating such locality in equivariant methods [9, 15, 20, 37, 61].
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** The feature extractor is a deep SE(3)-equivariant GNN encoder that is run only once at the beginning of the denoising process.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.5. Bi-equivariant Score Model), p. 4 (3.5. Bi-equivariant Score Model), p. 5 (4.3. Score Model), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), objective p. 4 (3.4. Score Matching Objectives), p. 4 (3.4. Score Matching Objectives), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), temporal p. 4 (4. Implementation), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), p. 6 (5. Experiments and Results), p. 1 (2.1. SO(3) Group Representation Theory), p. 2 (2.1. SO(3) Group Representation Theory).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Due to the bi-equivariance, the trained policy can be effectively generalized to previously unseen configurations in the observation of the scene and the grasp. representations are equivalent representations of the ... (p. 2, 2.1. SO(3) Group Representation Theory).
- **Objective/update evidence:** Still, the following mean squared error (MSE) loss can be used to train our score model st(g/Os, Oe) without requiring the integration of Eq. (p. 4, 3.4. Score Matching Objectives).
- **Temporal/runtime evidence:** In this section, we first provide the specific implementation of the bi-equivariant diffusion frame selection mechanism, which was postponed in Sec. (p. 4, 4. Implementation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
