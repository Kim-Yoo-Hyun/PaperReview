"""Report the effective paper audit and look up the evidence for a stable ID."""

import argparse
import hashlib
import json
import random
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "work/sources/batches/source_audit_2026_11.jsonl"
REPORT = ROOT / "research/SOURCE_AUDIT.md"
FIELDS = {
    "link": "링크", "title": "제목", "authors": "저자", "year": "연도",
    "venue": "발표처·게재", "summary": "요약·기여", "code": "코드",
    "weights": "가중치", "data": "데이터", "tags": "태그",
}
PASS, EDIT, OPEN = "통과", "수정 필요", "존재 불확실"
TIERS = ("CORE", "NEXT", "REFERENCE", "ARCHIVE")
FOLLOWUP_FIELDS = {"primary": "대표 서지", "arxiv": "arXiv 식별자", "doi": "DOI",
                   "project": "프로젝트 주소", "code_url": "코드 주소", "pdf": "원문 PDF",
                   "title": "제목", "authors": "저자", "code": "코드", "weights": "가중치", "data": "데이터"}
TEMPLATE_CLAIM = "observation-to-action closed loop의 한 지점을 바꾼다."
PROBE = ("문구 없음", "행동 근거 확인", "적용 범위 오류", "판정 유보")


def final(check):
    return check.get("after", check["status"])


