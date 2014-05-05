#!/bin/bash

find . -name "*.pyc" | xargs rm
find . -name "*.beam" | xargs rm

exit $?

