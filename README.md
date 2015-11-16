# Do It Live!

## Description
Take either urly bird or fredslist and push it live to heroku.

## Learning Objectives
* Understanding good production practices
* Be able to push a system live
* Understand how to treat sensitive information in settings files
* Logging

## Details

### Requirements
* Working and live on Heroku
* Can serve static assets

### Deliverables
* README.md including the below
	* URL to the working site
	* Examples of custom logging statements
* No system files (.direnv, .envrc)

### Normal Mode
Pick either urly bird or fred's list then make sure that it can run on heroku.  This should include:
* No sensitive data including secret key, database information, api keys/ids
* Must be able to serve static assets live
* Web app should have appropraite error pages for 400s and 500s
* Must have useful logging of some sort.  Pick at least 3 logging statements that can be seen in `heroku logs`

### Hard Mode
* Dump the data from your local system and import it on live
