## A few tips on how to manage this site

### Writing a new article

```
Title: Example
Slug: an-example
Date: 2019-05-21
Accroche: First example
image: /images/example/image.jpg
Author: Antoine

## Title

### Header

Do not use # Title as the title is already specified above. Use ## Header only.

Here is how to add a picture:
![Alt text photo "photo title"](/images/example/image.jpg){: .image .center}

.center can also be .left or .right.

HTML tags are supported.

Do not use an HTML tag right after a header. Leave a blank line in between.

To add a video, just copy paste the provided <iframe></iframe>.

text text text text text text text text text text text text text text text text
text text text text text text text text text text text text text text text

- list
- list
- list

*italic*
```

### Submiting an article

Commit a markdown file to /content/articles/

### Update leaflet

Download a new version, extract it to content/assets/. Keep only leaflet.js,
leaflet.css, leaflet.js.map and images/

### Update plugins

Copy from from https://github.com/pelican-plugins

### TODO

- Add support for <meta name=description" content="" /> in the theme
- Remove unused css
- Update theme
- Update plugin/include_assets.py to
  https://github.com/getpelican/pelican-plugins/tree/master/assets ?

### Make test

When running `make test`, connect to http://127.0.0.1:8000/

