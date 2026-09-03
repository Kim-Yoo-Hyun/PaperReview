# Insights — Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive body cue:** The touch shape fusion module is designed with two goals.
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then inputting them together ...
- **p. 5 / 3.3. Policy Training - extractive body cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 5 / 3.3. Policy Training - extractive body cue:** At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then use a touchconditioned ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Touch Shape Fusion), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This limitation presents challenges on two fronts.
- **p. 2 / 1. Introduction - extractive body cue:** However, acquiring 3D data presents greater challenges and costs compared to 2D image and text data.
- **p. 7 / 4.3. Evaluation on Policy - extractive body cue:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison ...
- **Boundary to test:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to guide the touch location ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance. | p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance) |
| Failure/limitation | Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ... | p. 7 (4.3. Evaluation on Policy) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 The policy model receives the denoised vector as input and is trained using reinforcement learning (Section 3.2).를 In this work, we employ a simulated robotic arm guided by a trained policy model to touch the target, enabling the acquisition of tactile images to reconstruct the target through touch interaction.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to guide the touch location ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, Diffusion, Generation, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing..
3. Compare against the body-reported baseline or a matched simpler baseline: Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ....
4. Report the body metric and its denominator/aggregation: Especially on the visual-tactile 3D reconstruction task, we obtain a very low CD error, which validates the multi-modal fusion ability of our model..
5. Re-run the body-reported ablation/failure condition: Through the ablation study, we validate the necessity of each module..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training); the primary result is directionally consistent at p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, article mechanism이 Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, ... 대비 Especially on the visual-tactile 3D reconstruction task, we obtain a very low CD error, which validates the multi-modal ...을 개선하고, Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
