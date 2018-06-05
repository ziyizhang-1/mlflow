# MLflow Website

This is the website for the MLflow project, built on an open source Jekyll theme called [Hydra](https://github.com/CloudCannon/hydra-jekyll-template).

# Building

Use the `bundle` command to run jekyll commands 

And when you're building to push to production use:

`JEKYLL_ENV=production bundle exec jekyll build`

...this will ensure that the sitemap and robots.txt is built correctly and that the google analytics snippet gets inserted into the pages.

# Develop

Hydra was built with [Jekyll](http://jekyllrb.com/) version 3.3.1, but should support newer versions as well.


Run `jekyll` commands through Bundler to ensure you're using the right versions:

~~~bash
$ bundle exec jekyll serve
~~~

## Building Docs
check out mlflow-prototype (or the post-release project whatever that's called), then go into docs and run make.

Copy over the html docs to the docs/directory and poing latest at it.

the redeploy


# Jekyll Theme Attribution

This site was built on the MIT licensed Jekyll Hydra theme

Hydra was made by [CloudCannon](http://cloudcannon.com/), the Cloud CMS for Jekyll.

