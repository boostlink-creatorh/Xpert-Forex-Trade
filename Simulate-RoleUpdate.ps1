param (
  [string]$UserId,
  [string]$Role
)

$allowedRoles = @("admin", "contributor", "viewer")
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if (-not $allowedRoles -contains $Role) {
  Write-Host "? [$timestamp] Invalid role: '$Role'. Allowed roles: $($allowedRoles -join ', ')"
  exit 1
}

$functionUrl = $env:SUPABASE_FUNCTION_URL
$slackWebhook = $env:SLACK_WEBHOOK_URL

if (-not $functionUrl) {
  Write-Host "?? [$timestamp] Missing SUPABASE_FUNCTION_URL environment variable."
  exit 1
}

$payload = @{ user_id = $UserId; role = $Role } | ConvertTo-Json -Compress

try {
  $response = Invoke-RestMethod -Uri $functionUrl -Method Post -Body $payload -ContentType "application/json"
  Write-Host "? [$timestamp] Role update simulated: $($response.message)"
} catch {
  Write-Host "? [$timestamp] API call failed: $($_.Exception.Message)"
  exit 1
}

if ($slackWebhook) {
  try {
    $slackPayload = @{ text = "?? Role update test: $UserId ? $Role ($timestamp)" } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri $slackWebhook -Method Post -Body $slackPayload -ContentType "application/json"
    Write-Host "?? [$timestamp] Slack notification sent."
  } catch {
    Write-Host "?? [$timestamp] Slack notification failed: $($_.Exception.Message)"
  }
}
