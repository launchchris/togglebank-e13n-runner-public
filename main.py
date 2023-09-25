import ldclient
from ldclient.config import Config
import names
import random
import time
import uuid
from utils.user_regions import random_region


def create_random_ld_user():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    plan = random.choice(["free", "silver", "gold"])
    customer_group = random.choice(
        ["low connection", "medium connection", "high connection"])
    email = first_name + "." + last_name + \
        random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])
    region = random_region()
    device_type = random.choice(["ios", "android", "web"])

    user = {
        "key": str(uuid.uuid4()),
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "region": region,
        "plan": plan,
        "customerGroup": customer_group,
        "deviceType": device_type,
        "convertedInFunnel": "false"
    }
    return user


def trades_made():
    possible_trades = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4,
                       4, 5, 6, 7]  # put numbers in list for easy weighting
    number_of_trades = random.choice(possible_trades)
    return number_of_trades


def main():
    print("Beginning Experiment Runner.")
    users_in_iteration = 4000  # REMEMBER: Not all users who flag will convert on button
    # ToggleBank metrics
    metric_cta_conversion = "cta-conversion"  # CTA Conversion in LD
    metric_traded_on_cta = "traded-on-cta"
    metric_num_trades = "number-of-trades-made"
    flag_name = "investment-trading-button-e13n-demo"
    sdk_key = input(
        "Hello! Please type in your SDK Key, and then press 'return' or 'Enter'")
    ldclient.set_config(Config(sdk_key))

    for i in range(users_in_iteration):

        random_user = create_random_ld_user()
        flag_variation = ldclient.get().variation(flag_name, random_user, False)

        # here we only initialize the flag, to represent users not converting
        if i < 1483:
            continue

        # for users that convert on Get Started now variation
        if flag_variation == "Get Started":
            if i < 3400:  # these users drop out of 'funnel'
                ldclient.get().track(metric_cta_conversion, random_user)
                continue

        # for users that convert on learn now variation
        else:
            if i < 3000:  # these users drop out of 'funnel'
                ldclient.get().track(metric_cta_conversion, random_user)
                continue

        # for users that converted, and did not drop out of funnel
        random_user.update({"convertedInFunnel": "true"})
        number_of_trades = trades_made()
        ldclient.get().track(metric_cta_conversion, random_user)
        ldclient.get().track(metric_traded_on_cta, random_user)
        ldclient.get().track(metric_num_trades, random_user, metric_value=number_of_trades)
    # close the client, flush the events
    ldclient.get().close()
    time.sleep(10)  # wait 10 seconds, just to make sure data settles
    print("Iteration one complete. Please stop this iteration in LD, and start a new one.")
    while True:
        awaiting_input = input(
            "Please type Y and press return or Enter to proceed with Iteration 2.")
        if awaiting_input == "Y":
            break
########################
# Iteration Two
########################

    i = 0
    ldclient.set_config(Config(sdk_key))
    for i in range(users_in_iteration):

        random_user = create_random_ld_user()
        flag_variation = ldclient.get().variation(flag_name, random_user, False)

        # here we only initialize the flag, to represent users not converting
        if i < 1783:
            continue

        # for users that convert on Get Started now variation
        if flag_variation == "Trade Now":
            if i < 2000:  # these users drop out of 'funnel'
                ldclient.get().track(metric_cta_conversion, random_user)
                continue

        # for users that convert on learn now variation
        else:
            if i < 3000:  # these users drop out of 'funnel'
                ldclient.get().track(metric_cta_conversion, random_user)
                continue

        # for users that converted, and did not drop out of funnel
        number_of_trades = trades_made()
        random_user.update({"convertedInFunnel": "true"})
        ldclient.get().track(metric_cta_conversion, random_user)
        ldclient.get().track(metric_traded_on_cta, random_user)
        ldclient.get().track(metric_num_trades, random_user, metric_value=number_of_trades)
    # close the client, flush the events
    time.sleep(10)  # wait 10 seconds, just to make sure data settles
    ldclient.get().close()
    print("Iteration two complete. Happy toggling!")


if __name__ == "__main__":
    main()
