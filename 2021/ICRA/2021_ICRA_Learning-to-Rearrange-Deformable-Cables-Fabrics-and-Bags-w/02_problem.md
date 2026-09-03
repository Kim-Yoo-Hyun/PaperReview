# Problem - Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.03385; PDF retrieval source: https://arxiv.org/pdf/2012.03385. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 2 (III. BACKGROUND)): Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Rearranging and manipulating deformable objects such as cables, fabrics, and bags is a long-standing challenge in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** The complex dynamics and highdimensional configuration spaces of deformables, compared to rigid objects, make manipulation difficult not only for multistep planning, but even for goal ...
- **p. 1 / Abstract - extractive body cue:** Goals cannot be as easily specified as rigid object poses, and may involve complex relative spatial relations such as "place the item inside the bag." ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **p. 1 / Abstract - extractive body cue:** In simulation and in physical experiments, we demonstrate that goal-conditioned Transporter Networks enable agents to manipulate deformable structures into flexibly specified configurations without test-time visual ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to rigid object manipulation, deformable object manipulation presents additional challenges due to more complex configuration spaces, dynamics, and sensing.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | first, FCN, fpick, takes, input, visual, observation, outputs, dense, per-pixel | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | train, policy, assume, access, small, dataset, stochastic, expert | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: first, FCN, fpick, takes, input, visual, observation, outputs, dense, per-pixel | p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: several, tasks, benchmark, tackle, them, novel, goal-conditioned, variants | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Contact, friction, constraints, between, soft, bodies, multi, solved | p. 4 (V. SIMULATOR AND TASKS), p. 4 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (V. SIMULATOR AND TASKS), p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| Success / guarantee | completion, contact success and robustness | p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to rigid object manipulation, deformable object manipulation presents additional challenges due to more complex configuration spaces, dynamics, and sensing.
- **p. 3 / III. BACKGROUND - extractive body cue:** While this discrete-time planar action parameterization has its limitations, we find that it remains sufficiently expressive for a number of tabletop tasks involving manipulation of ...
- **p. 2 / III. BACKGROUND - extractive body cue:** We first describe the problem formulation, followed by background on Transporter Networks [68].
- **p. 2 / III. BACKGROUND - extractive body cue:** Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 3 (III. BACKGROUND), p. 4 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS)): For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and ...
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Goal-Conditioned Transporter Networks We propose two goal-conditioned architectures based on Transporter Networks.
- **p. 3 / III. BACKGROUND - extractive body cue:** To train the policy, we assume access to a small dataset of N stochastic expert demonstrations D = {ξi}N i=1, where each episode ξi of ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** [53], [54]. with rotations and translations, this enables data augmentation by randomizing a rotation and translation for each training image.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Changes from Simulation Unlike in simulation, we cannot assume "perfect" grasping of deformable objects. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 2 (III. BACKGROUND), interface p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), objective p. 4 (V. SIMULATOR AND TASKS), p. 4 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
