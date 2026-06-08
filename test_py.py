import os
from pathlib import Path
import pathspec

# File types we actually care about
VALID_EXTENSIONS = ('.py', '.txt', '.json', '.yaml', '.yml', '.md', '.ini')

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 MB


def load_gitignore(root_folder):
    gitignore_path = os.path.join(root_folder, ".gitignore")

    if not os.path.exists(gitignore_path):
        return None

    with open(gitignore_path, 'r') as f:
        lines = f.readlines()

    spec = pathspec.PathSpec.from_lines("gitwildmatch", lines)
    return spec


def is_ignored(path, spec, root_folder):
    if spec is None:
        return False
    relative_path = os.path.relpath(path, root_folder)
    return spec.match_file(relative_path)


def collect_project_details(root_folder, output_file):
    spec = load_gitignore(root_folder)

    with open(output_file, 'w', encoding='utf-8') as out:

        for root, dirs, files in os.walk(root_folder):

            # Remove ignored directories
            dirs[:] = [
                d for d in dirs
                if not is_ignored(os.path.join(root, d), spec, root_folder)
            ]

            out.write(f"\n{'='*80}\n")
            out.write(f"FOLDER: {root}\n")
            out.write(f"{'='*80}\n\n")

            for file in files:
                file_path = os.path.join(root, file)

                if is_ignored(file_path, spec, root_folder):
                    continue

                if not file.endswith(VALID_EXTENSIONS):
                    continue

                try:
                    if os.path.getsize(file_path) > MAX_FILE_SIZE:
                        out.write(f"[Skipped large file: {file}]\n")
                        continue
                except:
                    continue

                out.write(f"\n{'-'*60}\n")
                out.write(f"FILE: {file}\n")
                out.write(f"{'-'*60}\n")

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"\n[Error reading file: {e}]\n")

                out.write("\n\n")


# ✅ Usage
root_folder = r"E:\New folder\Pdf_praser_llm"
output_file = "project_dump.txt"

collect_project_details(root_folder, output_file)

print("✅ Done! Filtered using .gitignore")