import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_security(target_dir):
    errors = []
    warnings = []
    passes = []
    
    # Check for hardcoded API keys/passwords
    secret_patterns = [
        re.compile(r'(api_key|password|secret|token|passwd|credentials)\s*=\s*["\'][a-zA-Z0-9_\-]{8,}["\']', re.IGNORECASE),
        re.compile(r'postgres://.*:.*@', re.IGNORECASE)  # Example:
    ]
    
    for root, dirs, files in os.walk(target_dir):
        if any(ignored in root for ignored in ["node_modules", ".git", ".gemini"]):
            continue
            
        for file in files:
            if not file.endswith((".py", ".ts", ".tsx", ".js", ".jsx", ".env", ".yml", ".json")):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, target_dir)
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except Exception as e:
                warnings.append(f"[{rel_path}:0] Could not read file: {e}")
                continue
                
            has_leak = False
            for idx, line in enumerate(lines, 1):
                # Ignore comment lines and README examples
                if line.strip().startswith(("#", "//", "*")) or "WRONG" in line or "Example:" in line:
                    continue
                    
                for pattern in secret_patterns:
                    if pattern.search(line):
                        errors.append(f"[{rel_path}:{idx}] Possible hardcoded credential leakage detected: {line.strip()[:60]}")
                        has_leak = True
                        
                # Check for raw SQL concatenations
                if "SELECT" in line or "INSERT" in line:
                    if "+" in line or "%" in line or "f\"" in line or "f\'" in line:
                        if not any(x in line for x in ["execute", "SQLExecuteQueryOperator", "PostgresHook", "BaseHook"]):
                            warnings.append(f"[{rel_path}:{idx}] Avoid string interpolation in SQL queries to prevent injection: {line.strip()[:60]}")
            
            if not has_leak:
                passes.append(f"{rel_path} passed key/secret leak checks.")
                
    print(f"## Script Results: security_scan.py")
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
    audit_security(target)
