import click
import os

# initialize click CLI app
# click is a framework that provides features to build CLI using decorators
@click.command()
def run():
    print("Hello")

if __name__ == '__main__':
    run()

def _walk_dir(dir):
    """Walk through dir and return true if
    we find a directory labelled .git, otherwise
    return false"""

    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(dir) == True:
            if filename.basename == ".git"
                return true
    return false

@click.command()
@click.option('-d', '--dir', default=".", type-str, help="Target pathh to scan")
def run(dir):
    print("Hello")