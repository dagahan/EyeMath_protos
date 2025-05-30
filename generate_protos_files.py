import os, sys
import argparse
import subprocess


os.system("pip install -r req.txt")

#python3 generate_protos_files.py /home/usov/myprojects/EyeMath -o /home/usov/myprojects/generated  --py --go


def find_proto_files(root_dir):
    proto_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # look for directories named 'proto'
        if os.path.basename(dirpath) == 'proto':
            for fname in filenames:
                if fname.endswith('.proto'):
                    proto_files.append(os.path.join(dirpath, fname))
    return proto_files


def gen_python(proto_file, proto_dir, out_dir):
    cmd = [
        'python3', '-m', 'grpc_tools.protoc',
        f'-I{proto_dir}',
        f'--python_out={out_dir}',
        f'--grpc_python_out={out_dir}',
        proto_file
    ]
    subprocess.run(cmd, check=True)


def gen_go(proto_file, proto_dir, out_dir):
    cmd = [
        'protoc',
        f'-I{proto_dir}',
        proto_file,
        f'--go_out={out_dir}',
        '--go_opt=paths=source_relative',
        f'--go-grpc_out={out_dir}',
        '--go-grpc_opt=paths=source_relative',
    ]
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description='Generate gRPC code from .proto files')
    parser.add_argument('root', help='Root directory to search for proto folders (absolute path)')
    parser.add_argument('-o', '--out', dest='outdir', required=True, help='Output directory for generated code')
    parser.add_argument('--py', action='store_true', help='Generate Python code')
    parser.add_argument('--go', action='store_true', help='Generate Go code')
    args = parser.parse_args()

    if not args.py and not args.go:
        parser.error('At least one of --py or --go must be specified')

    proto_files = find_proto_files(args.root)
    if not proto_files:
        print('No .proto files found in any proto/ directory under', args.root)
        return

    # prepare output directories
    if args.py:
        py_out = os.path.join(args.outdir, 'py')
        os.makedirs(py_out, exist_ok=True)
    if args.go:
        go_out = os.path.join(args.outdir, 'go')
        os.makedirs(go_out, exist_ok=True)

    for pf in proto_files:
        proto_dir = os.path.dirname(pf)
        print(f'Processing {pf}...')
        if args.py:
            print('  Generating Python code...')
            gen_python(pf, proto_dir, py_out)
        if args.go:
            print('  Generating Go code...')
            gen_go(pf, proto_dir, go_out)

    print('Generation complete!')


if __name__ == '__main__':
    main()
