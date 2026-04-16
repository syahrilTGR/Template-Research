import os
import sys
import argparse

# Add the docx skill scripts to the path so we can import their logic
SKILL_OFFICE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".agents", "skills", "docx", "scripts", "office"))
sys.path.append(SKILL_OFFICE_PATH)

try:
    import unpack as office_unpack
    import pack as office_pack
    print("Docx Surgery Tools Loaded Successfully.")
except ImportError as e:
    print(f"Error loading surgical tools: {e}")
    print(f"Path searched: {SKILL_OFFICE_PATH}")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="DOCX Surgery: Advanced Unpack/Pack tools for Academic Documents")
    subparsers = parser.add_subparsers(dest="command", help="Available surgical commands")

    # Unpack Command
    unpack_parser = subparsers.add_parser("unpack", help="Unpack a .docx into pretty-printed XML for editing")
    unpack_parser.add_argument("input_file", help="Path to the .docx file")
    unpack_parser.add_argument("output_dir", help="Directory where XML files will be extracted")
    unpack_parser.add_argument("--no-merge", action="store_false", dest="merge_runs", help="Don't merge identical runs")

    # Pack Command
    pack_parser = subparsers.add_parser("pack", help="Pack an XML directory back into a .docx")
    pack_parser.add_argument("input_dir", help="Directory containing the unpacked XML files")
    pack_parser.add_argument("output_file", help="Path for the generated .docx file")
    pack_parser.add_argument("--original", help="Original .docx file for structural validation")

    args = parser.parse_args()

    if args.command == "unpack":
        print(f"Performing surgery: Unpacking {args.input_file}...")
        _, message = office_unpack.unpack(args.input_file, args.output_dir, merge_runs=args.merge_runs)
        print(message)
    
    elif args.command == "pack":
        print(f"Performing surgery: Packing {args.input_dir}...")
        _, message = office_pack.pack(args.input_dir, args.output_file, original_file=args.original)
        print(message)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
