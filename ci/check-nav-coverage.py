#!/usr/bin/env python3
"""
检查 docs/ 下所有 Markdown 文件是否已添加到 mkdocs.yml 的导航中。

规则：docs/ 下的每个 .md 文件（文件名包含 deprecated 的除外）都必须
在 mkdocs.yml 中被引用，否则视为"未添加到网站"。

用法：
    python3 ci/check-nav-coverage.py

退出码：0 = 全部覆盖，1 = 存在未添加的文件
"""

from pathlib import Path
import sys


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    docs_dir = root / "docs"
    mkdocs_file = root / "mkdocs.yml"

    if not docs_dir.is_dir():
        print("错误：docs/ 目录不存在", file=sys.stderr)
        return 1
    if not mkdocs_file.is_file():
        print("错误：mkdocs.yml 不存在", file=sys.stderr)
        return 1

    mkdocs_text = mkdocs_file.read_text(encoding="utf-8")

    uncovered = []
    for file in sorted(docs_dir.rglob("*.md")):
        if "deprecated" in file.name:
            continue
        rel_path = file.relative_to(docs_dir).as_posix()
        if rel_path not in mkdocs_text:
            uncovered.append(rel_path)

    if not uncovered:
        print("✅ 全部通过：docs/ 下所有 Markdown 文件均已添加到 mkdocs.yml 导航")
        return 0

    print(f"❌ 发现 {len(uncovered)} 个未添加到导航的文件：\n")
    for rel_path in uncovered:
        print(f"  {rel_path}")
    print()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
