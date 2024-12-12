## OSSGadget Workflow

1. Run OSSGadget
2. Removed empty lines from output files via bash script
3. Ran gen_target_conf_og.py, using output from step 1 as input, to generate csv files

## Typomind Workflow

1. Run Typomind
2. Ran gen_target_conf_tm.py, using output from step 1 as input, to generate csv files

### Useful Scripts

`count_signals.py`: Get a count of signals in typomind and ossgadget.
`count_overlaps.py`: Get a count of typomind signal overlaps with ossgadget packages.