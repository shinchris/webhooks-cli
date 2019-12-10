# Introduction
Webhooks are user-defined HTTP callbacks that are triggered by specific actions taken on Tableau Server. When you create a Webhook, you need to specify a name, the event type, and the destination URL that defines where the Webhook will be sent. Whenever that event happens on Tableau Server, the Webhook will fire and send a HTTP POST request to the destination URL. The destination URL needs to be the address of some external server that will receive Webhooks from Tableau Server via HTTP POST and take some action.

You can read more about Webhooks in our [blog post](https://www.tableau.com/about/blog/2019/10/tableau-webhooks-support).

These instructions will provide you with step-by-step instructions on basics of Webhooks, including how to set them up, how to fire them, and how to integrate them into an example workflow.

***

## Module 1: Preparation
### What you will need:
1. Tableau Server - We recommend using your free **Tableau Developer Program online site**! You can also use any other Tableau Server instance, as long as it is on the 2019.4 version. 
1. Postman - A free third-party application which allows us to interact with the Tableau Server [REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm). If you would rather use a CLI (command-line interface) tool to interact with the Tableau Server REST API, visit the [webhooks-cli](https://github.com/shinchris/webhooks-cli/) repository on Github for more information.
1. Webhook test site - A simple external server that will receive your Webhooks and display them to you.

### Step 1: Tableau Server
**If you have already activated your free Developer Sandbox Site or are planning on using another Tableau Server instance, then you can skip this step.**
1. Go to the Tableau Developer Program [Sandbox Site page](https://tableau.com/developer/get-site).
1. From this page, you can either sign up for a new account or sign in using your existing credentials. The sign in button is located on the top right corner of the page.
1. After you sign in, go back to the Sandbox Site page, and click the **GET SITE** button to continue.
![Get Site](/assets/Get%20Site.png)
1. You should receive an email with instructions on activating your Sandbox Site.
1. After activating the site, try signing in to your site on [Tableau Online](https://online.tableau.com).
A successful sign in should take you to the main page of your site.
![Tableau Online](/assets/Tableau%20Online.png)

### Step 2: Postman
1. You can download Postman from their [download page](https://www.getpostman.com/downloads/).
1. Open up Postman
