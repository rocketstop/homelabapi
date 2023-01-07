from config import Config

if __name__ == "__main__":
    print('running')
    config = Config('../config.yaml.sample')
    print(config._CONFIG['application']['api_name'])
    print(config._CONFIG['outputs']['email'])
    print(config)
