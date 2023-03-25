# imgtaggen

Simple script to generate a long list of html &lt;img> tags

By default this script will include all gifs, pngs, webps, and jpgs and output the tags into a file
called `_tags.txt`

## What is this used for?

If you want to have a page containing hundreds of images but don't want to write each &lt;img&gt;
tag by hand, you can use this simple script to do this for you.

## Editing the script

You can exclude or include file types by simply adding or removing extentions from the tuple called
`IMAGE_TYPES`:

```python
IMAGE_TYPES = ('.png', '.gif', '.jpeg', '.jpg', '.webp', '.jfif')
```

You can also simply change the name of the output file by editing the `TAGS_FILE` variable:

```python
TAGS_FILE = '_tags.txt'
```

