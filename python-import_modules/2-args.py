#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    else:
        print(f"{count} argument{'s' if count != 1 else ''}:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
