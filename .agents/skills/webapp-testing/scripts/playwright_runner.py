import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_playwright(target_dir):
    errors = []
    warnings = []
    passes = []
    
    playwright_config_found = False
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if "playwright.config" in file:
                playwright_config_found = True
                passes.append(f"Discovered Playwright config file: {os.path.relpath(os.path.join(root, file), target_dir)}")
                
    if not playwright_config_found:
        warnings.append("No playwright.config.ts or playwright.config.js file discovered.")
        
    print(f"## Script Results: playwright_runner.py")
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
    check_playwright(target)
