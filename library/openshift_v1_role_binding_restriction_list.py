#!/usr/bin/env python

from ansible.module_utils.openshift_common import OpenShiftAnsibleModule, OpenShiftAnsibleException

DOCUMENTATION = '''
module: openshift_v1_role_binding_restriction_list
short_description: OpenShift RoleBindingRestrictionList
description:
- Retrieve a list of role_binding_restrictions. List operations provide a snapshot
  read of the underlying objects, returning a resource_version representing a consistent
  version of the listed objects.
version_added: 2.3.0
author: OpenShift (@openshift)
options:
  api_key:
    description:
    - Token used to connect to the API.
  cert_file:
    description:
    - Path to a certificate used to authenticate with the API.
    type: path
  context:
    description:
    - The name of a context found in the Kubernetes config file.
  debug:
    description:
    - Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log
    default: false
    type: bool
  force:
    description:
    - If set to C(True), and I(state) is C(present), an existing object will updated,
      and lists will be replaced, rather than merged.
    default: false
    type: bool
  host:
    description:
    - Provide a URL for acessing the Kubernetes API.
  key_file:
    description:
    - Path to a key file used to authenticate with the API.
    type: path
  kubeconfig:
    description:
    - Path to an existing Kubernetes config file. If not provided, and no other connection
      options are provided, the openshift client will attempt to load the default
      configuration file from I(~/.kube/config.json).
    type: path
  namespace:
    description:
    - Namespaces provide a scope for names. Names of resources need to be unique within
      a namespace, but not across namespaces. Provide the namespace for the object.
  password:
    description:
    - Provide a password for connecting to the API. Use in conjunction with I(username).
  resource_definition:
    description:
    - Provide the YAML definition for the object, bypassing any modules parameters
      intended to define object attributes.
    type: dict
  src:
    description:
    - Provide a path to a file containing the YAML definition of the object. Mutually
      exclusive with I(resource_definition).
    type: path
  ssl_ca_cert:
    description:
    - Path to a CA certificate used to authenticate with the API.
    type: path
  state:
    description:
    - Determines if an object should be created, patched, or deleted. When set to
      C(present), the object will be created, if it does not exist, or patched, if
      parameter values differ from the existing object's attributes, and deleted,
      if set to C(absent). A patch operation results in merging lists and updating
      dictionaries, with lists being merged into a unique set of values. If a list
      contains a dictionary with a I(name) or I(type) attribute, a strategic merge
      is performed, where individual elements with a matching I(name_) or I(type)
      are merged. To force the replacement of lists, set the I(force) option to C(True).
    default: present
    choices:
    - present
    - absent
  username:
    description:
    - Provide a username for connecting to the API.
  verify_ssl:
    description:
    - Whether or not to verify the API server's SSL certificates.
    type: bool
requirements:
- openshift == 1.0.0-snapshot
'''

EXAMPLES = '''
'''

