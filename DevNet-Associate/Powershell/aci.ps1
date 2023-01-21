# URL we're hitting to get the token
$url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"
# The payload we're passing is PS structured object with the username and password in it. Has nested sub-objects
$payload = @{
    aaaUser = @{
        attributes = @{
            name = "admin"
            pwd  = "ciscopsdt"
        }
    }
}
# Accept only a JSON response back
$headers = @{'Accept' = 'application/json' }
# Make POST request specifying the URL, payload converted to JSON, headers and store the returned token as Session variable s
$response = Invoke-RestMethod -Uri $url `
    -Method post `
    -Body ($payload | ConvertTo-Json) `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s
# Print token to the console - We actually don't need to do anything with it
Write-Host "Token: " -ForegroundColor Red -NoNewline
Write-Host $response.imdata.aaaLogin.attributes.token
# URL we're hitting to get application profile - We walk through the ACI managed object tree structure
$uri = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-common/monepg-default.json"
# Websession uses session that was created before via s object - Due to this we don't need to pass token back in to this request
# Powershell automatically converts returned JSON to powershell object
$ap = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -Websession $s
# Print to the console with formatting
Write-Host "App: " -ForegroundColor Red
Write-Host $ap.imdata.monEPGPol.attributes