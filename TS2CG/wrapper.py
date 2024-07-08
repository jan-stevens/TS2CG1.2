import subprocess
from sys import stderr
import argparse
from pathlib import Path

def run_binary(binary_name, args):
    current_dir = Path(__file__).parent
    binary_path = current_dir / binary_name

    if not binary_path.exists():
        raise FileNotFoundError(f"Binary {binary_name} not found at {binary_path}")

    cmd = [str(binary_path)] + args
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr, file=stderr)

    return result.returncode

def main():

    parser = argparse.ArgumentParser(description='TS2CG: converts triangulated surfaces (TS) to coarse-grained membrane models')
    parser.add_argument('module', choices=['SOL', 'PLM', 'PCG'], help='Choice of which module to run')
    parser.add_argument('args', nargs=argparse.REMAINDER, help='Arguments for the chosen module')

    args = parser.parse_args()

    return run_binary(args.module, args.args)

if __name__ == '__main__':
    main()
