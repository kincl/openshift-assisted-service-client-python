generate:
	podman run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/assisted-service-swagger.yaml -o /local -g python -c /local/generator-config.yaml --git-host github.com --git-user-id kincl --git-repo-id openshift-assisted-service-client-python -t /local/.openapi-generator/templates

.PHONY: test
test:
	python3 -m venv env
	env/bin/python -m pip install flake8 pytest
	env/bin/python -m pip install -r requirements.txt

	env/bin/flake8 openshift_assisted_service --count --ignore=F821 --select=E9,F63,F7,F82 --show-source --statistics
	env/bin/flake8 openshift_assisted_service --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	env/bin/pytest
