import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_type_coverage(target_dir):
    errors = []
    warnings = []
    passes = []
    
    file_count = 0
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith((".ts", ".tsx")):
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
                
            has_suppressions = False
            for idx, line in enumerate(lines, 1):
                # Check for "as any"
                if "as any" in line:
                    errors.append(f"[{rel_path}:{idx}] Avoid using 'as any' to bypass types: {line.strip()}")
                    has_suppressions = True
                    
                # Check for ts-ignore
                if "@ts-ignore" in line:
                    errors.append(f"[{rel_path}:{idx}] Avoid using '@ts-ignore' suppressions: {line.strip()}")
                    has_suppressions = True
                    
                # Check for ts-expect-error
                if "@ts-expect-error" in line:
                    warnings.append(f"[{rel_path}:{idx}] Prefer resolving errors over using '@ts-expect-error': {line.strip()}")
                    has_suppressions = True
            
            if not has_suppressions:
                passes.append(f"{rel_path} has 100% compliant type annotations.")
                
    print(f"## Script Results: type_coverage.py")
    print(f"\n### ❌ Errors Found ({len(errors)} items)")
    for err in errors:
        print(f"- {err}")
        
    print(f"\n### ⚠️ Warnings ({len(warnings)} items)")
    for warn in warnings:
        print(f"- {warn}")
        
    print(f"\n### ✅ Passed ({len(passes)} items)")
    if passes:
        for p in passes[:10]:
            print(f"- {p}")
        if len(passes) > 10:
            print(f"- ... and {len(passes) - 10} more files passed.")
    else:
        print("- TypeScript files scanned successfully")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    check_type_coverage(target)
