# Betbright challenge [![Build Status](https://travis-ci.org/pablopalacios/betbright.svg?branch=master)](https://travis-ci.org/pablopalacios/betbright) [![Coverage Status](https://coveralls.io/repos/github/pablopalacios/betbright/badge.svg?branch=master)](https://coveralls.io/github/pablopalacios/betbright?branch=master)

## Tests

### Test environment setup

This project has some test dependencies (such as pytest, coverage,
etc...). I made a Makefile to make it easier, so all you have to do is:

    make init

### Running tests

To run the tests you can also use make:

    make test

## LRU challenge

I've made a small module comparing time execution of fibonacci with
and without cache. To run it:

    make fib
