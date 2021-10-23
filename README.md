# Py3Canvas

A Python 3 library for accessing the Canvas LMS API. Generated from the Canvas API specs using a template.
All requests currently return json data.

Not all of the API's have been checked, if you fix an issue in one of the generated files please submit a pul request and I will integrate your changes.

## Quickstart

```python
from py3canvas.apis import accounts
account = accounts.AccountsAPI()
account.list_accounts()
```

## Configuration

The session initialization requires you to set an environment variables in your .bashrc or .profile
```bash
export CANVAS_TOKEN={token}
export PY3CANVAS_URL={Canvas Instance URL}
```


## Update Process

I have updated the builder scripts to use Python 3 rather than Python 2.7.

### Update spec files
To update the spec files run the following command:
```commandline
$ python builder.py update-spec-files --specfile-path specs/
```

### Build API modules
single file:
```commandline
$ python builder.py build-api-from-specfile --specfile specs/late_policy.json --output-folder py3canvas/apis/
```

whole folder:
```commandline
$ python builder.py build-all-apis --specfile-path specs/ --output-folder py3canvas/apis/
```
You may get some errors, so sometimes after you have ran the generation scripts on the entire directory you will need to go back and fix individual api endpoints.
