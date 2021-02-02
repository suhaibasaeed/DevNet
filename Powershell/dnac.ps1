# URL we're going to hit to get the token
$url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
# First we need to login using HTTP Basic Auth so set the user name
$user = 'devnetuser'
# Use ConvertTo-SecureString Cmdlet to create encrypted password object by specifying the plaintext password
$pw = ConvertTo-SecureString 'Cisco123!' -AsPlainText -Force
# Create PSCredential object passing in the username and the encrypted password object we created above
$Cred = New-Object System.Management.Automation.PSCredential ($user, $pw)

$headers = @{'Accept' = 'application/json' }
# POST request passing in credentials, headers and don't check SSL cert
$response = Invoke-RestMethod -Uri $url `
    -Method post `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

# Convert response to JSON then print to the console
$response | ConvertTo-Json | Write-Output
# Parse the token from the response
$token = $response.token
# The URL we're hitting to get client health
$url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"
# Headers now includes the token we retrieved in the preivous step
$headers = @{
    'Accept'       = 'application/json'
    'X-auth-token' = $token
}
# Get request
$response = Invoke-RestMethod -Uri $url `
    -Method get `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck
# Parse to get to the inner data structure we want
$details = $response.response.scoreDetail
# Loop through the categories and print each category
ForEach ($detail in $details) {
    Write-Host "Object " -ForegroundColor Blue -NoNewline
    Write-Host "$($detail.scoreCategory.value)" -ForegroundColor Red
}