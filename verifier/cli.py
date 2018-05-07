import argparse
from .verifier import Verifier


def parse_arguments():
    """
    Command line argument parser.
    """
    # argument parsed main help message.
    parser = argparse.ArgumentParser(description='Verify Steem transaction signatures.')

    # includes the transaction argument.
    parser.add_argument('transaction',
                        help='The transaction ID (hex) to verify the signatures.')

    # includes a custom rpc node argument.
    parser.add_argument('--node',
                        required=False,
                        default="https://steemd.privex.io",
                        help="HTTPS RPC node to connect, defaults to https://steemd.privex.io")

    # parse the command line arguments.
    args = parser.parse_args()

    # returns the parsed arguments.
    return args


def entry():
    """
    Command line entry point.
    """
    # parse the command line arguments.
    arguments = parse_arguments()

    # creates a verifier instance (with a custom RPC node).
    verifier = Verifier(node=arguments.node)

    # get the transaction id from arguments.
    transaction_id = arguments.transaction

    # find the transaction data by the transaction id.
    print("=> Retrieving transaction...")
    transaction_data = verifier.find_transaction(transaction_id)

    # extract the public keys from the transaction.
    print("\n=> Extracting public keys...")
    public_keys = verifier.get_public_keys(transaction_data)

    # print the public keys extract.
    print("\n=> Extracted public keys are:")
    for public_key in public_keys:
        print(public_key)

    # find the possible owners for the public keys.
    print("\n=> The accounts who signed the transaction (public key owners) are:")
    owners = verifier.get_key_owners(public_keys=public_keys)

    # print the possible owners (a public key may be used on multiple accounts).
    for owner in owners:
        print(' or '.join(str(candidate) for candidate in owner))
