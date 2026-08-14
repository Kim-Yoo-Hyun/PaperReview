#!/usr/bin/env python3
"""Build the long-term robotics-first reading plan and full registry tier index."""

from __future__ import annotations

import csv
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "PAPER.md"
RESEARCH = ROOT / "research"
PLAN = RESEARCH / "READING_PLAN.md"
INDEX = RESEARCH / "READING_TIERS.csv"
STATUS = RESEARCH / "READING_STATUS.csv"
SYNTHESIS = ROOT / "synthesis"


CORE_GROUPS = OrderedDict(
    [
        (
            "Planning, control, and whole-body foundations",
            [
                "Unified Approach for Motion and Force",
                "Probabilistic Roadmaps",
                "Rapidly-Exploring Random Trees",
                "CHOMP:",
                "TrajOpt:",
                "PDDLStream:",
                "Dynamic Whole-Body Motion Generation",
                "Hierarchical Quadratic Programming",
                "Whole-Body Nonlinear Model Predictive Control",
            ],
        ),
        (
            "RL, IL, and policy learning foundations",
            [
                "A Reduction of Imitation Learning",
                "Guided Policy Search under Unknown Dynamics",
                "Generative Adversarial Imitation Learning",
                "Trust Region Policy Optimization",
                "Proximal Policy Optimization Algorithms",
                "Soft Actor-Critic",
                "Domain Randomization for Transferring",
                "What Matters in Learning from Offline Human Demonstrations",
                "Implicit Behavioral Cloning",
                "Implicit Q-Learning",
                "Decision Transformer:",
                "Denoising Diffusion Probabilistic Models",
                "Flow Matching for Generative Modeling",
                "Diffusion Policy: Visuomotor",
                "Q-Transformer",
            ],
        ),
        (
            "Manipulation, contact, tactile, and dexterity",
            [
                "Contact-Invariant Optimization",
                "GraspNet-1Billion",
                "Contact-GraspNet",
                "Factory: Fast Contact",
                "Global Planning for Contact-Rich Manipulation",
                "Tactile-Driven Non-Prehensile",
                "RoboPack",
                "DexTrack",
            ],
        ),
        (
            "VLA and generalist robot policies",
            [
                "Learning Transferable Visual Models From Natural Language Supervision",
                "CLIPort",
                "PaLM-E:",
                "RT-1:",
                "RT-2:",
                "VoxPoser",
                "Open X-Embodiment",
                "Octo: An Open",
                "OpenVLA",
                "π0: A Vision-Language-Action Flow Model",
                "π0.5",
            ],
        ),
        (
            "Safety and robot world models",
            [
                "=World Models",
                "DayDreamer",
                "TD-MPC2",
                "Control Barrier Function Based",
                "Recovery RL",
            ],
        ),
        (
            "Locomotion, mobile manipulation, and humanoid systems",
            [
                "RMA:",
                "Robust Perceptive Locomotion",
                "ANYmal Parkour",
                "HumanoidBench",
                "OmniH2O",
                "Mobile ALOHA",
            ],
        ),
        (
            "Robotics-enabling 3D perception",
            [
                "=PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation",
                "DROID-SLAM",
                "=3D Gaussian Splatting for Real-Time Radiance Field Rendering",
                "ConceptFusion",
                "RVT:",
                "DUSt3R:",
            ],
        ),
    ]
)


