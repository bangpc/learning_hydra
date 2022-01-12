## Understanding Hydra setup process
1. Simple example:
   Run 'python main.py'
   Output:
       current working directory is {$PATH}/learning_hydra/module2/outputs/2022-01-12/14-58-30
       dataset:
         image:
           size: 124
           channels: 3
       classes: 10

   Explaination:
       omegaconf is installed by default with hydra. It is only used to provide the type annotation for cfg argument in func.
       @hydra.main(config_path="config", config_name="config") This is the main decorator function that is used when any function requires contents from a configuration file.
       Current working directory is changed. main.py exists in {$PATH}/learning_hydra/module2/main.py but the output shows the current working directory is {$PATH}/learning_hydra/module2/outputs/2022-01-12/14-58-30. This is the most important point when using Hydra. An explanation follows below.

2. 
