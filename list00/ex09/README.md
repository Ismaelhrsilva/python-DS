# ft_package

A sample test package (42 Piscine Python for Data Science — module 00, ex09).

## Build

```bash
pip install build
python -m build
```

## Install

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```