NEXT_GROUPS = OrderedDict(
    [
        (
            "RL, IL, offline learning, and robot data",
            [
                "Continuous Control with Deep",
                "Addressing Function Approximation Error",
                "Hindsight Experience Replay",
                "Constrained Policy Optimization",
                "Conservative Q-Learning",
                "MOPO:",
                "Minimalist Approach to Offline",
                "Learning Complex Dexterous Manipulation",
                "Learning Latent Plans from Play",
                "Relay Policy Learning",
                "RLBench:",
                "MimicGen",
                "DROID: A Large-Scale",
            ],
        ),
        (
            "Contact-rich, deformable, force, and dexterous manipulation",
            [
                "Control-Limited Differential",
                "In-Hand Manipulation via Motion Cones",
                "Towards Tight Convex Relaxations",
                "Physics-Driven Data Generation",
                "Complementarity-Free Multi-Contact",
                "SoftGym",
                "DiffSkill",
                "Neural Descriptor Fields",
                "Diffusion-EDFs",
                "IndustReal",
                "Binding Touch to Everything",
                "DenseMatcher:",
                "G3Flow:",
                "Reactive Diffusion Policy:",
                "AT-VLA",
                "ForceVLA2",
                "Dexterous World Models",
                "EquAct:",
            ],
        ),
        (
            "VLA, cross-embodiment, and long-horizon planning",
            [
                "BC-Z",
                "Perceiver-Actor",
                "VIMA:",
                "Inner Monologue",
                "SayPlan",
                "XSkill",
                "Scaling Proprioceptive-Visual Learning with Heterogeneous",
                "FAST: Efficient Action Tokenization",
                "Fine-Tuning Vision-Language-Action Models",
                "AtomicVLA",
                "PALM:",
                "ActiveVLA",
                "Spatial Memory for Out-of-Vision",
                "Counterfactual VLA",
                "Any3D-VLA",
                "MomaGraph",
            ],
        ),
        (
            "World models, uncertainty, failure detection, and recovery",
            [
                "Learning Latent Dynamics for Planning from Pixels",
                "Dream to Control",
                "Mastering Diverse Domains through World Models",
                "PIN-WM",
                "Unified World Models",
                "FlowDreamer",
                "Can We Detect Failures Without Failure Data?",
                "SAFE: Multitask",
                "WorldGym",
                "WMPO",
            ],
        ),
        (
            "Locomotion, whole-body control, mobile manipulation, and humanoids",
            [
                "DeepMimic",
                "Sim-to-Real: Learning Agile Locomotion",
                "Learning Quadrupedal Locomotion over Challenging Terrain",
                "Extreme Parkour",
                "Walk These Ways",
                "HumanPlus",
                "ASAP:",
                "LangWBC",
                "RoboPanoptes",
                "Demonstrating OK-Robot",
                "HWC-Loco",
                "VIRAL",
            ],
        ),
        (
            "Active and embodied 3D Vision",
            [
                "Where2Act",
                "FlowBot3D",
                "Ditto: Building Digital Twins",
                "VLMaps",
                "Open3DSG",
                "=VGGT: Visual Geometry Grounded Transformer",
                "SUGAR: Pre-training 3D Visual Representations for Robotics",
                "Splat-Nav",
                "EmbodiedSplat",
                "RoboSpatial:",
                "PointVLA",
            ],
        ),
    ]
)


SYNTHESIS_FILES = OrderedDict(
    [
        (
            "01_planning_control.md",
            ["Planning, control, and whole-body foundations"],
        ),
        (
            "02_rl_il_offline.md",
            [
                "RL, IL, and policy learning foundations",
                "RL, IL, offline learning, and robot data",
            ],
        ),
        (
            "03_manipulation_contact.md",
            [
                "Manipulation, contact, tactile, and dexterity",
                "Contact-rich, deformable, force, and dexterous manipulation",
            ],
        ),
        (
            "04_vla_generalist.md",
            [
                "VLA and generalist robot policies",
                "VLA, cross-embodiment, and long-horizon planning",
            ],
        ),
        (
            "05_world_models_safety.md",
            [
                "Safety and robot world models",
                "World models, uncertainty, failure detection, and recovery",
            ],
        ),
        (
            "06_locomotion_whole_body.md",
            [
                "Locomotion, mobile manipulation, and humanoid systems",
                "Locomotion, whole-body control, mobile manipulation, and humanoids",
            ],
        ),
        (
            "07_robotics_3d_perception.md",
            [
                "Robotics-enabling 3D perception",
                "Active and embodied 3D Vision",
            ],
        ),
    ]
)


ROW_RE = re.compile(
    r"^\| (?P<year>\d{4}) \| (?P<venue>[^|]+) \| "
    r"\[(?P<title>[^]]+)\]\((?P<path>\./[^)]+/01_overview\.md)\) \| "
    r"(?P<tags>[^|]+) \| (?P<pdf>[^|]+) \|"
)
REFERENCE_TAG_RE = re.compile(
    r"robot|vla|manipulation|locomotion|slam|navigation|world model|"
    r"reinforcement learning|imitation learning|whole.body|tactile|dexter",
    re.IGNORECASE,
)


