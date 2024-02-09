This code is for research with Professor Bartholomew for weather data in several basins in Dingle, Ireland.

# Older Stuff

Procedure Used:
- Download the files as a .tsv (Tab Separated Values)
- `python fix_tsv.py -h` to see commands for fix_tsv
- `python fix_tsv.py --filein <path_to_data.tsv> --fileout <AAA.csv>`
  - This will remove the index column and remove weirdness that occurs later
  - This will convert to a .csv (Comma Separated Values), a much nicer format
- `python aggregateN.py -h` to see commands for aggregateN
    - This is the main workhorse implemented
- To fix the 5 minute intervals:
    - Rain:     `python aggregateN.py --filein <AAA.csv> --fileout <BBB.csv> --endrow 3404`
    - Not Rain: `python aggregateN.py --filein <AAA.csv> --fileout <BBB.csv> --endrow 3404 --average`
- To group into days:
    - Rain:     `python aggregateN.py --filein <BBB.csv> --fileout <CCC.csv> --startrow 52 --grouprows 144`
    - Not Rain: `python aggregateN.py --filein <BBB.csv> --fileout <CCC.csv> --startrow 52 --grouprows 144 --average`
- More is possible from here (group by weeks, months, etc) 

# Newer Stuff

Procedure Used:
- Acquire the data as a .csv file
    - If there are no "," characters in the data, export it to .csv
    - Otherwise, follow the above instructions involving `fix_tsv.py`
- Get the desired chunks of data
    - Example (10am - 2pm): `python select_range.py --filein AAA.csv --fileout BBB.csv --endcol 4 --startcol 1`
    - Example (2pm - 4pm): `python select_range.py --filein AAA.csv --fileout BBB.csv --endcol 4 --startcol 1 --startrow 169 --include 24`
        - startrow = 169 because that is the first row @ 2 pm (14:00)
        - include = 24, as there are 24 rows between 2 pm and 4 pm assuming 5 minute increments
    - For more help and commands, see the help message: `python select_range.py --help`
- Use aggregateN again on the newly produced file
    - Example (10am - 2pm): `python aggregateN.py --filein BBB.csv --fileout CCC.csv --grouprows 48`
        - Rows were grouped by 48, as this is the number of rows between 10am and 2pm
    - Example (2pm - 4pm) `python aggregateN.py --filein BBB.csv --fileout CCC.csv --grouprows 24`
    - As always, for more help and commands, see the help message: `python aggregateN.py --help`
- **Additional Notes**
    - Ensure that the time intervals are consistent within the files being used. If they are not, see the above bullet point for **fixing 5 minute intervals**.