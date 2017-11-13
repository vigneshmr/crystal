.DEFAULT_GOAL := analysis

env:
	virtualenv env
	env/bin/pip install -r requirements.txt

.PHONY: analysis
analysis: env
	env/bin/ipython crystal/crystal.py
