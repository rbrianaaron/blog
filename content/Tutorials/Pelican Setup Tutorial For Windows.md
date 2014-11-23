Title: Pelican Setup Tutorial for Windows
Category: Tutorials
Tags: Pelican
Slug: pelican-setup-tutorial-windows
Author: Brian Aaron
Summary: A tutorial to create a skeleton Python Pelican project from installing a Python virtualenv and Pelican, to Pelican quickstart, to previewing the first test page.

The Pelican documentation for installing Pelican, while well written, does not include specific information for Windows users. For the experienced, this may not be a problem and this post is not for them.
This post is for novices, like myself. I hope it helps. 

This post will show the reader how to create a Pelican skeleton project from installing the virtualenv and Pelican to previewing the first test page.

**Note** This post assumes that you have installed Python, setuptools, pip, and virtualenv.

The Pelican documents recommend the following commands for installing Pelican in a virtualenv:

```
virtualenv ~/virtualenvs/pelican
CD ~/virtualenvs/pelican
source bin/activate
```

In Windows Powershell, I ran the first line and received the following feedback:

```
PS C:\Python27> virtualenv ~/virtualenvs/pelican
New python executable in ~/virtualenvs/pelican\Scripts\python.exe
Installing setuptools, pip...done.
```

However, the directory was not made in the home directory. The directory was located at:

```
C:\Python27\~\virtualenvs\pelican
```

Let's try again with the following commands in Windows Powershell:

```
PS C:\Users\Brian> virtualenv virtualenvs/pelican
New python executable in virtualenvs/pelican\Scripts\python.exe
Installing setuptools, pip...done.
```

The directory is now in `C:\Users\Brian\virtualenvs\pelican`.

I then moved to the pelican directory to run the `source bin/activate` command which resulted in the following error:

```
PS C:\Users\Brian\virtualenvs\pelican> source bin/activate
source : The term 'source' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ source bin/activate
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (source:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

The [virtualenv docs](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) section **activate script**
and its **!Note** section for Windows users explains how to change the execution policies to allow Windows to activate 
the environment. 

Here are the commands that I used along with errors I received along the way:

```
PS C:\> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
http://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
Set-ExecutionPolicy : Access to the registry key
'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied. To change the execution
policy for the default (LocalMachine) scope, start Windows PowerShell with the "Run as administrator" option. To
change the execution policy for the current user, run "Set-ExecutionPolicy -Scope CurrentUser".
At line:1 char:1
+ Set-ExecutionPolicy RemoteSigned
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.SetExecutionPolicyComma
   nd
PS C:\> Set-ExecutionPolicy -Scope CurrentUser

cmdlet Set-ExecutionPolicy at command pipeline position 1
Supply values for the following parameters:
ExecutionPolicy: RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
http://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

PS C:\Users\Brian\virtualenvs\pelican\Scripts> .\activate
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts>
```

Now, I can now pip install Pelican:

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pip install pelican
```

I will also install the two optional packages, Markdown and Typogrify.

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pip install Markdown

(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pip install typogrify
```

I will now try to run the pelican-quickstart command. My intention is to place the blog on my github page, so I answered those questions as yes. 

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican-quickstart
Welcome to pelican-quickstart v3.5.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? rbrianaaron
> Who will be the author of this web site? rbrianaaron
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) N
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at C:\Users\Brian\virtualenvs\pelican\Scripts
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts>
```

The Pelican docs show this 'hierarchy':

```
yourproject/
+-- content
¦   +-- (pages)
+-- output
+-- develop_server.sh
+-- fabfile.py
+-- Makefile
+-- pelicanconf.py       # Main settings file
+-- publishconf.py       # Settings to use when ready to publish
```

I expected to see something similar on my computer screen (I am a novice after all). I did not. However, when I reviewed the directory in 
Windows explorer, I did note that each of the items, in addition to many others, is listed in the Scripts folder, and they were the most recently created.

I read the next section of the documentation [Writing Content](http://docs.getpelican.com/en/3.5.0/content.html) , but I felt intimidated, so 
I returned to [Quickstart](http://docs.getpelican.com/en/3.5.0/quickstart.html), section **Create an Article**. 

I used NotePad and saved a file with a .md extension to `C:\Users\Brian\virtualenvs\pelican\Scripts\content`. 
The file contained:

```
Title: My First Page
Date: 2014-11-12 8:36
Category: Stuff

Following is my first page.
```

I then ran the `pelican` command as instructed under the **Generate your site** section.

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican content
Done: Processed 1 article(s), 0 draft(s) and 0 page(s) in 0.90 seconds.
```

Note. If the virtualenv is not activated and you run this command you will get the following error:

```
PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican content
Pelican : The term 'pelican' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pelican content
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (pelican:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command pelican was not found, but does exist in the current location. Windows PowerShell do
es not load commands from the current location by default. If you trust this command, instead type ".\pelican". See "get
-help about_Command_Precedence" for more details.
```

Rerun the command as follows:

```
PS C:\Users\Brian\virtualenvs\pelican\Scripts> .\pelican content
Done: Processed 1 article(s), 0 draft(s) and 0 page(s) in 4.85 seconds.
PS C:\Users\Brian\virtualenvs\pelican\Scripts>
```

I looked into the content folder and saw the following:

![Alt Text]({filename}../images/output.png)

As per **Preview your site** section of the [Quickstart](http://docs.getpelican.com/en/3.5.0/quickstart.html) page, 
I changed directories to my **output** directory and ran the following command:

```
PS C:\Users\Brian\virtualenvs\pelican\Scripts\output> python -m SimpleHTTPServer
```

The result was:

```
Serving HTTP on 0.0.0.0 port 8000 ...
127.0.0.1 - - [12/Nov/2014 09:10:55] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [12/Nov/2014 09:10:56] "GET /theme/css/main.css HTTP/1.1" 200 -
127.0.0.1 - - [12/Nov/2014 09:10:56] "GET /theme/css/reset.css HTTP/1.1" 200 -
127.0.0.1 - - [12/Nov/2014 09:10:56] "GET /theme/css/pygment.css HTTP/1.1" 200 -
127.0.0.1 - - [12/Nov/2014 09:10:56] "GET /theme/css/typogrify.css HTTP/1.1" 200 -
127.0.0.1 - - [12/Nov/2014 09:10:56] code 404, message File not found
127.0.0.1 - - [12/Nov/2014 09:10:56] "GET /favicon.ico HTTP/1.1" 404 -
```
 
On the [http://localhost:8000/](http://localhost:8000/) site in my web browser, I found:

![Alt Text]({filename}../images/first.png)

**__Success!__**

**Lesson Learned**