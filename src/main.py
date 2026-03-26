import sys

shell_init = True

while True :
    if shell_init == True :
        sys.stdout.write("NatureShell Indev")
        shell_init = False
    sys.stdout.write("\n>>> ")
    shell_input = sys.stdin.readline().strip()
