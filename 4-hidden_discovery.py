#!/usr/bin/python3
cat > /tmp/4-hidden_discovery.py << EOF
import importlib.util
import sys
import os

def main():
    pyc_path = "/tmp/hidden_4.pyc"
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()

    for name in names:
        print(name)

if __name__ == "__main__":
    main()
EOF
