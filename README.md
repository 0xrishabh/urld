# urld
A simple python url Decomposer


## Installing

git clone https://github.com/cYph3r1337/urld  
cd urld  
pip3 install -r requirements.txt  
python3 urld.py -h 


## Documentation 
`python3 urld.py -h`

`python3 urld.py -u "<YOUR URL> <OPTION>"` Structure of command

`python3 urld.py -u "<YOUR URL>" --hostname` to show *hostname* of the url.

`python3 urld.py -u "<YOUR URL>" --path` to show *path* part of the url.

`python3 urld.py -u "<YOUR URL>" --query` to show *query* part of the url.

`python3 urld.py -u "<YOUR URL>" --all` to show *all* parts of the url.

**urld also takes url from STDIN so, this works too**

`echo "<YOUR URL>" | python3 urld.py --all`


## Test command

`python3 urld.py -u "https://google.com/path/path2/?example=data" --all`

![shot](https://i.ibb.co/CBH6Hgm/Screenshot-from-2020-05-13-01-37-22.jpg)
