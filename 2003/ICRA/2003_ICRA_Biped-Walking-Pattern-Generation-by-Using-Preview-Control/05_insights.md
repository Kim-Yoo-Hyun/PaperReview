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

- **Paper-specific interface:** The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference. (p. 4, 1 Introduction).
- **Paper-specific mechanism:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an inverse problem When we represent ... (p. 3, 1 Introduction); the relevant task/metric cue is With the given reference of ZMP pref(k), the performance index is specified as J = ∞  i=k {Qee(i)2+∆xT (i)Qx∆x(i)+R∆u2(i)}, (14) where e(i) ≡p(i)-pref(i) is servo error, Qe, R > ... (p. 4, 1 Introduction). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, locomotion, ZMP, Control`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference. (p. 4, 1 Introduction); preserve the objective/update rule: (10) We can verify that this yields the same equation to Eq. (p. 2, 1 Introduction).
2. Use the paper-reported task/data/environment cue: 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum such that the mass should ... (p. 2, 1 Introduction).
3. Compare against the reported or matched baseline: We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. (p. 4, 1 Introduction).
4. Report the body metric with its denominator and aggregation: With the given reference of ZMP pref(k), the performance index is specified as J = ∞  i=k {Qee(i)2+∆xT (i)Qx∆x(i)+R∆u2(i)}, (14) where e(i) ≡p(i)-pref(i) is servo error, Qe, R > ... (p. 4, 1 Introduction).
5. Re-run the reported ablation or stress/failure condition: We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. (p. 4, 1 Introduction); if none is reported, design one around: In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 3 (1 Introduction), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), and measure the boundary at p. 4 (1 Introduction), p. 4 (1 Introduction).

## Falsifiable research question

Under the paper's stated interface (The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action ...), does the paper-specific mechanism (In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based ...) retain the reported evaluation outcome (With the given reference of ZMP pref(k), the performance index is specified as J = ∞  i=k ...) when tested against the paper's strongest explicit boundary (In this case, the resulted ZMP (bold line) does not 1623)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (With the given reference of ZMP pref(k), the performance index is specified as J = ∞  i=k ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. (p. 2, 1 Introduction).
- **Paper-supported outcome:** ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an inverse problem When we represent ... (p. 3, 1 Introduction).
- **Strongest explicit boundary:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
