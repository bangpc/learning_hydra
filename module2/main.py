from omegaconf import OmegaConf, DictConfig
import hydra
import os

@hydra.main(config_path="configs", config_name="config")
def configs(cfg: DictConfig):
    working_dir = os.getcwd()
    print(f"current working directory is {working_dir}")
    print(OmegaConf.to_yaml(cfg))

if __name__=="__main__":
    configs()

