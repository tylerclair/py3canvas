# Py3Canvas

A python library for accessing the Canvas LMS API. Generated from the Canvas API specs using a template.
All requests currently return json data.

Not all of the API's have been checked, if you fix an issue in one of the generated files please submit a pul request and I will integrate your changes.

Quickstart:
```python
from py3canvas.apis import accounts
account = accounts.AccountsAPI()
account.list_accounts()
```

Configuration:
The session initialization requires you to set an environment variable in your .bashrc or .profile
```bash
export CANVAS_TOKEN={token}
```