def parse_registry() -> list[dict[str, str]]:
    registry_text = REGISTRY.read_text()
    rows = []
    for line in registry_text.splitlines():
        match = ROW_RE.match(line)
        if match:
            row = {key: value.strip() for key, value in match.groupdict().items()}
            rows.append(row)
    declared_match = re.search(r"Total papers with folders: (\d+)", registry_text)
    if not declared_match:
        raise RuntimeError("PAPER.md does not declare its total paper count")
    declared_total = int(declared_match.group(1))
    if len(rows) != declared_total:
        raise RuntimeError(
            f"Registry declares {declared_total} papers but contains {len(rows)} table rows"
        )
    return rows


def resolve_groups(
    rows: list[dict[str, str]], groups: OrderedDict[str, list[str]]
) -> OrderedDict[str, list[dict[str, str]]]:
    resolved = OrderedDict()
    for group, queries in groups.items():
        papers = []
        for query in queries:
            if query.startswith("="):
                hits = [row for row in rows if row["title"] == query[1:]]
            else:
                hits = [row for row in rows if query.lower() in row["title"].lower()]
            if len(hits) != 1:
                titles = [row["title"] for row in hits]
                raise RuntimeError(f"Query {query!r} resolved to {len(hits)} papers: {titles}")
            papers.append(hits[0])
        resolved[group] = papers
    return resolved


def classify(rows: list[dict[str, str]]) -> tuple[dict[str, str], dict[str, str]]:
    core_groups = resolve_groups(rows, CORE_GROUPS)
    next_groups = resolve_groups(rows, NEXT_GROUPS)
    tier_by_path: dict[str, str] = {}
    track_by_path: dict[str, str] = {}

    for tier, groups in (("CORE", core_groups), ("NEXT", next_groups)):
        for track, papers in groups.items():
            for paper in papers:
                path = paper["path"]
                if path in tier_by_path:
                    raise RuntimeError(f"Duplicate curated paper: {paper['title']}")
                tier_by_path[path] = tier
                track_by_path[path] = track

    # Preserve established REFERENCE/ARCHIVE decisions from the generated index.
    # CORE/NEXT remain explicit in the groups above; new uncategorized papers fall
    # back to the robotics/VLA relevance rule below.
    existing_tiers: dict[str, str] = {}
    if INDEX.exists():
        with INDEX.open(newline="") as file:
            for old_row in csv.DictReader(file):
                if old_row.get("tier") in {"REFERENCE", "ARCHIVE"}:
                    existing_tiers[old_row.get("overview_path", "")] = old_row["tier"]

    for row in rows:
        path = row["path"]
        if path in tier_by_path:
            continue
        existing_tier = existing_tiers.get(path)
        if existing_tier == "REFERENCE":
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Curated reference"
        elif existing_tier == "ARCHIVE":
            tier_by_path[path] = "ARCHIVE"
            track_by_path[path] = "Outside current robotics-first scope"
        elif REFERENCE_TAG_RE.search(row["tags"]):
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Robotics/VLA tag reference"
        else:
            tier_by_path[path] = "ARCHIVE"
            track_by_path[path] = "Outside current robotics-first scope"
    return tier_by_path, track_by_path


def write_index(
    rows: list[dict[str, str]], tier_by_path: dict[str, str], track_by_path: dict[str, str]
) -> None:
    order = {"CORE": 0, "NEXT": 1, "REFERENCE": 2, "ARCHIVE": 3}
    curated_rank: dict[str, int] = {}
    rank = 0
    for groups in (resolve_groups(rows, CORE_GROUPS), resolve_groups(rows, NEXT_GROUPS)):
        for papers in groups.values():
            for paper in papers:
                curated_rank[paper["path"]] = rank
                rank += 1
    sorted_rows = sorted(
        rows,
        key=lambda row: (
            order[tier_by_path[row["path"]]],
            curated_rank.get(row["path"], 10_000),
            track_by_path[row["path"]],
            int(row["year"]),
            row["title"].lower(),
        ),
    )
    with INDEX.open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(
            [
                "tier",
                "track",
                "year",
                "venue",
                "title",
                "overview_path",
                "tags",
            ]
        )
        for row in sorted_rows:
            writer.writerow(
                [
                    tier_by_path[row["path"]],
                    track_by_path[row["path"]],
                    row["year"],
                    row["venue"],
                    row["title"],
                    row["path"],
                    row["tags"],
                ]
            )


