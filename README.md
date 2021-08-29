# imgtaggen

Simple script to generate a long list of html &lt;img> tags

By default this script will include all gifs, pngs, and jpgs and output the tags into a file called `_tags.txt`

## What is this used for?

If you want to have a page containing hundreds of images but don't want to write each <img> tag by hand, you can use this simple script to do this for you.

## Editing the script

You can exclude or include file types by simply adding or removing extentions from the tuple called "imageTypes":

`imageTypes = ('.png', '.gif', '.jpeg', '.jpg', '.PNG', '.GIF', '.JPEG', '.JPG')`

You can also simply change the name of the output file by editing the "txt" variable:

`txt = '_tags.txt'`
