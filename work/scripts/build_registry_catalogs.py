#!/usr/bin/env python3
"""Build cue-level benchmark and metric catalogs from the evaluation notes.

The catalogs are navigation aids, not replacements for paper-level evidence.
Every generated reference is explicitly marked ``cue_only`` because a token in
an evaluation note does not by itself prove that the resource was the primary
dataset, split, or reported metric.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
BENCHMARK_CATALOG = ROOT / "work" / "sources" / "benchmark_catalog.json"
METRIC_CATALOG = ROOT / "work" / "sources" / "metric_catalog.json"


BENCHMARK_VOCAB = [
    ("ScanNet", ["ScanNet"], "3D vision"),
    ("ScanNet200", ["ScanNet200"], "3D vision"),
    ("ScanRefer", ["ScanRefer"], "3D vision-language"),
    ("Nr3D", ["Nr3D"], "3D vision-language"),
    ("Sr3D", ["Sr3D"], "3D vision-language"),
    ("ReferIt3D", ["ReferIt3D"], "3D vision-language"),
    ("ScanQA", ["ScanQA"], "3D vision-language"),
    ("S3DIS", ["S3DIS"], "3D vision"),
    ("Replica", ["Replica"], "3D vision / simulation"),
    ("Matterport3D", ["Matterport3D"], "3D vision"),
    ("HM3D", ["HM3D"], "embodied navigation"),
    ("Habitat", ["Habitat"], "embodied navigation"),
    ("R2R", ["R2R"], "embodied navigation"),
    ("RxR", ["RxR"], "embodied navigation"),
    ("VLN-CE", ["VLN-CE"], "embodied navigation"),
    ("RLBench", ["RLBench"], "robot manipulation"),
    ("CALVIN", ["CALVIN"], "robot manipulation"),
    ("LIBERO", ["LIBERO"], "robot manipulation"),
    ("LIBERO-Safety", ["LIBERO-Safety"], "robot safety"),
    ("BridgeData", ["BridgeData", "BridgeData V2"], "robot data"),
    ("Open X-Embodiment", ["Open X-Embodiment", "OXE"], "robot data"),
    ("RoboMimic", ["RoboMimic"], "robot manipulation"),
    ("ManiSkill", ["ManiSkill", "ManiSkill2"], "robot manipulation / simulation"),
    ("Meta-World", ["Meta-World"], "robot manipulation / simulation"),
    ("nuScenes", ["nuScenes"], "autonomous driving"),
    ("Waymo", ["Waymo"], "autonomous driving"),
    ("KITTI", ["KITTI"], "autonomous driving"),
    ("SemanticKITTI", ["SemanticKITTI"], "autonomous driving"),
    ("RoboTwin", ["RoboTwin"], "robot manipulation"),
    ("SimplerEnv", ["SimplerEnv"], "robot manipulation / simulation"),
    ("RoboCasa", ["RoboCasa"], "robot manipulation"),
    ("FurnitureBench", ["FurnitureBench"], "robot manipulation"),
    ("HumanoidBench", ["HumanoidBench"], "humanoid control"),
    ("BEHAVIOR-1K", ["BEHAVIOR-1K"], "embodied household tasks"),
    ("VLABench", ["VLABench"], "VLA evaluation"),
    ("VLA-Arena", ["VLA-Arena"], "VLA evaluation"),
    ("DROID", ["DROID"], "robot data"),
    ("RoboNet", ["RoboNet"], "robot data"),
    ("Franka Kitchen", ["Franka Kitchen"], "robot manipulation"),
    ("TUM RGB-D", ["TUM RGB-D"], "RGB-D / SLAM"),
    ("EuRoC", ["EuRoC"], "visual-inertial odometry"),
    ("ETH3D", ["ETH3D"], "3D vision"),
    ("7-Scenes", ["7-Scenes"], "RGB-D / localization"),
    ("MegaDepth", ["MegaDepth"], "3D vision"),
    ("RealEstate10K", ["RealEstate10K"], "view synthesis"),
    ("DTU", ["DTU"], "multi-view reconstruction"),
    ("TartanAir", ["TartanAir"], "visual odometry / simulation"),
    ("SynGrasp", ["SynGrasp"], "grasping"),
    ("SocialNav-SUB", ["SocialNav-SUB"], "social navigation"),
]

METRIC_VOCAB = [
    ("Acc@0.25", ["Acc@0.25"], "higher_is_better", "accuracy"),
    ("Acc@0.5", ["Acc@0.5"], "higher_is_better", "accuracy"),
    ("mIoU", ["mIoU"], "higher_is_better", "overlap"),
    ("IoU", ["IoU"], "higher_is_better", "overlap"),
    ("AP", ["AP"], "higher_is_better", "detection"),
    ("mAP", ["mAP"], "higher_is_better", "detection"),
    ("success rate", ["success rate", "task success"], "higher_is_better", "task outcome"),
    ("SR", ["SR"], "higher_is_better", "navigation / task outcome"),
    ("SPL", ["SPL"], "higher_is_better", "navigation efficiency"),
    ("nDTW", ["nDTW"], "higher_is_better", "navigation trajectory"),
    ("RGS", ["RGS"], "higher_is_better", "instruction following"),
    ("BLEU", ["BLEU"], "higher_is_better", "language generation"),
    ("CIDEr", ["CIDEr"], "higher_is_better", "language generation"),
    ("ROUGE", ["ROUGE"], "higher_is_better", "language generation"),
    ("METEOR", ["METEOR"], "higher_is_better", "language generation"),
    ("EM", ["EM", "exact match"], "higher_is_better", "question answering"),
    ("F1", ["F1"], "higher_is_better", "classification / extraction"),
    ("PSNR", ["PSNR"], "higher_is_better", "image / view quality"),
    ("SSIM", ["SSIM"], "higher_is_better", "image / view quality"),
    ("LPIPS", ["LPIPS"], "lower_is_better", "perceptual image quality"),
    ("ATE", ["ATE"], "lower_is_better", "trajectory estimation"),
    ("RPE", ["RPE"], "lower_is_better", "trajectory estimation"),
    ("AUC", ["AUC"], "higher_is_better", "area under curve"),
    ("Chamfer", ["Chamfer", "Chamfer distance"], "lower_is_better", "geometry"),
    ("F-score", ["F-score", "F score"], "higher_is_better", "geometry / detection"),
    ("translation error", ["translation error"], "lower_is_better", "pose estimation"),
    ("rotation error", ["rotation error"], "lower_is_better", "pose estimation"),
    ("completion rate", ["completion rate"], "higher_is_better", "task outcome"),
    ("episode length", ["episode length"], "paper_specific", "efficiency / horizon"),
]


def cue_lines(text: str, aliases: list[str]) -> bool:
    for line in text.splitlines():
        lowered = line.casefold().strip()
        if lowered.startswith("#"):
            continue
        if any(marker in lowered for marker in ("not reported", "확인 필요", "confirm", "keyword cue", "metric / success signal")):
            continue
        if any(re.search(r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])", line, flags=re.IGNORECASE) for alias in aliases):
            return True
    return False


def build_catalog(papers: list[dict], vocabulary: list[tuple], kind: str) -> dict:
    entries = []
    for row in vocabulary:
        name, aliases, *metadata = row
        references = []
        for paper in papers:
            path = ROOT / paper["folder"] / "04_evaluation.md"
            if path.exists() and cue_lines(path.read_text(encoding="utf-8", errors="ignore"), aliases):
                references.append(
                    {
                        "paper_id": paper["paper_id"],
                        "source": f"{paper['folder']}/04_evaluation.md",
                        "evidence": "cue_only",
                    }
                )
        if not references:
            continue
        entry = {
            f"{kind}_id": f"{kind}:{re.sub(r'[^a-z0-9]+', '-', name.casefold()).strip('-')}",
            "name": name,
            "aliases": aliases,
            "paper_references": references,
            "reference_basis": "04_evaluation.md token cue; dataset/metric role, split, aggregation, and primary-vs-auxiliary status remain paper-specific.",
        }
        if kind == "benchmark":
            entry["family"] = metadata[0]
        else:
            entry["default_direction"] = metadata[0]
            entry["family"] = metadata[1]
        entries.append(entry)
    return {
        "schema_version": "1.0",
        "generated_on": str(date.today()),
        "catalog_type": kind,
        "evidence_policy": "Generated references are cue_only. Do not treat a token match as verified evaluation evidence; consult the paper's 04_evaluation.md and source location.",
        "entries": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the catalogs")
    args = parser.parse_args()
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    benchmarks = build_catalog(papers, BENCHMARK_VOCAB, "benchmark")
    metrics = build_catalog(papers, METRIC_VOCAB, "metric")
    print(
        {
            "mode": "apply" if args.apply else "dry-run",
            "benchmark_entries": len(benchmarks["entries"]),
            "metric_entries": len(metrics["entries"]),
            "benchmark_references": sum(len(x["paper_references"]) for x in benchmarks["entries"]),
            "metric_references": sum(len(x["paper_references"]) for x in metrics["entries"]),
        }
    )
    if not args.apply:
        return
    BENCHMARK_CATALOG.write_text(json.dumps(benchmarks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    METRIC_CATALOG.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

