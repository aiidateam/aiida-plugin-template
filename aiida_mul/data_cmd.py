import click
import sys

@click.group()
def parameters():
    """Command line interface for MultiplyParameters nodes"""
    pass

@parameters.command()
def list():
    """Output all MultiplyParameters nodes"""
    from aiida import is_dbenv_loaded, load_dbenv
    if not is_dbenv_loaded():
        load_dbenv()

    from aiida.orm.querybuilder import QueryBuilder
    from data import MultiplyParameters

    qb = QueryBuilder()
    qb.append(MultiplyParameters)
    results = qb.all()

    vsep = '\t'

    s = ""
    for result in results:
        obj = result[0]
        s += "{}, pk: {}\n".format(str(obj), obj.pk)
    sys.stdout.write(s)
