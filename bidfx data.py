"""
This code is a very simple processor for finding arbitrage opportunities in the exchange of GBP for USD. Unfortunately 
I learned Python today so I was unable to take into account effects such as execution time, slippage, market impact etc.
In further development this model could be easily extended to cover other currency pairs or even triplets (eg. buy Euros with dollars, buy pounds with euros, buy dollars with pounds)
"""

import pandas as pd
import numpy as np

def data_process(path):
    data = pd.read_csv(path)
#    date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")
    return data

GBPUSD_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_1/21sep-tick (1)/GBPUSD.csv")

"""
USDCAD_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_1/21sep-tick (1)/USDCAD.csv")

USDJPY_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_1/21sep-tick (1)/USDJPY.csv")

BTCUSD_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_2/21sep-tick (2)/BTCUSD.csv")

EURCAD_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_2/21sep-tick (2)/EURCAD.csv")

EURGBP_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_2/21sep-tick (2)/EURGBP.csv")

EURUSD_tick = data_process("C:/Users/Henry Jones/OneDrive/Documents/Durhack/BidFX Data/21sep-tick_2/21sep-tick (2)/EURUSD.csv")
"""

#print(pd.unique(GBPUSD_tick.loc[:,"Bank"]))

pd. set_option('mode.chained_assignment', None)


GBPUSD_df = pd.DataFrame(np.array([[0,0,0,0,0,0,0,0,0,0,0, 0, 0]]), columns = ['Time', 'Max Sell', 'Min Buy', 'BofA_B', 'BofA_S', 'HSBC_B', 'HSBC_S', 'Barc_B', 'Barc_S', 'Jeff_B', 'Jeff_S', 'DB_B', 'DB_S'])        

arb_count = 0

