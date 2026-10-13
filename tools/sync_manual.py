#!/usr/bin/env python3
"""Разносит docs/МАНУАЛ.html по трём копиям.

Источник правды один — docs/МАНУАЛ.html. Остальные три файла это его копии
для HTTP-сервера, сборки APK и сборки под iOS; руками их не трогать.

Запуск:  python3 tools/sync_manual.py          # синхронизировать
         python3 tools/sync_manual.py --check  # только проверить (для CI/перед коммитом)
"""

import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "МАНУАЛ.html"
COPIES = [
    ROOT / "docs" / "index.html",
    ROOT / "android-app" / "app" / "src" / "main" / "assets" / "manual.html",
    ROOT / "ios-app" / "PassatEcoFuel" / "manual.html",
]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    if not SRC.exists():
        sys.exit(f"нет источника: {SRC}")
    check = "--check" in sys.argv
    src_hash = digest(SRC)
    stale = [c for c in COPIES if not c.exists() or digest(c) != src_hash]

    if check:
        if stale:
            print("РАССИНХРОН:", *[str(c.relative_to(ROOT)) for c in stale], sep="\n  ")
            sys.exit(1)
        print(f"все {len(COPIES)} копии совпадают с источником ({src_hash[:12]})")
        return

    for c in stale:
        c.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SRC, c)
        print("обновлено:", c.relative_to(ROOT))
    if not stale:
        print("всё уже синхронно")
    print(f"sha256 источника: {src_hash[:12]}")


if __name__ == "__main__":
    main()
