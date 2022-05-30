#! /usr/bin/env python

# Take as argument an input directory,
# read its contents to generate a sample sheet
# (to be used for taxonomic profiling).
# Input files are assumed to be FASTQ files with extensions:
# .fq, .fastq, .fq.gz or .fastq.gz

import argparse
from pathlib import Path
import re
import sys

parser = argparse.ArgumentParser(
    description="Read files from input directory to generate a sample sheet."
)
parser.add_argument("input_dir", type=str, help="Directory to read input files from")

args = parser.parse_args()

input_dir = Path(args.input_dir)

print("Parsed arguments:", input_dir, file=sys.stderr)


def read_input_directory(input_dir):
    if input_dir.is_dir():
        input_files = list(input_dir.glob("*"))

    else:
        print("Input directory '%s' does not exist!" % input_dir)
        exit(1)

    return input_files


def infer_library_type(input_files):
    """
The files should derive from metagenomic data, which are in a single-end (SE)
or paired-end (PE) format, with or without UMIs in separate files.
It is assumed that files are:
    1. SE with no UMIs if files have no numbered extension or only '_R1' or '_1'
    2. PE without UMIs if files have '_[R]1' and '_[R]2' suffix, each in equal
       numbers ([R] is optional, there may or may not be an R)
    3. PE with UMIs if files have one of three suffixes: '_[R][123]', in equal
       numbers. It is assumed that UMIs are then _R2, which is checked by their
       file sizes. (_R1 and _R3 should be roughly equal, _R2 should be clearly smaller)
    """
    input_files_as_strings = [str(file) for file in input_files]

    if len(input_files) == 0:
        print("Input directory '%s' is empty!" % input_dir)
        exit(2)

    elif len(input_files) == 1:
        print("Only one file in '%s', assuming it's single-end." % input_dir)

    else:
        if len(input_files) % 3 == 0:
            # If the length is divisible by 3, it is most likely PE + UMIs
            forward = re.compile(".*_R?1\.f(ast)?q(\.gz)?")
            forward_matches = forward.findall("\n".join(input_files_as_strings))
            if len(forward_matches) == len(input_files) / 3:
                # This seems right, the list is 3 times as long as
                # the number of forward read files.
                print("Input files are PE + UMIs", file=sys.stderr)
                pass
            else:
                # Not forward x 3, then maybe PE without UMIs?
                pass

        else:
            # Not divisible by 3
            pass

        if len(input_files) % 2 == 0:
            # If the length is divisible by 2, it is most likely PE
            forward = re.compile(".*_R?1\.f(ast)?q(\.gz)?")
            forward_matches = forward.findall("\n".join(input_files_as_strings))
            if len(forward_matches) == len(input_files) / 2:
                # The list of input files is twice as long as the number of
                # forward reads: reads are most likely PE
                print("Input files are PE", file=sys.stderr)
                pass
            pass

        else:
            # If not divisible by 2 or 3, it's probably SE
            print("Files do not seem to be PE, treating as SE", file=sys.stderr)
            pass


if __name__ == "__main__":
    input_files = read_input_directory(input_dir)

    infer_library_type(input_files)

    exit(0)