def plan_section(
    tier: str, groups: OrderedDict[str, list[dict[str, str]]]
) -> list[str]:
    total = sum(len(papers) for papers in groups.values())
    lines = [f"## {tier} — {total} papers", ""]
    for track, papers in groups.items():
        lines.extend([f"### {track} — {len(papers)}", ""])
        for index, paper in enumerate(papers, 1):
            lines.append(
                f"{index}. [{paper['title']}]({'.' + paper['path']}) "
                f"— {paper['year']} {paper['venue']}."
            )
        lines.append("")
    return lines


def write_plan(
    rows: list[dict[str, str]], tier_by_path: dict[str, str]
) -> None:
    core_groups = resolve_groups(rows, CORE_GROUPS)
    next_groups = resolve_groups(rows, NEXT_GROUPS)
    counts = {
        tier: sum(value == tier for value in tier_by_path.values())
        for tier in ("CORE", "NEXT", "REFERENCE", "ARCHIVE")
    }
    lines = [
        "# Long-Term Robotics Reading Plan",
        "",
        "- Updated: 2026-08-12 KST",
        "- Source registry: [PAPER.md](../PAPER.md)",
        "- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)",
        "- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)",
        f"- Intensive-reading set: **{counts['CORE'] + counts['NEXT']} papers** "
        f"(CORE {counts['CORE']} + NEXT {counts['NEXT']})",
        "- Research stance: Robotics is the main axis; 3D Vision is selected when it changes robot state estimation, planning, control, or evaluation.",
        "",
        "## How to Use This Plan",
        "",
        "이 문서는 별도 priority 목록과 robotics roadmap을 합친 유일한 장기 reading roadmap이다. 논문은 다음 폐루프에서 맡는 역할을 기준으로 읽는다.",
        "",
        "`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`",
        "",
        "- **Robotics:** planning, control, learning, physical interaction, deployment가 주 연구축이다.",
        "- **VLA:** language 이해 자체보다 action representation, robot data, embodiment transfer, latency, memory, feedback, safety를 본다.",
        "- **3D Vision:** 독립 benchmark보다 manipulation, navigation, SLAM, spatial memory, active perception에 주는 downstream 효과를 본다.",
        "- **Humanoid:** 별도 축으로 분리하지 않고 locomotion, whole-body control, imitation, loco-manipulation 안에서 읽는다.",
        "",
        "### Default reading budget",
        "",
        "| Research track | Share | Focus |",
        "|---|---:|---|",
        "| Robot learning and control | 25% | RL/IL/offline RL, planning, optimal control, sim-to-real |",
        "| Manipulation and physical interaction | 25% | grasping, contact, tactile/force, dexterity, deformables, assembly |",
        "| VLA, world models, safety, and long horizon | 20% | generalist policies, predictive models, uncertainty, recovery, replanning |",
        "| Locomotion, whole-body, and mobile robotics | 15% | legged/humanoid control, loco-manipulation, navigation |",
        "| Robotics-enabling 3D Vision | 15% | geometry, SLAM, active perception, semantic/spatial memory |",
        "",
        "이 비율은 registry 구성 비율이 아니라 장기 읽기·비교·재현 시간의 기본값이다. 연구 주제가 정해지면 해당 track을 50% 이상으로 높일 수 있다.",
        "",
        "## Priority Criteria",
        "",
        "위에서 아래 순서로 판단하되 PDF 보유 여부는 고려하지 않는다.",
        "",
        "1. 실제 robot task와 closed-loop action/control에 직접 연결되는가",
        "2. 해당 분야의 foundation 또는 후속 연구의 핵심 prerequisite인가",
        "3. 해결하려는 연구 공백과 기존 접근의 한계가 명확한가",
        "4. contact, partial observability, uncertainty, safety, failure recovery를 실질적으로 다루는가",
        "5. real robot 또는 설득력 있는 physics evaluation이 있는가",
        "6. 평가 protocol, metric, baseline이 명확하고 재검증 가능한가",
        "7. 구현 난이도와 데이터·코드·하드웨어 접근성이 현실적인가",
        "8. embodiment, task, object, environment generalization을 검증하는가",
        "9. 최신 trend 중 후속 연구가 이어지는 핵심 flow를 형성하는가",
        "10. 현재 연구에서 반박·재사용·확장 가능한 contribution이 있는가",
        "",
        "## Tier Definitions",
        "",
        "| Tier | Papers | Use |",
        "|---|---:|---|",
        f"| CORE | {counts['CORE']} | 공통 기반과 주력 연구축. 순서대로 정독하고 비교 노트를 남긴다. |",
        f"| NEXT | {counts['NEXT']} | CORE 이후 트랙별로 정독한다. 연구 주제에 따라 내부 순서는 바꿀 수 있다. |",
        f"| REFERENCE | {counts['REFERENCE']} | 설계·실험 중 필요한 논문만 찾아 읽는다. 완독 목표가 아니다. |",
        f"| ARCHIVE | {counts['ARCHIVE']} | 현재 robotics-first 범위 밖의 검색·역사 자료. 삭제하지 않지만 읽기 큐에서 제외한다. |",
        "",
        "CORE와 NEXT만 장기 정독 대상이다. REFERENCE와 ARCHIVE의 개별 분류는 CSV에서 검색·필터링한다.",
        "",
        "## Completion Rule",
        "",
        "논문 하나를 완료 처리하려면 overview만 읽는 것으로 끝내지 않고 다음 네 가지를 남긴다.",
        "",
        "1. 문제 설정과 기존 접근 대비 핵심 가정",
        "2. observation/state/action/control interface",
        "3. 실험의 embodiment, task, data, metric, failure mode",
        "4. 현재 연구에 재사용할 요소와 반박하거나 확장할 지점",
        "",
        "## Long-Term Reading Sequence",
        "",
        "1. **Mechanics and control:** Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream → whole-body/force control.",
        "2. **Policy learning:** DAgger/GAIL → RoboMimic/RLBench → TRPO/PPO/SAC → offline RL → DDPM/Flow Matching → Diffusion Policy and scalable robot data.",
        "3. **Physical interaction:** contact mechanics and grasping → tactile/force feedback → dexterous, deformable, tool, assembly tasks.",
        "4. **Generalist policies:** CLIP/PaLM-E/CLIPort → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA/π0 → FAST/OpenVLA-OFT/π0.5.",
        "5. **Deployment:** World Models/Dreamer → DayDreamer/TD-MPC2 → FAIL-Detect/SAFE → safety filter and recovery.",
        "6. **Embodiment specialization:** locomotion, whole-body, mobile manipulation을 선택하고 필요한 3D perception을 역으로 연결한다.",
        "7. **Active spatial intelligence:** PointNet/3DGS/DUSt3R/VGGT → SLAM/semantic mapping → articulation, active perception, 3D-aware VLA.",
        "",
        "## Dependency-Based Reading Batches",
        "",
        "각 batch는 달력 기반 일정이 아니라 prerequisite 단위다. 한 batch 전체를 끝내야 다음으로 갈 필요는 없지만, 같은 계보에서는 왼쪽 논문을 먼저 읽는다.",
        "",
        "| Batch | Core question | Required spine | Branch after the spine | Exit artifact |",
        "|---|---|---|---|---|",
        "| A. Mechanics and feasibility | 학습 이전에 robot action의 feasibility와 constraint는 어떻게 표현되는가? | Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream | HQP / Whole-Body NMPC / contact optimization | planner·controller별 state, decision variable, guarantee 표 |",
        "| B. Learning objectives and data | policy가 expert, reward, value와 logged data에서 무엇을 학습하는가? | DAgger/GPS/GAIL → TRPO/PPO/SAC → RoboMimic → IBC/IQL | CQL/MOPO/TD3+BC, RLBench, MimicGen/DROID | objective × data-support × interaction 비교 표 |",
        "| C. Generative action policies | multimodal continuous action을 어떤 생성 과정으로 나타내는가? | DDPM / Flow Matching → Diffusion Policy → π0 | Diffusion-EDFs, Reactive Diffusion Policy, FAST | sampling step·chunk·latency·feedback 비교 표 |",
        "| D. Generalist VLA and scaling | semantic prior와 heterogeneous robot data가 action으로 어떻게 연결되는가? | CLIP/CLIPort/PaLM-E → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA | OpenVLA-OFT, π0/π0.5, memory/planning VLA | data × embodiment × action interface 비교 표 |",
        "| E. Contact, safety, and recovery | 접촉 변화와 실패를 얼마나 빨리 감지하고 수정하는가? | contact/grasp foundations → tactile dynamics/control → CBF/Recovery RL → FAIL-Detect/SAFE | ForceVLA2, WorldGym/WMPO | perturbation·force·intervention·recovery protocol |",
        "| F. Embodiment specialization | 동일 학습 원리가 legged, humanoid와 mobile manipulation에서 무엇이 달라지는가? | RMA → perceptive locomotion/parkour → HumanoidBench/OmniH2O/Mobile ALOHA | LangWBC, ASAP, HWC-Loco, VIRAL | dynamics/contact/whole-body coupling 비교 표 |",
        "| G. Action-relevant 3D | 더 좋은 geometry가 실제 robot decision을 언제 개선하는가? | PointNet → DROID-SLAM/3DGS → ConceptFusion/RVT/DUSt3R | VGGT/SUGAR, active 3D, PointVLA/Any3D-VLA | representation 고정 ablation과 downstream metric |",
        "",
        "Batch exit artifact를 채우기 전에는 해당 계보를 `SYNTHESIZED`로 올리지 않는다. 세부 paper sequence는 아래 CORE/NEXT 목록의 순서를 따른다.",
        "",
        "## Research Lenses Across Tracks",
        "",
        "- Robot learning을 behavior cloning으로 한정하지 않고 offline-to-online improvement, reward/value learning, failure/suboptimal data 활용까지 본다.",
        "- Contact를 예외가 아니라 state, dynamics, constraint, feedback signal로 다룬다.",
        "- Locomotion과 manipulation의 결합, balance와 task interaction의 공동 제어를 본다.",
        "- Safety를 constraint, uncertainty, monitoring, intervention, recovery의 여러 시간 척도로 나눈다.",
        "- Geometry가 learned policy 안에서 equivariance, 3D state, spatial memory, collision/contact structure로 어떤 역할을 하는지 본다.",
        "- Architecture보다 data coverage, quality, curation, embodiment diversity와 scaling law를 함께 비교한다.",
        "- Generative action model의 inference latency와 실제 closed-loop control frequency를 확인한다.",
        "- Tabletop success rate를 넘어 long horizon, real-world disturbances, sensor degradation, compromised contact, recovery를 평가한다.",
        "",
    ]
    lines.extend(plan_section("CORE", core_groups))
    lines.extend(plan_section("NEXT", next_groups))
    lines.extend(
        [
            "## REFERENCE — On-Demand Reading",
            "",
            "CORE/NEXT에는 포함되지 않지만 중요한 foundation, baseline, representation, dataset, benchmark 또는 Robotics/VLA 관련 논문이다. 연구 설계 중 필요할 때 찾아 읽으며 완독 목표로 삼지 않는다.",
            "",
            "## ARCHIVE — Search Only",
            "",
            "현재 robotics-first 방향과 직접 연결되지 않는 논문이다. 향후 연구축이 바뀌거나 특정 3D/VLM 배경이 필요할 때 다시 승격할 수 있으며, 레지스트리와 로컬 노트는 그대로 보존한다.",
            "",
        ]
    )
    PLAN.write_text("\n".join(lines))


