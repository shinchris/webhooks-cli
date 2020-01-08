# webhooks-cli
CLI tool for interacting with Tableau's Webhooks. This tool is written in Python and uses [Tableau Server Client](https://github.com/tableau/server-client-python) to communicate with Tableau Server.

# Instructions
For a general guide on how to use Tableau's Webhooks, there are [instructions](instructions.md) written to guide you through the way.

For the tool itself, there are executable files located in the /dist folder for windows and macOS. The source Python script is also provided in the root level of the repository.

When you run the executable, you need to specify an action. You can choose one of the following options:
* **create** - create a new Webhook on your site by proving a name, event type, and destination server URL.
* **list** - list out all Webhooks that exist on your site.
* **get** - Get a specific Webhook by its unique ID.
* **test** - Test out a specific Webhook by its unique ID.
* **delete** - Delete a specific Webhook by its unique ID.

There are also flags you can pass in when running the executables. If these values are not passed in, you will be prompted later. Password will be prompted later.
* **--server, -S** - URL of your desired Tableau Server instance.
* **--site, -s** - name of the site on your desired Tableau Server instance.
* **--username, -u** - username used to sign into your site.

# Examples
Open up terminal (macOS) or command prompt (windows) and run the following command from the /dist directory.

For macOS with and without flags:
```
./webhooks-cli-macOS list
```
```
./webhooks-cli-macOS list -S https://10ax.online.tableau.com -s webhookdemo -u testuser@tableau.com
```
For windows with and without flags:
```
webhooks-cli-windows.exe list
```
```
webhooks-cli-windows.exe list -S https://10ax.online.tableau.com -s webhookdemo -u testuser@tableau.com
```

If you did not pass in the optional flags, you will be prompted to enter them. After you enter in valid credential values, the tool will list out all Webhooks on your site.

All actions require the four credential values. Some actions will prompt you for additional values as needed. 
