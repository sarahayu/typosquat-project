## OSSGadget Workflow

1. Ran run_og.py
2. Removed empty lines from output files via bash script
3. Ran gen_target_conf_og.py, using output from step 1 as input, to generate csv files
4. Ran remove_populars_og.py, using output from step 3 as input, to remove squat candidates considered popular