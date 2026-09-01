# Insights — Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a ...
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 5 / 1 Introduction - extractive body cue:** To evaluate our method we used the physical parameters of HRP-2 prototype (HRP-2P) shown in Figure 9[22].
- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).
- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 4 / 1 Introduction - extractive body cue:** To obtain a smooth ZMP trajectory in double support, we used cubic spline.
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 1 / 1 Introduction - extractive body cue:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15].
- **p. 1 / 1 Introduction - extractive body cue:** Research on biped humanoid robots is currently one of the most exciting topics in the field of robotics and there are many ongoing projects [1, ...
- **p. 3 / 1 Introduction - extractive body cue:** On the other hand, a walking pattern generation is the inverse problem of this.
- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...
- **Boundary to test:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time of T ∗NL. By this way, we can use the ... | p. 6 (Figure/Table caption), p. 4 (1 Introduction) |
| Failure/limitation | 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ... | p. 5 (1 Introduction), p. 4 (1 Introduction) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference.를 (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs of the 3D-LIPM in the last section.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, locomotion, ZMP, Control`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an inverse problem When we represent a robot ....
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy..
5. Re-run the body-reported ablation/failure condition: 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (1 Introduction); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 4 (1 Introduction), p. 4 (1 Introduction); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, novel, walking mechanism이 a matched simpler baseline 대비 We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) ...을 개선하고, 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
