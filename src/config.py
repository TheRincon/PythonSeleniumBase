import yaml

class Config:
  __conf = yaml.load(open("../config/cfg.yml", 'r'), Loader=yaml.FullLoader)
  __setters = ["database", "browser"]

  @staticmethod
  def get(name):
    return Config.__conf[name]

  @staticmethod
  def set(name, value):
    if name in Config.__setters:
      Config.__conf[name] = value
    else:
      raise NameError("Name not accepted in set() method")
