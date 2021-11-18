## AutoM00sic is (read: will be) a gr8 way to automatically check for new uploads by artists and automatically download them (on sites supported by youtube-dl. dont expect spotify intergration) 

![milked](https://cdn.discordapp.com/attachments/310843140976148482/900958098531946506/milked.png)

# commands:

add --artist --website --platform

update // look for new uploads. print out avaliable downloads. 

remove -- artist (name)

download // downloads music 

list // lists all of the artists 

setup --path (path) changes download path

example: AutoM00sic.py add --artist siouxxie --website https://soundcloud.com/siouxxie --platform soundcloud 

# TODO:

actually query sites 

youtube-dl intergration

find a way to determine what is and is not updated. perhaps a --date-last-checked param for update that checks against uploaded date on site? 

NOTES: essentially just creates a db file of artist info as of now. pretty neat, RIGHT!? 
