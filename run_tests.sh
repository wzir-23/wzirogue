#!/bin/sh

coverage run --source '.' -m unittest -v
coverage report -m
