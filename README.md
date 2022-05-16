[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

Intention is to use: [![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pep.databio.org/en/latest/) and [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Simple portable metagenomics

This project aims to make taxonomic profiling for metagenomics simple.
The goal is to build a workflow for short-read shotgun metagenomics
input files (mainly from Illumina sequencing machines) that
automatically detects whether files are single-end, paired-end
or paired-end with unique molecular identifiers (UMIs) and
then process those data using [mOTUs](https://github.com/motu-tool/mOTUs),
convert the output to an R [phyloseq](https://joey711.github.io/phyloseq/index.html)
object and make some stacked bar charts of the taxonomic profiles.

Ideally, the user can download this workflow from this page
and run it with a single command to do taxonomic profiling
of metagenomics files in a given directory and be ready for
further processing in [R](https://www.r-project.org/).

## Development

The workflow is currently under development.
The following steps have been planned:

1. Create test data to work with
2. Create a PEP file that specifies the required and optional
workflow parameters.
3. Write a script that generates a sample sheet based
on an input directory.
4. Implement [pytest](https://docs.pytest.org/) to verify correct
functioning of the scripts.
5. Write a [snakemake]()
workflow that imports the PEP file and handles the processing of
the data.
    - write separte rules files that are imported depending on the
     specified configuration parameters (in the PEP file)
6. Write R-script to convert mOTUs output to phyloseq object
7. Connect sample sheet and phyloseq scripts to snakemake workflow

When all of that is ready and works, maybe I'll add more
functionality.
Perhaps another taxonomic profiler, such as 
[MetaPhlAn 3](https://huttenhower.sph.harvard.edu/metaphlan)?
Or support for deduplication of reads prior to analysis using the new
functionality in [fastp](https://github.com/OpenGene/fastp) version 0.22+?
