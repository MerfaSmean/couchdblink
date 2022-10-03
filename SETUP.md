## setup via command-line

To use the `DEFAULT_CRED_JSON_FILE_PATH` value, it needs to be added manually because its gubbins (with username,
password, etc.) are excluded from git.

There are many (better) ways, to achieve this, but the way it's done here is based on an old habit.

With the venv of your project activated:

- `git clone https://github.com/MerfaSmean/couchdblink.git`

The cloned project tree (simplified) looks something like:

```text
    - couchdblink/
      | - .bumpversion.cfg
      | - .gitignore
      | - couchdblink/
      |   | - __init__.py
      |      
      | - setup.py
      | - tests/
      |   | - __init__.py
      |
```

Change directory to move into the project folder:

- `cd couchdblink`

From here we can install the package using:

- `pip install -e .`

Now we change directory again and create the "nogit" folder (which git will ignore)
and put some files inside:

- `cd couchdblink`
- `mkdir nogit`
- `cd nogit`
- `touch __init__.py`
- `touch cred.json`
- `touch extra_config.py`

_NOTE:_ The `touch` command might not work on Windows where
a [PowerShell equivalent](https://devcoops.com/powershell-equivalent-touch-command-linux/)
is the `sc` command.

The ameded project tree should now include the "nogit" folder containing three new files:

```text
    - couchdblink/
      | - .bumpversion.cfg
      | - .gitignore
      | - couchdblink/
      |   | - __init__.py
      |   | - nogit/
      |   |   | - __init__.py
      |   |   | - cred.json
      |   |   | - extra_config.py
      |      
      | - setup.py
      | - tests/
      |   | - __init__.py
      |
```

Inside extra_config.py:

```python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEFAULT_CRED_JSON_FILE_PATH = os.path.join(basedir, "cred.json")

```

The path value of `DEFAULT_CRED_JSON_FILE_PATH` can be to any location, as long as python will be able to read it with
the `open` context manager.

At time of writing only the url field of cred.json is being used, so that file could be:

```json
{
  "url": "https://username:password@host.address"
}
```

But this is pre-alpha stage of dev, and very likely to require more from cred.json as more functions are added.