for i in range(0, len(GBPUSD_tick)):#len(GBPUSD_tick)
    Time = GBPUSD_df["Time"].iloc[-1]
    BofA_B = GBPUSD_df["BofA_B"].iloc[-1]
    BofA_S = GBPUSD_df["BofA_S"].iloc[-1]
    HSBC_B = GBPUSD_df["HSBC_B"].iloc[-1]
    HSBC_S = GBPUSD_df["HSBC_S"].iloc[-1]
    Barc_B = GBPUSD_df["Barc_B"].iloc[-1]
    Barc_S = GBPUSD_df["Barc_S"].iloc[-1]
    Jeff_B = GBPUSD_df["Jeff_B"].iloc[-1]
    Jeff_S = GBPUSD_df["Jeff_S"].iloc[-1]
    DB_B = GBPUSD_df["DB_B"].iloc[-1]
    DB_S = GBPUSD_df["DB_S"].iloc[-1]
    
    if GBPUSD_tick["Timestamp"].iloc[i] == Time or i == 0:
        
        if GBPUSD_tick["Bank"].iloc[i] == "BankOfAmerica":
            GBPUSD_df["BofA_B"].iloc[-1] = GBPUSD_tick["Buy price"].iloc[i]
            GBPUSD_df["BofA_S"].iloc[-1] = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].loc[i] == "HSBC":
            GBPUSD_df["HSBC_B"].iloc[-1] = GBPUSD_tick["Buy price"].iloc[i]
            GBPUSD_df["HSBC_S"].iloc[-1] = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "Barclays":
            GBPUSD_df["Barc_B"].iloc[-1] = GBPUSD_tick["Buy price"].iloc[i]
            GBPUSD_df["Barc_S"].iloc[-1] = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "Jeffries":
            GBPUSD_df["Jeff_B"].iloc[-1] = GBPUSD_tick["Buy price"].iloc[i]
            GBPUSD_df["Jeff_S"].iloc[-1] = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "DeutscheBank":
            GBPUSD_df["DB_B"].iloc[-1] = GBPUSD_tick["Buy price"].iloc[i]
            GBPUSD_df["DB_S"].iloc[-1] = GBPUSD_tick["Sell price"].iloc[i]
    else:
        if GBPUSD_df["Max Sell"].iloc[-1] > GBPUSD_df["Min Buy"].iloc[-1] and GBPUSD_df["Min Buy"].iloc[-1] != 0:
            if GBPUSD_df["BofA_S"].iloc[-1] == GBPUSD_df["Max Sell"].iloc[-1]:
                sell_opt = "BofA"
            elif GBPUSD_df["HSBC_S"].iloc[-1] == GBPUSD_df["Max Sell"].iloc[-1]:
                sell_opt = "HSBC"
            elif GBPUSD_df["Barc_S"].iloc[-1] == GBPUSD_df["Max Sell"].iloc[-1]:
                sell_opt = "Barc"
            elif GBPUSD_df["Jeff_S"].iloc[-1] == GBPUSD_df["Max Sell"].iloc[-1]:
                sell_opt = "Jeff"
            elif GBPUSD_df["DB_S"].iloc[-1] == GBPUSD_df["Max Sell"].iloc[-1]:
                sell_opt = "DB"
            
            if GBPUSD_df["BofA_B"].iloc[-1] == GBPUSD_df["Min Buy"].iloc[-1]:
                buy_opt = "BofA"
            elif GBPUSD_df["HSBC_B"].iloc[-1] == GBPUSD_df["Min Buy"].iloc[-1]:
                buy_opt = "HSBC"
            elif GBPUSD_df["Barc_B"].iloc[-1] == GBPUSD_df["Min Buy"].iloc[-1]:
                buy_opt = "Barc"
            elif GBPUSD_df["Jeff_B"].iloc[-1] == GBPUSD_df["Min Buy"].iloc[-1]:
                buy_opt = "Jeff"
            elif GBPUSD_df["DB_B"].iloc[-1] == GBPUSD_df["Min Buy"].iloc[-1]:
                buy_opt = "DB"

            print("Arbitrage at time " + str(Time) + ": Spread = " + str(GBPUSD_df["Max Sell"].iloc[-1]-GBPUSD_df["Min Buy"].iloc[-1]) + "     Buy from " + buy_opt + " for " + str(GBPUSD_df["Min Buy"].iloc[-1]) + "   Sell to " + sell_opt + " for " + str(GBPUSD_df["Max Sell"].iloc[-1]))
            arb_count +=1
        
        if GBPUSD_tick["Bank"].iloc[i] == "BankOfAmerica":
            BofA_B = GBPUSD_tick["Buy price"].iloc[i]
            BofA_S = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "HSBC":
            HSBC_B = GBPUSD_tick["Buy price"].iloc[i]
            HSBC_S = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "Barclays":
            Barc_B = GBPUSD_tick["Buy price"].iloc[i]
            Barc_S = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "Jeffries":
            Jeff_B = GBPUSD_tick["Buy price"].iloc[i]
            Jeff_S = GBPUSD_tick["Sell price"].iloc[i]
        elif GBPUSD_tick["Bank"].iloc[i] == "DeutscheBank":
            DB_B = GBPUSD_tick["Buy price"].iloc[i]
            DB_S = GBPUSD_tick["Sell price"].iloc[i]
            
        
        new_data = {
            "Time": [GBPUSD_tick["Timestamp"].iloc[i]], 
            "BofA_B": [BofA_B],
            "BofA_S": [BofA_S],
            "HSBC_B": [HSBC_B],
            "HSBC_S": [HSBC_S],
            "Barc_B": [Barc_B],
            "Barc_S": [Barc_S],
            "Jeff_B": [Jeff_B],
            "Jeff_S": [Jeff_S],
            "DB_B": [DB_B],
            "DB_S": [DB_S]
            }
        new_row = pd.DataFrame(new_data)
        GBPUSD_df = pd.concat([GBPUSD_df, new_row], ignore_index=True)
    GBPUSD_df["Max Sell"].iloc[-1] = max(GBPUSD_df["BofA_S"].iloc[-1], GBPUSD_df["HSBC_S"].iloc[-1], GBPUSD_df["Barc_S"].iloc[-1], GBPUSD_df["Jeff_S"].iloc[-1], GBPUSD_df["DB_S"].iloc[-1])
    GBPUSD_df["Min Buy"].iloc[-1] = min(GBPUSD_df["BofA_B"].iloc[-1], GBPUSD_df["HSBC_B"].iloc[-1], GBPUSD_df["Barc_B"].iloc[-1], GBPUSD_df["Jeff_B"].iloc[-1], GBPUSD_df["DB_B"].iloc[-1])
    

print(arb_count)
print(GBPUSD_df)



