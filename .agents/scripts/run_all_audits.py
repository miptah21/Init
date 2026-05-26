#!/usr/bin/env python3
"""
🧠 Global Verification Runner - run_all_audits.py
Batch executes all active validation scripts across skills to generate a unified project compliance dashboard.

Usage:
    python .agents/scripts/run_all_audits.py [target_directory] [--category category_name]

Categories:
    code, db, frontend, security, seo, test
"""

import os
import sys
import re
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Scripts Registry with Relative Paths
SCRIPTS_REGISTRY = [
    {
        "name": "api_validator.py",
        "category": "code",
        "rel_path": "skills/clean-code/scripts/api_validator.py"
    },
    {
        "name": "i18n_checker.py",
        "category": "code",
        "rel_path": "skills/clean-code/scripts/i18n_checker.py"
    },
    {
        "name": "lint_runner.py",
        "category": "code",
        "rel_path": "skills/clean-code/scripts/lint_runner.py"
    },
    {
        "name": "mobile_audit.py",
        "category": "code",
        "rel_path": "skills/clean-code/scripts/mobile_audit.py"
    },
    {
        "name": "type_coverage.py",
        "category": "code",
        "rel_path": "skills/clean-code/scripts/type_coverage.py"
    },
    {
        "name": "schema_validator.py",
        "category": "db",
        "rel_path": "skills/database-design/scripts/schema_validator.py"
    },
    {
        "name": "accessibility_checker.py",
        "category": "frontend",
        "rel_path": "skills/frontend-design/scripts/accessibility_checker.py"
    },
    {
        "name": "ux_audit.py",
        "category": "frontend",
        "rel_path": "skills/frontend-design/scripts/ux_audit.py"
    },
    {
        "name": "security_scan.py",
        "category": "security",
        "rel_path": "skills/security-auditor/scripts/security_scan.py"
    },
    {
        "name": "seo_checker.py",
        "category": "seo",
        "rel_path": "skills/seo-optimizer/scripts/seo_checker.py"
    },
    {
        "name": "geo_checker.py",
        "category": "seo",
        "rel_path": "skills/seo-optimizer/scripts/geo_checker.py"
    },
    {
        "name": "lighthouse_audit.py",
        "category": "frontend",
        "rel_path": "skills/frontend-performance/scripts/lighthouse_audit.py"
    },
    {
        "name": "test_runner.py",
        "category": "test",
        "rel_path": "skills/webapp-testing/scripts/test_runner.py"
    },
    {
        "name": "playwright_runner.py",
        "category": "test",
        "rel_path": "skills/webapp-testing/scripts/playwright_runner.py"
    }
]

