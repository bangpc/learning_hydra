import torch
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="configs", config_name="config.yaml")
def get_dataset(cfg: DictConfig):
    name_of_dataset = cfg.dataset.name
    num_samples = cfg.num_samples
    
    if name_of_dataset == "dataset1":
        feature_size = cfg.dataset.feature_size
        x = torch.randn(num_samples, feature_size)
        print(x.shape)
        return x

    elif name_of_dataset == "dataset2":
        dim1 = cfg.dataset.dim1
        dim2 = cfg.dataset.dim2
        x = torch.randn(num_samples, dim1, dim2)
        print(x.shape)
        return x

    else:
        raise ValueError("You outplayed the developer")

if __name__ == "__main__":
    get_dataset()
