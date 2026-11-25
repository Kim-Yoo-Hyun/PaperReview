# Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Hyunwoo Ryu, Jiwoo Kim, Hyunseok An, Junwoo Chang, Joohwan Seo, Taehan Kim, Yubin Kim, Chaewon Hwang, Jongeun Choi, Roberto Horowitz
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: equivariant, Diffusion, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf
- Code/Project: https://sites.google.com/view/diffusion-edfs
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Diffusion-EDFs는 장면과 조작 대상 좌표계의 변환을 모두 반영하도록 SE(3) 위에서 조작 자세를 확산 생성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion generative modeling has become a promising approach for learning robotic manipulation tasks from stochastic human demonstrations.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present Diffusion-EDFs, a novel SE(3)-equivariant diffusion-based approach for visual robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** We show that our proposed method achieves remarkable data efficiency, requiring only 5 to 10 human demonstrations for effective end-to-end training in less than an ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, our benchmark experiments demonstrate that our approach has superior generalizability and robustness compared to state-of-the-art methods.
- **p. 1 / Abstract - extractive body cue:** Lastly, we validate our methods with real hardware experiments.
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods require numerous demonstrations and do not generalize well on novel task configurations that are not provided during training.
- **p. 1 / 2.1. SO(3) Group Representation Theory - extractive body cue:** Irreducible representations are representations that cannot be reduced anymore, and hence constitute the building blocks of any larger representation.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** This enables our method to be trained end-to-end from only 5∼10 human demonstrations without requiring any pre-training and object segmentation, yet are highly generalizable to ...
- **p. 1 / 1. Introduction - extractive body cue:** A) and locality of robotic manipulation tasks in our method design.
- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (12), we propose the following models: sν;t(g/Os, Oe) = Z R3d3x ρν;t(x/Oe) esν;t(g, x/Os, Oe) (24) sω;t(g/Os, Oe) = Z R3d3x ρω;t(x/Oe) esω;t(g, x/Os, Oe) ...
- **p. 4 / 3.5. Bi-equivariant Score Model - extractive body cue:** (28)) of the score field, we propose using the following model with two EDFs: es□;t(g, x/Os, Oe) = ψ□;t(x/Oe) ⊗(→1) □;t D(R-1) φ□;t(g x/Os) (29) ...
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** This increased receptive field enables Diffusion-EDFs to understand scene-level context.
- **p. 5 / 4.3. Score Model - extractive body cue:** We use the weighted query points model similar to Ryu et al.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** In our multiscale EDF architecture, we use smaller message passing radius for small-scale points and larger radius for large-scale points.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** [61], we model P0 to be bi-equivariant (see Supp.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Due to the bi-equivariance, the trained policy can be effectively generalized to previously unseen configurations in the observation of the scene and the grasp. representations are equivalent representations of the real Wigner ... | RGB-D/point cloud, object state와 contact/task observation | p. 2 (2.1. SO(3) Group Representation Theory), p. 3 (3.1. Problem Formulation) |
| State/latent | Due, bi-equivariance, trained, policy, effectively, generalized, previously, unseen, configurations, observation, scene, grasp | object geometry, affordance, contact mode 또는 end-effector state | p. 2 (2.1. SO(3) Group Representation Theory), p. 3 (3.1. Problem Formulation), p. 2 (2.1. SO(3) Group Representation Theory) |
| Output/action | Let the target policy distribution1 be P0(g0/Os, Oe), where g0 ∈SE(3) is the target end-effector pose, and Os and Oe are the observed point clouds of the scene and the grasped object, ... | grasp, pose, force 또는 end-effector trajectory | p. 3 (3.1. Problem Formulation), p. 2 (2.1. SO(3) Group Representation Theory), p. 5 (4. Implementation) |
| Objective/outcome | The minimizer of Jt is neither ∇log Kt nor ∇log Pt/0 but the score function of the diffused marginal ∇log Pt, that is arg min st(g/Os,Oe) Jt = s∗ t (g/Os, Oe) ... | task completion, contact success, pose/force error와 generalization | p. 4 (3.4. Score Matching Objectives), p. 4 (3.4. Score Matching Objectives), p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |

## Main Claims and Actual Contribution

- 두 좌표계에 대해 등변인 점수 함수를 학습해 회전과 병진을 포함한 파지·배치 자세를 샘플링한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf#page=4)
- 소수의 사람 시연으로 학습한 뒤 물체 자세가 바뀌는 조건에서 일반화와 실물 조작 성능을 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |
| Embodiment/environment | The mug-on-a-hanger task is similar to the one in the simulation benchmark. | hardware/simulator version and reset protocol | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |
| Dataset/benchmark | Real Hardware Experiment Pipeline 1) The scene point cloud is observed via 3D SLAM algorithm with the wrist-mounted RGB-D Camera. | role, split, size and leakage | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 7 (5. Experiments and Results) |
| Metric | While slightly better than R-NDFs, SE(3)- DiffusionFields also record low success rates, presumably due to the lack of SE(3)-equivariance. | definition, denominator, direction and uncertainty | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results) |
| Baseline/ablation | 1, Diffusion-EDFs consistently outperform both the SE(3)-equivariant baseline (R-NDFs [68]) and diffusion model baseline (SE(3)-DiffusionFields [75]) in almost all scenarios, despite not being provided with pre-training or segmented inputs. | fair input/data/compute/action matching | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Conclusion - extractive body cue:** One limitation of Diffusion-EDFs is the inability of control-level or trajectory-level inference.
- **p. 8 / 7. Conclusion - extractive body cue:** The other limitation is the necessity of the grasp observation procedure, which prevents its application to closed-loop inference.
- **p. 6 / 5. Experiments and Results - extractive body cue:** In this task, even a minor error of a centimeter can result in complete failure due to noisy observation and the small size of mug ...
- **p. 7 / 5. Experiments and Results - extractive body cue:** E.2 for more details. on object segmentation are also unable to solve this task, as they cannot differentiate between bottles that are already placed on ...
- **p. 6 / 5. Experiments and Results - extractive body cue:** In particular, the baseline models completely fail with unsegmented observations.
- **p. 7 / 5. Experiments and Results - extractive body cue:** Pick-and-place success rates in various out-of-distribution settings in simulated environment.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 1 (2.1. SO(3) Group Representation Theory), p. 2 (2.1. SO(3) Group Representation Theory), p. 4 (3.5. Bi-equivariant Score Model), p. 5 (4.3. Score Model)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these methods require numerous demonstrations and do not generalize well on novel task configurations that are not provided during training. (p. 1, 1. Introduction).
- **Actual contribution:** This enables our method to be trained end-to-end from only 5∼10 human demonstrations without requiring any pre-training and object segmentation, yet are highly generalizable to out-of-distribution object configurations. (p. 1, 1. Introduction).
- **Evaluation boundary:** On the other hand, Diffusion-EDFs maintain total success rates around 80% even in the most adversarial scenarios due to the local equivariance [37, 61] inherited from EDFs and our local ... (p. 6, 5. Experiments and Results).
- **Explicit failure boundary:** In this task, even a minor error of a centimeter can result in complete failure due to noisy observation and the small size of mug handles. (p. 6, 5. Experiments and Results).

## 원문과 공개 자료

- 코드 · 다중 해상도 SE(3) 점수 모델 구현 · diffusion_edf/multiscale_score_model.py [배포 파일](https://raw.githubusercontent.com/tomato1mule/diffusion_edf/d1ae47fa4bf6e0133c5c373b20939c603d327fc0/diffusion_edf/multiscale_score_model.py)
- 가중치 · 실물 병을 집는 실험의 에너지 모델 가중치 · checkpoints/real_bottle/Pick_EBM_250.pt [배포 파일](https://media.githubusercontent.com/media/tomato1mule/diffusion_edf/d1ae47fa4bf6e0133c5c373b20939c603d327fc0/checkpoints/real_bottle/Pick_EBM_250.pt)
- 데이터 · 병을 선반에 놓는 시연 첫 단계의 장면 점군 · demo/panda_bottle_on_shelf/data/demo_0/step_0/scene_pcd/points.pt [배포 파일](https://media.githubusercontent.com/media/tomato1mule/diffusion_edf/d1ae47fa4bf6e0133c5c373b20939c603d327fc0/demo/panda_bottle_on_shelf/data/demo_0/step_0/scene_pcd/points.pt)
