"""Encoder measurement, action selection and signal-separation checks for the insertion task."""

import math
from typing import NamedTuple

import numpy as np


SEED = 20261119
ACTION_FOR_FAULT = {"slip": "regrasp", "fixture": "search"}


class Encoder(NamedTuple):
    quantum_mm: float
    sigma_mm: float

    @property
    def repeats(self):
        return 8 if self.sigma_mm else 1

    def measure(self, positions, stream, scene_index, repetition):
        positions = np.asarray(positions)
        if self.sigma_mm:
            rng = np.random.default_rng([SEED, stream, scene_index, repetition])
            positions = positions + rng.normal(0, self.sigma_mm, positions.shape)
        if self.quantum_mm:
            positions = self.quantum_mm * np.rint(positions / self.quantum_mm)
        return positions


ENCODERS = {
    "ideal": Encoder(0, 0), "quantized": Encoder(0.01, 0),
    "nominal": Encoder(0.01, 0.01), "coarse": Encoder(0.05, 0.05),
}


def features(positions):
    if positions.shape != (16, 2):
        raise ValueError("The selector needs the 16 pre-command x/z readings")
    displacements = positions[1:] - positions[0]
    displacements[:, 0] = np.abs(displacements[:, 0])
    windows = displacements.reshape(3, 5, 2)
    return np.median(windows, axis=1).ravel()


def fit_folds(cases, encoder):
    folds = {}
    for held_mm in sorted({abs(case["offset_mm"]) for case in cases}):
        train = [case for case in cases if abs(case["offset_mm"]) != held_mm]
        by_action = {action: [] for action in ACTION_FOR_FAULT.values()}
        for case in train:
            action = ACTION_FOR_FAULT[case["fault"]]
            for repetition in range(encoder.repeats):
                measured = encoder.measure(case["wrist_mm"], 0, case["index"], repetition)
                by_action[action].append(features(measured))
        folds[held_mm] = {
            "training_indices": [case["index"] for case in train],
            "means_mm": {a: np.mean(rows, axis=0).tolist() for a, rows in by_action.items()},
        }
    return folds


def choose_action(measured, means_mm):
    vector = features(measured)
    regrasp = np.linalg.norm(vector - means_mm["regrasp"])
    search = np.linalg.norm(vector - means_mm["search"])
    return "regrasp" if regrasp < search else "search"


def signal_separation(cases):
    """Equal-prior Gaussian discrimination upper bound with known signed offset and templates."""
    signed_pairs = {}
    for case in cases:
        signed_pairs.setdefault(case["offset_mm"], {})[case["fault"]] = np.asarray(case["wrist_mm"])
    rows = []
    for offset, pair in signed_pairs.items():
        slip, fixture = pair["slip"], pair["fixture"]
        delta = slip - fixture
        distance = float(np.linalg.norm(delta))
        digitizer = ENCODERS["quantized"]
        identical = np.array_equal(digitizer.measure(slip, 0, 0, 0), digitizer.measure(fixture, 0, 0, 0))
        rows.append({
            "offset_mm": offset, "max_difference_xz_um": (1000 * np.max(np.abs(delta), axis=0)).tolist(),
            "l2_distance_mm": distance, "quantized_traces_identical": identical,
            "ideal_accuracy_bound": {
                key: (1 + math.erf(distance / (2 * math.sqrt(2) * encoder.sigma_mm))) / 2
                for key, encoder in ENCODERS.items() if encoder.sigma_mm
            },
        })
    return rows
