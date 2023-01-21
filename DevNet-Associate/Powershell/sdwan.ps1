# URL we need to hit to get the cookie back
$url = 'https://sandboxsdwan.cisco.com:8443/j_security_check'
# The body will NOT be JSON but an object with the credentials
$login_body = @{
    j_username = 'devnetuser'
    j_password = 'Cisco123!'
}

$headers = @{'Accept' = 'application/json' }
# POST request with payload as normal object and store the returned token as Session variable s
#$response = `
Invoke-RestMethod -Uri $url `
    -Method post `
    -Body ($login_body) `
    -ContentType 'application/x-www-form-urlencoded' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s

# Get a list of all the vEdges
$uri = 'https://sandboxsdwan.cisco.com:8443/dataservice/device'
# Websession uses session that was created before via s object - Due to this we don't need to pass token back in to this request
$devs = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -Websession $s

Write-Host "Output!!!!!!!"
# Parse to get to inner data structure
$devices = $devs.data
# Loop through the list of devices and print to console
ForEach ($device in $devices) {
    write-host $device
}