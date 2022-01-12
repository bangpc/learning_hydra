## Understanding Hydra setup process
#  Simple example:
   Run 'python main.py'
   Output:
       current working directory is {$PATH}/learning_hydra/module2/outputs/2022-01-12/14-58-30
       dataset:
         image:
           size: 124
           channels: 3
       classes: 10

   Explaination:
     + omegaconf is installed by default with hydra. It is only used to provide the type annotation for cfg argument in func.
     + @hydra.main(config_path="config", config_name="config") This is the main decorator function that is used when any function requires contents from a configuration file.
     + Current working directory is changed. main.py exists in {$PATH}/learning_hydra/module2/main.py but the output shows the current working directory is {$PATH}/learning_hydra/module2/outputs/2022-01-12/14-58-30. This is the most important point when using Hydra. An explanation follows below.

   How hydra handles different runs:
     + Whenever a program is executed using python main.py Hydra will create a new folder in outputs directory with the following naming scheme outputs/YYYY-mm-dd/HH-MM-SS i.e. the date and time at which the file was executed
	```
	module2/
	├── .README.md.swp
	├── configs/
	│   └── config.yaml
	├── main.py
	├── outputs/
	│   └── 2022-01-12/
	│       ├── 16-48-20/
	│       │   ├── .hydra/
	│       │   │   ├── config.yaml
	│       │   │   ├── hydra.yaml
	│       │   │   └── overrides.yaml
	│       │   └── main.log
	├── README.md
	└── test.txt
	```
       When you run module2/main.py, hydra moves this file to module2/outputs/2022-01-12/15-03-57/main.py and then runs it. This means if your main.py relied on some external file, say test.txt, then you would have to use ../../../test.txt instead, as you are no longer running the program in module2 directory. This also means that everything you save to disk would be saved relative to module2/outputs/2022-01-12/15-03-57/
     
     + Hydra provides two utility functions to handle this situation:
        hydra.utils.get_original_cwd(): Get the original current working directory
	hydra.utils.to_absolute_path(file_name)

     + Content of each subfolder:
	16-48-20/
	├── .hydra/
	│   ├── config.yaml
	│   ├── hydra.yaml
	│   └── overrides.yaml
	└── main.log
	
	config.yaml - Copy of the config file passed to the function (It doesn't matter if you pass foo.yaml, this file would still be named config.yaml)
	hydra.yaml - Copy of the hydra config file. 
	overrides.yaml - Copy of any argument that you provide through the command line and which changes one of the default value would be stored here
	main.log - Output of the logger would be stored here, this only show Info and Warning. If you want to include Debug also, then override hydra.verbose=true in config or using command (i.e. python main.py hydra.verbose=true)
