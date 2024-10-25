from mantrapy.querier.querier import API, RPC, Querier

querier = Querier(API, RPC)

account_resp = querier.get_account("mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj")
print(account_resp.account.address)
