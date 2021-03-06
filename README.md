# pip-boilerplate

deploy python package with ease

## run Test

```sh

python setup.py test

```

## install

```sh
pip install .

```

## deploy

first make deploy_venv and install twine(deploy tool)

```sh
virtualenv deploy_venv -p python3
source deploy_venv/bin/activate
pip install twine

```

build and upload
```sh
python setup.py sdist bdist_wheel

twine upload dist/boilerplate-version.tar.gz

```

## Example Usage

### on command line

```sh
boiler login --id='adam' --password='smith'
boiler single_print --string='hello world'
boiler multi_print --string="hello" --string="world"

```

### on python code

```python
import boilerplate
boilerplate.login('adam', 'smith')

```

