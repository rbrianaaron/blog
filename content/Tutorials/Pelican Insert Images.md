Title: Insert Images in Your Pelican Page
Category: Tutorials
Tags: pelican, markdown
Slug: insert-images-in-your-pelican-page
Author: Brian Aaron
Summary: Learn to insert an image in your pelican page.

I thought it looked easy enough in the Pelican docs [articles-and-pages](http://docs.getpelican.com/en/3.5.0/content.html#articles-and-pages) section **Linking to static files** section.

I placed two `.png` images in the following directory:

```
C:\Users\Brian\virtualenvs\pelican\Scripts\content\images
```

I inserted the following scipt in my markdown file.

`
![Alt Text]({filename}/images/output.png)
`

When that didn't work, I tried:

`
![Alt Text]({filename}C:Users/Brian/virtualenvs/pelican/Scripts/content/images/output.png)
`

Here are the errors I got:

```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican content
WARNING: Unable to find `/images/output.png`, skipping url replacement.
WARNING: Unable to find `/images/first.png`, skipping url replacement.
Done: Processed 2 article(s), 0 draft(s) and 0 page(s) in 2.97 seconds.
```
```
(pelican) PS C:\Users\Brian\virtualenvs\pelican\Scripts> pelican content
WARNING: Unable to find `c:Users/Brian/virtualenvs/pelican/Scripts/content/images/output.png`, skipping url replacement.

WARNING: Unable to find `c:Users/Brian/virtualenvs/pelican/Scripts/content/images/first.png`, skipping url replacement.
Done: Processed 2 article(s), 0 draft(s) and 0 page(s) in 2.29 seconds.

```

It's tough to be a novice. Okay, let's try and figure out what I was really suppossed to do.

I look at the [docs](http://docs.getpelican.com/en/3.5.0/content.html#articles-and-pages) section **Linking to static files** again. 
I was supposed to ensure that the `STATIC_PATHS` setting in the `pelicanconf.py` file includes images, for example:

```
STATIC_PATHS = ['images']
```

I make the correction and generate the content again. I get the same error.

I review the [Writing Content docs](http://docs.getpelican.com/en/3.5.0/content.html) again, especially the following section in **Linking to static files**:

>For example, a project’s content directory might be structured like this:
```
content
+-- images
¦   +-- han.jpg
+-- pdfs
¦   +-- menu.pdf
+-- pages
    +-- test.md
```
I realize that my directory does not contain a pages folder. I add a pages folder and regenerate the page.

**Success!**


As I continue to play with directory structures, I discover that the above directory structure is not optimum. 

The Pelican Writing Content [docs](http://docs.getpelican.com/en/3.5.0/content.html?highlight=category) section **Articles and pages** states:

>Pelican considers “articles” to be chronological content, such as posts on a blog, and thus associated with a date.

>The idea behind “pages” is that they are usually not temporal in nature and are used for content that does not change very often (e.g., “About” or “Contact” pages)

I corrected my structure to include three directories under the content directory: images, pages, and Tutorials. Here the Tutorials serves as category under which
I'll put my articles.  
