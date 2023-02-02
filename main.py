# Import each python file as modules
import cash_on_hand, overheads, profit_loss

def main():
    """
    - This function will execute the functions in each python file.
    - No parameter is required
    """
    # call the functions from the imported modules
    overheads.overheads_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()

# execute the main function
main()