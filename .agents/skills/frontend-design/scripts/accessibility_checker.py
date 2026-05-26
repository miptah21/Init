import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_a11y(target_dir):
    errors = []
    warnings = []
    passes = []
    
    img_tag_regex = re.compile(r'<img[^>]*>')
    alt_attr_regex = re.compile(r'alt\s*=\s*["\'][^"\']*["\']')
    
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
                
            # Check img alt tags
            images = img_tag_regex.findall(content)
            images_checked = 0
            missing_alt = 0
            for img in images:
                images_checked += 1
                if not alt_attr_regex.search(img):
                    errors.append(f"[{rel_path}] Missing 'alt' attribute on image tag: {img}")
                    missing_alt += 1
                    
            if images_checked > 0 and missing_alt == 0:
                passes.append(f"{rel_path} has alt tags on all {images_checked} images.")
                
    print(f"## Script Results: accessibility_checker.py")
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
    else:
        print("- Accessibility checks complete.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_a11y(target)
