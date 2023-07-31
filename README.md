# openshift-assisted-service-client-python
Assisted installation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/kincl/openshift-assisted-service-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kincl/openshift-assisted-service-client-python.git`)

Then import the package:
```python
import openshift_assisted_service
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openshift_assisted_service
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.EventsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to return events for. (optional)
    host_id = 'host_id_example' # str | A host in the specified cluster to return events for (DEPRECATED. Use `host_ids` instead). (optional)
    host_ids = ['host_ids_example'] # List[str] | Hosts in the specified cluster to return events for. (optional)
    infra_env_id = 'infra_env_id_example' # str | The infra-env to return events for. (optional)
    limit = 56 # int | The maximum number of records to retrieve. (optional)
    offset = 56 # int | Number of records to skip before starting to return the records. (optional)
    order = 'ascending' # str | Order by event_time of events retrieved. (optional) (default to 'ascending')
    severities = ['severities_example'] # List[str] | Retrieved events severities. (optional)
    message = 'message_example' # str | Retrieved events message pattern. (optional)
    deleted_hosts = True # bool | Deleted hosts flag. (optional)
    cluster_level = True # bool | Cluster level events flag. (optional)
    categories = ['categories_example'] # List[str] | A comma-separated list of event categories. (optional)

    try:
        api_response = api_instance.v2_list_events(cluster_id=cluster_id, host_id=host_id, host_ids=host_ids, infra_env_id=infra_env_id, limit=limit, offset=offset, order=order, severities=severities, message=message, deleted_hosts=deleted_hosts, cluster_level=cluster_level, categories=categories)
        print("The response of EventsApi->v2_list_events:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->v2_list_events: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsApi* | [**v2_list_events**](docs/EventsApi.md#v2_list_events) | **GET** /v2/events | 
*InstallerApi* | [**bind_host**](docs/InstallerApi.md#bind_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/bind | 
*InstallerApi* | [**deregister_infra_env**](docs/InstallerApi.md#deregister_infra_env) | **DELETE** /v2/infra-envs/{infra_env_id} | 
*InstallerApi* | [**download_minimal_initrd**](docs/InstallerApi.md#download_minimal_initrd) | **GET** /v2/infra-envs/{infra_env_id}/downloads/minimal-initrd | 
*InstallerApi* | [**get_cluster_supported_platforms**](docs/InstallerApi.md#get_cluster_supported_platforms) | **GET** /v2/clusters/{cluster_id}/supported-platforms | 
*InstallerApi* | [**get_infra_env**](docs/InstallerApi.md#get_infra_env) | **GET** /v2/infra-envs/{infra_env_id} | 
*InstallerApi* | [**get_infra_env_download_url**](docs/InstallerApi.md#get_infra_env_download_url) | **GET** /v2/infra-envs/{infra_env_id}/downloads/image-url | 
*InstallerApi* | [**get_infra_env_presigned_file_url**](docs/InstallerApi.md#get_infra_env_presigned_file_url) | **GET** /v2/infra-envs/{infra_env_id}/downloads/files-presigned | 
*InstallerApi* | [**get_supported_architectures**](docs/InstallerApi.md#get_supported_architectures) | **GET** /v2/support-levels/architectures | 
*InstallerApi* | [**get_supported_features**](docs/InstallerApi.md#get_supported_features) | **GET** /v2/support-levels/features | 
*InstallerApi* | [**list_cluster_hosts**](docs/InstallerApi.md#list_cluster_hosts) | **GET** /v2/clusters/{cluster_id}/hosts | 
*InstallerApi* | [**list_infra_envs**](docs/InstallerApi.md#list_infra_envs) | **GET** /v2/infra-envs | 
*InstallerApi* | [**regenerate_infra_env_signing_key**](docs/InstallerApi.md#regenerate_infra_env_signing_key) | **POST** /v2/infra-envs/{infra_env_id}/regenerate-signing-key | 
*InstallerApi* | [**register_infra_env**](docs/InstallerApi.md#register_infra_env) | **POST** /v2/infra-envs | 
*InstallerApi* | [**transform_cluster_to_adding_hosts**](docs/InstallerApi.md#transform_cluster_to_adding_hosts) | **POST** /v2/clusters/{cluster_id}/actions/allow-add-hosts | 
*InstallerApi* | [**transform_cluster_to_day2**](docs/InstallerApi.md#transform_cluster_to_day2) | **POST** /v2/clusters/{cluster_id}/actions/allow-add-workers | 
*InstallerApi* | [**unbind_host**](docs/InstallerApi.md#unbind_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/unbind | 
*InstallerApi* | [**update_infra_env**](docs/InstallerApi.md#update_infra_env) | **PATCH** /v2/infra-envs/{infra_env_id} | 
*InstallerApi* | [**v2_cancel_installation**](docs/InstallerApi.md#v2_cancel_installation) | **POST** /v2/clusters/{cluster_id}/actions/cancel | 
*InstallerApi* | [**v2_complete_installation**](docs/InstallerApi.md#v2_complete_installation) | **POST** /v2/clusters/{cluster_id}/actions/complete-installation | 
*InstallerApi* | [**v2_deregister_cluster**](docs/InstallerApi.md#v2_deregister_cluster) | **DELETE** /v2/clusters/{cluster_id} | 
*InstallerApi* | [**v2_deregister_host**](docs/InstallerApi.md#v2_deregister_host) | **DELETE** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
*InstallerApi* | [**v2_download_cluster_credentials**](docs/InstallerApi.md#v2_download_cluster_credentials) | **GET** /v2/clusters/{cluster_id}/downloads/credentials | 
*InstallerApi* | [**v2_download_cluster_files**](docs/InstallerApi.md#v2_download_cluster_files) | **GET** /v2/clusters/{cluster_id}/downloads/files | 
*InstallerApi* | [**v2_download_cluster_logs**](docs/InstallerApi.md#v2_download_cluster_logs) | **GET** /v2/clusters/{cluster_id}/logs | 
*InstallerApi* | [**v2_download_host_ignition**](docs/InstallerApi.md#v2_download_host_ignition) | **GET** /v2/infra-env/{infra_env_id}/hosts/{host_id}/downloads/ignition | 
*InstallerApi* | [**v2_download_infra_env_files**](docs/InstallerApi.md#v2_download_infra_env_files) | **GET** /v2/infra-envs/{infra_env_id}/downloads/files | 
*InstallerApi* | [**v2_get_cluster**](docs/InstallerApi.md#v2_get_cluster) | **GET** /v2/clusters/{cluster_id} | 
*InstallerApi* | [**v2_get_cluster_default_config**](docs/InstallerApi.md#v2_get_cluster_default_config) | **GET** /v2/clusters/default-config | 
*InstallerApi* | [**v2_get_cluster_install_config**](docs/InstallerApi.md#v2_get_cluster_install_config) | **GET** /v2/clusters/{cluster_id}/install-config | 
*InstallerApi* | [**v2_get_cluster_ui_settings**](docs/InstallerApi.md#v2_get_cluster_ui_settings) | **GET** /v2/clusters/{cluster_id}/ui-settings | 
*InstallerApi* | [**v2_get_credentials**](docs/InstallerApi.md#v2_get_credentials) | **GET** /v2/clusters/{cluster_id}/credentials | 
*InstallerApi* | [**v2_get_host**](docs/InstallerApi.md#v2_get_host) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
*InstallerApi* | [**v2_get_host_ignition**](docs/InstallerApi.md#v2_get_host_ignition) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/ignition | 
*InstallerApi* | [**v2_get_ignored_validations**](docs/InstallerApi.md#v2_get_ignored_validations) | **GET** /v2/clusters/{cluster_id}/ignored-validations | 
*InstallerApi* | [**v2_get_next_steps**](docs/InstallerApi.md#v2_get_next_steps) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/instructions | 
*InstallerApi* | [**v2_get_preflight_requirements**](docs/InstallerApi.md#v2_get_preflight_requirements) | **GET** /v2/clusters/{cluster_id}/preflight-requirements | 
*InstallerApi* | [**v2_get_presigned_for_cluster_credentials**](docs/InstallerApi.md#v2_get_presigned_for_cluster_credentials) | **GET** /v2/clusters/{cluster_id}/downloads/credentials-presigned | 
*InstallerApi* | [**v2_get_presigned_for_cluster_files**](docs/InstallerApi.md#v2_get_presigned_for_cluster_files) | **GET** /v2/clusters/{cluster_id}/downloads/files-presigned | 
*InstallerApi* | [**v2_import_cluster**](docs/InstallerApi.md#v2_import_cluster) | **POST** /v2/clusters/import | 
*InstallerApi* | [**v2_install_cluster**](docs/InstallerApi.md#v2_install_cluster) | **POST** /v2/clusters/{cluster_id}/actions/install | 
*InstallerApi* | [**v2_install_host**](docs/InstallerApi.md#v2_install_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/install | 
*InstallerApi* | [**v2_list_clusters**](docs/InstallerApi.md#v2_list_clusters) | **GET** /v2/clusters | 
*InstallerApi* | [**v2_list_feature_support_levels**](docs/InstallerApi.md#v2_list_feature_support_levels) | **GET** /v2/feature-support-levels | 
*InstallerApi* | [**v2_list_hosts**](docs/InstallerApi.md#v2_list_hosts) | **GET** /v2/infra-envs/{infra_env_id}/hosts | 
*InstallerApi* | [**v2_list_of_cluster_operators**](docs/InstallerApi.md#v2_list_of_cluster_operators) | **GET** /v2/clusters/{cluster_id}/monitored-operators | 
*InstallerApi* | [**v2_post_step_reply**](docs/InstallerApi.md#v2_post_step_reply) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/instructions | 
*InstallerApi* | [**v2_register_cluster**](docs/InstallerApi.md#v2_register_cluster) | **POST** /v2/clusters | 
*InstallerApi* | [**v2_register_host**](docs/InstallerApi.md#v2_register_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts | 
*InstallerApi* | [**v2_report_monitored_operator_status**](docs/InstallerApi.md#v2_report_monitored_operator_status) | **PUT** /v2/clusters/{cluster_id}/monitored-operators | 
*InstallerApi* | [**v2_reset_cluster**](docs/InstallerApi.md#v2_reset_cluster) | **POST** /v2/clusters/{cluster_id}/actions/reset | 
*InstallerApi* | [**v2_reset_host**](docs/InstallerApi.md#v2_reset_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/reset | 
*InstallerApi* | [**v2_reset_host_validation**](docs/InstallerApi.md#v2_reset_host_validation) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/reset-validation/{validation_id} | Reset failed host validation.
*InstallerApi* | [**v2_set_ignored_validations**](docs/InstallerApi.md#v2_set_ignored_validations) | **PUT** /v2/clusters/{cluster_id}/ignored-validations | 
*InstallerApi* | [**v2_update_cluster**](docs/InstallerApi.md#v2_update_cluster) | **PATCH** /v2/clusters/{cluster_id} | 
*InstallerApi* | [**v2_update_cluster_install_config**](docs/InstallerApi.md#v2_update_cluster_install_config) | **PATCH** /v2/clusters/{cluster_id}/install-config | 
*InstallerApi* | [**v2_update_cluster_logs_progress**](docs/InstallerApi.md#v2_update_cluster_logs_progress) | **PUT** /v2/clusters/{cluster_id}/logs-progress | 
*InstallerApi* | [**v2_update_cluster_ui_settings**](docs/InstallerApi.md#v2_update_cluster_ui_settings) | **PUT** /v2/clusters/{cluster_id}/ui-settings | 
*InstallerApi* | [**v2_update_host**](docs/InstallerApi.md#v2_update_host) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
*InstallerApi* | [**v2_update_host_ignition**](docs/InstallerApi.md#v2_update_host_ignition) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/ignition | 
*InstallerApi* | [**v2_update_host_install_progress**](docs/InstallerApi.md#v2_update_host_install_progress) | **PUT** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/progress | 
*InstallerApi* | [**v2_update_host_installer_args**](docs/InstallerApi.md#v2_update_host_installer_args) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/installer-args | 
*InstallerApi* | [**v2_update_host_logs_progress**](docs/InstallerApi.md#v2_update_host_logs_progress) | **PUT** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/logs-progress | 
*InstallerApi* | [**v2_upload_cluster_ingress_cert**](docs/InstallerApi.md#v2_upload_cluster_ingress_cert) | **POST** /v2/clusters/{cluster_id}/uploads/ingress-cert | 
*InstallerApi* | [**v2_upload_logs**](docs/InstallerApi.md#v2_upload_logs) | **POST** /v2/clusters/{cluster_id}/logs | 
*ManagedDomainsApi* | [**v2_list_managed_domains**](docs/ManagedDomainsApi.md#v2_list_managed_domains) | **GET** /v2/domains | 
*ManifestsApi* | [**v2_create_cluster_manifest**](docs/ManifestsApi.md#v2_create_cluster_manifest) | **POST** /v2/clusters/{cluster_id}/manifests | 
*ManifestsApi* | [**v2_delete_cluster_manifest**](docs/ManifestsApi.md#v2_delete_cluster_manifest) | **DELETE** /v2/clusters/{cluster_id}/manifests | 
*ManifestsApi* | [**v2_download_cluster_manifest**](docs/ManifestsApi.md#v2_download_cluster_manifest) | **GET** /v2/clusters/{cluster_id}/manifests/files | 
*ManifestsApi* | [**v2_list_cluster_manifests**](docs/ManifestsApi.md#v2_list_cluster_manifests) | **GET** /v2/clusters/{cluster_id}/manifests | 
*ManifestsApi* | [**v2_update_cluster_manifest**](docs/ManifestsApi.md#v2_update_cluster_manifest) | **PATCH** /v2/clusters/{cluster_id}/manifests | 
*OperatorsApi* | [**v2_list_of_cluster_operators**](docs/OperatorsApi.md#v2_list_of_cluster_operators) | **GET** /v2/clusters/{cluster_id}/monitored-operators | 
*OperatorsApi* | [**v2_list_operator_properties**](docs/OperatorsApi.md#v2_list_operator_properties) | **GET** /v2/supported-operators/{operator_name} | 
*OperatorsApi* | [**v2_list_supported_operators**](docs/OperatorsApi.md#v2_list_supported_operators) | **GET** /v2/supported-operators | 
*OperatorsApi* | [**v2_report_monitored_operator_status**](docs/OperatorsApi.md#v2_report_monitored_operator_status) | **PUT** /v2/clusters/{cluster_id}/monitored-operators | 
*VersionsApi* | [**v2_list_component_versions**](docs/VersionsApi.md#v2_list_component_versions) | **GET** /v2/component-versions | 
*VersionsApi* | [**v2_list_supported_openshift_versions**](docs/VersionsApi.md#v2_list_supported_openshift_versions) | **GET** /v2/openshift-versions | 


## Documentation For Models

 - [ApiVip](docs/ApiVip.md)
 - [ApiVipConnectivityRequest](docs/ApiVipConnectivityRequest.md)
 - [ApiVipConnectivityResponse](docs/ApiVipConnectivityResponse.md)
 - [ArchitectureSupportLevelId](docs/ArchitectureSupportLevelId.md)
 - [BindHostParams](docs/BindHostParams.md)
 - [Boot](docs/Boot.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterCreateParams](docs/ClusterCreateParams.md)
 - [ClusterDefaultConfig](docs/ClusterDefaultConfig.md)
 - [ClusterHostRequirements](docs/ClusterHostRequirements.md)
 - [ClusterHostRequirementsDetails](docs/ClusterHostRequirementsDetails.md)
 - [ClusterNetwork](docs/ClusterNetwork.md)
 - [ClusterProgressInfo](docs/ClusterProgressInfo.md)
 - [ClusterValidationId](docs/ClusterValidationId.md)
 - [CompletionParams](docs/CompletionParams.md)
 - [ConnectivityCheckHost](docs/ConnectivityCheckHost.md)
 - [ConnectivityCheckNic](docs/ConnectivityCheckNic.md)
 - [ConnectivityRemoteHost](docs/ConnectivityRemoteHost.md)
 - [ConnectivityReport](docs/ConnectivityReport.md)
 - [ContainerImageAvailability](docs/ContainerImageAvailability.md)
 - [ContainerImageAvailabilityRequest](docs/ContainerImageAvailabilityRequest.md)
 - [ContainerImageAvailabilityResponse](docs/ContainerImageAvailabilityResponse.md)
 - [ContainerImageAvailabilityResult](docs/ContainerImageAvailabilityResult.md)
 - [Cpu](docs/Cpu.md)
 - [CreateManifestParams](docs/CreateManifestParams.md)
 - [Credentials](docs/Credentials.md)
 - [DhcpAllocationRequest](docs/DhcpAllocationRequest.md)
 - [DhcpAllocationResponse](docs/DhcpAllocationResponse.md)
 - [Disk](docs/Disk.md)
 - [DiskConfigParams](docs/DiskConfigParams.md)
 - [DiskEncryption](docs/DiskEncryption.md)
 - [DiskInfo](docs/DiskInfo.md)
 - [DiskInstallationEligibility](docs/DiskInstallationEligibility.md)
 - [DiskRole](docs/DiskRole.md)
 - [DiskSkipFormattingParams](docs/DiskSkipFormattingParams.md)
 - [DiskSpeed](docs/DiskSpeed.md)
 - [DiskSpeedCheckRequest](docs/DiskSpeedCheckRequest.md)
 - [DiskSpeedCheckResponse](docs/DiskSpeedCheckResponse.md)
 - [DomainResolutionRequest](docs/DomainResolutionRequest.md)
 - [DomainResolutionRequestDomainsInner](docs/DomainResolutionRequestDomainsInner.md)
 - [DomainResolutionResponse](docs/DomainResolutionResponse.md)
 - [DomainResolutionResponseResolutionsInner](docs/DomainResolutionResponseResolutionsInner.md)
 - [DownloadBootArtifactsRequest](docs/DownloadBootArtifactsRequest.md)
 - [DriveType](docs/DriveType.md)
 - [Error](docs/Error.md)
 - [Event](docs/Event.md)
 - [FeatureSupportLevel](docs/FeatureSupportLevel.md)
 - [FeatureSupportLevelFeaturesInner](docs/FeatureSupportLevelFeaturesInner.md)
 - [FeatureSupportLevelId](docs/FeatureSupportLevelId.md)
 - [FreeNetworkAddresses](docs/FreeNetworkAddresses.md)
 - [GetSupportedArchitectures200Response](docs/GetSupportedArchitectures200Response.md)
 - [GetSupportedFeatures200Response](docs/GetSupportedFeatures200Response.md)
 - [Gpu](docs/Gpu.md)
 - [Host](docs/Host.md)
 - [HostCreateParams](docs/HostCreateParams.md)
 - [HostIgnitionParams](docs/HostIgnitionParams.md)
 - [HostNetwork](docs/HostNetwork.md)
 - [HostProgress](docs/HostProgress.md)
 - [HostProgressInfo](docs/HostProgressInfo.md)
 - [HostRegistrationResponse](docs/HostRegistrationResponse.md)
 - [HostRegistrationResponseAllOfNextStepRunnerCommand](docs/HostRegistrationResponseAllOfNextStepRunnerCommand.md)
 - [HostRole](docs/HostRole.md)
 - [HostRoleUpdateParams](docs/HostRoleUpdateParams.md)
 - [HostStage](docs/HostStage.md)
 - [HostStaticNetworkConfig](docs/HostStaticNetworkConfig.md)
 - [HostTypeHardwareRequirements](docs/HostTypeHardwareRequirements.md)
 - [HostTypeHardwareRequirementsWrapper](docs/HostTypeHardwareRequirementsWrapper.md)
 - [HostUpdateParams](docs/HostUpdateParams.md)
 - [HostValidationId](docs/HostValidationId.md)
 - [IgnitionEndpoint](docs/IgnitionEndpoint.md)
 - [IgnoredValidations](docs/IgnoredValidations.md)
 - [ImageCreateParams](docs/ImageCreateParams.md)
 - [ImageInfo](docs/ImageInfo.md)
 - [ImageType](docs/ImageType.md)
 - [ImportClusterParams](docs/ImportClusterParams.md)
 - [InfraEnv](docs/InfraEnv.md)
 - [InfraEnvCreateParams](docs/InfraEnvCreateParams.md)
 - [InfraEnvUpdateParams](docs/InfraEnvUpdateParams.md)
 - [InfraError](docs/InfraError.md)
 - [IngressVip](docs/IngressVip.md)
 - [InstallCmdRequest](docs/InstallCmdRequest.md)
 - [InstallerArgsParams](docs/InstallerArgsParams.md)
 - [Interface](docs/Interface.md)
 - [Inventory](docs/Inventory.md)
 - [IoPerf](docs/IoPerf.md)
 - [KernelArgument](docs/KernelArgument.md)
 - [L2Connectivity](docs/L2Connectivity.md)
 - [L3Connectivity](docs/L3Connectivity.md)
 - [ListVersions](docs/ListVersions.md)
 - [LogsGatherCmdRequest](docs/LogsGatherCmdRequest.md)
 - [LogsProgressParams](docs/LogsProgressParams.md)
 - [LogsState](docs/LogsState.md)
 - [LogsType](docs/LogsType.md)
 - [MacInterfaceMapInner](docs/MacInterfaceMapInner.md)
 - [MachineNetwork](docs/MachineNetwork.md)
 - [ManagedDomain](docs/ManagedDomain.md)
 - [Manifest](docs/Manifest.md)
 - [Memory](docs/Memory.md)
 - [MemoryMethod](docs/MemoryMethod.md)
 - [MonitoredOperator](docs/MonitoredOperator.md)
 - [NextStepCmdRequest](docs/NextStepCmdRequest.md)
 - [NodeLabelParams](docs/NodeLabelParams.md)
 - [NtpSource](docs/NtpSource.md)
 - [NtpSynchronizationRequest](docs/NtpSynchronizationRequest.md)
 - [NtpSynchronizationResponse](docs/NtpSynchronizationResponse.md)
 - [OpenshiftVersion](docs/OpenshiftVersion.md)
 - [OperatorCreateParams](docs/OperatorCreateParams.md)
 - [OperatorHardwareRequirements](docs/OperatorHardwareRequirements.md)
 - [OperatorHostRequirements](docs/OperatorHostRequirements.md)
 - [OperatorMonitorReport](docs/OperatorMonitorReport.md)
 - [OperatorProperty](docs/OperatorProperty.md)
 - [OperatorStatus](docs/OperatorStatus.md)
 - [OperatorType](docs/OperatorType.md)
 - [OsImage](docs/OsImage.md)
 - [Platform](docs/Platform.md)
 - [PlatformType](docs/PlatformType.md)
 - [PreflightHardwareRequirements](docs/PreflightHardwareRequirements.md)
 - [PresignedUrl](docs/PresignedUrl.md)
 - [Proxy](docs/Proxy.md)
 - [RebootForReclaimRequest](docs/RebootForReclaimRequest.md)
 - [ReleaseImage](docs/ReleaseImage.md)
 - [Route](docs/Route.md)
 - [ServiceNetwork](docs/ServiceNetwork.md)
 - [SourceState](docs/SourceState.md)
 - [Step](docs/Step.md)
 - [StepReply](docs/StepReply.md)
 - [StepType](docs/StepType.md)
 - [Steps](docs/Steps.md)
 - [SupportLevel](docs/SupportLevel.md)
 - [SystemVendor](docs/SystemVendor.md)
 - [TangConnectivityRequest](docs/TangConnectivityRequest.md)
 - [TangConnectivityResponse](docs/TangConnectivityResponse.md)
 - [TangConnectivityResponseTangServerResponseInner](docs/TangConnectivityResponseTangServerResponseInner.md)
 - [TangConnectivityResponseTangServerResponseInnerSignaturesInner](docs/TangConnectivityResponseTangServerResponseInnerSignaturesInner.md)
 - [UpdateManifestParams](docs/UpdateManifestParams.md)
 - [UpgradeAgentRequest](docs/UpgradeAgentRequest.md)
 - [UpgradeAgentResponse](docs/UpgradeAgentResponse.md)
 - [UpgradeAgentResult](docs/UpgradeAgentResult.md)
 - [Usage](docs/Usage.md)
 - [V2ClusterUpdateParams](docs/V2ClusterUpdateParams.md)
 - [VerifiedVip](docs/VerifiedVip.md)
 - [VerifyVip](docs/VerifyVip.md)
 - [VersionedHostRequirements](docs/VersionedHostRequirements.md)
 - [VipType](docs/VipType.md)
 - [VipVerification](docs/VipVerification.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="agentAuth"></a>
### agentAuth

- **Type**: API key
- **API key parameter name**: X-Secret-Key
- **Location**: HTTP header

<a id="userAuth"></a>
### userAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="urlAuth"></a>
### urlAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

<a id="imageAuth"></a>
### imageAuth

- **Type**: API key
- **API key parameter name**: Image-Token
- **Location**: HTTP header

<a id="imageURLAuth"></a>
### imageURLAuth

- **Type**: API key
- **API key parameter name**: image_token
- **Location**: URL query string


## Author



