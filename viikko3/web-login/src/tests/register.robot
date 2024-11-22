*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pdiddy
    Set Password  partylikediddyparty
    Set Password confirmation  partylikediddyparty1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  dd
    Set Password  partylikediddyparty
    Set Password confirmation  partylikediddyparty1
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 3 characters long




*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


