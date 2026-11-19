"""Regenerate the documentation-only scene and preview using Python 3.11 stdlib."""

import json
from html import escape
from pathlib import Path

OUTPUT = Path(__file__).parent
ELEMENTS = []


def element(kind, x, y, width, height, **extra):
    """Use stable IDs/seeds so unchanged source produces unchanged artifacts."""
    index = len(ELEMENTS) + 1
    item = {
        "id": f"boundary-{index}", "type": kind, "x": x, "y": y,
        "width": width, "height": height, "angle": 0,
        "strokeColor": "#17324d", "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
        "roughness": 0, "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": None, "seed": index, "version": 1, "versionNonce": index,
        "isDeleted": False, "boundElements": None, "updated": 0,
        "link": None, "locked": False, **extra,
    }
    ELEMENTS.append(item)


def text(x, y, label, size=18):
    lines = label.splitlines()
    element("text", x, y, max(map(len, lines)) * size * 0.62,
            len(lines) * size * 1.25, text=label, originalText=label,
            fontSize=size, fontFamily=3, textAlign="left", verticalAlign="top",
            containerId=None, lineHeight=1.25, autoResize=True)


def box(x, y, title, body, dashed=False):
    element("rectangle", x, y, 460, 140, backgroundColor="#edf3f8",
            strokeStyle="dashed" if dashed else "solid")
    text(x + 20, y + 16, title, 17)
    text(x + 20, y + 52, body, 16)


def arrow(x, y, dx, dy, dashed=False):
    element("arrow", x, y, abs(dx), abs(dy), points=[[0, 0], [dx, dy]],
            startBinding=None, endBinding=None, startArrowhead=None,
            endArrowhead="arrow", elbowed=False,
            strokeStyle="dashed" if dashed else "solid")


def render():
    text(40, 24, "Compound Engineering | source boundaries", 26)
    text(40, 65, "Baseline 1c3b073 (2026-11-12 check) | source model, not a runtime trace", 16)
    box(40, 110, "Inherited EveryInc / community source",
        "Kieran Klaassen; Nityesh Agarwal\nHuman / AI credits retained in history\nInherited parent: 6d8c867")
    box(600, 110, "JD-attributed maintenance delta",
        "Two commits: 4dacc08 and 1c3b073\nCI + lint cleanup; not new plugins\nNo upstream acceptance claim")
    arrow(500, 180, 100, 0)
    box(40, 300, "Local marketplace snapshot",
        "Catalog: compound-engineering 2.18.0\nPlugin: 2.20.0 | 27 agents / 20 commands\n13 skills | separate Coding Tutor 1.2.1")
    box(600, 300, "Documentation and checks",
        "Static HTML/CSS/JS: no site build\nCI: Ruff / stdlib imports / Ruby syntax\nNot an end-to-end plugin test")
    arrow(270, 250, 0, 50)
    arrow(830, 250, 0, 50)
    arrow(500, 370, 100, 0)
    box(40, 500, "Claude Code + target project (optional)",
        "Local catalog OR upstream installation\nPlan > Work > Review > Compound\nTools and scripts can change project", True)
    box(600, 500, "External integrations (optional)",
        "Playwright MCP / Context7\nGemini skill: separate API credentials\nNot started or verified by this diagram", True)
    arrow(270, 440, 0, 60, True)
    arrow(500, 570, 100, 0, True)
    text(40, 680, "Solid = source relationship | Dashed = optional execution, NOT RUN", 17)
    text(40, 713, "MIT notices retained; two skills reference missing LICENSE.txt terms.", 16)
    text(40, 740, "Source-derived overview; no installation, deployment or ownership certification.", 16)

    scene = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
             "elements": ELEMENTS, "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
             "files": {}}
    (OUTPUT / "source-boundaries.excalidraw").write_text(json.dumps(scene, indent=2) + "\n")
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 800" role="img" aria-labelledby="title desc">',
           '<title id="title">Compound Engineering source boundaries</title>',
           '<desc id="desc">Inherited source, JD maintenance delta, local snapshot, static docs, and optional execution. Generated from the same scene as the editable Excalidraw.</desc>',
           '<rect width="1100" height="800" fill="#ffffff"/>',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#17324d"/></marker></defs>']
    for item in ELEMENTS:
        x, y = item["x"], item["y"]
        dash = ' stroke-dasharray="7 5"' if item["strokeStyle"] == "dashed" else ""
        if item["type"] == "rectangle":
            svg.append(f'<rect x="{x}" y="{y}" width="460" height="140" fill="#edf3f8" stroke="#17324d"{dash}/>')
        elif item["type"] == "arrow":
            dx, dy = item["points"][1]
            svg.append(f'<path d="M {x} {y} l {dx} {dy}" fill="none" stroke="#17324d" marker-end="url(#arrow)"{dash}/>')
        else:
            size = item["fontSize"]
            for line_index, line in enumerate(item["text"].splitlines()):
                baseline = y + size + line_index * size * item["lineHeight"]
                svg.append(f'<text x="{x}" y="{baseline}" font-family="monospace" font-size="{size}" fill="#17324d">{escape(line)}</text>')
    svg.append("</svg>")
    (OUTPUT / "source-boundaries.svg").write_text("\n".join(svg) + "\n")


if __name__ == "__main__":
    render()
