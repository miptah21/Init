import os
import sys
import re

# Ensure Windows terminal standard out supports UTF-8 emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def lint_directory(target_dir):
    errors = []
    warnings = []
    passes = []
    
    file_count = 0
    
    for root, dirs, files in os.walk(target_dir):
        # Skip node_modules, git, and other common directories
        if any(ignored in root for ignored in ["node_modules", ".git", "_deprecated", ".gemini"]):
            continue
            
        for file in files:
            if file == "audit_report.md" or not file.endswith((".py", ".ts", ".tsx", ".js", ".jsx", ".md")):
                continue
                
            file_count += 1
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            # Rule 1: File size constraints (specifically SKILL.md under 250 lines)
            file_content = "".join(lines)
            if "lint-ignore" not in file_content and "lint-ignore-file-size" not in file_content:
                if file == "SKILL.md":
                    if len(lines) > 250:
                        warnings.append(f"[{rel_path}:0] SKILL.md exceeds 250 lines constraint ({len(lines)} lines)")
                    else:
                        passes.append(f"{rel_path} size is within constraints ({len(lines)} lines)")
                elif len(lines) > 500 and not file.endswith(".md"):
                    warnings.append(f"[{rel_path}:0] File is large ({len(lines)} lines). Consider modularizing.")
                
            nest_level = 0
            in_deep_nest = False
            for idx, line in enumerate(lines, 1):
                # Rule 2: Guard unacceptable comments (only for JS/TS/React files)
                if file.endswith((".ts", ".tsx", ".js", ".jsx")) and "//" in line:
                    if re.search(r"//\s*(Increment|Initialize|Assign|Return)", line, re.IGNORECASE):
                        errors.append(f"[{rel_path}:{idx}] Redundant comment: {line.strip()}")
                    elif re.search(r"//\s*.*i\+\+", line, re.IGNORECASE) or re.search(r"i\+\+\s*//", line):
                        errors.append(f"[{rel_path}:{idx}] Obvious comment: {line.strip()}")
                        
                # Rule 3: Check nesting level (approximate curly brace nesting - restrict to JS/TS files)
                if file.endswith((".ts", ".tsx", ".js", ".jsx")):
                    stripped = line.strip()
                    if "{" in stripped:
                        nest_level += stripped.count("{")
                    if "}" in stripped:
                        nest_level -= stripped.count("}")
                    if nest_level > 4:
                        if not in_deep_nest:
                            warnings.append(f"[{rel_path}:{idx}] Deeply nested block starts here (nesting level: {nest_level})")
                            in_deep_nest = True
                    else:
                        in_deep_nest = False
                    
    # Compile results
    print(f"## Script Results: lint_runner.py")
    print(f"\n### ❌ Errors Found ({len(errors)} items)")
    for err in errors:
        print(f"- {err}")
        
    print(f"\n### ⚠️ Warnings ({len(warnings)} items)")
    for warn in warnings:
        print(f"- {warn}")
        
    print(f"\n### ✅ Passed ({len(passes)} items)")
    if passes:
        for p in passes[:10]:  # Limit output
            print(f"- {p}")
        if len(passes) > 10:
            print(f"- ... and {len(passes) - 10} more files passed.")
    else:
        print("- General project layout checked")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    lint_directory(target)
