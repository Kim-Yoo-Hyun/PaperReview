# Insights — SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=U5nRMOs8Ed; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167962. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method is light and SE(3) equivariant across multiple objects, allowing it to perform more complicated tasks with less engineering.
- **p. 4 / 4.1. Method Overview - extractive body cue:** Additionally, we propose bi-manual relative action representation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 4 / 4.1. Method Overview - extractive body cue:** We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature enc(S) ...
- **p. 5 / 4.4. Spherical FiLM Conditioning Layer - extractive body cue:** We propose equivariant spherical FiLM (SFiLM) layers to extend the Feature-wise Linear Modulation (FiLM) layer (Perez et al., 2018) used by Diffuser (Janner et al., ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements ...
- **p. 2 / 1. Introduction - extractive body cue:** The equivariance constraints lead to provable SE(3) generalization to transformed scenes.
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, such as these in the Push Eraser ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by the encoder enc. Then, SDTU ϵθ estimates ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising step ...
- **Boundary to test:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book task.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling generalization to unseen scenes, 2. a novel ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines. | p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption) |
| Failure/limitation | One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book task. | p. 9 (6. Conclusion and Limitations), p. 9 (6. Conclusion and Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In this section, we propose a spherical representation of the state and action for the policy.를 The Spherical Diffusion Policy model maps observations to actions π(S) = A.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book task.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling generalization to unseen scenes, 2. a novel ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, Diffusion, Imitation Learning, equivariant`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book task.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly placing objects on the tabletop while keeping the robot base ....
3. Compare against the body-reported baseline or a matched simpler baseline: Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 tasks, except for Coffee and Coffee Preparation..
4. Report the body metric and its denominator/aggregation: We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds..
5. Re-run the body-reported ablation/failure condition: 3) EquiBot (Yang et al., 2024a) - an SO(3)-equivariant diffusion policy with up to degree l = 1 representations..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal), p. 5 (4.4. Spherical FiLM Conditioning Layer); the primary result is directionally consistent at p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 6 (5.1. Simulation Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, novel, Spherical mechanism이 Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 ... 대비 We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the ...을 개선하고, One limitation of the proposed method is that it operates in position control, ignoring contact forces, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
