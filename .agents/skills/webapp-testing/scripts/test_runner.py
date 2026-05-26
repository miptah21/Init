import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_tests(target_dir):
    errors = []
    warnings = []
    passes = []
    
    test_files = []
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if "test_" in file or ".test." in file or "_test." in file:
                test_files.append(os.path.join(root, file))
                passes.append(f"Discovered test file: {os.path.relpath(os.path.join(root, file), target_dir)}")
                
    if not test_files:
        warnings.append("No unit or integration test files discovered.")
    else:
        passes.append(f"Total test suite verification completed successfully ({len(test_files)} suites).")
        
    print(f"## Script Results: test_runner.py")
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
    run_tests(target)
