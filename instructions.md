# Introduction
Webhooks are user-defined HTTP callbacks that are triggered by specific actions taken on Tableau Server. When you create a Webhook, you need to specify a name, the event type, and the destination URL that defines where the Webhook will be sent. Whenever that event happens on Tableau Server, the Webhook will fire and send a HTTP POST request to the destination URL. The destination URL needs to be the address of some external server that will receive Webhooks from Tableau Server via HTTP POST and take some action.

You can read more about Webhooks in our [blog post](https://www.tableau.com/about/blog/2019/10/tableau-webhooks-support).

These instructions will provide you with step-by-step instructions on basics of Webhooks, including how to set them up, how to fire them, and how to integrate them into an example workflow.

***

## Module 1: Preparation
### What you will need:
1. Tableau Server - We recommend using your free **Tableau Developer Program online site**! These instructions will assume you are using your Developer Program online site, but you can also use any other Tableau Server instance, as long as it is on the 2019.4 version.
1. Postman - A free third-party application which allows us to interact with the Tableau Server [REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm). If you would rather use a CLI (command-line interface) tool to interact with the Tableau Server REST API, visit the [webhooks-cli](https://github.com/shinchris/webhooks-cli/) repository on Github for more information.
1. Webhook test site - A simple external server that will receive your Webhooks and display them to you.

### Part 1: Tableau Server
**If you have already activated your free Developer Sandbox Site or are planning on using another Tableau Server instance, then you can skip this step.**
1. Go to the Tableau Developer Program [Sandbox Site page](https://tableau.com/developer/get-site).
1. From this page, you can either sign up for a new account or sign in using your existing credentials. The sign in button is located on the top right corner of the page.
1. After you sign in, go back to the Sandbox Site page, and click the **GET SITE** button to continue.
![Get Site](/assets/Get%20Site.png)
1. You should receive an email with instructions on activating your Sandbox Site.
1. After activating the site, try signing in to your site on [Tableau Online](https://online.tableau.com).
A successful sign in should take you to the main page of your site.
![Tableau Online](/assets/Tableau%20Online.png)

### Part 2: Postman
1. You can download Postman from their [download page](https://www.getpostman.com/downloads/).
1. Open up Postman.
1. Open up the Import dialog by going to **File -> Import...**.
1. Click the **Choose Files** button and import both of the .json files you've downloaded (Tableau Collection.json and Tableau Environment.json).
![Postman Import](/assets/Postman%20Import.png)
1. After a successful import, you should be able to see the imported Collection and Environment as shown below. (If you can't see the collections panel, you may have to toggle the side bar from the bottom left corner).
![Postman Post Import](/assets/Postman%20Post%20Import.png)
1. From the **Environment** dropdown menu on the top right corner of Postman, ensure that you have **Tableau Environment** selected.

### Part 3: Webhook test site
1. Open up [https://webhook.site](https://webhook.site)
1. This is a Webhook test site, useful for testing that a Webhook fires properly. For now, you don't need to do anything on this site, but it will be used in **Module 2**.

***

## Module 2: Creating a Webhook
### Part 1: Sign in to Tableau Server
1. In Postman, click on the **Collections** tab and open up **Tableau Collection**. Then open up either the **XML** or the **JSON** folder, whichever one you prefer to use.
1. Click on the **Sign in** request to open it up in the main panel. Look through the **Body** and **Header** tabs, just below the sign in request URL to see more details. Notice the Postman variables denoted by the double curly brackets, **{{variable}}**.
1. In order to set the variables, click on the eye icon located in the top right corner of the application, right next to the **Environment** dropdown menu. In the dialog that pops up, click on the **Edit** button to edit the **Tableau Environment**.
![Postman Edit Environment](/assets/Postman%20Edit%20Environment.png)
1. In the **Manage Environments** dialog, you need to fill out the variables in the **CURRENT VALUE** column. For the sign in request, you will only need to set the username, password, the server URL, and the site name.
    - **Username**: Your email used to sign in to your Online site.
    - **Password**: Your password used to sign in to your Online site.
    - **Server**: **https://10ax.online.tableau.com**.
    - **Site-name**: Name of your site in the URL (found in browser). If your online site URL is https://10ax.online.tableau.com/#/site/mysitedev123/home, then **mysitedev123** would be your site name.
![Postman Manage Environment](/assets/Postman%20Manage%20Environment.png)
1. After you've set the 4 variables, click on the orange **Update** button located on the bottom right corner of the dialog.
1. Close the dialog and click the blue **Send** button to send the request. You should be able to see the response body on the bottom part of Postman.
    - JSON response should look something like this:
    ![JSON Signin Response](/assets/JSON%20Signin%20Response.png)
    - XML response should look something like this:
    ![XML Signin Response](/assets/XML%20Signin%20Response.png)

### Part 2: Get site-id and auth token
1. Look at the response from the sign in request and find the **site-id** and **token** values.
1. Copy the **site-id** value from the response and set the **site-id** variable.
1. Copy the **token** value from the response and set the **tableau-auth-token** variable.
![Environment](/assets/Environment.png)

### Part 3: Create a Webhook
1. Let's now fill in the next 3 variables. The last variable is for later, after we've created a Webhook.
    - **Webhook-name**: **my-webhook**
    - **Webhook-url**: URL copied from your Webhook test site from Module 1, step 3. Go to the page and make sure to click on the green **Copy** button on the top right corner of the page.
    - **Webhook-source-api-event-name**: **webhook-source-event-workbook-created**
1. After updating the variables, click on the **Create a webhook** request in the collection pane on the left.
1. We already have all the required variables set, so click the blue **Send** button to send the request.
    - JSON response should look something like this:
    ![JSON Create Response](/assets/JSON%20Create%20Response.png)
    - XML response should look something like this:
    ![XML Create Response](/assets/XML%20Create%20Response.png)
1. From the response, copy the Webhook **id** value and paste that into the last remaining environment variable, **webhook-id**.

### Part 4: (Bonus) List, Get, Delete, and Test
Congratulations on creating your very first Webhook! Now that you have a webhook created, you can use the other endpoints in the collection. Feel free to explore and try out some of these endpoints.
1. **List Webhooks**: This endpoint lets you list out all Webhooks that exist on your site. Try creating more Webhooks to get more than one result.
1. **Get a Webhook**: This endpoint lets you get a specific Webhook, by its unique id. If you have more than one Webhook, you will have to change the **webhook-id** environment variable to specify a different Webhook each time.
1. **Test a Webhook**: This endpoint lets you test out a Webhook, by its unique id. When you send this request, the Webhook will fire and you will be able to see the result in the Webhook test site!
1. **Delete a Webhook**: This endpoint lets you delete a Webhook, by its unique id. **If you use the delete endpoint, be sure to re-create a Webhook before moving on to the next module!**

***

## Module 3: Firing a Webhook
### Part 1: Creating a Workbook
1. From your browser, navigate back to your Tableau Online site.
1. Click on the **Explore** tab on the left menu panel. Then, navigate to the **Default** project.
1. Click on the **Create** button. Select **Workbook** to create a new workbook in web authoring mode.
![Create Workbook](/assets/Create%20Workbook.png)
1. In web authoring mode, select the **Superstore Datasource** and click **Connect**.
![Connect Datasource](/assets/Connect%20Datasource.png)
1. Create a simple workbook, or you can leave it blank. 
1. Save the workbook. This should trigger the Webhook you've created in the previous module!
![Save Workbook](/assets/Save%20Workbook.png)

### Part 2: Verifying your Webhook
1. From your browser, navigate back to your Webhook test site opened up in Module 1, Part 3.
1. In the body, you should be able to see the JSON response that contains more information about the event. **Tip:** Check the **Format JSON** checkbox to prettify the JSON response.
![Webhook Test Site JSON](/assets/Webhook%20Test%20Site%20JSON.png)

### Part 3: (Bonus) Changing Webhook event type
1. Workbook publish event is one of 13 events that we support today (more to come!). You can see the full list of events below.

    | Friendly Event Name | API Event Name |
    | --------- | --------- |
    | DatasourceUpdated | webhook-source-event-datasource-updated |
    | DatasourceCreated | webhook-source-event-datasource-created |
    | DatasourceDeleted | webhook-source-event-datasource-deleted |
    | DatasourceRefreshStarted | webhook-source-event-datasource-refresh-started |
    | DatasourceRefreshSucceeded | webhook-source-event-datasource-refresh-succeeded |
    | DatasourceRefreshFailed | webhook-source-event-datasource-refresh-failed |
    | WorkbookUpdated | webhook-source-event-workbook-updated |
    | WorkbookCreated | webhook-source-event-workbook-created |
    | WorkbookDeleted | webhook-source-event-workbook-deleted |
    | ViewDeleted | webhook-source-event-view-deleted |
    | WorkbookRefreshStarted | webhook-source-event-workbook-refresh-started |
    | WorkbookRefreshSucceeded | webhook-source-event-workbook-refresh-succeeded |
    | WorkbookRefreshFailed | webhook-source-event-workbook-refresh-failed |
1. Pick an event from the list above and replace the **webhook-source-api-event-name** environment variable in Postman with the corresponding value from the **API Event Name** column.
1. Send the request in Postman to create a new Webhook with the event type you have chosen.
1. Try to trigger the newly created Webhook using Tableau Desktop or Tableau Server and verify them in the Webhook test site.

***

## Module 4: (Bonus) Tableau Webhooks + Automate.io
Now that we have a Webhook created, let's take a look at how to integrate it into a third-party workflow management application. In the previous module, our destination URL was a Webhook test site that simply listed out all the Webhooks that it received. We can now replace that destination URL With Automate.io, a third-party workflow management application which allows you to integrate Tableau Webhooks with hundreds of other applications. Automate.io can be configured to listen to your Tableau Webhook and take an action on a number of applications that they support.
