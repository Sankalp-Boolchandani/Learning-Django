Self notes:
  - Always add the app as soon as you create it in the setting .py to register it. Why? So that the apps are integrated/mapped correctly in django
  - Urls.py: all the related routing
  - views.py: all the logics are written in views.py
  - templates: htmls that are rendered using views
  - context: **used in views.py**, helps us to send backend data to the templates(html pages), in html pages the data can be rendered using double curly brackets.(-{{data}}-)
  - base-template: a common template for all the html pages with the required data to avoid writing same code multiple times. DRY(dont repeat yourself). Done using block tag 