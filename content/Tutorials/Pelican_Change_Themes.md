Title: Changing Pelican Themes
Category: Tutorials
Tags: Pelican
Slug: changing-pelican-themes
Author: Brian Aaron
Summary: This post will guide the reader on how to install and change Pelican themes. 


This post will guide the reader on how to install and change Pelican themes. 

This post is for complete novices like myself. It is not intended for experienced users.

CD to the Scripts directory of your project and activate the virtualenv. 

```
PS C:\Users\Brian> cd virtualenvs\pelican\Scripts
PS C:\Users\Brian\virtualenvs\pelican\Scripts> .\activate
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts>
```

I tried the following commands as per the Pelican docs section 'pelican-themes'(http://docs.getpelican.com/en/3.5.0/pelican-themes.html).

(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican-themes -l
notmyidea
simple
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican-themes --list
notmyidea
simple

I have currently have two themes, 'notmyidea' and 'simple'.

Now how to install in a new theme?

I start my journey by going to http://pelican-themes-gallery.place.org/ to look at different themes. 
I decided on the pelican-bootstrap3 theme.

I then review the information on the GitHub pelican-themes [site](https://github.com/getpelican/pelican-themes).

I open Git Bash in order to clone the themes respository. I `cd` to my Users\Brian\virtualenvs\pelican directory in Git Bash. 


I then `cd` to pelican themes and enter the following to clone the respository into my directory.

```
git clone --recursive https://github.com/getpelican/pelican-themes.git
```

According to the Git [docs](http://git-scm.com/book/en/v2/Git-Tools-Submodules) the `--recursive` command, 

>If you pass --recursive to the git clone command, it will automatically initialize and update each submodule in the repository.

I highly reccomend the youtube video [Copying a GitHub Repository to Your Local Computer](https://www.youtube.com/watch?v=O72FWNeO-xY&index=7&list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD)
if you have questions about the general process of cloning a repository.

When I look at the directory in Windows Explorer, I see that under the pelican-themes folder, each theme is has a folder with its associated files.

I get a little confused here because the instructions on the Git Hub pelican-themes site differ from the pelican docs.

The Git Hub site states the following:

>To use one of the themes, edit your Pelican settings file to include this line:

```
THEME = "/home/user/pelican-themes/theme-name"
```

>So, for instance, to use the mnmlist theme, you would edit your settings file to include:

```
THEME = "/home/user/pelican-themes/mnmlist"
```

I could not find any file that resembled a Pelican settings file. 

After reviewing a couple other blogs posts, especially [http://terriyu.info/blog/posts/2013/07/pelican-setup/](http://terriyu.info/blog/posts/2013/07/pelican-setup/) 
and [http://www.circuidipity.com/pelican.html](http://www.circuidipity.com/pelican.html).
It seems the 'Pelican settings file remark' refers to the pelicanconf.py file.

Later, I see that this issue is explained in the Pelican [docs](http://docs.getpelican.com/en/3.5.0/settings.html) under the section **Settings**. The sections states:

>Pelican is configurable thanks to a settings file you can pass to the command line:

```
pelican content -s path/to/your/pelicanconf.py
```
>(If you used the `pelican-quickstart` command, your primary settings file will be named `pelicanconf.py` by default.)

After some time of playing around, I realize there are two ways to install a theme, via the command line only and via changing the `pelicanconf.py` file.

The command line option
***

As per the Pelican Themes [docs](http://docs.getpelican.com/en/3.5.0/pelican-themes.html) sections, **Installing themes** and **Listing the installed themes**,
I install a pelican theme and then use the -l command to make sure it is installed.

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican-themes --install C:\Users\Brian\virtualenvs\pelican\pel
ican-themes\pelican-bootstrap3
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican-themes -l
notmyidea
pelican-bootstrap3
simple
```

I also specify the theme directly with the -t command as per the GitHub [page](https://github.com/getpelican/pelican-themes).

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican -t pelican-bootstrap3
Done: Processed 1 article(s), 0 draft(s) and 0 page(s) in 0.67 seconds.
```

I regenerate the content and run the simple server as follows:

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> cd output
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts\output> python -m SimpleHTTPServer
```

I look on [http://localhost:8000/](http://localhost:8000/). **Success!**



Changing the pelicanconf.py file
***

I then played with variations of configuring the theme in the pelicanconf.py file such as inserting:

```
THEME = "C:/Users/Brian/virtualenvs/pelican/pelican-themes/blueidea"

```

I run the commands:

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican content
Done: Processed 0 article(s), 0 draft(s) and 4 page(s) in 1.49 seconds.
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> cd output
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts\output> python -m SimpleHTTPServer
```

I look on [http://localhost:8000/](http://localhost:8000/). **Success!**





