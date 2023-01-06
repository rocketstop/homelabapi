import yaml

all_outputs = ("email", "pushbullet", "pushover", "telegram", "webhook")

with open("/code/app/config.yaml", mode="rt", encoding="utf-8") as file:
    configuration = yaml.safe_load(file)

    app_settings = configuration["application"]
    for key, value in app_settings.items():
        match key:
            case "api_name":
                api_title = value
            case "api_key":
                app_api_key = value
            case "current_outputs":
                if "," in value:
                    current_outputs = value.split(",")
                else:
                    if value == "all":
                        current_outputs = all_outputs
                    else:
                        current_outputs = [value]

    outputs = {}
    output_settings = configuration["outputs"]
    for key, value in output_settings.items():
        match key:
            case "email":
                outputs["email"] = value
            case "pushbullet":
                outputs["pushbullet"] = value
            case "pushover":
                outputs["pushover"] = value
            case "telegram":
                outputs["telegram"] = value
            case "webhook":
                outputs["webhook"] = value
