from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
rpc_cn = AuthServiceProxy("http://jp:plaza@127.0.0.1:9050")

"""
ZCash wallet using RPC
----------------------
Features:
[0] : Address generation (t and z)
[1] : List addresses (t and z)
[2] : Send zcash
[3] : Receive zcash (t and z)
[4] : Show transactions
[5] : Show balance
"""

# type Address = String
# data AddressType = "t" | "z" :: String

# Main
def main():
    menu()
    select_choice()

# Print the menu of options
def menu():
    print("ZyCash Wallet Menu")
    print("----------------------------")
    print("[0] : Address generation")
    print("[1] : List addresses")
    print("[2] : Send ZCash")
    print("[3] : Receive ZCash")
    print("[4] : Show transactions")
    print("[5] : Show balance")

# User select choice from menu
def select_choice():
    user_choice = input("Select an option: ")
    if (user_choice == "0"):
        gen_address_first()
    elif (user_choice == "1"):
        list_addresses_first()
    elif (user_choice == "2"):
        send_first()
    elif (user_choice == "3"):
        receive_first()
    elif (user_choice == "4"):
        show_tx_first()
    elif (user_choice == "5"):
        get_balance_first()
    else:
        print("Input not recognized")
        select_choice()

def error_input():
    print("Input not recognized")
    main()


# [0] : Address generation (t and z - by default it is z)
"""
add_type = "t" | "z" :: String
"""
def gen_address(add_type="z"):
    if (add_type == "z"):
        add = rpc_cn.z_getnewaddress("sapling")
        print("New z-address: %s" %(add))
    else:
        add = rpc_cn.getnewaddress()
        print("New t-address: %s" %(add))

def gen_address_first():
    add_type = input("Address type (t or z): ")
    if (add_type in ["t","z"]):
        gen_address(add_type)
    else:
        error_input()


# [1] : List addresses (by default show all, or specify t or z)
"""
add_type :: Maybe AddressType
"""
def list_addresses(add_type=None):
    print("Addresses:")
    print("----------------------------")
    if (not add_type):
        add_z = rpc_cn.z_listaddresses()
        list_add_t = rpc_cn.listreceivedbyaddress(1,True)
        add_t = [list_add_t[k]["address"] for k in range(len(list_add_t))]
        for address in (add_z+add_t):
            print(address)
            print("----------------------------")

def list_addresses_first():
    add_type = input("Address type (t or z): ")
    if (add_type in ["t","z", ""]):
        list_addresses(add_type)
    else:
        error_input()


"""
Address the zcash is being sent from
add_from :: Address
(Address, Amount) output addresses and amounts
add_to :: [(Address, Float)]
Change address (if specified)
change :: Maybe Address
"""
def send(add_from, add_to, change=None):
    print("send")

def send_first():
    add_from = input("Address from: ")
    add_to = input("Address to: ")
    change = input("Change address (return if default): ")

    if (is_valid(add_from) and is_valid(add_to) and is_valid(change)):
        send()
    else:
        error_input()


# [3] : Receive zcash (t and z), new="yes" if new address generated, "no" if use existing address
"""
new = "yes" | "no" :: String
"""
def receive(new="yes"):
    if (new == "yes"):
        return gen_address("z")
    elif (new == "no"):
        return list_addresses

def receive_first():
    new = input("Generate new address ('y' or 'n'): ")
    if (new in ["y","n"]):
        receive(new)
    else:
        error_input()


# [4] : Show transactions
"""
Show transaction belonging to one address (or all addresses if None)
add :: Maybe Address
"""
def show_tx(add=None):
    print("show_tx")

def show_tx_first():
    add = input("Address for transactions (or 'all'): ")
    if (add == "all"):
        show_tx()
    elif (is_valid(add)):
        show_tx(add)
    else:
        error_input()


# [5] : Show balance
"""
Show transaction belonging to one address (or all addresses if None)
add :: Maybe Address
"""
def get_balance(add=None):
    print("get_balance")

def get_balance_first():
    add = input("Address for transactions (or 'all'): ")
    if (add == "all"):
        show_tx()
    elif (is_valid(add)):
        get_balance(add)
    else:
        error_input()

# Check whether given address is valid
def is_valid(add):
    if (add == ""):
        return True
    else:
        return True


# Run
main()
