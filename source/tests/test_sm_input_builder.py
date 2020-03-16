from manifest.sm_input_builder import InputBuilder, SCPResourceProperties, \
    StackSetResourceProperties
from utils.logger import Logger
logger = Logger('info')

# declare SCP state machine input variables
name = "policy_name"
description = "policy_description"
policy_url = "https://s3.amazonaws.com/bucket/prefix"
account_id = "account_id_1"
policy_list = []
operation = "operation_id"
ou_list = [
    [
        "ou_name_1",
        "Attach"
    ],
    [
        "ou_name_2",
        "Attach"
    ]
]
delimiter = ":"

# declare Stack Set state machine input variables
stack_set_name = "StackSetName1"
template_url = "https://s3.amazonaws.com/bucket/prefix"
parameters = {"Key1": "Value1",
              "Key2": "Value2"}
capabilities = "CAPABILITY_NAMED_IAM"
account_list = ["account_id_1",
                "account_id_2"]
region_list = ["us-east-1",
               "us-east-2"]
ssm_parameters = {
    "/ssm/parameter/store/key": "value"
}


def build_scp_input():
    # get SCP output
    resource_properties = SCPResourceProperties(name, description, policy_url,
                                                policy_list, account_id,
                                                operation, ou_list, delimiter)
    scp_input = InputBuilder(resource_properties.get_scp_input_map())
    return scp_input.input_map()


def build_stack_set_input():
    # get stack set output
    resource_properties = StackSetResourceProperties(
        stack_set_name, template_url, parameters,
        capabilities, account_list, region_list,
        ssm_parameters)
    ss_input = InputBuilder(resource_properties.get_stack_set_input_map())
    return ss_input.input_map()


def test_scp_input_type():
    # check if returned input is of type dict
    scp_input = build_scp_input()
    assert isinstance(scp_input, dict)


def test_scp_resource_property_type():
    # check if resource property is not None
    scp_input = build_scp_input()
    assert isinstance(scp_input.get("ResourceProperties"), dict)


def test_request_type_value():
    # check the default request type is create
    scp_input = build_scp_input()
    assert scp_input.get("RequestType") == "Create"


def test_stack_set_input_type():
    # check if returned input is of type dict
    stack_set_input = build_stack_set_input()
    assert isinstance(stack_set_input, dict)


def test_ss_resource_property_type():
    # check if resource property is not None
    stack_set_input = build_stack_set_input()
    assert isinstance(stack_set_input.get("ResourceProperties"), dict)


def test_ss_request_type_value():
    # check the default request type is create
    stack_set_input = build_stack_set_input()
    assert stack_set_input.get("RequestType") == "Create"
