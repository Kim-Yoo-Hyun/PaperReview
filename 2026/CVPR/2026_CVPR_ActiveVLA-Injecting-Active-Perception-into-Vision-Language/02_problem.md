# Problem - ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction)): However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent advances in robot manipulation have leveraged pretrained vision-language models (VLMs) and explored integrating 3D spatial signals into these models for effective action prediction, giving ...
- **p. 1 / Abstract - extractive body cue:** However, most existing approaches overlook the importance of active perception: they typically rely on static, wrist-mounted cameras that provide an end-effector-centric viewpoint.
- **p. 1 / Abstract - extractive body cue:** As a result, these models are unable to adaptively select optimal viewpoints or resolutions during task execution, which significantly limits their performance in long-horizon tasks ...
- **p. 1 / Abstract - extractive body cue:** To address these limThis CVPR paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 1 / Abstract - extractive body cue:** Except for this watermark, it is identical to the accepted version; the final published version of the proceedings is available on IEEE Xplore.
- **p. 2 / 1. Introduction - extractive body cue:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this limitation is crucial for developing embodied agents capable of adaptive and reliable interaction in complex, real-world environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | framework, equips, robots, active, perception, capabilities, enabling, adaptive, viewpoint, selection | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | However, most, current, VLA, approaches, primarily, process, visual | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: framework, equips, robots, active, perception, capabilities, enabling, adaptive, viewpoint, selection | p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, summarized, Active, Perception, Vision-Language-Action, Models, ActiveVLA, novel | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: translation, target, determined, mathbf, mathcal, hierarchical, feature, fusion | p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.2. Ablation Study), p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Addressing this limitation is crucial for developing embodied agents capable of adaptive and reliable interaction in complex, real-world environments.
- **p. 3 / 1. Introduction - extractive body cue:** Real-world robot evaluations show strong generalization and high success rates, highlighting the practical impact of active perception in long-horizon and precision-critical tasks.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 6 (3.3. 3D Action Prediction)): The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142

- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose ActiveVLA, a novel vision-language-action framework that explicitly integrates active perception into robotic manipulation.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** This global-local fusion allows the model to combine overall scene understanding with fine spatial precision, enabling accurate and safe manipulation in complex environments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | It remains robust to variations in object size, color, lighting, and texture, obtaining 72.4% on MO-SIZE and 64.4% ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. 3D Action Prediction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), interface p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. 3D Action Prediction), objective p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction).
- **Assumption/failure evidence:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, 65.6%). (p. 6, 4.1. Experimental Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
