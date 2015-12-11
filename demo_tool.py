"""Demo app that takes in a variable number of input files and generates as many output files as it is asked for"""
import click


@click.command()
@click.option('--infile', multiple=True, type=click.Path(exists=True), help='Input files')
@click.option('--outfile', multiple=True, type=click.Path(), help='Output files')
def cli(infile, outfile):
  out_str = '\n'.join(infile)
  for fname in outfile:
    with open(fname, 'w') as fp:
      fp.write(out_str)
