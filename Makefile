generate:
	podman run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/assisted-service-swagger.yaml -o /local -g python -c /local/generator-config.yaml --git-host github.com --git-user-id kincl --git-repo-id openshift-assisted-service-client-python
