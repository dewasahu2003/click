# Use a pipeline as a high-level helper
from transformers import pipeline
import click
from colorama import Fore


# to get the version of package
@click.command()
@click.option("--ver", is_flag=True, default=True)
def version(ver):
    if ver:
        click.echo(Fore.GREEN + "0.1.7")


# to generate
@click.command()
@click.option("--text", type=click.STRING, help="generate text from sentence")
def generate(text):
    model = pipeline("text-generation", model="gpt2")
    output = model(text)
    click.echo("-" * 100)
    print(Fore.GREEN +output[0]["generated_text"])


@click.group()
def main():
    pass


main.add_command(version)
main.add_command(generate)


if __name__ == "__main__":
    main()
