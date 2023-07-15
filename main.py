# Use a pipeline as a high-level helper
from transformers import pipeline
import click


class Config:
    def __init__(self) -> None:
        self.verbose = False


@click.group()
@click.option("--ver", is_flag=True)
def tell(ver):
    if ver:
        click.echo("0.1.5")


verbose_decorator = click.make_pass_decorator(Config, ensure=True)


@click.group()
@verbose_decorator
@click.option("--string", help="tell2 text input", type=str)
def tell2(config, string):
    click.echo("hello from tell2")
    config.hello = string


@click.command()
@click.option("--version", is_flag=True, default=True, help="tell version of package")
@verbose_decorator
def get_version(config, version):
    if version:
        click.echo(config.hello)
        click.echo("0.1.6")
    else:
        pass


@click.command()
@click.option("--text", type=click.STRING, help="generate text from sentence")
def summaries(text):
    # model = pipeline("text-generation", model="gpt2")
    output = [
        {
            "generated_text": text
            + "the model is very large so doing hardcoding to understand"
        }
    ]
    print("-" * 20)
    print(output[0]["generated_text"])


@click.command()
@click.option("--text", type=click.STRING, help="generate text from sentence")
@click.option("--is_curious", default=False, help="want the model to be more curious")
def curious(is_curious, text):
    if is_curious:
        model = pipeline("text-generation", model="gpt2")
        output = model(text + "fill my curiosity")
        print("-" * 20)
        print(output[0]["generated_text"])


tell.add_command(summaries)
tell.add_command(curious)
tell2.add_command(get_version)


@click.group()
def main():
    pass


main.add_command(tell)
main.add_command(tell2)
main.add_command(get_version)

if __name__ == "__main__":
    main()
