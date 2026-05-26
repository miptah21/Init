import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_seo(target_dir):
    errors = []
    warnings = []
    passes = []
    
    title_regex = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)
    h1_regex = re.compile(r'<h1[^>]*>(.*?)</h1>', re.IGNORECASE)
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith((".html", ".jsx", ".tsx")):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            if file.endswith(".html"):
                # Title check
                titles = title_regex.findall(content)
                if not titles:
                    errors.append(f"[{rel_path}] Missing <title> tag on page.")
                else:
                    title_len = len(titles[0])
                    if title_len < 30 or title_len > 60:
                        warnings.append(f"[{rel_path}] Title length ({title_len}) is outside recommended 30-60 characters.")
                    else:
                        passes.append(f"{rel_path} title length is optimal ({title_len} chars).")
                        
                # H1 checks
                h1s = h1_regex.findall(content)
                if len(h1s) > 1:
                    errors.append(f"[{rel_path}] Multiple <h1> tags found. Only one allowed per page.")
                elif len(h1s) == 0:
                    warnings.append(f"[{rel_path}] No <h1> tag found. Add exactly one per page.")
                    
    print(f"## Script Results: seo_checker.py")
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
    audit_seo(target)