def check_rtk():
    """Verify if the 'rtk' tool is available in the system PATH."""
    rtk_path = shutil.which("rtk")
    if rtk_path:
        try:
            res = subprocess.run(["rtk", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if res.returncode == 0:
                ver = res.stdout.strip().replace("\n", " ")
                return True, ver
        except Exception:
            pass
        return True, "rtk (available)"
    return False, "Not Found"

def run_script(script_path, target_dir):
    """Execute a single validation script in a subprocess and capture output."""
    cmd = [sys.executable, str(script_path), str(target_dir)]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore', timeout=30)
        return res.returncode, res.stdout, res.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Execution timeout expired (30s)."
    except Exception as e:
        return -2, "", f"Failed to launch script: {e}"

def parse_metrics(output):
    """Parse errors, warnings, and passed items from standard script outputs using regex."""
    err_match = re.search(r'Errors Found\s*\((\d+)\s*items?\)', output, re.IGNORECASE)
    warn_match = re.search(r'Warnings\s*\((\d+)\s*items?\)', output, re.IGNORECASE)
    pass_match = re.search(r'Passed\s*\((\d+)\s*items?\)', output, re.IGNORECASE)
    
    errs = int(err_match.group(1)) if err_match else 0
    warns = int(warn_match.group(1)) if warn_match else 0
    passes = int(pass_match.group(1)) if pass_match else 0
    
    # Fallback to general lines checks if regex misses
    if not err_match and "Errors Found" in output:
        errs = len(re.findall(r'^-\s+\[', output, re.MULTILINE))
        
    return errs, warns, passes

def main():
    # Parse CLI Arguments
    args = sys.argv[1:]
    target_dir = "."
    category_filter = None
    
    # Process target dir and options
    clean_args = []
    idx = 0
    while idx < len(args):
        if args[idx] == "--category" and idx + 1 < len(args):
            category_filter = args[idx+1].lower()
            idx += 2
        else:
            clean_args.append(args[idx])
            idx += 1
            
    if clean_args:
        target_dir = clean_args[0]
        
    target_path = Path(target_dir).resolve()
    agents_dir = Path(__file__).resolve().parent.parent
    
    print(f"\n🧠 Starting Global Compliance Auditing Suite...")
    print(f"Target Directory: {target_path}")
    if category_filter:
        print(f"Category Filter: {category_filter}")
        
    # Check for RTK
    rtk_active, rtk_info = check_rtk()
    
    results = []
    total_errors = 0
    total_warnings = 0
    total_passed = 0
    
    # Run each eligible script
    for item in SCRIPTS_REGISTRY:
        if category_filter and item["category"] != category_filter:
            continue
            
        script_full_path = agents_dir / item["rel_path"]
        if not script_full_path.exists():
            # Script missing physically, record error
            results.append({
                "name": item["name"],
                "category": item["category"],
                "status": "Missing",
                "errors": 1,
                "warnings": 0,
                "passed": 0,
                "output": "Verification script not found at expected path.",
                "stderr": f"Missing: {script_full_path}"
            })
            total_errors += 1
            continue
            
        print(f" -> Running [{item['name']}] ...")
        ret_code, stdout, stderr = run_script(script_full_path, target_path)
        
        if ret_code != 0:
            status = "Execution Error"
            errs, warns, passes = 1, 0, 0
        else:
            status = "Passed" if "Errors Found (0 items)" in stdout or "Passed" in stdout else "Issues Found"
            errs, warns, passes = parse_metrics(stdout)
            
        total_errors += errs
        total_warnings += warns
        total_passed += passes
        
        results.append({
            "name": item["name"],
            "category": item["category"],
            "status": status,
            "errors": errs,
            "warnings": warns,
            "passed": passes,
            "output": stdout,
            "stderr": stderr
        })
        
    # Build consolidated Markdown Report
    report = []
    report.append("# Unified Compliance & Verification Report")
    report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Target: `{target_path}`")
    report.append("")
    
    # RTK Alert Banner
    if rtk_active:
        report.append(f"> [!TIP]\n> **RTK Token Optimization Active:** Successfully detected `{rtk_info}` on the PATH. Native commands are configured to run with compression benefits (60-90% savings).")
    else:
        report.append("> [!WARNING]\n> **RTK Missing Warning:** The `rtk` token optimization utility was not detected on your system `PATH`. Install `rtk` (Rust binary) to compress terminal responses by 60-90% and save tokens.")
        
    report.append("")
    report.append("## Executive Compliance Dashboard")
    report.append("")
    report.append("| Script Name | Category | Status | Errors ❌ | Warnings ⚠️ | Passed ✅ |")
    report.append("| :--- | :--- | :--- | :---: | :---: | :---: |")
    
    for r in results:
        status_emoji = "✅" if r["errors"] == 0 and r["warnings"] == 0 else ("⚠️" if r["errors"] == 0 else "❌")
        report.append(f"| `{r['name']}` | `{r['category']}` | {status_emoji} {r['status']} | {r['errors']} | {r['warnings']} | {r['passed']} |")
        
    report.append("")
    report.append(f"### Total Aggregated Metrics:")
    report.append(f"- **Total Errors ❌:** {total_errors}")
    report.append(f"- **Total Warnings ⚠️:** {total_warnings}")
    report.append(f"- **Total Checks Passed ✅:** {total_passed}")
    report.append("")
    
    # Detailed sections if issues exist
    report.append("## Detailed Compliance Findings")
    for r in results:
        if r["errors"] > 0 or r["warnings"] > 0:
            report.append(f"\n### Findings for `{r['name']}` ({r['category']})")
            if r["output"]:
                # Strip standard passed list to keep it brief
                lines = r["output"].split("\n")
                filtered_lines = []
                in_passed = False
                for line in lines:
                    if "### ✅ Passed" in line:
                        in_passed = True
                    if in_passed and line.strip().startswith("-"):
                        continue
                    filtered_lines.append(line)
                report.append("\n".join(filtered_lines))
            if r["stderr"]:
                report.append(f"**Execution Error (stderr):**\n```\n{r['stderr']}\n```")
                
    report_content = "\n".join(report)
    
    # Write report to disk
    report_file = Path(target_path) / "audit_report.md"
    try:
        report_file.write_text(report_content, encoding='utf-8')
        print(f"\n✅ Consolidated compliance report successfully written to: {report_file}")
    except Exception as e:
        print(f"\n⚠️ Warning: Could not write consolidated report file: {e}")
        
    # Output unified summary to console
    print("\n" + "="*60)
    print("COMPLIANCE RUNNER SUMMARY")
    print("="*60)
    print(f"Total Errors Found:    {total_errors}")
    print(f"Total Warnings Found:  {total_warnings}")
    print(f"Total Passed Checks:   {total_passed}")
    print("-"*60)
    if total_errors > 0:
        print("❌ STATUS: COMPLIANCE AUDIT FAILED (Errors detected).")
    else:
        print("✅ STATUS: COMPLIANCE AUDIT PASSED.")
    print("="*60)
    
    # Exit code maps to errors presence
    sys.exit(1 if total_errors > 0 else 0)

if __name__ == "__main__":
    main()
