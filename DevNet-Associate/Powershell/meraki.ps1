# URL we're hitting
$url = "https://dashboard.meraki.com/api/v0/organizations"
# HTTP headers including API Key
$headers = @{
    'Accept'                 = 'application/json'
    'X-Cisco-Meraki-API-Key' = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}
# Make Get request passing in URL, headers and store it in an object called orgs
$orgs = Invoke-RestMethod -Uri $url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers
# Loop through the list of organisation and get the Organisation ID of the Org called DevNet Sandbox
ForEach ($org in $orgs) {
    If ($org.name -eq 'DevNet Sandbox') {
        $orgId = $org.id
    }
}

# Set next URL we're hitting to have the organisation ID of DevNet Sandbox - get the list of sites
$net_url = "https://dashboard.meraki.com/api/v0/organizations/$($orgId)/networks"
# Get requests using Invoke-RestMethod Cmdlet passing in same as before - Only the URL has changed
$networks = Invoke-RestMethod -Uri $net_url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers
# Loop through the sites in this organisation and find the one that is called DNSBM2 - Get the Network ID of this site
ForEach ($network in $networks) {
    If ($network.name -eq 'DNSMB2') {
        $netId = $network.id
    }
}

# Use network ID we extracted above in the next URL - we want the list of devices in this site
$devices_url = "https://dashboard.meraki.com/api/v0/networks/$($netId)/devices"
# Send get request - only URL changes
$devices = Invoke-RestMethod -Uri $devices_url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers
# Convert the output to JSON and print to console
$devices | ConvertTo-Json | Write-Output

