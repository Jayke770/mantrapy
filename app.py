import cosmpy
from mnemonic import Mnemonic
from cosmpy.aerial.client import LedgerClient, NetworkConfig, Address
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey

networkConfig = NetworkConfig(
    chain_id="mantra-dukong-1",
    faucet_url=None,
    fee_denomination="uom",
    staking_denomination="uom",
    url="rest+https://api.dukong.mantrachain.io",
    fee_minimum_gas_price=0,
)
ledger_client = LedgerClient(networkConfig)

mnemonic = (
    "tooth general spread logic junk believe update uncover trash special major paddle"
)
receiver = Address("mantra15vu32m33t4flneamm9n07syfzjzkfex95vjegv")
wallet = LocalWallet.from_mnemonic(mnemonic, "mantra")
print(wallet.address())
print(ledger_client.query_bank_all_balances(receiver))
