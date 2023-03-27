function dosomework {
    [CmdletBinding()]
    param (
    )
    Write hi

    try {
        failthis
    }
    catch {
        # There is nothing here!
    }
    write-output hi
}