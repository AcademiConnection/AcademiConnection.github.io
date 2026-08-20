#!/usr/bin/env python3
"""
检查学术关系网络文档中的链接规范。

规则：对于每个机构目录下的 *_network.md 文件，如果在 README.md 正文中
提到了该文件名，则必须将其作为 Markdown 链接（[text](filename) 格式）引用，
不能以纯文本形式出现。

退出码：0 = 全部通过，1 = 发现问题
"""

from pathlib import Path
import re
import sys


def check_institution(directory: Path) -> list[dict]:
    """检查单个机构目录的链接规范，返回问题列表。"""
    readme = directory / "README.md"
    if not readme.exists():
        return []

    text = readme.read_text(encoding="utf-8")
    issues = []
    report_files = [
        file.name
        for file in directory.iterdir()
        if file.is_file()
        and (file.name.endswith("_network.md") or file.name.endswith("_profile.md"))
    ]

    for filename in report_files:
        if filename not in text:
            issues.append({
                "file": readme,
                "target": filename,
                "type": "missing",
                "message": "目录内存在该报告文件，但 README.md 中未引用",
            })
            continue

        link_pattern = re.compile(r"\[[^\]]*\]\(" + re.escape(filename) + r"\)")
        if link_pattern.search(text):
            continue

        # 文件名在正文中出现但未被链接：作为裸文本或仅出现在链接文本中
        # 先把所有 Markdown 链接（包括格式正确的和格式错误的）中的文件名移除，
        # 再检查剩余文本中是否还有该文件名
        text_without_links = re.sub(
            r"\[[^\]]*" + re.escape(filename) + r"[^\]]*\]\([^)]+\)",
            "",
            text,
        )
        text_without_links = re.sub(
            r"\[[^\]]*\]\(" + re.escape(filename) + r"\)",
            "",
            text_without_links,
        )

        if filename not in text_without_links:
            continue

        # 提取出现位置上下文
        contexts = []
        for match in re.finditer(re.escape(filename), text_without_links):
            start = max(0, match.start() - 40)
            end = min(len(text_without_links), match.end() + 40)
            contexts.append(text_without_links[start:end].replace("\n", " "))
            if len(contexts) >= 3:
                break

        issues.append({
            "file": readme,
            "target": filename,
            "type": "bare",
            "message": "报告文件名以裸文本出现，未使用 Markdown 链接",
            "contexts": contexts,
        })

    return issues


def main() -> int:
    docs_dir = Path("docs")
    if not docs_dir.is_dir():
        print("错误：docs/ 目录不存在", file=sys.stderr)
        return 1

    issues = []
    for directory in sorted(docs_dir.glob("*_faculty_network")):
        issues.extend(check_institution(directory))

    if not issues:
        print("✅ 全部通过：机构 README 中的报告文件均已正确使用 Markdown 链接引用")
        return 0

    missing_count = sum(issue["type"] == "missing" for issue in issues)
    bare_count = sum(issue["type"] == "bare" for issue in issues)
    print(f"❌ 发现 {len(issues)} 处问题（未引用: {missing_count}，裸文本: {bare_count}）\n")

    for issue in issues:
        print(f"📄 {issue['file']}")
        print(f"   目标: {issue['target']}")
        print(f"   问题: {issue['message']}")
        for context in issue.get("contexts", []):
            print(f"   上下文: ...{context}...")
        print()

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
