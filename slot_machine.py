# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:28:20 2023

@author: Ghasemi
"""
def main():
    # Get the totalbet from the user
    while True:
        try:
            totalbet = int(input("Enter the total bet or einsatz: "))
            if totalbet <= 0:
                print("Total bet must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate the proline_total_bet (totalbet / 10)
    proline_total_bet = totalbet / 10

    print(f"Total bet: {totalbet}")
    print(f"Proline total bet: {proline_total_bet}")

    return totalbet, proline_total_bet  # Return the values as a tuple

def bet(totalbet):
    tb = totalbet
    return tb

def bett(proline_total_bet):
    ptb = proline_total_bet
    return ptb


#################################33
import pandas as pd
import random

def generate_random_reel_picture(df):
    # Get the number of rows in the DataFrame
    num_rows = len(df)

    # Check if the DataFrame has at least 4 rows
    if num_rows >= 4:
        # Generate a random start position (row index)
        start_position = random.randint(0, num_rows - 4)

        # Get the symbols for the selected reel picture (4 rows, 5 columns)
        reel_picture = df.iloc[start_position:start_position + 4, 0:5].values.tolist()

        # Compute the scatter count in the reel picture
        #scatter_count = sum(row.count(scatter_symbol) for row in reel_picture)

        # Return the reel picture as a single 2D list and scatter count
        return reel_picture
    else:
        print("The DataFrame does not have enough rows to create a reel picture.")
        return None
######################################################

def count_scatters(reel_picture):
    scatter_count = 0
    for row in reel_picture:
        scatter_count += row.count('SCA_1')
    return scatter_count

def evaluate_reel_picturee(reel_picture):
    # Calculate the total win amount
    total_wine = 0

    scatter_count = count_scatters(reel_picture)
    tb=bet(totalbet)
   
   
    if scatter_count == 5:
        total_wine = 500000*tb  # Set the payout for exactly 5 scatter symbols
    elif scatter_count == 4:
        total_wine = 5000*tb   # Set the payout for exactly 4 scatter symbols
    elif scatter_count == 3:
        total_wine = 1000*tb   # Set the payout for exactly 3 scatter symbols
    else:
        # Calculate wins based on other symbols and win models (if needed)
        for row in reel_picture:
            # Add code here to check for winning combinations based on other symbols and win models
            pass

    return total_wine

###############################################3
def define_win_models1():
    # Define the win models (list of winning combinations) and their corresponding payouts
   
    win_models1 = [
        # Model 1: Three, four, and five symbols in second row/line1
       ([(0, 1), (1, 1), (2, 1)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
       ([(0, 1), (1, 1), (2, 1),(3, 1)], {'TOP_1': { 4: 6*ptb}, 'HIG_1': { 4: 5*ptb}, 'HIG_2': { 4: 4*ptb}, 'HIG_3': { 4: 3*ptb }, 'low_1': { 4: 2*ptb },'low_2': { 4: 2*ptb },'low_3': { 4: 2*ptb },'low_4': { 4: 2*ptb }}),
       ([(0, 1), (1, 1), (2, 1),(3, 1),(4,1)], {'TOP_1': { 5: 12*ptb}, 'HIG_1': { 5: 8*ptb}, 'HIG_2': { 5: 8*ptb}, 'HIG_3': { 5: 8*ptb}, 'low_1': { 5: 3*ptb}, 'low_2': { 5: 3*ptb},'low_3': { 5: 3},'low_4': { 5: 3*ptb},'WLD_1': { 5: 78}}),
        
       ]
      

    return win_models1
def handle_wild_in_second_column1(reel_picture):
    if reel_picture[1][1] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][1] = reel_picture[1][0]
    return reel_picture

def handle_wild_in_third_column1(reel_picture):
    if reel_picture[1][2] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][2] = reel_picture[1][0]
    return reel_picture

def handle_wild_in_fourth_column1(reel_picture):
    if reel_picture[1][3] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][3] = reel_picture[1][0]
    return reel_picture
def handle_wild_in_fifth_column1(reel_picture):
    if reel_picture[1][4] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][4] = reel_picture[1][0]
    return reel_picture
def handle_wild_in_first_column1(reel_picture):
    if reel_picture[1][0] == 'WLD_1':
        i = 1
        while i < 5 and reel_picture[1][i] == 'WLD_1':
            i += 1

        if i < 5 and reel_picture[1][i] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][:i+1] = [reel_picture[1][i]] * (i+1)
    return reel_picture




def evaluate_reel_picture1(reel_picture, win_models1):
    # Check each win model and calculate the total win amount
    total_win = 0
    
    reel_picture1 =handle_wild_in_first_column1(reel_picture)
    reel_picture1  = handle_wild_in_second_column1(reel_picture)
    reel_picture1  = handle_wild_in_third_column1(reel_picture)
    reel_picture1  = handle_wild_in_fourth_column1(reel_picture)
    reel_picture1  = handle_wild_in_fifth_column1(reel_picture)
   
    
    for mode1, symbol_payouts in win_models1:
        symbols_on_mode1 = [reel_picture1[y][x] for x, y in mode1]
        if len(set(symbols_on_mode1)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode1[0]
            consecutive_count = symbols_on_mode1.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win
    

############################################################
def define_win_models2():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models2 = [
        # Model 1: Three, four, and five symbols in first row /line2
       ([(0, 0), (1, 0), (2, 0)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
       ([(0, 0), (1, 0), (2, 0),(3, 0)], {'TOP_1': { 4: 6*ptb}, 'HIG_1': { 4: 5*ptb}, 'HIG_2': { 4: 4*ptb}, 'HIG_3': { 4: 3*ptb }, 'low_1': { 4: 2*ptb },'low_2': { 4: 2*ptb },'low_3': { 4: 2*ptb },'low_4': { 4: 2*ptb }}),
       ([(0, 0), (1, 0), (2, 0),(3, 0),(4,0)], {'TOP_1': { 5: 12*ptb}, 'HIG_1': { 5: 8*ptb}, 'HIG_2': { 5: 8*ptb}, 'HIG_3': { 5: 8*ptb}, 'low_1': { 5: 3*ptb}, 'low_2': { 5: 3*ptb},'low_3': { 5: 3*ptb},'low_4': { 5: 3*ptb},'WLD_1': { 5: 78}}),
        
       ]
       

    return win_models2


def handle_wild_in_second_column2(reel_picture):
    if reel_picture[0][1] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][1] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_third_column2(reel_picture):
    if reel_picture[0][2] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][2] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_fourth_column2(reel_picture):
    if reel_picture[0][3] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][3] = reel_picture[0][0]
    return reel_picture
def handle_wild_in_fifth_column2(reel_picture):
    if reel_picture[0][4] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][4] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_first_column2(reel_picture):
    if reel_picture[0][0] == 'WLD_1':
        i = 1
        while i < 5 and reel_picture[0][i] == 'WLD_1':
            i += 1

        if i < 5 and reel_picture[0][i] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][:i+1] = [reel_picture[0][i]] * (i+1)
    return reel_picture



def evaluate_reel_picture2(reel_picture, win_models2):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture2=handle_wild_in_first_column2(reel_picture)
    reel_picture2 = handle_wild_in_second_column2(reel_picture)
    reel_picture2 = handle_wild_in_third_column2(reel_picture)
    reel_picture2 = handle_wild_in_fourth_column2(reel_picture)
    reel_picture2 = handle_wild_in_fifth_column2(reel_picture)


    for mode2, symbol_payouts in win_models2:
        symbols_on_mode2 = [reel_picture2[y][x] for x, y in mode2]
        if len(set(symbols_on_mode2)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode2[0]
            consecutive_count = symbols_on_mode2.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win
################################
def define_win_models3():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models3 = [
        # Model 1: Three, four, and five symbols in third row /line 3
       ([(0, 2), (1, 2), (2, 2)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
       ([(0, 2), (1, 2), (2, 2),(3, 2)], {'TOP_1': { 4: 6*ptb}, 'HIG_1': { 4: 5*ptb}, 'HIG_2': { 4: 4*ptb}, 'HIG_3': { 4: 3*ptb }, 'low_1': { 4: 2*ptb },'low_2': { 4: 2*ptb },'low_3': { 4: 2*ptb },'low_4': { 4: 2*ptb }}),
       ([(0, 2), (1, 2), (2, 2),(3, 2),(4,2)], {'TOP_1': { 5: 12*ptb}, 'HIG_1': { 5: 8*ptb}, 'HIG_2': { 5: 8*ptb}, 'HIG_3': { 5: 8*ptb}, 'low_1': { 5: 3*ptb}, 'low_2': { 5: 3*ptb},'low_3': { 5: 3*ptb},'low_4': { 5: 3*ptb},'WLD_1': { 5: 78}}),
        
       ]
       

    return win_models3
def handle_wild_in_second_column3(reel_picture):
    if reel_picture[2][1] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][1] = reel_picture[2][0]
    return reel_picture

def handle_wild_in_third_column3(reel_picture):
    if reel_picture[2][2] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][2] = reel_picture[2][0]
    return reel_picture

def handle_wild_in_fourth_column3(reel_picture):
    if reel_picture[2][3] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][3] = reel_picture[2][0]
    return reel_picture
def handle_wild_in_fifth_column3(reel_picture):
    if reel_picture[2][4] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][4] = reel_picture[2][0]
    return reel_picture
def handle_wild_in_firth_column3(reel_picture):
    if reel_picture[2][0] == 'WLD_1':
        i = 1
        while i < 5 and reel_picture[2][i] == 'WLD_1':
            i += 1

        if i < 5 and reel_picture[2][i] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][:i+1] = [reel_picture[2][i]] * (i+1)
    return reel_picture




def evaluate_reel_picture3(reel_picture, win_models3):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture3=handle_wild_in_firth_column3(reel_picture)
    reel_picture3 = handle_wild_in_second_column3(reel_picture)
    reel_picture3 = handle_wild_in_third_column3(reel_picture)
    reel_picture3 = handle_wild_in_fourth_column3(reel_picture)
    reel_picture3 = handle_wild_in_fifth_column3(reel_picture)
    for mode3, symbol_payouts in win_models3:
        symbols_on_mode3 = [reel_picture3[y][x] for x, y in mode3]
        if len(set(symbols_on_mode3)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode3[0]
            consecutive_count = symbols_on_mode3.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win

#########################
def define_win_models4():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models4 = [
        # Model 1: Three, four, and five symbols in forth / line 4
       ([(0, 3), (1, 3), (2, 3)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
       ([(0, 3), (1, 3), (2, 3),(3, 3)], {'TOP_1': { 4: 6*ptb}, 'HIG_1': { 4: 5*ptb}, 'HIG_2': { 4: 4*ptb}, 'HIG_3': { 4: 3*ptb }, 'low_1': { 4: 2*ptb },'low_2': { 4: 2*ptb },'low_3': { 4: 2*ptb },'low_4': { 4: 2*ptb }}),
       ([(0, 3), (1, 3), (2, 3),(3, 3),(4,3)], {'TOP_1': { 5: 12*ptb}, 'HIG_1': { 5: 8*ptb}, 'HIG_2': { 5: 8*ptb}, 'HIG_3': { 5: 8*ptb}, 'low_1': { 5: 3*ptb}, 'low_2': { 5: 3*ptb},'low_3': { 5: 3*ptb},'low_4': { 5: 3*ptb},'WLD_1': { 5: 78}}),
        
       ]
       

    return win_models4
def handle_wild_in_second_column4(reel_picture):
    if reel_picture[3][1] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][1] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_third_column4(reel_picture):
    if reel_picture[3][2] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][2] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_fourth_column4(reel_picture):
    if reel_picture[3][3] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][3] = reel_picture[3][0]
    return reel_picture
def handle_wild_in_fifth_column4(reel_picture):
    if reel_picture[3][4] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][4] = reel_picture[3][0]
    return reel_picture
def handle_wild_in_fourth_row4(reel_picture):
    if reel_picture[3][0] == 'WLD_1':
        i = 1
        while i < 5 and reel_picture[3][i] == 'WLD_1':
            i += 1

        if i < 5 and reel_picture[3][i] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][:i+1] = [reel_picture[3][i]] * (i+1)
    return reel_picture







def evaluate_reel_picture4(reel_picture, win_models4):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture4 =handle_wild_in_fourth_row4(reel_picture)
    reel_picture4 = handle_wild_in_second_column4(reel_picture)
    reel_picture4 = handle_wild_in_third_column4(reel_picture)
    reel_picture4= handle_wild_in_fourth_column4(reel_picture)
    reel_picture4= handle_wild_in_fifth_column4(reel_picture)


    for mode4, symbol_payouts in win_models4:
        symbols_on_mode4 = [reel_picture4[y][x] for x, y in mode4]
        if len(set(symbols_on_mode4)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode4[0]
            consecutive_count = symbols_on_mode4.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win
#####################################
def define_win_models5():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models5 = [
        # Model 1: line5
        ([(0, 3), (1, 2), (2, 1)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
        ([(0, 3), (1, 2), (2, 1),(3, 2)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb }, 'low_1': {4: 2*ptb }, 'low_2': {4: 2*ptb},'low_3': {4: 2*ptb},'low_4': {4: 2*ptb}}),
        ([(0, 3), (1, 2), (2, 1),(3, 2),(4, 3)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb }, 'low_1': {5: 3*ptb }, 'low_2': {5: 3*ptb},'low_3': {5: 3*ptb},'WLD_1': {5: 78}}),
        
       ]
       

    return win_models5
def handle_wild_in_second_column5(reel_picture):
    if reel_picture[2][1] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][1] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_third_column5(reel_picture):
    if reel_picture[1][2] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][2] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_fourth_column5(reel_picture):
    if reel_picture[2][3] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][3] = reel_picture[3][0]
    return reel_picture
def handle_wild_in_fifth_column5(reel_picture):
    if reel_picture[3][4] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][4] = reel_picture[3][0]
    return reel_picture
def handle_wild_in_first_column5(reel_picture):
    if reel_picture[3][0] == 'WLD_1':
        if reel_picture[2][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[2][1]
        elif reel_picture[1][2] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[2][1] = reel_picture[1][2]
        elif reel_picture[2][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[2][1] = reel_picture[1][2] = reel_picture[2][3]
        elif reel_picture[3][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[2][1] = reel_picture[1][2] = reel_picture[2][3] = reel_picture[3][4]
    return reel_picture 



def evaluate_reel_picture5(reel_picture, win_models5):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture
    reel_picture5 = handle_wild_in_first_column5(reel_picture)
    reel_picture5 = handle_wild_in_second_column5(reel_picture)
    reel_picture5 = handle_wild_in_third_column5(reel_picture)
    reel_picture5 = handle_wild_in_fourth_column5(reel_picture)
    reel_picture5 = handle_wild_in_fifth_column5(reel_picture)


    for mode5, symbol_payouts in win_models5:
        symbols_on_mode5 = [reel_picture5[y][x] for x, y in mode5]
        if len(set(symbols_on_mode5)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode5[0]
            consecutive_count = symbols_on_mode5.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win
########################################################
    
def define_win_models6():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models6 = [
        # Model 1: line6
        ([(0, 0), (1, 1), (2, 2)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
        ([(0, 0), (1, 1), (2, 2),(3, 1)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb }, 'low_1': {4: 2*ptb }, 'low_2': {4: 2*ptb},'low_3': {4: 2*ptb},'low_4': {4: 2*ptb}}),
        ([(0, 0), (1, 1), (2, 2),(3, 1),(4, 0)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb }, 'low_1': {5: 3*ptb }, 'low_2': {5: 3*ptb},'low_3': {5: 3*ptb},'low_4': {5: 3*ptb},'WLD_1': {5: 78}}),
        
       ]
       

    return win_models6

def handle_wild_in_second_column6(reel_picture):
    if reel_picture[1][1] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][1] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_third_column6(reel_picture):
    if reel_picture[2][2] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][2] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_fourth_column6(reel_picture):
    if reel_picture[1][3] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][3] = reel_picture[0][0]
    return reel_picture
def handle_wild_in_fifth_column6(reel_picture):
    if reel_picture[0][4] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][4] = reel_picture[0][0]
    return reel_picture
def handle_wild_in_first_column6(reel_picture):
    if reel_picture[0][0] == 'WLD_1':
        if reel_picture[1][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[1][1]
        elif reel_picture[2][2] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[1][1] = reel_picture[2][2]
        elif reel_picture[1][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[1][1] = reel_picture[2][2] = reel_picture[1][3]
        elif reel_picture[0][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[1][1] = reel_picture[2][2] = reel_picture[1][3] = reel_picture[0][4]
    return reel_picture 


def evaluate_reel_picture6(reel_picture, win_models6):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture6 =  handle_wild_in_first_column6(reel_picture)
    reel_picture6 = handle_wild_in_second_column6(reel_picture)
    reel_picture6 = handle_wild_in_third_column6(reel_picture)
    reel_picture6= handle_wild_in_fourth_column6(reel_picture)
    reel_picture6 = handle_wild_in_fifth_column6(reel_picture)


    for mode6, symbol_payouts in win_models6:
        symbols_on_mode6 = [reel_picture6[y][x] for x, y in mode6]
        if len(set(symbols_on_mode6)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode6[0]
            consecutive_count = symbols_on_mode6.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win



#######################################
def define_win_models7():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models7 = [
        # Model 1:  line7 
        ([(0, 3), (1, 3), (2, 0)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb}, 'low_1': {3: 1*ptb}, 'low_2': {3: 1*ptb}, 'low_3': {3: 1*ptb}, 'low_4': {3: 1*ptb}}),
        ([(0, 3), (1, 3), (2, 0), (3, 3)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb}, 'low_1': {4: 2*ptb}, 'low_2': {4: 2*ptb}, 'low_3': {4: 2*ptb}, 'low_4': {4: 2*ptb}}),
        ([(0, 3), (1, 3), (2, 0), (3, 3), (4, 3)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb}, 'low_1': {5: 3*ptb}, 'low_2': {5: 3*ptb}, 'low_3': {5: 3*ptb}, 'low_4': {5: 3*ptb},'WLD_1': {5: 78}}),
    ]
    return win_models7

def handle_wild_in_second_column7(reel_picture):
    if reel_picture[3][1] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][1] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_third_column7(reel_picture):
    if reel_picture[0][2] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][2] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_fourth_column7(reel_picture):
    if reel_picture[3][3] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][3] = reel_picture[3][0]
    return reel_picture
def handle_wild_in_fifth_column7(reel_picture):
    if reel_picture[3][4] == 'WLD_1':
        if reel_picture[3][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][4] = reel_picture[3][0]
    return reel_picture

def handle_wild_in_first_column7(reel_picture):
    if reel_picture[3][0] == 'WLD_1':
        if reel_picture[3][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[3][1]
        elif reel_picture[0][2] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[3][1] = reel_picture[0][2]
        elif reel_picture[3][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[3][1] = reel_picture[0][2] = reel_picture[3][3]
        elif reel_picture[3][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][0] = reel_picture[3][1] = reel_picture[0][2] = reel_picture[3][3] = reel_picture[3][4]
    return reel_picture 




def evaluate_reel_picture7(reel_picture, win_models7):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture7 = handle_wild_in_first_column7(reel_picture)
    reel_picture7 = handle_wild_in_second_column7(reel_picture)
    reel_picture7= handle_wild_in_third_column7(reel_picture)
    reel_picture7 = handle_wild_in_fourth_column7(reel_picture)
    reel_picture7= handle_wild_in_fifth_column7(reel_picture)
    
    
    for mode7, symbol_payouts in win_models7:
        symbols_on_mode7 = [reel_picture7[y][x] for x, y in mode7]
        if len(set(symbols_on_mode7)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode7[0]
            consecutive_count = symbols_on_mode7.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win= payout

    return total_win  
#######################################
def define_win_models8():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models8 = [
        # Model 1:   line 8
        ([(0, 0), (1, 0), (2, 3)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
        ([(0, 0), (1, 0), (2, 3),(3, 0)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb }, 'low_1': {4: 2*ptb }, 'low_2': {4: 2*ptb},'low_3': {4: 2*ptb},'low_4': {4: 2*ptb}}),
        ([(0, 0), (1, 0), (2, 3),(3, 0),(4, 0)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb }, 'low_1': {5: 3*ptb }, 'low_2': {5: 3*ptb},'low_3': {5: 3*ptb},'low_4': {5: 3*ptb},'WLD_1': {5: 78}}),
        
       ]
       

    return win_models8
def handle_wild_in_second_column8(reel_picture):
    if reel_picture[0][1] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][1] = reel_picture[0][0]
    return reel_picture
def handle_wild_in_third_column8(reel_picture):
    if reel_picture[3][2] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[3][2] = reel_picture[0][0]
    return reel_picture

def handle_wild_in_fourth_column8(reel_picture):
    if reel_picture[0][3] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][3] = reel_picture[0][0]
    return reel_picture
def handle_wild_in_fifth_column8(reel_picture):
    if reel_picture[0][4] == 'WLD_1':
        if reel_picture[0][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][4] = reel_picture[0][0]

    return reel_picture

def handle_wild_in_first_column8(reel_picture):
    if reel_picture[0][0] == 'WLD_1':
        if reel_picture[0][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[0][1]
        elif reel_picture[3][2] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[0][1] = reel_picture[3][2]
        elif reel_picture[0][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[0][1] = reel_picture[3][2] = reel_picture[0][3]
        elif reel_picture[0][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[0][0] = reel_picture[0][1] = reel_picture[3][2] = reel_picture[0][3] = reel_picture[0][4]
    return reel_picture 





def evaluate_reel_picture8(reel_picture, win_models8):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture8=handle_wild_in_first_column8(reel_picture)
    reel_picture8=handle_wild_in_second_column8(reel_picture)
    reel_picture8=handle_wild_in_third_column8(reel_picture)
    reel_picture8=handle_wild_in_fourth_column8(reel_picture)
    reel_picture8=handle_wild_in_fifth_column8(reel_picture)
    
   
    
    for mode8, symbol_payouts in win_models8:
        symbols_on_mode8 = [reel_picture8[y][x] for x, y in mode8]
        if len(set(symbols_on_mode8)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode8[0]
            consecutive_count = symbols_on_mode8.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win


#############################
def define_win_models9():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models9 = [
        # Model 1: line 9
        ([(0, 2), (1, 1), (2, 2)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
        ([(0, 2), (1, 1), (2, 2),(3, 1)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb }, 'low_1': {4: 2*ptb }, 'low_2': {4: 2*ptb},'low_3': {4: 2*ptb},'low_4': {4: 2*ptb}}),
        ([(0, 2), (1, 1), (2, 2),(3, 1),(4, 2)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb }, 'low_1': {5: 3*ptb}, 'low_2': {5: 3*ptb},'low_3': {5: 3*ptb},'WLD_1': {5: 78}}),
        
       ]
       

    return win_models9
def handle_wild_in_second_column9(reel_picture):
    if reel_picture[1][1] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][1] = reel_picture[2][0]
    return reel_picture

def handle_wild_in_third_column9(reel_picture):
    if reel_picture[2][2] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][2] = reel_picture[2][0]
    return reel_picture

def handle_wild_in_fourth_column9(reel_picture):
    if reel_picture[1][3] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][3] = reel_picture[2][0]
    return reel_picture
def handle_wild_in_fifth_column9(reel_picture):
    if reel_picture[2][4] == 'WLD_1':
        if reel_picture[2][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][4] = reel_picture[2][0]

    return reel_picture
def handle_wild_in_first_column9(reel_picture):
    if reel_picture[2][0] == 'WLD_1':
        if reel_picture[1][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][0] = reel_picture[1][1]
        elif reel_picture[2][2] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][0] = reel_picture[1][1] = reel_picture[2][2]
        elif reel_picture[1][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][0] = reel_picture[1][1] = reel_picture[2][2] = reel_picture[1][3]
        elif reel_picture[2][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][0] = reel_picture[1][1] = reel_picture[2][2] = reel_picture[1][3] = reel_picture[2][4]
    return reel_picture 





def evaluate_reel_picture9(reel_picture, win_models9):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture9 =handle_wild_in_first_column9(reel_picture)
    reel_picture9 = handle_wild_in_second_column9(reel_picture)
    reel_picture9 = handle_wild_in_third_column9(reel_picture)
    reel_picture9 = handle_wild_in_fourth_column9(reel_picture)
    reel_picture9 = handle_wild_in_fifth_column9(reel_picture)

    

    for mode9, symbol_payouts in win_models9:
        symbols_on_mode9 = [reel_picture9[y][x] for x, y in mode9]
        if len(set(symbols_on_mode9)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode9[0]
            consecutive_count = symbols_on_mode9.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win
########################################
def define_win_models10():
    # Define the win models (list of winning combinations) and their corresponding payouts
    win_models10 = [
        # Model 1:  line 10
        ([(0, 1), (1, 2), (2, 1)], {'TOP_1': {3: 3*ptb}, 'HIG_1': {3: 2*ptb}, 'HIG_2': {3: 2*ptb}, 'HIG_3': {3: 1*ptb }, 'low_1': {3: 1*ptb }, 'low_2': {3: 1*ptb},'low_3': {3: 1*ptb},'low_4': {3: 1*ptb}}),
        ([(0, 1), (1, 2), (2, 1),(3, 2)], {'TOP_1': {4: 6*ptb}, 'HIG_1': {4: 5*ptb}, 'HIG_2': {4: 4*ptb}, 'HIG_3': {4: 3*ptb }, 'low_1': {4: 2*ptb }, 'low_2': {4: 2*ptb},'low_3': {4: 2*ptb},'low_4': {4: 2*ptb}}),
        ([(0, 1), (1, 2), (2, 1),(3, 2),(4, 1)], {'TOP_1': {5: 12*ptb}, 'HIG_1': {5: 8*ptb}, 'HIG_2': {5: 8*ptb}, 'HIG_3': {5: 8*ptb }, 'low_1': {5: 3*ptb }, 'low_2': {5: 3*ptb},'low_3': {5: 3*ptb},'WLD_1': {5: 78},}),
        
       ]
       

    return win_models10
def handle_wild_in_second_column10(reel_picture):
    if reel_picture[2][1] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][1] = reel_picture[1][0]
    return reel_picture

def handle_wild_in_third_column10(reel_picture):
    if reel_picture[1][2] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][2] = reel_picture[1][0]
    return reel_picture

def handle_wild_in_fourth_column10(reel_picture):
    if reel_picture[2][3] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[2][3] = reel_picture[1][0]
    return reel_picture
def handle_wild_in_fifth_column10(reel_picture):
    if reel_picture[1][4] == 'WLD_1':
        if reel_picture[1][0] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][4] = reel_picture[1][0]

    return reel_picture
def handle_wild_in_first_column10(reel_picture):
    if reel_picture[1][0] == 'WLD_1':
        if reel_picture[2][1] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][0] = reel_picture[2][1]
        elif reel_picture[1][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][0] = reel_picture[2][1] = reel_picture[1][3]
        elif reel_picture[2][3] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][0] = reel_picture[2][1] = reel_picture[1][3] = reel_picture[2][3]
        elif reel_picture[1][4] not in ['WLD_1', 'SCA_1']:
            reel_picture[1][0] = reel_picture[2][1] = reel_picture[1][3] = reel_picture[2][3] = reel_picture[1][4]
    return reel_picture 



def evaluate_reel_picture10(reel_picture, win_models10):
    # Check each win model and calculate the total win amount
    total_win = 0
    reel_picture10 =handle_wild_in_first_column10(reel_picture)
    reel_picture10 = handle_wild_in_second_column10(reel_picture)
    reel_picture10 = handle_wild_in_third_column10(reel_picture)
    reel_picture10 = handle_wild_in_fourth_column10(reel_picture)
    reel_picture10= handle_wild_in_fifth_column10(reel_picture)

    for mode10, symbol_payouts in win_models10:
        symbols_on_mode10 = [reel_picture10[y][x] for x, y in mode10]
        if len(set(symbols_on_mode10)) == 1:
            # All symbols on the model are the same (winning combination)
            symbol = symbols_on_mode10[0]
            consecutive_count = symbols_on_mode10.count(symbol)
            if symbol in symbol_payouts and consecutive_count >= 3:
                # Calculate the win amount based on the number of consecutive symbols
                payout = symbol_payouts[symbol][consecutive_count]
                total_win  =  payout

    return total_win

###############Run codes


def evaluate_total_win(reel_picture):
    win_models1 = define_win_models1()
    win_models2 = define_win_models2()
    win_models3 = define_win_models3()
    win_models4 = define_win_models4()
    win_models5 = define_win_models5()
    win_models6 = define_win_models6()
    win_models7 = define_win_models7() 
    win_models8 = define_win_models8()
    win_models9 = define_win_models9()      
    win_models10 = define_win_models10()

    # Make copies of the original reel picture
    reel_picture_copy1 = [row[:] for row in reel_picture]
    reel_picture_copy2 = [row[:] for row in reel_picture]
    reel_picture_copy3 = [row[:] for row in reel_picture]
    reel_picture_copy4 = [row[:] for row in reel_picture]
    reel_picture_copy5 = [row[:] for row in reel_picture]
    reel_picture_copy6 = [row[:] for row in reel_picture]
    reel_picture_copy7 = [row[:] for row in reel_picture]
    reel_picture_copy8 = [row[:] for row in reel_picture]
    reel_picture_copy9 = [row[:] for row in reel_picture]
    reel_picture_copy10 = [row[:] for row in reel_picture]
    reel_picture_copy11= [row[:] for row in reel_picture]

    total_win_amount1 = evaluate_reel_picture1(reel_picture_copy1, win_models1)
    total_win_amount2 = evaluate_reel_picture2(reel_picture_copy2, win_models2)
    total_win_amount3 = evaluate_reel_picture3(reel_picture_copy3, win_models3)
    total_win_amount4 = evaluate_reel_picture4(reel_picture_copy4, win_models4)
    total_win_amount5 = evaluate_reel_picture5(reel_picture_copy5, win_models5)
    total_win_amount6 = evaluate_reel_picture6(reel_picture_copy6, win_models6)  
    total_win_amount7 = evaluate_reel_picture7(reel_picture_copy7, win_models7)
    total_win_amount8 = evaluate_reel_picture8(reel_picture_copy8, win_models8)
    total_win_amount9 = evaluate_reel_picture9(reel_picture_copy9, win_models9)
    total_win_amount10 = evaluate_reel_picture10(reel_picture_copy10, win_models10)
    win_amount =evaluate_reel_picturee(reel_picture_copy11)
    return total_win_amount1 + total_win_amount2+total_win_amount3+total_win_amount4+total_win_amount5+total_win_amount6+total_win_amount7+total_win_amount8+total_win_amount9+total_win_amount10+win_amount 


def simulate_10_spins():
    spins_data = []

    for _ in range(10):
        df = pd.read_excel("E:\Sarvenaz\python workeshop\sample.Xlsx", sheet_name="Sheet2")
        reel_picture = generate_random_reel_picture(df)
        total_win = evaluate_total_win(reel_picture)
        spins_data.append((reel_picture, total_win))

    return spins_data
###############################
totalbet, proline_total_bet = main()
tb = bet(totalbet)  # Call the function and assign the returned value to tb
ptb = bett(proline_total_bet)
spins_data = simulate_10_spins()
first_spin_reel_picture, first_spin_total_win = spins_data[0]
# Access the win amounts for all 10 spins and see 10 reel picture
for index, (reel_picture, total_win) in enumerate(spins_data, 1):
    print(f"Spin {index}: Reel Picture = {reel_picture}, Total win amount = {total_win}")





