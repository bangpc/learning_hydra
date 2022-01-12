from omegaconf import OmegaConf
conf = OmegaConf.load('config.yaml')

# Accessing values (dot notation or dictionary notation)
print("channels: ",conf.dataset.image.channels)
print("classes before: ",conf['dataset']['classes'])

# Modifying a value
conf.dataset.classes = 15

print("classes after modified: ",conf['dataset']['classes'])