def write_status(
    rows: list[dict[str, str]], tier_by_path: dict[str, str], track_by_path: dict[str, str]
) -> None:
    """Create/update the intensive-reading tracker while preserving user-entered fields."""
    fieldnames = [
        "tier",
        "track",
        "sequence",
        "status",
        "evidence_level",
        "year",
        "venue",
        "title",
        "overview_path",
        "started_on",
        "completed_on",
        "problem_and_assumptions",
        "observation_state_action_control",
        "embodiment_task_data_metrics",
        "failure_modes",
        "research_relevance",
        "next_action",
        "personal_notes",
    ]
    preserved: dict[str, dict[str, str]] = {}
    if STATUS.exists():
        with STATUS.open(newline="") as file:
            for old_row in csv.DictReader(file):
                preserved[old_row.get("overview_path", "")] = old_row

    curated = [
        row for row in rows if tier_by_path[row["path"]] in {"CORE", "NEXT"}
    ]
    tier_order = {"CORE": 0, "NEXT": 1}
    track_order = {
        track: index
        for index, track in enumerate([*CORE_GROUPS.keys(), *NEXT_GROUPS.keys()])
    }
    curated_rank: dict[str, int] = {}
    rank = 0
    for groups in (resolve_groups(rows, CORE_GROUPS), resolve_groups(rows, NEXT_GROUPS)):
        for papers in groups.values():
            for paper in papers:
                curated_rank[paper["path"]] = rank
                rank += 1
    curated.sort(
        key=lambda row: (
            tier_order[tier_by_path[row["path"]]],
            track_order[track_by_path[row["path"]]],
            curated_rank[row["path"]],
        )
    )

    sequence_by_tier = {"CORE": 0, "NEXT": 0}
    output_rows = []
    for row in curated:
        path = row["path"]
        tier = tier_by_path[path]
        sequence_by_tier[tier] += 1
        old = preserved.get(path, {})
        output = {field: old.get(field, "") for field in fieldnames}
        output.update(
            {
                "tier": tier,
                "track": track_by_path[path],
                "sequence": str(sequence_by_tier[tier]),
                "status": old.get("status") or "UNREAD",
                "evidence_level": old.get("evidence_level") or "CURATION_ONLY",
                "year": row["year"],
                "venue": row["venue"],
                "title": row["title"],
                "overview_path": path,
            }
        )
        output_rows.append(output)

    with STATUS.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)


