## reactpy-github-buttons

![](docs/showcase.png)


 Minimal [ReactPy] wrapper for [github-buttons].

## Usage

    pip install reactpy-github-buttons


## Simple  Example

*./examples/star_example.py*
```
from reactpy import component, html, run
from reactpy_github_buttons import StarButton

@component
def AppMain():
    return StarButton(user='reactive-python', repo='reactpy')


if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
```

## Building

    poetry install --no-root

    cd js
    npm install
    npm run build

## Testing

    playwright install

Then:

    pytest 

or:

    pytest --headed

## Publish 

    rm -rf dist && poetry build
    poetry publish

Or to local repo

    poetry publish -r pypicloud


[github-buttons]: https://github.com/buttons/github-buttons
[ReactPy]: https://github.com/reactive-python/reactpy