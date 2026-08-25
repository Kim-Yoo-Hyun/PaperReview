"""Canonical registry taxonomy shared by import and audit tools."""

from __future__ import annotations


CATEGORY_MAP = {
    "3D Equivariance, Calibration, and Registration": "3D Geometry, Registration, and Equivariance",
    "Foundations: Equivariance and Geometry": "3D Geometry, Registration, and Equivariance",
    "3D Generative Modeling and Diffusion": "3D Generative Modeling",
    "Foundations: Diffusion and Generative Models": "Foundations: Generative Models",
    "3D Large Multimodal Models": "3D Vision-Language Understanding",
    "3D Scene Graphs and Graph Reasoning": "3D Vision-Language Understanding",
    "3D Semantic Understanding and Alignment": "3D Vision-Language Understanding",
    "3D Vision-Language Grounding": "3D Vision-Language Understanding",
    "3D Reconstruction, Geometry, and SLAM": "3D Geometry, Reconstruction, and SLAM",
    "Foundations: Monocular Geometry": "3D Geometry, Reconstruction, and SLAM",
    "Foundations: SLAM and Sensor Geometry": "3D Geometry, Reconstruction, and SLAM",
    "3D Representation Learning and Foundation Models": "3D Representation Learning",
    "Foundations: 3D Geometry and Point Clouds": "3D Representation Learning",
    "Foundations: 3D Representation Learning": "3D Representation Learning",
    "3D Scene Representations and Neural Fields": "Neural Scene Representations",
    "Foundations: 3D Scene Representations": "Neural Scene Representations",
    "Language-Embedded NeRF and Gaussian Fields": "Language-Grounded 3D Scene Representations",
    "Foundations: 3D Detection and BEV Perception": "Autonomous 3D Perception and Sensor Fusion",
    "Foundations: 3D Semantic Occupancy": "Autonomous 3D Perception and Sensor Fusion",
    "Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception": "Autonomous 3D Perception and Sensor Fusion",
    "Sensor Fusion, LiDAR, and Autonomous Driving": "Autonomous 3D Perception and Sensor Fusion",
    "Foundations: Transformer and Language Models": "Foundations: Vision and Language Models",
    "Foundations: Vision Foundation Models": "Foundations: Vision and Language Models",
    "Foundations: Vision-Language Models": "Foundations: Vision and Language Models",
    "Foundations: Robot Motion Planning and Control": "Robotics Foundations: Planning and Control",
    "Foundations: Model-Based Robot Control": "Robotics Foundations: Planning and Control",
    "Robot Motion Planning and Control": "Robotics Foundations: Planning and Control",
    "Foundations: Imitation and Inverse Reinforcement Learning": "Robotics Foundations: Robot Learning",
    "Foundations: RL and Imitation Learning": "Robotics Foundations: Robot Learning",
    "Foundations: Reinforcement Learning for Robotics": "Robotics Foundations: Robot Learning",
    "Foundations: Robot Learning and Sim-to-Real": "Robotics Foundations: Robot Learning",
    "Foundations: Contact-Rich Manipulation": "Robotics Foundations: Contact and Whole-Body Control",
    "Foundations: Whole-Body Control": "Robotics Foundations: Contact and Whole-Body Control",
    "Foundations: Legged Locomotion": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Legged Locomotion": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Legged Loco-Manipulation": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Locomotion and Whole-Body Control": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Mobile Manipulation": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Whole-Body Robot Learning": "Locomotion, Whole-Body, and Mobile Manipulation",
    "Assembly, Tools, and Deformable Object Manipulation": "Manipulation, Contact, and Dexterity",
    "Contact-Rich and Model-Based Manipulation": "Manipulation, Contact, and Dexterity",
    "Equivariance, Diffusion, and 3D Action": "Manipulation, Contact, and Dexterity",
    "Tactile and Dexterous Manipulation": "Manipulation, Contact, and Dexterity",
    "Tactile, Force, and Contact-Aware VLA": "Manipulation, Contact, and Dexterity",
    "Imitation Learning and Learning from Demonstration": "Robot Learning and Data",
    "Offline Reinforcement Learning for Robotics": "Robot Learning and Data",
    "Robot Datasets and Long-Horizon Embodied Benchmarks": "Robot Learning and Data",
    "Robot Learning and Manipulation": "Robot Learning and Data",
    "Cross-Embodiment Robot Learning and Action Representations": "Robot Learning and Data",
    "Domain-Diverse Robot Learning": "Robot Learning and Data",
    "Foundations: Vision-Language-Action and Robotics": "VLA and Generalist Robot Policies",
    "Vision-Language-Action and Robot Manipulation": "VLA and Generalist Robot Policies",
    "Long-Horizon VLA and Skill Composition": "VLA and Generalist Robot Policies",
    "Long-Horizon Task and Motion Planning with Language": "Planning and Long-Horizon Reasoning",
    "Failure Recovery and Test-Time VLA Reasoning": "World Models, Safety, and Recovery",
    "Foundations: Robot World Models": "World Models, Safety, and Recovery",
    "Robot World Models": "World Models, Safety, and Recovery",
    "Robot World Models and Policy Evaluation": "World Models, Safety, and Recovery",
    "Safe Robotics and Constrained Control": "World Models, Safety, and Recovery",
    "Safe Robotics and Perception-Based Safety Filters": "World Models, Safety, and Recovery",
    "Safe VLA, Uncertainty, and Failure Detection": "World Models, Safety, and Recovery",
    "Uncertainty-Aware Robot World Models": "World Models, Safety, and Recovery",
    "4D and Geometry-Grounded Robot World Models": "World Models, Safety, and Recovery",
    "Active 3D Perception and Articulated Object Interaction": "Robotics-Enabling 3D Perception",
    "Navigation and Embodied AI": "Embodied Navigation and Mapping",
    "Open-Vocabulary 3D Mapping": "Embodied Navigation and Mapping",
}

TAG_ALIASES = {
    "robotics": "Robotics",
    "reinforcement learning": "Reinforcement Learning",
    "imitation learning": "Imitation Learning",
    "planning": "Planning",
    "dataset": "Dataset",
    "benchmark": "Benchmark",
    "navigation": "Navigation",
    "generation": "Generation",
    "graph reasoning": "Graph Reasoning",
    "3d scene graph": "3D Scene Graph",
    "embodied ai": "Embodied AI",
}


def canonical_category(value: str) -> str:
    return CATEGORY_MAP.get(value, value)


def canonical_tags(values: list[str]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        canonical = TAG_ALIASES.get(value.casefold(), value)
        key = canonical.casefold()
        if key not in seen:
            seen.add(key)
            output.append(canonical)
    return output


def canonicalize(paper: dict) -> dict:
    paper["category"] = canonical_category(paper["category"])
    paper["tags"] = canonical_tags(paper.get("tags", []))
    return paper
