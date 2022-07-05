from subprocess import run, Popen

with open("passwords.txt") as pwfp:
    lines = pwfp.readlines()

for word in lines:
    op = run(
        ["python3", "login.py"],
        input=word,
        capture_output=True,
        encoding="utf-8",
        text=True,
    )
    if "in" in op.stdout:
        print(f"password is {word}")
        break
