# URL we're hitting - specifying YANG data model for specific interface
$uri = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1'
# Use ConvertTo-SecureString Cmdlet to create encrypted password object by specifying the plaintext password
$password = ConvertTo-SecureString 'C1sco12345' -AsPlainText -Force
# Create PSCredential object passing in the username and the encrypted password object we created above
$Cred = New-Object System.Management.Automation.PSCredential ('developer', $password)
# Specify HTTP headers - We only want YANG data back in JSON format
$headers = @{'Accept' = 'application/yang-data+json' }
# GET request passing in URI and the other things we need to pass into the HTTP headers - Basic Auth etc and don't check SSL cert
$response = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/yang-data+json' `
    -Headers $headers `
    -SkipCertificateCheck
# Result of the get request stored in the powershell object called $response
# Convert the returned object to JSON and write it to the console
$response | ConvertTo-Json | Write-Output
# Use dot notation to parse through the keys of the object - Notice the quotes as - & : are operators in powershell
$response.'Cisco-IOS-XE-interfaces-oper:interface'.name
# If the admin-status key is if-state-up then print confirmation to the console
if ($response.'Cisco-IOS-XE-interfaces-oper:interface'.'admin-status' -eq 'if-state-up') {
    Write-Host ($response.'Cisco-IOS-XE-interfaces-oper:interface'.name)'is up'
}
