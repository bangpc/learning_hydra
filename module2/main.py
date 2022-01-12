from omegaconf import OmegaConf, DictConfig
import hydra
import os
import logging
log = logging.getLogger(__name__)

@hydra.main(config_path="configs", config_name="config")
def configs(cfg: DictConfig):
    working_dir = os.getcwd()
    print(f"current working directory is {working_dir}")
    print(OmegaConf.to_yaml(cfg))

    # Read file
    # This will give error because working directory changed
    try:
        path = f"test.txt"
        with open(path, "r") as f:
            print("File 'test.txt' content:\n",f.read())
    except:
        print(f"Error because current directory is {working_dir} \n")
    
    # This will process normally
    # Apply hydra.utils.get_original_cwd()
    orig_cwd = hydra.utils.get_original_cwd()
    path = f"{orig_cwd}/test.txt"
    with open(path, "r") as f:
        print("Apply hydra.utils.get_original_cwd() \n" \
              "File 'test.txt' content:\n",f.read())
    
    # Apply hydra.utils.to_absolute_path(file_name)
    path = hydra.utils.to_absolute_path("test.txt")
    with open(path, "r") as f:
        print("Apply hydra.utils.to_absolute_path(file_name) \n" \
              "File 'test.txt' content:\n",f.read())

    log.debug("Debug level message")
    log.info("Info level message")
    log.warning("Warning level message")

if __name__=="__main__":
    configs()

