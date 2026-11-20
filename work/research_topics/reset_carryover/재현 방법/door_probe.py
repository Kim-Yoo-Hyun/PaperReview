"""Check whether a public robosuite latch is still displaced after releasing it."""

import hashlib
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

import mujoco
import numpy as np


REVISION = "a071383d53568ab798eb315c0e95357911be922d"
ASSET_HASH = "411d0acbc8aa4d331da4309021ca7a5fe5c59d6c22e66408101492e99c723679"


def load_fixture(raw):
    if hashlib.sha256(raw).hexdigest() != ASSET_HASH:
        raise ValueError("Input differs from the pinned robosuite door_lock.xml")
    xml = ET.fromstring(raw)
    xml.remove(xml.find("asset"))
    for geom in xml.iter("geom"):
        geom.attrib.pop("material", None)
    # The standalone object normally inherits radians from robosuite's base.xml.
    ET.SubElement(xml, "compiler", angle="radian", inertiagrouprange="0 0", autolimits="true")
    ET.SubElement(xml, "option", timestep="0.002")
    hinge = xml.find(".//joint[@name='hinge']")
    hinge.set("frictionloss", "0.0")  # Door._load_model() passes both overrides.
    hinge.set("damping", "0.1")
    equalities = ET.SubElement(xml, "equality")
    for name in ("hinge", "latch_joint"):
        ET.SubElement(equalities, "joint", name="hold_" + name, joint1=name,
                      polycoef="0 0 0 0 0", active="false", solref="0.006 1")
    return mujoco.MjModel.from_xml_string(ET.tostring(xml, encoding="unicode"))


def probe(model, target_rad, reset, dwell_s):
    data = mujoco.MjData(model)
    hinge = model.joint("hinge").qposadr.item()
    latch = model.joint("latch_joint").qposadr.item()
    dof = model.joint("latch_joint").dofadr.item()
    site = model.site("handle").id
    data.eq_active[model.equality("hold_hinge").id] = 1
    for _ in range(round(0.4 / model.opt.timestep)):
        torque = 4 * (target_rad - data.qpos[latch]) - 0.1 * data.qvel[dof]
        data.qfrc_applied[dof] = min(1.0, max(-1.0, torque))
        mujoco.mj_step(model, data)
    attained = data.qpos[latch].item()
    data.qfrc_applied[:] = 0
    data.eq_active[model.equality("hold_latch_joint").id] = int(reset == "reference")
    mujoco.mj_step(model, data, nstep=round(dwell_s / model.opt.timestep))
    data.eq_active[:] = 0
    mujoco.mj_forward(model, data)
    if np.any(data.warning.number) or not np.all(np.isfinite(data.qpos)):
        raise RuntimeError("Invalid public fixture simulation")
    return {
        "handle_target_rad": target_rad, "reset": reset, "dwell_s": dwell_s,
        "attained_handle_rad": round(attained, 8),
        "panel_rad": round(data.qpos[hinge].item(), 8),
        "handle_rad": round(data.qpos[latch].item(), 8),
        "handle_speed_rad_s": round(data.qvel[dof].item(), 8),
        "handle_site_world_m": [round(v.item(), 8) for v in data.site_xpos[site]],
    }


if __name__ == "__main__":
    model = load_fixture(Path(__file__).with_name("door_lock.xml").read_bytes())
    rows = []
    differences = {}
    for dwell_s in (0.6, 3.0):
        for reset in ("ordinary", "reference"):
            minus, plus = [probe(model, target, reset, dwell_s) for target in (-0.6, 0.6)]
            rows.extend((minus, plus))
            differences[f"{reset}/{dwell_s}s"] = {
                "panel_angle_difference_deg": round(math.degrees(plus["panel_rad"] - minus["panel_rad"]), 6),
                "handle_angle_difference_deg": round(math.degrees(plus["handle_rad"] - minus["handle_rad"]), 6),
                "handle_site_distance_mm": round(1000 * math.dist(plus["handle_site_world_m"], minus["handle_site_world_m"]), 6),
            }
    result = {
        "evidence": "simulated_fixture_only", "revision": REVISION, "asset_sha256": ASSET_HASH,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "mujoco": mujoco.__version__,
        "degrees_of_freedom": model.nv, "pairs_of_preparations": differences, "states": rows,
    }
    print(json.dumps(result, indent=2, allow_nan=False))
