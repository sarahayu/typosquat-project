## OSSGadget Workflow

1. Ran process_popular_csv.py
2. Removed empty lines from output files via bash script
3. Ran gen_target_conf.py, using output from step 1 as input, to generate csv files
4. Ran remove_populars.py, using output from step 3 as input, to remove squat candidates considered popular