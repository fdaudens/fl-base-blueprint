FRONTLINE base
==============

This is a base blueprint for FRONTLINE Tarbell projects. This is here to be forked, though it can be used directly.

What's here:

- `_sccs`: Basic styles common to all projects. This will get copied into your project root when you start a new project. Add new `scss` files to the version in your project, not in the blueprint.
- `config.rb`: SASS configuration, also copied into the root project
- `css/base.css`: Generated file from `_scss/base.scss`, which will get you started. You'll probably override this.
- `font`: Common fonts for FRONTLINE

Template files:

- `_base.html`: basic structure of a project
- `_footer.html`: source, credits, end notes
- `_nav.html`: standard nav
- `_ad-tile.html`: because it has to be included on most projects
- `index.html`: this gets copied into your project
