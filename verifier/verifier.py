import steem as stm
from steembase.base58 import Base58
from steembase.transactions import SignedTransaction


class Verifier:
    """
    Verifier Class.
    """

    # Verifier()
    def __init__(self, node="https://steemd.privex.io", key_prefix="STM"):
        """
        Verifier init method.

        :param node: Custom node to connect to.
        :param key_prefix:  Public key prefix (STM on Steem).
        """
        # assign the client instance using the custom node.
        steem_client = stm.Steem(nodes=[node])
        # assign steemd as client on
        self.client = steem_client.steemd
        # assign the chain params.
        self.chain = self.client.chain_params
        # assign the public key prefix.
        self.key_prefix = key_prefix

    # Verifier().find_transaction
    def find_transaction(self, transaction_id):
        """
        Transaction finder method

        :param transaction_id: Transaction ID to find.
        :return: Transaction data (when found).
        """
        # find the transaction data from the api client.
        transaction_data = self.client.get_transaction(transaction_id)
        # transaction = SignedTransaction(transaction_data)
        return transaction_data

    # Verifier().get_public_keys
    def get_public_keys(self, transaction_data):
        """
        Extract public keys from the transaction signatures.

        :param transaction_data: The transaction data to extract the keys from.
        :return: List of public keys used to sign a the transaction.
        """
        # creates a signed transaction instance.
        transaction = SignedTransaction(transaction_data)

        # start a public keys array.
        public_keys = []

        # find all public keys matching the transaction signatures.
        for key in transaction.verify(chain=self.chain):
            # convert each key to Base58, with the current chain prefix (STM)
            public_keys.append(self.key_prefix + str(Base58(data=key)))

        # finally return the list of public keys.
        return public_keys

    def get_key_owners(self, public_keys):
        """
        Get the public key owners (or candidates when collision).

        :param public_keys: List of public keys to find the owners.
        :return: List of possible owners for each key.
        """
        # extract the public key owners
        owners = self.client.get_key_references(public_keys)

        # return the owners / candidates list.
        return owners
