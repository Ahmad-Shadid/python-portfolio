#access_check.py
MAX_FAILED = 5
role = input("Role :")
MFA_passed = input("MFA passed ? (yes/no) :")
failed_attempts = int(input("Failed attempts :"))
mfa_ok = MFA_passed == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed_attempts < MAX_FAILED
print(f"MFA ok: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")