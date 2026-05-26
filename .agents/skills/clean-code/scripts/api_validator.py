import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def validate_api(target_dir):
    errors = []
    warnings = []
    passes = []
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith(".py"):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            in_handler = False
            handler_start = 0
            has_try = False
            
            for idx, line in enumerate(lines, 1):
                # Simple heuristic for API routing handlers
                if "@app.get" in line or "@app.post" in line or "@router.get" in line or "@router.post" in line:
                    in_handler = True
                    handler_start = idx
                    has_try = False
                    
                if in_handler:
                    if "try:" in line:
                        has_try = True
                    # End of handler function (e.g. next def or standard indents reset)
                    if idx > handler_start + 1 and line.startswith("def "):
                        if not has_try:
                            warnings.append(f"[{rel_path}:{handler_start}] Route handler missing try/except block.")
                        in_handler = False
                        
            passes.append(f"{rel_path} API routing checks complete.")
            
    print(f"## Script Results: api_validator.py")
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

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    validate_api(target)