def bibliography_digest(paper, fields):
    values = {k: paper["sources"]["primary"]["url"] if k == "primary" else paper[k] for k in fields}
    return hashlib.sha256(json.dumps(values, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def current_checks(row):
    states = {field: final(check) for field, check in row["checks"].items()}
    post = row.get("postcheck", {})
    follow = {**row.get("followup", {}), **post.get("resources", {})}
    for field in ("title", "authors", "code", "weights", "data"):
        if field in follow:
            states[field] = follow[field]["status"]
    endpoints = {key: PASS if endpoint["state"] in ("opened", "pdf-header", "title-checked-pdf") else OPEN
                 for key, endpoint in row["checks"]["link"]["endpoints"].items()}
    for field in ("primary", "project", "pdf", "code_url"):
        if field in follow:
            endpoints["code" if field == "code_url" else field] = follow[field]["status"]
    if "primary" in post.get("bibliography", {}):
        endpoints["primary"] = PASS
    states["link"] = PASS if endpoints and all(s == PASS for s in endpoints.values()) else OPEN
    for field in post.get("bibliography", {}):
        if field in ("title", "authors", "year", "venue"):
            states[field] = PASS
    if qualification := post.get("qualification"):
        states[qualification["field"]] = qualification["status"]
    for field, check in post.get("edits", {}).items():
        states[field] = check["status"]
    return states


def check_applied(rows, papers, root):
    """Compare the dated corrections (including later evidence) with this checkout."""
    by_id = {p["paper_id"]: p for p in papers}
    errors = []
    original = later = 0
    for row in rows:
        pid = row["id"]
        paper = by_id[pid]
        post = row.get("postcheck", {})
        follow = {**row.get("followup", {}), **post.get("resources", {})}
        edits = post.get("edits", {})

        def expect(field, value, target):
            if value != target:
                errors.append(f"{pid} {field} differs from the reviewed correction")

        def check_source(field, target):
            source_key = {"pdf": "paper_pdf", "code_url": "code"}.get(field, field)
            actual = (paper["sources"].get(source_key) or {}).get("url")
            expect(f"sources.{source_key}", actual, target)
            if field in ("primary", "pdf"):
                key = "page" if field == "primary" else "pdf"
                expect(key, paper.get(key) or None, target)

        def check_artifact(field, target):
            key = "checkpoint" if field == "weights" else field
            expect(f"reproducibility.{key}", paper["reproducibility"][key]["status"], target)
            if field != "weights":
                expect(f"artifacts.{key}_status", paper["artifacts"][key + "_status"], target)

        for field, item in row["checks"].items():
            if item.get("kind") not in ("오류", "보완"):
                continue
            original += item["kind"] == "오류"
            corrected = item["corrected"]
            if field == "link":
                for key, value in corrected.items():
                    follow_key = "code_url" if key == "code" else key
                    check_source(key, follow.get(follow_key, {}).get("corrected", value))
            elif field == "summary":
                overview = (root / paper["folder"] / "01_overview.md").read_text()
                claims = [corrected] if isinstance(corrected, str) else [corrected["summary"], *corrected["contributions"]]
                if not all(claim in overview for claim in claims):
                    errors.append(f"{pid} reviewed summary or contribution missing from overview")
            elif field in ("code", "weights", "data"):
                check_artifact(field, follow.get(field, {}).get("corrected", corrected))
            else:
                effective = edits.get(field, follow.get(field, {})).get("corrected", corrected)
                expect(field, paper[field], effective)
                if field in ("year", "venue"):
                    expect("publication." + field, paper["publication"][field], paper[field])
        for field, item in follow.items():
            later += field in row.get("followup", {})
            if field in ("primary", "project", "pdf", "code_url"):
                check_source(field, item["corrected"])
            elif field in ("doi", "arxiv"):
                expect(field, paper["identifiers"].get(field), item["corrected"])
                if field == "arxiv":
                    check_source("preprint", item["source"])
            elif field in ("code", "weights", "data"):
                check_artifact(field, item["corrected"])
                profile = paper["reproducibility"]["checkpoint" if field == "weights" else field]
                expect(field + " evidence", profile.get("source"), item["source"])
            elif field == "title":
                expect(field, paper[field], item["corrected"])
            elif field == "authors":
                effective = edits.get(field, item)["corrected"]
                expect(field, paper[field], effective)
                overview = (root / paper["folder"] / "01_overview.md").read_text()
                if "- Authors: " + ", ".join(effective) not in overview.splitlines():
                    errors.append(f"{pid} reviewed author byline missing from overview")
        if post:
            overview = (root / paper["folder"] / "01_overview.md").read_text()
            expect("bibliographic values", bibliography_digest(paper, post["bibliography"]), post["bibliography_sha256"])
            positive = {field for field, key in (("code", "code"), ("weights", "checkpoint"), ("data", "data"))
                        if paper["reproducibility"][key]["status"] in ("released", "reported")}
            expect("release endpoint coverage", set(post.get("availability", {})), positive)
            for field, probe in post.get("availability", {}).items():
                key = "checkpoint" if field == "weights" else field
                expect(field + " release source", paper["reproducibility"][key].get("source"), probe["url"])
            if TEMPLATE_CLAIM in overview:
                errors.append(f"{pid} blanket robot-action claim reappeared")
            for axis, cue in post.get("removed_search_cues", {}).items():
                if cue in paper.get("facets", {}).get(axis, []):
                    errors.append(f"{pid} unsupported search cue reappeared: {axis}.{cue}")
            for field, item in edits.items():
                value = item["corrected"]
                if field == "summary":
                    for claim in [value["summary"], *value["contributions"]]:
                        if claim not in overview:
                            errors.append(f"{pid} reviewed summary or contribution missing from overview")
                else:
                    expect(field, paper[field], value)
                    header = "Authors" if field == "authors" else "Tags"
                    if f"- {header}: " + ", ".join(value) not in overview.splitlines():
                        errors.append(f"{pid} reviewed {field} missing from overview")
    if errors:
        raise ValueError("\n".join(errors))
    return original, later


def tally(rows, fields):
    checks = [[row["checks"][key] for key in fields] for row in rows]
    errors = sum(any(c.get("kind") == "오류" for c in group) for group in checks)
    additions = sum(any(c.get("kind") == "보완" for c in group) for group in checks)
    uncertain = sum(any(final(c) == OPEN for c in group) for group in checks)
    return errors, additions, uncertain


def pct(n, total):
    return f"{100*n/total:.2f}%"


def validate(rows, meta):
    ids = [r["id"] for r in rows]
    if not rows or len(ids) != meta["paper_count"] or ids != sorted(set(ids)):
        raise ValueError("Dated paper cohort count, order or uniqueness differs from its descriptor")
    for i, row in enumerate(rows):
        if row["batch"] != i // meta["batch_size"] + 1 or set(row["checks"]) != set(FIELDS):
            raise ValueError(f"Incomplete batch or missing fields for {row['id']}")
        if row["tier_at_audit"] not in TIERS:
            raise ValueError(f"Invalid reading tier at the time of audit for {row['id']}")
        if row["existence"] == PASS and not row["identity_source"].startswith("https://"):
            raise ValueError(f"Missing primary identity source for {row['id']}")
        for name, check in row["checks"].items():
            if check["status"] not in (PASS, EDIT, OPEN) or not check.get("source"):
                raise ValueError(f"Invalid finding for {row['id']} {name}")
            if check["status"] == EDIT and (
                check.get("kind") not in ("오류", "보완") or
                final(check) not in (PASS, OPEN, EDIT) or
                not {"before", "corrected"}.issubset(check)
            ):
                raise ValueError(f"Incomplete correction for {row['id']} {name}")
        for name, change in (*row.get("followup", {}).items(), *row.get("postcheck", {}).get("resources", {}).items()):
            if (name not in FOLLOWUP_FIELDS or change.get("kind") not in ("오류", "보완")
                or change.get("status") not in (PASS, OPEN) or not change.get("basis")
                or not change.get("source", "").startswith("https://")
                or not {"before", "corrected"}.issubset(change)):
                raise ValueError(f"Incomplete follow-up for {row['id']} {name}")


def render(rows, meta):
    validate(rows, meta)
    post = meta["postcheck"]
    n = len(rows)
    states = {r["id"]: current_checks(r) for r in rows}
    expected = set(random.Random(post["seed"]).sample(sorted(states), post["sample_size"]))
    sample = [r for r in rows if "scope_probe" in r["postcheck"]]
    if {r["id"] for r in sample} != expected:
        raise ValueError("Post-correction sample differs from the frozen sampling frame")
    for r in rows:
        evidence = r["postcheck"]
        if not set(evidence["bibliography"]) <= {"title", "authors", "year", "venue", "primary"}:
            raise ValueError(f"Unknown bibliographic check for {r['id']}")
        if any(not v.startswith("https://") for v in evidence["bibliography"].values()):
            raise ValueError(f"Missing bibliographic source for {r['id']}")
        for field, probe in evidence.get("availability", {}).items():
            if (field not in ("code", "weights", "data") or not probe["url"].startswith(("https://", "http://"))
                or probe["response"] not in ("웹페이지 응답", "파일·목록 응답", "접근 제한", "확인 유보")):
                raise ValueError(f"Invalid release endpoint for {r['id']} {field}")
        for field, change in evidence.get("edits", {}).items():
            if (field not in ("summary", "tags", "authors") or change.get("kind") not in ("오류", "보완")
                or change.get("status") not in (PASS, OPEN) or not change.get("source", "").startswith("https://")
                or not change.get("basis") or not {"before", "corrected"} <= change.keys()):
                raise ValueError(f"Invalid post-correction evidence for {r['id']} {field}")
        if probe := evidence.get("scope_probe"):
            if probe["result"] not in PROBE or not probe["basis"]:
                raise ValueError(f"Incomplete scope review for {r['id']}")
            if probe["result"] != "문구 없음" and not probe.get("source", "").startswith("https://"):
                raise ValueError(f"Missing scope source for {r['id']}")
            if probe["result"] == "적용 범위 오류" and evidence["edits"]["summary"]["kind"] != "오류":
                raise ValueError(f"Missing scope correction for {r['id']}")

    def counts(group):
        final_states = [states[r["id"]].values() for r in group]
        failed = sum(EDIT in s for s in final_states)
        passed = sum(all(value == PASS for value in s) for s in final_states)
        return passed, len(group) - failed - passed, failed

    found = Counter(k for r in rows for k, c in r["postcheck"].get("edits", {}).items() if c["kind"] == "오류")
    changed = sum(any(c["kind"] == "오류" for c in r["postcheck"].get("edits", {}).values()) for r in rows)
    probed = Counter(r["postcheck"]["scope_probe"]["result"] for r in sample)
    cleaned = sum(bool(r["postcheck"].get("template_sections")) for r in rows)
    appearances = sum(r["postcheck"].get("template_sections", 0) for r in rows)
    aligned = sum(r["postcheck"].get("aligned_batch_summary", False) for r in rows)
    cue_rows = [r for r in rows if r["postcheck"].get("removed_search_cues")]
    cue_counts = Counter(cue for r in cue_rows for cue in r["postcheck"]["removed_search_cues"].values())
    affected = sum(bool(r["postcheck"].get("removed_search_cues")) or
                   any(c["kind"] == "오류" for c in r["postcheck"].get("edits", {}).values()) for r in rows)
    biblios = Counter(k for r in rows for k in r["postcheck"]["bibliography"])
    releases = [(field, probe) for r in rows for field, probe in r["postcheck"].get("availability", {}).items()]
    released_fields = Counter(field for field, _ in releases)
    accessible = sum(probe["response"] in ("파일·목록 응답", "웹페이지 응답") for _, probe in releases)
    passed, unknown, failed = counts(rows)
    first_papers, _, _ = tally(rows, FIELDS)
    first_fields = sum(c.get("kind") == "오류" for r in rows for c in r["checks"].values())
    later = [r for r in rows if r.get("followup")]
    later_errors = sum(v["kind"] == "오류" for r in later for v in r["followup"].values())
    later_papers = sum(any(v["kind"] == "오류" for v in r["followup"].values()) for r in later)
    old_scope = sum(r["checks"]["summary"].get("scope") is not None for r in rows)
    historic = "https://github.com/Kim-Yoo-Hyun/PaperReview/blob/" + post["baseline_commit"]
    ledger = "../work/sources/batches/source_audit_2026_11.jsonl"
    lines = [
        "# 원문 감사", "",
        f"{post['verified_on']} KST 기준. 직전 교정본 {n:,}편에서 **추가 오류 {changed}편({pct(changed, n)}), {sum(found.values())}개 필드**를 확인해 고쳤다. "
        f"갱신한 원장을 다시 대조한 결과 **확인된 잔여 오류는 {failed}/{n:,}편({pct(failed, n)})**, "
        f"10개 필드에 근거가 갖춰진 논문은 **{passed}편**, 한 필드 이상 미확인인 논문은 **{unknown:,}편**이다. "
        f"[조사 시작 판본]({historic}/work/sources/papers.json) · [논문별 판정과 직접 근거]({ledger})", "",
        "## 오류율과 검증 범위", "",
        "| 측정 | 분자 / 분모 | 의미 |", "|---|---:|---|",
        f"| 직전 교정본의 추가 확인 오류 | {changed} / {n:,} ({pct(changed,n)}) | 이번 점검에서 사실 오류가 입증된 논문. 같은 논문은 한 번만 센다. |",
        f"| 이번 반영 후 확인 오류 | {failed} / {n:,} ({pct(failed,n)}) | 10개 필드의 최신 판정 중 ‘수정 필요’가 남은 논문 |",
        f"| 현재 전 항목 통과 | {passed} / {n:,} ({pct(passed,n)}) | 서지·링크, 기여·태그, 공개 자료 세 종류가 모두 통과 |",
        f"| 현재 미확인 필드 보유 | {unknown:,} / {n:,} ({pct(unknown,n)}) | 미확인은 오류로 확정하거나 통과 처리하지 않았다. |", "",
        f"논문 기록과 자동 검색 분류를 함께 보면, 이번에 오류를 고친 논문은 중복을 제외해 {affected}/{n:,}편({pct(affected,n)})이다. "
        f"자동 분류에서 잘못 붙은 검색 단서와 논문 내용 자체의 오류는 위 표에서 구별했다.", "",
        f"**[해석]** 미확인 필드에서 추가 오류가 나올 수 있어 전체의 실제 잔여 오류율은 점으로 추정할 수 없다. "
        f"기존 통과 판정을 전제로, 미확인만 해소될 때 가능한 논문 단위 범위는 {pct(failed,n)}–{pct(failed+unknown,n)}다. "
        "이는 표본 신뢰구간이 아니다. 연구 비교에 쓸 요약과 공개 자료부터 미확인 필드를 계속 대조할 필요가 있다.", "",
        "## 교정 재검증", "",
        f"- 전 {n:,}편에서 대표 URL과 논문별 서지 출처에 다시 접근했다. 독립적으로 표제를 식별한 논문은 {biblios['title']:,}편, "
        f"대표 URL 자체에서 표제를 확인한 논문은 {biblios['primary']:,}편이다. "
        f"새 서지에서 순서가 일치하는 저자열 {biblios['authors']:,}편, 해당 판본의 등록 연도 {biblios['year']:,}편, 게재 근거 {biblios['venue']:,}편을 대조했다. "
        "논문별 서지 필드·프로그램 표제·PDF 첫 쪽을 사용했다. 대소문자·구두점·공백·수식 표기를 정규화해 제목을 비교하고, "
        "저자열은 각 이름의 성·이름 표기를 정리한 뒤 순서를 비교했다. 저자 수·순서가 다르거나 프로그램과 게재본이 다르면 표제면을 확인했다.",
        f"- 원장이 공개로 기록한 코드 {released_fields['code']}건·가중치 {released_fields['weights']}건·데이터 {released_fields['data']}건의 "
        f"출처를 다시 열었다. {len(releases)}건 중 {accessible}건에서 파일·목록 또는 웹페이지가 응답했다. "
        "AgiBot World Alpha는 인증 없이 파일 주소를 열 수 없었고, 저자 배포 목록에서 같은 리비전의 파일과 이용 조건을 확인했다. "
        "응답 결과는 접근성 검사다. 구현의 완전성, 가중치 호환성, 실험 재현성은 별도 검증 대상이다. "
        "[AgiBot World Alpha 배포 정보](https://huggingface.co/api/datasets/agibot-world/AgiBotWorld-Alpha)",
        f"- 안정 ID를 정렬한 직전 원장에서 `random.Random({post['seed']}).sample(ids, {len(sample)})`로 비복원 추출했다. "
        f"교체 없이 {len(sample)}편의 overview에서 동일한 폐루프 행동 주장과 평가 범위를 점검했다. "
        f"해당 문구 없음 {probed['문구 없음']}편, 행동과 연결되는 근거 확인 {probed['행동 근거 확인']}편, "
        f"원문 범위를 벗어난 귀속 {probed['적용 범위 오류']}편, 판정 유보 {probed['판정 유보']}편이었다. "
        "이 표본은 특정 서술 오류를 찾기 위한 검사다. 표본의 발견률을 열 가지 필드의 전체 오류율로 일반화할 수 없다.",
        f"- 같은 서식이 남아 있던 **{cleaned:,}개 overview의 {appearances:,}곳**을 정리했다. "
        "원문의 출력·평가가 확인된 경우 요약과 기여를 구체화했고, 나머지 자동 발췌에는 출처 수준을 표시했다. "
        f"기존 정규화 배치에서 이미 확인한 {aligned}편은 그 요약과 기여를 overview에 연결했다. 공통 문구를 지운 일만으로 요약을 통과시키지 않았다.",
        f"- 자동 검색 분류에서 ‘reinforcement’의 일부가 ‘force’로 읽혀 {len(cue_rows)}편에 잘못된 단서가 붙었다. "
        f"힘·토크 단서 {cue_counts['force_torque']}건과 접촉 단서 {cue_counts['contact_rich']}건을 제거하고 생성 규칙을 고쳤다. "
        "독립적인 접촉 단어가 있는 논문은 해당 단서를 유지했다.",
        f"- 이번에 확인한 사실 오류는 " + ", ".join(f"{FIELDS[k]} {found[k]}건" for k in FIELDS if found[k]) + "이다. "
        "원문에서 대상으로 삼은 출력과 실험으로 보인 효과를 구분한다. 예를 들어 3DVG-Transformer는 언어가 가리키는 3D 물체를 찾고, "
        "Masked Autoencoders는 가려진 패치를 복원해 시각 표현을 학습한다. "
        "[3DVG-Transformer 게재본](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html) · "
        "[Masked Autoencoders 게재본](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html)", "",
        "## 항목별 결과", "",
        "| 항목 | 이번 재점검에서 확인한 오류 | 현재 통과 | 존재 불확실 | 수정 필요 |",
        "|---|---:|---:|---:|---:|",
    ]
    for field, label in FIELDS.items():
        c = Counter(v[field] for v in states.values())
        lines.append(f"| {label} | {found[field]} | {c[PASS]:,} | {c[OPEN]:,} | {c[EDIT]} |")
    lines += ["", "링크는 대표 원문과 기재한 부가 주소별로 판정한다. 원문만 열리더라도 다른 링크의 판정은 유지한다. "
              "잘못된 주소를 걷어낸 뒤 대체 주소가 확인되지 않은 경우에는 그 역할이 미확인이다. "
              "저자의 공개 표명이나 배포 파일로 코드·가중치·데이터를 각각 판단한다. 배포 근거를 찾지 못한 상태는 ‘존재 불확실’이다. "
              "DeXtreme은 저자판과 출판사 등록 서지의 저자 수가 달라 최종 게재본 저자열을 미확인으로 남겼다. "
              f"기존 요약 판정에는 overview 대신 검증한 정규화 배치의 요약·기여를 대상으로 명시한 {old_scope}편이 포함된다. "
              "논문별 근거의 `scope`에서 대상 텍스트를 확인할 수 있다.", "",
              "## 읽기 등급별 확인 범위", "", "| 등급 | 논문 | 전 항목 통과 | 요약·기여 미확인 | 태그 미확인 | 공개 여부 중 한 가지 이상 미확인 |",
              "|---|---:|---:|---:|---:|---:|"]
    for tier in TIERS:
        group = [r for r in rows if r["tier_at_audit"] == tier]
        ss = [states[r["id"]] for r in group]
        pending_artifacts = sum(any(v[k] == OPEN for k in ("code","weights","data")) for v in ss)
        lines.append(f"| {tier} | {len(group)} | {counts(group)[0]} | {sum(v['summary']==OPEN for v in ss)} | "
                     f"{sum(v['tags']==OPEN for v in ss)} | {pending_artifacts} |")
    lines += ["", "## 배치별 결과", "", "| 배치 | 논문별 원장 행 | 편수 | 전 항목 통과 | 미확인 | 수정 필요 |",
              "|---:|---|---:|---:|---:|---:|"]
    for b in sorted({r["batch"] for r in rows}):
        group = [r for r in rows if r["batch"] == b]
        start = 1 + (b-1) * meta["batch_size"]
        complete, pending, outstanding = counts(group)
        lines.append(f"| <a id=\"batch-{b:02}\"></a>{b} | [{group[0]['id']}–{group[-1]['id']}]({ledger}#L{start}-L{start+len(group)-1}) "
                     f"| {len(group)} | {complete} | {pending} | {outstanding} |")
    lines += ["", "## 이전 감사", "",
              f"- 11월 19일의 파일 진단은 당시 1,227편의 태그 표기, 중복 의심, 발표일 해상도를 점검했다. 비슷한 제목으로 잡힌 GR00T N1.5와 N1.6은 별도 판본으로 유지했다. "
              f"정식 발표일이 연도 단위인 항목에서 최근 6개월 비중을 확정할 수 없다. [당시 분모·검사 기준]({historic}/research/REGISTRY_AUDIT.md) · [현행 통계](./REGISTRY_STATS.md)",
              f"- 같은 날 집중 읽기 477편 중 CORE 30편·NEXT 20편의 층화표본에서는 10/50편에서 11개 오류를 고쳤다. "
              f"당시 두 등급 모집단의 가중 추정은 11.7%였다. [50편의 원문·추출법·판정]({historic}/research/SAMPLE_AUDIT.md)",
              f"- 11월 20일 첫 전수 감사의 **교정 전** 발견률은 {first_papers}/{n:,}편({pct(first_papers,n)}), {first_fields}개 필드였다. "
              f"그 뒤 {len(later)}편에서 {sum(len(r['followup']) for r in later)}개 필드의 증거를 보강하며 {later_papers}편의 오류 {later_errors}건을 교정했다. "
              f"각 시점의 오류는 같은 논문에서 겹칠 수 있다. [당시 13개 배치와 논문별 표]({historic}/research/SOURCE_AUDIT.md)", "",
              "## 논문별 조회", "",
              "한 논문의 현재 10개 판정, 최초 판정, 교정 전후 값과 원문 출처를 안정 ID로 조회한다. 전체 보고서는 같은 원장에서 생성된다.", "",
              "```bash", "python3 work/scripts/render_source_audit.py --paper pr-0027",
              "python3 work/scripts/render_source_audit.py --verify-corrections", "```"]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the dated Markdown report")
    parser.add_argument("--paper", metavar="ID", help="display the current decisions and source evidence for one paper")
    parser.add_argument("--verify-corrections", action="store_true",
                        help="compare this audit's effective corrections with the current manifest and notes")
    args = parser.parse_args()
    meta = json.loads((ROOT / "work/sources/registry_meta.json").read_text())["source_audit"]
    rows = [json.loads(s) for s in SOURCE.read_text().splitlines()]
    if args.paper:
        row = next((r for r in rows if r["id"] == args.paper), None)
        if row is None:
            parser.error(f"unknown audit ID {args.paper}")
        print(json.dumps({"current": current_checks(row), "evidence": row}, ensure_ascii=False, indent=2))
        return
    if args.verify_corrections:
        papers = json.loads((ROOT / "work/sources/papers.json").read_text())
        original, later = check_applied(rows, papers, ROOT)
        additions = sum(c.get("kind") == "보완" for r in rows for c in r["checks"].values())
        newest = sum(len(r["postcheck"].get(k, {})) for r in rows for k in ("edits", "resources"))
        print(f"Matched {original} original errors, {additions} additions, {later} follow-up fields and {newest} post-correction fields")
    text = render(rows, meta)
    if args.write:
        REPORT.write_text(text)
    elif not REPORT.exists() or REPORT.read_text() != text:
        raise SystemExit("Source audit Markdown is out of date. Run with --write.")
    print(f"{len(rows)} paper records, {len(FIELDS)} checks per paper")


if __name__ == "__main__":
    main()
