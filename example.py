import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    name = "emilio"
    return (name,)


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _(name):
    print(name)
    return


if __name__ == "__main__":
    app.run()
