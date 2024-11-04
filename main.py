from master.txbuilder.builder import TxBuilder
from master.wallet.wallet import wallet_from_mnemonic

mnemonic = (
    "tooth general spread logic junk believe update uncover trash special major paddle"
)
wallet = wallet_from_mnemonic(mnemonic)
builder = TxBuilder(wallet, is_testnet=True)
body, auth, sign_doc = builder.bank_send(
    "mantra1wf2eqtltm35tc5dllhp9uuzy66qvuwhve7zzgr", 1, "uom"
)
resp = builder.broadcast_tx(body, auth, builder.sign_message(sign_doc))
print(resp)