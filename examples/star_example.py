from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_btn import GithubButton

@component
def AppMain():


    return html.div(
        GithubButton(
            href="https://github.com/themesberg/tailwind-dashboard-windster",
            data_text="Star",
            data_size="large",
            data_show_count="true",
            data_icon="octicon-star",
            data_color_scheme='red',
            aria_label="Star tom-james-watson/p2p.chat on GitHub"
        )

    )

# python -m examples.star_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
