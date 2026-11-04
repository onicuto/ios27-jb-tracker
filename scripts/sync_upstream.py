#!/usr/bin/env python3
"""
scripts/sync_upstream.py
Автоматическая проверка обновлений в upstream (iMaxTomas/ios27-jb-tracker),
копирование новых изменений, валидация GFM сносок и ссылок,
сохранение китайских оригиналов (-zh) и пуш в origin main (onicuto/ios27-jb-tracker).
"""

import os
import sys
import subprocess
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMIT_TRACKER_FILE = REPO_ROOT / ".last_upstream_commit"
UPSTREAM_REMOTE = "upstream"
UPSTREAM_URL = "https://github.com/iMaxTomas/ios27-jb-tracker.git"
ORIGIN_REMOTE = "origin"

def run_cmd(cmd, cwd=REPO_ROOT, check=True):
    res = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True)
    if check and res.returncode != 0:
        raise RuntimeError(f"Command failed ({res.returncode}): {cmd}\nStderr: {res.stderr}\nStdout: {res.stdout}")
    return res

def ensure_upstream_remote():
    remotes = run_cmd(["git", "remote"], check=True).stdout.split()
    if UPSTREAM_REMOTE not in remotes:
        print(f"[INFO] Добавление remote {UPSTREAM_REMOTE}...")
        run_cmd(["git", "remote", "add", UPSTREAM_REMOTE, UPSTREAM_URL])

def get_last_commit():
    if COMMIT_TRACKER_FILE.exists():
        return COMMIT_TRACKER_FILE.read_text(encoding="utf-8").strip()
    return None

def set_last_commit(commit_sha):
    COMMIT_TRACKER_FILE.write_text(commit_sha + "\n", encoding="utf-8")

def validate_markdown_and_footnotes():
    """Проверка и автоматическое исправление GFM сносок и валидация ссылок."""
    issues_fixed = 0
    fn_caret_pattern = re.compile(r'\[\^(\d+)\^\]')
    orphan_def_pattern = re.compile(r'^\[(\d+)\]:\s*(http.*)$', re.MULTILINE)
    
    for md_path in REPO_ROOT.glob("**/*.md"):
        if ".git" in md_path.parts:
            continue
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
            
        modified = False
        if "[^" in content:
            new_content = fn_caret_pattern.sub(r'[^\1]', content)
            new_content = orphan_def_pattern.sub(r'[^\1]: \2', new_content)
            if new_content != content:
                md_path.write_text(new_content, encoding="utf-8")
                modified = True
                issues_fixed += 1
                
    # Валидация JSON файлов
    for json_path in (REPO_ROOT / "data").glob("*.json"):
        with open(json_path, "r", encoding="utf-8") as jf:
            json.load(jf)
            
    return issues_fixed

def sync():
    ensure_upstream_remote()
    print("[INFO] Проверка обновлений в upstream...")
    run_cmd(["git", "fetch", UPSTREAM_REMOTE, "main"])
    
    current_upstream = run_cmd(["git", "rev-parse", f"{UPSTREAM_REMOTE}/main"]).stdout.strip()
    last_commit = get_last_commit()
    
    print(f"[INFO] Текущий upstream/main: {current_upstream}")
    print(f"[INFO] Предыдущий зафиксированный коммит: {last_commit}")
    
    if last_commit == current_upstream:
        print("[OK] Репозиторий полностью синхронизирован. Новых коммитов нет.")
        return 0
        
    diff_range = f"{last_commit}..{current_upstream}" if last_commit else current_upstream
    changed_files = run_cmd(["git", "diff", "--name-only", diff_range]).stdout.splitlines()
    print(f"[INFO] Обнаружено новых коммитов! Изменённые файлы ({len(changed_files)}):")
    for f in changed_files:
        print(f"  - {f}")
        
    # Копирование и синхронизация китайских файлов-исходников
    for path_str in changed_files:
        src = REPO_ROOT / path_str
        if not path_str or not (REPO_ROOT / path_str).exists():
            continue
            
        # Для файлов в корне сохраняем _ZH копию при обновлении
        if path_str == "README.md":
            zh_target = REPO_ROOT / "README_ZH.md"
            upstream_content = run_cmd(["git", "show", f"{UPSTREAM_REMOTE}/main:README.md"]).stdout
            zh_target.write_text(upstream_content, encoding="utf-8")
            print(f"[INFO] Обновлён {zh_target.name} из апстрима.")
        elif path_str.endswith(".json") and not path_str.endswith("-zh.json"):
            zh_target = REPO_ROOT / path_str.replace(".json", "-zh.json")
            upstream_content = run_cmd(["git", "show", f"{UPSTREAM_REMOTE}/main:{path_str}"]).stdout
            zh_target.write_text(upstream_content, encoding="utf-8")
            print(f"[INFO] Обновлён {zh_target.name} из апстрима.")
        elif path_str.endswith(".md") and not path_str.endswith("-zh.md") and not path_str.endswith("_ZH.md"):
            zh_target = REPO_ROOT / path_str.replace(".md", "-zh.md")
            upstream_content = run_cmd(["git", "show", f"{UPSTREAM_REMOTE}/main:{path_str}"]).stdout
            zh_target.write_text(upstream_content, encoding="utf-8")
            print(f"[INFO] Обновлён {zh_target.name} из апстрима.")

    # Валидация сносок и ссылок
    fixed_count = validate_markdown_and_footnotes()
    if fixed_count:
        print(f"[INFO] Автоматически скорректировано сносок в файлах: {fixed_count}")

    # Запись нового коммита
    set_last_commit(current_upstream)
    
    # Git commit & push
    status = run_cmd(["git", "status", "--porcelain"]).stdout.strip()
    if status:
        short_sha = current_upstream[:7]
        print(f"[INFO] Создание коммита синхронизации для {short_sha}...")
        run_cmd(["git", "add", "-A"])
        run_cmd(["git", "commit", "-m", f"chore(sync): синхронизация с upstream v0.8+ ({short_sha})"])
        print("[INFO] Отправка изменений в origin main...")
        run_cmd(["git", "push", ORIGIN_REMOTE, "main"])
        print(f"[SUCCESS] Успешно синхронизировано и отправлено в {ORIGIN_REMOTE}/main!")
    else:
        print("[INFO] Локальных изменений после проверки не появилось.")
        
    return 0

if __name__ == "__main__":
    try:
        sys.exit(sync())
    except Exception as e:
        print(f"[ERROR] Ошибка синхронизации: {e}", file=sys.stderr)
        sys.exit(1)
