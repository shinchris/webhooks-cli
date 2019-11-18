import argparse
import getpass
import tableauserverclient as TSC


def main():
    parser = argparse.ArgumentParser(description='Interact with Webhooks on Tableau Server.')
    parser.add_argument('action', choices=['create', 'get', 'list', 'delete'],
                        help='Action to take with Webhooks')
    parser.add_argument('--server', '-S', required=True, help='Server address')
    parser.add_argument('--site', '-s', required=True, help='Site name')
    parser.add_argument('--username', '-u', required=True, help='Username to sign into server')
    args = parser.parse_args()

    password = getpass.getpass('Password: ')

    tableau_auth = TSC.TableauAuth(args.username, password, args.site)
    server = TSC.Server(args.server, use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        print('Signed into ' + tableau_auth.site_id + '.')
        action = args.action

        if action == 'create':
            create_webhook(server)
        elif action == 'get':
            get_webhook(server)
        elif action == 'list':
            list_webhooks(server)
        elif action == 'delete':
            delete_webhook(server)


def create_webhook(server):
    webhook_name = input('Webhook name: ')
    webhook_event = input('Webhook event: ')
    destination_url = input('Destination URL: ')
    print('Creating a new webhook...')

    new_webhook = TSC.WebhookItem()
    new_webhook.name = webhook_name
    new_webhook.event = webhook_event
    new_webhook.url = destination_url

    new_webhook = server.webhooks.create(new_webhook)
    print('Successfully created a new webhook.')

    owner_name = get_owner_name(server, new_webhook.owner_id)
    print_webhook(new_webhook, owner_name)


def get_webhook(server):
    webhook_id = input('Webhook ID: ')
    print('Getting webhook ' + webhook_id + '...')

    webhook = server.webhooks.get_by_id(webhook_id)
    owner_name = get_owner_name(server, webhook.owner_id)

    print_webhook(webhook, owner_name)


def list_webhooks(server):
    print('Listing all webhooks on site...')

    all_webhooks, _ = server.webhooks.get()
    for webhook in all_webhooks:
        owner_name = get_owner_name(server, webhook.owner_id)
        print_webhook(webhook, owner_name)

    total_webhooks = len(all_webhooks)
    if total_webhooks == 1:
        print('\tThere is 1 webhook on your site.\n')
    else:
        print('\tThere are ' + str(total_webhooks) + ' webhooks on your site.\n')


def delete_webhook(server):
    webhook_id = input('Webhook ID: ')
    print('Deleting webhook ' + webhook_id + '...')

    server.webhooks.delete(webhook_id)

    print('Successfully deleted webhook ' + webhook_id + '.')


def get_owner_name(server, owner_id):
    return server.users.get_by_id(owner_id).name


def print_webhook(webhook, owner_name):
    print()
    print('\tID: ' + webhook.id)
    print('\tName: ' + webhook.name)
    print('\tEvent: ' + webhook.event)
    print('\tDestination URL: ' + webhook.url)
    print('\tOwner ID: ' + webhook.owner_id)
    print('\tOwner Name: ' + owner_name)
    print()


if __name__ == '__main__':
    main()
