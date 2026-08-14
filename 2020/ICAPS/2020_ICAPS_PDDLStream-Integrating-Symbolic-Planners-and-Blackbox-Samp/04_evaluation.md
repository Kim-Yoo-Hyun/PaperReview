# Evaluation — PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / ICAPS
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, task and motion planning, symbolic planning, sampling, manipulation planning
- Official paper: https://ojs.aaai.org/index.php/ICAPS/article/view/6739
- Official PDF: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593
- Code/Project: https://github.com/caelan/pddlstream
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 ICAPS 페이지는 3개 simulated robotics domain과 여러 real-world robot task 평가를 보고한다.
- Planning success, cost, sample/solver calls와 wall-clock time을 함께 확인해야 한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

Blocks 또는 kitchen TAMP 예제에서 sampler 제거·노이즈·실패율을 바꾸며 planning success와 호출 수를 측정한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
