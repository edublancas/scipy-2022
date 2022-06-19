**Please show your support by starring our main repo. [Click here!](https://github.com/ploomber/ploomber)**

---

# Ploomber: Developing Maintainable and Reproducible Data Pipelines Interactively From Jupyter, VSCode, and PyCharm

Facilitators: Eduardo Blancas and Ido Michael

*Please follow the setup instructions before the workshop*. If you have any issues, send us a [message on Slack](https://ploomber.io/community)


## Setup instructions

* Ensure you have a GitHub account
* Fork this repository (click on fork in the upper right button)

### Local environment setup

If using [conda](https://www.google.com/search?q=miniconda):

```sh
# create virtual env
conda create --name ploomber-workshop python=3.9 --yes

# activate env
conda activate ploomber-workshop

# install packages
pip install -r requirements.txt
```

If using `pip`:

```sh
# create virtual env
python -m venv ploomber-workshop

# activate it (if using windows, see note below)
source ploomber-workshop/bin/activate

# install packages
pip install -r requirements.txt
```

*Note:* If using Windows, the command to activate the environment is different, [click here](https://docs.python.org/3/library/venv.html) and scroll down, you'll find a table with the command to run depending on your system.


## Testing setup

To check your setup, run (it may take a few seconds):

```
python check.py
```

If everything is good, you'll see the following message:

> Everything is working correctly!

If you have any issues setting up, send us a message on our [community's](https://ploomber.io/community) `#ask-anything` channel.

## Content

See the [`instructions.md`](instructions.md) file.
