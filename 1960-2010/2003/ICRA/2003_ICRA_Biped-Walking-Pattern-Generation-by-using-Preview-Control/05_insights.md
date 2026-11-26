# Insights — Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4, 5. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

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
- **Evidence boundary (DOC-QA2):** Eq. (14)는 설계 목적식이다. Figs. 7–8의 preview-length comparison과 §3.4의 multibody mismatch 분석을 결과 근거로 사용한다. 후자의 보정 전 maximum ZMP error는 x 2.3 cm, y 1.6 cm이며 이 값은 범용 robot success rate가 아니다. (PDF pp. 4–5)
- **Failure implication:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- 현재 등급·주 트랙·태그는 [논문 개요](./01_overview.md)에서 확인한다.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 y [m] time [s] ZMP multibody ZMP ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference. (p. 4, 1 Introduction); preserve the objective/update rule: (10) We can verify that this yields the same equation to Eq. (p. 2, 1 Introduction).
2. Use the paper-reported task/data/environment cue: 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum such that the mass should ... (p. 2, 1 Introduction).
3. Compare against the reported or matched baseline: We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. (p. 4, 1 Introduction).
4. 최소 재현에서는 Eq. (14)의 weights, sampling interval, COM height와 preview period를 고정하고 reference 대비 ZMP tracking error를 x/y별로 보고한다. 설계 cost J와 empirical error를 분리하며 1.6 s/0.8 s 비교를 먼저 확인한다. (DOC-QA2, PDF pp. 4–5)
5. Re-run the reported ablation or stress/failure condition: We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. (p. 4, 1 Introduction); if none is reported, design one around: In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 3 (1 Introduction), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), and measure the boundary at p. 4 (1 Introduction), p. 4 (1 Introduction).

## Falsifiable research question

**Researcher interpretation (DOC-QA2):** 같은 reference·model·cost weights에서 preview period를 1.6 s에서 0.8 s로 줄일 때 tracking error와 stability가 어떻게 달라지는가? Figs. 7–8의 기존 현상을 재현하는 질문이며 그 자체가 새로운 contribution은 아니다. (PDF pp. 4–5)

**Reject/revise rule (Researcher interpretation; DOC-QA2):** 같은 조건에서 preview 변화와 model mismatch를 분리하지 못하거나, tracking error 개선을 낙상 방지로 과해석하면 연구 주장을 축소한다. Eq. (14) 목적식의 존재만으로 empirical improvement를 인정하지 않는다. (PDF pp. 4–5)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. (p. 2, 1 Introduction).
- **Paper-supported outcome (DOC-QA2):** 0.8 s preview는 1.6 s보다 ZMP reference tracking이 좋지 않지만 state feedback의 stability는 유지된다고 보고한다. Cart-table에서 얻은 trajectory를 HRP-2P multibody model에 적용하면 보정 전 최대 x/y ZMP mismatch 2.3/1.6 cm가 발생한다. (PDF pp. 4–5, Figs. 7–10)
- **Strongest explicit boundary:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
