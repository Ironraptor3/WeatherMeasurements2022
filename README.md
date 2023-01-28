This code is for research with Professor Bartholomew for weather data in several basins in Dingle, Ireland.

Procedure Used:
- Download the files as a .tsv (Tab Separated Values)
- `python removeCol0.py -h` to see commands for removeCol0
- `python removeCol0.py --filein <path_to_data.tsv> --fileout <AAA.tsv>`
  - This will remove the index column and remove weirdness that occurs later
- `python tsvToCsv.py -h` to see commands for tsvToCsv
- `python tsvToCsv.py --filein <AAA.tsv> --fileout <BBB.csv>`
  - This will convert to a .csv (Comma Separated Values), a much nicer format
- `python aggregateN.py -h` to see commands for aggregateN
    - This is the main workhorse implemented
- To fix the 5 minute intervals:
    - Rain:     `python aggregateN.py --filein <BBB.csv> --fileout <CCC.csv> --endrow 3404`
    - Not Rain: `python aggregateN.py --filein <BBB.csv> --fileout <CCC.csv> --endrow 3404 --average`
- To group into days:
    - Rain:     `python aggregateN.py --filein <CCC.csv> --fileout <DDD.csv> --startrow 52 --grouprows 144`
    - Not Rain: `python aggregateN.py --filein <CCC.csv> --fileout <DDD.csv> --startrow 52 --grouprows 144 --average`
- More is possible from here (group by weeks, months, etc) 
