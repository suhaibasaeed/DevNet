function dosomework {
    [CmdletBinding()]
    param (
    )
    Write-Output hi

    try {
        failthis
    }
    catch {
        # There is nothing here!
    }
    write-output hi
}