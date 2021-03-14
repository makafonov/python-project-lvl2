# Вычислитель отличий

[![Actions Status](https://github.com/makafonov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/makafonov/python-project-lvl2/actions) [![Diff generator CI](https://github.com/makafonov/python-project-lvl2/actions/workflows/workflow.yml/badge.svg)](https://github.com/makafonov/python-project-lvl2/actions/workflows/workflow.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/04e6d64c0afc2c0a08e7/maintainability)](https://codeclimate.com/github/makafonov/python-project-lvl2/maintainability)

Вычислитель отличий – программа определяющая разницу между двумя структурами данных.

**Возможности утилиты:**

* Поддержка разных входных форматов: yaml, json

* Генерация отчета в виде plain text, stylish и json

**Пример использования:**

```bash
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```
