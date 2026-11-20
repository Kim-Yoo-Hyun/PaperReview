"""Render the paper-by-paper source audit from its dated evidence ledger."""

import argparse
import json
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


def final(check):
    return check.get("after", check["status"])


def check_applied(rows, papers, root):
    """Compare the dated corrections (including later evidence) with this checkout."""
    by_id = {p["paper_id"]: p for p in papers}
    errors = []
    original = later = 0
    for row in rows:
        pid = row["id"]
        paper = by_id[pid]
        follow = row.get("followup", {})

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
            if item.get("kind") != "오류":
                continue
            original += 1
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
                expect(field, paper[field], follow.get(field, {}).get("corrected", corrected))
                if field in ("year", "venue"):
                    expect("publication." + field, paper["publication"][field], paper[field])
        for field, item in follow.items():
            later += 1
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
                expect(field, paper[field], item["corrected"])
                overview = (root / paper["folder"] / "01_overview.md").read_text()
                if "- Authors: " + ", ".join(item["corrected"]) not in overview.splitlines():
                    errors.append(f"{pid} reviewed author byline missing from overview")
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
        for name, change in row.get("followup", {}).items():
            if (name not in FOLLOWUP_FIELDS or change.get("kind") not in ("오류", "보완")
                or change.get("status") not in (PASS, OPEN) or not change.get("basis")
                or not change.get("source", "").startswith("https://")
                or not {"before", "corrected"}.issubset(change)):
                raise ValueError(f"Incomplete follow-up for {row['id']} {name}")


def mark(c):
    if c["status"] == EDIT:
        return ("오" if c["kind"] == "오류" else "보") + "→" + {PASS: "✓", OPEN: "?", EDIT: "!"}[final(c)]
    return "✓" if c["status"] == PASS else "?"


def followup_report(rows):
    updated = [r for r in rows if r.get("followup")]
    if not updated:
        return []
    counts = Counter((field, v["kind"], v["status"]) for r in updated for field, v in r["followup"].items())
    faults = sum(n for (_, kind, _), n in counts.items() if kind == "오류")
    affected = sum(any(v["kind"] == "오류" for v in r["followup"].values()) for r in updated)
    checked_pdf = sum(r.get("followup", {}).get("pdf", {}).get("status") == PASS
                      and r["checks"]["link"].get("endpoints", {}).get("pdf", {}).get("state") == "access-unconfirmed"
                      for r in rows)
    lines = ["", "## 교정 재검증", "",
             f"첫 감사 뒤 {len(updated):,}편에서 {sum(counts.values())}개 필드를 재검토해 반영했다. "
             f"그중 {affected}편에서 현재 기록과 근거가 어긋난 {faults}건을 고쳤다. "
             f"앞서 접근을 확인하지 못했던 PDF 주소 {checked_pdf}건은 표제면을 확인한 판본으로 교체했다. "
             "아래 표의 단위는 논문별 필드다. "
             "같은 사실이 여러 노트·색인에 반복된 경우는 한 번만 센다. "
             "‘현재 미확인’에는 잘못된 주소를 제거한 뒤 대체 주소를 찾지 못한 경우와 배포 근거가 부족해 기존 단정을 거둔 경우가 포함된다. "
             "[이전 값·현재 값·직접 근거](../work/sources/batches/source_audit_2026_11.jsonl)", "",
             "| 필드 | 확인 오류 교정 | 근거 보완 | 현재 통과 | 현재 미확인 |",
             "|---|---:|---:|---:|---:|"]
    for field, label in FOLLOWUP_FIELDS.items():
        fixed, unconfirmed = counts[field, "오류", PASS], counts[field, "오류", OPEN]
        added, qualified = counts[field, "보완", PASS], counts[field, "보완", OPEN]
        lines.append(f"| {label} | {fixed + unconfirmed} | {added + qualified} | "
                     f"{fixed + added} | {unconfirmed + qualified} |")
    core_open = sum(r["tier_at_audit"] == "CORE" and any(
        r.get("followup", {}).get(k, {}).get("status", final(r["checks"][k])) == OPEN
        for k in ("code", "weights", "data")) for r in rows)
    next_summaries = sum(r["tier_at_audit"] == "NEXT" and final(r["checks"]["summary"]) == OPEN for r in rows)
    lines += ["", f"교정 후에도 CORE {core_open}편에는 공개 자료 세 종류 중 미확인 항목이 있다. "
              f"NEXT {next_summaries}편은 요약·기여의 원문 대조가 남았다."]
    lines += ["", "아래 배치별 오류율과 논문별 기호는 첫 감사 시점의 기록이다. "
              "해당 ID의 `followup`에 이후 판정과 변경 사유가 있다. "
              "`python3 work/scripts/render_source_audit.py --verify-corrections`로 이 판본의 교정값을 원장 및 요약과 다시 대조할 수 있다."]
    return lines


