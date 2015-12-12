"""Demo app that takes in a CSV file of inputs and metadata and produces a single output text file of the same. For
testing"""
import csv
import json

import click


def process(row, header):
  return {k: v for k, v in zip(header, row)}


@click.command()
@click.argument('csvfile', type=click.Path(exists=True))
@click.option('--outfile', type=click.Path(), help='Output file')
def cli(csvfile, outfile):
  """Demo app that takes in a CSV file of inputs and metadata and produces a single output text file of the same.
  For testing.
  The format of the CSV is (first line is the header):

  \b
  File1, File2, Meta1, Meta2
  f1, f2, m1, m2
  .....
  """
  data = [row for row in csv.reader(open(csvfile, 'r'), skipinitialspace = True)]
  header = data[0]
  rows = [process(row, header) for row in data[1:]]
  json.dump(rows, open(outfile, 'w'), indent=2)


if __name__ == '__main__':
  cli()