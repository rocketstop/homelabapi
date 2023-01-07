import yaml
import os
from pydantic import BaseModel

all_outputs = ("email", "pushbullet", "pushover", "telegram", "webhook")


class Config(object):
    _CONFIG_FILE: str = None
    _CONFIG: dict = None

    # def __new__(cls, config_file: str):
    #     """ Singleton """
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Config, cls).__new__(cls)
    #     return cls.instance

    def __init__(self, config_file: str = None):
        super().__init__()

        if config_file is None:
            config_file = Config.get_env_var("CONFIG_FILE")

        assert os.path.exists(config_file)
        print('loading ')
        configuration: dict = Config.configuration_from_yaml(config_file)
        self._CONFIG = configuration

    @staticmethod
    def configuration_from_yaml(filename="config.yml") -> dict:
        with open(filename, mode="rt", encoding="utf-8") as file:
            configuration = yaml.safe_load(file)

        return configuration

    @staticmethod
    def get_env_var(envvar: str) -> str:
        if envvar not in os.environ:
            raise Exception("Please set the {envvar} environment variable")
        return os.environ[envvar]

            # app_settings = configuration["application"]
            # for key, value in app_settings.items():
            #     match key:
            #         case "api_name":
            #             api_title = value
            #         case "api_key":
            #             app_api_key = value
            #         case "current_outputs":
            #             if "," in value:
            #                 current_outputs = value.split(",")
            #             else:
            #                 if value == "all":
            #                     current_outputs = all_outputs
            #                 else:
            #                     current_outputs = [value]
            #
            # outputs = {}
            # output_settings = configuration["outputs"]
            # for key, value in output_settings.items():
            #     match key:
            #         case "email":
            #             outputs["email"] = value
            #         case "pushbullet":
            #             outputs["pushbullet"] = value
            #         case "pushover":
            #             outputs["pushover"] = value
            #         case "telegram":
            #             outputs["telegram"] = value
            #         case "webhook":
            #             outputs["webhook"] = value