RETURN = '''
api_version:
  type: string
  description: Requested API version
role_binding_restriction_list:
  type: complex
  returned: when I(state) = C(present)
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    items:
      description:
      - Items is a list of RoleBindingRestriction objects.
      type: list
      contains:
        api_version:
          description:
          - APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value,
            and may reject unrecognized values.
          type: str
        kind:
          description:
          - Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated. In CamelCase.
          type: str
        metadata:
          description:
          - Standard object's metadata.
          type: complex
          contains:
            annotations:
              description:
              - Annotations is an unstructured key value map stored with a resource
                that may be set by external tools to store and retrieve arbitrary
                metadata. They are not queryable and should be preserved when modifying
                objects.
              type: complex
              contains: str, str
            cluster_name:
              description:
              - The name of the cluster which the object belongs to. This is used
                to distinguish resources with same name and namespace in different
                clusters. This field is not set anywhere right now and apiserver is
                going to ignore it if set in create or update request.
              type: str
            creation_timestamp:
              description:
              - CreationTimestamp is a timestamp representing the server time when
                this object was created. It is not guaranteed to be set in happens-before
                order across separate operations. Clients may not set this value.
                It is represented in RFC3339 form and is in UTC. Populated by the
                system. Read-only. Null for lists.
              type: complex
              contains: {}
            deletion_grace_period_seconds:
              description:
              - Number of seconds allowed for this object to gracefully terminate
                before it will be removed from the system. Only set when deletionTimestamp
                is also set. May only be shortened. Read-only.
              type: int
            deletion_timestamp:
              description:
              - DeletionTimestamp is RFC 3339 date and time at which this resource
                will be deleted. This field is set by the server when a graceful deletion
                is requested by the user, and is not directly settable by a client.
                The resource is expected to be deleted (no longer visible from resource
                lists, and not reachable by name) after the time in this field. Once
                set, this value may not be unset or be set further into the future,
                although it may be shortened or the resource may be deleted prior
                to this time. For example, a user may request that a pod is deleted
                in 30 seconds. The Kubelet will react by sending a graceful termination
                signal to the containers in the pod. After that 30 seconds, the Kubelet
                will send a hard termination signal (SIGKILL) to the container and
                after cleanup, remove the pod from the API. In the presence of network
                partitions, this object may still exist after this timestamp, until
                an administrator or automated process can determine the resource is
                fully terminated. If not set, graceful deletion of the object has
                not been requested. Populated by the system when a graceful deletion
                is requested. Read-only.
              type: complex
              contains: {}
            finalizers:
              description:
              - Must be empty before the object is deleted from the registry. Each
                entry is an identifier for the responsible component that will remove
                the entry from the list. If the deletionTimestamp of the object is
                non-nil, entries in this list can only be removed.
              type: list
              contains: str
            generate_name:
              description:
              - GenerateName is an optional prefix, used by the server, to generate
                a unique name ONLY IF the Name field has not been provided. If this
                field is used, the name returned to the client will be different than
                the name passed. This value will also be combined with a unique suffix.
                The provided value has the same validation rules as the Name field,
                and may be truncated by the length of the suffix required to make
                the value unique on the server. If this field is specified and the
                generated name exists, the server will NOT return a 409 - instead,
                it will either return 201 Created or 500 with Reason ServerTimeout
                indicating a unique name could not be found in the time allotted,
                and the client should retry (optionally after the time indicated in
                the Retry-After header). Applied only if Name is not specified.
              type: str
            generation:
              description:
              - A sequence number representing a specific generation of the desired
                state. Populated by the system. Read-only.
              type: int
            labels:
              description:
              - Map of string keys and values that can be used to organize and categorize
                (scope and select) objects. May match selectors of replication controllers
                and services.
              type: complex
              contains: str, str
            name:
              description:
              - Name must be unique within a namespace. Is required when creating
                resources, although some resources may allow a client to request the
                generation of an appropriate name automatically. Name is primarily
                intended for creation idempotence and configuration definition. Cannot
                be updated.
              type: str
            namespace:
              description:
              - Namespace defines the space within each name must be unique. An empty
                namespace is equivalent to the "default" namespace, but "default"
                is the canonical representation. Not all objects are required to be
                scoped to a namespace - the value of this field for those objects
                will be empty. Must be a DNS_LABEL. Cannot be updated.
              type: str
            owner_references:
              description:
              - List of objects depended by this object. If ALL objects in the list
                have been deleted, this object will be garbage collected. If this
                object is managed by a controller, then an entry in this list will
                point to this controller, with the controller field set to true. There
                cannot be more than one managing controller.
              type: list
              contains:
                api_version:
                  description:
                  - API version of the referent.
                  type: str
                controller:
                  description:
                  - If true, this reference points to the managing controller.
                  type: bool
                kind:
                  description:
                  - Kind of the referent.
                  type: str
                name:
                  description:
                  - Name of the referent.
                  type: str
                uid:
                  description:
                  - UID of the referent.
                  type: str
            resource_version:
              description:
              - An opaque value that represents the internal version of this object
                that can be used by clients to determine when objects have changed.
                May be used for optimistic concurrency, change detection, and the
                watch operation on a resource or set of resources. Clients must treat
                these values as opaque and passed unmodified back to the server. They
                may only be valid for a particular resource or set of resources. Populated
                by the system. Read-only. Value must be treated as opaque by clients
                and .
              type: str
            self_link:
              description:
              - SelfLink is a URL representing this object. Populated by the system.
                Read-only.
              type: str
            uid:
              description:
              - UID is the unique in time and space value for this object. It is typically
                generated by the server on successful creation of a resource and is
                not allowed to change on PUT operations. Populated by the system.
                Read-only.
              type: str
        spec:
          description:
          - Spec defines the matcher.
          type: complex
          contains:
            grouprestriction:
              description:
              - GroupRestriction matches against group subjects.
              type: complex
              contains:
                groups:
                  description:
                  - Groups is a list of groups used to match against an individual
                    user's groups. If the user is a member of one of the whitelisted
                    groups, the user is allowed to be bound to a role.
                  type: list
                  contains: str
                labels:
                  description:
                  - Selectors specifies a list of label selectors over group labels.
                  type: list
                  contains:
                    match_expressions:
                      description:
                      - matchExpressions is a list of label selector requirements.
                        The requirements are ANDed.
                      type: list
                      contains:
                        key:
                          description:
                          - key is the label key that the selector applies to.
                          type: str
                        operator:
                          description:
                          - operator represents a key's relationship to a set of values.
                            Valid operators ard In, NotIn, Exists and DoesNotExist.
                          type: str
                        values:
                          description:
                          - values is an array of string values. If the operator is
                            In or NotIn, the values array must be non-empty. If the
                            operator is Exists or DoesNotExist, the values array must
                            be empty. This array is replaced during a strategic merge
                            patch.
                          type: list
                          contains: str
                    match_labels:
                      description:
                      - matchLabels is a map of {key,value} pairs. A single {key,value}
                        in the matchLabels map is equivalent to an element of matchExpressions,
                        whose key field is "key", the operator is "In", and the values
                        array contains only "value". The requirements are ANDed.
                      type: complex
                      contains: str, str
            serviceaccountrestriction:
              description:
              - ServiceAccountRestriction matches against service-account subjects.
              type: complex
              contains:
                namespaces:
                  description:
                  - Namespaces specifies a list of literal namespace names.
                  type: list
                  contains: str
                serviceaccounts:
                  description:
                  - ServiceAccounts specifies a list of literal service-account names.
                  type: list
                  contains:
                    name:
                      description:
                      - Name is the name of the service account.
                      type: str
                    namespace:
                      description:
                      - Namespace is the namespace of the service account. Service
                        accounts from inside the whitelisted namespaces are allowed
                        to be bound to roles. If Namespace is empty, then the namespace
                        of the RoleBindingRestriction in which the ServiceAccountReference
                        is embedded is used.
                      type: str
            userrestriction:
              description:
              - UserRestriction matches against user subjects.
              type: complex
              contains:
                groups:
                  description:
                  - Groups specifies a list of literal group names.
                  type: list
                  contains: str
                labels:
                  description:
                  - Selectors specifies a list of label selectors over user labels.
                  type: list
                  contains:
                    match_expressions:
                      description:
                      - matchExpressions is a list of label selector requirements.
                        The requirements are ANDed.
                      type: list
                      contains:
                        key:
                          description:
                          - key is the label key that the selector applies to.
                          type: str
                        operator:
                          description:
                          - operator represents a key's relationship to a set of values.
                            Valid operators ard In, NotIn, Exists and DoesNotExist.
                          type: str
                        values:
                          description:
                          - values is an array of string values. If the operator is
                            In or NotIn, the values array must be non-empty. If the
                            operator is Exists or DoesNotExist, the values array must
                            be empty. This array is replaced during a strategic merge
                            patch.
                          type: list
                          contains: str
                    match_labels:
                      description:
                      - matchLabels is a map of {key,value} pairs. A single {key,value}
                        in the matchLabels map is equivalent to an element of matchExpressions,
                        whose key field is "key", the operator is "In", and the values
                        array contains only "value". The requirements are ANDed.
                      type: complex
                      contains: str, str
                users:
                  description:
                  - Users specifies a list of literal user names.
                  type: list
                  contains: str
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    metadata:
      description:
      - Standard object's metadata.
      type: complex
      contains:
        resource_version:
          description:
          - String that identifies the server's internal version of this object that
            can be used by clients to determine when objects have changed. Value must
            be treated as opaque by clients and passed unmodified back to the server.
            Populated by the system. Read-only.
          type: str
        self_link:
          description:
          - SelfLink is a URL representing this object. Populated by the system. Read-only.
          type: str
'''


def main():
    try:
        module = OpenShiftAnsibleModule('role_binding_restriction_list', 'V1')
    except OpenShiftAnsibleException as exc:
        # The helper failed to init, so there is no module object. All we can do is raise the error.
        raise Exception(exc.message)

    try:
        module.execute_module()
    except OpenShiftAnsibleException as exc:
        module.fail_json(msg="Module failed!", error=str(exc))


if __name__ == '__main__':
    main()
