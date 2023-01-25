> *"Remember when your mom used to always asked you to clean your room?*
>
> *She probably never asked you to clean your Download folder, but you should still do it"*

A small and very simple utility to automatically clean up your folders with some simple rules.

## Usage
Write in `cleaners.yaml` the rule you want
```YAML
cleaner_name:
  path: "/path/to/folder/that/need/cleaning"
  rules:
    "Target1":
      - "pattern1"
      - "pattern2"
    "Target2":
      - "pattern3"
```

then call the cleaner:

```
python client.py clean cleaner_name
```

> <font color="red">Warning</font>: When using the same pattern for differents targets, the first occurence of the pattern will sort all matching files in its target. 
> 
> Following occurences will not match any file and thus do nothing.


TODO:
- add poetry build
- implement verify command
