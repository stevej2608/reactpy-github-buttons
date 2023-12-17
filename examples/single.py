from reactpy import component, run
from reactpy_github_buttons import StarButton

@component
def AppMain():
    return StarButton(user="buttons", repo="github-buttons", large=True, standard_icon=True, show_count=True)

# python -m examples.single_button

if __name__ == "__main__":
    run(AppMain)