def write_synthesis_queues() -> None:
    """Refresh generated paper queues without touching hand-written synthesis."""
    with STATUS.open(newline="") as file:
        status_rows = list(csv.DictReader(file))
    rows_by_track: dict[str, list[dict[str, str]]] = {}
    for row in status_rows:
        rows_by_track.setdefault(row["track"], []).append(row)

    start_marker = "<!-- READING_QUEUE:START -->"
    end_marker = "<!-- READING_QUEUE:END -->"
    for filename, tracks in SYNTHESIS_FILES.items():
        document = SYNTHESIS / filename
        text = document.read_text()
        if start_marker not in text or end_marker not in text:
            raise RuntimeError(f"Missing generated queue markers in {document}")
        queue = [start_marker, "", "## Assigned Reading Queue", ""]
        for track in tracks:
            papers = rows_by_track.get(track, [])
            queue.extend(
                [
                    f"### {track} — {len(papers)}",
                    "",
                    "| Tier | Paper | Year / Venue | Status | Evidence |",
                    "|---|---|---|---|---|",
                ]
            )
            for paper in papers:
                relative_path = "." + paper["overview_path"]
                queue.append(
                    f"| {paper['tier']} | [{paper['title']}]({relative_path}) | "
                    f"{paper['year']} / {paper['venue']} | `{paper['status']}` | `{paper['evidence_level']}` |"
                )
            queue.append("")
        queue.append(end_marker)
        prefix, remainder = text.split(start_marker, 1)
        _, suffix = remainder.split(end_marker, 1)
        document.write_text(prefix + "\n".join(queue) + suffix)


def main() -> None:
    rows = parse_registry()
    tier_by_path, track_by_path = classify(rows)
    write_status(rows, tier_by_path, track_by_path)
    write_index(rows, tier_by_path, track_by_path)
    write_plan(rows, tier_by_path)
    write_synthesis_queues()
    counts = {
        tier: sum(value == tier for value in tier_by_path.values())
        for tier in ("CORE", "NEXT", "REFERENCE", "ARCHIVE")
    }
    print(counts)


if __name__ == "__main__":
    main()