def render(rows, meta):
    validate(rows, meta)
    n = len(rows)
    errors, additions, uncertain = tally(rows, FIELDS)
    filechecks = sum(r["inspected_text"]["format"] in ("pdf", "html") for r in rows)
    pdf_checks = [r["checks"]["link"]["endpoints"]["pdf"] for r in rows
                  if "pdf" in r["checks"]["link"].get("endpoints", {})]
    pdf_opened = sum(c["state"] in ("pdf-header", "title-checked-pdf") for c in pdf_checks)
    confirmed = sum(r["existence"] == PASS for r in rows)
    count_errors = sum(c.get("kind") == "오류" for r in rows for c in r["checks"].values())
    entry = "`work/sources/batches/source_audit_2026_11.jsonl`"
    lines = [
        "# 원문 전수 감사", "",
        f"{meta['verified_on']} KST 기준으로 감사 시작 시점의 원장 {n:,}개 항목을 고정했다. "
        f"논문과 저자 기술 발표 {confirmed:,}건의 존재를 확인했다. 교정 전 한 항목 이상에서 사실 오류가 확인된 논문은 "
        f"**{errors}/{n:,}편({pct(errors,n)})**이다. 여러 필드에 걸친 오류는 총 {count_errors}건이다. "
        f"[교정 전 원장](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/{meta['baseline_commit']}/work/sources/papers.json) · "
        "[논문별 판정·교정값·원문 위치](../work/sources/batches/source_audit_2026_11.jsonl)",
        *followup_report(rows),
        "", "## 판정 기준", "",
        "- **통과**는 해당 항목의 기록과 근거가 일치한다는 뜻이다. **수정 필요**는 교정 전 판정이며, 원문과 모순되거나 오류가 입증된 기록은 ‘오류’, 누락·불완전 기록을 채우거나 근거 없는 단정을 완화한 경우는 ‘보완’으로 구분한다.",
        "- 저자 필드의 빈칸을 채우거나 `project_only`에서 구현 파일을 처음 식별한 경우는 보완으로 집계한다. `not_released`로 기록한 산출물의 실제 배포 파일을 확인한 경우는 오류다.",
        "- **존재 불확실**은 해당 필드에 필요한 근거를 확보하지 못했다는 뜻이다. 예를 들어 저자 배포 가중치의 존재를 확인하지 못한 논문도 표제면과 발표처는 각각 통과할 수 있다. 접근 제한만으로 링크 오류나 미공개를 선언하지 않았다.",
        "- **서지와 링크.** 원래 기재된 원문·프로젝트·코드 URL을 열고 제목이나 대상과 대조했다. 반복 404나 다른 논문으로의 연결은 오류로 셌다. 브라우저 확인 화면·접근 제한에서는 접근 가능한 동일 논문 판본을 찾고 원래 주소와 새 주소를 기록했다. 프리프린트 연도, 학회 개최연도, 논문집 출판연도, 저널 권호를 구분했다. 저자 순서는 해당 판본의 표제면 또는 출판사 서지를 따랐다. 학회 프로그램에 나열된 발표자 순서는 저자 순서로 사용하지 않았다.",
        f"- **PDF 링크.** 별도 PDF 주소가 등록된 {len(pdf_checks):,}편 중 {pdf_opened:,}편에서 파일 서명 또는 해당 논문의 표제면을 확인했다. 나머지 {len(pdf_checks)-pdf_opened:,}편은 링크 판정에 미확인으로 반영했다. 별도 PDF 주소가 없는 논문은 공식 원문 링크로 점검했다.",
        f"- **요약과 기여.** 공식 초록과 저자 원문을 대조했다. {filechecks:,}편은 표제를 확인한 PDF 본문 또는 HTML 본문 구획을 추가로 확보했다. PDF의 선택된 쪽이나 HTML의 일부 절을 읽은 것만으로 기여 전체를 통과시키지 않았다. 원문 문장의 위치만 복원한 경우에는 저자 자신의 연구인지, 어떤 조건의 결과인지가 확인될 때까지 미확인으로 남겼다. 직전 배치의 원문 대조를 재사용한 경우 개별 근거에 날짜와 대상을 표시했다.",
        "- **공개 여부.** 논문의 구현, 해당 버전의 모델 파일, 저자가 배포한 데이터 목록을 각각 점검했다. 비교 방법 재구현, 다른 세대의 체크포인트, 프로젝트 홈페이지는 별도로 구분했다. 부분 공개는 확인한 파일 또는 구성요소 수준에서만 통과다. 다운로드·학습·실기 재현은 이 판정에 포함되지 않는다.",
        "- **태그.** 원래 태그가 저자의 입력·방법·평가 또는 명시된 검색 주제와 연결되는지 확인했다. 남은 태그의 역할이 모호하면 미확인으로 뒀다. 아래에는 확인된 불일치만 설명한다.",
        "- **판본 이력.** 논문 노트에서 날짜가 적힌 과거 PDF 추출 기록은 그때 사용한 판본을 가리킨다. 현재 원문은 overview의 Official paper와 원장에서, 교체한 주소와 사유는 이 감사의 논문별 근거에서 확인할 수 있다.", "",
        "## 항목별 결과", "",
        "| 항목 | 교정 전 확인 오류 | 보완 | 교정 후 통과 | 교정 후 존재 불확실 |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, label in FIELDS.items():
        e, a, u = tally(rows, [key])
        passed = sum(final(r["checks"][key]) == PASS for r in rows)
        lines.append(f"| {label} | {e} | {a} | {passed} | {u} |")
    oe, oa, ou = tally(rows, ["code", "weights", "data"])
    lines += [
        f"| 공개 여부 3종 합집합(논문 수) | {oe} | {oa} | {n-ou} | {ou} |", "",
        f"같은 논문에 오류와 보완이 함께 있으면 두 열에 각각 들어간다. 논문 기준으로는 오류 {errors}편, "
        f"보완 {additions:,}편, 교정 후 전 항목 통과 {n-uncertain}편이다. 잔여 확인 오류는 "
        f"{sum(any(final(c)==EDIT for c in r['checks'].values()) for r in rows)}편이며, "
        f"하나 이상 미확인 필드가 남은 논문은 {uncertain:,}편이다.", "",
        "**[해석]** 교정 전 오류율은 이번 전수 선별에서 확인한 하한이다. 미확인 필드까지 모두 판독한 뒤의 오류율은 아직 계산할 수 없다. 전체 원장을 대상으로 한 집계여서 표본 신뢰구간을 적용하지 않는다. "
        "후속 전수 검증은 미확인 필드를 대상으로 이어갈 필요가 있다. 연구 비교에서 인용할 요약·기여의 주체와 실험 조건, 가중치·데이터의 버전과 라이선스·공개 범위를 우선한다. "
        "직전 CORE/NEXT 층화표본의 오류율은 모집단과 감사 전 상태가 달라 이번 수치와 합산하지 않는다. [50편 표본 감사](./SAMPLE_AUDIT.md)", "",
        "## 읽기 등급별 확인 범위", "",
        "| 감사 당시 등급 | 편수 | 요약·기여 통과 | 태그 통과 | 코드·가중치·데이터 모두 통과 |",
        "|---|---:|---:|---:|---:|",
    ]
    for tier in TIERS:
        group = [row["checks"] for row in rows if row["tier_at_audit"] == tier]
        complete = sum(all(final(c[key]) == PASS for key in ("code", "weights", "data")) for c in group)
        summaries = sum(final(c["summary"]) == PASS for c in group)
        tags = sum(final(c["tags"]) == PASS for c in group)
        lines.append(f"| {tier} | {len(group)} | {summaries} | {tags} | {complete} |")
    lines += [
        "", "## 배치별 결과", "",
        "| 배치 | 안정 ID | 편수 | 교정 전 오류 논문 | 확인 오류율 | 보완 논문 | 교정 후 미확인 논문 |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    batches = sorted({r["batch"] for r in rows})
    for b in batches:
        group = [r for r in rows if r["batch"] == b]
        e, a, u = tally(group, FIELDS)
        lines.append(f"| [{b}](#batch-{b:02}) | {group[0]['id']}–{group[-1]['id']} | {len(group)} | {e} | {pct(e,len(group))} | {a} | {u} |")
    lines += ["", "## 태그 불일치", "", "| ID | 제거 | 반영 | 원문에서 확인한 차이 |", "|---|---|---|---|"]
    for r in rows:
        c = r["checks"]["tags"]
        if c.get("kind") != "오류":
            continue
        removed = ", ".join(v for v in c["before"] if v not in c["corrected"])
        added = ", ".join(v for v in c["corrected"] if v not in c["before"])
        lines.append(f"| {r['id']} | {removed} | {added or '—'} | {c['basis']} [원문]({c['source']}) |")
    lines += ["", "## 논문별 판정", "",
              "**✓** 통과 · **오→✓** 사실 오류 교정 · **보→✓** 누락·근거 보완 · **?** 존재 불확실 · **오→? / 보→?** 확인된 기록을 교정하거나 보완했고 같은 항목에 미확인 사항이 남았다. "
              f"각 행은 안정 ID 순서다. {entry}의 같은 ID에서 필드별 원문 주소, 이전 값·교정값, 접근 상태, 배포 파일 또는 대조 위치를 확인할 수 있다."]
    for b in batches:
        lines += ["", f'<a id="batch-{b:02}"></a>', "", f"### 배치 {b:02}", "",
                  "| ID · 공식 표제 | " + " | ".join(FIELDS.values()) + " |",
                  "|---|" + "---:|"*len(FIELDS)]
        for r in rows:
            if r["batch"] == b:
                title = r["title"].replace("|", "&#124;").replace("\n", " ")
                lines.append(f"| [{r['id']}]({r['identity_source']}) {title} | " +
                             " | ".join(mark(r["checks"][key]) for key in FIELDS) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the dated Markdown report")
    parser.add_argument("--verify-corrections", action="store_true",
                        help="compare this audit's effective corrections with the current manifest and notes")
    args = parser.parse_args()
    meta = json.loads((ROOT / "work/sources/registry_meta.json").read_text())["source_audit"]
    rows = [json.loads(s) for s in SOURCE.read_text().splitlines()]
    if args.verify_corrections:
        papers = json.loads((ROOT / "work/sources/papers.json").read_text())
        original, later = check_applied(rows, papers, ROOT)
        print(f"Matched {original} original corrections and {later} follow-up fields")
    text = render(rows, meta)
    if args.write:
        REPORT.write_text(text)
    elif not REPORT.exists() or REPORT.read_text() != text:
        raise SystemExit("Source audit Markdown is out of date. Run with --write.")
    print(f"{len(rows)} paper records, {len(FIELDS)} checks per paper")


if __name__ == "__main__":
    main()
