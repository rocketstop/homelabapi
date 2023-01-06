app_dir = "app"
api_version = "0.2.0"
api_title = "homelabapi"
api_description = "Welcome to " + api_title + "."
input_success = "Success! Your input request was accepted by " + api_title
input_failure = "Failure! Your input request was NOT accepted by " + api_title
desc_healthchecks = "Receive a POST request from HealthChecks"
desc_input = "This is the default POST endpoint. This endpoint should be used if none of the service-specific endpoints or webhooks apply."
desc_monit = "Receive a POST request from Monit"
desc_smokeping = "Receive a POST request from SmokePing"
desc_uptimerobot = "Receive a POST request from UptimeRobot"
desc_changedetectionio = "Receive a webhook from ChangeDetection.io"
desc_headphones = "Receive a webhook from Headphones"
desc_homeassistant = "Receive a webhook from Home Assistant"
desc_lazylibrarian = "Receive a webhook from LazyLibrarian"
desc_radarr = "Receive a webhook from Radarr"
desc_sonarr = "Receive a webhook from Sonarr"
desc_synology = "Receive a webhook from a Synology NAS"
desc_tailscale = "Receive a webhook from Tailscale"
subject_changedetectionio = "ChangeDetection.io"
subject_headphones = "Headphones"
subject_homeassistant = "Home Assistant"
subject_lazylibrarian = "LazyLibrarian"
subject_monit = "Monit"
subject_radarr = "Radarr"
subject_sonarr = "Sonarr"
subject_synology = "NAS"
subject_tailscale = "Tailscale"
sample_api_key = "abc123def456ghi789j0abc123def456ghi789j0"
sample_subject = "Output (" + api_title + ")"
sample_message = "This is a sample message."
sample_url = "https://example.com"
sample_priority = "1"
sample_source = "Service Name"
sample_healthchecks_name = "$NAME"
sample_healthchecks_status = "$STATUS"
sample_healthchecks_tags = "$TAGS"
sample_healthchecks_time = "$NOW"
sample_healthchecks_uuid = "$CODE"
sample_monit_action = "n/a"
sample_monit_date = "Sun, 18 Dec 20222 19:22:25"
sample_monit_description = (
    "cpu usage of 99.7% matches resource limit [cpu usage > 80.0%]"
)
sample_monit_event = "Resource limit matched"
sample_monit_host = "email.example.com"
sample_monit_process_children = "xxx"
sample_monit_process_cpu_percent = "xxx"
sample_monit_process_pid = "xxx"
sample_monit_process_memory = "xxx"
sample_monit_program_status = "xxx"
sample_monit_service = "ssh"
sample_smokeping_alertname = "hostdown"
sample_smokeping_hostname = "127.0.0.1"
sample_smokeping_losspattern = "loss: 100%"
sample_smokeping_target = "MyServerName"
sample_smokeping_rtt = "U"
sample_uptimerobot_adt = "*alertDateTime*"
sample_uptimerobot_ade = "*alertDetails*"
sample_uptimerobot_adu = "*alertDuration*"
sample_uptimerobot_at = "*alertType*"
sample_uptimerobot_atfn = "*alertTypeFriendlyName*"
sample_uptimerobot_mac = "*monitorAlertContacts*"
sample_uptimerobot_mfn = "*monitorFriendlyName*"
sample_uptimerobot_mid = "*monitorID*"
sample_uptimerobot_murl = "*monitorURL*"
sample_uptimerobot_sed = "*sslExpiryDate*"
sample_uptimerobot_sedl = "*sslExpiryDaysLeft*"
tags_metadata = [
    {
        "name": "Default Endpoint",
        "description": "",
    },
    {
        "name": "Service Endpoints",
        "description": "",
    },
    {
        "name": "Service Webhooks",
        "description": "",
    },
]
