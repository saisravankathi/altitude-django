# Django Mock Application 

## Features

- Dashboard for Stories
- Story/ Article Detail View
- Publish Content
- Publish Story


## Django Models:

- Publisher (default email@email.com)
- Story
- Content

## Model Relationships (* indicates many associations)

- Publisher(1) Story(*)
- Story(1) Content(*)

### Further Enhancements
***It can be further integrated with Django Restframework (rest_framework) to create RestAPIs for third party Integrations***

## Dependencies
- Django - 3.0.3

## Instructions
- Install Django using
```
pip install django - (Windows)
pip3 install django - (OSX, Linux)
``` 

- execute
```
python manage.py runserver - (Windows)
python3 manage.py runsever - (OSX, Linux)
```

## Overview

- HomePage (/home)
- StoryDetailPage (/story/<story_id>)
- Publish Story (/create-story)
- Publish Content (/create-content)
- Publishing the Story and Content could be done from Admin console(/admin) 
  - Credentials:
    ***admin/nimda***
