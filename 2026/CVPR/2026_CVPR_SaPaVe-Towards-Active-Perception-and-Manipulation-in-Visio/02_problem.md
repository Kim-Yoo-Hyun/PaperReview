# Problem - SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)): However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Active perception and manipulation are crucial for robots to interact with complex scenes.
- **p. 1 / Abstract - extractive PDF cue:** Existing methods struggle to unify semantic-driven perception actively with robust, viewpoint-invariant execution accordingly.
- **p. 1 / Abstract - extractive PDF cue:** To this end, we propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner.
- **p. 1 / Abstract - extractive PDF cue:** Central to our approach is a decoupling of camera and manipulation actions, contrary to shared-action-space, and learning in a bottom-up strategy: we first train semantic ...
- **p. 1 / Abstract - extractive PDF cue:** To support this, we introduce ActiveViewPose-200K, comprising † Corresponding author ‡ Project leader 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, observation, language, instruction, policy, predicts, joint, action, trajectory, Ahead | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | ensure, temporal, consistency, smooth, execution, adopt, action, chunking | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Given, observation, language, instruction, policy, predicts, joint, action, trajectory, Ahead | p. 3 (3.1. Problem Formulation), p. 4 (Model), p. 3 (3.1. Problem Formulation) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, threefold, SaPaVe, novel, end-to-end, framework, first | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (Model) |
| Objective / loss / cost | policy/action modeling objective; cue terms: objective, minimize, Mean, Squared, Error, between, predicted, camera | p. 5 (3.3. Two-Stage Training Strategy), p. 5 (3.3. Two-Stage Training Strategy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 4 (Model) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.1. Experimental Setup), p. 7 (4.3. Fixed and Dynamic Cameras Evaluation), p. 8 (4.6. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Unlike prior works that unify camera motion and manipulation into a single action space, we decouple them and propose a two-stage learning strategy for active ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** At each timestep t, the observation Ot comprises the current RGB image It ∈RH×W ×3 and optional 3D geometric information Gt (e.g., depth maps and ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (Model), p. 4 (Model), p. 5 (3.3. Two-Stage Training Strategy)): In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in a data-efficient way. • We ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 4 / Model - extractive PDF cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.
- **p. 4 / Model - extractive PDF cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** To fill this gap, we propose a large-scale, high-quality dataset, ActiveViewPose-200K, comprising 200k image-language and camera movement pairs (see Sec.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This result indicates that a fixed camera greatly limits the model's ability to explore the accessible space, leading ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 4, our model demonstrates strong generalization to previously unseen objects, indicating robust high-level semantic understanding that enables it ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Problem Formulation), p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), interface p. 3 (3.1. Problem Formulation), p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Architecture), objective p. 5 (3.3. Two-Stage Training Strategy), p. 5 (3.3. Two-Stage Training Strategy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
