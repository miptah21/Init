import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_i18n(target_dir):
    errors = []
    warnings = []
    passes = []
    
    # Simple regex to check for hardcoded raw text inside tags or attributes in JSX/TSX
    # e.g., <div>Hello World</div>
    raw_text_regex = re.compile(r'>\s*([A-Za-z0-9 ]{2,50})\s*<')
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith((".tsx", ".jsx", ".html")):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            if "i18n-ignore" in content:
                continue
                
            matches = raw_text_regex.findall(content)
            has_hardcoded = False
            for match in matches:
                match_str = match.strip()
                if match_str and not match_str.isdigit():
                    warnings.append(f"[{rel_path}] Hardcoded raw text found: \"{match_str}\" — consider extracting to i18n file.")
                    has_hardcoded = True
            
            if not has_hardcoded:
                passes.append(f"{rel_path} has no hardcoded static UI strings.")
                
    print(f"## Script Results: i18n_checker.py")
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
        print("- UI files scanned successfully")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    check_i18n(target)
