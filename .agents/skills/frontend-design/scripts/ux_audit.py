import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_ux(target_dir):
    errors = []
    warnings = []
    passes = []
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith((".css", ".jsx", ".tsx", ".html")):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            # Check for font-family overrides that skip core variables
            if "font-family:" in content and "var(--" not in content and file.endswith(".css"):
                warnings.append(f"[{rel_path}] Hardcoded font-family in CSS. Use CSS variables instead.")
                
            # Check for standard responsive layouts (e.g. presence of grid or flex)
            if file.endswith(".css"):
                if "display: grid" in content or "display: flex" in content:
                    passes.append(f"{rel_path} uses modern layout system (flex/grid).")
                else:
                    warnings.append(f"[{rel_path}] No modern layout systems (flex/grid) detected in CSS file.")
                    
    print(f"## Script Results: ux_audit.py")
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
    audit_ux(target)
